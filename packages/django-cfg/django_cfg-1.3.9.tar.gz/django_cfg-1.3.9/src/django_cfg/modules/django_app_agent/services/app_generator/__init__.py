"""
Application Generator Module for Django App Agent.

This module provides a decomposed, modular approach to Django application generation
with AI assistance. The module is split into logical components for better maintainability.

Components:
- context: Generation context management
- validation: Requirements and code validation
- structure: Basic app structure and template generation
- ai_integration: AI-powered code generation
- main: Main orchestration service
"""

from .main import AppGeneratorService
from .context import GenerationContext
from .validation import GenerationValidator
from .structure import StructureGenerator
from .ai_integration import AIGenerationManager

__all__ = [
    # Main service
    "AppGeneratorService",
    
    # Core components
    "GenerationContext",
    "GenerationValidator", 
    "StructureGenerator",
    "AIGenerationManager",
]
