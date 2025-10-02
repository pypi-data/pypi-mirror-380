"""
DataGuild Snowflake Lineage Extractor v2.

This module provides comprehensive lineage extraction from Snowflake including:
1. External lineage (S3 to Table via COPY operations)
2. Table-to-Table and View-to-Table lineage via access_history
3. Column-level lineage tracking and analysis
4. Time-based lineage extraction with redundant run handling
"""

import json
import logging
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Collection, Iterable, List, Optional, Set, Tuple, Type

from pydantic import BaseModel, Field, validator

from dataguild.configuration.datetimes import parse_absolute_time
from dataguild.api.closeable import Closeable
from dataguild.source.aws.s3_util import make_s3_urn_for_lineage
from dataguild.source.snowflake.constants import (
    LINEAGE_PERMISSION_ERROR,
    SnowflakeEdition,
)
from dataguild.source.snowflake.config import SnowflakeV2Config
from dataguild.source.snowflake.connection import (
    SnowflakeConnection,
    SnowflakePermissionError,
)
from dataguild.source.snowflake.query import SnowflakeQuery
from dataguild.source.snowflake.report import SnowflakeV2Report
from dataguild.source.snowflake.utils import (
    SnowflakeCommonMixin,
    SnowflakeFilter,
    SnowflakeIdentifierBuilder,
)
from dataguild.source.state.redundant_run_skip_handler import (
    RedundantLineageRunSkipHandler,
)
from dataguild.metadata.schema_classes import DatasetLineageTypeClass, UpstreamClass
from dataguild.metadata.urns import CorpUserUrn
from dataguild.sql_parsing.sql_parsing_aggregator import (
    KnownLineageMapping,
    KnownQueryLineageInfo,
    SqlParsingAggregator,
    UrnStr,
)
from dataguild.source.snowflake.stored_proc_lineage import (
    StoredProcCall,
    StoredProcLineageTracker,
)
from dataguild.sql_parsing.sqlglot_lineage import (
    ColumnLineageInfo,
    ColumnRef,
    DownstreamColumnRef,
)
from dataguild.sql_parsing.sqlglot_utils import get_query_fingerprint
from dataguild.utilities.perf_timer import PerfTimer
from dataguild.utilities.time import ts_millis_to_datetime

logger: logging.Logger = logging.getLogger(__name__)

# Constants for lineage types
EXTERNAL_LINEAGE = "external_lineage"
TABLE_LINEAGE = "table_lineage"
VIEW_LINEAGE = "view_lineage"


def pydantic_parse_json(field: str) -> classmethod:
    """
    Create a Pydantic validator for parsing JSON fields.

    Args:
        field: Field name to create validator for

    Returns:
        Pydantic validator function
    """
    def _parse_from_json(cls: Type, v: Any) -> dict:
        if isinstance(v, str):
            return json.loads(v)
        return v

    return validator(field, pre=True, allow_reuse=True)(_parse_from_json)


class UpstreamColumnNode(BaseModel):
    """Represents an upstream column reference in lineage."""

    object_name: str
    object_domain: str
    column_name: str


class ColumnUpstreamJob(BaseModel):
    """Represents a set of column upstreams for a specific query."""

    column_upstreams: List[UpstreamColumnNode]
    query_id: str


class ColumnUpstreamLineage(BaseModel):
    """Represents column-level lineage information."""

    column_name: Optional[str] = None
    upstreams: List[ColumnUpstreamJob] = Field(default_factory=list)


class UpstreamTableNode(BaseModel):
    """Represents an upstream table in lineage."""

    upstream_object_domain: str
    upstream_object_name: str
    query_id: str


class Query(BaseModel):
    """Represents a SQL query with metadata."""

    query_id: str
    query_text: str
    start_time: str


class UpstreamLineageEdge(BaseModel):
    """
    Represents a complete lineage edge with upstream and downstream information.

    This model handles JSON parsing for complex nested structures returned
    from Snowflake's access_history queries.
    """

    DOWNSTREAM_TABLE_NAME: str
    DOWNSTREAM_TABLE_DOMAIN: str
    UPSTREAM_TABLES: Optional[List[UpstreamTableNode]] = None
    UPSTREAM_COLUMNS: Optional[List[ColumnUpstreamLineage]] = None
    QUERIES: Optional[List[Query]] = None

    # JSON parsing validators for complex fields
    _json_upstream_tables = pydantic_parse_json("UPSTREAM_TABLES")
    _json_upstream_columns = pydantic_parse_json("UPSTREAM_COLUMNS")
    _json_queries = pydantic_parse_json("QUERIES")


