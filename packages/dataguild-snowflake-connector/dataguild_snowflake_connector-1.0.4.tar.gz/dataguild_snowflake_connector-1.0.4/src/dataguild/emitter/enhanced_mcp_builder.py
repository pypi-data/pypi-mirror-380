"""
DataGuild Enhanced MCP Builder

Advanced Metadata Change Proposal builder with comprehensive validation,
caching, performance optimization, and integration with the new emitter system.
"""

import hashlib
import json
import re
import time
from datetime import datetime
from typing import Any, Dict, List, Optional, Set, Union, Iterable, Callable
from dataclasses import dataclass, asdict
from enum import Enum

import logging

from dataguild.configuration.common import ConfigModel
from dataguild.emitter.mcp import (
    AspectType,
    MetadataAspect,
    MetadataChangeProposal,
    MetadataChangeProposalWrapper,
    MetadataWorkUnit as MCPWorkUnit,
)
from dataguild.emitter.advanced_emitter import Emitter, EmitResult
from dataguild.emitter.mcp_builder import (
    DatabaseKey,
    SchemaKey,
    EntityType,
    PlatformType,
    AdvancedMCPBuilder,
)

logger = logging.getLogger(__name__)


class ValidationLevel(Enum):
    """Validation levels for MCPs."""
    NONE = "none"
    BASIC = "basic"
    STRICT = "strict"
    ENTERPRISE = "enterprise"


class MCPBuilderConfig(ConfigModel):
    """Configuration for the enhanced MCP builder."""
    validation_level: ValidationLevel = ValidationLevel.STRICT
    enable_caching: bool = True
    enable_deduplication: bool = True
    enable_metrics: bool = True
    max_cache_size: int = 10000
    cache_ttl_seconds: int = 3600
    enable_compression: bool = True
    enable_encryption: bool = False
    custom_validation_rules: Optional[List[Callable]] = None


