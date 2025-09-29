"""
Template Manager Service for Django App Agent Module.

This package provides sophisticated Jinja2-based template rendering
with feature-driven code generation capabilities.
"""

from .main import TemplateManagerService
from .jinja_engine import JinjaTemplateEngine
from .template_loader import TemplateLoader
from .variable_processor import VariableProcessor

__all__ = [
    "TemplateManagerService",
    "JinjaTemplateEngine",
    "TemplateLoader", 
    "VariableProcessor",
]
