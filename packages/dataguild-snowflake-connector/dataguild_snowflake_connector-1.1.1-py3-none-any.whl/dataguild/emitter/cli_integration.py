"""
DataGuild Emitter CLI Integration

Enhanced CLI integration for DataGuild emitters with comprehensive
configuration, validation, and monitoring capabilities.
"""

import json
import logging
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

import click
import yaml
from click import Context, Option

from dataguild.api.workunit import MetadataWorkUnit
from dataguild.emitter.dataguild_rest_emitter import (
    DataGuildRestEmitter,
    DataGuildRestEmitterConfig,
    create_dataguild_rest_emitter
)
from dataguild.emitter.dataguild_kafka_emitter import (
    DataGuildKafkaEmitter,
    DataGuildKafkaEmitterConfig,
    create_dataguild_kafka_emitter
)
from dataguild.emitter.mcp import (
    MetadataChangeProposal,
    MetadataChangeProposalWrapper,
    MCPBuilder,
    create_dataset_mcp,
    create_lineage_mcp,
    create_schema_mcp
)

logger = logging.getLogger(__name__)


@dataclass
class EmitterConfig:
    """Unified emitter configuration."""
    emitter_type: str  # 'rest' or 'kafka'
    config: Union[DataGuildRestEmitterConfig, DataGuildKafkaEmitterConfig]
    output_file: Optional[str] = None
    batch_size: int = 100
    enable_validation: bool = True
    enable_monitoring: bool = True


class EmitterCLI:
    """Enhanced CLI for DataGuild emitters."""
    
    def __init__(self):
        self.emitter = None
        self.config = None
        self.stats = {
            "total_emitted": 0,
            "successful": 0,
            "failed": 0,
            "batches": 0
        }
    
    def load_config(self, config_file: str) -> EmitterConfig:
        """Load emitter configuration from file."""
        try:
            with open(config_file, 'r') as f:
                config_data = yaml.safe_load(f)
            
            emitter_type = config_data.get("emitter_type", "rest")
            
            if emitter_type == "rest":
                emitter_config = DataGuildRestEmitterConfig(
                    server_url=config_data["server_url"],
                    token=config_data.get("token"),
                    timeout_sec=config_data.get("timeout_sec", 30),
                    batch_size=config_data.get("batch_size", 100),
                    enable_tracing=config_data.get("enable_tracing", True)
                )
            elif emitter_type == "kafka":
                emitter_config = DataGuildKafkaEmitterConfig(
                    bootstrap_servers=config_data["bootstrap_servers"],
                    topic_name=config_data.get("topic_name", "dataguild-metadata"),
                    partition_count=config_data.get("partition_count", 3),
                    enable_avro_serialization=config_data.get("enable_avro_serialization", True)
                )
            else:
                raise ValueError(f"Unsupported emitter type: {emitter_type}")
            
            return EmitterConfig(
                emitter_type=emitter_type,
                config=emitter_config,
                output_file=config_data.get("output_file"),
                batch_size=config_data.get("batch_size", 100),
                enable_validation=config_data.get("enable_validation", True),
                enable_monitoring=config_data.get("enable_monitoring", True)
            )
            
        except Exception as e:
            logger.error(f"Failed to load configuration: {e}")
            raise
    
    def create_emitter(self, config: EmitterConfig):
        """Create emitter instance from configuration."""
        try:
            if config.emitter_type == "rest":
                self.emitter = DataGuildRestEmitter(config.config)
            elif config.emitter_type == "kafka":
                self.emitter = DataGuildKafkaEmitter(config.config)
            else:
                raise ValueError(f"Unsupported emitter type: {config.emitter_type}")
            
            self.config = config
            logger.info(f"✅ Created {config.emitter_type.upper()} emitter")
            
        except Exception as e:
            logger.error(f"❌ Failed to create emitter: {e}")
            raise
    
    def test_connection(self) -> bool:
        """Test emitter connection."""
        try:
            if hasattr(self.emitter, 'test_connection'):
                return self.emitter.test_connection()
            else:
                logger.warning("⚠️ Connection testing not supported for this emitter type")
                return True
        except Exception as e:
            logger.error(f"❌ Connection test failed: {e}")
            return False
    
    def emit_workunits(self, workunits: List[MetadataWorkUnit]) -> Dict[str, Any]:
        """Emit workunits using the configured emitter."""
        if not self.emitter:
            raise RuntimeError("Emitter not initialized")
        
        results = {
            "total": len(workunits),
            "successful": 0,
            "failed": 0,
            "errors": []
        }
        
        try:
            # Process in batches
            batch_size = self.config.batch_size
            for i in range(0, len(workunits), batch_size):
                batch = workunits[i:i + batch_size]
                batch_results = self._emit_batch(batch)
                
                # Update results
                for result in batch_results:
                    if result.success:
                        results["successful"] += 1
                    else:
                        results["failed"] += 1
                        results["errors"].append({
                            "workunit_id": result.workunit_id,
                            "error": str(result.error) if result.error else "Unknown error"
                        })
                
                self.stats["batches"] += 1
                logger.info(f"📦 Processed batch {i//batch_size + 1}: {len(batch)} workunits")
            
            self.stats["total_emitted"] += len(workunits)
            self.stats["successful"] += results["successful"]
            self.stats["failed"] += results["failed"]
            
            logger.info(f"✅ Emission complete: {results['successful']}/{results['total']} successful")
            
        except Exception as e:
            logger.error(f"❌ Emission failed: {e}")
            results["errors"].append({"error": str(e)})
        
        return results
    
    def _emit_batch(self, workunits: List[MetadataWorkUnit]) -> List[Any]:
        """Emit a batch of workunits."""
        try:
            if self.config.emitter_type == "rest":
                # Convert workunits to MCPs
                mcps = []
                for workunit in workunits:
                    if hasattr(workunit, 'mcp_raw') and workunit.mcp_raw:
                        mcp = self._workunit_to_mcp(workunit)
                        mcps.append(mcp)
                
                if mcps:
                    return self.emitter.emit_mcps_batch(mcps)
                else:
                    # Emit as raw workunits
                    return [self.emitter.emit_workunit(w) for w in workunits]
            
            elif self.config.emitter_type == "kafka":
                return [self.emitter.emit_workunit(w) for w in workunits]
            
            else:
                raise ValueError(f"Unsupported emitter type: {self.config.emitter_type}")
                
        except Exception as e:
            logger.error(f"❌ Batch emission failed: {e}")
            # Return failed results for all workunits
            return [type('EmitResult', (), {
                'workunit_id': w.id,
                'success': False,
                'error': e
            })() for w in workunits]
    
    def _workunit_to_mcp(self, workunit: MetadataWorkUnit) -> MetadataChangeProposal:
        """Convert workunit to MCP."""
        mcp_raw = workunit.mcp_raw
        
        return MetadataChangeProposal(
            entityType=mcp_raw.get("entityType", "dataset"),
            changeType=mcp_raw.get("changeType", "UPSERT"),
            entityUrn=mcp_raw.get("entityUrn", workunit.id),
            aspectName=mcp_raw.get("aspectName", "unknown"),
            aspect=mcp_raw.get("aspect", {}),
            systemMetadata=mcp_raw.get("systemMetadata", {})
        )
    
    def get_stats(self) -> Dict[str, Any]:
        """Get emission statistics."""
        stats = self.stats.copy()
        if self.emitter and hasattr(self.emitter, 'get_stats'):
            stats.update(self.emitter.get_stats())
        return stats
    
    def close(self):
        """Close the emitter."""
        if self.emitter:
            self.emitter.close()
            self.emitter = None


