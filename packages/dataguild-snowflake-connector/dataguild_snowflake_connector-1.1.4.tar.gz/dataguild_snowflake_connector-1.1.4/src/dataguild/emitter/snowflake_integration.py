"""
DataGuild Snowflake Connector Emitter Integration

Enhanced integration between DataGuild Snowflake connector and emitters
with comprehensive metadata processing and emission capabilities.
"""

import json
import logging
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union, Iterator

from dataguild.api.workunit import MetadataWorkUnit
from dataguild.emitter.dataguild_rest_emitter import DataGuildRestEmitter, EmitResult
from dataguild.emitter.dataguild_kafka_emitter import DataGuildKafkaEmitter, KafkaEmitResult
from dataguild.emitter.mcp import (
    MetadataChangeProposal,
    create_dataset_mcp,
    create_lineage_mcp,
    create_schema_mcp,
    create_datajob_mcp,
    create_dataflow_mcp
)

logger = logging.getLogger(__name__)


@dataclass
class SnowflakeEmissionConfig:
    """Configuration for Snowflake metadata emission."""
    enable_emission: bool = True
    emitter_type: str = "rest"  # 'rest' or 'kafka'
    batch_size: int = 100
    enable_validation: bool = True
    enable_deduplication: bool = True
    enable_lineage_emission: bool = True
    enable_schema_emission: bool = True
    enable_usage_emission: bool = True
    enable_operation_emission: bool = True


