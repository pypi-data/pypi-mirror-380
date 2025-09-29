"""
Data Models for Validation Service.

This module defines the data structures used by the validation service
for requests, responses, and validation issues.
"""

from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field, ConfigDict

from ...models.responses import QualityMetrics, GeneratedFile


class ValidationRequest(BaseModel):
    """Request for code validation."""
    
    model_config = ConfigDict(extra='forbid', validate_assignment=True)
    
    files: List[GeneratedFile] = Field(description="Files to validate")
    validation_rules: List[str] = Field(
        default_factory=lambda: ["syntax", "django_best_practices", "security", "quality"],
        description="Validation rules to apply"
    )
    strict_mode: bool = Field(default=False, description="Whether to use strict validation")
    custom_rules: Dict[str, Any] = Field(default_factory=dict, description="Custom validation rules")


class ValidationIssue(BaseModel):
    """Represents a validation issue."""
    
    model_config = ConfigDict(extra='forbid', validate_assignment=True)
    
    severity: str = Field(description="Issue severity: error, warning, info")
    category: str = Field(description="Issue category: syntax, security, quality, etc.")
    message: str = Field(description="Issue description message")
    file_path: str = Field(description="Path to the file with the issue")
    line_number: Optional[int] = Field(default=None, description="Line number of the issue")
    column: Optional[int] = Field(default=None, description="Column number of the issue")
    rule_id: str = Field(default="", description="Validation rule identifier")
    suggestion: Optional[str] = Field(default=None, description="Suggested fix for the issue")


class ValidationResult(BaseModel):
    """Result of code validation."""
    
    model_config = ConfigDict(extra='forbid', validate_assignment=True)
    
    is_valid: bool = Field(description="Whether the code passed validation")
    quality_metrics: QualityMetrics = Field(description="Calculated quality metrics")
    issues: List[ValidationIssue] = Field(default_factory=list, description="List of validation issues")
    summary: Dict[str, Any] = Field(default_factory=dict, description="Validation summary")
    
    @property
    def error_count(self) -> int:
        """Count of error-level issues."""
        return len([i for i in self.issues if i.severity == "error"])
    
    @property
    def warning_count(self) -> int:
        """Count of warning-level issues."""
        return len([i for i in self.issues if i.severity == "warning"])
    
    @property
    def info_count(self) -> int:
        """Count of info-level issues."""
        return len([i for i in self.issues if i.severity == "info"])
