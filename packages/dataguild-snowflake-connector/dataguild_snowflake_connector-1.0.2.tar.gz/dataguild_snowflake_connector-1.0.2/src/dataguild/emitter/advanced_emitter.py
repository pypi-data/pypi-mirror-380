"""
DataGuild Advanced Emitter System

Enterprise-grade emitter implementation inspired by DataHub's best practices
with comprehensive error handling, batching, retry logic, and observability.
"""

import asyncio
import json
import logging
import time
import uuid
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Protocol,
    Sequence,
    Set,
    Union,
    cast,
)
from urllib.parse import urljoin

import requests
from requests.adapters import HTTPAdapter, Retry
from requests.exceptions import HTTPError, RequestException, Timeout

from dataguild.api.workunit import MetadataWorkUnit
from dataguild.configuration.common import ConfigModel, ConfigurationError
from dataguild.emitter.mcp import (
    AspectType,
    BatchedMCPEmitter,
    MetadataAspect,
    MetadataChangeProposal,
    MetadataChangeProposalWrapper,
    MetadataWorkUnit as MCPWorkUnit,
)

logger = logging.getLogger(__name__)


class EmitMode(Enum):
    """Emit modes for different processing strategies."""
    SYNC = "sync"
    ASYNC = "async"
    ASYNC_WAIT = "async_wait"
    BATCH = "batch"


class EmitStatus(Enum):
    """Status of emitted workunits."""
    PENDING = "pending"
    PROCESSING = "processing"
    SUCCESS = "success"
    FAILED = "failed"
    RETRY = "retry"


@dataclass
class EmitResult:
    """Result of an emit operation."""
    workunit_id: str
    status: EmitStatus
    message: Optional[str] = None
    timestamp: datetime = field(default_factory=datetime.now)
    retry_count: int = 0
    error: Optional[Exception] = None


class EmitterConfig(ConfigModel):
    """Configuration for the advanced emitter."""
    # Connection settings
    server_url: str
    token: Optional[str] = None
    timeout_sec: float = 30.0
    connect_timeout_sec: float = 10.0
    read_timeout_sec: float = 30.0
    
    # Retry settings
    retry_max_times: int = 3
    retry_backoff_factor: float = 2.0
    retry_status_codes: List[int] = [429, 500, 502, 503, 504]
    
    # Batching settings
    batch_size: int = 100
    batch_timeout_sec: float = 5.0
    max_payload_bytes: int = 15 * 1024 * 1024  # 15MB
    
    # Performance settings
    max_workers: int = 10
    enable_deduplication: bool = True
    enable_compression: bool = True
    
    # Observability settings
    enable_metrics: bool = True
    enable_tracing: bool = False
    log_level: str = "INFO"
    
    # Advanced settings
    emit_mode: EmitMode = EmitMode.BATCH
    custom_headers: Dict[str, str] = {}
    ca_certificate_path: Optional[str] = None
    disable_ssl_verification: bool = False


class Emitter(Protocol):
    """Protocol for all emitter implementations."""
    
    def emit(
        self,
        workunit: Union[MetadataWorkUnit, MCPWorkUnit],
        callback: Optional[Callable[[EmitResult], None]] = None,
    ) -> None:
        """Emit a single workunit."""
        ...
    
    def emit_batch(
        self,
        workunits: Sequence[Union[MetadataWorkUnit, MCPWorkUnit]],
        callback: Optional[Callable[[List[EmitResult]], None]] = None,
    ) -> List[EmitResult]:
        """Emit a batch of workunits."""
        ...
    
    def flush(self) -> None:
        """Flush any pending workunits."""
        ...
    
    def close(self) -> None:
        """Close the emitter and cleanup resources."""
        ...


