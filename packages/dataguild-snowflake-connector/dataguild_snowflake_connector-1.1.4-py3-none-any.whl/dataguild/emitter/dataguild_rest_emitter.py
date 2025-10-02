"""
DataGuild REST Emitter - enterprise Compatible Implementation

Enterprise-grade REST emitter with comprehensive error handling, batching,
retry logic, and observability features inspired by enterprise's best practices.
"""

import asyncio
import functools
import json
import logging
import time
import uuid
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
from typing import Any, Dict, List, Optional, Sequence, Union, Callable
from urllib.parse import urljoin

import requests
from requests.adapters import HTTPAdapter, Retry
from requests.exceptions import HTTPError, RequestException, Timeout

from dataguild.api.workunit import MetadataWorkUnit
from dataguild.configuration.common import ConfigModel, ConfigurationError, OperationalError
from dataguild.emitter.mcp import (
    MetadataChangeProposal,
    MetadataChangeProposalWrapper,
    MetadataChangeEvent,
)

logger = logging.getLogger(__name__)

# Constants
_DEFAULT_TIMEOUT_SEC = 30
_TIMEOUT_LOWER_BOUND_SEC = 1
_DEFAULT_RETRY_STATUS_CODES = [429, 500, 502, 503, 504]
_DEFAULT_RETRY_METHODS = ["HEAD", "GET", "POST", "PUT", "DELETE", "OPTIONS", "TRACE"]
_DEFAULT_RETRY_MAX_TIMES = 4
_INGEST_MAX_PAYLOAD_BYTES = 15 * 1024 * 1024  # 15MB


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
    trace_id: Optional[str] = None


@dataclass
class TraceData:
    """Trace data for async operations."""
    trace_id: str
    status: str
    created_at: datetime = field(default_factory=datetime.now)


class DataGuildRestEmitterConfig(ConfigModel):
    """Configuration for the DataGuild REST emitter."""
    # Connection settings
    server_url: str
    token: Optional[str] = None
    timeout_sec: float = _DEFAULT_TIMEOUT_SEC
    connect_timeout_sec: float = 10.0
    read_timeout_sec: float = 30.0
    
    # Retry settings
    retry_max_times: int = _DEFAULT_RETRY_MAX_TIMES
    retry_backoff_factor: float = 2.0
    retry_status_codes: List[int] = [500, 502, 503, 504, 429]
    
    # Batching settings
    batch_size: int = 100
    batch_timeout_sec: float = 5.0
    max_payload_bytes: int = _INGEST_MAX_PAYLOAD_BYTES
    
    # Performance settings
    max_workers: int = 10
    enable_deduplication: bool = True
    enable_compression: bool = True
    
    # Advanced settings
    enable_tracing: bool = True
    trace_timeout_sec: float = 3600.0
    enable_circuit_breaker: bool = True
    circuit_breaker_failure_threshold: int = 5
    circuit_breaker_timeout_sec: float = 60.0


class CircuitBreaker:
    """Circuit breaker pattern for fault tolerance."""
    
    def __init__(self, failure_threshold: int = 5, timeout_sec: float = 60.0):
        self.failure_threshold = failure_threshold
        self.timeout_sec = timeout_sec
        self.failure_count = 0
        self.last_failure_time = None
        self.state = "CLOSED"  # CLOSED, OPEN, HALF_OPEN
    
    def can_execute(self) -> bool:
        """Check if the circuit breaker allows execution."""
        if self.state == "CLOSED":
            return True
        elif self.state == "OPEN":
            if self.last_failure_time and time.time() - self.last_failure_time > self.timeout_sec:
                self.state = "HALF_OPEN"
                return True
            return False
        else:  # HALF_OPEN
            return True
    
    def record_success(self):
        """Record a successful operation."""
        self.failure_count = 0
        self.state = "CLOSED"
    
    def record_failure(self):
        """Record a failed operation."""
        self.failure_count += 1
        self.last_failure_time = time.time()
        
        if self.failure_count >= self.failure_threshold:
            self.state = "OPEN"


