"""
Architectural Pattern Detection Module for Project Scanner.

This module handles detection of architectural patterns and
conventions within Django/django-cfg projects.
"""

from typing import List, Dict, Any
from pathlib import Path

from ...models.context import ArchitecturalPattern
from ..base import ServiceDependencies
from .models import ProjectScanRequest, ScanResult


class PatternDetectionEngine:
    """Handles detection of architectural patterns in projects."""
    
    def __init__(self):
        """Initialize pattern detection engine."""
        # Architectural pattern indicators
        self.pattern_indicators = {
            "mvc_pattern": ["models.py", "views.py", "templates/"],
            "api_pattern": ["serializers.py", "viewsets.py", "api/"],
            "service_layer": ["services/", "services.py"],
            "repository_pattern": ["repositories/", "repository.py"],
            "factory_pattern": ["factories/", "factory.py"],
            "command_pattern": ["management/commands/", "commands/"],
            "observer_pattern": ["signals.py", "observers/"],
            "middleware_pattern": ["middleware.py", "middleware/"],
            "django_cfg_pattern": ["config.py", "cfg_config.py", "modules/"],
            "rest_api": ["rest_framework", "serializers.py", "viewsets.py"],
            "graphql_api": ["graphene", "schema.py", "graphql/"],
            "celery_tasks": ["tasks.py", "celery.py", "workers/"],
            "testing_pattern": ["tests/", "test_*.py", "conftest.py"],
            "documentation": ["docs/", "README.md", "*.rst"],
            "containerization": ["Dockerfile", "docker-compose.yml", ".dockerignore"],
            "ci_cd": [".github/", ".gitlab-ci.yml", "Jenkinsfile"],
        }
    
    async def detect_patterns(
        self,
        request: ProjectScanRequest,
        result: ScanResult,
        dependencies: ServiceDependencies
    ) -> None:
        """Detect architectural patterns in the project."""
        try:
            patterns = []
            
            for pattern_name, indicators in self.pattern_indicators.items():
                evidence = []
                files_using_pattern = []
                
                for indicator in indicators:
                    # Search for pattern indicators
                    if indicator.endswith("/"):
                        # Directory pattern
                        for path in request.project_root.rglob(indicator.rstrip("/")):
                            if path.is_dir():
                                evidence.append(f"Directory: {path.relative_to(request.project_root)}")
                                # Find files in this directory
                                for file in path.rglob("*.py"):
                                    files_using_pattern.append(str(file.relative_to(request.project_root)))
                    else:
                        # File pattern
                        for path in request.project_root.rglob(indicator):
                            if path.is_file():
                                evidence.append(f"File: {path.relative_to(request.project_root)}")
                                files_using_pattern.append(str(path.relative_to(request.project_root)))
                
                if evidence:
                    # Calculate confidence based on evidence strength
                    confidence = min(1.0, len(evidence) / 3.0)  # Max confidence with 3+ pieces of evidence
                    
                    pattern = ArchitecturalPattern(
                        name=pattern_name,
                        description=f"Detected {pattern_name.replace('_', ' ')} pattern",
                        confidence=confidence,
                        evidence=evidence[:10],  # Limit evidence list
                        files_using_pattern=files_using_pattern[:20]  # Limit file list
                    )
                    patterns.append(pattern)
            
            result.architectural_patterns = patterns
            
        except Exception as e:
            dependencies.log_error("Failed to detect patterns", e)
    
    def detect_django_version(self, apps: List[Any]) -> str:
        """Detect Django version from project structure."""
        # This is a placeholder - would need actual implementation
        # based on Django features used in the codebase
        return "5.0+"  # Default assumption for modern projects
