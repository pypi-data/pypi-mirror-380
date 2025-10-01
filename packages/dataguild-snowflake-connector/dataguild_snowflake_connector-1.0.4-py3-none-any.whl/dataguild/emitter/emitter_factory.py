"""
DataGuild Emitter Factory

Factory for creating and configuring emitters with different backends
and configurations, inspired by DataHub's emitter patterns.
"""

import json
import logging
import os
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union, Type
from enum import Enum

from dataguild.configuration.common import ConfigModel, ConfigurationError
from dataguild.emitter.advanced_emitter import (
    Emitter,
    BaseEmitter,
    DataGuildRestEmitter,
    DataGuildKafkaEmitter,
    CompositeEmitter,
    AdvancedBatchedEmitter,
    EmitterConfig,
    create_rest_emitter,
    create_kafka_emitter,
    create_composite_emitter,
    create_batched_emitter,
)
from dataguild.emitter.enhanced_mcp_builder import EnhancedMCPBuilder, MCPBuilderConfig

logger = logging.getLogger(__name__)


class EmitterType(Enum):
    """Supported emitter types."""
    REST = "rest"
    KAFKA = "kafka"
    COMPOSITE = "composite"
    BATCHED = "batched"
    FILE = "file"
    CONSOLE = "console"


class KafkaConfig(ConfigModel):
    """Kafka configuration."""
    bootstrap_servers: str
    topic: str = "dataguild-metadata"
    schema_registry_url: Optional[str] = None
    security_protocol: str = "PLAINTEXT"
    sasl_mechanism: Optional[str] = None
    sasl_username: Optional[str] = None
    sasl_password: Optional[str] = None
    ssl_ca_location: Optional[str] = None
    ssl_certificate_location: Optional[str] = None
    ssl_key_location: Optional[str] = None
    producer_config: Optional[Dict[str, Any]] = None


class FileEmitterConfig(ConfigModel):
    """File emitter configuration."""
    output_path: str
    format: str = "json"  # json, jsonl, avro
    compression: Optional[str] = None  # gzip, bz2, xz
    append: bool = False
    max_file_size: int = 100 * 1024 * 1024  # 100MB
    max_files: int = 10


class ConsoleEmitterConfig(ConfigModel):
    """Console emitter configuration."""
    format: str = "pretty"  # pretty, json, compact
    colorize: bool = True
    show_metadata: bool = True


