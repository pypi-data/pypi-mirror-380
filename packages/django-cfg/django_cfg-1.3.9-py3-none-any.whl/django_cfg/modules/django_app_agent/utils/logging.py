"""
Structured logging utilities for Django App Agent Module.

This module provides comprehensive logging functionality with:
- Structured JSON logging
- Context-aware log entries
- Performance tracking
- Agent operation logging
- Integration with Django logging
"""

import logging
import json
import time
import uuid
from typing import Any, Dict, Optional, Callable, TypeVar, ParamSpec
from functools import wraps
from pathlib import Path
from datetime import datetime, timezone
from contextlib import contextmanager
from contextvars import ContextVar

from pydantic import BaseModel, Field, ConfigDict

from ..core.config import LogLevel

# Type variables for decorators
P = ParamSpec('P')
T = TypeVar('T')

# Context variables for structured logging
correlation_id_var: ContextVar[Optional[str]] = ContextVar('correlation_id', default=None)
operation_context_var: ContextVar[Optional[str]] = ContextVar('operation_context', default=None)


class LogEntry(BaseModel):
    """Structured log entry model."""
    
    model_config = ConfigDict(
        extra='forbid',
        validate_assignment=True
    )
    
    timestamp: str = Field(description="ISO timestamp")
    level: str = Field(description="Log level")
    message: str = Field(description="Log message")
    module: str = Field(description="Module name")
    operation: Optional[str] = Field(default=None, description="Current operation")
    correlation_id: Optional[str] = Field(default=None, description="Correlation ID")
    component: str = Field(description="Component that generated the log")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata")
    
    @classmethod
    def create(
        cls,
        level: str,
        message: str,
        component: str,
        *,
        operation: Optional[str] = None,
        correlation_id: Optional[str] = None,
        **metadata: Any
    ) -> "LogEntry":
        """Create a structured log entry."""
        return cls(
            timestamp=datetime.now(timezone.utc).isoformat(),
            level=level,
            message=message,
            module="django_app_agent",
            operation=operation or operation_context_var.get(),
            correlation_id=correlation_id or correlation_id_var.get(),
            component=component,
            metadata=metadata
        )


class StructuredFormatter(logging.Formatter):
    """Custom formatter for structured JSON logging."""
    
    def format(self, record: logging.LogRecord) -> str:
        """Format log record as structured JSON."""
        # Extract structured data if present
        if hasattr(record, 'structured_data'):
            log_entry = record.structured_data
        else:
            # Create structured entry from standard log record
            log_entry = LogEntry.create(
                level=record.levelname,
                message=record.getMessage(),
                component=record.name,
                filename=getattr(record, 'filename', ''),
                lineno=getattr(record, 'lineno', 0),
                funcName=getattr(record, 'funcName', '')
            )
        
        return json.dumps(log_entry.model_dump(), ensure_ascii=False)


class StructuredLogger:
    """Structured logger for Django App Agent operations."""
    
    def __init__(self, component: str, logger: Optional[logging.Logger] = None):
        """Initialize structured logger.
        
        Args:
            component: Component name for logging context
            logger: Optional logger instance (creates one if not provided)
        """
        self.component = component
        self.logger = logger or logging.getLogger(f"django_app_agent.{component}")
    
    def _log(
        self,
        level: str,
        message: str,
        *,
        operation: Optional[str] = None,
        correlation_id: Optional[str] = None,
        **metadata: Any
    ) -> None:
        """Internal logging method."""
        log_entry = LogEntry.create(
            level=level,
            message=message,
            component=self.component,
            operation=operation,
            correlation_id=correlation_id,
            **metadata
        )
        
        # Get numeric log level
        numeric_level = getattr(logging, level)
        
        # Create log record with structured data
        record = self.logger.makeRecord(
            name=self.logger.name,
            level=numeric_level,
            fn="",
            lno=0,
            msg=message,
            args=(),
            exc_info=None
        )
        record.structured_data = log_entry
        
        self.logger.handle(record)
    
    def debug(self, message: str, **metadata: Any) -> None:
        """Log debug message."""
        self._log("DEBUG", message, **metadata)
    
    def info(self, message: str, **metadata: Any) -> None:
        """Log info message."""
        self._log("INFO", message, **metadata)
    
    def warning(self, message: str, **metadata: Any) -> None:
        """Log warning message."""
        self._log("WARNING", message, **metadata)
    
    def error(self, message: str, **metadata: Any) -> None:
        """Log error message."""
        self._log("ERROR", message, **metadata)
    
    def critical(self, message: str, **metadata: Any) -> None:
        """Log critical message."""
        self._log("CRITICAL", message, **metadata)
    
    @contextmanager
    def operation_context(self, operation: str, correlation_id: Optional[str] = None):
        """Context manager for operation logging."""
        if correlation_id is None:
            correlation_id = str(uuid.uuid4())
        
        # Set context variables
        correlation_token = correlation_id_var.set(correlation_id)
        operation_token = operation_context_var.set(operation)
        
        self.info(
            f"Starting operation: {operation}",
            operation=operation,
            correlation_id=correlation_id
        )
        
        start_time = time.time()
        
        try:
            yield correlation_id
        except Exception as e:
            self.error(
                f"Operation failed: {operation}",
                operation=operation,
                correlation_id=correlation_id,
                error=str(e),
                error_type=type(e).__name__
            )
            raise
        finally:
            execution_time = time.time() - start_time
            self.info(
                f"Completed operation: {operation}",
                operation=operation,
                correlation_id=correlation_id,
                execution_time_seconds=execution_time
            )
            
            # Reset context variables
            correlation_id_var.reset(correlation_token)
            operation_context_var.reset(operation_token)


