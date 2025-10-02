"""
DataGuild Snowflake Error Handling and Validation

Comprehensive error handling, validation, and recovery mechanisms for the
Snowflake connector to ensure robust operation in production environments.
"""

import logging
import traceback
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional, Union, Callable
from functools import wraps
import json

logger = logging.getLogger(__name__)


class ErrorSeverity(Enum):
    """Error severity levels for classification and handling."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class ErrorCategory(Enum):
    """Error categories for better classification and handling."""
    CONNECTION = "connection"
    PERMISSION = "permission"
    QUERY = "query"
    SERIALIZATION = "serialization"
    CONFIGURATION = "configuration"
    NETWORK = "network"
    TIMEOUT = "timeout"
    VALIDATION = "validation"
    UNKNOWN = "unknown"


class SnowflakeConnectorError(Exception):
    """Base exception for Snowflake connector errors."""
    
    def __init__(
        self,
        message: str,
        category: ErrorCategory = ErrorCategory.UNKNOWN,
        severity: ErrorSeverity = ErrorSeverity.MEDIUM,
        details: Optional[Dict[str, Any]] = None,
        recoverable: bool = True,
        original_error: Optional[Exception] = None
    ):
        super().__init__(message)
        self.message = message
        self.category = category
        self.severity = severity
        self.details = details or {}
        self.recoverable = recoverable
        self.original_error = original_error
        self.timestamp = datetime.now()
        self.traceback = traceback.format_exc()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert error to dictionary for serialization."""
        return {
            "message": self.message,
            "category": self.category.value,
            "severity": self.severity.value,
            "details": self.details,
            "recoverable": self.recoverable,
            "timestamp": self.timestamp.isoformat(),
            "traceback": self.traceback,
            "original_error": str(self.original_error) if self.original_error else None
        }


class ConnectionError(SnowflakeConnectorError):
    """Connection-related errors."""
    
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None, original_error: Optional[Exception] = None):
        super().__init__(
            message=message,
            category=ErrorCategory.CONNECTION,
            severity=ErrorSeverity.HIGH,
            details=details,
            recoverable=True,
            original_error=original_error
        )


class PermissionError(SnowflakeConnectorError):
    """Permission-related errors."""
    
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None, original_error: Optional[Exception] = None):
        super().__init__(
            message=message,
            category=ErrorCategory.PERMISSION,
            severity=ErrorSeverity.HIGH,
            details=details,
            recoverable=False,
            original_error=original_error
        )


class QueryError(SnowflakeConnectorError):
    """Query execution errors."""
    
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None, original_error: Optional[Exception] = None):
        super().__init__(
            message=message,
            category=ErrorCategory.QUERY,
            severity=ErrorSeverity.MEDIUM,
            details=details,
            recoverable=True,
            original_error=original_error
        )


class SerializationError(SnowflakeConnectorError):
    """Serialization-related errors."""
    
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None, original_error: Optional[Exception] = None):
        super().__init__(
            message=message,
            category=ErrorCategory.SERIALIZATION,
            severity=ErrorSeverity.MEDIUM,
            details=details,
            recoverable=True,
            original_error=original_error
        )


class ConfigurationError(SnowflakeConnectorError):
    """Configuration-related errors."""
    
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None, original_error: Optional[Exception] = None):
        super().__init__(
            message=message,
            category=ErrorCategory.CONFIGURATION,
            severity=ErrorSeverity.HIGH,
            details=details,
            recoverable=False,
            original_error=original_error
        )


class ValidationError(SnowflakeConnectorError):
    """Validation-related errors."""
    
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None, original_error: Optional[Exception] = None):
        super().__init__(
            message=message,
            category=ErrorCategory.VALIDATION,
            severity=ErrorSeverity.MEDIUM,
            details=details,
            recoverable=False,
            original_error=original_error
        )


