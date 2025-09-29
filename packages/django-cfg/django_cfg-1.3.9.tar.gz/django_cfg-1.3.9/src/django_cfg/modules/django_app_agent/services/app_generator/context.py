"""
Generation Context for Django App Agent Module.

This module contains the GenerationContext class that manages state
and data throughout the application generation process.
"""

from typing import List, Dict, Any
from pathlib import Path

from pydantic import BaseModel, Field, ConfigDict

from ...models.requests import AppGenerationRequest
from ...models.responses import GeneratedFile


class GenerationContext(BaseModel):
    """Context for application generation process."""
    
    model_config = ConfigDict(extra='forbid', validate_assignment=True)
    
    request: AppGenerationRequest = Field(description="Original generation request")
    target_directory: Path = Field(description="Target directory for generated app")
    template_variables: Dict[str, Any] = Field(default_factory=dict, description="Template variables")
    generated_files: List[GeneratedFile] = Field(default_factory=list, description="Generated files")
    validation_results: Dict[str, Any] = Field(default_factory=dict, description="Validation results")
    agent_outputs: Dict[str, Any] = Field(default_factory=dict, description="AI agent outputs")
    
    @property
    def app_directory(self) -> Path:
        """Get the application directory path."""
        return self.target_directory / self.request.app_name
    
    def add_generated_file(self, file: GeneratedFile) -> None:
        """Add a generated file to the context."""
        self.generated_files.append(file)
    
    def get_files_by_type(self, file_type: str) -> List[GeneratedFile]:
        """Get generated files by type."""
        return [f for f in self.generated_files if f.file_type == file_type]
