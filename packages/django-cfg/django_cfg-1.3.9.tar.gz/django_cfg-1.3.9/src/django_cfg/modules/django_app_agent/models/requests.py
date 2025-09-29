"""
Request models for Django App Agent Module.

This module defines all request models with:
- Complete Pydantic 2 validation
- Type-safe field definitions
- Business logic validation
- Clear documentation
"""

from typing import List, Optional, Dict, Any, Set
from pathlib import Path
from pydantic import Field, field_validator, model_validator

from .base import BaseAgentModel, ValidationMixin
from .enums import AppFeature, AppComplexity, AppType, QuestionType, ImpactLevel
from ..utils.validation import validate_app_name, validate_description


class AppGenerationRequest(BaseAgentModel, ValidationMixin):
    """Request for generating a Django application."""
    
    # Core application details
    app_name: str = Field(
        description="Name of the Django application to generate",
        min_length=2,
        max_length=50,
        pattern=r'^[a-z][a-z0-9_]*$'
    )
    
    description: str = Field(
        description="Detailed description of the application purpose and functionality",
        min_length=10,
        max_length=500
    )
    
    # Application configuration
    app_type: AppType = Field(
        default=AppType.DJANGO_CFG,
        description="Type of Django application to generate"
    )
    
    features: List[AppFeature] = Field(
        default_factory=list,
        description="List of features to include in the generated application"
    )
    
    complexity: AppComplexity = Field(
        default=AppComplexity.MODERATE,
        description="Complexity level of the application"
    )
    
    # Generation options
    enable_questioning: bool = Field(
        default=True,
        description="Whether to enable intelligent questioning system"
    )
    
    max_questions: int = Field(
        default=20,
        ge=0,
        le=50,
        description="Maximum number of questions to ask during generation"
    )
    
    questioning_timeout_minutes: int = Field(
        default=15,
        ge=1,
        le=60,
        description="Timeout for questioning session in minutes"
    )
    
    # Quality requirements
    quality_threshold: float = Field(
        default=8.0,
        ge=0.0,
        le=10.0,
        description="Minimum quality score required for generated code"
    )
    
    # Integration options
    target_apps: List[str] = Field(
        default_factory=list,
        description="Existing apps to analyze for integration patterns"
    )
    
    exclude_patterns: List[str] = Field(
        default_factory=list,
        description="Patterns to exclude from generation"
    )
    
    # Output configuration
    output_directory: Optional[Path] = Field(
        default=None,
        description="Custom output directory for generated files"
    )
    
    # Advanced options
    custom_requirements: Dict[str, Any] = Field(
        default_factory=dict,
        description="Custom requirements and constraints"
    )
    
    # UI options
    rich_interface: bool = Field(
        default=True,
        description="Enable Rich CLI interface with progress bars"
    )
    
    verbose_output: bool = Field(
        default=False,
        description="Enable verbose output during generation"
    )
    
    @field_validator('app_name')
    @classmethod
    def validate_app_name_field(cls, v: str) -> str:
        """Validate application name using utility function."""
        return validate_app_name(v, check_reserved=True)
    
    @field_validator('description')
    @classmethod
    def validate_description_field(cls, v: str) -> str:
        """Validate application description."""
        return validate_description(v, min_length=10, max_length=500)
    
    @field_validator('features')
    @classmethod
    def validate_features_list(cls, v: List[AppFeature]) -> List[AppFeature]:
        """Validate and deduplicate features list."""
        if not v:
            return []
        
        # Convert strings to enums if needed
        enum_features = []
        for feature in v:
            if isinstance(feature, str):
                enum_features.append(AppFeature(feature))
            else:
                enum_features.append(feature)
        
        # Remove duplicates while preserving order
        seen = set()
        unique_features = []
        for feature in enum_features:
            if feature not in seen:
                seen.add(feature)
                unique_features.append(feature)
        
        return unique_features
    
    @field_validator('complexity')
    @classmethod
    def validate_complexity_enum(cls, v) -> AppComplexity:
        """Ensure complexity is proper enum."""
        if isinstance(v, str):
            return AppComplexity(v)
        return v
    
    @field_validator('app_type')
    @classmethod
    def validate_app_type_enum(cls, v) -> AppType:
        """Ensure app_type is proper enum."""
        if isinstance(v, str):
            return AppType(v)
        return v
    
    @field_validator('target_apps')
    @classmethod
    def validate_target_apps(cls, v: List[str]) -> List[str]:
        """Validate target apps list."""
        if not v:
            return []
        
        validated_apps = []
        for app_name in v:
            try:
                validated_name = validate_app_name(app_name, check_reserved=False)
                validated_apps.append(validated_name)
            except Exception:
                # Skip invalid app names
                continue
        
        return validated_apps
    
    @model_validator(mode='after')
    def validate_consistency(self) -> 'AppGenerationRequest':
        """Validate consistency between fields."""
        # Note: Pydantic 2 handles enum conversion automatically, 
        # so we don't need to manually convert them here
        
        # Auto-populate features based on complexity if not specified
        if not self.features:
            self.features = list(self.complexity.get_recommended_features())
        
        # Validate feature dependencies
        all_features = set(self.features)
        for feature in self.features:
            dependencies = feature.get_dependencies()
            missing_deps = dependencies - all_features
            if missing_deps:
                # Add missing dependencies
                self.features.extend(list(missing_deps))
        
        # Adjust max_questions based on complexity
        if self.max_questions > self.complexity.get_max_questions():
            self.max_questions = self.complexity.get_max_questions()
        
        # Validate app type supports all requested features
        unsupported_features = []
        for feature in self.features:
            if not self.app_type.supports_feature(feature):
                unsupported_features.append(feature)
        
        if unsupported_features:
            raise ValueError(
                f"App type {self.app_type} does not support features: {unsupported_features}"
            )
        
        return self
    
    def get_estimated_time_minutes(self) -> int:
        """Get estimated generation time in minutes."""
        base_time = self.complexity.get_estimated_time_minutes()
        
        # Add time for additional features
        feature_multiplier = len(self.features) / len(self.complexity.get_recommended_features())
        adjusted_time = int(base_time * max(1.0, feature_multiplier))
        
        # Add questioning time if enabled
        if self.enable_questioning:
            adjusted_time += min(self.questioning_timeout_minutes, 10)
        
        return adjusted_time
    
    def get_feature_set(self) -> Set[AppFeature]:
        """Get set of features for easy lookup."""
        return set(self.features)
    
    def has_feature(self, feature: AppFeature) -> bool:
        """Check if a specific feature is requested."""
        return feature in self.get_feature_set()


