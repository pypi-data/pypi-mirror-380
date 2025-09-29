"""
Template Loader for Django App Agent.

This module handles loading Jinja2 templates from files and
providing them to the template engine.
"""

from typing import Dict, Optional
from pathlib import Path

from pydantic import BaseModel, Field

from ...core.exceptions import ValidationError


class TemplateLoader(BaseModel):
    """Loads Jinja2 templates from the templates directory."""
    
    templates_dir: Path = Field(description="Directory containing template files")
    template_cache: Dict[str, str] = Field(default_factory=dict, description="Template cache")
    
    def __init__(self, **data):
        """Initialize template loader."""
        if 'templates_dir' not in data:
            # Default to templates directory relative to this file
            current_dir = Path(__file__).parent
            data['templates_dir'] = current_dir / "templates"
        
        super().__init__(**data)
        
        # Validate templates directory exists
        if not self.templates_dir.exists():
            raise ValidationError(
                f"Templates directory does not exist: {self.templates_dir}",
                validation_type="template_directory"
            )
    
    def load_template(self, template_name: str) -> str:
        """Load a template by name."""
        # Check cache first
        if template_name in self.template_cache:
            return self.template_cache[template_name]
        
        # Try to load from file
        template_path = self.templates_dir / template_name
        
        if not template_path.exists():
            # Try with .j2 extension if not provided
            if not template_name.endswith('.j2'):
                template_path = self.templates_dir / f"{template_name}.j2"
        
        if not template_path.exists():
            raise ValidationError(
                f"Template file not found: {template_name}",
                validation_type="template_not_found"
            )
        
        try:
            content = template_path.read_text(encoding='utf-8')
            # Cache the template
            self.template_cache[template_name] = content
            return content
            
        except Exception as e:
            raise ValidationError(
                f"Failed to read template file {template_name}: {e}",
                validation_type="template_read_error"
            )
    
    def load_all_templates(self) -> Dict[str, str]:
        """Load all templates from the templates directory."""
        templates = {}
        
        for template_path in self.templates_dir.glob("*.j2"):
            template_name = template_path.name
            try:
                content = self.load_template(template_name)
                templates[template_name] = content
            except ValidationError:
                # Skip templates that can't be loaded
                continue
        
        return templates
    
    def get_available_templates(self) -> list[str]:
        """Get list of available template names."""
        return [p.name for p in self.templates_dir.glob("*.j2")]
    
    def clear_cache(self) -> None:
        """Clear the template cache."""
        self.template_cache.clear()
    
    def reload_template(self, template_name: str) -> str:
        """Reload a template, bypassing cache."""
        # Remove from cache if present
        if template_name in self.template_cache:
            del self.template_cache[template_name]
        
        # Load fresh copy
        return self.load_template(template_name)
