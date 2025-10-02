"""
DataGuild MCP (Metadata Change Proposal) Classes

enterprise-compatible metadata change proposal and event classes
for enterprise-grade metadata ingestion and processing.
"""

import json
import logging
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional, Union

# Import MetadataWorkUnit from the correct location
try:
    from dataguild.api.workunit import MetadataWorkUnit
except ImportError:
    # Fallback if not available
    MetadataWorkUnit = None

logger = logging.getLogger(__name__)


class ChangeType(Enum):
    """Types of metadata changes."""
    CREATE = "CREATE"
    UPDATE = "UPDATE"
    UPSERT = "UPSERT"
    DELETE = "DELETE"
    PATCH = "PATCH"


class EntityType(Enum):
    """enterprise entity types."""
    DATASET = "dataset"
    DATAJOB = "dataJob"
    DATAFLOW = "dataFlow"
    CHART = "chart"
    DASHBOARD = "dashboard"
    CORP_USER = "corpUser"
    CORP_GROUP = "corpGroup"
    CONTAINER = "container"
    DOMAIN = "domain"
    GLOSSARY_TERM = "glossaryTerm"
    GLOSSARY_NODE = "glossaryNode"
    TAG = "tag"
    ML_FEATURE = "mlFeature"
    ML_FEATURE_TABLE = "mlFeatureTable"
    ML_MODEL = "mlModel"
    ML_MODEL_GROUP = "mlModelGroup"
    ML_PRIMARY_KEY = "mlPrimaryKey"
    NOTEBOOK = "notebook"
    POST = "post"
    SYSTEM_METADATA = "systemMetadata"
    TIMESERIES = "timeseries"
    VIEW = "view"


class AspectType(Enum):
    """Metadata aspect types."""
    DATASET_PROPERTIES = "datasetProperties"
    SCHEMA_METADATA = "schemaMetadata"
    OWNERSHIP = "ownership"
    GLOBAL_TAGS = "globalTags"
    GLOSSARY_TERMS = "glossaryTerms"
    DOMAINS = "domains"
    DEPRECATION = "deprecation"
    DATA_PLATFORM_INSTANCE = "dataPlatformInstance"
    DATASET_USAGE_STATISTICS = "datasetUsageStatistics"
    DATASET_PROFILE = "datasetProfile"
    DATASET_LINEAGE = "datasetLineage"
    UPSTREAM_LINEAGE = "upstreamLineage"
    DOWNSTREAM_LINEAGE = "downstreamLineage"
    BROWSE_PATHS = "browsePaths"
    DATA_PRODUCT = "dataProduct"
    SUB_TYPES = "subTypes"
    CONTAINER_PROPERTIES = "containerProperties"
    CHART_INFO = "chartInfo"
    DASHBOARD_INFO = "dashboardInfo"
    CORP_USER_INFO = "corpUserInfo"
    CORP_GROUP_INFO = "corpGroupInfo"
    ML_FEATURE_PROPERTIES = "mlFeatureProperties"
    ML_FEATURE_TABLE_PROPERTIES = "mlFeatureTableProperties"
    ML_MODEL_PROPERTIES = "mlModelProperties"
    ML_MODEL_GROUP_PROPERTIES = "mlModelGroupProperties"
    ML_PRIMARY_KEY_PROPERTIES = "mlPrimaryKeyProperties"
    NOTEBOOK_INFO = "notebookInfo"
    POST_INFO = "postInfo"
    SYSTEM_METADATA = "systemMetadata"
    TIMESERIES_PROPERTIES = "timeseriesProperties"
    VIEW_PROPERTIES = "viewProperties"


class MetadataAspect:
    """Base class for metadata aspects."""
    
    def aspect_name(self) -> str:
        """Return the aspect name."""
        raise NotImplementedError
    
    def validate(self) -> bool:
        """Validate the aspect content."""
        return True
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        raise NotImplementedError


