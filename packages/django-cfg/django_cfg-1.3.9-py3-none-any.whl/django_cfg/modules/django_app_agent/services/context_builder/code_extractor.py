"""
Code Extraction Module for Context Builder.

This module handles extraction of relevant code samples
and examples from existing project files.
"""

from typing import Dict, Optional
from pathlib import Path

from ..base import ServiceDependencies
from .models import ContextBuildRequest, ContextResult


class CodeExtractor:
    """Handles extraction of code samples for context building."""
    
    def __init__(self):
        """Initialize code extractor."""
        # Map features to their corresponding files
        self.feature_files = {
            "models": "models.py",
            "views": "views.py", 
            "urls": "urls.py",
            "admin": "admin.py",
            "forms": "forms.py",
            "tests": "tests.py",
            "serializers": "serializers.py",
            "viewsets": "viewsets.py",
            "filters": "filters.py",
            "pagination": "pagination.py",
            "tasks": "tasks.py",
            "signals": "signals.py",
            "middleware": "middleware.py"
        }
    
    async def extract_code_samples(
        self,
        request: ContextBuildRequest,
        result: ContextResult,
        dependencies: ServiceDependencies
    ) -> None:
        """Extract relevant code samples for context."""
        if not request.generation_request:
            return
        
        samples = {}
        
        # Extract samples for each requested feature
        for feature in request.generation_request.features:
            feature_samples = await self._extract_feature_samples(
                feature.value, request, result, dependencies
            )
            if feature_samples:
                samples[feature.value] = feature_samples
        
        result.code_samples = samples
    
    async def _extract_feature_samples(
        self,
        feature: str,
        request: ContextBuildRequest,
        result: ContextResult,
        dependencies: ServiceDependencies
    ) -> Optional[str]:
        """Extract code samples for a specific feature."""
        # Find the best example of this feature in existing apps
        best_sample = None
        max_complexity = 0
        
        for app in result.project_context.apps:
            app_path = Path(app.path)
            
            filename = self.feature_files.get(feature)
            if not filename:
                continue
            
            file_path = app_path / filename
            if not file_path.exists():
                continue
            
            try:
                content = file_path.read_text()
                
                # Simple complexity measure (lines of meaningful code)
                lines = [line.strip() for line in content.split('\n')]
                meaningful_lines = [line for line in lines if line and not line.startswith('#')]
                complexity = len(meaningful_lines)
                
                if complexity > max_complexity:
                    max_complexity = complexity
                    # Truncate sample if too long
                    if len(content) > 2000:
                        content = content[:2000] + "\n# ... (truncated)"
                    best_sample = content
                    
            except Exception:
                continue
        
        return best_sample
    
    def extract_specific_patterns(
        self,
        project_root: Path,
        pattern_type: str,
        max_samples: int = 3
    ) -> Dict[str, str]:
        """Extract specific code patterns from the project."""
        samples = {}
        
        pattern_searches = {
            "model_definitions": ["models.py"],
            "view_classes": ["views.py"],
            "url_patterns": ["urls.py"],
            "admin_configs": ["admin.py"],
            "serializer_classes": ["serializers.py"],
            "test_cases": ["tests.py", "test_*.py"]
        }
        
        search_files = pattern_searches.get(pattern_type, [])
        
        for search_pattern in search_files:
            for file_path in project_root.rglob(search_pattern):
                if file_path.is_file():
                    try:
                        content = file_path.read_text()
                        relative_path = file_path.relative_to(project_root)
                        
                        # Truncate if too long
                        if len(content) > 1500:
                            content = content[:1500] + "\n# ... (truncated)"
                        
                        samples[str(relative_path)] = content
                        
                        # Limit number of samples
                        if len(samples) >= max_samples:
                            break
                    except Exception:
                        continue
        
        return samples
