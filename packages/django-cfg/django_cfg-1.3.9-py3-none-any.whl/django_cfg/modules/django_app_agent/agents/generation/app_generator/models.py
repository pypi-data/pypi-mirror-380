"""
Data models for the App Generator Agent.

This module contains Pydantic models used for request/response
handling in the AI agent.
"""

from typing import List, Dict, Any
from pydantic import BaseModel, Field

from ....models.enums import AppFeature, AppType, AppComplexity


class FileGenerationRequest(BaseModel):
    """Request for generating a specific file."""
    
    app_name: str = Field(description="Name of the Django application")
    description: str = Field(description="Application description")
    feature: AppFeature = Field(description="Feature to generate")
    app_type: AppType = Field(description="Type of Django application")
    complexity: AppComplexity = Field(description="Application complexity level")
    additional_context: Dict[str, Any] = Field(default_factory=dict, description="Additional context")


class GeneratedFileResponse(BaseModel):
    """Response containing generated file content."""
    
    filename: str = Field(description="Name of the generated file")
    content: str = Field(description="File content")
    imports: List[str] = Field(default_factory=list, description="Required imports")
    dependencies: List[str] = Field(default_factory=list, description="Package dependencies")
    description: str = Field(description="File description")
