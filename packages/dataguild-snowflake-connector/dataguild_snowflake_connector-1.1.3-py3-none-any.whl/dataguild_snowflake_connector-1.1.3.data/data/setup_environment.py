#!/usr/bin/env python3
"""
DataGuild Snowflake Connector - Environment Setup Script
========================================================

This script helps set up the environment for the DataGuild Snowflake Connector,
including dependency installation, configuration validation, and testing.

Usage:
    python setup_environment.py [--install] [--test] [--validate]
"""

import argparse
import asyncio
import logging
import subprocess
import sys
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def check_python_version():
    """Check if Python version is compatible."""
    logger.info("🐍 Checking Python version...")
    
    if sys.version_info < (3, 8):
        logger.error(f"❌ Python 3.8+ required, found {sys.version}")
        return False
    
    logger.info(f"✅ Python {sys.version.split()[0]} is compatible")
    return True

def install_dependencies():
    """Install required dependencies."""
    logger.info("📦 Installing dependencies...")
    
    try:
        # Install the package
        subprocess.run([sys.executable, "-m", "pip", "install", "dataguild-snowflake-connector"], 
                      check=True, capture_output=True, text=True)
        logger.info("✅ Package installed successfully")
        
        # Install additional dependencies for examples
        additional_deps = [
            "pytest>=6.0.0",
            "pytest-asyncio>=0.18.0",
            "jupyter>=1.0.0",
            "notebook>=6.0.0"
        ]
        
        for dep in additional_deps:
            try:
                subprocess.run([sys.executable, "-m", "pip", "install", dep], 
                              check=True, capture_output=True, text=True)
                logger.info(f"✅ Installed: {dep}")
            except subprocess.CalledProcessError:
                logger.warning(f"⚠️  Failed to install: {dep}")
        
        return True
        
    except subprocess.CalledProcessError as e:
        logger.error(f"❌ Installation failed: {e}")
        return False

def create_directories():
    """Create necessary directories."""
    logger.info("📁 Creating directories...")
    
    directories = [
        "examples",
        "logs",
        "data",
        "config"
    ]
    
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        logger.info(f"✅ Created: {directory}/")
    
    return True

def create_sample_files():
    """Create sample configuration and example files."""
    logger.info("📝 Creating sample files...")
    
    # Sample configuration
    config_path = Path("snowflake_config.yml")
    if not config_path.exists():
        config_content = """# DataGuild Snowflake Connector Configuration
account_id: your-account.snowflakecomputing.com
username: your-username
password: your-password
warehouse: your-warehouse
database: your-database
role: your-role

# Connection settings
connection_timeout: 300
query_timeout: 600
max_workers: 4

# Extraction settings
include_tables_bool: true
include_views: true
include_procedures: true
include_streams: true
include_tags: true
include_usage_stats: true
include_table_lineage: true
include_column_lineage: true

# Database filtering
database_pattern:
  allow:
    - PRODUCTION_DB
    - STAGING_DB
  deny:
    - SNOWFLAKE.*
  ignoreCase: true

# Schema filtering
schema_pattern:
  allow:
    - PUBLIC
    - ANALYTICS
  deny:
    - INFORMATION_SCHEMA
  ignoreCase: true

# AI settings
enable_ai_intelligence: false
performance_monitoring: true
warn_no_datasets: false
"""
        with open(config_path, 'w') as f:
            f.write(config_content)
        logger.info("✅ Created: snowflake_config.yml")
    
    # Sample test script
    test_script = Path("test_connection.py")
    if not test_script.exists():
        test_content = """#!/usr/bin/env python3
\"\"\"
Test script for DataGuild Snowflake Connector
\"\"\"

import asyncio
import logging
from dataguild.source.snowflake.main import SnowflakeV2Source
from dataguild.source.snowflake.config import SnowflakeV2Config
from dataguild.api.common import PipelineContext

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def test():
    try:
        config = SnowflakeV2Config.from_yaml("snowflake_config.yml")
        ctx = PipelineContext(pipeline_name="test")
        source = SnowflakeV2Source(ctx, config)
        
        count = 0
        async for work_unit in source.get_workunits():
            count += 1
            logger.info(f"Found: {work_unit.entity.name}")
            if count >= 3:
                break
        
        logger.info(f"✅ Test successful! Found {count} entities")
        return True
    except Exception as e:
        logger.error(f"❌ Test failed: {e}")
        return False

if __name__ == "__main__":
    asyncio.run(test())
"""
        with open(test_script, 'w') as f:
            f.write(test_content)
        test_script.chmod(0o755)  # Make executable
        logger.info("✅ Created: test_connection.py")
    
    return True