class QuestioningRequest(BaseAgentModel):
    """Request for conducting an intelligent questioning session."""
    
    user_intent: str = Field(
        description="User's stated intent or goal for the application",
        min_length=5,
        max_length=200
    )
    
    project_path: Path = Field(
        description="Path to the Django project for context analysis"
    )
    
    app_generation_request: AppGenerationRequest = Field(
        description="Associated app generation request"
    )
    
    max_questions: int = Field(
        default=20,
        ge=1,
        le=50,
        description="Maximum number of questions to ask"
    )
    
    timeout_minutes: int = Field(
        default=15,
        ge=1,
        le=60,
        description="Maximum time for questioning session"
    )
    
    focus_areas: List[str] = Field(
        default_factory=list,
        description="Specific areas to focus questions on"
    )
    
    skip_basic_questions: bool = Field(
        default=False,
        description="Skip basic questions and focus on advanced topics"
    )
    
    @field_validator('project_path')
    @classmethod
    def validate_project_path(cls, v: Path) -> Path:
        """Validate that project path exists and is a directory."""
        from ..utils.validation import validate_file_path
        
        return validate_file_path(
            v,
            must_exist=True,
            must_be_dir=True
        )


class DiagnosticRequest(BaseAgentModel):
    """Request for diagnosing problems in Django applications."""
    
    project_path: Path = Field(
        description="Path to the Django project to diagnose"
    )
    
    app_name: Optional[str] = Field(
        default=None,
        description="Specific app to focus diagnosis on"
    )
    
    problem_description: str = Field(
        description="Description of the problem or issue",
        min_length=10,
        max_length=1000
    )
    
    error_messages: List[str] = Field(
        default_factory=list,
        description="Any error messages encountered"
    )
    
    symptoms: List[str] = Field(
        default_factory=list,
        description="Observed symptoms of the problem"
    )
    
    recent_changes: List[str] = Field(
        default_factory=list,
        description="Recent changes that might be related"
    )
    
    urgency_level: ImpactLevel = Field(
        default=ImpactLevel.MEDIUM,
        description="Urgency level of the problem"
    )
    
    include_suggestions: bool = Field(
        default=True,
        description="Whether to include solution suggestions"
    )
    
    max_suggestions: int = Field(
        default=5,
        ge=1,
        le=20,
        description="Maximum number of solution suggestions"
    )
    
    @field_validator('project_path')
    @classmethod
    def validate_project_path(cls, v: Path) -> Path:
        """Validate that project path exists."""
        from ..utils.validation import validate_file_path
        
        return validate_file_path(
            v,
            must_exist=True,
            must_be_dir=True
        )
    
    @field_validator('app_name')
    @classmethod
    def validate_app_name_field(cls, v: Optional[str]) -> Optional[str]:
        """Validate app name if provided."""
        if v is None:
            return v
        
        return validate_app_name(v, check_reserved=False)
    
    @field_validator('problem_description')
    @classmethod
    def validate_problem_description(cls, v: str) -> str:
        """Validate problem description."""
        return validate_description(v, min_length=10, max_length=1000)


