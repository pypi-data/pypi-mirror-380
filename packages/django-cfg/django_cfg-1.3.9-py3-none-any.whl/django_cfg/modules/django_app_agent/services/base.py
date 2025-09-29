"""
Base service classes for Django App Agent Module.

This module provides the foundation for all business logic services,
including common patterns for dependency injection, error handling,
logging, and async operations.
"""

from typing import TypeVar, Generic, Optional, Dict, Any, List, Union
from abc import ABC, abstractmethod
from datetime import datetime, timezone
from pathlib import Path
import asyncio
import uuid

from pydantic import BaseModel, Field, ConfigDict

from ..core.config import AgentConfig
from ..core.exceptions import DjangoAppAgentError, ValidationError
from ..utils.logging import StructuredLogger, get_logger

# Type variables for generic service operations
InputT = TypeVar('InputT')
OutputT = TypeVar('OutputT')


class ServiceError(DjangoAppAgentError):
    """Base exception for service layer errors."""
    
    def __init__(
        self, 
        message: str, 
        service_name: str,
        operation: str,
        details: Optional[Dict[str, Any]] = None
    ):
        super().__init__(message, details)
        self.service_name = service_name
        self.operation = operation


class ServiceResult(BaseModel, Generic[OutputT]):
    """Standard result wrapper for service operations."""
    
    model_config = ConfigDict(
        extra='forbid',
        validate_assignment=True,
        arbitrary_types_allowed=True
    )
    
    # Result metadata
    operation_id: str = Field(description="Unique operation identifier")
    service_name: str = Field(description="Name of the service that produced this result")
    operation_name: str = Field(description="Name of the operation performed")
    
    # Execution information
    success: bool = Field(description="Whether the operation was successful")
    start_time: datetime = Field(description="Operation start time")
    end_time: Optional[datetime] = Field(default=None, description="Operation end time")
    
    # Result data
    data: Optional[OutputT] = Field(default=None, description="Operation result data")
    error: Optional[str] = Field(default=None, description="Error message if failed")
    
    # Performance metrics
    execution_time_seconds: float = Field(default=0.0, description="Total execution time")
    memory_usage_mb: Optional[float] = Field(default=None, description="Peak memory usage")
    
    # Context information
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata")
    warnings: List[str] = Field(default_factory=list, description="Operation warnings")
    
    @property
    def is_successful(self) -> bool:
        """Check if operation was successful."""
        return self.success and self.error is None
    
    @property
    def is_failed(self) -> bool:
        """Check if operation failed."""
        return not self.success or self.error is not None
    
    def mark_completed(self, data: Optional[OutputT] = None) -> None:
        """Mark operation as successfully completed."""
        self.end_time = datetime.now(timezone.utc)
        self.execution_time_seconds = (self.end_time - self.start_time).total_seconds()
        self.success = True
        if data is not None:
            self.data = data
    
    def mark_failed(self, error: str, details: Optional[Dict[str, Any]] = None) -> None:
        """Mark operation as failed."""
        self.end_time = datetime.now(timezone.utc)
        self.execution_time_seconds = (self.end_time - self.start_time).total_seconds()
        self.success = False
        self.error = error
        if details:
            self.metadata.update(details)
    
    def add_warning(self, warning: str) -> None:
        """Add a warning to the result."""
        self.warnings.append(warning)
    
    def get_summary(self) -> Dict[str, Any]:
        """Get operation summary."""
        return {
            "operation_id": self.operation_id,
            "service_name": self.service_name,
            "operation_name": self.operation_name,
            "success": self.success,
            "execution_time_seconds": self.execution_time_seconds,
            "has_data": self.data is not None,
            "has_error": self.error is not None,
            "warnings_count": len(self.warnings),
            "metadata_keys": list(self.metadata.keys())
        }