def validate_configuration():
    """Validate the configuration file."""
    logger.info("🔍 Validating configuration...")
    
    config_path = Path("snowflake_config.yml")
    if not config_path.exists():
        logger.error("❌ Configuration file not found: snowflake_config.yml")
        return False
    
    try:
        from dataguild.source.snowflake.config import SnowflakeV2Config
        config = SnowflakeV2Config.from_yaml(str(config_path))
        logger.info("✅ Configuration file is valid")
        
        # Check required fields
        required_fields = ['account_id', 'username', 'password', 'warehouse', 'database']
        missing_fields = []
        
        for field in required_fields:
            if not getattr(config, field, None):
                missing_fields.append(field)
        
        if missing_fields:
            logger.warning(f"⚠️  Missing required fields: {', '.join(missing_fields)}")
            logger.warning("Please edit snowflake_config.yml with your Snowflake credentials")
        else:
            logger.info("✅ All required fields are present")
        
        return True
        
    except Exception as e:
        logger.error(f"❌ Configuration validation failed: {e}")
        return False

async def test_connection():
    """Test the Snowflake connection."""
    logger.info("🔌 Testing Snowflake connection...")
    
    try:
        from dataguild.source.snowflake.main import SnowflakeV2Source
        from dataguild.source.snowflake.config import SnowflakeV2Config
        from dataguild.api.common import PipelineContext
        
        config = SnowflakeV2Config.from_yaml("snowflake_config.yml")
        ctx = PipelineContext(pipeline_name="setup_test")
        source = SnowflakeV2Source(ctx, config)
        
        # Test connection
        count = 0
        async for work_unit in source.get_workunits():
            count += 1
            if count >= 1:  # Just test one entity
                break
        
        logger.info("✅ Connection test successful")
        return True
        
    except Exception as e:
        logger.error(f"❌ Connection test failed: {e}")
        logger.error("Please check your Snowflake credentials in snowflake_config.yml")
        return False

def run_tests():
    """Run the test suite."""
    logger.info("🧪 Running tests...")
    
    try:
        # Run basic import test
        subprocess.run([sys.executable, "-c", 
                       "import dataguild; print(f'Package version: {dataguild.__version__}')"], 
                      check=True, capture_output=True, text=True)
        logger.info("✅ Import test passed")
        
        # Run configuration test
        if validate_configuration():
            logger.info("✅ Configuration test passed")
        else:
            logger.warning("⚠️  Configuration test failed")
        
        return True
        
    except subprocess.CalledProcessError as e:
        logger.error(f"❌ Tests failed: {e}")
        return False

def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="DataGuild Snowflake Connector Setup")
    parser.add_argument("--install", action="store_true", help="Install dependencies")
    parser.add_argument("--test", action="store_true", help="Run tests")
    parser.add_argument("--validate", action="store_true", help="Validate configuration")
    parser.add_argument("--all", action="store_true", help="Run all setup steps")
    
    args = parser.parse_args()
    
    logger.info("🚀 DataGuild Snowflake Connector - Environment Setup")
    logger.info("=" * 60)
    
    success = True
    
    # Check Python version
    if not check_python_version():
        success = False
    
    # Install dependencies
    if args.install or args.all:
        if not install_dependencies():
            success = False
    
    # Create directories and files
    if args.all:
        create_directories()
        create_sample_files()
    
    # Validate configuration
    if args.validate or args.all:
        if not validate_configuration():
            success = False
    
    # Run tests
    if args.test or args.all:
        if not run_tests():
            success = False
    
    # Summary
    logger.info("\n" + "=" * 60)
    if success:
        logger.info("🎉 Setup completed successfully!")
        logger.info("\n📚 Next steps:")
        logger.info("   1. Edit snowflake_config.yml with your credentials")
        logger.info("   2. Run: python test_connection.py")
        logger.info("   3. Run: python examples/basic_usage.py")
        logger.info("   4. Visit: https://dataguild-snowflake.readthedocs.io")
    else:
        logger.error("❌ Setup completed with errors")
        logger.error("Please check the logs above and fix any issues")
    
    return success

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
