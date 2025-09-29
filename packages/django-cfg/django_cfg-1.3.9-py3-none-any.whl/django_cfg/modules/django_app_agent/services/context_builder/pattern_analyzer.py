"""
Pattern Analysis Module for Context Builder.

This module handles identification and analysis of architectural
patterns relevant to the development context.
"""

from typing import Set, List, Dict, Any

from ...models.context import ArchitecturalPattern
from ..base import ServiceDependencies
from .models import ContextBuildRequest, ContextResult


class PatternAnalyzer:
    """Handles analysis of architectural patterns for context building."""
    
    def __init__(self):
        """Initialize pattern analyzer."""
        # Pattern relevance mapping
        self.pattern_relevance = {
            "service_layer": {"models", "api", "business_logic"},
            "repository_pattern": {"models", "data_access"},
            "factory_pattern": {"models", "objects"},
            "observer_pattern": {"signals", "events"},
            "command_pattern": {"management_commands", "tasks"},
            "mvc_pattern": {"models", "views", "urls"},
            "api_pattern": {"api", "serializers", "viewsets"},
            "rest_api": {"api", "serializers", "viewsets", "rest_framework"},
            "graphql_api": {"api", "graphql", "schema"},
            "celery_tasks": {"tasks", "background_jobs"},
            "testing_pattern": {"tests", "testing"},
            "django_cfg_pattern": {"config", "modules", "django_cfg"}
        }
    
    async def identify_relevant_patterns(
        self,
        request: ContextBuildRequest,
        scan_result,
        result: ContextResult,
        dependencies: ServiceDependencies
    ) -> None:
        """Identify architectural patterns relevant to the generation request."""
        all_patterns = scan_result.architectural_patterns
        
        if not request.generation_request:
            # If no specific request, include all high-confidence patterns
            result.relevant_patterns = [p for p in all_patterns if p.confidence >= 0.7]
            return
        
        # Filter patterns based on requested features
        relevant_patterns = []
        requested_features = {f.value for f in request.generation_request.features}
        
        for pattern in all_patterns:
            # Check if pattern is relevant to requested features
            if self._is_pattern_relevant(pattern, requested_features):
                relevant_patterns.append(pattern)
        
        result.relevant_patterns = relevant_patterns
    
    def _is_pattern_relevant(self, pattern: ArchitecturalPattern, features: Set[str]) -> bool:
        """Check if architectural pattern is relevant to requested features."""
        relevant_features = self.pattern_relevance.get(pattern.name, set())
        return bool(relevant_features.intersection(features))
    
    def analyze_pattern_compatibility(
        self,
        patterns: List[ArchitecturalPattern],
        requested_features: Set[str]
    ) -> Dict[str, float]:
        """Analyze compatibility between patterns and requested features."""
        compatibility_scores = {}
        
        for pattern in patterns:
            relevant_features = self.pattern_relevance.get(pattern.name, set())
            overlap = len(relevant_features.intersection(requested_features))
            total_relevant = len(relevant_features)
            
            if total_relevant > 0:
                compatibility_scores[pattern.name] = (overlap / total_relevant) * pattern.confidence
            else:
                compatibility_scores[pattern.name] = 0.0
        
        return compatibility_scores
