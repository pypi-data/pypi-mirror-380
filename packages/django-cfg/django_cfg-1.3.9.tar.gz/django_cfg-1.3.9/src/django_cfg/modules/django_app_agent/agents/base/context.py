"""
Context management for Django App Agent AI agents.

This module provides context classes for dependency injection and
execution management following Pydantic AI patterns.
"""

from typing import Optional, Dict, Any, List
from dataclasses import dataclass, field
from pathlib import Path
from datetime import datetime, timezone

from pydantic import BaseModel, Field, ConfigDict

from ...core.config import AgentConfig, AIProvider
from ...models.context import ProjectContext, InfrastructureContext
from ...utils.logging import StructuredLogger, get_logger


class AgentDependencies(BaseModel):
    """Base dependencies for all Django App Agent AI agents.
    
    This follows Pydantic AI dependency injection patterns and provides
    common dependencies that all agents need.
    """
    
    model_config = ConfigDict(
        extra='forbid',
        validate_assignment=True,
        arbitrary_types_allowed=True  # For logger and config objects
    )
    
    # Core configuration
    config: AgentConfig = Field(description="Agent configuration")
    logger: StructuredLogger = Field(description="Structured logger instance")
    
    # Project context
    project_context: Optional[ProjectContext] = Field(
        default=None,
        description="Django project context information"
    )
    
    infrastructure_context: Optional[InfrastructureContext] = Field(
        default=None,
        description="Infrastructure context for code generation"
    )
    
    # Execution context
    correlation_id: str = Field(description="Correlation ID for tracing")
    operation_name: str = Field(description="Name of the current operation")
    
    # Working directories
    project_root: Optional[Path] = Field(
        default=None,
        description="Root directory of the Django project"
    )
    
    output_directory: Optional[Path] = Field(
        default=None,
        description="Directory for generated output"
    )
    
    # Execution metadata
    execution_metadata: Dict[str, Any] = Field(
        default_factory=dict,
        description="Additional metadata for execution"
    )
    
    def get_api_key(self, provider: str) -> Optional[str]:
        """Get API key for AI provider."""
        try:
            ai_provider = AIProvider(provider)
            return self.config.get_api_key(ai_provider)
        except ValueError:
            return None
    
    def has_project_context(self) -> bool:
        """Check if project context is available."""
        return self.project_context is not None
    
    def get_project_path(self) -> Optional[Path]:
        """Get project path from context or direct setting."""
        if self.project_context:
            return self.project_context.project_path
        return self.project_root
    
    def log_operation(self, message: str, **metadata: Any) -> None:
        """Log operation with context."""
        self.logger.info(
            message,
            operation=self.operation_name,
            correlation_id=self.correlation_id,
            **metadata
        )
    
    def log_error(self, message: str, error: Exception, **metadata: Any) -> None:
        """Log error with context."""
        self.logger.error(
            message,
            operation=self.operation_name,
            correlation_id=self.correlation_id,
            error=str(error),
            error_type=type(error).__name__,
            **metadata
        )


@dataclass
class AgentContext:
    """Execution context for Django App Agent operations.
    
    This class manages the execution context for agent operations,
    including timing, progress tracking, and result collection.
    """
    
    # Execution tracking
    start_time: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    end_time: Optional[datetime] = field(default=None)
    
    # Progress tracking
    current_stage: str = field(default="initialization")
    progress_percentage: float = field(default=0.0)
    
    # Result collection
    intermediate_results: List[Dict[str, Any]] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    
    # Performance metrics
    token_usage: Dict[str, int] = field(default_factory=dict)
    api_calls_count: int = field(default=0)
    
    def mark_completed(self) -> None:
        """Mark the context as completed."""
        self.end_time = datetime.now(timezone.utc)
        self.progress_percentage = 100.0
    
    def update_progress(self, stage: str, percentage: float) -> None:
        """Update progress information."""
        self.current_stage = stage
        self.progress_percentage = min(100.0, max(0.0, percentage))
    
    def add_result(self, result: Dict[str, Any]) -> None:
        """Add intermediate result."""
        self.intermediate_results.append({
            **result,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "stage": self.current_stage
        })
    
    def add_error(self, error: str) -> None:
        """Add error message."""
        self.errors.append(error)
    
    def add_warning(self, warning: str) -> None:
        """Add warning message."""
        self.warnings.append(warning)
    
    def track_token_usage(self, provider: str, tokens: int) -> None:
        """Track token usage by provider."""
        self.token_usage[provider] = self.token_usage.get(provider, 0) + tokens
    
    def increment_api_calls(self) -> None:
        """Increment API calls counter."""
        self.api_calls_count += 1
    
    @property
    def execution_time_seconds(self) -> float:
        """Get execution time in seconds."""
        end = self.end_time or datetime.now(timezone.utc)
        return (end - self.start_time).total_seconds()
    
    @property
    def is_completed(self) -> bool:
        """Check if execution is completed."""
        return self.end_time is not None
    
    @property
    def has_errors(self) -> bool:
        """Check if there are any errors."""
        return len(self.errors) > 0
    
    @property
    def total_tokens_used(self) -> int:
        """Get total tokens used across all providers."""
        return sum(self.token_usage.values())
    
    def get_summary(self) -> Dict[str, Any]:
        """Get execution summary."""
        return {
            "start_time": self.start_time.isoformat(),
            "end_time": self.end_time.isoformat() if self.end_time else None,
            "execution_time_seconds": self.execution_time_seconds,
            "current_stage": self.current_stage,
            "progress_percentage": self.progress_percentage,
            "is_completed": self.is_completed,
            "results_count": len(self.intermediate_results),
            "errors_count": len(self.errors),
            "warnings_count": len(self.warnings),
            "total_tokens_used": self.total_tokens_used,
            "api_calls_count": self.api_calls_count,
        }


def create_agent_dependencies(
    config: AgentConfig,
    correlation_id: str,
    operation_name: str,
    project_root: Optional[Path] = None,
    output_directory: Optional[Path] = None,
    **metadata: Any
) -> AgentDependencies:
    """Factory function to create AgentDependencies.
    
    Args:
        config: Agent configuration
        correlation_id: Correlation ID for tracing
        operation_name: Name of the operation
        project_root: Optional project root directory
        output_directory: Optional output directory
        **metadata: Additional metadata
        
    Returns:
        Configured AgentDependencies instance
    """
    logger = get_logger(f"agents.{operation_name}")
    
    return AgentDependencies(
        config=config,
        logger=logger,
        correlation_id=correlation_id,
        operation_name=operation_name,
        project_root=project_root,
        output_directory=output_directory,
        execution_metadata=metadata
    )
