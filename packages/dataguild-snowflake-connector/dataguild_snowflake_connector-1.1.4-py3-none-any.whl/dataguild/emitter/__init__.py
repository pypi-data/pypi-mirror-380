"""
DataGuild Emitter System

Enterprise-grade emitter system for metadata ingestion with comprehensive
error handling, batching, retry logic, and observability features.

Inspired by DataHub's best practices and designed for high-performance
metadata processing in enterprise environments.
"""

# Core emitter classes
from .advanced_emitter import (
    # Enums
    EmitMode,
    EmitStatus,
    
    # Data classes
    EmitResult,
    EmitterConfig,
    
    # Protocols
    Emitter,
    
    # Base classes
    BaseEmitter,
    
    # Implementations
    DataGuildRestEmitter,
    DataGuildKafkaEmitter,
    CompositeEmitter,
    AdvancedBatchedEmitter,
    
    # Factory functions
    create_rest_emitter,
    create_kafka_emitter,
    create_composite_emitter,
    create_batched_emitter,
)

# Enhanced MCP builder
from .enhanced_mcp_builder import (
    # Enums
    ValidationLevel,
    
    # Data classes
    MCPBuilderConfig,
    
    # Main classes
    EnhancedMCPBuilder,
    
    # Convenience functions
    create_enhanced_mcp,
    create_dataset_mcp,
    create_container_mcp,
    create_schema_field_mcp,
)

# Emitter factory
from .emitter_factory import (
    # Enums
    EmitterType,
    
    # Data classes
    KafkaConfig,
    FileEmitterConfig,
    ConsoleEmitterConfig,
    
    # Main classes
    EmitterFactory,
    
    # Convenience functions
    create_emitter,
    create_emitter_from_config,
    create_mcp_builder,
    register_emitter,
    get_supported_emitter_types,
)

# Legacy MCP support
from .mcp import (
    AspectType,
    MetadataAspect,
    MetadataChangeProposal,
    MetadataChangeProposalWrapper,
    MetadataWorkUnit as MCPWorkUnit,
    BatchedMCPEmitter,
)

# MCP builders
from .mcp_builder import (
    EntityType,
    PlatformType,
    DatabaseKey,
    SchemaKey,
    AdvancedMCPBuilder,
    make_database_key,
    make_schema_key,
    make_data_platform_urn,
    make_dataset_urn_with_platform_instance,
    make_dataset_urn_from_keys,
    make_schema_field_urn,
    make_tag_urn,
    make_container_urn,
    make_container_urn_from_schema_key,
)

# MCE builders
from .mce_builder import (
    make_assertion_urn,
    make_data_platform_urn as make_data_platform_urn_mce,
    make_dataplatform_instance_urn,
    make_dataset_urn as make_dataset_urn_mce,
    make_dataset_urn_with_platform_instance as make_dataset_urn_with_platform_instance_mce,
    make_user_urn,
    make_group_urn,
    make_tag_urn as make_tag_urn_mce,
    make_domain_urn,
    make_container_urn as make_container_urn_mce,
    get_sys_time,
    validate_urn,
    extract_platform_from_dataset_urn,
    generate_hash_id,
    make_audit_stamp,
)

# Examples
from . import examples

# Version information
__version__ = "1.0.0"
__author__ = "DataGuild Team"
__email__ = "team@dataguild.io"

# Import typing for type hints
from typing import Optional

