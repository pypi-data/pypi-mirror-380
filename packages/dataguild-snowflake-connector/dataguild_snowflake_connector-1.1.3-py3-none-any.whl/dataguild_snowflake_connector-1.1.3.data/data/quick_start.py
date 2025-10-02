#!/usr/bin/env python3
"""
DataGuild Snowflake Connector - Quick Start Script
==================================================

This script provides a quick way to test the DataGuild Snowflake Connector
with minimal configuration.

Usage:
    python quick_start.py
"""

import asyncio
import logging
import sys
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def create_sample_config():
    """Create a sample configuration file."""
    config_content = """# DataGuild Snowflake Connector - Sample Configuration
# Replace these values with your actual Snowflake credentials

account_id: your-account.snowflakecomputing.com
username: your-username
password: your-password
warehouse: your-warehouse
database: your-database
role: your-role

# Basic settings
connection_timeout: 300
query_timeout: 600
max_workers: 2

# What to extract
include_tables_bool: true
include_views: true
include_procedures: false
include_streams: false
include_tags: true
include_usage_stats: false
include_table_lineage: true
include_column_lineage: true

# Database filtering
database_pattern:
  allow:
    - YOUR_DATABASE
  deny:
    - SNOWFLAKE.*
  ignoreCase: true

# Schema filtering
schema_pattern:
  allow:
    - PUBLIC
  deny:
    - INFORMATION_SCHEMA
  ignoreCase: true

# AI settings
enable_ai_intelligence: false
performance_monitoring: true
warn_no_datasets: false
"""
    
    config_path = Path("snowflake_config.yml")
    if not config_path.exists():
        with open(config_path, 'w') as f:
            f.write(config_content)
        logger.info(f"✅ Created sample configuration: {config_path}")
        logger.info("📝 Please edit snowflake_config.yml with your Snowflake credentials")
        return True
    else:
        logger.info(f"✅ Configuration file already exists: {config_path}")
        return True

async def test_connection():
    """Test the Snowflake connection."""
    try:
        from dataguild.source.snowflake.main import SnowflakeV2Source
        from dataguild.source.snowflake.config import SnowflakeV2Config
        from dataguild.api.common import PipelineContext
        
        logger.info("🔍 Testing Snowflake connection...")
        
        # Load configuration
        config = SnowflakeV2Config.from_yaml("snowflake_config.yml")
        
        # Create pipeline context
        ctx = PipelineContext(pipeline_name="quick_start_test")
        
        # Initialize source
        source = SnowflakeV2Source(ctx, config)
        
        # Test connection by extracting a few entities
        count = 0
        async for work_unit in source.get_workunits():
            count += 1
            entity = work_unit.entity
            logger.info(f"📊 Found: {entity.name} (Type: {entity.type})")
            
            # Limit to 5 entities for quick test
            if count >= 5:
                break
        
        logger.info(f"✅ Connection successful! Found {count} entities")
        return True
        
    except Exception as e:
        logger.error(f"❌ Connection failed: {e}")
        return False

async def main():
    """Main function."""
    logger.info("🚀 DataGuild Snowflake Connector - Quick Start")
    logger.info("=" * 50)
    
    # Check if package is installed
    try:
        import dataguild
        logger.info(f"✅ Package installed: dataguild-snowflake-connector v{dataguild.__version__}")
    except ImportError:
        logger.error("❌ Package not installed. Please run: pip install dataguild-snowflake-connector")
        return False
    
    # Create sample configuration
    if not create_sample_config():
        return False
    
    # Test connection
    if await test_connection():
        logger.info("\n🎉 Quick start completed successfully!")
        logger.info("📚 Next steps:")
        logger.info("   1. Edit snowflake_config.yml with your credentials")
        logger.info("   2. Run: python examples/basic_usage.py")
        logger.info("   3. Visit: https://dataguild-snowflake.readthedocs.io")
        return True
    else:
        logger.error("\n❌ Quick start failed. Please check your configuration.")
        return False

if __name__ == "__main__":
    success = asyncio.run(main())
    sys.exit(0 if success else 1)