class ErrorHandler:
    """Centralized error handling and recovery mechanism."""
    
    def __init__(self):
        self.error_counts: Dict[str, int] = {}
        self.error_history: List[Dict[str, Any]] = []
        self.max_error_history = 1000
        self.max_retries = 3
        self.retry_delays = [1, 5, 15]  # seconds
    
    def handle_error(
        self,
        error: Exception,
        context: Optional[Dict[str, Any]] = None,
        retry_count: int = 0
    ) -> bool:
        """
        Handle an error and determine if it should be retried.
        
        Args:
            error: The exception that occurred
            context: Additional context about the error
            retry_count: Current retry attempt number
            
        Returns:
            True if the error should be retried, False otherwise
        """
        # Convert generic exceptions to SnowflakeConnectorError
        if not isinstance(error, SnowflakeConnectorError):
            error = self._classify_error(error, context)
        
        # Log the error
        self._log_error(error, context)
        
        # Record error statistics
        self._record_error(error)
        
        # Determine if error should be retried
        should_retry = self._should_retry(error, retry_count)
        
        if should_retry:
            logger.info(f"Error will be retried (attempt {retry_count + 1}/{self.max_retries})")
        else:
            logger.error(f"Error will not be retried: {error.message}")
        
        return should_retry
    
    def _classify_error(self, error: Exception, context: Optional[Dict[str, Any]] = None) -> SnowflakeConnectorError:
        """Classify a generic exception into a specific SnowflakeConnectorError."""
        error_message = str(error)
        error_type = type(error).__name__
        
        # Connection errors
        if any(keyword in error_message.lower() for keyword in [
            'connection', 'connect', 'network', 'timeout', 'refused', 'unreachable'
        ]):
            return ConnectionError(
                message=f"Connection error: {error_message}",
                details={"error_type": error_type, "context": context},
                original_error=error
            )
        
        # Permission errors
        if any(keyword in error_message.lower() for keyword in [
            'permission', 'access denied', 'unauthorized', 'forbidden', 'insufficient privileges'
        ]):
            return PermissionError(
                message=f"Permission error: {error_message}",
                details={"error_type": error_type, "context": context},
                original_error=error
            )
        
        # Configuration errors (check before query errors to avoid false positives)
        if any(keyword in error_message.lower() for keyword in [
            'config', 'configuration', 'setting', 'parameter', 'invalid value'
        ]):
            return ConfigurationError(
                message=f"Configuration error: {error_message}",
                details={"error_type": error_type, "context": context},
                original_error=error
            )
        
        # Query errors
        if any(keyword in error_message.lower() for keyword in [
            'sql', 'query', 'syntax', 'table not found', 'column not found'
        ]):
            return QueryError(
                message=f"Query error: {error_message}",
                details={"error_type": error_type, "context": context},
                original_error=error
            )
        
        # Serialization errors
        if any(keyword in error_message.lower() for keyword in [
            'serialize', 'json', 'encode', 'decode', 'pickle', 'marshal'
        ]):
            return SerializationError(
                message=f"Serialization error: {error_message}",
                details={"error_type": error_type, "context": context},
                original_error=error
            )
        
        
        # Default to unknown error
        return SnowflakeConnectorError(
            message=f"Unknown error: {error_message}",
            details={"error_type": error_type, "context": context},
            original_error=error
        )
    
    def _log_error(self, error: SnowflakeConnectorError, context: Optional[Dict[str, Any]] = None):
        """Log the error with appropriate level based on severity."""
        log_message = f"[{error.category.value.upper()}] {error.message}"
        
        if context:
            log_message += f" | Context: {json.dumps(context, default=str)}"
        
        if error.details:
            log_message += f" | Details: {json.dumps(error.details, default=str)}"
        
        if error.severity == ErrorSeverity.CRITICAL:
            logger.critical(log_message)
        elif error.severity == ErrorSeverity.HIGH:
            logger.error(log_message)
        elif error.severity == ErrorSeverity.MEDIUM:
            logger.warning(log_message)
        else:
            logger.info(log_message)
    
    def _record_error(self, error: SnowflakeConnectorError):
        """Record error statistics and history."""
        # Update error counts
        error_key = f"{error.category.value}_{error.severity.value}"
        self.error_counts[error_key] = self.error_counts.get(error_key, 0) + 1
        
        # Add to error history
        error_record = error.to_dict()
        self.error_history.append(error_record)
        
        # Maintain history size limit
        if len(self.error_history) > self.max_error_history:
            self.error_history = self.error_history[-self.max_error_history:]
    
    def _should_retry(self, error: SnowflakeConnectorError, retry_count: int) -> bool:
        """Determine if an error should be retried."""
        # Don't retry if max retries reached
        if retry_count >= self.max_retries:
            return False
        
        # Don't retry non-recoverable errors
        if not error.recoverable:
            return False
        
        # Don't retry critical errors
        if error.severity == ErrorSeverity.CRITICAL:
            return False
        
        # Don't retry permission errors
        if error.category == ErrorCategory.PERMISSION:
            return False
        
        # Don't retry configuration errors
        if error.category == ErrorCategory.CONFIGURATION:
            return False
        
        return True
    
    def get_error_summary(self) -> Dict[str, Any]:
        """Get a summary of error statistics."""
        return {
            "error_counts": self.error_counts,
            "total_errors": len(self.error_history),
            "recent_errors": self.error_history[-10:] if self.error_history else [],
            "error_categories": list(set(error["category"] for error in self.error_history)),
            "error_severities": list(set(error["severity"] for error in self.error_history))
        }