@dataclass(frozen=True)
class SnowflakeColumnId:
    """
    Immutable identifier for a Snowflake column.

    Used for tracking column-level lineage relationships
    across different tables and views.
    """

    column_name: str
    object_name: str
    object_domain: Optional[str] = None


class SnowflakeLineageExtractor(SnowflakeCommonMixin, Closeable):
    """
    Extracts comprehensive lineage information from Snowflake.

    This extractor handles multiple types of lineage relationships:
    1. "Table to View" lineage via object_dependencies view + View definition SQL parsing
    2. "S3 to Table" lineage via external tables and copy_history view
    3. "View to Table" and "Table to Table" lineage via access_history view

    Edition Note: Snowflake Standard Edition does not have Access History Feature,
    so it does not support lineage extraction for access_history-based edges.

    Examples:
        >>> extractor = SnowflakeLineageExtractor(
        ...     config=config,
        ...     report=report,
        ...     connection=connection,
        ...     filters=filters,
        ...     identifiers=identifiers,
        ...     redundant_run_skip_handler=handler,
        ...     sql_aggregator=aggregator
        ... )
        >>> extractor.add_time_based_lineage_to_aggregator(
        ...     discovered_tables=tables,
        ...     discovered_views=views
        ... )
    """

    def __init__(
        self,
        config: SnowflakeV2Config,
        report: SnowflakeV2Report,
        connection: SnowflakeConnection,
        filters: SnowflakeFilter,
        identifiers: SnowflakeIdentifierBuilder,
        redundant_run_skip_handler: Optional[RedundantLineageRunSkipHandler],
        sql_aggregator: SqlParsingAggregator,
    ) -> None:
        """
        Initialize the Snowflake lineage extractor.

        Args:
            config: Snowflake configuration with lineage settings
            report: Report object for tracking extraction progress
            connection: Active Snowflake connection
            filters: Filters for datasets and objects
            identifiers: Builder for generating URNs and identifiers
            redundant_run_skip_handler: Handler for avoiding redundant runs
            sql_aggregator: Aggregator for processing SQL and lineage
        """
        self.config = config
        self.report = report
        self.connection = connection
        self.filters = filters
        self.identifiers = identifiers
        self.redundant_run_skip_handler = redundant_run_skip_handler
        self.sql_aggregator = sql_aggregator

        # Initialize stored procedure lineage tracker
        self.stored_proc_tracker = StoredProcLineageTracker(
            platform="snowflake",
            shared_connection=connection
        )

        # Get time window for lineage extraction
        self.start_time, self.end_time = (
            self.report.lineage_start_time,
            self.report.lineage_end_time,
        ) = self.get_time_window()

        logger.info(
            f"Initialized SnowflakeLineageExtractor for time window: "
            f"{self.start_time} to {self.end_time}"
        )

    def get_time_window(self) -> Tuple[datetime, datetime]:
        """
        Determine the time window for lineage extraction.

        Uses redundant run skip handler to suggest optimal time windows
        if available, otherwise uses configuration defaults.

        Returns:
            Tuple of (start_time, end_time) for lineage extraction
        """
        if self.redundant_run_skip_handler:
            return self.redundant_run_skip_handler.suggest_run_time_window(
                (
                    self.config.start_time
                    if not self.config.ignore_start_time_lineage
                    else ts_millis_to_datetime(0)
                ),
                self.config.end_time,
            )
        else:
            return (
                (
                    self.config.start_time
                    if not self.config.ignore_start_time_lineage
                    else ts_millis_to_datetime(0)
                ),
                self.config.end_time,
            )

    def add_time_based_lineage_to_aggregator(
        self,
        discovered_tables: List[str],
        discovered_views: List[str],
    ) -> None:
        """
        Main entry point for adding time-based lineage to the SQL aggregator.

        This method orchestrates the extraction of both external and internal
        lineage relationships within the configured time window.

        Args:
            discovered_tables: List of discovered table identifiers
            discovered_views: List of discovered view identifiers
        """
        if not self._should_ingest_lineage():
            logger.info("Skipping lineage ingestion based on redundant run handler")
            return

        logger.info("Starting time-based lineage extraction")

        # Extract S3 dataset -> Snowflake table lineage
        self._populate_external_upstreams(discovered_tables)

        # Extract Snowflake view/table -> Snowflake table lineage
        self.populate_table_upstreams(discovered_tables)

        # Extract stored procedure lineage
        self._process_stored_proc_lineage(discovered_tables)

        logger.info("Completed time-based lineage extraction")

    def update_state(self):
        """
        Update the state for redundant run handling.

        This should be called after successful lineage extraction
        to mark the current time window as processed.
        """
        if self.redundant_run_skip_handler:
            # Update the checkpoint state for this run
            self.redundant_run_skip_handler.update_state(
                (
                    self.config.start_time
                    if not self.config.ignore_start_time_lineage
                    else ts_millis_to_datetime(0)
                ),
                self.config.end_time,
            )
            logger.info("Updated redundant run skip handler state")

    def populate_table_upstreams(self, discovered_tables: List[str]) -> None:
        """
        Populate table-to-table lineage from Snowflake's access_history.

        This method extracts lineage relationships between Snowflake objects
        using the access_history view, which requires Enterprise Edition or above.

        Args:
            discovered_tables: List of discovered table identifiers
        """
        if self.report.edition == SnowflakeEdition.STANDARD:
            logger.info(
                "Snowflake Account is Standard Edition. Table to Table and View to Table "
                "Lineage Feature is not supported."
            )
            # TODO: use sql_aggregator.add_observed_query to report queries from
            # snowflake.account_usage.query_history and let DataGuild generate lineage, usage and operations
            return

        logger.info("Extracting table-to-table lineage from access_history")

        with PerfTimer() as timer:
                results = self._fetch_upstream_lineages_for_tables()
            
        if not results:
            logger.warning("No upstream lineage results found")
            return

        self.populate_known_query_lineage(discovered_tables, results)
        self.report.table_lineage_query_secs = timer.elapsed_seconds()

        logger.info(
            f"Upstream lineage detected for {self.report.num_tables_with_known_upstreams} tables. "
            f"Processing took {self.report.table_lineage_query_secs:.2f} seconds."
        )

    def populate_known_query_lineage(
        self,
        discovered_assets: Collection[str],
        results: Iterable[UpstreamLineageEdge],
    ) -> None:
        """
        Process upstream lineage results and add them to the SQL aggregator.

        Args:
            discovered_assets: Collection of discovered asset identifiers
            results: Iterable of upstream lineage edges from Snowflake
        """
        processed_count = 0

        for db_row in results:
            try:
                dataset_name = self.identifiers.get_dataset_identifier_from_qualified_name(
                    db_row.DOWNSTREAM_TABLE_NAME
                )

                # Skip if dataset not discovered or no queries available
                if dataset_name not in discovered_assets or not db_row.QUERIES:
                    continue

                # Process each query in the lineage edge
                for query in db_row.QUERIES:
                    known_lineage = self.get_known_query_lineage(
                        query, dataset_name, db_row
                    )

                    if known_lineage and known_lineage.upstreams:
                        self.report.num_tables_with_known_upstreams += 1
                        self.sql_aggregator.add_known_query_lineage(known_lineage, True)
                        processed_count += 1

                        logger.debug(
                            f"Added lineage for {dataset_name}: "
                            f"{len(known_lineage.upstreams)} upstreams"
                        )
                    else:
                        logger.debug(f"No lineage found for {dataset_name}")

            except Exception as e:
                logger.error(f"Error processing lineage edge: {e}", exc_info=True)
                continue

        logger.info(f"Processed {processed_count} known query lineage entries")

    def get_known_query_lineage(
        self, query: Query, dataset_name: str, db_row: UpstreamLineageEdge
    ) -> Optional[KnownQueryLineageInfo]:
        """
        Convert a query and lineage edge into a KnownQueryLineageInfo object.

        Args:
            query: Query information from Snowflake
            dataset_name: Downstream dataset identifier
            db_row: Upstream lineage edge data

        Returns:
            KnownQueryLineageInfo object or None if no upstreams
        """
        if not db_row.UPSTREAM_TABLES:
            return None

        try:
            downstream_table_urn = self.identifiers.gen_dataset_urn(dataset_name)

            known_lineage = KnownQueryLineageInfo(
                query_id=get_query_fingerprint(
                    query.query_text, self.identifiers.platform, fast=True
                ),
                query_text=query.query_text,
                downstream=downstream_table_urn,
                upstreams=self.map_query_result_upstreams(
                    db_row.UPSTREAM_TABLES, query.query_id
                ),
                column_lineage=(
                    self.map_query_result_fine_upstreams(
                        downstream_table_urn,
                        db_row.UPSTREAM_COLUMNS,
                        query.query_id,
                    )
                    if (self.config.include_column_lineage and db_row.UPSTREAM_COLUMNS)
                    else None
                ),
                timestamp=parse_absolute_time(query.start_time),
            )

            return known_lineage

        except Exception as e:
            logger.error(f"Error creating known query lineage: {e}")
            return None

    def _populate_external_upstreams(self, discovered_tables: List[str]) -> None:
        """
        Populate external lineage from S3 and other external sources.

        This method extracts lineage from COPY operations that load data
        from external sources like S3 into Snowflake tables.

        Args:
            discovered_tables: List of discovered table identifiers
        """
        logger.info("Extracting external lineage from copy history")

        with PerfTimer() as timer:
            self.report.num_external_table_edges_scanned = 0

            for entry in self._get_copy_history_lineage(discovered_tables):
                self.sql_aggregator.add(entry)

            self.report.external_lineage_queries_secs = timer.elapsed_seconds()

        logger.info(
            f"External lineage extraction completed. "
            f"Scanned {self.report.num_external_table_edges_scanned} edges in "
            f"{self.report.external_lineage_queries_secs:.2f} seconds."
        )

    def _get_copy_history_lineage(
        self, discovered_tables: List[str]
    ) -> Iterable[KnownLineageMapping]:
        """
        Extract lineage from Snowflake's copy_history view.

        Handles cases where tables are populated from external stages/S3 locations via COPY.
        Examples:
        - COPY INTO category_english FROM @external_s3_stage;
        - COPY INTO category_english FROM 's3://bucket/path/' CREDENTIALS=(...);

        Note: Snowflake does not log this information to the access_history table.

        Args:
            discovered_tables: List of discovered table identifiers

        Yields:
            KnownLineageMapping objects representing external lineage
        """
        query: str = SnowflakeQuery.copy_lineage_history(
            start_time_millis=int(self.start_time.timestamp() * 1000),
            end_time_millis=int(self.end_time.timestamp() * 1000),
            downstreams_deny_pattern=self.config.temporary_tables_pattern,
        )

        try:
            for db_row in self.connection.query(query):
                try:
                    known_lineage_mapping = self._process_external_lineage_result_row(
                        db_row, discovered_tables, identifiers=self.identifiers
                    )

                    if known_lineage_mapping:
                        self.report.num_external_table_edges_scanned += 1
                        yield known_lineage_mapping

                except Exception as e:
                    logger.error(f"Error processing external lineage row: {e}")
                    continue

        except Exception as e:
            if isinstance(e, SnowflakePermissionError):
                error_msg = (
                    "Failed to get external lineage. Please grant imported privileges "
                    "on SNOWFLAKE database."
                )
                self.warn_if_stateful_else_error(LINEAGE_PERMISSION_ERROR, error_msg)
            else:
                self.structured_reporter.warning(
                    "Error fetching external lineage from Snowflake",
                    exc=e,
                )
            self.report_status(EXTERNAL_LINEAGE, False)

    @classmethod
    def _process_external_lineage_result_row(
        cls,
        db_row: dict,
        discovered_tables: Optional[Collection[str]],
        identifiers: SnowflakeIdentifierBuilder,
    ) -> Optional[KnownLineageMapping]:
        """
        Process a single row from copy_history query into a lineage mapping.

        Args:
            db_row: Database row from copy_history query
            discovered_tables: Collection of discovered table identifiers
            identifiers: Identifier builder for generating URNs

        Returns:
            KnownLineageMapping or None if not applicable
        """
        # Extract downstream table identifier
        key: str = identifiers.get_dataset_identifier_from_qualified_name(
            db_row["DOWNSTREAM_TABLE_NAME"]
        )

        # Skip if table not discovered
        if discovered_tables is not None and key not in discovered_tables:
            return None

        # Process upstream locations
        if db_row["UPSTREAM_LOCATIONS"] is not None:
            try:
                external_locations = json.loads(db_row["UPSTREAM_LOCATIONS"])

                for loc in external_locations:
                    if loc.startswith("s3://"):
                        return KnownLineageMapping(
                            upstream_urn=make_s3_urn_for_lineage(
                                loc, identifiers.identifier_config.env
                            ),
                            downstream_urn=identifiers.gen_dataset_urn(key),
                        )

            except Exception as e:
                logger.error(f"Error parsing upstream locations: {e}")

        return None

    def _fetch_upstream_lineages_for_tables(self) -> Iterable[UpstreamLineageEdge]:
        """
        Fetch upstream lineage information from Snowflake's access_history.

        Returns:
            Iterable of UpstreamLineageEdge objects
        """
        query: str = SnowflakeQuery.table_to_table_lineage_history_v2(
                start_time_millis=int(self.start_time.timestamp() * 1000),
                end_time_millis=int(self.end_time.timestamp() * 1000),
                upstreams_deny_pattern=self.config.temporary_tables_pattern,
                include_column_lineage=self.config.include_column_lineage,
            )

        try:
            for db_row in self.connection.query(query):
                edge = self._process_upstream_lineage_row(db_row)
                if edge:
                    yield edge

        except Exception as e:
            if isinstance(e, SnowflakePermissionError):
                error_msg = (
                    "Failed to get table/view to table lineage. Please grant imported "
                    "privileges on SNOWFLAKE database."
                )
                self.warn_if_stateful_else_error(LINEAGE_PERMISSION_ERROR, error_msg)
            else:
                self.structured_reporter.warning(
                    "Failed to extract table/view -> table lineage from Snowflake",
                    exc=e,
                )
            self.report_status(TABLE_LINEAGE, False)

    def _process_upstream_lineage_row(
        self, db_row: dict
    ) -> Optional[UpstreamLineageEdge]:
        """
        Process a single upstream lineage row into an UpstreamLineageEdge.

        Args:
            db_row: Raw database row from access_history query

        Returns:
            UpstreamLineageEdge or None if parsing failed
        """
        try:
            # Handle empty queries array case
            _queries = db_row.get("QUERIES")
            if _queries == "[\n  {}\n]":
                # Snowflake sometimes returns an empty object in the array
                # Set to empty array to avoid Pydantic parsing errors
                db_row["QUERIES"] = "[]"

            return UpstreamLineageEdge.parse_obj(db_row)

        except Exception as e:
            self.report.num_upstream_lineage_edge_parsing_failed += 1

            # Extract key information for debugging
            upstream_tables = db_row.get("UPSTREAM_TABLES")
            downstream_table = db_row.get("DOWNSTREAM_TABLE_NAME")

            self.structured_reporter.warning(
                "Failed to parse lineage edge",
                context=(
                    f"Upstreams: {upstream_tables} "
                    f"Downstream: {downstream_table} "
                    f"Full row: {db_row}"
                ),
                exc=e,
            )
            return None

    def map_query_result_upstreams(
        self, upstream_tables: Optional[List[UpstreamTableNode]], query_id: str
    ) -> List[UrnStr]:
        """
        Map upstream table nodes to URN strings.

        Args:
            upstream_tables: List of upstream table nodes
            query_id: Query ID to match against

        Returns:
            List of upstream URN strings
        """
        if not upstream_tables:
            return []

        upstreams: List[UrnStr] = []

        for upstream_table in upstream_tables:
            if upstream_table and upstream_table.query_id == query_id:
                try:
                    upstream_name = (
                        self.identifiers.get_dataset_identifier_from_qualified_name(
                            upstream_table.upstream_object_name
                        )
                    )

                    # Validate upstream against patterns if configured
                    if upstream_name and (
                        not self.config.validate_upstreams_against_patterns
                        or self.filters.is_dataset_pattern_allowed(
                            upstream_name,
                            upstream_table.upstream_object_domain,
                        )
                    ):
                        upstreams.append(
                            self.identifiers.gen_dataset_urn(upstream_name)
                        )

                except Exception as e:
                    logger.debug(f"Error processing upstream table: {e}", exc_info=True)

        return upstreams

    def map_query_result_fine_upstreams(
        self,
        dataset_urn: str,
        column_wise_upstreams: Optional[List[ColumnUpstreamLineage]],
        query_id: str,
    ) -> List[ColumnLineageInfo]:
        """
        Map column-wise upstream information to ColumnLineageInfo objects.

        Args:
            dataset_urn: URN of the downstream dataset
            column_wise_upstreams: List of column upstream lineage information
            query_id: Query ID to match against

        Returns:
            List of ColumnLineageInfo objects
        """
        if not column_wise_upstreams:
            return []

        fine_upstreams: List[ColumnLineageInfo] = []

        for column_with_upstreams in column_wise_upstreams:
            if column_with_upstreams:
                try:
                    self._process_add_single_column_upstream(
                        dataset_urn, fine_upstreams, column_with_upstreams, query_id
                    )
                except Exception as e:
                    logger.debug(f"Error processing column upstream: {e}", exc_info=True)

        return fine_upstreams

    def _process_add_single_column_upstream(
        self,
        dataset_urn: str,
        fine_upstreams: List[ColumnLineageInfo],
        column_with_upstreams: ColumnUpstreamLineage,
        query_id: str,
    ) -> None:
        """
        Process a single column's upstream lineage information.

        Args:
            dataset_urn: URN of the downstream dataset
            fine_upstreams: List to append new ColumnLineageInfo to
            column_with_upstreams: Column upstream lineage data
            query_id: Query ID to match against
        """
        column_name = column_with_upstreams.column_name
        upstream_jobs = column_with_upstreams.upstreams

        if column_name and upstream_jobs:
            for upstream_job in upstream_jobs:
                if not upstream_job or upstream_job.query_id != query_id:
                    continue

                fine_upstream = self.build_finegrained_lineage(
                    dataset_urn=dataset_urn,
                    col=column_name,
                    upstream_columns={
                        SnowflakeColumnId(
                            column_name=col.column_name,
                            object_name=col.object_name,
                            object_domain=col.object_domain,
                        )
                        for col in upstream_job.column_upstreams
                    },
                )

                if fine_upstream:
                    fine_upstreams.append(fine_upstream)

    def build_finegrained_lineage(
        self,
        dataset_urn: str,
        col: str,
        upstream_columns: Set[SnowflakeColumnId],
    ) -> Optional[ColumnLineageInfo]:
        """
        Build fine-grained column lineage information.

        Args:
            dataset_urn: URN of the downstream dataset
            col: Downstream column name
            upstream_columns: Set of upstream column identifiers

        Returns:
            ColumnLineageInfo or None if no valid upstreams
        """
        column_upstreams = self.build_finegrained_lineage_upstreams(upstream_columns)

        if not column_upstreams:
            return None

        column_lineage = ColumnLineageInfo(
            downstream=DownstreamColumnRef(
                dataset=dataset_urn,
                column=self.identifiers.snowflake_identifier(col)
            ),
            upstreams=sorted(column_upstreams),
        )

        return column_lineage

    def build_finegrained_lineage_upstreams(
        self, upstream_columns: Set[SnowflakeColumnId]
    ) -> List[ColumnRef]:
        """
        Build list of upstream column references.

        Args:
            upstream_columns: Set of upstream column identifiers

        Returns:
            List of ColumnRef objects
        """
        column_upstreams = []

        for upstream_col in upstream_columns:
            if (
                upstream_col.object_name
                and upstream_col.column_name
                and (
                    not self.config.validate_upstreams_against_patterns
                    or self.filters.is_dataset_pattern_allowed(
                        upstream_col.object_name,
                        upstream_col.object_domain,
                    )
                )
            ):
                try:
                    upstream_dataset_name = (
                        self.identifiers.get_dataset_identifier_from_qualified_name(
                            upstream_col.object_name
                        )
                    )

                    column_upstreams.append(
                        ColumnRef(
                            table=self.identifiers.gen_dataset_urn(upstream_dataset_name),
                            column=self.identifiers.snowflake_identifier(
                                upstream_col.column_name
                            ),
                        )
                    )

                except Exception as e:
                    logger.debug(f"Error building upstream column ref: {e}")

        return column_upstreams

    def get_external_upstreams(self, external_lineage: Set[str]) -> List[UpstreamClass]:
        """
        Convert external lineage entries to UpstreamClass objects.

        Args:
            external_lineage: Set of external lineage URN strings

        Returns:
            List of UpstreamClass objects
        """
        external_upstreams = []

        for external_lineage_entry in sorted(external_lineage):
            # Currently only handle S3 external sources
            if external_lineage_entry.startswith("s3://"):
                external_upstream_table = UpstreamClass(
                    dataset=make_s3_urn_for_lineage(
                        external_lineage_entry, self.config.env
                    ),
                    type=DatasetLineageTypeClass.COPY,
                )
                external_upstreams.append(external_upstream_table)

        return external_upstreams

    def _should_ingest_lineage(self) -> bool:
        """
        Determine if lineage should be ingested for this run.

        Uses redundant run skip handler to avoid processing the same
        time window multiple times.

        Returns:
            True if lineage should be ingested, False otherwise
        """
        if (
            self.redundant_run_skip_handler
            and self.redundant_run_skip_handler.should_skip_this_run(
                cur_start_time=(
                    self.config.start_time
                    if not self.config.ignore_start_time_lineage
                    else ts_millis_to_datetime(0)
                ),
                cur_end_time=self.config.end_time,
            )
        ):
            # Skip this run - already processed
            self.report.report_warning(
                "lineage-extraction",
                "Skip this run as there was already a run for current ingestion window.",
            )
            return False

        return True

    def report_status(self, step: str, status: bool) -> None:
        """
        Report the status of a lineage extraction step.

        Args:
            step: Name of the step being reported
            status: Whether the step was successful
        """
        if self.redundant_run_skip_handler:
            self.redundant_run_skip_handler.report_current_run_status(step, status)

    def _process_stored_proc_lineage(self, discovered_tables: List[str]) -> None:
        """
        Process stored procedure lineage from Snowflake query history.
        
        This method identifies stored procedure calls and tracks their related queries
        to build comprehensive lineage for procedure-level transformations.
        
        Args:
            discovered_tables: List of discovered table identifiers
        """
        if not self.stored_proc_tracker:
            logger.debug("Stored procedure tracker not initialized, skipping stored proc lineage")
            return
            
        logger.info("Processing stored procedure lineage...")
        
        try:
            # Query for stored procedure calls in the time window
            stored_proc_query = f"""
            SELECT 
                query_id,
                query_text,
                start_time,
                user_name,
                database_name,
                schema_name
            FROM snowflake.account_usage.query_history 
            WHERE query_text ILIKE 'CALL %'
                AND start_time >= '{self.start_time}'
                AND start_time <= '{self.end_time}'
                AND query_type = 'CALL'
            ORDER BY start_time DESC
            """
            
            with self.connection.execute_query(stored_proc_query) as cursor:
                for row in cursor:
                    try:
                        # Create stored procedure call
                        call = StoredProcCall(
                            snowflake_root_query_id=row.query_id,
                            query_text=row.query_text,
                            timestamp=row.start_time,
                            user=CorpUserUrn(f"{row.user_name}@company.com"),  # Default domain
                            default_db=row.database_name or "UNKNOWN",
                            default_schema=row.schema_name or "UNKNOWN"
                        )
                        
                        # Add to tracker
                        self.stored_proc_tracker.add_stored_proc_call(call)
                        logger.debug(f"Added stored procedure call: {call.get_procedure_name()}")
                        
                    except Exception as e:
                        logger.warning(f"Failed to process stored procedure call {row.query_id}: {e}")
                        continue
            
            # Query for related queries that belong to stored procedures
            related_queries_query = f"""
            SELECT 
                query_id,
                query_text,
                root_query_id,
                start_time,
                user_name,
                database_name,
                schema_name
            FROM snowflake.account_usage.query_history 
            WHERE root_query_id IS NOT NULL
                AND root_query_id != query_id
                AND start_time >= '{self.start_time}'
                AND start_time <= '{self.end_time}'
                AND query_type IN ('SELECT', 'INSERT', 'UPDATE', 'DELETE', 'MERGE', 'CREATE_TABLE_AS_SELECT')
            ORDER BY start_time DESC
            """
            
            with self.connection.execute_query(related_queries_query) as cursor:
                for row in cursor:
                    try:
                        # Create a mock PreparsedQuery for the stored proc tracker
                        from dataguild.sql_parsing.sql_parsing_aggregator import PreparsedQuery
                        
                        # Extract upstream and downstream datasets from query
                        upstreams = self._extract_datasets_from_query(row.query_text, discovered_tables)
                        downstream = self._extract_downstream_from_query(row.query_text, discovered_tables)
                        
                        query = PreparsedQuery(
                            query_id=row.query_id,
                            query_text=row.query_text,
                            upstreams=upstreams,
                            downstream=downstream,
                            column_lineage=None,
                            column_usage=None,
                            inferred_schema=None,
                            confidence_score=0.7,
                            query_count=1,
                            user=CorpUserUrn(f"{row.user_name}@company.com"),
                            timestamp=row.start_time,
                            session_id="",
                            query_type=row.query_type,
                            extra_info={"snowflake_root_query_id": row.root_query_id}
                        )
                        
                        # Add to stored procedure tracker
                        success = self.stored_proc_tracker.add_related_query(query)
                        if success:
                            logger.debug(f"Associated query {row.query_id} with stored procedure {row.root_query_id}")
                            
                    except Exception as e:
                        logger.warning(f"Failed to process related query {row.query_id}: {e}")
                        continue
            
            # Generate lineage entries from stored procedures
            for lineage_entry in self.stored_proc_tracker.build_merged_lineage_entries():
                self.sql_aggregator.add(lineage_entry)
                logger.debug(f"Added stored procedure lineage: {len(lineage_entry.upstreams)} upstreams -> {lineage_entry.downstream}")
            
            logger.info("Stored procedure lineage processing completed")
            
        except Exception as e:
            logger.error(f"Failed to process stored procedure lineage: {e}")
            raise

    def _extract_datasets_from_query(self, query_text: str, discovered_tables: List[str]) -> List[UrnStr]:
        """Extract upstream dataset URNs from a SQL query."""
        upstreams = []
        query_upper = query_text.upper()
        
        for table in discovered_tables:
            table_name = table.split('.')[-1].split(',')[0]  # Extract table name
            if table_name.upper() in query_upper:
                upstreams.append(table)
        
        return upstreams

    def _extract_downstream_from_query(self, query_text: str, discovered_tables: List[str]) -> Optional[UrnStr]:
        """Extract downstream dataset URN from a SQL query."""
        query_upper = query_text.upper()
        
        # Look for CREATE TABLE AS SELECT, INSERT INTO, UPDATE, MERGE patterns
        if any(pattern in query_upper for pattern in ['CREATE TABLE', 'INSERT INTO', 'UPDATE', 'MERGE']):
            for table in discovered_tables:
                table_name = table.split('.')[-1].split(',')[0]
                if table_name.upper() in query_upper:
                    return table
        
        return None

    def close(self) -> None:
        """Close the lineage extractor and clean up resources."""
        logger.info("Closing SnowflakeLineageExtractor")
        
        # Close stored procedure tracker if initialized
        if self.stored_proc_tracker:
            self.stored_proc_tracker.close()
            self.stored_proc_tracker = None