class EmitterFactory:
    """
    Factory for creating emitters with different configurations.
    
    Supports multiple emitter types and automatic configuration
    from environment variables and configuration files.
    """
    
    def __init__(self):
        self._emitter_registry: Dict[str, Type[BaseEmitter]] = {
            EmitterType.REST.value: DataGuildRestEmitter,
            EmitterType.KAFKA.value: DataGuildKafkaEmitter,
            EmitterType.COMPOSITE.value: CompositeEmitter,
            EmitterType.BATCHED.value: AdvancedBatchedEmitter,
        }
        self._config_cache: Dict[str, Any] = {}
    
    def register_emitter(self, emitter_type: str, emitter_class: Type[BaseEmitter]) -> None:
        """Register a custom emitter type."""
        self._emitter_registry[emitter_type] = emitter_class
        logger.info(f"Registered emitter type: {emitter_type}")
    
    def create_emitter(
        self,
        emitter_type: Union[str, EmitterType],
        config: Optional[Dict[str, Any]] = None,
        **kwargs
    ) -> Emitter:
        """
        Create an emitter of the specified type.
        
        Args:
            emitter_type: Type of emitter to create
            config: Configuration dictionary
            **kwargs: Additional configuration parameters
            
        Returns:
            Configured emitter instance
            
        Raises:
            ConfigurationError: If emitter type is not supported or configuration is invalid
        """
        if isinstance(emitter_type, EmitterType):
            emitter_type = emitter_type.value
        
        if emitter_type not in self._emitter_registry:
            raise ConfigurationError(f"Unsupported emitter type: {emitter_type}")
        
        # Merge configuration
        final_config = self._merge_config(emitter_type, config or {}, kwargs)
        
        # Create emitter
        emitter_class = self._emitter_registry[emitter_type]
        
        try:
            if emitter_type == EmitterType.REST.value:
                return self._create_rest_emitter(final_config)
            elif emitter_type == EmitterType.KAFKA.value:
                return self._create_kafka_emitter(final_config)
            elif emitter_type == EmitterType.COMPOSITE.value:
                return self._create_composite_emitter(final_config)
            elif emitter_type == EmitterType.BATCHED.value:
                return self._create_batched_emitter(final_config)
            else:
                return emitter_class(final_config)
                
        except Exception as e:
            raise ConfigurationError(f"Failed to create {emitter_type} emitter: {e}")
    
    def _merge_config(
        self,
        emitter_type: str,
        config: Dict[str, Any],
        kwargs: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Merge configuration from multiple sources."""
        # Start with default configuration
        merged_config = self._get_default_config(emitter_type)
        
        # Add configuration from dict
        merged_config.update(config)
        
        # Add configuration from kwargs
        merged_config.update(kwargs)
        
        # Load from environment variables
        env_config = self._load_from_environment(emitter_type)
        merged_config.update(env_config)
        
        return merged_config
    
    def _get_default_config(self, emitter_type: str) -> Dict[str, Any]:
        """Get default configuration for emitter type."""
        defaults = {
            EmitterType.REST.value: {
                "server_url": "http://localhost:8080",
                "timeout_sec": 30.0,
                "retry_max_times": 3,
                "batch_size": 100,
            },
            EmitterType.KAFKA.value: {
                "bootstrap_servers": "localhost:9092",
                "topic": "dataguild-metadata",
                "timeout_sec": 30.0,
                "batch_size": 100,
            },
            EmitterType.COMPOSITE.value: {
                "emitters": [],
            },
            EmitterType.BATCHED.value: {
                "batch_size": 100,
                "batch_timeout_sec": 5.0,
                "base_emitter": None,
            },
        }
        return defaults.get(emitter_type, {})
    
    def _load_from_environment(self, emitter_type: str) -> Dict[str, Any]:
        """Load configuration from environment variables."""
        env_config = {}
        
        # Common environment variables
        if "DATAGUILD_SERVER_URL" in os.environ:
            env_config["server_url"] = os.environ["DATAGUILD_SERVER_URL"]
        
        if "DATAGUILD_TOKEN" in os.environ:
            env_config["token"] = os.environ["DATAGUILD_TOKEN"]
        
        if "DATAGUILD_BATCH_SIZE" in os.environ:
            try:
                env_config["batch_size"] = int(os.environ["DATAGUILD_BATCH_SIZE"])
            except ValueError:
                logger.warning(f"Invalid DATAGUILD_BATCH_SIZE: {os.environ['DATAGUILD_BATCH_SIZE']}")
        
        # Kafka-specific environment variables
        if emitter_type == EmitterType.KAFKA.value:
            if "KAFKA_BOOTSTRAP_SERVERS" in os.environ:
                env_config["bootstrap_servers"] = os.environ["KAFKA_BOOTSTRAP_SERVERS"]
            
            if "KAFKA_TOPIC" in os.environ:
                env_config["topic"] = os.environ["KAFKA_TOPIC"]
            
            if "KAFKA_SCHEMA_REGISTRY_URL" in os.environ:
                env_config["schema_registry_url"] = os.environ["KAFKA_SCHEMA_REGISTRY_URL"]
        
        return env_config
    
    def _create_rest_emitter(self, config: Dict[str, Any]) -> DataGuildRestEmitter:
        """Create a REST emitter."""
        emitter_config = EmitterConfig(
            server_url=config["server_url"],
            token=config.get("token"),
            timeout_sec=config.get("timeout_sec", 30.0),
            retry_max_times=config.get("retry_max_times", 3),
            batch_size=config.get("batch_size", 100),
            custom_headers=config.get("custom_headers", {}),
            ca_certificate_path=config.get("ca_certificate_path"),
            disable_ssl_verification=config.get("disable_ssl_verification", False),
        )
        return create_rest_emitter(emitter_config)
    
    def _create_kafka_emitter(self, config: Dict[str, Any]) -> DataGuildKafkaEmitter:
        """Create a Kafka emitter."""
        # Create Kafka configuration
        kafka_config = {
            "bootstrap.servers": config["bootstrap_servers"],
        }
        
        # Add security configuration
        if config.get("security_protocol"):
            kafka_config["security.protocol"] = config["security_protocol"]
        
        if config.get("sasl_mechanism"):
            kafka_config["sasl.mechanism"] = config["sasl_mechanism"]
            kafka_config["sasl.username"] = config.get("sasl_username")
            kafka_config["sasl.password"] = config.get("sasl_password")
        
        # Add SSL configuration
        if config.get("ssl_ca_location"):
            kafka_config["ssl.ca.location"] = config["ssl_ca_location"]
        if config.get("ssl_certificate_location"):
            kafka_config["ssl.certificate.location"] = config["ssl_certificate_location"]
        if config.get("ssl_key_location"):
            kafka_config["ssl.key.location"] = config["ssl_key_location"]
        
        # Add producer configuration
        if config.get("producer_config"):
            kafka_config.update(config["producer_config"])
        
        # Create emitter configuration
        emitter_config = EmitterConfig(
            server_url=config.get("server_url", "kafka://"),
            batch_size=config.get("batch_size", 100),
            timeout_sec=config.get("timeout_sec", 30.0),
        )
        
        return create_kafka_emitter(emitter_config, kafka_config)
    
    def _create_composite_emitter(self, config: Dict[str, Any]) -> CompositeEmitter:
        """Create a composite emitter."""
        emitters = []
        
        for emitter_config in config.get("emitters", []):
            emitter_type = emitter_config.get("type")
            emitter_params = emitter_config.get("config", {})
            
            if emitter_type:
                emitter = self.create_emitter(emitter_type, emitter_params)
                emitters.append(emitter)
        
        if not emitters:
            raise ConfigurationError("Composite emitter requires at least one sub-emitter")
        
        return create_composite_emitter(emitters)
    
    def _create_batched_emitter(self, config: Dict[str, Any]) -> AdvancedBatchedEmitter:
        """Create a batched emitter."""
        base_emitter_config = config.get("base_emitter")
        if not base_emitter_config:
            raise ConfigurationError("Batched emitter requires a base emitter configuration")
        
        # Create base emitter
        base_emitter_type = base_emitter_config.get("type")
        base_emitter_params = base_emitter_config.get("config", {})
        
        if not base_emitter_type:
            raise ConfigurationError("Base emitter type is required")
        
        base_emitter = self.create_emitter(base_emitter_type, base_emitter_params)
        
        # Create batched emitter configuration
        emitter_config = EmitterConfig(
            server_url=config.get("server_url", "http://localhost:8080"),
            batch_size=config.get("batch_size", 100),
            batch_timeout_sec=config.get("batch_timeout_sec", 5.0),
        )
        
        return create_batched_emitter(emitter_config, base_emitter)
    
    def create_from_config_file(self, config_path: str) -> Emitter:
        """
        Create an emitter from a configuration file.
        
        Args:
            config_path: Path to configuration file (JSON or YAML)
            
        Returns:
            Configured emitter instance
        """
        try:
            with open(config_path, 'r') as f:
                if config_path.endswith('.yaml') or config_path.endswith('.yml'):
                    import yaml
                    config = yaml.safe_load(f)
                else:
                    config = json.load(f)
            
            emitter_type = config.get("type")
            if not emitter_type:
                raise ConfigurationError("Configuration file must specify emitter type")
            
            emitter_config = config.get("config", {})
            return self.create_emitter(emitter_type, emitter_config)
            
        except FileNotFoundError:
            raise ConfigurationError(f"Configuration file not found: {config_path}")
        except json.JSONDecodeError as e:
            raise ConfigurationError(f"Invalid JSON in configuration file: {e}")
        except Exception as e:
            raise ConfigurationError(f"Failed to load configuration file: {e}")
    
    def create_mcp_builder(
        self,
        config: Optional[Dict[str, Any]] = None
    ) -> EnhancedMCPBuilder:
        """
        Create an enhanced MCP builder.
        
        Args:
            config: Optional configuration for the MCP builder
            
        Returns:
            Configured MCP builder instance
        """
        builder_config = MCPBuilderConfig()
        
        if config:
            # Update builder configuration from provided config
            for key, value in config.items():
                if hasattr(builder_config, key):
                    setattr(builder_config, key, value)
        
        return EnhancedMCPBuilder(builder_config)
    
    def get_supported_emitter_types(self) -> List[str]:
        """Get list of supported emitter types."""
        return list(self._emitter_registry.keys())
    
    def validate_config(self, emitter_type: str, config: Dict[str, Any]) -> bool:
        """
        Validate configuration for an emitter type.
        
        Args:
            emitter_type: Type of emitter
            config: Configuration to validate
            
        Returns:
            True if configuration is valid
            
        Raises:
            ConfigurationError: If configuration is invalid
        """
        if emitter_type not in self._emitter_registry:
            raise ConfigurationError(f"Unsupported emitter type: {emitter_type}")
        
        # Basic validation
        if emitter_type == EmitterType.REST.value:
            if "server_url" not in config:
                raise ConfigurationError("REST emitter requires server_url")
        
        elif emitter_type == EmitterType.KAFKA.value:
            if "bootstrap_servers" not in config:
                raise ConfigurationError("Kafka emitter requires bootstrap_servers")
        
        elif emitter_type == EmitterType.COMPOSITE.value:
            if "emitters" not in config or not config["emitters"]:
                raise ConfigurationError("Composite emitter requires emitters list")
        
        elif emitter_type == EmitterType.BATCHED.value:
            if "base_emitter" not in config:
                raise ConfigurationError("Batched emitter requires base_emitter")
        
        return True


# Global factory instance
_factory = EmitterFactory()


# Convenience functions
def create_emitter(
    emitter_type: Union[str, EmitterType],
    config: Optional[Dict[str, Any]] = None,
    **kwargs
) -> Emitter:
    """Create an emitter using the global factory."""
    return _factory.create_emitter(emitter_type, config, **kwargs)


def create_emitter_from_config(config_path: str) -> Emitter:
    """Create an emitter from a configuration file."""
    return _factory.create_from_config_file(config_path)


def create_mcp_builder(config: Optional[Dict[str, Any]] = None) -> EnhancedMCPBuilder:
    """Create an MCP builder using the global factory."""
    return _factory.create_mcp_builder(config)


def register_emitter(emitter_type: str, emitter_class: Type[BaseEmitter]) -> None:
    """Register a custom emitter type."""
    _factory.register_emitter(emitter_type, emitter_class)


def get_supported_emitter_types() -> List[str]:
    """Get list of supported emitter types."""
    return _factory.get_supported_emitter_types()


# Export all classes and functions
__all__ = [
    # Enums
    'EmitterType',
    
    # Data classes
    'KafkaConfig',
    'FileEmitterConfig',
    'ConsoleEmitterConfig',
    
    # Main classes
    'EmitterFactory',
    
    # Convenience functions
    'create_emitter',
    'create_emitter_from_config',
    'create_mcp_builder',
    'register_emitter',
    'get_supported_emitter_types',
]
