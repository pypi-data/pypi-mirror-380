"""
Core module for Django App Agent.

This module contains the foundational components including:
- Exception hierarchy
- Configuration management
- Base classes and interfaces
- Logging infrastructure
"""

from .exceptions import (
    DjangoAppAgentError,
    ConfigurationError,
    GenerationError,
    ValidationError,
    QualityValidationError,
    AgentExecutionError,
    AuthenticationError,
    RateLimitError,
    TimeoutError as AgentTimeoutError,
)

__all__ = [
    "DjangoAppAgentError",
    "ConfigurationError", 
    "GenerationError",
    "ValidationError",
    "QualityValidationError",
    "AgentExecutionError",
    "AuthenticationError",
    "RateLimitError",
    "AgentTimeoutError",
]
