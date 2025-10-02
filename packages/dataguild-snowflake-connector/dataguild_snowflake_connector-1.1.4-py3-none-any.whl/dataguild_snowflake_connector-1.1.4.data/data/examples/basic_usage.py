#!/usr/bin/env python3
"""
DataGuild Snowflake Connector - Basic Usage Example
===================================================

This example demonstrates how to use the DataGuild Snowflake Connector
for basic metadata extraction from a Snowflake database.

Prerequisites:
1. Install the package: pip install dataguild-snowflake-connector
2. Configure snowflake_config.yml with your Snowflake credentials
3. Ensure you have appropriate permissions on your Snowflake account

Usage:
    python basic_usage.py
"""

import asyncio
import logging
import sys
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

try:
    from dataguild.source.snowflake.main import SnowflakeV2Source
    from dataguild.source.snowflake.config import SnowflakeV2Config
    from dataguild.api.common import PipelineContext
    from dataguild.utilities.performance_monitor import PerformanceMonitor
except ImportError as e:
    logger.error(f"Failed to import DataGuild modules: {e}")
    logger.error("Please install the package: pip install dataguild-snowflake-connector")
    sys.exit(1)


async def basic_metadata_extraction():
    """
    Basic metadata extraction example.
    """
    logger.info("🚀 Starting DataGuild Snowflake Connector - Basic Usage")
    
    try:
        # Load configuration
        config_path = Path("snowflake_config.yml")
        if not config_path.exists():
            logger.error(f"Configuration file not found: {config_path}")
            logger.error("Please create snowflake_config.yml with your Snowflake credentials")
            return False
        
        config = SnowflakeV2Config.from_yaml(str(config_path))
        logger.info("✅ Configuration loaded successfully")
        
        # Create pipeline context
        ctx = PipelineContext(pipeline_name="basic_metadata_extraction")
        logger.info("✅ Pipeline context created")
        
        # Initialize performance monitor
        monitor = PerformanceMonitor()
        
        # Initialize source
        source = SnowflakeV2Source(ctx, config)
        logger.info("✅ Snowflake source initialized")
        
        # Extract metadata
        logger.info("🔍 Starting metadata extraction...")
        extracted_count = 0
        
        with monitor.timer("metadata_extraction"):
            async for work_unit in source.get_workunits():
                extracted_count += 1
                
                # Log basic information about each entity
                entity = work_unit.entity
                logger.info(f"📊 Extracted: {entity.name} (Type: {entity.type})")
                
                if hasattr(entity, 'description') and entity.description:
                    logger.info(f"   Description: {entity.description[:100]}...")
                
                # Log every 10 entities to avoid spam
                if extracted_count % 10 == 0:
                    logger.info(f"📈 Progress: {extracted_count} entities extracted")
        
        # Get performance metrics
        metrics = monitor.get_metrics("metadata_extraction")
        logger.info("📊 Extraction completed!")
        logger.info(f"   Total entities: {extracted_count}")
        logger.info(f"   Average time per entity: {metrics.get_average_time():.3f}s")
        logger.info(f"   Total extraction time: {metrics.total_time:.3f}s")
        
        return True
        
    except Exception as e:
        logger.error(f"❌ Extraction failed: {e}")
        logger.exception("Full error details:")
        return False


async def advanced_metadata_extraction():
    """
    Advanced metadata extraction with AI intelligence.
    """
    logger.info("🤖 Starting Advanced Metadata Extraction with AI Intelligence")
    
    try:
        from dataguild.ai.intelligent_extractor import DataGuildIntelligentExtractor
        from dataguild.ai.gemma_client import GemmaConfig
        
        # Load configuration
        config = SnowflakeV2Config.from_yaml("snowflake_config.yml")
        
        # Enable AI intelligence
        config.enable_ai_intelligence = True
        logger.info("✅ AI intelligence enabled")
        
        # Create pipeline context
        ctx = PipelineContext(pipeline_name="ai_powered_extraction")
        
        # Initialize AI extractor (if API key is available)
        ai_extractor = None
        if hasattr(config, 'ai_api_key') and config.ai_api_key:
            ai_config = GemmaConfig(
                model_name="gemma-7b-it",
                api_key=config.ai_api_key,
                max_tokens=2048
            )
            ai_extractor = DataGuildIntelligentExtractor(ai_config)
            logger.info("✅ AI extractor initialized")
        else:
            logger.warning("⚠️  AI API key not configured, skipping AI features")
        
        # Initialize source
        source = SnowflakeV2Source(ctx, config)
        
        # Extract metadata with AI enhancement
        extracted_count = 0
        ai_enhanced_count = 0
        
        async for work_unit in source.get_workunits():
            extracted_count += 1
            
            # Basic extraction
            entity = work_unit.entity
            logger.info(f"📊 Extracted: {entity.name} (Type: {entity.type})")
            
            # AI enhancement (if available)
            if ai_extractor:
                try:
                    enhanced_metadata = await ai_extractor.enhance_metadata(work_unit)
                    ai_enhanced_count += 1
                    
                    if hasattr(enhanced_metadata.entity, 'ai_description'):
                        logger.info(f"🤖 AI Description: {enhanced_metadata.entity.ai_description[:100]}...")
                    
                    if hasattr(enhanced_metadata.entity, 'data_classification'):
                        logger.info(f"🏷️  Data Classification: {enhanced_metadata.entity.data_classification}")
                        
                except Exception as e:
                    logger.warning(f"⚠️  AI enhancement failed for {entity.name}: {e}")
            
            # Limit for demo
            if extracted_count >= 20:
                logger.info("🛑 Demo limit reached (20 entities)")
                break
        
        logger.info("📊 Advanced extraction completed!")
        logger.info(f"   Total entities: {extracted_count}")
        logger.info(f"   AI enhanced: {ai_enhanced_count}")
        
        return True
        
    except ImportError:
        logger.warning("⚠️  AI modules not available, skipping advanced example")
        return True
    except Exception as e:
        logger.error(f"❌ Advanced extraction failed: {e}")
        logger.exception("Full error details:")
        return False


