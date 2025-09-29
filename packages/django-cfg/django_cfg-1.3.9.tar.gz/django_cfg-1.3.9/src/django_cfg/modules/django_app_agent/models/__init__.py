"""
Pydantic 2 models for Django App Agent Module.

This module contains all data models using Pydantic 2 with:
- 100% type safety (no Any types)
- Comprehensive validation
- Structured data throughout
- Clear separation of concerns
"""

from .base import BaseAgentModel, TimestampedModel
from .enums import (
    AppFeature,
    AppComplexity,
    AppType,
    QuestionType,
    ImpactLevel,
    GenerationStage,
    ValidationSeverity,
)
from .requests import (
    AppGenerationRequest,
    QuestioningRequest,
    DiagnosticRequest,
)
from .responses import (
    AppGenerationResult,
    QuestioningResult,
    DiagnosticResult,
    GeneratedFile,
    QualityMetrics,
)
from .context import (
    ProjectContext,
    DjangoAppInfo,
    ArchitecturalPattern,
    InfrastructureContext,
)

__all__ = [
    # Base models
    "BaseAgentModel",
    "TimestampedModel",
    
    # Enums
    "AppFeature",
    "AppComplexity", 
    "AppType",
    "QuestionType",
    "ImpactLevel",
    "GenerationStage",
    "ValidationSeverity",
    
    # Request models
    "AppGenerationRequest",
    "QuestioningRequest",
    "DiagnosticRequest",
    
    # Response models
    "AppGenerationResult",
    "QuestioningResult",
    "DiagnosticResult",
    "GeneratedFile",
    "QualityMetrics",
    
    # Context models
    "ProjectContext",
    "DjangoAppInfo",
    "ArchitecturalPattern",
    "InfrastructureContext",
]
