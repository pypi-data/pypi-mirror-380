"""
Context models for Django App Agent Module.

This module defines context models for:
- Project structure analysis
- Django app information
- Architectural patterns
- Infrastructure context
"""

from typing import List, Optional, Dict, Any, Set
from pathlib import Path
from pydantic import Field, field_validator, computed_field

from .base import BaseAgentModel, ValidationMixin
from .enums import AppType, AppFeature


class ArchitecturalPattern(BaseAgentModel):
    """Information about an architectural pattern found in the project."""
    
    name: str = Field(
        description="Name of the architectural pattern",
        min_length=1,
        max_length=100
    )
    
    description: str = Field(
        description="Description of the pattern and its purpose",
        min_length=10,
        max_length=500
    )
    
    confidence: float = Field(
        ge=0.0,
        le=1.0,
        description="Confidence level in pattern detection (0-1)"
    )
    
    evidence: List[str] = Field(
        default_factory=list,
        description="Evidence supporting the presence of this pattern"
    )
    
    files_using_pattern: List[str] = Field(
        default_factory=list,
        description="Files that implement this pattern"
    )
    
    benefits: List[str] = Field(
        default_factory=list,
        description="Benefits of using this pattern"
    )
    
    implementation_notes: List[str] = Field(
        default_factory=list,
        description="Notes on how the pattern is implemented"
    )
    
    @computed_field
    @property
    def is_high_confidence(self) -> bool:
        """Check if this pattern detection has high confidence."""
        return self.confidence >= 0.8
    
    @computed_field
    @property
    def usage_score(self) -> float:
        """Calculate usage score based on evidence and files."""
        evidence_score = min(1.0, len(self.evidence) / 3.0)  # Reduced threshold
        files_score = min(1.0, len(self.files_using_pattern) / 2.0)  # Reduced threshold
        return (evidence_score + files_score + self.confidence) / 3.0


class DjangoAppInfo(BaseAgentModel, ValidationMixin):
    """Information about a Django application in the project."""
    
    name: str = Field(
        description="Name of the Django app",
        min_length=1,
        max_length=50
    )
    
    path: Path = Field(
        description="Path to the app directory"
    )
    
    # App structure information
    has_models: bool = Field(
        default=False,
        description="Whether the app has models"
    )
    
    has_views: bool = Field(
        default=False,
        description="Whether the app has views"
    )
    
    has_admin: bool = Field(
        default=False,
        description="Whether the app has admin configuration"
    )
    
    has_tests: bool = Field(
        default=False,
        description="Whether the app has tests"
    )
    
    has_services: bool = Field(
        default=False,
        description="Whether the app uses service layer pattern"
    )
    
    has_async_views: bool = Field(
        default=False,
        description="Whether the app has async views"
    )
    
    # Pattern information
    model_patterns: List[str] = Field(
        default_factory=list,
        description="Patterns used in models"
    )
    
    view_patterns: List[str] = Field(
        default_factory=list,
        description="Patterns used in views"
    )
    
    service_patterns: List[str] = Field(
        default_factory=list,
        description="Patterns used in services"
    )
    
    test_patterns: List[str] = Field(
        default_factory=list,
        description="Patterns used in tests"
    )
    
    # Metrics
    dependencies: List[str] = Field(
        default_factory=list,
        description="External dependencies used by this app"
    )
    
    lines_of_code: int = Field(
        ge=0,
        default=0,
        description="Total lines of code in the app"
    )
    
    complexity_score: float = Field(
        ge=0.0,
        le=10.0,
        default=5.0,
        description="Complexity score of the app (0-10)"
    )
    
    quality_score: float = Field(
        ge=0.0,
        le=10.0,
        default=7.0,
        description="Quality score of the app (0-10)"
    )
    
    @field_validator('name')
    @classmethod
    def validate_app_name(cls, v: str) -> str:
        """Validate Django app name."""
        from ..utils.validation import validate_app_name
        return validate_app_name(v, check_reserved=False)
    
    @computed_field
    @property
    def features_implemented(self) -> Set[AppFeature]:
        """Get set of features implemented by this app."""
        features = set()
        
        if self.has_models:
            features.add(AppFeature.MODELS)
        if self.has_views:
            features.add(AppFeature.VIEWS)
        if self.has_admin:
            features.add(AppFeature.ADMIN)
        if self.has_tests:
            features.add(AppFeature.TESTS)
        
        return features
    
    @computed_field
    @property
    def all_patterns(self) -> Set[str]:
        """Get all patterns used in this app."""
        all_patterns = set()
        all_patterns.update(self.model_patterns)
        all_patterns.update(self.view_patterns)
        all_patterns.update(self.service_patterns)
        all_patterns.update(self.test_patterns)
        return all_patterns
    
    @computed_field
    @property
    def is_well_structured(self) -> bool:
        """Check if app follows good structure practices."""
        return (
            self.has_models and
            self.has_views and
            self.has_tests and
            self.quality_score >= 7.0
        )
    
    def get_integration_compatibility(self, other_app: "DjangoAppInfo") -> float:
        """Calculate compatibility score with another app."""
        # Compare patterns
        common_patterns = self.all_patterns & other_app.all_patterns
        total_patterns = self.all_patterns | other_app.all_patterns
        
        if not total_patterns:
            return 0.5  # Neutral if no patterns
        
        pattern_similarity = len(common_patterns) / len(total_patterns)
        
        # Compare dependencies
        common_deps = set(self.dependencies) & set(other_app.dependencies)
        total_deps = set(self.dependencies) | set(other_app.dependencies)
        
        if total_deps:
            dep_similarity = len(common_deps) / len(total_deps)
        else:
            dep_similarity = 1.0  # Perfect if no dependencies
        
        # Weighted average
        return (pattern_similarity * 0.7 + dep_similarity * 0.3)