# Export all classes
__all__ = [
    'SnowflakeLineageExtractor',
    'UpstreamLineageEdge',
    'UpstreamTableNode',
    'UpstreamColumnNode',
    'ColumnUpstreamJob',
    'ColumnUpstreamLineage',
    'Query',
    'SnowflakeColumnId',
    'pydantic_parse_json',
]


# Example usage and testing
if __name__ == "__main__":
    print("=== DataGuild Snowflake Lineage Extractor Examples ===\n")

    # Example 1: Create Pydantic models
    upstream_table = UpstreamTableNode(
        upstream_object_domain="TABLE",
        upstream_object_name="RAW.CUSTOMERS",
        query_id="query123"
    )

    query = Query(
        query_id="query123",
        query_text="INSERT INTO analytics.customer_summary SELECT * FROM raw.customers",
        start_time="2024-01-15T10:30:00Z"
    )

    lineage_edge = UpstreamLineageEdge(
        DOWNSTREAM_TABLE_NAME="ANALYTICS.CUSTOMER_SUMMARY",
        DOWNSTREAM_TABLE_DOMAIN="TABLE",
        UPSTREAM_TABLES=[upstream_table],
        QUERIES=[query]
    )

    print("Example 1: Pydantic Models")
    print(f"Upstream Table: {upstream_table}")
    print(f"Query: {query}")
    print(f"Lineage Edge downstream: {lineage_edge.DOWNSTREAM_TABLE_NAME}")
    print(f"Lineage Edge upstreams: {len(lineage_edge.UPSTREAM_TABLES or [])}")
    print()

    # Example 2: Snowflake Column ID
    column_id = SnowflakeColumnId(
        column_name="customer_id",
        object_name="raw.customers",
        object_domain="TABLE"
    )

    print("Example 2: Snowflake Column ID")
    print(f"Column ID: {column_id}")
    print(f"Column name: {column_id.column_name}")
    print(f"Object name: {column_id.object_name}")
    print()

    # Example 3: JSON parsing validation
    print("Example 3: JSON Parsing")
    json_data = {
        "DOWNSTREAM_TABLE_NAME": "ANALYTICS.SUMMARY",
        "DOWNSTREAM_TABLE_DOMAIN": "TABLE",
        "UPSTREAM_TABLES": '[{"upstream_object_domain": "TABLE", "upstream_object_name": "RAW.DATA", "query_id": "q1"}]',
        "QUERIES": '[{"query_id": "q1", "query_text": "SELECT * FROM raw.data", "start_time": "2024-01-15T10:00:00Z"}]'
    }

    try:
        parsed_edge = UpstreamLineageEdge.parse_obj(json_data)
        print(f"Successfully parsed lineage edge: {parsed_edge.DOWNSTREAM_TABLE_NAME}")
        print(f"Upstream tables: {len(parsed_edge.UPSTREAM_TABLES or [])}")
        print(f"Queries: {len(parsed_edge.QUERIES or [])}")
    except Exception as e:
        print(f"Error parsing lineage edge: {e}")
