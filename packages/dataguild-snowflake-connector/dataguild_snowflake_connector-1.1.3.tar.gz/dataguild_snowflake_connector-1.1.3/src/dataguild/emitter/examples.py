"""
DataGuild Emitter Examples

Comprehensive examples demonstrating how to use the DataGuild emitter system
for various use cases and scenarios.
"""

import json
import logging
from datetime import datetime
from typing import Dict, List, Optional, Any

from dataguild.emitter.advanced_emitter import (
    EmitterConfig,
    EmitMode,
    create_rest_emitter,
    create_kafka_emitter,
    create_composite_emitter,
    create_batched_emitter,
)
from dataguild.emitter.enhanced_mcp_builder import (
    EnhancedMCPBuilder,
    MCPBuilderConfig,
    ValidationLevel,
    create_enhanced_mcp,
    create_dataset_mcp,
    create_container_mcp,
)
from dataguild.emitter.emitter_factory import (
    EmitterFactory,
    EmitterType,
    create_emitter,
    create_emitter_from_config,
)
from dataguild.emitter.mcp import (
    AspectType,
    MetadataAspect,
    MetadataChangeProposalWrapper,
)

logger = logging.getLogger(__name__)


class DatasetPropertiesAspect(MetadataAspect):
    """Example dataset properties aspect."""
    
    def __init__(self, description: str, tags: List[str], custom_properties: Dict[str, str]):
        self.description = description
        self.tags = tags
        self.custom_properties = custom_properties
    
    def aspect_name(self) -> str:
        return AspectType.DATASET_PROPERTIES.value
    
    def validate(self) -> bool:
        return bool(self.description and self.tags)
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "description": self.description,
            "tags": self.tags,
            "customProperties": self.custom_properties,
        }


class SchemaMetadataAspect(MetadataAspect):
    """Example schema metadata aspect."""
    
    def __init__(self, fields: List[Dict[str, Any]]):
        self.fields = fields
    
    def aspect_name(self) -> str:
        return AspectType.SCHEMA_METADATA.value
    
    def validate(self) -> bool:
        return bool(self.fields)
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "fields": self.fields,
        }


def example_basic_rest_emitter():
    """Example: Basic REST emitter usage."""
    print("=== Basic REST Emitter Example ===")
    
    # Create emitter configuration
    config = EmitterConfig(
        server_url="http://localhost:8080",
        token="your-token-here",
        batch_size=50,
        timeout_sec=30.0,
    )
    
    # Create emitter
    emitter = create_rest_emitter(config)
    
    # Create a sample workunit
    aspect = DatasetPropertiesAspect(
        description="Sample dataset",
        tags=["sample", "test"],
        custom_properties={"owner": "data-team"}
    )
    
    workunit = create_enhanced_mcp(
        entity_urn="urn:li:dataset:(urn:li:dataPlatform:snowflake,sample_db.sample_schema.sample_table,PROD)",
        aspect=aspect,
        change_type="UPSERT"
    )
    
    # Emit the workunit
    def callback(result):
        print(f"Emit result: {result.status} - {result.message}")
    
    emitter.emit(workunit, callback)
    emitter.flush()
    emitter.close()
    
    print("Basic REST emitter example completed")


def example_kafka_emitter():
    """Example: Kafka emitter usage."""
    print("=== Kafka Emitter Example ===")
    
    # Create emitter configuration
    config = EmitterConfig(
        server_url="kafka://localhost:9092",
        batch_size=100,
    )
    
    # Create Kafka configuration
    kafka_config = {
        "bootstrap.servers": "localhost:9092",
        "topic": "dataguild-metadata",
        "security.protocol": "PLAINTEXT",
    }
    
    # Create emitter
    emitter = create_kafka_emitter(config, kafka_config)
    
    # Create sample workunits
    workunits = []
    for i in range(5):
        aspect = DatasetPropertiesAspect(
            description=f"Dataset {i}",
            tags=[f"tag-{i}"],
            custom_properties={"index": str(i)}
        )
        
        workunit = create_enhanced_mcp(
            entity_urn=f"urn:li:dataset:(urn:li:dataPlatform:snowflake,db.schema.table_{i},PROD)",
            aspect=aspect,
            change_type="UPSERT"
        )
        workunits.append(workunit)
    
    # Emit batch
    results = emitter.emit_batch(workunits)
    print(f"Emitted {len(results)} workunits to Kafka")
    
    emitter.close()
    print("Kafka emitter example completed")


def example_composite_emitter():
    """Example: Composite emitter with multiple backends."""
    print("=== Composite Emitter Example ===")
    
    # Create REST emitter
    rest_config = EmitterConfig(
        server_url="http://localhost:8080",
        token="your-token-here",
    )
    rest_emitter = create_rest_emitter(rest_config)
    
    # Create Kafka emitter
    kafka_config = EmitterConfig(server_url="kafka://localhost:9092")
    kafka_emitter_config = {
        "bootstrap.servers": "localhost:9092",
        "topic": "dataguild-metadata",
    }
    kafka_emitter = create_kafka_emitter(kafka_config, kafka_emitter_config)
    
    # Create composite emitter
    composite_emitter = create_composite_emitter([rest_emitter, kafka_emitter])
    
    # Create and emit workunit
    aspect = DatasetPropertiesAspect(
        description="Composite emitter test",
        tags=["composite", "test"],
        custom_properties={"emitter": "composite"}
    )
    
    workunit = create_enhanced_mcp(
        entity_urn="urn:li:dataset:(urn:li:dataPlatform:snowflake,composite.test,PROD)",
        aspect=aspect,
        change_type="UPSERT"
    )
    
    composite_emitter.emit(workunit)
    composite_emitter.flush()
    composite_emitter.close()
    
    print("Composite emitter example completed")