class ProjectContext(BaseAgentModel):
    """Context information about the Django project."""
    
    project_path: Path = Field(
        description="Path to the Django project root"
    )
    
    project_type: str = Field(
        default="django",
        description="Type of Django project (django, django_cfg)"
    )
    
    # Project structure
    django_apps: List[DjangoAppInfo] = Field(
        default_factory=list,
        description="Information about Django apps in the project"
    )
    
    # Architectural information
    architectural_patterns: List[str] = Field(
        default_factory=list,
        description="Architectural patterns used across the project"
    )
    
    security_features: List[str] = Field(
        default_factory=list,
        description="Security features implemented in the project"
    )
    
    performance_features: List[str] = Field(
        default_factory=list,
        description="Performance optimization features"
    )
    
    testing_patterns: List[str] = Field(
        default_factory=list,
        description="Testing patterns and frameworks used"
    )
    
    # Quality metrics
    documentation_level: str = Field(
        default="basic",
        description="Level of documentation (basic, good, comprehensive)"
    )
    
    code_quality_score: float = Field(
        ge=0.0,
        le=10.0,
        default=7.0,
        description="Overall code quality score"
    )
    
    type_safety_percentage: float = Field(
        ge=0.0,
        le=100.0,
        default=70.0,
        description="Percentage of code that is type-safe"
    )
    
    @field_validator('project_path')
    @classmethod
    def validate_project_path(cls, v: Path) -> Path:
        """Validate project path exists."""
        from ..utils.validation import validate_file_path
        return validate_file_path(v, must_exist=True, must_be_dir=True)
    
    @computed_field
    @property
    def total_apps_count(self) -> int:
        """Get total number of Django apps."""
        return len(self.django_apps)
    
    @computed_field
    @property
    def apps_with_tests_count(self) -> int:
        """Get number of apps with tests."""
        return sum(1 for app in self.django_apps if app.has_tests)
    
    @computed_field
    @property
    def test_coverage_percentage(self) -> float:
        """Calculate test coverage percentage."""
        if not self.django_apps:
            return 0.0
        return (self.apps_with_tests_count / self.total_apps_count) * 100
    
    @computed_field
    @property
    def common_patterns(self) -> Set[str]:
        """Get patterns that are common across multiple apps."""
        if len(self.django_apps) < 2:
            return set()
        
        pattern_counts: Dict[str, int] = {}
        for app in self.django_apps:
            for pattern in app.all_patterns:
                pattern_counts[pattern] = pattern_counts.get(pattern, 0) + 1
        
        # Patterns used in at least 50% of apps
        threshold = max(1, len(self.django_apps) // 2)
        return {pattern for pattern, count in pattern_counts.items() if count >= threshold}
    
    def get_app_by_name(self, name: str) -> Optional[DjangoAppInfo]:
        """Get app information by name."""
        for app in self.django_apps:
            if app.name == name:
                return app
        return None
    
    def get_apps_using_pattern(self, pattern: str) -> List[DjangoAppInfo]:
        """Get apps that use a specific pattern."""
        return [app for app in self.django_apps if pattern in app.all_patterns]
    
    def get_recommended_patterns_for_new_app(self) -> List[str]:
        """Get recommended patterns for a new app based on existing patterns."""
        # Prioritize common patterns
        common = list(self.common_patterns)
        
        # Add project-level architectural patterns
        project_patterns = [p for p in self.architectural_patterns if p not in common]
        
        return common + project_patterns
    
    def analyze_integration_opportunities(self, app_name: str) -> Dict[str, Any]:
        """Analyze integration opportunities for a new app."""
        similar_apps = []
        potential_dependencies = set()
        
        # Find apps with similar patterns
        for app in self.django_apps:
            if len(app.all_patterns) > 0:
                similar_apps.append({
                    "name": app.name,
                    "similarity_score": len(app.all_patterns & self.common_patterns) / len(app.all_patterns),
                    "patterns": list(app.all_patterns)
                })
        
        # Sort by similarity
        similar_apps.sort(key=lambda x: x["similarity_score"], reverse=True)
        
        # Identify potential dependencies
        for app in self.django_apps:
            if app.has_models and "user" in app.name.lower():
                potential_dependencies.add(f"{app.name}.models")
        
        return {
            "similar_apps": similar_apps[:3],  # Top 3 similar apps
            "potential_dependencies": list(potential_dependencies),
            "recommended_patterns": self.get_recommended_patterns_for_new_app(),
            "integration_complexity": "low" if len(similar_apps) > 0 else "medium"
        }


class InfrastructureContext(BaseAgentModel):
    """Infrastructure context for code generation."""
    
    project_context: ProjectContext = Field(
        description="Project-level context information"
    )
    
    target_app_type: AppType = Field(
        description="Type of app being generated"
    )
    
    integration_targets: List[str] = Field(
        default_factory=list,
        description="Apps to integrate with"
    )
    
    # Generation constraints
    must_follow_patterns: List[str] = Field(
        default_factory=list,
        description="Patterns that must be followed"
    )
    
    avoid_patterns: List[str] = Field(
        default_factory=list,
        description="Patterns to avoid"
    )
    
    # Quality requirements
    minimum_quality_score: float = Field(
        ge=0.0,
        le=10.0,
        default=8.0,
        description="Minimum required quality score"
    )
    
    require_type_safety: bool = Field(
        default=True,
        description="Whether type safety is required"
    )
    
    require_tests: bool = Field(
        default=True,
        description="Whether tests are required"
    )
    
    # Infrastructure preferences
    preferred_async_style: str = Field(
        default="async_await",
        description="Preferred async programming style"
    )
    
    database_preferences: List[str] = Field(
        default_factory=list,
        description="Database-related preferences"
    )
    
    @computed_field
    @property
    def effective_patterns(self) -> List[str]:
        """Get effective patterns after applying constraints."""
        # Start with project patterns
        base_patterns = self.project_context.get_recommended_patterns_for_new_app()
        
        # Add must-follow patterns
        effective = list(set(base_patterns + self.must_follow_patterns))
        
        # Remove avoided patterns
        effective = [p for p in effective if p not in self.avoid_patterns]
        
        return effective
    
    @computed_field
    @property
    def integration_complexity(self) -> str:
        """Assess integration complexity."""
        if not self.integration_targets:
            return "none"
        
        if len(self.integration_targets) == 1:
            return "simple"
        elif len(self.integration_targets) <= 3:
            return "moderate"
        else:
            return "complex"
    
    def get_integration_requirements(self) -> Dict[str, Any]:
        """Get specific integration requirements."""
        requirements = {
            "imports_needed": [],
            "model_relationships": [],
            "service_dependencies": [],
            "url_integrations": []
        }
        
        for target_app_name in self.integration_targets:
            target_app = self.project_context.get_app_by_name(target_app_name)
            if target_app:
                if target_app.has_models:
                    requirements["imports_needed"].append(f"{target_app_name}.models")
                
                if target_app.has_services:
                    requirements["service_dependencies"].append(f"{target_app_name}.services")
                
                # Check for user model integration
                if "user" in target_app_name.lower():
                    requirements["model_relationships"].append("User foreign key relationships")
        
        return requirements