# Main exports
__all__ = [
    # Core emitter system
    "EmitMode",
    "EmitStatus", 
    "EmitResult",
    "EmitterConfig",
    "Emitter",
    "BaseEmitter",
    "DataGuildRestEmitter",
    "DataGuildKafkaEmitter",
    "CompositeEmitter",
    "AdvancedBatchedEmitter",
    
    # Factory functions
    "create_rest_emitter",
    "create_kafka_emitter", 
    "create_composite_emitter",
    "create_batched_emitter",
    
    # Enhanced MCP builder
    "ValidationLevel",
    "MCPBuilderConfig",
    "EnhancedMCPBuilder",
    "create_enhanced_mcp",
    "create_dataset_mcp",
    "create_container_mcp",
    "create_schema_field_mcp",
    
    # Emitter factory
    "EmitterType",
    "KafkaConfig",
    "FileEmitterConfig", 
    "ConsoleEmitterConfig",
    "EmitterFactory",
    "create_emitter",
    "create_emitter_from_config",
    "create_mcp_builder",
    "register_emitter",
    "get_supported_emitter_types",
    
    # Legacy MCP support
    "AspectType",
    "MetadataAspect",
    "MetadataChangeProposal",
    "MetadataChangeProposalWrapper",
    "MCPWorkUnit",
    "BatchedMCPEmitter",
    
    # MCP builders
    "EntityType",
    "PlatformType", 
    "DatabaseKey",
    "SchemaKey",
    "AdvancedMCPBuilder",
    "make_database_key",
    "make_schema_key",
    "make_data_platform_urn",
    "make_dataset_urn_with_platform_instance",
    "make_dataset_urn_from_keys",
    "make_schema_field_urn",
    "make_tag_urn",
    "make_container_urn",
    "make_container_urn_from_schema_key",
    
    # MCE builders
    "make_assertion_urn",
    "make_data_platform_urn_mce",
    "make_dataplatform_instance_urn",
    "make_dataset_urn_mce",
    "make_dataset_urn_with_platform_instance_mce",
    "make_user_urn",
    "make_group_urn",
    "make_tag_urn_mce",
    "make_domain_urn",
    "make_container_urn_mce",
    "get_sys_time",
    "validate_urn",
    "extract_platform_from_dataset_urn",
    "generate_hash_id",
    "make_audit_stamp",
    
    # Examples
    "examples",
    
    # Version info
    "__version__",
    "__author__",
    "__email__",
]


def get_version() -> str:
    """Get the current version of the DataGuild emitter system."""
    return __version__


def get_supported_platforms() -> list:
    """Get list of supported data platforms."""
    return [platform.value for platform in PlatformType]


def get_supported_entity_types() -> list:
    """Get list of supported entity types."""
    return [entity_type.value for entity_type in EntityType]


def get_supported_aspect_types() -> list:
    """Get list of supported aspect types."""
    return [aspect_type.value for aspect_type in AspectType]


def create_default_emitter(server_url: str, token: Optional[str] = None) -> Emitter:
    """
    Create a default emitter with sensible defaults.
    
    Args:
        server_url: URL of the DataGuild server
        token: Optional authentication token
        
    Returns:
        Configured emitter instance
    """
    config = EmitterConfig(
        server_url=server_url,
        token=token,
        batch_size=100,
        timeout_sec=30.0,
        retry_max_times=3,
    )
    return create_rest_emitter(config)


def create_default_mcp_builder() -> EnhancedMCPBuilder:
    """
    Create a default MCP builder with sensible defaults.
    
    Returns:
        Configured MCP builder instance
    """
    config = MCPBuilderConfig(
        validation_level=ValidationLevel.STRICT,
        enable_caching=True,
        enable_metrics=True,
    )
    return EnhancedMCPBuilder(config)


# Quick start functions
def quick_start_rest(server_url: str, token: Optional[str] = None) -> tuple[Emitter, EnhancedMCPBuilder]:
    """
    Quick start with REST emitter and MCP builder.
    
    Args:
        server_url: URL of the DataGuild server
        token: Optional authentication token
        
    Returns:
        Tuple of (emitter, mcp_builder)
    """
    emitter = create_default_emitter(server_url, token)
    mcp_builder = create_default_mcp_builder()
    return emitter, mcp_builder


def quick_start_kafka(
    bootstrap_servers: str,
    topic: str = "dataguild-metadata",
    token: Optional[str] = None
) -> tuple[Emitter, EnhancedMCPBuilder]:
    """
    Quick start with Kafka emitter and MCP builder.
    
    Args:
        bootstrap_servers: Kafka bootstrap servers
        topic: Kafka topic name
        token: Optional authentication token
        
    Returns:
        Tuple of (emitter, mcp_builder)
    """
    config = EmitterConfig(
        server_url="kafka://",
        token=token,
        batch_size=100,
    )
    kafka_config = {
        "bootstrap.servers": bootstrap_servers,
        "topic": topic,
    }
    emitter = create_kafka_emitter(config, kafka_config)
    mcp_builder = create_default_mcp_builder()
    return emitter, mcp_builder