class SnowflakeEmitterIntegration:
    """
    Enhanced integration between DataGuild Snowflake connector and emitters.
    
    Features:
    - Automatic MCP conversion from workunits
    - Intelligent batching and deduplication
    - Comprehensive metadata type support
    - Error handling and retry logic
    - Performance monitoring and statistics
    """
    
    def __init__(
        self,
        emitter: Union[DataGuildRestEmitter, DataGuildKafkaEmitter],
        config: SnowflakeEmissionConfig
    ):
        self.emitter = emitter
        self.config = config
        self.stats = {
            "total_processed": 0,
            "successful_emissions": 0,
            "failed_emissions": 0,
            "batches_processed": 0,
            "mcp_conversions": 0,
            "lineage_emissions": 0,
            "schema_emissions": 0,
            "usage_emissions": 0,
            "operation_emissions": 0
        }
        self._processed_workunits = set()  # For deduplication
    
    def emit_workunits(self, workunits: List[MetadataWorkUnit]) -> Dict[str, Any]:
        """Emit a list of workunits with enhanced processing."""
        if not self.config.enable_emission:
            logger.info("Emission disabled, skipping workunits")
            return {"status": "disabled", "count": len(workunits)}
        
        results = {
            "total": len(workunits),
            "successful": 0,
            "failed": 0,
            "skipped": 0,
            "errors": []
        }
        
        try:
            # Filter and deduplicate workunits
            filtered_workunits = self._filter_workunits(workunits)
            results["skipped"] = len(workunits) - len(filtered_workunits)
            
            # Process in batches
            batch_size = self.config.batch_size
            for i in range(0, len(filtered_workunits), batch_size):
                batch = filtered_workunits[i:i + batch_size]
                batch_results = self._process_batch(batch)
                
                # Update results
                results["successful"] += batch_results["successful"]
                results["failed"] += batch_results["failed"]
                results["errors"].extend(batch_results.get("errors", []))
                
                self.stats["batches_processed"] += 1
                logger.info(f"📦 Processed batch {i//batch_size + 1}: {len(batch)} workunits")
            
            self.stats["total_processed"] += len(filtered_workunits)
            self.stats["successful_emissions"] += results["successful"]
            self.stats["failed_emissions"] += results["failed"]
            
            logger.info(f"✅ Emission complete: {results['successful']}/{results['total']} successful")
            
        except Exception as e:
            logger.error(f"❌ Emission failed: {e}")
            results["errors"].append({"error": str(e)})
        
        return results
    
    def _filter_workunits(self, workunits: List[MetadataWorkUnit]) -> List[MetadataWorkUnit]:
        """Filter and deduplicate workunits."""
        filtered = []
        
        for workunit in workunits:
            # Deduplication
            if self.config.enable_deduplication and workunit.id in self._processed_workunits:
                continue
            
            # Validation
            if self.config.enable_validation and not self._validate_workunit(workunit):
                continue
            
            filtered.append(workunit)
            self._processed_workunits.add(workunit.id)
        
        return filtered
    
    def _validate_workunit(self, workunit: MetadataWorkUnit) -> bool:
        """Validate a workunit before emission."""
        try:
            # Check required fields
            if not workunit.id:
                logger.warning(f"Workunit missing ID: {workunit}")
                return False
            
            # Check MCP raw data if present
            if hasattr(workunit, 'mcp_raw') and workunit.mcp_raw:
                required_fields = ['entityType', 'changeType', 'entityUrn', 'aspectName', 'aspect']
                for field in required_fields:
                    if field not in workunit.mcp_raw:
                        logger.warning(f"Workunit {workunit.id} missing required field: {field}")
                        return False
            
            return True
            
        except Exception as e:
            logger.warning(f"Validation error for workunit {workunit.id}: {e}")
            return False
    
    def _process_batch(self, workunits: List[MetadataWorkUnit]) -> Dict[str, Any]:
        """Process a batch of workunits."""
        results = {
            "successful": 0,
            "failed": 0,
            "errors": []
        }
        
        try:
            # Convert workunits to MCPs
            mcps = []
            for workunit in workunits:
                mcp = self._workunit_to_mcp(workunit)
                if mcp:
                    mcps.append(mcp)
                    self.stats["mcp_conversions"] += 1
            
            if not mcps:
                logger.warning("No valid MCPs generated from batch")
                return results
            
            # Emit MCPs
            if isinstance(self.emitter, DataGuildRestEmitter):
                emit_results = self.emitter.emit_mcps_batch(mcps)
            elif isinstance(self.emitter, DataGuildKafkaEmitter):
                emit_results = self.emitter.emit_mcps_batch(mcps)
            else:
                raise ValueError(f"Unsupported emitter type: {type(self.emitter)}")
            
            # Process results
            for result in emit_results:
                if hasattr(result, 'success') and result.success:
                    results["successful"] += 1
                else:
                    results["failed"] += 1
                    results["errors"].append({
                        "workunit_id": getattr(result, 'workunit_id', 'unknown'),
                        "error": str(getattr(result, 'error', 'Unknown error'))
                    })
            
        except Exception as e:
            logger.error(f"❌ Batch processing failed: {e}")
            results["failed"] = len(workunits)
            results["errors"].append({"error": str(e)})
        
        return results
    
    def _workunit_to_mcp(self, workunit: MetadataWorkUnit) -> Optional[MetadataChangeProposal]:
        """Convert a workunit to MCP with enhanced processing."""
        try:
            # Check if workunit has MCP raw data
            if hasattr(workunit, 'mcp_raw') and workunit.mcp_raw:
                mcp_raw = workunit.mcp_raw
                
                # Create MCP from raw data
                mcp = MetadataChangeProposal(
                    entityType=mcp_raw.get("entityType", "dataset"),
                    changeType=mcp_raw.get("changeType", "UPSERT"),
                    entityUrn=mcp_raw.get("entityUrn", workunit.id),
                    aspectName=mcp_raw.get("aspectName", "unknown"),
                    aspect=mcp_raw.get("aspect", {}),
                    systemMetadata=mcp_raw.get("systemMetadata", {})
                )
                
                # Track emission type
                self._track_emission_type(mcp_raw.get("aspectName", ""))
                
                return mcp
            
            else:
                # Try to infer MCP from workunit metadata
                return self._infer_mcp_from_workunit(workunit)
                
        except Exception as e:
            logger.error(f"Failed to convert workunit {workunit.id} to MCP: {e}")
            return None
    
    def _infer_mcp_from_workunit(self, workunit: MetadataWorkUnit) -> Optional[MetadataChangeProposal]:
        """Infer MCP from workunit metadata when MCP raw is not available."""
        try:
            metadata = getattr(workunit, 'metadata', {})
            
            # Try to determine entity type from workunit ID
            entity_type = "dataset"
            if "lineage" in workunit.id.lower():
                entity_type = "dataset"
            elif "schema" in workunit.id.lower():
                entity_type = "dataset"
            elif "usage" in workunit.id.lower():
                entity_type = "dataset"
            elif "operation" in workunit.id.lower():
                entity_type = "dataJob"
            
            # Create basic MCP
            mcp = MetadataChangeProposal(
                entityType=entity_type,
                changeType="UPSERT",
                entityUrn=workunit.id,
                aspectName="unknown",
                aspect=metadata,
                systemMetadata={}
            )
            
            return mcp
            
        except Exception as e:
            logger.error(f"Failed to infer MCP from workunit {workunit.id}: {e}")
            return None
    
    def _track_emission_type(self, aspect_name: str):
        """Track emission type for statistics."""
        if "lineage" in aspect_name.lower():
            self.stats["lineage_emissions"] += 1
        elif "schema" in aspect_name.lower():
            self.stats["schema_emissions"] += 1
        elif "usage" in aspect_name.lower():
            self.stats["usage_emissions"] += 1
        elif "operation" in aspect_name.lower():
            self.stats["operation_emissions"] += 1
    
    def emit_specific_metadata(
        self,
        metadata_type: str,
        entity_urn: str,
        aspect_data: Dict[str, Any],
        change_type: str = "UPSERT"
    ) -> Optional[Union[EmitResult, KafkaEmitResult]]:
        """Emit specific metadata types with enhanced processing."""
        try:
            if metadata_type == "lineage" and self.config.enable_lineage_emission:
                mcp = create_lineage_mcp(
                    entity_urn,
                    aspect_data.get("upstreams", []),
                    change_type
                )
            elif metadata_type == "schema" and self.config.enable_schema_emission:
                mcp = create_schema_mcp(
                    entity_urn,
                    aspect_data,
                    change_type
                )
            elif metadata_type == "datajob" and self.config.enable_operation_emission:
                mcp = create_datajob_mcp(
                    entity_urn,
                    "dataJobInfo",
                    aspect_data,
                    change_type
                )
            elif metadata_type == "dataflow" and self.config.enable_operation_emission:
                mcp = create_dataflow_mcp(
                    entity_urn,
                    "dataFlowInfo",
                    aspect_data,
                    change_type
                )
            else:
                # Generic dataset MCP
                mcp = create_dataset_mcp(
                    entity_urn,
                    metadata_type,
                    aspect_data,
                    change_type
                )
            
            # Emit MCP
            if isinstance(self.emitter, DataGuildRestEmitter):
                return self.emitter.emit_mcp(mcp)
            elif isinstance(self.emitter, DataGuildKafkaEmitter):
                return self.emitter.emit_mcp(mcp)
            else:
                raise ValueError(f"Unsupported emitter type: {type(self.emitter)}")
                
        except Exception as e:
            logger.error(f"Failed to emit {metadata_type} metadata: {e}")
            return None
    
    def get_stats(self) -> Dict[str, Any]:
        """Get comprehensive emission statistics."""
        stats = self.stats.copy()
        
        # Add emitter-specific stats
        if hasattr(self.emitter, 'get_stats'):
            emitter_stats = self.emitter.get_stats()
            stats.update(emitter_stats)
        
        # Calculate success rate
        total = stats["total_processed"]
        if total > 0:
            stats["success_rate"] = stats["successful_emissions"] / total
        else:
            stats["success_rate"] = 0.0
        
        return stats
    
    def close(self):
        """Close the emitter integration."""
        if hasattr(self.emitter, 'close'):
            self.emitter.close()
        
        logger.info("✅ Snowflake emitter integration closed")


# Factory functions
def create_snowflake_rest_emitter_integration(
    server_url: str,
    token: Optional[str] = None,
    config: Optional[SnowflakeEmissionConfig] = None
) -> SnowflakeEmitterIntegration:
    """Create a Snowflake REST emitter integration."""
    from dataguild.emitter.dataguild_rest_emitter import create_dataguild_rest_emitter
    
    emitter = create_dataguild_rest_emitter(server_url=server_url, token=token)
    config = config or SnowflakeEmissionConfig()
    
    return SnowflakeEmitterIntegration(emitter, config)


def create_snowflake_kafka_emitter_integration(
    bootstrap_servers: str,
    topic_name: str = "dataguild-metadata",
    config: Optional[SnowflakeEmissionConfig] = None
) -> SnowflakeEmitterIntegration:
    """Create a Snowflake Kafka emitter integration."""
    from dataguild.emitter.dataguild_kafka_emitter import create_dataguild_kafka_emitter
    
    emitter = create_dataguild_kafka_emitter(
        bootstrap_servers=bootstrap_servers,
        topic_name=topic_name
    )
    config = config or SnowflakeEmissionConfig()
    
    return SnowflakeEmitterIntegration(emitter, config)

