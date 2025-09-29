"""
Django App Discovery Module for Project Scanner.

This module handles discovery and analysis of Django applications
within a project structure.
"""

from typing import List, Optional, Dict, Any
from pathlib import Path
import ast
import re

from ...models.context import DjangoAppInfo
from ...models.enums import AppType
from ..base import ServiceDependencies
from .models import ProjectScanRequest, ScanResult


class AppDiscoveryEngine:
    """Handles discovery and analysis of Django applications."""
    
    def __init__(self):
        """Initialize app discovery engine."""
        # Django file patterns
        self.django_files = {
            "models.py": "models",
            "views.py": "views", 
            "urls.py": "urls",
            "admin.py": "admin",
            "forms.py": "forms",
            "tests.py": "tests",
            "apps.py": "apps",
            "serializers.py": "serializers",
            "signals.py": "signals",
            "middleware.py": "middleware",
            "management": "management_commands"
        }
    
    async def discover_django_apps(
        self,
        request: ProjectScanRequest,
        result: ScanResult,
        dependencies: ServiceDependencies
    ) -> None:
        """Discover Django applications in the project."""
        apps_found = []
        
        try:
            # Look for Django app indicators
            for path in request.project_root.rglob("apps.py"):
                app_dir = path.parent
                
                # Skip if too deep or excluded
                if len(app_dir.relative_to(request.project_root).parts) > request.scan_depth:
                    continue
                
                if self._is_excluded(app_dir.name, request.exclude_patterns):
                    continue
                
                # Analyze app structure
                app_info = await self.analyze_django_app(app_dir, request, dependencies)
                if app_info:
                    apps_found.append(app_info)
            
            # Also look for directories with Django files (even without apps.py)
            for django_file in self.django_files.keys():
                for path in request.project_root.rglob(django_file):
                    app_dir = path.parent
                    
                    # Skip if already found or excluded
                    if any(app.path == str(app_dir) for app in apps_found):
                        continue
                    
                    if self._is_excluded(app_dir.name, request.exclude_patterns):
                        continue
                    
                    # Check if it looks like a Django app
                    if self._looks_like_django_app(app_dir):
                        app_info = await self.analyze_django_app(app_dir, request, dependencies)
                        if app_info:
                            apps_found.append(app_info)
            
            result.discovered_apps = apps_found
            
        except Exception as e:
            dependencies.log_error("Failed to discover Django apps", e)
            # Don't fail the entire scan, just log the error
    
    async def analyze_django_app(
        self,
        app_dir: Path,
        request: ProjectScanRequest,
        dependencies: ServiceDependencies
    ) -> Optional[DjangoAppInfo]:
        """Analyze a single Django application."""
        try:
            app_name = app_dir.name
            
            # Count Django components
            models_count = self._count_models(app_dir)
            views_count = self._count_views(app_dir)
            urls_count = self._count_urls(app_dir)
            admin_registered = self._count_admin_registrations(app_dir)
            
            # Check for migrations
            has_migrations = (app_dir / "migrations").exists() and \
                           any((app_dir / "migrations").glob("*.py"))
            
            # Detect if it's a django-cfg app
            is_django_cfg_app = self._is_django_cfg_app(app_dir)
            
            # Analyze dependencies
            dependencies_list = self._analyze_app_dependencies(app_dir)
            
            return DjangoAppInfo(
                name=app_name,
                path=str(app_dir),
                is_django_cfg_app=is_django_cfg_app,
                models_count=models_count,
                views_count=views_count,
                urls_count=urls_count,
                admin_registered_models=admin_registered,
                has_migrations=has_migrations,
                dependencies=dependencies_list,
                description=self._extract_app_description(app_dir)
            )
            
        except Exception as e:
            dependencies.log_error(f"Failed to analyze app {app_dir.name}", e)
            return None
    
    def _is_excluded(self, name: str, exclude_patterns: List[str]) -> bool:
        """Check if name matches any exclude pattern."""
        for pattern in exclude_patterns:
            if pattern.startswith("*") and name.endswith(pattern[1:]):
                return True
            elif pattern.endswith("*") and name.startswith(pattern[:-1]):
                return True
            elif pattern == name:
                return True
        return False
    
    def _looks_like_django_app(self, app_dir: Path) -> bool:
        """Check if directory looks like a Django app."""
        django_indicators = ["models.py", "views.py", "apps.py", "admin.py"]
        found_indicators = sum(1 for indicator in django_indicators if (app_dir / indicator).exists())
        return found_indicators >= 2  # At least 2 Django files
    
    def _is_django_cfg_app(self, app_dir: Path) -> bool:
        """Check if app is a django-cfg app."""
        # Look for django-cfg specific patterns
        cfg_indicators = [
            "config.py",
            "cfg_config.py", 
            "modules/",
            "__cfg__.py"
        ]
        
        for indicator in cfg_indicators:
            if (app_dir / indicator).exists():
                return True
        
        # Check for django-cfg imports in apps.py
        apps_file = app_dir / "apps.py"
        if apps_file.exists():
            try:
                content = apps_file.read_text()
                if "django_cfg" in content or "BaseCfgModule" in content:
                    return True
            except Exception:
                pass
        
        return False
    
    def _count_models(self, app_dir: Path) -> int:
        """Count models in models.py."""
        models_file = app_dir / "models.py"
        if not models_file.exists():
            return 0
        
        try:
            content = models_file.read_text()
            tree = ast.parse(content)
            
            model_count = 0
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    # Check if it inherits from Model
                    for base in node.bases:
                        if isinstance(base, ast.Attribute) and base.attr == "Model":
                            model_count += 1
                        elif isinstance(base, ast.Name) and "Model" in base.id:
                            model_count += 1
            
            return model_count
        except Exception:
            return 0
    
    def _count_views(self, app_dir: Path) -> int:
        """Count views in views.py."""
        views_file = app_dir / "views.py"
        if not views_file.exists():
            return 0
        
        try:
            content = views_file.read_text()
            tree = ast.parse(content)
            
            view_count = 0
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    view_count += 1
                elif isinstance(node, ast.ClassDef):
                    # Check if it's a class-based view
                    for base in node.bases:
                        if isinstance(base, ast.Attribute) and "View" in base.attr:
                            view_count += 1
                        elif isinstance(base, ast.Name) and "View" in base.id:
                            view_count += 1
            
            return view_count
        except Exception:
            return 0
    
    def _count_urls(self, app_dir: Path) -> int:
        """Count URL patterns in urls.py."""
        urls_file = app_dir / "urls.py"
        if not urls_file.exists():
            return 0
        
        try:
            content = urls_file.read_text()
            # Count path() and url() calls
            path_count = content.count("path(")
            url_count = content.count("url(")
            return path_count + url_count
        except Exception:
            return 0
    
    def _count_admin_registrations(self, app_dir: Path) -> int:
        """Count admin registrations in admin.py."""
        admin_file = app_dir / "admin.py"
        if not admin_file.exists():
            return 0
        
        try:
            content = admin_file.read_text()
            # Count admin.register calls and @admin.register decorators
            register_count = content.count("admin.register(")
            decorator_count = content.count("@admin.register")
            return register_count + decorator_count
        except Exception:
            return 0
    
    def _analyze_app_dependencies(self, app_dir: Path) -> List[str]:
        """Analyze app dependencies from imports."""
        dependencies = set()
        
        # Analyze Python files for imports
        for py_file in app_dir.rglob("*.py"):
            try:
                content = py_file.read_text()
                tree = ast.parse(content)
                
                for node in ast.walk(tree):
                    if isinstance(node, ast.Import):
                        for alias in node.names:
                            if "." in alias.name:
                                dependencies.add(alias.name.split(".")[0])
                    elif isinstance(node, ast.ImportFrom):
                        if node.module:
                            if "." in node.module:
                                dependencies.add(node.module.split(".")[0])
                            else:
                                dependencies.add(node.module)
            except Exception:
                continue
        
        # Filter to keep only relevant dependencies
        relevant_deps = []
        for dep in dependencies:
            if dep in ["django", "rest_framework", "django_cfg"] or dep.startswith("django_"):
                relevant_deps.append(dep)
        
        return relevant_deps
    
    def _extract_app_description(self, app_dir: Path) -> Optional[str]:
        """Extract app description from apps.py or docstrings."""
        apps_file = app_dir / "apps.py"
        if apps_file.exists():
            try:
                content = apps_file.read_text()
                tree = ast.parse(content)
                
                for node in ast.walk(tree):
                    if isinstance(node, ast.ClassDef):
                        # Look for verbose_name in Config class
                        for item in node.body:
                            if isinstance(item, ast.Assign):
                                for target in item.targets:
                                    if isinstance(target, ast.Name) and target.id == "verbose_name":
                                        if isinstance(item.value, ast.Constant):
                                            return item.value.value
                        
                        # Use class docstring as fallback
                        if ast.get_docstring(node):
                            return ast.get_docstring(node)
            except Exception:
                pass
        
        return None