class BaseEmitter(ABC):
    """Base class for all emitter implementations."""
    
    def __init__(self, config: EmitterConfig):
        self.config = config
        self._session: Optional[requests.Session] = None
        self._metrics: Dict[str, Any] = {
            "emitted_count": 0,
            "success_count": 0,
            "error_count": 0,
            "retry_count": 0,
            "batch_count": 0,
        }
        self._dedup_cache: Set[str] = set()
        self._setup_logging()
    
    def _setup_logging(self) -> None:
        """Setup logging configuration."""
        logging.basicConfig(
            level=getattr(logging, self.config.log_level.upper()),
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
    
    @abstractmethod
    def _create_session(self) -> requests.Session:
        """Create and configure the HTTP session."""
        ...
    
    @abstractmethod
    def _emit_single(
        self,
        workunit: Union[MetadataWorkUnit, MCPWorkUnit],
        session: requests.Session,
    ) -> EmitResult:
        """Emit a single workunit."""
        ...
    
    def _get_session(self) -> requests.Session:
        """Get or create the HTTP session."""
        if self._session is None:
            self._session = self._create_session()
        return self._session
    
    def _should_deduplicate(self, workunit: Union[MetadataWorkUnit, MCPWorkUnit]) -> bool:
        """Check if workunit should be deduplicated."""
        if not self.config.enable_deduplication:
            return False
        
        # Generate content hash for deduplication
        if isinstance(workunit, MCPWorkUnit):
            content_hash = workunit.mcp.get_hash()
        else:
            # For MetadataWorkUnit, use a combination of URN and aspect
            # Handle both urn attribute and fallback to id
            urn = getattr(workunit, 'urn', workunit.id)
            aspect_name = getattr(workunit, 'aspect_name', 'unknown')
            content_hash = f"{urn}:{aspect_name}"
        
        if content_hash in self._dedup_cache:
            logger.debug(f"Skipping duplicate workunit: {workunit.id}")
            return True
        
        self._dedup_cache.add(content_hash)
        return False
    
    def emit(
        self,
        workunit: Union[MetadataWorkUnit, MCPWorkUnit],
        callback: Optional[Callable[[EmitResult], None]] = None,
    ) -> None:
        """Emit a single workunit."""
        try:
            # Check deduplication
            if self._should_deduplicate(workunit):
                result = EmitResult(
                    workunit_id=workunit.id,
                    status=EmitStatus.SUCCESS,
                    message="Skipped duplicate workunit"
                )
                if callback:
                    callback(result)
                return
            
            session = self._get_session()
            result = self._emit_single(workunit, session)
            
            # Update metrics
            self._metrics["emitted_count"] += 1
            if result.status == EmitStatus.SUCCESS:
                self._metrics["success_count"] += 1
            elif result.status == EmitStatus.FAILED:
                self._metrics["error_count"] += 1
            elif result.status == EmitStatus.RETRY:
                self._metrics["retry_count"] += 1
            
            if callback:
                callback(result)
                
        except Exception as e:
            logger.error(f"Failed to emit workunit {workunit.id}: {e}")
            result = EmitResult(
                workunit_id=workunit.id,
                status=EmitStatus.FAILED,
                error=e,
                message=str(e)
            )
            self._metrics["error_count"] += 1
            if callback:
                callback(result)
    
    def emit_batch(
        self,
        workunits: Sequence[Union[MetadataWorkUnit, MCPWorkUnit]],
        callback: Optional[Callable[[List[EmitResult]], None]] = None,
    ) -> List[EmitResult]:
        """Emit a batch of workunits."""
        results = []
        session = self._get_session()
        
        # Filter out duplicates
        filtered_workunits = []
        for workunit in workunits:
            if not self._should_deduplicate(workunit):
                filtered_workunits.append(workunit)
        
        if not filtered_workunits:
            logger.debug("All workunits were duplicates, skipping batch")
            return results
        
        try:
            # Process in chunks to respect payload limits
            chunks = self._chunk_workunits(filtered_workunits)
            
            for chunk in chunks:
                chunk_results = self._emit_chunk(chunk, session)
                results.extend(chunk_results)
            
            self._metrics["batch_count"] += 1
            self._metrics["emitted_count"] += len(filtered_workunits)
            
            if callback:
                callback(results)
                
        except Exception as e:
            logger.error(f"Failed to emit batch: {e}")
            # Create failed results for all workunits
            for workunit in filtered_workunits:
                results.append(EmitResult(
                    workunit_id=workunit.id,
                    status=EmitStatus.FAILED,
                    error=e,
                    message=str(e)
                ))
            self._metrics["error_count"] += len(filtered_workunits)
            if callback:
                callback(results)
        
        return results
    
    def _chunk_workunits(
        self,
        workunits: Sequence[Union[MetadataWorkUnit, MCPWorkUnit]]
    ) -> List[List[Union[MetadataWorkUnit, MCPWorkUnit]]]:
        """Split workunits into chunks based on size limits."""
        chunks = []
        current_chunk = []
        current_size = 0
        
        for workunit in workunits:
            # Estimate workunit size
            workunit_size = self._estimate_workunit_size(workunit)
            
            if (current_chunk and 
                (len(current_chunk) >= self.config.batch_size or 
                 current_size + workunit_size > self.config.max_payload_bytes)):
                chunks.append(current_chunk)
                current_chunk = []
                current_size = 0
            
            current_chunk.append(workunit)
            current_size += workunit_size
        
        if current_chunk:
            chunks.append(current_chunk)
        
        return chunks
    
    def _estimate_workunit_size(self, workunit: Union[MetadataWorkUnit, MCPWorkUnit]) -> int:
        """Estimate the size of a workunit in bytes."""
        try:
            if isinstance(workunit, MCPWorkUnit):
                return len(json.dumps(workunit.get_metadata()).encode())
            else:
                return len(json.dumps(workunit.aspect).encode())
        except Exception:
            # Fallback to a reasonable default
            return 1024
    
    def _emit_chunk(
        self,
        workunits: List[Union[MetadataWorkUnit, MCPWorkUnit]],
        session: requests.Session,
    ) -> List[EmitResult]:
        """Emit a chunk of workunits."""
        results = []
        
        for workunit in workunits:
            try:
                result = self._emit_single(workunit, session)
                results.append(result)
                
                # Update metrics
                if result.status == EmitStatus.SUCCESS:
                    self._metrics["success_count"] += 1
                elif result.status == EmitStatus.FAILED:
                    self._metrics["error_count"] += 1
                elif result.status == EmitStatus.RETRY:
                    self._metrics["retry_count"] += 1
                    
            except Exception as e:
                logger.error(f"Failed to emit workunit {workunit.id}: {e}")
                results.append(EmitResult(
                    workunit_id=workunit.id,
                    status=EmitStatus.FAILED,
                    error=e,
                    message=str(e)
                ))
                self._metrics["error_count"] += 1
        
        return results
    
    def flush(self) -> None:
        """Flush any pending workunits."""
        # Base implementation - subclasses can override
        pass
    
    def close(self) -> None:
        """Close the emitter and cleanup resources."""
        if self._session:
            self._session.close()
            self._session = None
    
    def get_metrics(self) -> Dict[str, Any]:
        """Get emitter metrics."""
        return self._metrics.copy()
    
    def reset_metrics(self) -> None:
        """Reset emitter metrics."""
        self._metrics = {
            "emitted_count": 0,
            "success_count": 0,
            "error_count": 0,
            "retry_count": 0,
            "batch_count": 0,
        }
        self._dedup_cache.clear()


class DataGuildRestEmitter(BaseEmitter):
    """REST-based emitter for DataGuild platform."""
    
    def _create_session(self) -> requests.Session:
        """Create and configure the HTTP session."""
        session = requests.Session()
        
        # Setup headers
        headers = {
            "Content-Type": "application/json",
            "User-Agent": f"DataGuild-Snowflake-Connector/1.0",
        }
        
        if self.config.token:
            headers["Authorization"] = f"Bearer {self.config.token}"
        
        headers.update(self.config.custom_headers)
        session.headers.update(headers)
        
        # Setup retry strategy
        retry_strategy = Retry(
            total=self.config.retry_max_times,
            status_forcelist=self.config.retry_status_codes,
            backoff_factor=self.config.retry_backoff_factor,
            raise_on_status=False,
        )
        
        adapter = HTTPAdapter(
            pool_connections=100,
            pool_maxsize=100,
            max_retries=retry_strategy
        )
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        
        # Setup SSL
        if self.config.ca_certificate_path:
            session.verify = self.config.ca_certificate_path
        elif self.config.disable_ssl_verification:
            session.verify = False
        
        # Setup timeout
        original_request = session.request
        
        def request_with_timeout(*args, **kwargs):
            if 'timeout' not in kwargs:
                kwargs['timeout'] = (self.config.connect_timeout_sec, self.config.read_timeout_sec)
            return original_request(*args, **kwargs)
        
        session.request = request_with_timeout
        
        return session
    
    def _emit_single(
        self,
        workunit: Union[MetadataWorkUnit, MCPWorkUnit],
        session: requests.Session,
    ) -> EmitResult:
        """Emit a single workunit via REST API."""
        try:
            # Convert workunit to JSON payload
            payload = self._workunit_to_payload(workunit)
            
            # Determine endpoint based on workunit type
            if isinstance(workunit, MCPWorkUnit):
                endpoint = "/api/v1/metadata/ingest"
            else:
                endpoint = "/api/v1/metadata/ingest"
            
            url = urljoin(self.config.server_url, endpoint)
            
            # Make request
            response = session.post(url, json=payload)
            response.raise_for_status()
            
            return EmitResult(
                workunit_id=workunit.id,
                status=EmitStatus.SUCCESS,
                message="Successfully emitted"
            )
            
        except HTTPError as e:
            logger.error(f"HTTP error emitting workunit {workunit.id}: {e}")
            return EmitResult(
                workunit_id=workunit.id,
                status=EmitStatus.FAILED,
                error=e,
                message=f"HTTP error: {e.response.status_code}"
            )
        except RequestException as e:
            logger.error(f"Request error emitting workunit {workunit.id}: {e}")
            return EmitResult(
                workunit_id=workunit.id,
                status=EmitStatus.RETRY,
                error=e,
                message=f"Request error: {str(e)}"
            )
        except Exception as e:
            logger.error(f"Unexpected error emitting workunit {workunit.id}: {e}")
            return EmitResult(
                workunit_id=workunit.id,
                status=EmitStatus.FAILED,
                error=e,
                message=f"Unexpected error: {str(e)}"
            )
    
    def _workunit_to_payload(self, workunit: Union[MetadataWorkUnit, MCPWorkUnit]) -> Dict[str, Any]:
        """Convert workunit to API payload with proper serialization."""
        if isinstance(workunit, MCPWorkUnit):
            return {
                "workunit_id": workunit.id,
                "mcp": self._safe_serialize(workunit.mcp.to_dict()),
                "priority": workunit.priority,
                "batch_id": workunit.batch_id,
                "created_at": self._safe_timestamp(workunit.created_at),
            }
        else:
            # Handle both urn attribute and fallback to id
            urn = getattr(workunit, 'urn', workunit.id)
            aspect_name = getattr(workunit, 'aspect_name', 'unknown')
            aspect = getattr(workunit, 'aspect', getattr(workunit, 'metadata', {}))
            created_at = getattr(workunit, 'created_at', 
                               getattr(workunit, 'created_timestamp', 
                                      datetime.now()))
            
            return {
                "workunit_id": workunit.id,
                "urn": urn,
                "aspect_name": aspect_name,
                "aspect": self._safe_serialize(aspect),
                "created_at": self._safe_timestamp(created_at),
            }
    
    def _safe_serialize(self, obj: Any) -> Any:
        """Safely serialize objects to JSON-compatible format."""
        if obj is None:
            return None
        
        # Handle datetime objects
        if isinstance(obj, datetime):
            return obj.isoformat()
        
        # Handle enum objects
        if hasattr(obj, 'value'):
            return obj.value
        
        # Handle TimeWindowUnit specifically
        if hasattr(obj, '__class__') and 'TimeWindowUnit' in str(obj.__class__):
            return str(obj)
        
        # Handle dictionaries
        if isinstance(obj, dict):
            return {k: self._safe_serialize(v) for k, v in obj.items()}
        
        # Handle lists
        if isinstance(obj, (list, tuple)):
            return [self._safe_serialize(item) for item in obj]
        
        # Handle objects with to_dict method
        if hasattr(obj, 'to_dict'):
            try:
                return self._safe_serialize(obj.to_dict())
            except Exception:
                return str(obj)
        
        # Handle objects with model_dump method (Pydantic v2)
        if hasattr(obj, 'model_dump'):
            try:
                return self._safe_serialize(obj.model_dump())
            except Exception:
                return str(obj)
        
        # Handle objects with dict method (Pydantic v1)
        if hasattr(obj, 'dict'):
            try:
                return self._safe_serialize(obj.dict())
            except Exception:
                return str(obj)
        
        # For other objects, try to convert to string
        try:
            # Check if it's JSON serializable
            json.dumps(obj)
            return obj
        except (TypeError, ValueError):
            return str(obj)
    
    def _safe_timestamp(self, timestamp: Any) -> str:
        """Safely convert timestamp to ISO format string."""
        if timestamp is None:
            return datetime.now().isoformat()
        
        if isinstance(timestamp, datetime):
            return timestamp.isoformat()
        
        if isinstance(timestamp, (int, float)):
            # Assume it's a Unix timestamp
            return datetime.fromtimestamp(timestamp).isoformat()
        
        if hasattr(timestamp, 'isoformat'):
            return timestamp.isoformat()
        
        return str(timestamp)


class DataGuildKafkaEmitter(BaseEmitter):
    """Kafka-based emitter for DataGuild platform."""
    
    def __init__(self, config: EmitterConfig, kafka_config: Dict[str, Any]):
        super().__init__(config)
        self.kafka_config = kafka_config
        self._producer = None
        self._setup_kafka()
    
    def _setup_kafka(self) -> None:
        """Setup Kafka producer."""
        try:
            from confluent_kafka import Producer
            
            self._producer = Producer(self.kafka_config)
            logger.info("Kafka producer initialized successfully")
        except ImportError:
            raise ConfigurationError("confluent-kafka is required for Kafka emitter")
        except Exception as e:
            raise ConfigurationError(f"Failed to initialize Kafka producer: {e}")
    
    def _create_session(self) -> requests.Session:
        """Kafka emitter doesn't use HTTP sessions."""
        return None
    
    def _emit_single(
        self,
        workunit: Union[MetadataWorkUnit, MCPWorkUnit],
        session: requests.Session,
    ) -> EmitResult:
        """Emit a single workunit via Kafka."""
        try:
            # Convert workunit to message
            message = self._workunit_to_message(workunit)
            
            # Determine topic
            topic = self.kafka_config.get("topic", "dataguild-metadata")
            
            # Produce message
            self._producer.produce(
                topic=topic,
                key=workunit.id,
                value=json.dumps(message).encode(),
                callback=self._delivery_callback
            )
            
            # Flush to ensure delivery
            self._producer.flush(timeout=1.0)
            
            return EmitResult(
                workunit_id=workunit.id,
                status=EmitStatus.SUCCESS,
                message="Successfully produced to Kafka"
            )
            
        except Exception as e:
            logger.error(f"Kafka error emitting workunit {workunit.id}: {e}")
            return EmitResult(
                workunit_id=workunit.id,
                status=EmitStatus.FAILED,
                error=e,
                message=f"Kafka error: {str(e)}"
            )
    
    def _workunit_to_message(self, workunit: Union[MetadataWorkUnit, MCPWorkUnit]) -> Dict[str, Any]:
        """Convert workunit to Kafka message with proper serialization."""
        if isinstance(workunit, MCPWorkUnit):
            return {
                "type": "mcp",
                "workunit_id": workunit.id,
                "mcp": self._safe_serialize(workunit.mcp.to_dict()),
                "priority": workunit.priority,
                "batch_id": workunit.batch_id,
                "created_at": self._safe_timestamp(workunit.created_at),
            }
        else:
            # Handle both urn attribute and fallback to id
            urn = getattr(workunit, 'urn', workunit.id)
            aspect_name = getattr(workunit, 'aspect_name', 'unknown')
            aspect = getattr(workunit, 'aspect', getattr(workunit, 'metadata', {}))
            created_at = getattr(workunit, 'created_at', 
                               getattr(workunit, 'created_timestamp', 
                                      datetime.now()))
            
            return {
                "type": "metadata",
                "workunit_id": workunit.id,
                "urn": urn,
                "aspect_name": aspect_name,
                "aspect": self._safe_serialize(aspect),
                "created_at": self._safe_timestamp(created_at),
            }
    
    def _safe_serialize(self, obj: Any) -> Any:
        """Safely serialize objects to JSON-compatible format."""
        if obj is None:
            return None
        
        # Handle datetime objects
        if isinstance(obj, datetime):
            return obj.isoformat()
        
        # Handle enum objects
        if hasattr(obj, 'value'):
            return obj.value
        
        # Handle TimeWindowUnit specifically
        if hasattr(obj, '__class__') and 'TimeWindowUnit' in str(obj.__class__):
            return str(obj)
        
        # Handle dictionaries
        if isinstance(obj, dict):
            return {k: self._safe_serialize(v) for k, v in obj.items()}
        
        # Handle lists
        if isinstance(obj, (list, tuple)):
            return [self._safe_serialize(item) for item in obj]
        
        # Handle objects with to_dict method
        if hasattr(obj, 'to_dict'):
            try:
                return self._safe_serialize(obj.to_dict())
            except Exception:
                return str(obj)
        
        # Handle objects with model_dump method (Pydantic v2)
        if hasattr(obj, 'model_dump'):
            try:
                return self._safe_serialize(obj.model_dump())
            except Exception:
                return str(obj)
        
        # Handle objects with dict method (Pydantic v1)
        if hasattr(obj, 'dict'):
            try:
                return self._safe_serialize(obj.dict())
            except Exception:
                return str(obj)
        
        # For other objects, try to convert to string
        try:
            # Check if it's JSON serializable
            json.dumps(obj)
            return obj
        except (TypeError, ValueError):
            return str(obj)
    
    def _safe_timestamp(self, timestamp: Any) -> str:
        """Safely convert timestamp to ISO format string."""
        if timestamp is None:
            return datetime.now().isoformat()
        
        if isinstance(timestamp, datetime):
            return timestamp.isoformat()
        
        if isinstance(timestamp, (int, float)):
            # Assume it's a Unix timestamp
            return datetime.fromtimestamp(timestamp).isoformat()
        
        if hasattr(timestamp, 'isoformat'):
            return timestamp.isoformat()
        
        return str(timestamp)
    
    def _delivery_callback(self, err, msg):
        """Kafka delivery callback."""
        if err:
            logger.error(f"Message delivery failed: {err}")
        else:
            logger.debug(f"Message delivered to {msg.topic()} [{msg.partition()}]")


class CompositeEmitter(BaseEmitter):
    """Composite emitter that can use multiple emitters."""
    
    def __init__(self, emitters: List[BaseEmitter]):
        # Use the first emitter's config as the base
        super().__init__(emitters[0].config if emitters else EmitterConfig(server_url=""))
        self.emitters = emitters
    
    def _create_session(self) -> requests.Session:
        """Composite emitter doesn't create its own session."""
        return None
    
    def _emit_single(
        self,
        workunit: Union[MetadataWorkUnit, MCPWorkUnit],
        session: requests.Session,
    ) -> EmitResult:
        """Emit to all configured emitters."""
        results = []
        
        for emitter in self.emitters:
            try:
                result = emitter._emit_single(workunit, session)
                results.append(result)
            except Exception as e:
                logger.error(f"Error in composite emitter: {e}")
                results.append(EmitResult(
                    workunit_id=workunit.id,
                    status=EmitStatus.FAILED,
                    error=e,
                    message=str(e)
                ))
        
        # Return the first successful result, or the first result if none succeeded
        for result in results:
            if result.status == EmitStatus.SUCCESS:
                return result
        
        return results[0] if results else EmitResult(
            workunit_id=workunit.id,
            status=EmitStatus.FAILED,
            message="No emitters available"
        )
    
    def close(self) -> None:
        """Close all emitters."""
        for emitter in self.emitters:
            emitter.close()


class AdvancedBatchedEmitter(BaseEmitter):
    """Advanced batched emitter with intelligent batching and retry logic."""
    
    def __init__(self, config: EmitterConfig, base_emitter: BaseEmitter):
        super().__init__(config)
        self.base_emitter = base_emitter
        self._pending_workunits: List[Union[MetadataWorkUnit, MCPWorkUnit]] = []
        self._batch_timer: Optional[float] = None
        self._lock = asyncio.Lock()
    
    def _create_session(self) -> requests.Session:
        """Use the base emitter's session."""
        return self.base_emitter._get_session()
    
    def _emit_single(
        self,
        workunit: Union[MetadataWorkUnit, MCPWorkUnit],
        session: requests.Session,
    ) -> EmitResult:
        """Add workunit to batch instead of emitting immediately."""
        self._pending_workunits.append(workunit)
        
        # Check if we should process the batch
        if (len(self._pending_workunits) >= self.config.batch_size or
            (self._batch_timer and time.time() - self._batch_timer >= self.config.batch_timeout_sec)):
            return self._process_batch()
        
        # Start batch timer if this is the first workunit
        if not self._batch_timer:
            self._batch_timer = time.time()
        
        return EmitResult(
            workunit_id=workunit.id,
            status=EmitStatus.PENDING,
            message="Added to batch"
        )
    
    def _process_batch(self) -> EmitResult:
        """Process the current batch of workunits."""
        if not self._pending_workunits:
            return EmitResult(
                workunit_id="batch",
                status=EmitStatus.SUCCESS,
                message="No workunits to process"
            )
        
        try:
            # Emit the batch using the base emitter
            results = self.base_emitter.emit_batch(self._pending_workunits)
            
            # Clear the batch
            self._pending_workunits.clear()
            self._batch_timer = None
            
            # Return success if all workunits succeeded
            if all(result.status == EmitStatus.SUCCESS for result in results):
                return EmitResult(
                    workunit_id="batch",
                    status=EmitStatus.SUCCESS,
                    message=f"Successfully processed batch of {len(results)} workunits"
                )
            else:
                return EmitResult(
                    workunit_id="batch",
                    status=EmitStatus.FAILED,
                    message=f"Batch processing completed with errors: {len([r for r in results if r.status != EmitStatus.SUCCESS])} failures"
                )
                
        except Exception as e:
            logger.error(f"Failed to process batch: {e}")
            return EmitResult(
                workunit_id="batch",
                status=EmitStatus.FAILED,
                error=e,
                message=f"Batch processing failed: {str(e)}"
            )
    
    def flush(self) -> None:
        """Flush any pending workunits."""
        if self._pending_workunits:
            self._process_batch()
    
    def close(self) -> None:
        """Close the emitter and flush pending workunits."""
        self.flush()
        self.base_emitter.close()


# Factory functions
def create_rest_emitter(config: EmitterConfig) -> DataGuildRestEmitter:
    """Create a REST-based emitter."""
    return DataGuildRestEmitter(config)


def create_kafka_emitter(config: EmitterConfig, kafka_config: Dict[str, Any]) -> DataGuildKafkaEmitter:
    """Create a Kafka-based emitter."""
    return DataGuildKafkaEmitter(config, kafka_config)


def create_composite_emitter(emitters: List[BaseEmitter]) -> CompositeEmitter:
    """Create a composite emitter."""
    return CompositeEmitter(emitters)


def create_batched_emitter(config: EmitterConfig, base_emitter: BaseEmitter) -> AdvancedBatchedEmitter:
    """Create an advanced batched emitter."""
    return AdvancedBatchedEmitter(config, base_emitter)


# Export all classes and functions
__all__ = [
    # Enums
    'EmitMode',
    'EmitStatus',
    
    # Data classes
    'EmitResult',
    'EmitterConfig',
    
    # Protocols
    'Emitter',
    
    # Base classes
    'BaseEmitter',
    
    # Implementations
    'DataGuildRestEmitter',
    'DataGuildKafkaEmitter',
    'CompositeEmitter',
    'AdvancedBatchedEmitter',
    
    # Factory functions
    'create_rest_emitter',
    'create_kafka_emitter',
    'create_composite_emitter',
    'create_batched_emitter',
]