class ServiceDependencies(BaseModel):
    """Dependencies for service operations."""
    
    model_config = ConfigDict(
        extra='forbid',
        validate_assignment=True,
        arbitrary_types_allowed=True
    )
    
    config: AgentConfig = Field(description="Agent configuration")
    logger: StructuredLogger = Field(description="Structured logger instance")
    operation_id: str = Field(default_factory=lambda: str(uuid.uuid4()), description="Unique operation ID")
    project_root: Optional[Path] = Field(default=None, description="Project root directory")
    output_directory: Optional[Path] = Field(default=None, description="Output directory")
    context_data: Dict[str, Any] = Field(default_factory=dict, description="Additional context data")
    
    def get_project_path(self) -> Path:
        """Get project root path."""
        return self.project_root or Path.cwd()
    
    def get_output_path(self) -> Path:
        """Get output directory path."""
        return self.output_directory or self.get_project_path()
    
    def log_operation(self, message: str, **kwargs: Any) -> None:
        """Log operation with context."""
        self.logger.info(
            message,
            operation_id=self.operation_id,
            **kwargs
        )
    
    def log_error(self, message: str, error: Exception, **kwargs: Any) -> None:
        """Log error with context."""
        self.logger.error(
            message,
            operation_id=self.operation_id,
            error=str(error),
            error_type=type(error).__name__,
            **kwargs
        )