def retry_on_error(
    max_retries: int = 3,
    retry_delays: List[int] = None,
    error_handler: Optional[ErrorHandler] = None
):
    """
    Decorator for retrying functions on error.
    
    Args:
        max_retries: Maximum number of retry attempts
        retry_delays: List of delay times between retries (in seconds)
        error_handler: Error handler instance to use
    """
    if retry_delays is None:
        retry_delays = [1, 5, 15]
    
    if error_handler is None:
        error_handler = ErrorHandler()
    
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_error = None
            
            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_error = e
                    
                    # Handle the error
                    should_retry = error_handler.handle_error(
                        error=e,
                        context={
                            "function": func.__name__,
                            "attempt": attempt + 1,
                            "max_retries": max_retries
                        },
                        retry_count=attempt
                    )
                    
                    if not should_retry or attempt == max_retries:
                        break
                    
                    # Wait before retrying
                    if attempt < len(retry_delays):
                        import time
                        time.sleep(retry_delays[attempt])
            
            # If we get here, all retries failed
            raise last_error
        
        return wrapper
    return decorator


def validate_configuration(config: Any) -> bool:
    """
    Validate configuration object.
    
    Args:
        config: Configuration object to validate
        
    Returns:
        True if configuration is valid, False otherwise
    """
    try:
        # Check if config has required attributes
        required_attrs = ['account_id', 'username', 'password']
        for attr in required_attrs:
            if not hasattr(config, attr):
                raise ValidationError(f"Missing required configuration attribute: {attr}")
            
            value = getattr(config, attr)
            if not value:
                raise ValidationError(f"Configuration attribute '{attr}' cannot be empty")
        
        # Validate account_id format
        if hasattr(config, 'account_id'):
            account_id = config.account_id
            if not isinstance(account_id, str) or len(account_id) < 3:
                raise ValidationError("account_id must be a non-empty string")
        
        # Validate username format
        if hasattr(config, 'username'):
            username = config.username
            if not isinstance(username, str) or len(username) < 1:
                raise ValidationError("username must be a non-empty string")
        
        # Validate password format
        if hasattr(config, 'password'):
            password = config.password
            # Handle SecretStr type from Pydantic
            if hasattr(password, 'get_secret_value'):
                password = password.get_secret_value()
            if not isinstance(password, str) or len(password) < 1:
                raise ValidationError("password must be a non-empty string")
        
        # Validate time windows if present
        if hasattr(config, 'start_time') and hasattr(config, 'end_time'):
            if config.start_time and config.end_time:
                if config.end_time <= config.start_time:
                    raise ValidationError("end_time must be after start_time")
        
        logger.debug("✅ Configuration validation passed")
        return True
        
    except ValidationError as e:
        logger.error(f"Configuration validation failed: {e.message}")
        return False
    except Exception as e:
        logger.error(f"Unexpected error during configuration validation: {e}")
        return False


def safe_execute(
    func: Callable,
    *args,
    error_handler: Optional[ErrorHandler] = None,
    default_return: Any = None,
    **kwargs
) -> Any:
    """
    Safely execute a function with error handling.
    
    Args:
        func: Function to execute
        *args: Function arguments
        error_handler: Error handler instance
        default_return: Value to return if function fails
        **kwargs: Function keyword arguments
        
    Returns:
        Function result or default_return if execution fails
    """
    if error_handler is None:
        error_handler = ErrorHandler()
    
    try:
        return func(*args, **kwargs)
    except Exception as e:
        error_handler.handle_error(e, context={"function": func.__name__})
        return default_return


# Export main classes and functions
__all__ = [
    'ErrorSeverity',
    'ErrorCategory',
    'SnowflakeConnectorError',
    'ConnectionError',
    'PermissionError',
    'QueryError',
    'SerializationError',
    'ConfigurationError',
    'ValidationError',
    'ErrorHandler',
    'retry_on_error',
    'validate_configuration',
    'safe_execute',
]