async def rest_api_integration_example():
    """
    Example of integrating with REST API for metadata emission.
    """
    logger.info("🌐 Starting REST API Integration Example")
    
    try:
        from dataguild.emitter.dataguild_rest_emitter import DataGuildRestEmitter, DataGuildRestEmitterConfig
        from dataguild.emitter.mcp import MetadataChangeProposal, AspectType
        
        # Configure REST emitter
        rest_config = DataGuildRestEmitterConfig(
            server_url="https://api.dataguild.com",
            token="your-api-token",  # Replace with actual token
            batch_size=100,
            retry_max_times=3,
            timeout_sec=30.0
        )
        
        # Initialize emitter
        emitter = DataGuildRestEmitter(rest_config)
        logger.info("✅ REST emitter configured")
        
        # Create sample metadata change proposal
        mcp = MetadataChangeProposal(
            entityType="dataset",
            changeType="UPSERT",
            entityUrn="urn:li:dataset:(snowflake,PROD_DB.PUBLIC.CUSTOMERS,PROD)",
            aspectName=AspectType.DATASET_PROPERTIES.value,
            aspect={
                "name": "CUSTOMERS",
                "description": "Customer data table with PII information",
                "customProperties": {
                    "owner": "data-team@company.com",
                    "pii": "true",
                    "retention_days": "2555",
                    "data_classification": "confidential"
                }
            }
        )
        
        logger.info("📤 Sample MCP created")
        logger.info(f"   Entity: {mcp.entityUrn}")
        logger.info(f"   Aspect: {mcp.aspectName}")
        
        # Note: Actual emission would require valid API credentials
        logger.info("ℹ️  To emit to REST API, configure valid credentials in rest_config")
        
        return True
        
    except Exception as e:
        logger.error(f"❌ REST API integration example failed: {e}")
        logger.exception("Full error details:")
        return False


async def main():
    """
    Main function to run all examples.
    """
    logger.info("=" * 60)
    logger.info("🚀 DataGuild Snowflake Connector - Examples")
    logger.info("=" * 60)
    
    # Run basic extraction
    logger.info("\n" + "=" * 40)
    logger.info("📊 BASIC METADATA EXTRACTION")
    logger.info("=" * 40)
    
    basic_success = await basic_metadata_extraction()
    
    if basic_success:
        logger.info("✅ Basic extraction completed successfully")
    else:
        logger.error("❌ Basic extraction failed")
        return False
    
    # Run advanced extraction
    logger.info("\n" + "=" * 40)
    logger.info("🤖 ADVANCED AI-POWERED EXTRACTION")
    logger.info("=" * 40)
    
    advanced_success = await advanced_metadata_extraction()
    
    if advanced_success:
        logger.info("✅ Advanced extraction completed successfully")
    else:
        logger.warning("⚠️  Advanced extraction had issues")
    
    # Run REST API integration example
    logger.info("\n" + "=" * 40)
    logger.info("🌐 REST API INTEGRATION EXAMPLE")
    logger.info("=" * 40)
    
    rest_success = await rest_api_integration_example()
    
    if rest_success:
        logger.info("✅ REST API integration example completed")
    else:
        logger.warning("⚠️  REST API integration example had issues")
    
    # Summary
    logger.info("\n" + "=" * 60)
    logger.info("📊 SUMMARY")
    logger.info("=" * 60)
    logger.info(f"Basic Extraction: {'✅ Success' if basic_success else '❌ Failed'}")
    logger.info(f"Advanced Extraction: {'✅ Success' if advanced_success else '⚠️  Issues'}")
    logger.info(f"REST API Example: {'✅ Success' if rest_success else '⚠️  Issues'}")
    
    if basic_success:
        logger.info("\n🎉 DataGuild Snowflake Connector is working correctly!")
        logger.info("📚 For more examples, visit: https://dataguild-snowflake.readthedocs.io")
        return True
    else:
        logger.error("\n❌ Please check your configuration and try again")
        return False


if __name__ == "__main__":
    # Run the examples
    success = asyncio.run(main())
    sys.exit(0 if success else 1)
