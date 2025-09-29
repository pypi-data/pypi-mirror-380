"""
Main Project Scanner Service for Django App Agent Module.

This service provides comprehensive project structure analysis,
coordinating app discovery, dependency analysis, and pattern detection.
"""

from typing import Dict, Any
from pathlib import Path

from ..base import BaseService, ServiceDependencies
from ...models.context import ProjectContext
from ...core.exceptions import FileSystemError

from .models import ProjectScanRequest, ScanResult
from .app_discovery import AppDiscoveryEngine
from .pattern_detection import PatternDetectionEngine


class ProjectScannerService(BaseService[ProjectScanRequest, ScanResult]):
    """
    Service for comprehensive Django/django-cfg project analysis.
    
    Capabilities:
    - Discover Django applications and their structure
    - Analyze project dependencies and relationships
    - Detect architectural patterns and conventions
    - Generate comprehensive project context
    - Identify integration opportunities
    """
    
    def __init__(self, config):
        """Initialize project scanner service."""
        super().__init__("project_scanner", config)
        
        # Initialize sub-engines
        self.app_discovery = AppDiscoveryEngine()
        self.pattern_detection = PatternDetectionEngine()
    
    async def process(
        self, 
        request: ProjectScanRequest, 
        dependencies: ServiceDependencies
    ) -> ScanResult:
        """
        Process project scanning request.
        
        Args:
            request: Project scanning request
            dependencies: Service dependencies for logging and operations
            
        Returns:
            ScanResult with comprehensive project analysis
        """
        try:
            dependencies.log_operation(
                f"Starting project scan for '{request.project_root}'",
                project_root=str(request.project_root),
                scan_depth=request.scan_depth
            )
            
            # Initialize result with basic project context
            result = ScanResult(
                project_context=ProjectContext(
                    project_root=str(request.project_root),
                    project_name=request.project_root.name,
                    django_version="Unknown",
                    is_django_cfg_project=False,
                    apps=[],
                    architectural_patterns=[],
                    integration_opportunities=[]
                )
            )
            
            # Scan project structure
            await self._scan_project_structure(request, result, dependencies)
            
            # Discover Django applications
            await self.app_discovery.discover_django_apps(request, result, dependencies)
            
            # Analyze dependencies if requested
            if request.analyze_dependencies:
                await self._analyze_dependencies(request, result, dependencies)
            
            # Detect architectural patterns if requested
            if request.detect_patterns:
                await self.pattern_detection.detect_patterns(request, result, dependencies)
            
            # Update project context with findings
            self._update_project_context(result)
            
            dependencies.log_operation(
                "Project scan completed successfully",
                apps_found=len(result.discovered_apps),
                patterns_detected=len(result.architectural_patterns)
            )
            
            return result
            
        except Exception as e:
            raise FileSystemError(
                f"Failed to scan project structure: {e}",
                file_path=str(request.project_root),
                operation="scan_project"
            )
    
    async def _scan_project_structure(
        self,
        request: ProjectScanRequest,
        result: ScanResult,
        dependencies: ServiceDependencies
    ) -> None:
        """Scan basic project structure and collect file statistics."""
        try:
            file_counts = {}
            total_files = 0
            total_directories = 0
            directories_scanned = 0
            
            # Walk through project directory
            for path in request.project_root.rglob("*"):
                # Check depth limit
                relative_path = path.relative_to(request.project_root)
                if len(relative_path.parts) > request.scan_depth:
                    continue
                
                # Check exclusion patterns
                if self._is_excluded(path.name, request.exclude_patterns):
                    continue
                
                if path.is_file():
                    total_files += 1
                    suffix = path.suffix.lower()
                    file_counts[suffix] = file_counts.get(suffix, 0) + 1
                elif path.is_dir():
                    total_directories += 1
                    directories_scanned += 1
            
            # Store file summary
            result.file_summary = {
                "total_files": total_files,
                "total_directories": total_directories,
                "file_types": file_counts,
                "python_files": file_counts.get(".py", 0),
                "template_files": file_counts.get(".html", 0) + file_counts.get(".htm", 0),
                "static_files": file_counts.get(".css", 0) + file_counts.get(".js", 0) + file_counts.get(".scss", 0),
                "config_files": file_counts.get(".yml", 0) + file_counts.get(".yaml", 0) + file_counts.get(".json", 0)
            }
            
            # Store scan statistics
            result.scan_statistics = {
                "files_scanned": total_files,
                "directories_scanned": directories_scanned,
                "scan_depth": request.scan_depth
            }
            
        except Exception as e:
            raise FileSystemError(
                f"Failed to scan project structure: {e}",
                file_path=str(request.project_root),
                operation="scan_project"
            )
    
    async def _analyze_dependencies(
        self,
        request: ProjectScanRequest,
        result: ScanResult,
        dependencies: ServiceDependencies
    ) -> None:
        """Analyze dependencies between discovered apps."""
        try:
            dependency_graph = {}
            
            for app in result.discovered_apps:
                app_deps = []
                
                # Find dependencies to other discovered apps
                for other_app in result.discovered_apps:
                    if app.name != other_app.name:
                        # Check if app imports from other_app
                        if other_app.name in app.dependencies:
                            app_deps.append(other_app.name)
                
                dependency_graph[app.name] = app_deps
            
            result.dependency_graph = dependency_graph
            
        except Exception as e:
            dependencies.log_error("Failed to analyze dependencies", e)
    
    def _update_project_context(self, result: ScanResult) -> None:
        """Update project context with scan results."""
        # Check if it's a django-cfg project
        is_django_cfg = any(app.is_django_cfg_app for app in result.discovered_apps)
        
        # Detect Django version (placeholder)
        django_version = self.pattern_detection.detect_django_version(result.discovered_apps)
        
        # Update project context
        result.project_context.django_version = django_version
        result.project_context.is_django_cfg_project = is_django_cfg
        result.project_context.apps = result.discovered_apps
        result.project_context.architectural_patterns = result.architectural_patterns
        
        # Generate integration opportunities (placeholder)
        result.project_context.integration_opportunities = [
            "Consider adding API endpoints for existing models",
            "Implement caching for frequently accessed data",
            "Add comprehensive test coverage"
        ]
    
    def _is_excluded(self, name: str, exclude_patterns: list[str]) -> bool:
        """Check if name matches any exclude pattern."""
        for pattern in exclude_patterns:
            if pattern.startswith("*") and name.endswith(pattern[1:]):
                return True
            elif pattern.endswith("*") and name.startswith(pattern[:-1]):
                return True
            elif pattern == name:
                return True
        return False