# CLI Commands
@click.group()
@click.option('--verbose', '-v', is_flag=True, help='Enable verbose logging')
@click.option('--log-file', help='Log file path')
@click.pass_context
def cli(ctx: Context, verbose: bool, log_file: Optional[str]):
    """DataGuild Emitter CLI - Enterprise metadata emission."""
    # Configure logging
    log_level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        filename=log_file
    )
    
    ctx.ensure_object(dict)
    ctx.obj['verbose'] = verbose


@cli.command()
@click.option('--config', '-c', required=True, help='Configuration file path')
@click.option('--input', '-i', required=True, help='Input metadata file (JSON)')
@click.option('--output', '-o', help='Output file for results')
@click.option('--test-connection', is_flag=True, help='Test connection before emitting')
@click.pass_context
def emit(ctx: Context, config: str, input: str, output: Optional[str], test_connection: bool):
    """Emit metadata using the configured emitter."""
    try:
        # Initialize CLI
        cli_instance = EmitterCLI()
        
        # Load configuration
        click.echo("📋 Loading configuration...")
        emitter_config = cli_instance.load_config(config)
        cli_instance.create_emitter(emitter_config)
        
        # Test connection if requested
        if test_connection:
            click.echo("🔌 Testing connection...")
            if not cli_instance.test_connection():
                click.echo("❌ Connection test failed", err=True)
                sys.exit(1)
            click.echo("✅ Connection test passed")
        
        # Load workunits
        click.echo("📂 Loading workunits...")
        with open(input, 'r') as f:
            data = json.load(f)
        
        if 'workunits' in data:
            workunits_data = data['workunits']
        else:
            workunits_data = data
        
        # Convert to workunit objects
        workunits = []
        for item in workunits_data:
            if isinstance(item, dict) and 'id' in item:
                workunit = MetadataWorkUnit(
                    id=item['id'],
                    metadata=item.get('metadata', {}),
                    mcp_raw=item.get('mcp_raw', {})
                )
                workunits.append(workunit)
        
        click.echo(f"📊 Loaded {len(workunits)} workunits")
        
        # Emit workunits
        click.echo("🚀 Starting emission...")
        results = cli_instance.emit_workunits(workunits)
        
        # Display results
        click.echo(f"\n📈 Emission Results:")
        click.echo(f"  Total: {results['total']}")
        click.echo(f"  Successful: {results['successful']}")
        click.echo(f"  Failed: {results['failed']}")
        
        if results['errors']:
            click.echo(f"\n❌ Errors:")
            for error in results['errors'][:5]:  # Show first 5 errors
                click.echo(f"  - {error}")
            if len(results['errors']) > 5:
                click.echo(f"  ... and {len(results['errors']) - 5} more")
        
        # Save results if output specified
        if output:
            with open(output, 'w') as f:
                json.dump(results, f, indent=2)
            click.echo(f"💾 Results saved to {output}")
        
        # Show final stats
        stats = cli_instance.get_stats()
        click.echo(f"\n📊 Final Statistics:")
        for key, value in stats.items():
            click.echo(f"  {key}: {value}")
        
        cli_instance.close()
        
    except Exception as e:
        click.echo(f"❌ Error: {e}", err=True)
        sys.exit(1)