def example_batched_emitter():
    """Example: Batched emitter with intelligent batching."""
    print("=== Batched Emitter Example ===")
    
    # Create base emitter
    base_config = EmitterConfig(
        server_url="http://localhost:8080",
        token="your-token-here",
    )
    base_emitter = create_rest_emitter(base_config)
    
    # Create batched emitter
    batched_config = EmitterConfig(
        server_url="http://localhost:8080",
        batch_size=10,
        batch_timeout_sec=2.0,
    )
    batched_emitter = create_batched_emitter(batched_config, base_emitter)
    
    # Create multiple workunits
    workunits = []
    for i in range(25):
        aspect = DatasetPropertiesAspect(
            description=f"Batched dataset {i}",
            tags=[f"batch-{i // 10}"],
            custom_properties={"batch_id": str(i // 10)}
        )
        
        workunit = create_enhanced_mcp(
            entity_urn=f"urn:li:dataset:(urn:li:dataPlatform:snowflake,batch.schema.table_{i},PROD)",
            aspect=aspect,
            change_type="UPSERT",
            batch_id=f"batch-{i // 10}"
        )
        workunits.append(workunit)
    
    # Emit workunits (they will be automatically batched)
    for workunit in workunits:
        batched_emitter.emit(workunit)
    
    # Flush remaining workunits
    batched_emitter.flush()
    batched_emitter.close()
    
    print("Batched emitter example completed")


def example_dataset_workflow():
    """Example: Complete dataset metadata workflow."""
    print("=== Dataset Workflow Example ===")
    
    # Create emitter
    config = EmitterConfig(
        server_url="http://localhost:8080",
        token="your-token-here",
        batch_size=50,
    )
    emitter = create_rest_emitter(config)
    
    # Create MCP builder with enhanced configuration
    builder_config = MCPBuilderConfig(
        validation_level=ValidationLevel.STRICT,
        enable_caching=True,
        enable_metrics=True,
    )
    mcp_builder = EnhancedMCPBuilder(builder_config)
    
    # 1. Create container (schema) metadata
    container_aspect = DatasetPropertiesAspect(
        description="Sales schema containing customer and order data",
        tags=["sales", "customer", "orders"],
        custom_properties={"department": "sales", "owner": "sales-team"}
    )
    
    container_workunit = mcp_builder.create_container_mcp(
        platform="snowflake",
        database_name="SALES_DB",
        schema_name="CUSTOMER_DATA",
        aspect=container_aspect,
        change_type="UPSERT"
    )
    
    # 2. Create dataset (table) metadata
    dataset_aspect = DatasetPropertiesAspect(
        description="Customer information table",
        tags=["customer", "pii", "sales"],
        custom_properties={"table_type": "fact", "refresh_frequency": "daily"}
    )
    
    dataset_workunit = mcp_builder.create_dataset_mcp(
        platform="snowflake",
        database_name="SALES_DB",
        schema_name="CUSTOMER_DATA",
        table_name="CUSTOMERS",
        aspect=dataset_aspect,
        change_type="UPSERT"
    )
    
    # 3. Create schema metadata
    schema_fields = [
        {
            "fieldPath": "customer_id",
            "type": "NUMBER",
            "nativeDataType": "NUMBER(38,0)",
            "description": "Unique customer identifier",
            "tags": ["primary_key", "identifier"]
        },
        {
            "fieldPath": "first_name",
            "type": "STRING",
            "nativeDataType": "VARCHAR(100)",
            "description": "Customer first name",
            "tags": ["pii", "name"]
        },
        {
            "fieldPath": "last_name",
            "type": "STRING",
            "nativeDataType": "VARCHAR(100)",
            "description": "Customer last name",
            "tags": ["pii", "name"]
        },
        {
            "fieldPath": "email",
            "type": "STRING",
            "nativeDataType": "VARCHAR(255)",
            "description": "Customer email address",
            "tags": ["pii", "contact"]
        },
        {
            "fieldPath": "created_at",
            "type": "TIMESTAMP",
            "nativeDataType": "TIMESTAMP_NTZ",
            "description": "Record creation timestamp",
            "tags": ["audit", "timestamp"]
        }
    ]
    
    schema_aspect = SchemaMetadataAspect(fields=schema_fields)
    
    schema_workunit = mcp_builder.create_dataset_mcp(
        platform="snowflake",
        database_name="SALES_DB",
        schema_name="CUSTOMER_DATA",
        table_name="CUSTOMERS",
        aspect=schema_aspect,
        change_type="UPSERT"
    )
    
    # 4. Create field-level metadata
    field_workunits = []
    for field in schema_fields:
        field_aspect = DatasetPropertiesAspect(
            description=field["description"],
            tags=field["tags"],
            custom_properties={
                "data_type": field["type"],
                "native_data_type": field["nativeDataType"]
            }
        )
        
        field_workunit = mcp_builder.create_schema_field_mcp(
            dataset_urn=dataset_workunit.mcp.entityUrn,
            field_path=field["fieldPath"],
            aspect=field_aspect,
            change_type="UPSERT"
        )
        field_workunits.append(field_workunit)
    
    # 5. Emit all workunits
    all_workunits = [container_workunit, dataset_workunit, schema_workunit] + field_workunits
    
    def batch_callback(results):
        success_count = sum(1 for r in results if r.status.value == "success")
        print(f"Emitted {success_count}/{len(results)} workunits successfully")
    
    results = emitter.emit_batch(all_workunits, batch_callback)
    
    # 6. Get metrics
    metrics = mcp_builder.get_performance_metrics()
    print(f"MCP Builder metrics: {metrics}")
    
    emitter_metrics = emitter.get_metrics()
    print(f"Emitter metrics: {emitter_metrics}")
    
    emitter.close()
    print("Dataset workflow example completed")


def example_factory_usage():
    """Example: Using the emitter factory."""
    print("=== Emitter Factory Example ===")
    
    # Create emitter using factory
    emitter = create_emitter(
        EmitterType.REST,
        {
            "server_url": "http://localhost:8080",
            "token": "your-token-here",
            "batch_size": 100,
        }
    )
    
    # Create workunit
    aspect = DatasetPropertiesAspect(
        description="Factory-created dataset",
        tags=["factory", "test"],
        custom_properties={"created_by": "factory"}
    )
    
    workunit = create_enhanced_mcp(
        entity_urn="urn:li:dataset:(urn:li:dataPlatform:snowflake,factory.test,PROD)",
        aspect=aspect,
        change_type="UPSERT"
    )
    
    # Emit workunit
    emitter.emit(workunit)
    emitter.flush()
    emitter.close()
    
    print("Factory usage example completed")


def example_config_file_usage():
    """Example: Using configuration files."""
    print("=== Configuration File Example ===")
    
    # Create sample configuration file
    config_data = {
        "type": "rest",
        "config": {
            "server_url": "http://localhost:8080",
            "token": "your-token-here",
            "batch_size": 50,
            "timeout_sec": 30.0,
            "retry_max_times": 3,
        }
    }
    
    # Write configuration to file
    with open("emitter_config.json", "w") as f:
        json.dump(config_data, f, indent=2)
    
    # Create emitter from configuration file
    emitter = create_emitter_from_config("emitter_config.json")
    
    # Create and emit workunit
    aspect = DatasetPropertiesAspect(
        description="Config file dataset",
        tags=["config", "file"],
        custom_properties={"config_source": "file"}
    )
    
    workunit = create_enhanced_mcp(
        entity_urn="urn:li:dataset:(urn:li:dataPlatform:snowflake,config.test,PROD)",
        aspect=aspect,
        change_type="UPSERT"
    )
    
    emitter.emit(workunit)
    emitter.flush()
    emitter.close()
    
    print("Configuration file example completed")


def example_error_handling():
    """Example: Error handling and retry logic."""
    print("=== Error Handling Example ===")
    
    # Create emitter with retry configuration
    config = EmitterConfig(
        server_url="http://invalid-server:8080",  # Invalid server for testing
        timeout_sec=5.0,
        retry_max_times=2,
        retry_backoff_factor=1.0,
    )
    emitter = create_rest_emitter(config)
    
    # Create workunit
    aspect = DatasetPropertiesAspect(
        description="Error handling test",
        tags=["error", "test"],
        custom_properties={"test_type": "error_handling"}
    )
    
    workunit = create_enhanced_mcp(
        entity_urn="urn:li:dataset:(urn:li:dataPlatform:snowflake,error.test,PROD)",
        aspect=aspect,
        change_type="UPSERT"
    )
    
    # Define error callback
    def error_callback(result):
        if result.error:
            print(f"Error occurred: {result.error}")
            print(f"Status: {result.status}")
            print(f"Message: {result.message}")
        else:
            print(f"Success: {result.message}")
    
    # Emit workunit (will fail due to invalid server)
    emitter.emit(workunit, error_callback)
    emitter.close()
    
    print("Error handling example completed")


def main():
    """Run all examples."""
    print("DataGuild Emitter Examples")
    print("=" * 50)
    
    try:
        example_basic_rest_emitter()
        print()
        
        example_kafka_emitter()
        print()
        
        example_composite_emitter()
        print()
        
        example_batched_emitter()
        print()
        
        example_dataset_workflow()
        print()
        
        example_factory_usage()
        print()
        
        example_config_file_usage()
        print()
        
        example_error_handling()
        print()
        
        print("All examples completed successfully!")
        
    except Exception as e:
        print(f"Example failed: {e}")
        logger.exception("Example execution failed")


if __name__ == "__main__":
    main()
