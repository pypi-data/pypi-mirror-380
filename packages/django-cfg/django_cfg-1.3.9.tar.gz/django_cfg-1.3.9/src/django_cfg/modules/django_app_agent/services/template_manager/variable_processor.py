"""
Variable Processor for Template Manager.

This module handles processing and enrichment of template variables
based on app features and context.
"""

from typing import Dict, Any, List, Set
import re

from pydantic import BaseModel, Field

from ...models.enums import AppType, AppFeature
from ...models.requests import TemplateRequest
from ..base import ServiceDependencies


class VariableProcessor(BaseModel):
    """Processes and enriches template variables."""
    
    def __init__(self, **data):
        """Initialize variable processor."""
        super().__init__(**data)
    
    async def process_variables(
        self,
        request: TemplateRequest,
        dependencies: ServiceDependencies
    ) -> Dict[str, Any]:
        """Process and enrich template variables."""
        # Start with provided variables
        variables = dict(request.variables)
        
        # Add standard variables
        variables.update(self._get_standard_variables(request))
        
        # Add feature-based variables
        variables.update(self._get_feature_variables(request))
        
        # Add computed variables
        variables.update(self._get_computed_variables(request, variables))
        
        dependencies.log_operation(
            "Variables processed",
            total_variables=len(variables),
            standard_vars=len(self._get_standard_variables(request)),
            feature_vars=len(self._get_feature_variables(request))
        )
        
        return variables
    
    def _get_standard_variables(self, request: TemplateRequest) -> Dict[str, Any]:
        """Get standard template variables."""
        app_name = request.variables.get('app_name', 'myapp')
        description = request.variables.get('description', f'Django application: {app_name}')
        
        return {
            'app_name': app_name,
            'description': description,
            'app_type': request.app_type if isinstance(request.app_type, str) else request.app_type.value,
            'features': {(f.value if hasattr(f, 'value') else f): True for f in request.features},
            
            # Name variations
            'app_name_snake': self._to_snake_case(app_name),
            'app_name_camel': self._to_camel_case(app_name),
            'app_name_pascal': self._to_pascal_case(app_name),
            'app_name_kebab': self._to_kebab_case(app_name),
            'app_name_title': self._to_title_case(app_name),
            
            # Pluralization
            'app_name_plural': self._pluralize(app_name),
            'app_name_singular': self._singularize(app_name),
        }
    
    def _get_feature_variables(self, request: TemplateRequest) -> Dict[str, Any]:
        """Get feature-specific variables."""
        features_dict = {}
        
        # Create feature flags
        for feature in AppFeature:
            features_dict[feature.value] = feature in request.features
        
        # Add feature groups
        features_dict.update({
            'has_authentication': any(f in request.features for f in [
                AppFeature.AUTHENTICATION, AppFeature.SECURITY
            ]),
            'has_api': any(f in request.features for f in [
                AppFeature.API, AppFeature.SERIALIZERS, AppFeature.VIEWSETS
            ]),
            'has_admin': AppFeature.ADMIN in request.features,
            'has_forms': AppFeature.FORMS in request.features,
            'has_tests': AppFeature.TESTS in request.features,
            'has_models': AppFeature.MODELS in request.features,
            'has_views': AppFeature.VIEWS in request.features,
            'has_urls': AppFeature.URLS in request.features,
            
            # Advanced features
            'has_advanced_features': any(f in request.features for f in [
                AppFeature.SERIALIZERS, AppFeature.VIEWSETS, AppFeature.FILTERS,
                AppFeature.PAGINATION, AppFeature.SECURITY, AppFeature.TASKS
            ]),
            
            # Django-CFG specific
            'is_django_cfg': request.app_type == AppType.DJANGO_CFG,
            'has_cfg_features': any(f in request.features for f in [
                AppFeature.CFG_CONFIG, AppFeature.CFG_MODULES
            ]),
        })
        
        return {'features': features_dict}
    
    def _get_computed_variables(
        self,
        request: TemplateRequest,
        existing_vars: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Get computed variables based on existing variables."""
        app_name = existing_vars.get('app_name', 'myapp')
        
        computed = {
            # Model class names
            'model_class': f"{self._to_pascal_case(app_name)}Model",
            'admin_class': f"{self._to_pascal_case(app_name)}Admin",
            'form_class': f"{self._to_pascal_case(app_name)}Form",
            'serializer_class': f"{self._to_pascal_case(app_name)}Serializer",
            
            # View class names
            'list_view_class': f"{self._to_pascal_case(app_name)}ListView",
            'detail_view_class': f"{self._to_pascal_case(app_name)}DetailView",
            'create_view_class': f"{self._to_pascal_case(app_name)}CreateView",
            'update_view_class': f"{self._to_pascal_case(app_name)}UpdateView",
            'delete_view_class': f"{self._to_pascal_case(app_name)}DeleteView",
            
            # URL patterns
            'url_namespace': app_name,
            'url_prefix': self._to_kebab_case(app_name),
            
            # Template paths
            'template_dir': app_name,
            'list_template': f"{app_name}/list.html",
            'detail_template': f"{app_name}/detail.html",
            'form_template': f"{app_name}/form.html",
            
            # Database table name
            'db_table': f"{app_name}_{self._to_snake_case(app_name)}model",
            
            # Permissions
            'add_permission': f"{app_name}.add_{self._to_snake_case(app_name)}model",
            'change_permission': f"{app_name}.change_{self._to_snake_case(app_name)}model",
            'delete_permission': f"{app_name}.delete_{self._to_snake_case(app_name)}model",
            'view_permission': f"{app_name}.view_{self._to_snake_case(app_name)}model",
        }
        
        return computed
    
    # String transformation utilities
    def _to_snake_case(self, text: str) -> str:
        """Convert text to snake_case."""
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
        s2 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1)
        return s2.lower().replace(' ', '_').replace('-', '_')
    
    def _to_camel_case(self, text: str) -> str:
        """Convert text to camelCase."""
        components = re.split(r'[_\s-]+', text.lower())
        return components[0] + ''.join(word.capitalize() for word in components[1:])
    
    def _to_pascal_case(self, text: str) -> str:
        """Convert text to PascalCase."""
        components = re.split(r'[_\s-]+', text.lower())
        return ''.join(word.capitalize() for word in components)
    
    def _to_kebab_case(self, text: str) -> str:
        """Convert text to kebab-case."""
        return self._to_snake_case(text).replace('_', '-')
    
    def _to_title_case(self, text: str) -> str:
        """Convert text to Title Case."""
        return text.replace('_', ' ').replace('-', ' ').title()
    
    def _pluralize(self, text: str) -> str:
        """Simple pluralization."""
        if text.endswith('y'):
            return text[:-1] + 'ies'
        elif text.endswith(('s', 'sh', 'ch', 'x', 'z')):
            return text + 'es'
        else:
            return text + 's'
    
    def _singularize(self, text: str) -> str:
        """Simple singularization."""
        if text.endswith('ies'):
            return text[:-3] + 'y'
        elif text.endswith('es') and not text.endswith(('ses', 'ches', 'xes', 'zes')):
            return text[:-2]
        elif text.endswith('s') and not text.endswith('ss'):
            return text[:-1]
        else:
            return text