def setup_logging(
    level: LogLevel = LogLevel.INFO,
    log_file: Optional[Path] = None,
    enable_structured: bool = True
) -> None:
    """Set up logging configuration for Django App Agent Module.
    
    Args:
        level: Logging level
        log_file: Optional log file path
        enable_structured: Whether to use structured JSON logging
    """
    # Get root logger for the module
    logger = logging.getLogger("django_app_agent")
    logger.setLevel(getattr(logging, level.value))
    
    # Clear existing handlers
    logger.handlers.clear()
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(getattr(logging, level.value))
    
    if enable_structured:
        console_handler.setFormatter(StructuredFormatter())
    else:
        console_handler.setFormatter(
            logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
        )
    
    logger.addHandler(console_handler)
    
    # File handler if specified
    if log_file:
        log_file.parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(getattr(logging, level.value))
        file_handler.setFormatter(StructuredFormatter())
        logger.addHandler(file_handler)
    
    # Prevent propagation to avoid duplicate logs
    logger.propagate = False


def get_logger(component: str) -> StructuredLogger:
    """Get a structured logger for a component.
    
    Args:
        component: Component name
        
    Returns:
        Structured logger instance
    """
    return StructuredLogger(component)


def log_execution_time(operation: str) -> Callable[[Callable[P, T]], Callable[P, T]]:
    """Decorator to log execution time of functions.
    
    Args:
        operation: Operation name for logging
        
    Returns:
        Decorated function
    """
    def decorator(func: Callable[P, T]) -> Callable[P, T]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            logger = get_logger(func.__module__ or "unknown")
            
            with logger.operation_context(operation):
                start_time = time.time()
                try:
                    result = func(*args, **kwargs)
                    execution_time = time.time() - start_time
                    logger.info(
                        f"Function {func.__name__} completed",
                        function_name=func.__name__,
                        execution_time_seconds=execution_time
                    )
                    return result
                except Exception as e:
                    execution_time = time.time() - start_time
                    logger.error(
                        f"Function {func.__name__} failed",
                        function_name=func.__name__,
                        execution_time_seconds=execution_time,
                        error=str(e),
                        error_type=type(e).__name__
                    )
                    raise
        
        return wrapper
    return decorator


def log_agent_operation(
    agent_name: str,
    operation: str
) -> Callable[[Callable[P, T]], Callable[P, T]]:
    """Decorator to log AI agent operations.
    
    Args:
        agent_name: Name of the AI agent
        operation: Operation being performed
        
    Returns:
        Decorated function
    """
    def decorator(func: Callable[P, T]) -> Callable[P, T]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            logger = get_logger(f"agents.{agent_name}")
            
            with logger.operation_context(f"{agent_name}.{operation}"):
                logger.info(
                    f"Agent {agent_name} starting {operation}",
                    agent_name=agent_name,
                    operation=operation
                )
                
                start_time = time.time()
                try:
                    result = func(*args, **kwargs)
                    execution_time = time.time() - start_time
                    logger.info(
                        f"Agent {agent_name} completed {operation}",
                        agent_name=agent_name,
                        operation=operation,
                        execution_time_seconds=execution_time,
                        success=True
                    )
                    return result
                except Exception as e:
                    execution_time = time.time() - start_time
                    logger.error(
                        f"Agent {agent_name} failed {operation}",
                        agent_name=agent_name,
                        operation=operation,
                        execution_time_seconds=execution_time,
                        success=False,
                        error=str(e),
                        error_type=type(e).__name__
                    )
                    raise
        
        return wrapper
    return decorator