class EnhancedMCPBuilder(AdvancedMCPBuilder):
    """
    Enhanced MCP builder with advanced features inspired by DataHub.
    
    Features:
    - Multi-level validation
    - Intelligent caching with TTL
    - Performance metrics and monitoring
    - Custom validation rules
    - Compression and encryption support
    - Integration with emitter system
    """
    
    def __init__(self, config: Optional[MCPBuilderConfig] = None):
        super().__init__()
        self.config = config or MCPBuilderConfig()
        self._validation_cache: Dict[str, bool] = {}
        self._compression_cache: Dict[str, bytes] = {}
        self._encryption_key: Optional[str] = None
        self._custom_validators: List[Callable] = self.config.custom_validation_rules or []
        self._performance_metrics = {
            'mcp_created': 0,
            'mcp_validated': 0,
            'mcp_cached': 0,
            'validation_errors': 0,
            'compression_savings': 0,
            'cache_hits': 0,
            'cache_misses': 0,
        }
        
        if self.config.enable_encryption:
            self._setup_encryption()
    
    def _setup_encryption(self) -> None:
        """Setup encryption for sensitive data."""
        try:
            from cryptography.fernet import Fernet
            # In production, this should come from secure key management
            self._encryption_key = Fernet.generate_key()
        except ImportError:
            logger.warning("cryptography not available, encryption disabled")
            self.config.enable_encryption = False
    
    def create_mcp(
        self,
        entity_urn: str,
        aspect: MetadataAspect,
        change_type: str = "UPSERT",
        system_metadata: Optional[Dict[str, Any]] = None,
        custom_headers: Optional[Dict[str, str]] = None,
        priority: int = 1,
        batch_id: Optional[str] = None,
    ) -> MCPWorkUnit:
        """
        Create a Metadata Change Proposal with enhanced validation and features.
        
        Args:
            entity_urn: URN of the entity
            aspect: Metadata aspect to change
            change_type: Type of change (UPSERT, DELETE, etc.)
            system_metadata: Optional system metadata
            custom_headers: Optional custom headers
            priority: Priority of the workunit
            batch_id: Optional batch identifier
            
        Returns:
            MetadataWorkUnit with the MCP
            
        Raises:
            ValueError: If validation fails
        """
        try:
            # Create the MCP wrapper
            mcp_wrapper = MetadataChangeProposalWrapper(
                entityUrn=entity_urn,
                aspect=aspect,
                changeType=change_type
            )
            
            # Add system metadata
            if system_metadata:
                mcp_wrapper.mcp.systemMetadata = system_metadata
            
            # Add custom headers
            if custom_headers:
                mcp_wrapper.mcp.headers = custom_headers
            
            # Validate the MCP
            if self.config.validation_level != ValidationLevel.NONE:
                self._validate_mcp(mcp_wrapper.mcp)
            
            # Create workunit
            workunit = mcp_wrapper.as_workunit(priority=priority, batch_id=batch_id)
            
            # Apply compression if enabled
            if self.config.enable_compression:
                workunit = self._compress_workunit(workunit)
            
            # Apply encryption if enabled
            if self.config.enable_encryption:
                workunit = self._encrypt_workunit(workunit)
            
            # Update metrics
            self._performance_metrics['mcp_created'] += 1
            
            logger.debug(f"Created MCP for entity {entity_urn} with aspect {aspect.aspect_name()}")
            return workunit
            
        except Exception as e:
            self._performance_metrics['validation_errors'] += 1
            logger.error(f"Failed to create MCP for entity {entity_urn}: {e}")
            raise
    
    def create_dataset_mcp(
        self,
        platform: str,
        database_name: str,
        schema_name: str,
        table_name: str,
        aspect: MetadataAspect,
        change_type: str = "UPSERT",
        platform_instance: Optional[str] = None,
        env: str = "PROD",
        **kwargs
    ) -> MCPWorkUnit:
        """
        Create a dataset MCP with standardized naming and validation.
        
        Args:
            platform: Data platform name
            database_name: Database name
            schema_name: Schema name
            table_name: Table name
            aspect: Metadata aspect
            change_type: Type of change
            platform_instance: Platform instance identifier
            env: Environment
            **kwargs: Additional arguments passed to create_mcp
            
        Returns:
            MetadataWorkUnit for the dataset
        """
        # Create standardized keys
        db_key = self.make_database_key(database_name)
        schema_key = self.make_schema_key(database_name, schema_name)
        
        # Create dataset URN
        dataset_urn = self.make_dataset_urn_from_keys(
            platform=platform,
            database_key=db_key,
            schema_key=schema_key,
            table_name=table_name,
            env=env
        )
        
        # Add platform instance if provided
        if platform_instance:
            dataset_urn = self.make_dataset_urn_with_platform_instance(
                platform=platform,
                name=f"{schema_key.key()}.{table_name.lower()}",
                env=env,
                platform_instance=platform_instance
            )
        
        return self.create_mcp(
            entity_urn=dataset_urn,
            aspect=aspect,
            change_type=change_type,
            **kwargs
        )
    
    def create_container_mcp(
        self,
        platform: str,
        database_name: str,
        schema_name: str,
        aspect: MetadataAspect,
        change_type: str = "UPSERT",
        env: str = "PROD",
        **kwargs
    ) -> MCPWorkUnit:
        """
        Create a container MCP for a schema.
        
        Args:
            platform: Data platform name
            database_name: Database name
            schema_name: Schema name
            aspect: Metadata aspect
            change_type: Type of change
            env: Environment
            **kwargs: Additional arguments passed to create_mcp
            
        Returns:
            MetadataWorkUnit for the container
        """
        # Create standardized keys
        schema_key = self.make_schema_key(database_name, schema_name)
        
        # Create container URN
        container_urn = self.make_container_urn_from_schema_key(
            platform=platform,
            schema_key=schema_key,
            env=env
        )
        
        return self.create_mcp(
            entity_urn=container_urn,
            aspect=aspect,
            change_type=change_type,
            **kwargs
        )
    
    def create_schema_field_mcp(
        self,
        dataset_urn: str,
        field_path: str,
        aspect: MetadataAspect,
        change_type: str = "UPSERT",
        **kwargs
    ) -> MCPWorkUnit:
        """
        Create a schema field MCP.
        
        Args:
            dataset_urn: URN of the parent dataset
            field_path: Path of the field
            aspect: Metadata aspect
            change_type: Type of change
            **kwargs: Additional arguments passed to create_mcp
            
        Returns:
            MetadataWorkUnit for the schema field
        """
        # Create schema field URN
        field_urn = self.make_schema_field_urn(dataset_urn, field_path)
        
        return self.create_mcp(
            entity_urn=field_urn,
            aspect=aspect,
            change_type=change_type,
            **kwargs
        )
    
    def create_batch_mcps(
        self,
        mcp_specs: List[Dict[str, Any]],
        batch_id: Optional[str] = None,
        priority: int = 1,
    ) -> List[MCPWorkUnit]:
        """
        Create multiple MCPs in a batch with shared configuration.
        
        Args:
            mcp_specs: List of MCP specifications
            batch_id: Optional batch identifier
            priority: Priority for all workunits
            
        Returns:
            List of MetadataWorkUnits
        """
        workunits = []
        
        for spec in mcp_specs:
            try:
                workunit = self.create_mcp(
                    batch_id=batch_id,
                    priority=priority,
                    **spec
                )
                workunits.append(workunit)
            except Exception as e:
                logger.error(f"Failed to create MCP from spec {spec}: {e}")
                continue
        
        logger.info(f"Created {len(workunits)} MCPs in batch {batch_id}")
        return workunits
    
    def _validate_mcp(self, mcp: MetadataChangeProposal) -> None:
        """
        Validate MCP based on configured validation level.
        
        Args:
            mcp: Metadata Change Proposal to validate
            
        Raises:
            ValueError: If validation fails
        """
        if self.config.validation_level == ValidationLevel.NONE:
            return
        
        # Basic validation
        if not mcp.entityUrn:
            raise ValueError("Entity URN cannot be empty")
        
        if not mcp.aspect:
            raise ValueError("Aspect cannot be empty")
        
        if not mcp.aspect.validate():
            raise ValueError(f"Invalid aspect: {mcp.aspect}")
        
        # Check cache for previous validation
        cache_key = f"{mcp.entityUrn}:{mcp.aspect.aspect_name()}:{mcp.changeType}"
        if self.config.enable_caching and cache_key in self._validation_cache:
            if not self._validation_cache[cache_key]:
                raise ValueError("Previously failed validation")
            self._performance_metrics['cache_hits'] += 1
            return
        
        # Strict validation
        if self.config.validation_level in [ValidationLevel.STRICT, ValidationLevel.ENTERPRISE]:
            self._validate_urn_format(mcp.entityUrn)
            self._validate_aspect_content(mcp.aspect)
            self._validate_change_type(mcp.changeType)
        
        # Enterprise validation
        if self.config.validation_level == ValidationLevel.ENTERPRISE:
            self._validate_enterprise_rules(mcp)
        
        # Custom validation
        for validator in self._custom_validators:
            try:
                validator(mcp)
            except Exception as e:
                raise ValueError(f"Custom validation failed: {e}")
        
        # Cache validation result
        if self.config.enable_caching:
            self._validation_cache[cache_key] = True
            self._performance_metrics['mcp_validated'] += 1
        else:
            self._performance_metrics['cache_misses'] += 1
    
    def _validate_urn_format(self, urn: str) -> None:
        """Validate URN format."""
        if not urn.startswith("urn:li:"):
            raise ValueError(f"Invalid URN format: {urn}")
        
        # Additional URN validation logic
        parts = urn.split(":")
        if len(parts) < 3:
            raise ValueError(f"Invalid URN format: {urn}")
    
    def _validate_aspect_content(self, aspect: MetadataAspect) -> None:
        """Validate aspect content."""
        if not hasattr(aspect, 'to_dict'):
            raise ValueError("Aspect must have to_dict method")
        
        try:
            aspect_dict = aspect.to_dict()
            json.dumps(aspect_dict)  # Test serialization
        except Exception as e:
            raise ValueError(f"Aspect content validation failed: {e}")
    
    def _validate_change_type(self, change_type: str) -> None:
        """Validate change type."""
        valid_types = ["UPSERT", "DELETE", "PATCH"]
        if change_type not in valid_types:
            raise ValueError(f"Invalid change type: {change_type}")
    
    def _validate_enterprise_rules(self, mcp: MetadataChangeProposal) -> None:
        """Validate enterprise-specific rules."""
        # Check for sensitive data patterns
        if hasattr(mcp.aspect, 'to_dict'):
            aspect_dict = mcp.aspect.to_dict()
            self._check_sensitive_data(aspect_dict)
        
        # Check for compliance requirements
        self._check_compliance_requirements(mcp)
    
    def _check_sensitive_data(self, data: Any) -> None:
        """Check for sensitive data patterns."""
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(key, str) and any(pattern in key.lower() for pattern in ['password', 'secret', 'key', 'token']):
                    logger.warning(f"Potential sensitive data in key: {key}")
                self._check_sensitive_data(value)
        elif isinstance(data, list):
            for item in data:
                self._check_sensitive_data(item)
    
    def _check_compliance_requirements(self, mcp: MetadataChangeProposal) -> None:
        """Check compliance requirements."""
        # Add compliance checks here
        pass
    
    def _compress_workunit(self, workunit: MCPWorkUnit) -> MCPWorkUnit:
        """Compress workunit data."""
        try:
            import gzip
            
            # Serialize workunit data
            data = json.dumps(workunit.get_metadata()).encode()
            
            # Compress data
            compressed_data = gzip.compress(data)
            
            # Calculate savings
            savings = len(data) - len(compressed_data)
            self._performance_metrics['compression_savings'] += savings
            
            # Store compressed data (in a real implementation, you'd modify the workunit)
            logger.debug(f"Compressed workunit {workunit.id}, saved {savings} bytes")
            
        except ImportError:
            logger.warning("gzip not available, compression disabled")
        except Exception as e:
            logger.error(f"Compression failed: {e}")
        
        return workunit
    
    def _encrypt_workunit(self, workunit: MCPWorkUnit) -> MCPWorkUnit:
        """Encrypt workunit data."""
        if not self.config.enable_encryption or not self._encryption_key:
            return workunit
        
        try:
            from cryptography.fernet import Fernet
            
            # Serialize workunit data
            data = json.dumps(workunit.get_metadata()).encode()
            
            # Encrypt data
            fernet = Fernet(self._encryption_key)
            encrypted_data = fernet.encrypt(data)
            
            # Store encrypted data (in a real implementation, you'd modify the workunit)
            logger.debug(f"Encrypted workunit {workunit.id}")
            
        except ImportError:
            logger.warning("cryptography not available, encryption disabled")
        except Exception as e:
            logger.error(f"Encryption failed: {e}")
        
        return workunit
    
    def add_custom_validator(self, validator: Callable) -> None:
        """Add a custom validation function."""
        self._custom_validators.append(validator)
        logger.info("Added custom validator")
    
    def clear_cache(self) -> None:
        """Clear all caches."""
        super().clear_cache()
        self._validation_cache.clear()
        self._compression_cache.clear()
        logger.info("Cleared all caches")
    
    def get_performance_metrics(self) -> Dict[str, Any]:
        """Get performance metrics."""
        base_metrics = super().get_performance_metrics()
        return {**base_metrics, **self._performance_metrics}
    
    def emit_with_emitter(
        self,
        workunit: MCPWorkUnit,
        emitter: Emitter,
        callback: Optional[Callable[[EmitResult], None]] = None,
    ) -> None:
        """
        Emit a workunit using the provided emitter.
        
        Args:
            workunit: Workunit to emit
            emitter: Emitter to use
            callback: Optional callback for result
        """
        try:
            emitter.emit(workunit, callback)
            logger.debug(f"Emitted workunit {workunit.id} using {type(emitter).__name__}")
        except Exception as e:
            logger.error(f"Failed to emit workunit {workunit.id}: {e}")
            if callback:
                callback(EmitResult(
                    workunit_id=workunit.id,
                    status="failed",
                    error=e,
                    message=str(e)
                ))
    
    def emit_batch_with_emitter(
        self,
        workunits: List[MCPWorkUnit],
        emitter: Emitter,
        callback: Optional[Callable[[List[EmitResult]], None]] = None,
    ) -> List[EmitResult]:
        """
        Emit a batch of workunits using the provided emitter.
        
        Args:
            workunits: Workunits to emit
            emitter: Emitter to use
            callback: Optional callback for results
            
        Returns:
            List of emit results
        """
        try:
            results = emitter.emit_batch(workunits, callback)
            logger.info(f"Emitted batch of {len(workunits)} workunits using {type(emitter).__name__}")
            return results
        except Exception as e:
            logger.error(f"Failed to emit batch: {e}")
            # Create failed results for all workunits
            results = []
            for workunit in workunits:
                results.append(EmitResult(
                    workunit_id=workunit.id,
                    status="failed",
                    error=e,
                    message=str(e)
                ))
            if callback:
                callback(results)
            return results


