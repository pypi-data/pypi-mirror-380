"""
Structure Generator for Django App Agent Module.

This module handles creation of basic application structure
and feature-specific files using templates.
"""

from typing import Dict, List
from pathlib import Path

from ..base import ServiceDependencies
from ...core.exceptions import FileSystemError
from ...models.responses import GeneratedFile
from ...models.enums import AppFeature, FileType
from .context import GenerationContext


class StructureGenerator:
    """Handles generation of application structure and files."""
    
    def __init__(self):
        """Initialize structure generator with feature file mappings."""
        self.feature_files: Dict[AppFeature, List[str]] = {
            AppFeature.MODELS: ["models.py"],
            AppFeature.VIEWS: ["views.py"],
            AppFeature.URLS: ["urls.py"],
            AppFeature.ADMIN: ["admin.py"],
            AppFeature.FORMS: ["forms.py"],
            AppFeature.TESTS: ["tests.py"],
            AppFeature.API: ["serializers.py", "viewsets.py"],
            AppFeature.SERIALIZERS: ["serializers.py"],
            AppFeature.VIEWSETS: ["viewsets.py"],
            AppFeature.FILTERS: ["filters.py"],
            AppFeature.PAGINATION: ["pagination.py"],
            AppFeature.SECURITY: ["security.py"],
            AppFeature.AUTHENTICATION: ["authentication.py"],
            AppFeature.TASKS: ["tasks.py"],
            AppFeature.DOCS: ["docs.py"],
            AppFeature.SERVICES: ["services/"],
            AppFeature.CFG_CONFIG: ["config.py"],
            AppFeature.CFG_MODULES: ["modules/"],
        }
    
    async def generate_app_structure(
        self,
        context: GenerationContext,
        dependencies: ServiceDependencies
    ) -> None:
        """Generate basic application directory structure."""
        try:
            # Create app directory
            context.app_directory.mkdir(parents=True, exist_ok=True)
            
            # Create basic structure
            basic_dirs = ["migrations", "templates", "static", "tests"]
            for dir_name in basic_dirs:
                (context.app_directory / dir_name).mkdir(exist_ok=True)
            
            # Create __init__.py
            init_file = context.app_directory / "__init__.py"
            init_content = f'"""Django app: {context.request.app_name}"""'
            
            generated_file = GeneratedFile(
                relative_path=str(init_file.relative_to(context.target_directory)),
                absolute_path=init_file,
                content=init_content,
                line_count=len(init_content.split('\n')),
                file_type=FileType.INIT,
                type_safety_score=8.0,
                complexity_score=2.0,  # Simple __init__.py file
                description="Application initialization file"
            )
            
            init_file.write_text(init_content)
            context.add_generated_file(generated_file)
            
        except Exception as e:
            raise FileSystemError(
                f"Failed to create app structure: {e}",
                file_path=str(context.app_directory),
                operation="create_app_structure"
            )
    
    async def generate_feature_files(
        self,
        context: GenerationContext,
        dependencies: ServiceDependencies
    ) -> None:
        """Generate files for requested features."""
        for feature in context.request.features:
            await self.generate_feature(feature, context, dependencies)
    
    async def generate_feature(
        self,
        feature: AppFeature,
        context: GenerationContext,
        dependencies: ServiceDependencies
    ) -> None:
        """Generate files for a specific feature."""
        files_to_create = self.feature_files.get(feature, [])
        
        for file_pattern in files_to_create:
            if file_pattern.endswith("/"):
                # Directory
                dir_path = context.app_directory / file_pattern.rstrip("/")
                dir_path.mkdir(parents=True, exist_ok=True)
            else:
                # File
                await self.generate_feature_file(feature, file_pattern, context, dependencies)
    
    async def generate_feature_file(
        self,
        feature: AppFeature,
        filename: str,
        context: GenerationContext,
        dependencies: ServiceDependencies
    ) -> None:
        """Generate a specific feature file."""
        file_path = context.app_directory / filename
        
        # Generate basic template content
        content = self.get_template_content(feature, filename, context)
        
        # Create generated file record
        generated_file = GeneratedFile(
            relative_path=str(file_path.relative_to(context.target_directory)),
            absolute_path=file_path,
            content=content,
            line_count=len(content.split('\n')),
            file_type=self.get_file_type(filename),
            type_safety_score=7.0,  # Default score for generated files
            complexity_score=5.0,  # Moderate complexity for feature files
            description=f"{feature.value} implementation file"
        )
        
        # Write file
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content)
        
        context.add_generated_file(generated_file)
    
    def get_template_content(
        self,
        feature: AppFeature,
        filename: str,
        context: GenerationContext
    ) -> str:
        """Get template content for a feature file."""
        app_name = context.request.app_name
        description = context.request.description
        
        templates = {
            "models.py": f'''"""
Models for {app_name} application.

{description}
"""

from django.db import models


class {app_name.title().replace('_', '')}Model(models.Model):
    """Main model for {app_name} application."""
    
    name = models.CharField(max_length=100, help_text="Name of the item")
    description = models.TextField(blank=True, help_text="Description of the item")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "{app_name.replace('_', ' ').title()}"
        verbose_name_plural = "{app_name.replace('_', ' ').title()}s"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name
''',
            "views.py": f'''"""
Views for {app_name} application.

{description}
"""

from django.shortcuts import render
from django.views.generic import ListView, DetailView


class {app_name.title().replace('_', '')}ListView(ListView):
    """List view for {app_name} items."""
    
    template_name = '{app_name}/list.html'
    context_object_name = 'items'
    paginate_by = 10


class {app_name.title().replace('_', '')}DetailView(DetailView):
    """Detail view for {app_name} items."""
    
    template_name = '{app_name}/detail.html'
    context_object_name = 'item'
''',
            "urls.py": f'''"""
URL configuration for {app_name} application.

{description}
"""

from django.urls import path
from . import views

app_name = '{app_name}'

urlpatterns = [
    path('', views.{app_name.title().replace('_', '')}ListView.as_view(), name='list'),
    path('<int:pk>/', views.{app_name.title().replace('_', '')}DetailView.as_view(), name='detail'),
]
''',
            "admin.py": f'''"""
Admin configuration for {app_name} application.

{description}
"""

from django.contrib import admin
from .models import {app_name.title().replace('_', '')}Model


@admin.register({app_name.title().replace('_', '')}Model)
class {app_name.title().replace('_', '')}Admin(admin.ModelAdmin):
    """Admin interface for {app_name} model."""
    
    list_display = ['name', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at', 'updated_at']
''',
            "forms.py": f'''"""
Forms for {app_name} application.

{description}
"""

from django import forms
from .models import {app_name.title().replace('_', '')}Model


class {app_name.title().replace('_', '')}Form(forms.ModelForm):
    """Form for {app_name} model."""
    
    class Meta:
        model = {app_name.title().replace('_', '')}Model
        fields = ['name', 'description']
        widgets = {{
            'description': forms.Textarea(attrs={{'rows': 4}}),
        }}
''',
            "tests.py": f'''"""
Tests for {app_name} application.

{description}
"""

from django.test import TestCase
from .models import {app_name.title().replace('_', '')}Model


class {app_name.title().replace('_', '')}TestCase(TestCase):
    """Test cases for {app_name} application."""
    
    def test_placeholder(self):
        """Placeholder test."""
        self.assertTrue(True)
''',
            "apps.py": f'''"""
App configuration for {app_name}.

{description}
"""

from django.apps import AppConfig


class {app_name.title().replace('_', '')}Config(AppConfig):
    """Configuration for {app_name} application."""
    
    default_auto_field = 'django.db.models.BigAutoField'
    name = '{app_name}'
    verbose_name = '{app_name.replace("_", " ").title()}'
'''
        }
        
        return templates.get(filename, f"# {filename} for {app_name}\n# Generated by Django App Agent\n")
    
    def get_file_type(self, filename: str) -> FileType:
        """Determine file type from filename."""
        # Map specific Django files to their types
        if filename == "__init__.py":
            return FileType.INIT
        elif filename == "models.py":
            return FileType.MODEL
        elif filename == "views.py":
            return FileType.VIEW
        elif filename == "admin.py":
            return FileType.ADMIN
        elif filename == "urls.py":
            return FileType.URL
        elif filename == "forms.py":
            return FileType.FORM
        elif filename == "tests.py":
            return FileType.TEST
        elif filename.endswith('.html'):
            return FileType.TEMPLATE
        elif filename.endswith('.py'):
            return FileType.CONFIG  # Default for other Python files
        else:
            return FileType.CONFIG  # Default fallback
