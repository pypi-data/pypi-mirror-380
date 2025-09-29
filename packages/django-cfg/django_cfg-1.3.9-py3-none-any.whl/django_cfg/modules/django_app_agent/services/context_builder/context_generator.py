"""
Context Generation Module for Context Builder.

This module handles generation of specific context for different
Django features and components.
"""

from typing import List, Dict, Any
from pathlib import Path
import re

from ..base import ServiceDependencies
from .models import ContextBuildRequest, ContextResult


class ContextGenerator:
    """Handles generation of feature-specific context."""
    
    def __init__(self):
        """Initialize context generator."""
        # Map features to their context building strategies
        self.context_strategies = {
            "models": self._build_models_context,
            "views": self._build_views_context,
            "urls": self._build_urls_context,
            "admin": self._build_admin_context,
            "api": self._build_api_context,
            "tests": self._build_tests_context,
            "serializers": self._build_api_context,
            "viewsets": self._build_api_context,
            "forms": self._build_forms_context
        }
    
    async def build_generation_context(
        self,
        request: ContextBuildRequest,
        result: ContextResult,
        dependencies: ServiceDependencies
    ) -> None:
        """Build context specific to the generation request."""
        gen_request = request.generation_request
        if not gen_request:
            return
        
        # Build context for each requested feature
        for feature in gen_request.features:
            feature_name = feature.value
            
            if feature_name in self.context_strategies:
                strategy = self.context_strategies[feature_name]
                await strategy(request, result, dependencies)
    
    async def _build_models_context(
        self,
        request: ContextBuildRequest,
        result: ContextResult,
        dependencies: ServiceDependencies
    ) -> None:
        """Build context for models generation."""
        # Find existing models in the project
        existing_models = []
        
        for app in result.project_context.apps:
            if app.models_count > 0:
                app_path = Path(app.path)
                models_file = app_path / "models.py"
                
                if models_file.exists():
                    try:
                        content = models_file.read_text()
                        # Extract model class names
                        model_classes = re.findall(r'class\s+(\w+)\s*\([^)]*Model[^)]*\):', content)
                        existing_models.extend([(app.name, model) for model in model_classes])
                    except Exception:
                        pass
        
        # Add to context summary
        result.context_summary["existing_models"] = existing_models
        result.context_summary["model_patterns"] = [
            p for p in result.relevant_patterns 
            if "model" in p.name.lower() or "data" in p.name.lower()
        ]
    
    async def _build_views_context(
        self,
        request: ContextBuildRequest,
        result: ContextResult,
        dependencies: ServiceDependencies
    ) -> None:
        """Build context for views generation."""
        # Find existing view patterns
        view_patterns = []
        
        for app in result.project_context.apps:
            if app.views_count > 0:
                app_path = Path(app.path)
                views_file = app_path / "views.py"
                
                if views_file.exists():
                    try:
                        content = views_file.read_text()
                        
                        # Detect view types
                        if "class" in content and "View" in content:
                            view_patterns.append("class_based_views")
                        if "def " in content and "request" in content:
                            view_patterns.append("function_based_views")
                        if "async def" in content:
                            view_patterns.append("async_views")
                            
                    except Exception:
                        pass
        
        result.context_summary["view_patterns"] = list(set(view_patterns))
    
    async def _build_urls_context(
        self,
        request: ContextBuildRequest,
        result: ContextResult,
        dependencies: ServiceDependencies
    ) -> None:
        """Build context for URLs generation."""
        # Analyze URL patterns in existing apps
        url_patterns = []
        
        for app in result.project_context.apps:
            app_path = Path(app.path)
            urls_file = app_path / "urls.py"
            
            if urls_file.exists():
                try:
                    content = urls_file.read_text()
                    
                    # Detect URL pattern styles
                    if "path(" in content:
                        url_patterns.append("django_path")
                    if "re_path(" in content:
                        url_patterns.append("regex_path")
                    if "include(" in content:
                        url_patterns.append("url_include")
                        
                except Exception:
                    pass
        
        result.context_summary["url_patterns"] = list(set(url_patterns))
    
    async def _build_admin_context(
        self,
        request: ContextBuildRequest,
        result: ContextResult,
        dependencies: ServiceDependencies
    ) -> None:
        """Build context for admin generation."""
        # Find admin registration patterns
        admin_patterns = []
        
        for app in result.project_context.apps:
            if app.admin_registered_models > 0:
                app_path = Path(app.path)
                admin_file = app_path / "admin.py"
                
                if admin_file.exists():
                    try:
                        content = admin_file.read_text()
                        
                        # Detect admin patterns
                        if "@admin.register" in content:
                            admin_patterns.append("decorator_registration")
                        if "admin.site.register" in content:
                            admin_patterns.append("function_registration")
                        if "ModelAdmin" in content:
                            admin_patterns.append("custom_admin_classes")
                            
                    except Exception:
                        pass
        
        result.context_summary["admin_patterns"] = list(set(admin_patterns))
    
    async def _build_api_context(
        self,
        request: ContextBuildRequest,
        result: ContextResult,
        dependencies: ServiceDependencies
    ) -> None:
        """Build context for API generation."""
        # Find API patterns
        api_patterns = []
        
        for app in result.project_context.apps:
            app_path = Path(app.path)
            
            # Check for DRF patterns
            for api_file in ["serializers.py", "viewsets.py", "views.py"]:
                file_path = app_path / api_file
                if file_path.exists():
                    try:
                        content = file_path.read_text()
                        
                        if "rest_framework" in content:
                            api_patterns.append("django_rest_framework")
                        if "Serializer" in content:
                            api_patterns.append("serializers")
                        if "ViewSet" in content:
                            api_patterns.append("viewsets")
                        if "APIView" in content:
                            api_patterns.append("api_views")
                            
                    except Exception:
                        pass
        
        result.context_summary["api_patterns"] = list(set(api_patterns))
    
    async def _build_tests_context(
        self,
        request: ContextBuildRequest,
        result: ContextResult,
        dependencies: ServiceDependencies
    ) -> None:
        """Build context for tests generation."""
        # Find testing patterns
        test_patterns = []
        
        for app in result.project_context.apps:
            app_path = Path(app.path)
            
            # Check for test files
            test_files = list(app_path.glob("test*.py")) + [app_path / "tests.py"]
            
            for test_file in test_files:
                if test_file.exists():
                    try:
                        content = test_file.read_text()
                        
                        if "TestCase" in content:
                            test_patterns.append("django_testcase")
                        if "pytest" in content or "def test_" in content:
                            test_patterns.append("pytest")
                        if "Client" in content:
                            test_patterns.append("test_client")
                        if "factory" in content.lower():
                            test_patterns.append("factory_boy")
                            
                    except Exception:
                        pass
        
        result.context_summary["test_patterns"] = list(set(test_patterns))
    
    async def _build_forms_context(
        self,
        request: ContextBuildRequest,
        result: ContextResult,
        dependencies: ServiceDependencies
    ) -> None:
        """Build context for forms generation."""
        # Find form patterns
        form_patterns = []
        
        for app in result.project_context.apps:
            app_path = Path(app.path)
            forms_file = app_path / "forms.py"
            
            if forms_file.exists():
                try:
                    content = forms_file.read_text()
                    
                    if "ModelForm" in content:
                        form_patterns.append("model_forms")
                    if "Form" in content and "ModelForm" not in content:
                        form_patterns.append("regular_forms")
                    if "widgets" in content:
                        form_patterns.append("custom_widgets")
                        
                except Exception:
                    pass
        
        result.context_summary["form_patterns"] = list(set(form_patterns))
