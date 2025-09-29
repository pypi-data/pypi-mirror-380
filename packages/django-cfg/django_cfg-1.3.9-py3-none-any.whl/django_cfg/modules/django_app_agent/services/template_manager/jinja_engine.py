"""
Jinja2 Template Engine for Django App Agent.

This module provides a powerful Jinja2-based template engine
with custom filters and functions for Django code generation.
"""

from typing import Dict, Any, Set, Optional, List
import re
from pathlib import Path

from jinja2 import Environment, BaseLoader, TemplateNotFound, select_autoescape
from jinja2.exceptions import TemplateError

from ...core.exceptions import ValidationError


class StringTemplateLoader(BaseLoader):
    """Custom Jinja2 loader for string-based templates."""
    
    def __init__(self, templates: Dict[str, str]):
        """Initialize with template dictionary."""
        self.templates = templates
    
    def get_source(self, environment: Environment, template: str) -> tuple:
        """Get template source."""
        if template not in self.templates:
            raise TemplateNotFound(template)
        
        source = self.templates[template]
        return source, None, lambda: True


class JinjaTemplateEngine:
    """Jinja2-based template engine with Django-specific features."""
    
    def __init__(self):
        """Initialize Jinja2 environment with custom filters."""
        self.templates: Dict[str, str] = {}
        self.env = self._create_environment()
    
    def _create_environment(self) -> Environment:
        """Create Jinja2 environment with custom filters and functions."""
        env = Environment(
            loader=StringTemplateLoader(self.templates),
            autoescape=select_autoescape(['html', 'xml']),
            trim_blocks=True,
            lstrip_blocks=True
        )
        
        # Add custom filters
        env.filters.update({
            'snake_case': self._snake_case,
            'camel_case': self._camel_case,
            'pascal_case': self._pascal_case,
            'kebab_case': self._kebab_case,
            'title_case': self._title_case,
            'plural': self._pluralize,
            'singular': self._singularize,
            'django_field': self._django_field_repr,
            'python_repr': self._python_repr,
            'indent': self._indent,
            'comment_block': self._comment_block
        })
        
        # Add custom functions
        env.globals.update({
            'now': self._now,
            'uuid4': self._uuid4,
            'range': range,
            'enumerate': enumerate,
            'zip': zip
        })
        
        return env
    
    def add_template(self, name: str, content: str) -> None:
        """Add a template to the engine."""
        self.templates[name] = content
        # Recreate environment to update loader
        self.env = self._create_environment()
    
    def add_templates(self, templates: Dict[str, str]) -> None:
        """Add multiple templates to the engine."""
        self.templates.update(templates)
        # Recreate environment to update loader
        self.env = self._create_environment()
    
    def render(
        self, 
        template_name: str, 
        variables: Dict[str, Any]
    ) -> tuple[str, Set[str], Set[str]]:
        """
        Render template with variables.
        
        Returns:
            tuple: (rendered_content, variables_used, missing_variables)
        """
        try:
            template = self.env.get_template(template_name)
            
            # Get template variables (simplified approach - read template source from file)
            template_vars = set()
            try:
                # Get template source from the loader
                source, _ = self.env.loader.get_source(self.env, template_name)
                ast = self.env.parse(source)
                for node in ast.find_all('Name'):
                    if node.ctx == 'load':
                        template_vars.add(node.name)
            except Exception:
                # Fallback: assume all provided variables are used
                template_vars = set(variables.keys())
            
            # Remove Jinja2 built-ins and our custom functions
            builtin_vars = {
                'range', 'enumerate', 'zip', 'now', 'uuid4',
                'loop', 'super', 'self', 'varargs', 'kwargs'
            }
            template_vars = template_vars - builtin_vars
            
            # Check for missing variables
            missing_vars = template_vars - set(variables.keys())
            variables_used = template_vars - missing_vars
            
            # Render template
            rendered = template.render(**variables)
            
            return rendered, variables_used, missing_vars
            
        except TemplateNotFound:
            raise ValidationError(
                f"Template '{template_name}' not found",
                validation_type="template_not_found"
            )
        except TemplateError as e:
            raise ValidationError(
                f"Template rendering failed: {e}",
                validation_type="template_rendering"
            )
    
    # Custom filters
    def _snake_case(self, text: str) -> str:
        """Convert text to snake_case."""
        # Handle camelCase and PascalCase
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
        s2 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1)
        return s2.lower().replace(' ', '_').replace('-', '_')
    
    def _camel_case(self, text: str) -> str:
        """Convert text to camelCase."""
        components = re.split(r'[_\s-]+', text.lower())
        return components[0] + ''.join(word.capitalize() for word in components[1:])
    
    def _pascal_case(self, text: str) -> str:
        """Convert text to PascalCase."""
        components = re.split(r'[_\s-]+', text.lower())
        return ''.join(word.capitalize() for word in components)
    
    def _kebab_case(self, text: str) -> str:
        """Convert text to kebab-case."""
        return self._snake_case(text).replace('_', '-')
    
    def _title_case(self, text: str) -> str:
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
        elif text.endswith('es'):
            return text[:-2]
        elif text.endswith('s') and not text.endswith('ss'):
            return text[:-1]
        else:
            return text
    
    def _django_field_repr(self, field_type: str, **kwargs) -> str:
        """Generate Django field representation."""
        args = []
        for key, value in kwargs.items():
            if isinstance(value, str):
                args.append(f"{key}='{value}'")
            else:
                args.append(f"{key}={value}")
        
        if args:
            return f"models.{field_type}({', '.join(args)})"
        else:
            return f"models.{field_type}()"
    
    def _python_repr(self, value: Any) -> str:
        """Python representation of value."""
        return repr(value)
    
    def _indent(self, text: str, width: int = 4, first: bool = False) -> str:
        """Indent text by specified width."""
        lines = text.split('\n')
        indent_str = ' ' * width
        
        if first:
            return '\n'.join(indent_str + line for line in lines)
        else:
            return lines[0] + '\n' + '\n'.join(indent_str + line for line in lines[1:])
    
    def _comment_block(self, text: str, style: str = 'python') -> str:
        """Create comment block in specified style."""
        if style == 'python':
            lines = text.split('\n')
            return '\n'.join(f'# {line}' for line in lines)
        elif style == 'docstring':
            return f'"""\n{text}\n"""'
        else:
            return text
    
    # Custom functions
    def _now(self) -> str:
        """Current timestamp."""
        from datetime import datetime
        return datetime.now().isoformat()
    
    def _uuid4(self) -> str:
        """Generate UUID4."""
        import uuid
        return str(uuid.uuid4())
