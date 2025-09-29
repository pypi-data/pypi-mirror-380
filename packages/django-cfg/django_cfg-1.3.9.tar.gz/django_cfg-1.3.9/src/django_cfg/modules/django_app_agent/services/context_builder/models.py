"""
Data Models for Context Builder Service.

This module contains Pydantic models for context building
requests, results, and related data structures.
"""

from typing import List, Dict, Any, Optional
from pathlib import Path

from pydantic import BaseModel, Field, ConfigDict

from ...models.context import ProjectContext, ArchitecturalPattern
from ...models.requests import AppGenerationRequest


class ContextBuildRequest(BaseModel):
    """Request for building development context."""
    
    model_config = ConfigDict(extra='forbid', validate_assignment=True)
    
    project_root: Path = Field(description="Root directory of the project")
    target_app_name: Optional[str] = Field(default=None, description="Name of app being generated")
    generation_request: Optional[AppGenerationRequest] = Field(default=None, description="App generation request")
    include_code_samples: bool = Field(default=True, description="Whether to include code samples")
    max_context_size: int = Field(default=50000, ge=1000, description="Maximum context size in characters")
    focus_areas: List[str] = Field(default_factory=list, description="Areas to focus context on")


class ContextResult(BaseModel):
    """Result of context building operation."""
    
    model_config = ConfigDict(extra='forbid', validate_assignment=True)
    
    project_context: ProjectContext = Field(description="Comprehensive project context")
    relevant_patterns: List[ArchitecturalPattern] = Field(default_factory=list, description="Relevant architectural patterns")
    code_samples: Dict[str, str] = Field(default_factory=dict, description="Code samples for reference")
    integration_points: List[Dict[str, Any]] = Field(default_factory=list, description="Potential integration points")
    recommendations: List[str] = Field(default_factory=list, description="Development recommendations")
    context_summary: Dict[str, Any] = Field(default_factory=dict, description="Context summary information")
