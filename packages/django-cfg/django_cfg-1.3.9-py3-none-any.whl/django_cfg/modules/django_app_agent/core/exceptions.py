"""
Exception hierarchy for Django App Agent Module.

This module defines a comprehensive exception hierarchy following best practices:
- Clear inheritance structure
- Contextual error information
- Structured error data with Pydantic models
- Support for error recovery and retry logic
"""

from typing import Optional, Dict, Any, List
from pathlib import Path
from pydantic import BaseModel, Field, ConfigDict


class ErrorContext(BaseModel):
    """Context information for errors."""
    
    model_config = ConfigDict(
        extra='forbid',
        validate_assignment=True,
        str_strip_whitespace=True
    )
    
    operation: str = Field(description="Operation that caused the error")
    component: str = Field(description="Component where error occurred")
    timestamp: str = Field(description="Error timestamp")
    correlation_id: Optional[str] = Field(default=None, description="Correlation ID for tracing")
    additional_data: Dict[str, Any] = Field(default_factory=dict, description="Additional error context")


class DjangoAppAgentError(Exception):
    """Base exception for all Django App Agent Module errors."""
    
    def __init__(
        self,
        message: str,
        *,
        error_code: Optional[str] = None,
        context: Optional[ErrorContext] = None,
        cause: Optional[Exception] = None,
        recoverable: bool = False
    ) -> None:
        """Initialize Django App Agent error.
        
        Args:
            message: Human-readable error message
            error_code: Machine-readable error code
            context: Error context information
            cause: Original exception that caused this error
            recoverable: Whether this error can be recovered from
        """
        super().__init__(message)
        self.message = message
        self.error_code = error_code or self.__class__.__name__
        self.context = context
        self.cause = cause
        self.recoverable = recoverable
    
    def __str__(self) -> str:
        """String representation of the error."""
        parts = [self.message]
        
        if self.error_code:
            parts.append(f"[{self.error_code}]")
        
        if self.context:
            parts.append(f"Operation: {self.context.operation}")
            parts.append(f"Component: {self.context.component}")
        
        return " | ".join(parts)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert error to dictionary representation."""
        return {
            "error_type": self.__class__.__name__,
            "message": self.message,
            "error_code": self.error_code,
            "context": self.context.model_dump() if self.context else None,
            "recoverable": self.recoverable,
            "cause": str(self.cause) if self.cause else None,
        }


class ConfigurationError(DjangoAppAgentError):
    """Error in module configuration or setup."""
    
    def __init__(
        self,
        message: str,
        *,
        config_key: Optional[str] = None,
        config_file: Optional[Path] = None,
        **kwargs
    ) -> None:
        """Initialize configuration error.
        
        Args:
            message: Error message
            config_key: Configuration key that caused the error
            config_file: Configuration file path
            **kwargs: Additional arguments for base class
        """
        super().__init__(message, **kwargs)
        self.config_key = config_key
        self.config_file = config_file


class GenerationError(DjangoAppAgentError):
    """Error during application generation process."""
    
    def __init__(
        self,
        message: str,
        *,
        app_name: Optional[str] = None,
        generation_stage: Optional[str] = None,
        partial_results: Optional[List[str]] = None,
        **kwargs
    ) -> None:
        """Initialize generation error.
        
        Args:
            message: Error message
            app_name: Name of app being generated
            generation_stage: Stage where error occurred
            partial_results: Partial results before error
            **kwargs: Additional arguments for base class
        """
        super().__init__(message, recoverable=True, **kwargs)
        self.app_name = app_name
        self.generation_stage = generation_stage
        self.partial_results = partial_results or []


class ValidationError(DjangoAppAgentError):
    """Error during validation of generated code or user input."""
    
    def __init__(
        self,
        message: str,
        *,
        validation_type: Optional[str] = None,
        field_name: Optional[str] = None,
        field_value: Optional[Any] = None,
        **kwargs
    ) -> None:
        """Initialize validation error.
        
        Args:
            message: Error message
            validation_type: Type of validation that failed
            field_name: Field that failed validation
            field_value: Value that failed validation
            **kwargs: Additional arguments for base class
        """
        super().__init__(message, **kwargs)
        self.validation_type = validation_type
        self.field_name = field_name
        self.field_value = field_value


class QualityValidationError(ValidationError):
    """Error when generated code doesn't meet quality standards."""
    
    def __init__(
        self,
        message: str,
        *,
        quality_score: Optional[float] = None,
        minimum_score: Optional[float] = None,
        quality_issues: Optional[List[str]] = None,
        **kwargs
    ) -> None:
        """Initialize quality validation error.
        
        Args:
            message: Error message
            quality_score: Actual quality score achieved
            minimum_score: Minimum required quality score
            quality_issues: List of specific quality issues
            **kwargs: Additional arguments for base class
        """
        super().__init__(message, validation_type="quality", **kwargs)
        self.quality_score = quality_score
        self.minimum_score = minimum_score
        self.quality_issues = quality_issues or []