@dataclass
class SystemMetadata:
    """System metadata for tracking changes."""
    last_observed_at: Optional[datetime] = None
    run_id: Optional[str] = None
    properties: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        result = {}
        if self.last_observed_at:
            result["lastObservedAt"] = self.last_observed_at.isoformat()
        if self.run_id:
            result["runId"] = self.run_id
        if self.properties:
            result["properties"] = self.properties
        return result


@dataclass
class MetadataChangeProposal:
    """
    enterprise-compatible Metadata Change Proposal.
    
    Represents a single change to a metadata entity's aspect.
    """
    entityType: str
    changeType: str
    entityUrn: str
    aspectName: str
    aspect: Dict[str, Any]
    systemMetadata: Optional[SystemMetadata] = None
    
    def __post_init__(self):
        """Validate the MCP after initialization."""
        if not self.entityType:
            raise ValueError("entityType cannot be empty")
        if not self.changeType:
            raise ValueError("changeType cannot be empty")
        if not self.entityUrn:
            raise ValueError("entityUrn cannot be empty")
        if not self.aspectName:
            raise ValueError("aspectName cannot be empty")
        if not self.aspect:
            raise ValueError("aspect cannot be empty")
    
    def to_obj(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        result = {
            "entityType": self.entityType,
            "changeType": self.changeType,
            "entityUrn": self.entityUrn,
            "aspectName": self.aspectName,
            "aspect": self.aspect
        }
        
        if self.systemMetadata:
            result["systemMetadata"] = self.systemMetadata.to_dict()
        
        return result
    
    def to_json(self) -> str:
        """Convert to JSON string."""
        return json.dumps(self.to_obj(), indent=2)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'MetadataChangeProposal':
        """Create from dictionary."""
        system_metadata = None
        if "systemMetadata" in data:
            sm_data = data["systemMetadata"]
            system_metadata = SystemMetadata(
                last_observed_at=datetime.fromisoformat(sm_data["lastObservedAt"]) if sm_data.get("lastObservedAt") else None,
                run_id=sm_data.get("runId"),
                properties=sm_data.get("properties", {})
            )
        
        return cls(
            entityType=data["entityType"],
            changeType=data["changeType"],
            entityUrn=data["entityUrn"],
            aspectName=data["aspectName"],
            aspect=data["aspect"],
            systemMetadata=system_metadata
        )
    
    @classmethod
    def from_json(cls, json_str: str) -> 'MetadataChangeProposal':
        """Create from JSON string."""
        data = json.loads(json_str)
        return cls.from_dict(data)


@dataclass
class MetadataChangeProposalWrapper:
    """
    Wrapper for MetadataChangeProposal with additional metadata.
    
    Used for batch processing and advanced features.
    """
    mcp: MetadataChangeProposal
    timestamp: datetime = field(default_factory=datetime.now)
    source: Optional[str] = None
    version: str = "1.0"
    tags: List[str] = field(default_factory=list)
    properties: Dict[str, Any] = field(default_factory=dict)
    
    def to_obj(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        return {
            "mcp": self.mcp.to_obj(),
            "timestamp": self.timestamp.isoformat(),
            "source": self.source,
            "version": self.version,
            "tags": self.tags,
            "properties": self.properties
        }
    
    def to_json(self) -> str:
        """Convert to JSON string."""
        return json.dumps(self.to_obj(), indent=2)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'MetadataChangeProposalWrapper':
        """Create from dictionary."""
        mcp = MetadataChangeProposal.from_dict(data["mcp"])
        return cls(
            mcp=mcp,
            timestamp=datetime.fromisoformat(data["timestamp"]) if data.get("timestamp") else datetime.now(),
            source=data.get("source"),
            version=data.get("version", "1.0"),
            tags=data.get("tags", []),
            properties=data.get("properties", {})
        )


@dataclass
class MetadataChangeEvent:
    """
    enterprise-compatible Metadata Change Event.
    
    Represents a complete snapshot or delta change to a metadata entity.
    """
    proposedSnapshot: Optional[Dict[str, Any]] = None
    proposedDelta: Optional[Dict[str, Any]] = None
    systemMetadata: Optional[SystemMetadata] = None
    
    def __post_init__(self):
        """Validate the MCE after initialization."""
        if not self.proposedSnapshot and not self.proposedDelta:
            raise ValueError("Either proposedSnapshot or proposedDelta must be provided")
    
    def to_obj(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        result = {}
        
        if self.proposedSnapshot:
            result["proposedSnapshot"] = self.proposedSnapshot
        if self.proposedDelta:
            result["proposedDelta"] = self.proposedDelta
        if self.systemMetadata:
            result["systemMetadata"] = self.systemMetadata.to_dict()
        
        return result
    
    def to_json(self) -> str:
        """Convert to JSON string."""
        return json.dumps(self.to_obj(), indent=2)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'MetadataChangeEvent':
        """Create from dictionary."""
        system_metadata = None
        if "systemMetadata" in data:
            sm_data = data["systemMetadata"]
            system_metadata = SystemMetadata(
                last_observed_at=datetime.fromisoformat(sm_data["lastObservedAt"]) if sm_data.get("lastObservedAt") else None,
                run_id=sm_data.get("runId"),
                properties=sm_data.get("properties", {})
            )
        
        return cls(
            proposedSnapshot=data.get("proposedSnapshot"),
            proposedDelta=data.get("proposedDelta"),
            systemMetadata=system_metadata
        )


class MCPBuilder:
    """
    Builder class for creating MetadataChangeProposals.
    
    Provides a fluent API for constructing MCPs with proper validation.
    """
    
    def __init__(self):
        self._entity_type: Optional[str] = None
        self._change_type: Optional[str] = None
        self._entity_urn: Optional[str] = None
        self._aspect_name: Optional[str] = None
        self._aspect: Optional[Dict[str, Any]] = None
        self._system_metadata: Optional[SystemMetadata] = None
    
    def entity_type(self, entity_type: Union[str, EntityType]) -> 'MCPBuilder':
        """Set the entity type."""
        if isinstance(entity_type, EntityType):
            self._entity_type = entity_type.value
        else:
            self._entity_type = entity_type
        return self
    
    def change_type(self, change_type: Union[str, ChangeType]) -> 'MCPBuilder':
        """Set the change type."""
        if isinstance(change_type, ChangeType):
            self._change_type = change_type.value
        else:
            self._change_type = change_type
        return self
    
    def entity_urn(self, entity_urn: str) -> 'MCPBuilder':
        """Set the entity URN."""
        self._entity_urn = entity_urn
        return self
    
    def aspect_name(self, aspect_name: str) -> 'MCPBuilder':
        """Set the aspect name."""
        self._aspect_name = aspect_name
        return self
    
    def aspect(self, aspect: Dict[str, Any]) -> 'MCPBuilder':
        """Set the aspect data."""
        self._aspect = aspect
        return self
    
    def system_metadata(self, system_metadata: SystemMetadata) -> 'MCPBuilder':
        """Set the system metadata."""
        self._system_metadata = system_metadata
        return self
    
    def build(self) -> MetadataChangeProposal:
        """Build the MetadataChangeProposal."""
        if not self._entity_type:
            raise ValueError("entity_type is required")
        if not self._change_type:
            raise ValueError("change_type is required")
        if not self._entity_urn:
            raise ValueError("entity_urn is required")
        if not self._aspect_name:
            raise ValueError("aspect_name is required")
        if not self._aspect:
            raise ValueError("aspect is required")
        
        return MetadataChangeProposal(
            entityType=self._entity_type,
            changeType=self._change_type,
            entityUrn=self._entity_urn,
            aspectName=self._aspect_name,
            aspect=self._aspect,
            systemMetadata=self._system_metadata
        )


# Utility functions
def create_dataset_mcp(
    dataset_urn: str,
    aspect_name: str,
    aspect_data: Dict[str, Any],
    change_type: ChangeType = ChangeType.UPSERT
) -> MetadataChangeProposal:
    """Create a dataset MCP."""
    return MCPBuilder() \
        .entity_type(EntityType.DATASET) \
        .change_type(change_type) \
        .entity_urn(dataset_urn) \
        .aspect_name(aspect_name) \
        .aspect(aspect_data) \
        .build()


def create_datajob_mcp(
    datajob_urn: str,
    aspect_name: str,
    aspect_data: Dict[str, Any],
    change_type: ChangeType = ChangeType.UPSERT
) -> MetadataChangeProposal:
    """Create a data job MCP."""
    return MCPBuilder() \
        .entity_type(EntityType.DATAJOB) \
        .change_type(change_type) \
        .entity_urn(datajob_urn) \
        .aspect_name(aspect_name) \
        .aspect(aspect_data) \
        .build()


def create_dataflow_mcp(
    dataflow_urn: str,
    aspect_name: str,
    aspect_data: Dict[str, Any],
    change_type: ChangeType = ChangeType.UPSERT
) -> MetadataChangeProposal:
    """Create a data flow MCP."""
    return MCPBuilder() \
        .entity_type(EntityType.DATAFLOW) \
        .change_type(change_type) \
        .entity_urn(dataflow_urn) \
        .aspect_name(aspect_name) \
        .aspect(aspect_data) \
        .build()


def create_lineage_mcp(
    downstream_urn: str,
    upstream_urns: List[str],
    change_type: ChangeType = ChangeType.UPSERT
) -> MetadataChangeProposal:
    """Create a lineage MCP."""
    aspect_data = {
        "upstreams": [
            {
                "dataset": upstream_urn,
                "type": "COPY"
            }
            for upstream_urn in upstream_urns
        ]
    }
    
    return MCPBuilder() \
        .entity_type(EntityType.DATASET) \
        .change_type(change_type) \
        .entity_urn(downstream_urn) \
        .aspect_name("upstreamLineage") \
        .aspect(aspect_data) \
        .build()


def create_schema_mcp(
    dataset_urn: str,
    schema_data: Dict[str, Any],
    change_type: ChangeType = ChangeType.UPSERT
) -> MetadataChangeProposal:
    """Create a schema metadata MCP."""
    return MCPBuilder() \
        .entity_type(EntityType.DATASET) \
        .change_type(change_type) \
        .entity_urn(dataset_urn) \
        .aspect_name("schemaMetadata") \
        .aspect(schema_data) \
        .build()


class BatchedMCPEmitter:
    """Batched MCP emitter for efficient metadata publishing."""
    
    def __init__(self, batch_size: int = 100):
        self.batch_size = batch_size
        self.batch: List[MetadataChangeProposal] = []
        self.logger = logging.getLogger(__name__)
    
    def add_mcp(self, mcp: MetadataChangeProposal) -> None:
        """Add an MCP to the current batch."""
        self.batch.append(mcp)
        if len(self.batch) >= self.batch_size:
            self.flush()
    
    def flush(self) -> None:
        """Flush the current batch."""
        if self.batch:
            self.logger.info(f"Flushing batch of {len(self.batch)} MCPs")
            # In a real implementation, this would send to the metadata service
            self.batch.clear()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.flush()


# Export all classes and functions
__all__ = [
    'ChangeType',
    'EntityType',
    'AspectType',
    'MetadataAspect',
    'SystemMetadata',
    'MetadataChangeProposal',
    'MetadataChangeProposalWrapper',
    'MetadataChangeEvent',
    'MCPBuilder',
    'BatchedMCPEmitter',
    'create_dataset_mcp',
    'create_datajob_mcp',
    'create_dataflow_mcp',
    'create_lineage_mcp',
    'create_schema_mcp',
]