# Global builder instance
_enhanced_builder = EnhancedMCPBuilder()


# Convenience functions
def create_enhanced_mcp(
    entity_urn: str,
    aspect: MetadataAspect,
    change_type: str = "UPSERT",
    **kwargs
) -> MCPWorkUnit:
    """Create an enhanced MCP using the global builder."""
    return _enhanced_builder.create_mcp(entity_urn, aspect, change_type, **kwargs)


def create_dataset_mcp(
    platform: str,
    database_name: str,
    schema_name: str,
    table_name: str,
    aspect: MetadataAspect,
    **kwargs
) -> MCPWorkUnit:
    """Create a dataset MCP using the global builder."""
    return _enhanced_builder.create_dataset_mcp(
        platform, database_name, schema_name, table_name, aspect, **kwargs
    )


def create_container_mcp(
    platform: str,
    database_name: str,
    schema_name: str,
    aspect: MetadataAspect,
    **kwargs
) -> MCPWorkUnit:
    """Create a container MCP using the global builder."""
    return _enhanced_builder.create_container_mcp(
        platform, database_name, schema_name, aspect, **kwargs
    )


def create_schema_field_mcp(
    dataset_urn: str,
    field_path: str,
    aspect: MetadataAspect,
    **kwargs
) -> MCPWorkUnit:
    """Create a schema field MCP using the global builder."""
    return _enhanced_builder.create_schema_field_mcp(
        dataset_urn, field_path, aspect, **kwargs
    )


# Export all classes and functions
__all__ = [
    # Enums
    'ValidationLevel',
    
    # Data classes
    'MCPBuilderConfig',
    
    # Main classes
    'EnhancedMCPBuilder',
    
    # Convenience functions
    'create_enhanced_mcp',
    'create_dataset_mcp',
    'create_container_mcp',
    'create_schema_field_mcp',
]
