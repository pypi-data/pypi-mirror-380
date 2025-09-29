"""
Django App Agent Module - AI-Powered Django Application Generator.

This module provides intelligent Django application generation using AI agents
with infrastructure-aware code generation and intelligent questioning systems.

Key Features:
- AI-powered code generation with Pydantic AI
- Infrastructure-aware pattern recognition
- Intelligent questioning for requirement gathering
- Type-safe everything with Pydantic 2
- Rich CLI interface with progress tracking
- Multi-agent orchestration for complex workflows

Usage:
    from django_cfg.modules.django_app_agent import AppGeneratorService
    
    service = AppGeneratorService()
    result = await service.generate_app(request)
"""

from typing import TYPE_CHECKING

# Version information
__version__ = "0.4.0"
__author__ = "Django-CFG Team"
__email__ = "team@django-cfg.dev"

# Module metadata
__title__ = "Django App Agent"
__description__ = "AI-Powered Django Application Generator"
__url__ = "https://github.com/django-cfg/django-cfg"
__license__ = "MIT"

# Public API exports (lazy loading for performance)
if TYPE_CHECKING:
    from .services.app_generator import AppGeneratorService
    from .services.questioning_service import QuestioningService
    from .services.diagnostic_service import DiagnosticService
    from .models.requests import AppGenerationRequest
    from .models.responses import AppGenerationResult
    from .core.exceptions import (
        DjangoAppAgentError,
        GenerationError,
        ValidationError,
        ConfigurationError
    )

__all__ = [
    # Services
    "AppGeneratorService",
    "QuestioningService", 
    "DiagnosticService",
    
    # Models
    "AppGenerationRequest",
    "AppGenerationResult",
    
    # Exceptions
    "DjangoAppAgentError",
    "GenerationError",
    "ValidationError",
    "ConfigurationError",
    
    # Metadata
    "__version__",
    "__author__",
    "__title__",
    "__description__",
]


def get_version() -> str:
    """Get the current version of Django App Agent Module."""
    return __version__


def get_info() -> dict[str, str]:
    """Get module information."""
    return {
        "title": __title__,
        "version": __version__,
        "description": __description__,
        "author": __author__,
        "url": __url__,
        "license": __license__,
    }