@cli.command()
@click.option('--config', '-c', required=True, help='Configuration file path')
@click.pass_context
def test(ctx: Context, config: str):
    """Test emitter configuration and connection."""
    try:
        cli_instance = EmitterCLI()
        
        # Load configuration
        click.echo("📋 Loading configuration...")
        emitter_config = cli_instance.load_config(config)
        cli_instance.create_emitter(emitter_config)
        
        # Test connection
        click.echo("🔌 Testing connection...")
        if cli_instance.test_connection():
            click.echo("✅ Connection test passed")
        else:
            click.echo("❌ Connection test failed")
            sys.exit(1)
        
        # Test emission with sample data
        click.echo("🧪 Testing emission with sample data...")
        sample_workunit = MetadataWorkUnit(
            id="test-workunit",
            metadata={"test": "data"},
            mcp_raw={
                "entityType": "dataset",
                "changeType": "UPSERT",
                "entityUrn": "urn:li:dataset:(test,test_table,PROD)",
                "aspectName": "schemaMetadata",
                "aspect": {"fields": []}
            }
        )
        
        results = cli_instance.emit_workunits([sample_workunit])
        if results['successful'] > 0:
            click.echo("✅ Sample emission successful")
        else:
            click.echo("❌ Sample emission failed")
            sys.exit(1)
        
        cli_instance.close()
        click.echo("🎉 All tests passed!")
        
    except Exception as e:
        click.echo(f"❌ Test failed: {e}", err=True)
        sys.exit(1)


@cli.command()
@click.option('--emitter-type', type=click.Choice(['rest', 'kafka']), default='rest')
@click.option('--output', '-o', required=True, help='Output configuration file')
@click.pass_context
def init_config(ctx: Context, emitter_type: str, output: str):
    """Initialize a new emitter configuration file."""
    try:
        if emitter_type == 'rest':
            config_template = {
                "emitter_type": "rest",
                "server_url": "http://localhost:8080",
                "token": "your-token-here",
                "timeout_sec": 30,
                "batch_size": 100,
                "enable_tracing": True,
                "enable_validation": True,
                "enable_monitoring": True
            }
        else:  # kafka
            config_template = {
                "emitter_type": "kafka",
                "bootstrap_servers": "localhost:9092",
                "topic_name": "dataguild-metadata",
                "partition_count": 3,
                "enable_avro_serialization": True,
                "enable_partitioning": True,
                "batch_size": 1000,
                "enable_validation": True,
                "enable_monitoring": True
            }
        
        with open(output, 'w') as f:
            yaml.dump(config_template, f, default_flow_style=False, indent=2)
        
        click.echo(f"✅ Configuration template created: {output}")
        click.echo("📝 Please edit the configuration file with your settings")
        
    except Exception as e:
        click.echo(f"❌ Failed to create configuration: {e}", err=True)
        sys.exit(1)


@cli.command()
@click.option('--config', '-c', required=True, help='Configuration file path')
@click.pass_context
def validate_config(ctx: Context, config: str):
    """Validate emitter configuration."""
    try:
        cli_instance = EmitterCLI()
        
        # Load configuration
        click.echo("📋 Loading configuration...")
        emitter_config = cli_instance.load_config(config)
        
        # Validate configuration
        click.echo("✅ Configuration syntax is valid")
        
        # Test emitter creation
        click.echo("🔧 Testing emitter creation...")
        cli_instance.create_emitter(emitter_config)
        click.echo("✅ Emitter creation successful")
        
        cli_instance.close()
        click.echo("🎉 Configuration validation passed!")
        
    except Exception as e:
        click.echo(f"❌ Configuration validation failed: {e}", err=True)
        sys.exit(1)


if __name__ == '__main__':
    cli()