class DataGuildRestEmitter:
    """
    DataGuild REST Emitter - enterprise Compatible Implementation.
    
    Features:
    - enterprise-compatible API endpoints
    - Advanced batching with chunking
    - Circuit breaker pattern
    - Async processing with tracing
    - Comprehensive error handling
    - Retry logic with exponential backoff
    """
    
    def __init__(self, config: DataGuildRestEmitterConfig):
        self.config = config
        self._session = None
        self._circuit_breaker = CircuitBreaker(
            config.circuit_breaker_failure_threshold,
            config.circuit_breaker_timeout_sec
        ) if config.enable_circuit_breaker else None
        self._pending_traces: Dict[str, TraceData] = {}
        self._batch_buffer: List[MetadataChangeProposal] = []
        self._batch_lock = asyncio.Lock()
        
        # Initialize session
        self._build_session()
    
    def _build_session(self) -> requests.Session:
        """Build and configure the requests session."""
        session = requests.Session()
        
        # Set headers
        session.headers.update({
            "Content-Type": "application/json",
            "User-Agent": f"DataGuild-Client/1.0 (rest; {self.config.server_url})",
        })
        
        if self.config.token:
            session.headers["Authorization"] = f"Bearer {self.config.token}"
        
        # Configure retry strategy
        retry_strategy = Retry(
            total=self.config.retry_max_times,
            status_forcelist=self.config.retry_status_codes,
            backoff_factor=self.config.retry_backoff_factor,
            allowed_methods=self.config.retry_max_times,
            raise_on_status=False,
        )
        
        adapter = HTTPAdapter(
            pool_connections=100,
            pool_maxsize=100,
            max_retries=retry_strategy
        )
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        
        # Set timeout
        if self.config.timeout_sec:
            session.request = functools.partial(
                session.request,
                timeout=self.config.timeout_sec
            )
        
        self._session = session
        return session
    
    def test_connection(self) -> bool:
        """Test connection to the DataGuild server."""
        try:
            if not self._circuit_breaker or self._circuit_breaker.can_execute():
                response = self._session.get(f"{self.config.server_url}/health")
                response.raise_for_status()
                
                if self._circuit_breaker:
                    self._circuit_breaker.record_success()
                
                logger.info("✅ DataGuild server connection successful")
                return True
            else:
                logger.warning("⚠️ Circuit breaker is OPEN, connection test skipped")
                return False
                
        except Exception as e:
            if self._circuit_breaker:
                self._circuit_breaker.record_failure()
            logger.error(f"❌ DataGuild server connection failed: {e}")
            return False
    
    def emit_mcp(
        self,
        mcp: Union[MetadataChangeProposal, MetadataChangeProposalWrapper],
        emit_mode: EmitMode = EmitMode.SYNC,
        wait_timeout: Optional[timedelta] = None
    ) -> EmitResult:
        """Emit a single MetadataChangeProposal."""
        if not self._circuit_breaker or self._circuit_breaker.can_execute():
            try:
                # Prepare MCP for emission
                mcp_obj = self._prepare_mcp(mcp)
                
                # Build payload
                payload_dict = {
                    "proposal": mcp_obj,
                    "async": "true" if emit_mode in (EmitMode.ASYNC, EmitMode.ASYNC_WAIT) else "false"
                }
                
                # Emit to server
                url = f"{self.config.server_url}/aspects?action=ingestProposal"
                response = self._emit_generic(url, json.dumps(payload_dict))
                
                # Handle tracing for async operations
                trace_data = None
                if emit_mode == EmitMode.ASYNC_WAIT and self.config.enable_tracing:
                    trace_data = self._extract_trace_data(response)
                    if trace_data:
                        self._pending_traces[trace_data.trace_id] = trace_data
                
                # Record success
                if self._circuit_breaker:
                    self._circuit_breaker.record_success()
                
                return EmitResult(
                    workunit_id=mcp.entityUrn,
                    status=EmitStatus.SUCCESS,
                    message="Successfully emitted MCP",
                    trace_id=trace_data.trace_id if trace_data else None
                )
                
            except Exception as e:
                if self._circuit_breaker:
                    self._circuit_breaker.record_failure()
                
                logger.error(f"Failed to emit MCP {mcp.entityUrn}: {e}")
                return EmitResult(
                    workunit_id=mcp.entityUrn,
                    status=EmitStatus.FAILED,
                    error=e,
                    message=str(e)
                )
        else:
            return EmitResult(
                workunit_id=getattr(mcp, 'entityUrn', 'unknown'),
                status=EmitStatus.FAILED,
                message="Circuit breaker is OPEN"
            )
    
    async def emit_mcps_batch(
        self,
        mcps: Sequence[Union[MetadataChangeProposal, MetadataChangeProposalWrapper]],
        emit_mode: EmitMode = EmitMode.BATCH
    ) -> List[EmitResult]:
        """Emit multiple MCPs in batches."""
        if not mcps:
            return []
        
        results = []
        
        # Chunk large batches
        chunks = self._chunk_mcps(mcps)
        
        for chunk in chunks:
            try:
                # Prepare chunk for emission
                mcp_objs = [self._prepare_mcp(mcp) for mcp in chunk]
                
                # Build batch payload
                payload_dict = {
                    "proposals": mcp_objs,
                    "async": "true" if emit_mode in (EmitMode.ASYNC, EmitMode.ASYNC_WAIT) else "false"
                }
                
                # Emit batch
                url = f"{self.config.server_url}/aspects?action=ingestProposal"
                response = self._emit_generic(url, json.dumps(payload_dict))
                
                # Record success for all MCPs in chunk
                for mcp in chunk:
                    results.append(EmitResult(
                        workunit_id=mcp.entityUrn,
                        status=EmitStatus.SUCCESS,
                        message="Successfully emitted in batch"
                    ))
                
                if self._circuit_breaker:
                    self._circuit_breaker.record_success()
                
            except Exception as e:
                if self._circuit_breaker:
                    self._circuit_breaker.record_failure()
                
                # Record failure for all MCPs in chunk
                for mcp in chunk:
                    results.append(EmitResult(
                        workunit_id=mcp.entityUrn,
                        status=EmitStatus.FAILED,
                        error=e,
                        message=f"Batch emission failed: {str(e)}"
                    ))
        
        return results
    
    def emit_workunit(self, workunit: MetadataWorkUnit) -> EmitResult:
        """Emit a DataGuild MetadataWorkUnit."""
        try:
            # Convert workunit to MCP if it has mcp_raw
            if hasattr(workunit, 'mcp_raw') and workunit.mcp_raw:
                mcp = self._workunit_to_mcp(workunit)
                return self.emit_mcp(mcp)
            else:
                # Emit as raw metadata
                return self._emit_raw_metadata(workunit)
                
        except Exception as e:
            logger.error(f"Failed to emit workunit {workunit.id}: {e}")
            return EmitResult(
                workunit_id=workunit.id,
                status=EmitStatus.FAILED,
                error=e,
                message=str(e)
            )
    
    def _prepare_mcp(self, mcp: Union[MetadataChangeProposal, MetadataChangeProposalWrapper]) -> Dict[str, Any]:
        """Prepare MCP for emission."""
        if isinstance(mcp, MetadataChangeProposalWrapper):
            return mcp.to_obj()
        else:
            return mcp.to_obj()
    
    def _workunit_to_mcp(self, workunit: MetadataWorkUnit) -> MetadataChangeProposal:
        """Convert DataGuild workunit to MCP."""
        mcp_raw = workunit.mcp_raw
        
        return MetadataChangeProposal(
            entityType=mcp_raw.get("entityType", "dataset"),
            changeType=mcp_raw.get("changeType", "UPSERT"),
            entityUrn=mcp_raw.get("entityUrn", workunit.id),
            aspectName=mcp_raw.get("aspectName", "unknown"),
            aspect=mcp_raw.get("aspect", {}),
            systemMetadata=mcp_raw.get("systemMetadata", {})
        )
    
    def _emit_raw_metadata(self, workunit: MetadataWorkUnit) -> EmitResult:
        """Emit raw metadata without MCP conversion."""
        try:
            # Emit to custom DataGuild endpoint
            url = f"{self.config.server_url}/metadata/ingest"
            payload = {
                "workunit_id": workunit.id,
                "metadata_type": type(workunit).__name__,
                "metadata": workunit.metadata if hasattr(workunit, 'metadata') else {},
                "timestamp": datetime.now().isoformat()
            }
            
            response = self._emit_generic(url, json.dumps(payload))
            
            return EmitResult(
                workunit_id=workunit.id,
                status=EmitStatus.SUCCESS,
                message="Successfully emitted raw metadata"
            )
            
        except Exception as e:
            return EmitResult(
                workunit_id=workunit.id,
                status=EmitStatus.FAILED,
                error=e,
                message=str(e)
            )
    
    def _chunk_mcps(self, mcps: Sequence[MetadataChangeProposal]) -> List[List[MetadataChangeProposal]]:
        """Chunk MCPs to respect payload size limits."""
        chunks = []
        current_chunk = []
        current_size = 0
        
        for mcp in mcps:
            mcp_size = len(json.dumps(self._prepare_mcp(mcp)))
            
            if current_size + mcp_size > self.config.max_payload_bytes and current_chunk:
                chunks.append(current_chunk)
                current_chunk = [mcp]
                current_size = mcp_size
            else:
                current_chunk.append(mcp)
                current_size += mcp_size
        
        if current_chunk:
            chunks.append(current_chunk)
        
        return chunks
    
    def _emit_generic(self, url: str, payload: Union[str, Dict[str, Any]]) -> requests.Response:
        """Generic emission method with error handling."""
        if not isinstance(payload, str):
            payload = json.dumps(payload)
        
        payload_size = len(payload)
        if payload_size > self.config.max_payload_bytes:
            logger.warning(
                f"Payload size ({payload_size}) exceeds limit ({self.config.max_payload_bytes})"
            )
        
        logger.debug(f"Emitting to {url} (size: {payload_size} bytes)")
        
        try:
            response = self._session.post(url, data=payload)
            response.raise_for_status()
            return response
            
        except HTTPError as e:
            try:
                error_info = response.json()
                raise OperationalError(
                    f"Failed to emit to DataGuild server: {error_info.get('message', str(e))}",
                    error_info
                ) from e
            except (json.JSONDecodeError, AttributeError):
                raise OperationalError(
                    f"Failed to emit to DataGuild server: {str(e)}"
                ) from e
                
        except RequestException as e:
            raise OperationalError(
                f"Network error emitting to DataGuild server: {str(e)}"
            ) from e
    
    def _extract_trace_data(self, response: requests.Response) -> Optional[TraceData]:
        """Extract trace data from response for async operations."""
        try:
            response_data = response.json()
            trace_id = response_data.get("traceId")
            if trace_id:
                return TraceData(
                    trace_id=trace_id,
                    status=response_data.get("status", "PENDING")
                )
        except (json.JSONDecodeError, KeyError):
            pass
        return None
    
    async def await_traces(self, timeout_sec: float = 3600.0) -> Dict[str, EmitStatus]:
        """Await completion of pending traces."""
        if not self._pending_traces:
            return {}
        
        start_time = time.time()
        results = {}
        
        while self._pending_traces and (time.time() - start_time) < timeout_sec:
            for trace_id, trace_data in list(self._pending_traces.items()):
                try:
                    # Check trace status
                    status_url = f"{self.config.server_url}/traces/{trace_id}/status"
                    response = self._session.get(status_url)
                    
                    if response.status_code == 200:
                        status_data = response.json()
                        status = status_data.get("status", "PENDING")
                        
                        if status in ["SUCCESS", "FAILED"]:
                            results[trace_id] = EmitStatus.SUCCESS if status == "SUCCESS" else EmitStatus.FAILED
                            del self._pending_traces[trace_id]
                        else:
                            trace_data.status = status
                    
                except Exception as e:
                    logger.debug(f"Error checking trace {trace_id}: {e}")
            
            if self._pending_traces:
                await asyncio.sleep(1.0)  # Wait 1 second before next check
        
        # Mark remaining traces as failed due to timeout
        for trace_id in self._pending_traces:
            results[trace_id] = EmitStatus.FAILED
        
        return results
    
    def close(self):
        """Close the emitter and clean up resources."""
        if self._session:
            self._session.close()
        
        # Await any pending traces
        if self._pending_traces:
            logger.info(f"Awaiting {len(self._pending_traces)} pending traces...")
            # Note: In a real implementation, you'd want to properly await this
            self._pending_traces.clear()
        
        logger.info("DataGuild REST emitter closed")


# Factory function
def create_dataguild_rest_emitter(
    server_url: str,
    token: Optional[str] = None,
    **kwargs
) -> DataGuildRestEmitter:
    """Create a DataGuild REST emitter with the given configuration."""
    config = DataGuildRestEmitterConfig(
        server_url=server_url,
        token=token,
        **kwargs
    )
    return DataGuildRestEmitter(config)

