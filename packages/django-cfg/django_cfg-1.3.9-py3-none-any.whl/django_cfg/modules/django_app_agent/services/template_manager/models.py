"""
Data Models for Template Manager Service.

This module contains Pydantic models for template processing
requests, results, and related data structures.
"""

from typing import Dict, Any, Optional, List, Set

from pydantic import BaseModel, Field, ConfigDict

from ...models.enums import AppType, AppFeature


class TemplateRequest(BaseModel):
    """Request for template processing."""
    
    model_config = ConfigDict(extra='forbid', validate_assignment=True)
    
    template_name: str = Field(description="Name of the template to process")
    app_type: AppType = Field(description="Type of application")
    variables: Dict[str, Any] = Field(default_factory=dict, description="Template variables")
    features: List[AppFeature] = Field(default_factory=list, description="Requested features")
    custom_templates: Dict[str, str] = Field(default_factory=dict, description="Custom template overrides")


class TemplateResult(BaseModel):
    """Result of template processing."""
    
    model_config = ConfigDict(extra='forbid', validate_assignment=True)
    
    rendered_content: str = Field(description="Rendered template content")
    template_name: str = Field(description="Name of the processed template")
    variables_used: Set[str] = Field(default_factory=set, description="Variables that were used in rendering")
    missing_variables: Set[str] = Field(default_factory=set, description="Variables that were missing")
    template_metadata: Dict[str, Any] = Field(default_factory=dict, description="Template processing metadata")
