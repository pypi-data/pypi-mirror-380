"""
Data Models for Project Scanner Service.

This module contains Pydantic models for project scanning
requests, results, and related data structures.
"""

from typing import List, Dict, Any
from pathlib import Path

from pydantic import BaseModel, Field, ConfigDict

from ...models.context import ProjectContext, DjangoAppInfo, ArchitecturalPattern
from ...core.exceptions import ValidationError


class ProjectScanRequest(BaseModel):
    """Request for project scanning operation."""
    
    model_config = ConfigDict(extra='forbid', validate_assignment=True)
    
    project_root: Path = Field(description="Root directory of the project to scan")
    scan_depth: int = Field(default=3, ge=1, le=10, description="Maximum directory depth to scan")
    include_patterns: List[str] = Field(
        default_factory=lambda: ["*.py", "*.md", "*.txt", "*.yml", "*.yaml", "*.json"],
        description="File patterns to include in scanning"
    )
    exclude_patterns: List[str] = Field(
        default_factory=lambda: ["__pycache__", "*.pyc", ".git", "node_modules", "venv", ".env"],
        description="File/directory patterns to exclude from scanning"
    )
    analyze_dependencies: bool = Field(default=True, description="Whether to analyze dependencies")
    detect_patterns: bool = Field(default=True, description="Whether to detect architectural patterns")
    
    def model_post_init(self, __context: Any) -> None:
        """Validate project root exists."""
        if not self.project_root.exists():
            raise ValidationError(
                f"Project root directory does not exist: {self.project_root}",
                validation_type="project_path"
            )
        if not self.project_root.is_dir():
            raise ValidationError(
                f"Project root is not a directory: {self.project_root}",
                validation_type="project_path"
            )


class ScanResult(BaseModel):
    """Result of project scanning operation."""
    
    model_config = ConfigDict(extra='forbid', validate_assignment=True)
    
    project_context: ProjectContext = Field(description="Comprehensive project context")
    discovered_apps: List[DjangoAppInfo] = Field(default_factory=list, description="Discovered Django applications")
    architectural_patterns: List[ArchitecturalPattern] = Field(default_factory=list, description="Detected architectural patterns")
    file_summary: Dict[str, Any] = Field(default_factory=dict, description="File structure summary")
    dependency_graph: Dict[str, List[str]] = Field(default_factory=dict, description="Application dependency graph")
    scan_statistics: Dict[str, int] = Field(default_factory=dict, description="Scanning statistics")