class BaseService(ABC, Generic[InputT, OutputT]):
    """
    Abstract base class for all services in the Django App Agent module.
    
    Provides common functionality for:
    - Dependency injection and configuration
    - Structured logging and error handling
    - Operation tracking and metrics
    - Async operation support
    - Type safety with generics
    """
    
    def __init__(self, service_name: str, config: AgentConfig):
        """Initialize base service.
        
        Args:
            service_name: Name of the service for logging and identification
            config: Agent configuration
        """
        self.service_name = service_name
        self.config = config
        self.logger = get_logger(f"services.{service_name}")
        self._active_operations: Dict[str, ServiceResult] = {}
    
    def create_dependencies(
        self,
        operation_id: Optional[str] = None,
        project_root: Optional[Path] = None,
        output_directory: Optional[Path] = None,
        **context_data: Any
    ) -> ServiceDependencies:
        """Create service dependencies for an operation.
        
        Args:
            operation_id: Optional operation ID
            project_root: Optional project root directory
            output_directory: Optional output directory
            **context_data: Additional context data
            
        Returns:
            ServiceDependencies instance
        """
        return ServiceDependencies(
            config=self.config,
            logger=self.logger,
            operation_id=operation_id or str(uuid.uuid4()),
            project_root=project_root,
            output_directory=output_directory,
            context_data=context_data
        )
    
    def create_result(
        self,
        operation_name: str,
        operation_id: Optional[str] = None
    ) -> ServiceResult[OutputT]:
        """Create a new service result.
        
        Args:
            operation_name: Name of the operation
            operation_id: Optional operation ID
            
        Returns:
            ServiceResult instance
        """
        op_id = operation_id or str(uuid.uuid4())
        result = ServiceResult[OutputT](
            operation_id=op_id,
            service_name=self.service_name,
            operation_name=operation_name,
            success=False,
            start_time=datetime.now(timezone.utc)
        )
        
        # Track active operation
        self._active_operations[op_id] = result
        
        return result
    
    def complete_operation(self, result: ServiceResult[OutputT]) -> None:
        """Complete an operation and remove from active tracking.
        
        Args:
            result: The completed service result
        """
        # Remove from active operations
        self._active_operations.pop(result.operation_id, None)
        
        # Log completion
        self.logger.info(
            f"Operation {result.operation_name} completed",
            operation_id=result.operation_id,
            success=result.success,
            execution_time_seconds=result.execution_time_seconds,
            has_warnings=len(result.warnings) > 0
        )
    
    async def execute_with_result(
        self,
        operation_name: str,
        operation_func: callable,
        dependencies: ServiceDependencies,
        *args: Any,
        **kwargs: Any
    ) -> ServiceResult[OutputT]:
        """Execute an operation with automatic result tracking.
        
        Args:
            operation_name: Name of the operation
            operation_func: Function to execute
            dependencies: Service dependencies
            *args: Positional arguments for operation_func
            **kwargs: Keyword arguments for operation_func
            
        Returns:
            ServiceResult with operation outcome
        """
        result = self.create_result(operation_name, dependencies.operation_id)
        
        try:
            # Execute operation
            if asyncio.iscoroutinefunction(operation_func):
                data = await operation_func(dependencies, *args, **kwargs)
            else:
                data = operation_func(dependencies, *args, **kwargs)
            
            # Mark as completed
            result.mark_completed(data)
            
        except Exception as e:
            # Mark as failed
            error_msg = f"Operation {operation_name} failed: {e}"
            result.mark_failed(error_msg, {"exception_type": type(e).__name__})
            
            # Log error
            dependencies.log_error(error_msg, e)
            
            # Re-raise if it's a service error, otherwise wrap it
            if isinstance(e, ServiceError):
                raise
            else:
                raise ServiceError(
                    error_msg,
                    service_name=self.service_name,
                    operation=operation_name,
                    cause=e
                ) from e
        
        finally:
            # Complete operation tracking
            self.complete_operation(result)
        
        return result
    
    @abstractmethod
    async def process(self, input_data: InputT, dependencies: ServiceDependencies) -> OutputT:
        """
        Process input data and return output.
        
        This is the main method that subclasses must implement.
        
        Args:
            input_data: Input data for processing
            dependencies: Service dependencies
            
        Returns:
            Processed output data
        """
        pass
    
    async def run(
        self,
        input_data: InputT,
        operation_id: Optional[str] = None,
        project_root: Optional[Path] = None,
        output_directory: Optional[Path] = None,
        **context_data: Any
    ) -> ServiceResult[OutputT]:
        """
        Run the service with input data and return a result.
        
        Args:
            input_data: Input data for processing
            operation_id: Optional operation ID
            project_root: Optional project root directory
            output_directory: Optional output directory
            **context_data: Additional context data
            
        Returns:
            ServiceResult with operation outcome
        """
        # Create dependencies
        dependencies = self.create_dependencies(
            operation_id=operation_id,
            project_root=project_root,
            output_directory=output_directory,
            **context_data
        )
        
        # Execute with result tracking
        return await self.execute_with_result(
            "process",
            self.process,
            dependencies,
            input_data
        )
    
    def get_active_operations(self) -> Dict[str, ServiceResult]:
        """Get currently active operations."""
        return self._active_operations.copy()
    
    def get_service_status(self) -> Dict[str, Any]:
        """Get service status information."""
        return {
            "service_name": self.service_name,
            "active_operations_count": len(self._active_operations),
            "active_operation_ids": list(self._active_operations.keys()),
            "config_loaded": self.config is not None,
            "logger_configured": self.logger is not None
        }
    
    def validate_input(self, input_data: InputT) -> None:
        """
        Validate input data before processing.
        
        Override this method to add custom validation logic.
        
        Args:
            input_data: Input data to validate
            
        Raises:
            ValidationError: If input data is invalid
        """
        if input_data is None:
            raise ValidationError(
                "Input data cannot be None",
                validation_type="input_validation"
            )
    
    def __repr__(self) -> str:
        """String representation of the service."""
        return f"{self.__class__.__name__}(service_name='{self.service_name}')"


def create_service_dependencies(
    config: AgentConfig,
    service_name: str,
    operation_id: Optional[str] = None,
    project_root: Optional[Path] = None,
    output_directory: Optional[Path] = None,
    **context_data: Any
) -> ServiceDependencies:
    """
    Factory function to create service dependencies.
    
    Args:
        config: Agent configuration
        service_name: Name of the service
        operation_id: Optional operation ID
        project_root: Optional project root directory
        output_directory: Optional output directory
        **context_data: Additional context data
        
    Returns:
        ServiceDependencies instance
    """
    logger = get_logger(f"services.{service_name}")
    
    return ServiceDependencies(
        config=config,
        logger=logger,
        operation_id=operation_id or str(uuid.uuid4()),
        project_root=project_root,
        output_directory=output_directory,
        context_data=context_data
    )
