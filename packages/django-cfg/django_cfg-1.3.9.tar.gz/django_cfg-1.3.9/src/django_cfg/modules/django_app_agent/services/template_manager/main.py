"""
Template Manager Service for Django App Agent Module.

This service provides sophisticated Jinja2-based template rendering
with feature-driven code generation capabilities.
"""

from typing import Dict, Any, Set, Optional, List
from pathlib import Path

from pydantic import BaseModel, Field

from ...core.config import AgentConfig
from ...core.exceptions import ValidationError
from ...models.enums import AppType, AppFeature
from ...models.requests import TemplateRequest
from ...models.responses import TemplateResult
from ..base import BaseService, ServiceDependencies
from .jinja_engine import JinjaTemplateEngine
from .template_loader import TemplateLoader
from .variable_processor import VariableProcessor


class TemplateManagerService(BaseService[TemplateRequest, TemplateResult]):
    """
    Advanced template management service with Jinja2 support.
    
    Features:
    - Jinja2 template engine with custom filters
    - File-based template loading
    - Feature-driven template selection
    - Variable processing and validation
    - Template caching and optimization
    """
    
    def __init__(self, config: AgentConfig):
        """Initialize template manager service."""
        super().__init__("template_manager", config)
        self.config = config
        
        # Initialize components
        self.template_loader = TemplateLoader()
        self.jinja_engine = JinjaTemplateEngine()
        self.variable_processor = VariableProcessor()
        
        # Load all templates into engine
        self._load_templates()
    
    async def process(
        self,
        request: TemplateRequest,
        dependencies: ServiceDependencies
    ) -> TemplateResult:
        """
        Process template rendering request.
        
        Args:
            request: Template processing request
            dependencies: Service dependencies
            
        Returns:
            TemplateResult with rendered content
        """
        dependencies.log_operation(
            f"Processing template '{request.template_name}'",
            app_type=request.app_type if isinstance(request.app_type, str) else request.app_type.value,
            features_count=len(request.features),
            variables_count=len(request.variables)
        )
        
        try:
            # Determine template name
            template_name = self._resolve_template_name(request, dependencies)
            
            # Process variables
            processed_variables = await self.variable_processor.process_variables(
                request, dependencies
            )
            
            # Render template
            rendered_content, variables_used, missing_vars = self.jinja_engine.render(
                template_name, processed_variables
            )
            
            # Create result
            result = TemplateResult(
                rendered_content=rendered_content,
                template_name=template_name,
                variables_used=list(variables_used),
                missing_variables=list(missing_vars),
                template_metadata={
                    "app_type": request.app_type if isinstance(request.app_type, str) else request.app_type.value,
                    "features": [(f.value if hasattr(f, 'value') else f) for f in request.features],
                    "template_engine": "jinja2",
                    "rendered_size": len(rendered_content),
                    "variables_processed": len(processed_variables)
                }
            )
            
            dependencies.log_operation(
                "Template processing completed successfully",
                template_name=template_name,
                rendered_size=len(rendered_content),
                variables_used=len(variables_used),
                missing_variables=len(missing_vars)
            )
            
            return result
            
        except Exception as e:
            dependencies.log_error("Template processing failed", e)
            raise
    
    def _load_templates(self) -> None:
        """Load all templates into the Jinja2 engine."""
        templates = self.template_loader.load_all_templates()
        self.jinja_engine.add_templates(templates)
    
    def _resolve_template_name(
        self,
        request: TemplateRequest,
        dependencies: ServiceDependencies
    ) -> str:
        """Resolve the actual template name to use."""
        template_name = request.template_name
        
        # If template_name doesn't end with .j2, add it
        if not template_name.endswith('.j2'):
            template_name = f"{template_name}.j2"
        
        # Check if template exists
        available_templates = self.template_loader.get_available_templates()
        
        if template_name not in available_templates:
            # Try app-type specific template
            app_type_str = request.app_type if isinstance(request.app_type, str) else request.app_type.value
            app_specific_name = f"{app_type_str}_{template_name}"
            if app_specific_name in available_templates:
                template_name = app_specific_name
            else:
                raise ValidationError(
                    f"Template '{template_name}' not found. Available templates: {available_templates}",
                    validation_type="template_not_found"
                )
        
        return template_name
    
    def reload_templates(self) -> None:
        """Reload all templates from disk."""
        self.template_loader.clear_cache()
        self._load_templates()
    
    def get_available_templates(self) -> List[str]:
        """Get list of available template names."""
        return self.template_loader.get_available_templates()
    
    def add_custom_template(self, name: str, content: str) -> None:
        """Add a custom template at runtime."""
        self.jinja_engine.add_template(name, content)
