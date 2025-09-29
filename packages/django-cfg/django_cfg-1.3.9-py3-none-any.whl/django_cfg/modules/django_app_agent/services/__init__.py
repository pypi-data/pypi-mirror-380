"""
Service Layer for Django App Agent Module.

This module provides business logic services for:
- Application generation and management
- Project structure analysis and scanning
- Template management and code generation
- Context building for AI agents
- Validation and quality assurance
- Reporting and documentation generation

Services follow the base service pattern with:
- Dependency injection via configuration
- Structured logging and error handling
- Async operations for performance
- Type safety with Pydantic v2
"""

from .base import BaseService, ServiceResult, ServiceError
from .project_scanner import ProjectScannerService
from .app_generator import AppGeneratorService
from .context_builder import ContextBuilderService
from .template_manager import TemplateManagerService
from .validation_service import ValidationService
from .questioning_service import QuestioningService
from .report_service import ReportService

__all__ = [
    # Base service infrastructure
    "BaseService",
    "ServiceResult", 
    "ServiceError",
    
    # Core services
    "ProjectScannerService",
    "AppGeneratorService",
    "ContextBuilderService",
    "TemplateManagerService",
    "ValidationService",
    "QuestioningService",
    "ReportService",
]