class ContextualQuestion(BaseAgentModel):
    """A contextual question generated by the intelligent questioning system."""
    
    id: str = Field(description="Unique question identifier")
    
    text: str = Field(
        description="The question text to display to the user",
        min_length=10,
        max_length=500
    )
    
    question_type: QuestionType = Field(
        description="Type of question (yes/no, multiple choice, etc.)"
    )
    
    impact_level: ImpactLevel = Field(
        description="Impact level of this question on the final result"
    )
    
    context_evidence: List[str] = Field(
        default_factory=list,
        description="Evidence from codebase that prompted this question"
    )
    
    options: Optional[List[str]] = Field(
        default=None,
        description="Available options for multiple choice questions"
    )
    
    default_answer: Optional[str] = Field(
        default=None,
        description="Default answer if user skips"
    )
    
    architectural_implications: List[str] = Field(
        default_factory=list,
        description="How the answer affects architectural decisions"
    )
    
    @field_validator('question_type')
    @classmethod
    def validate_question_type_enum(cls, v) -> QuestionType:
        """Ensure question_type is proper enum."""
        if isinstance(v, str):
            return QuestionType(v)
        return v
    
    @field_validator('impact_level')
    @classmethod
    def validate_impact_level_enum(cls, v) -> ImpactLevel:
        """Ensure impact_level is proper enum."""
        if isinstance(v, str):
            return ImpactLevel(v)
        return v
    
    @model_validator(mode='after')
    def validate_question_consistency(self) -> 'ContextualQuestion':
        """Validate question consistency."""
        # Note: Pydantic 2 handles enum conversion automatically
        
        # Questions requiring options must have them
        if self.question_type.requires_options() and not self.options:
            raise ValueError(f"Question type {self.question_type} requires options")
        
        # Validate default answer is in options if provided
        if self.default_answer and self.options:
            if self.default_answer not in self.options:
                raise ValueError("Default answer must be one of the provided options")
        
        return self


class QuestionResponse(BaseAgentModel):
    """Response to a contextual question."""
    
    question_id: str = Field(description="ID of the question being answered")
    
    answer: str = Field(
        description="User's answer to the question",
        min_length=1,
        max_length=1000
    )
    
    confidence: float = Field(
        default=1.0,
        ge=0.0,
        le=1.0,
        description="User's confidence in their answer (0-1)"
    )
    
    notes: Optional[str] = Field(
        default=None,
        max_length=500,
        description="Additional notes or context from user"
    )


class TemplateRequest(BaseAgentModel):
    """Request for template rendering."""
    
    template_name: str = Field(
        description="Name of the template to render",
        min_length=1,
        max_length=100
    )
    
    app_type: AppType = Field(
        description="Type of Django application"
    )
    
    features: List[AppFeature] = Field(
        default_factory=list,
        description="List of features to include in template"
    )
    
    variables: Dict[str, Any] = Field(
        default_factory=dict,
        description="Template variables for rendering"
    )
    
    custom_templates: Dict[str, str] = Field(
        default_factory=dict,
        description="Custom template overrides"
    )
