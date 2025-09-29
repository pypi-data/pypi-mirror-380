"""
Context Builder Module for Django App Agent.

This module provides comprehensive context building capabilities
for AI agents, including project analysis, pattern identification,
and intelligent context optimization.

Components:
- models: Data models for requests and results
- pattern_analyzer: Architectural pattern analysis
- code_extractor: Code sample extraction
- context_generator: Feature-specific context generation
- main: Main orchestration service
"""

from .main import ContextBuilderService
from .models import ContextBuildRequest, ContextResult
from .pattern_analyzer import PatternAnalyzer
from .code_extractor import CodeExtractor
from .context_generator import ContextGenerator

__all__ = [
    # Main service
    "ContextBuilderService",
    
    # Data models
    "ContextBuildRequest",
    "ContextResult",
    
    # Core components
    "PatternAnalyzer",
    "CodeExtractor",
    "ContextGenerator",
]