class AgentExecutionError(DjangoAppAgentError):
    """Error during AI agent execution."""
    
    def __init__(
        self,
        message: str,
        *,
        agent_name: Optional[str] = None,
        agent_operation: Optional[str] = None,
        retry_count: int = 0,
        max_retries: int = 3,
        **kwargs
    ) -> None:
        """Initialize agent execution error.
        
        Args:
            message: Error message
            agent_name: Name of the agent that failed
            agent_operation: Operation the agent was performing
            retry_count: Number of retries attempted
            max_retries: Maximum number of retries allowed
            **kwargs: Additional arguments for base class
        """
        recoverable = retry_count < max_retries
        super().__init__(message, recoverable=recoverable, **kwargs)
        self.agent_name = agent_name
        self.agent_operation = agent_operation
        self.retry_count = retry_count
        self.max_retries = max_retries


class AuthenticationError(DjangoAppAgentError):
    """Error with AI service authentication."""
    
    def __init__(
        self,
        message: str,
        *,
        provider: Optional[str] = None,
        api_key_hint: Optional[str] = None,
        **kwargs
    ) -> None:
        """Initialize authentication error.
        
        Args:
            message: Error message
            provider: AI service provider (openai, anthropic, etc.)
            api_key_hint: Hint about API key (first/last chars)
            **kwargs: Additional arguments for base class
        """
        super().__init__(message, **kwargs)
        self.provider = provider
        self.api_key_hint = api_key_hint


class RateLimitError(DjangoAppAgentError):
    """Error when AI service rate limits are exceeded."""
    
    def __init__(
        self,
        message: str,
        *,
        provider: Optional[str] = None,
        retry_after: Optional[int] = None,
        requests_remaining: Optional[int] = None,
        **kwargs
    ) -> None:
        """Initialize rate limit error.
        
        Args:
            message: Error message
            provider: AI service provider
            retry_after: Seconds to wait before retry
            requests_remaining: Number of requests remaining
            **kwargs: Additional arguments for base class
        """
        super().__init__(message, recoverable=True, **kwargs)
        self.provider = provider
        self.retry_after = retry_after
        self.requests_remaining = requests_remaining


class TimeoutError(DjangoAppAgentError):
    """Error when operations exceed time limits."""
    
    def __init__(
        self,
        message: str,
        *,
        operation: Optional[str] = None,
        timeout_seconds: Optional[float] = None,
        elapsed_seconds: Optional[float] = None,
        **kwargs
    ) -> None:
        """Initialize timeout error.
        
        Args:
            message: Error message
            operation: Operation that timed out
            timeout_seconds: Configured timeout
            elapsed_seconds: Actual elapsed time
            **kwargs: Additional arguments for base class
        """
        super().__init__(message, recoverable=True, **kwargs)
        self.operation = operation
        self.timeout_seconds = timeout_seconds
        self.elapsed_seconds = elapsed_seconds


class FileSystemError(DjangoAppAgentError):
    """Error when file system operations fail."""
    
    def __init__(
        self,
        message: str,
        *,
        file_path: Optional[str] = None,
        operation: Optional[str] = None,
        **kwargs
    ) -> None:
        """Initialize file system error.
        
        Args:
            message: Error message
            file_path: Path to the file that caused the error
            operation: File system operation that failed
            **kwargs: Additional arguments for base class
        """
        super().__init__(message, recoverable=True, **kwargs)
        self.file_path = file_path
        self.operation = operation


# Exception mapping for easy lookup
EXCEPTION_MAP: Dict[str, type[DjangoAppAgentError]] = {
    "configuration": ConfigurationError,
    "generation": GenerationError,
    "validation": ValidationError,
    "quality": QualityValidationError,
    "agent": AgentExecutionError,
    "auth": AuthenticationError,
    "rate_limit": RateLimitError,
    "timeout": TimeoutError,
    "filesystem": FileSystemError,
}


def create_error(
    error_type: str,
    message: str,
    **kwargs
) -> DjangoAppAgentError:
    """Create an error of the specified type.
    
    Args:
        error_type: Type of error to create
        message: Error message
        **kwargs: Additional arguments for the error
        
    Returns:
        Appropriate error instance
        
    Raises:
        ValueError: If error_type is not recognized
    """
    if error_type not in EXCEPTION_MAP:
        raise ValueError(f"Unknown error type: {error_type}")
    
    error_class = EXCEPTION_MAP[error_type]
    return error_class(message, **kwargs)
