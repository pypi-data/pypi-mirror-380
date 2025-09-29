"""
Response models for Django App Agent Module.

This module defines all response models with:
- Complete result structures
- Quality metrics and validation
- File generation results
- Error handling information
"""

from typing import List, Optional, Dict, Any, Set
from pathlib import Path
from datetime import datetime, timezone
from pydantic import Field, field_validator, computed_field

from .base import BaseAgentModel, TimestampedModel, MetricsModel, ErrorModel, ValidationMixin
from .enums import GenerationStage, ValidationSeverity, FileType, AppFeature
from .requests import ContextualQuestion, QuestionResponse


class QualityMetrics(MetricsModel):
    """Quality metrics for generated code."""
    
    overall_score: float = Field(
        ge=0.0,
        le=10.0,
        description="Overall quality score (0-10)"
    )
    
    type_safety_score: float = Field(
        ge=0.0,
        le=10.0,
        description="Type safety score (0-10)"
    )
    
    pattern_consistency: float = Field(
        ge=0.0,
        le=10.0,
        description="Architectural pattern consistency score (0-10)"
    )
    
    code_complexity: float = Field(
        ge=0.0,
        le=10.0,
        description="Code complexity score (lower is better, 0-10)"
    )
    
    test_coverage: float = Field(
        ge=0.0,
        le=100.0,
        description="Test coverage percentage (0-100)"
    )
    
    documentation_coverage: float = Field(
        ge=0.0,
        le=100.0,
        description="Documentation coverage percentage (0-100)"
    )
    
    performance_score: float = Field(
        ge=0.0,
        le=10.0,
        description="Performance optimization score (0-10)"
    )
    
    security_score: float = Field(
        ge=0.0,
        le=10.0,
        description="Security best practices score (0-10)"
    )
    
    maintainability_score: float = Field(
        ge=0.0,
        le=10.0,
        description="Code maintainability score (0-10)"
    )
    
    @computed_field
    @property
    def is_production_ready(self) -> bool:
        """Check if quality metrics indicate production readiness."""
        return (
            self.overall_score >= 8.0 and
            self.type_safety_score >= 9.0 and
            self.security_score >= 8.0 and
            self.test_coverage >= 80.0
        )
    
    @computed_field
    @property
    def quality_grade(self) -> str:
        """Get letter grade for overall quality."""
        if self.overall_score >= 9.0:
            return "A"
        elif self.overall_score >= 8.0:
            return "B"
        elif self.overall_score >= 7.0:
            return "C"
        elif self.overall_score >= 6.0:
            return "D"
        else:
            return "F"
    
    def get_improvement_areas(self) -> List[str]:
        """Get list of areas that need improvement."""
        areas = []
        
        if self.type_safety_score < 9.0:
            areas.append("Type safety needs improvement")
        
        if self.pattern_consistency < 8.0:
            areas.append("Architectural pattern consistency")
        
        if self.test_coverage < 80.0:
            areas.append("Test coverage is insufficient")
        
        if self.security_score < 8.0:
            areas.append("Security best practices")
        
        if self.performance_score < 7.0:
            areas.append("Performance optimization")
        
        if self.documentation_coverage < 70.0:
            areas.append("Documentation coverage")
        
        return areas


class ValidationIssue(BaseAgentModel):
    """A validation issue found in generated code."""
    
    severity: ValidationSeverity = Field(
        description="Severity level of the issue"
    )
    
    message: str = Field(
        description="Human-readable description of the issue",
        min_length=1,
        max_length=500
    )
    
    file_path: Optional[str] = Field(
        default=None,
        description="File path where the issue was found"
    )
    
    line_number: Optional[int] = Field(
        default=None,
        ge=1,
        description="Line number where the issue occurs"
    )
    
    rule_id: Optional[str] = Field(
        default=None,
        description="ID of the validation rule that was violated"
    )
    
    suggestion: Optional[str] = Field(
        default=None,
        max_length=500,
        description="Suggested fix for the issue"
    )
    
    auto_fixable: bool = Field(
        default=False,
        description="Whether this issue can be automatically fixed"
    )
    
    @computed_field
    @property
    def is_blocking(self) -> bool:
        """Check if this issue blocks generation."""
        return self.severity.is_blocking()


class GeneratedFile(BaseAgentModel):
    """Information about a generated file."""
    
    relative_path: str = Field(
        description="Relative path of the file within the app"
    )
    
    absolute_path: Path = Field(
        description="Absolute path where the file will be created"
    )
    
    content: str = Field(
        description="Generated file content"
    )
    
    line_count: int = Field(
        ge=0,
        description="Number of lines in the file"
    )
    
    file_type: FileType = Field(
        description="Type of the generated file"
    )
    
    type_safety_score: float = Field(
        ge=0.0,
        le=10.0,
        description="Type safety score for this file"
    )
    
    complexity_score: float = Field(
        ge=0.0,
        le=10.0,
        description="Complexity score for this file"
    )
    
    patterns_used: List[str] = Field(
        default_factory=list,
        description="Architectural patterns used in this file"
    )
    
    description: str = Field(
        description="Human-readable description of the file's purpose"
    )
    
    follows_conventions: bool = Field(
        default=True,
        description="Whether the file follows coding conventions"
    )
    
    imports: List[str] = Field(
        default_factory=list,
        description="List of imports used in the file"
    )
    
    exports: List[str] = Field(
        default_factory=list,
        description="List of classes/functions exported by the file"
    )
    
    dependencies: List[str] = Field(
        default_factory=list,
        description="External dependencies required by this file"
    )
    
    @field_validator('line_count', mode='before')
    @classmethod
    def calculate_line_count(cls, v: int, info) -> int:
        """Calculate line count from content if not provided."""
        if v == 0 and 'content' in info.data:
            return len(info.data['content'].splitlines())
        return v
    
    @computed_field
    @property
    def size_bytes(self) -> int:
        """Get file size in bytes."""
        return len(self.content.encode('utf-8'))
    
    @computed_field
    @property
    def is_large_file(self) -> bool:
        """Check if file exceeds size limits."""
        return self.line_count > 500  # Based on technical requirements
    
    def get_quality_summary(self) -> Dict[str, Any]:
        """Get quality summary for this file."""
        return {
            "type_safety_score": self.type_safety_score,
            "complexity_score": self.complexity_score,
            "follows_conventions": self.follows_conventions,
            "line_count": self.line_count,
            "patterns_count": len(self.patterns_used),
            "dependencies_count": len(self.dependencies)
        }


class AppGenerationResult(TimestampedModel):
    """Result of application generation process."""
    
    # Basic result information
    app_name: str = Field(description="Name of the generated application")
    generation_id: str = Field(description="Unique identifier for this generation")
    success: bool = Field(description="Whether generation completed successfully")
    
    # Timing information
    total_execution_time_seconds: float = Field(
        ge=0.0,
        description="Total time taken for generation in seconds"
    )
    
    # Generation statistics
    files_count: int = Field(
        ge=0,
        description="Number of files generated"
    )
    
    lines_of_code: int = Field(
        ge=0,
        description="Total lines of code generated"
    )
    
    # Quality metrics
    quality_score: float = Field(
        ge=0.0,
        le=10.0,
        description="Overall quality score"
    )
    
    type_safety_score: float = Field(
        ge=0.0,
        le=10.0,
        description="Type safety score"
    )
    
    pattern_consistency_score: float = Field(
        ge=0.0,
        le=10.0,
        description="Pattern consistency score"
    )
    
    test_coverage_percentage: float = Field(
        ge=0.0,
        le=100.0,
        description="Test coverage percentage"
    )
    
    # Integration information
    integration_successful: bool = Field(
        description="Whether integration with existing project was successful"
    )
    
    # Generated content
    generated_files: List[GeneratedFile] = Field(
        default_factory=list,
        description="List of generated files"
    )
    
    patterns_followed: List[str] = Field(
        default_factory=list,
        description="Architectural patterns that were followed"
    )
    
    dependencies_resolved: List[str] = Field(
        default_factory=list,
        description="Dependencies that were resolved and added"
    )
    
    # Issues and warnings
    errors: List[ValidationIssue] = Field(
        default_factory=list,
        description="Errors encountered during generation"
    )
    
    warnings: List[ValidationIssue] = Field(
        default_factory=list,
        description="Warnings from validation"
    )
    
    # Output paths
    report_directory: Path = Field(
        description="Directory containing generation reports"
    )
    
    generation_report_path: Path = Field(
        description="Path to the detailed generation report"
    )
    
    @computed_field
    @property
    def has_critical_errors(self) -> bool:
        """Check if there are any critical errors."""
        return any(error.severity == ValidationSeverity.CRITICAL for error in self.errors)
    
    @computed_field
    @property
    def blocking_issues_count(self) -> int:
        """Count of issues that block deployment."""
        return sum(1 for error in self.errors if error.is_blocking)
    
    @computed_field
    @property
    def quality_metrics(self) -> QualityMetrics:
        """Get comprehensive quality metrics."""
        return QualityMetrics(
            overall_score=self.quality_score,
            type_safety_score=self.type_safety_score,
            pattern_consistency=self.pattern_consistency_score,
            test_coverage=self.test_coverage_percentage,
            # Calculate other metrics from generated files
            code_complexity=self._calculate_average_complexity(),
            documentation_coverage=self._calculate_documentation_coverage(),
            performance_score=8.0,  # Default for now
            security_score=8.5,     # Default for now
            maintainability_score=self._calculate_maintainability_score()
        )
    
    def _calculate_average_complexity(self) -> float:
        """Calculate average complexity across all files."""
        if not self.generated_files:
            return 0.0
        
        total_complexity = sum(f.complexity_score for f in self.generated_files)
        return total_complexity / len(self.generated_files)
    
    def _calculate_documentation_coverage(self) -> float:
        """Calculate documentation coverage percentage."""
        if not self.generated_files:
            return 0.0
        
        # Simple heuristic: files with docstrings
        documented_files = sum(
            1 for f in self.generated_files
            if '"""' in f.content or "'''" in f.content
        )
        
        return (documented_files / len(self.generated_files)) * 100
    
    def _calculate_maintainability_score(self) -> float:
        """Calculate maintainability score."""
        if not self.generated_files:
            return 0.0
        
        # Factors: follows conventions, reasonable complexity, good patterns
        convention_score = sum(1 for f in self.generated_files if f.follows_conventions)
        convention_ratio = convention_score / len(self.generated_files)
        
        avg_complexity = self._calculate_average_complexity()
        complexity_score = max(0, 10 - avg_complexity)  # Lower complexity = higher score
        
        pattern_score = min(10, len(self.patterns_followed))
        
        return (convention_ratio * 4 + complexity_score * 3 + pattern_score * 3) / 10
    
    def get_files_by_type(self, file_type: FileType) -> List[GeneratedFile]:
        """Get all generated files of a specific type."""
        return [f for f in self.generated_files if f.file_type == file_type]
    
    def get_summary(self) -> Dict[str, Any]:
        """Get a summary of the generation result."""
        return {
            "app_name": self.app_name,
            "success": self.success,
            "execution_time_seconds": self.total_execution_time_seconds,
            "files_generated": self.files_count,
            "lines_of_code": self.lines_of_code,
            "quality_score": self.quality_score,
            "type_safety_score": self.type_safety_score,
            "test_coverage": self.test_coverage_percentage,
            "errors_count": len(self.errors),
            "warnings_count": len(self.warnings),
            "critical_errors": self.has_critical_errors,
            "patterns_used": len(self.patterns_followed),
            "dependencies_added": len(self.dependencies_resolved)
        }


class QuestioningResult(TimestampedModel):
    """Result of an intelligent questioning session."""
    
    session_id: str = Field(description="Unique session identifier")
    success: bool = Field(description="Whether questioning completed successfully")
    
    questions_asked: List[ContextualQuestion] = Field(
        default_factory=list,
        description="Questions that were asked"
    )
    
    responses_received: List[QuestionResponse] = Field(
        default_factory=list,
        description="Responses received from user"
    )
    
    session_duration_seconds: float = Field(
        ge=0.0,
        description="Duration of questioning session in seconds"
    )
    
    completion_percentage: float = Field(
        ge=0.0,
        le=100.0,
        description="Percentage of questions completed"
    )
    
    context_quality_score: float = Field(
        ge=0.0,
        le=10.0,
        description="Quality of context gathered (0-10)"
    )
    
    architectural_insights: List[str] = Field(
        default_factory=list,
        description="Key architectural insights discovered"
    )
    
    integration_requirements: List[str] = Field(
        default_factory=list,
        description="Integration requirements identified"
    )
    
    @computed_field
    @property
    def response_rate(self) -> float:
        """Calculate response rate (responses / questions)."""
        if not self.questions_asked:
            return 0.0
        return len(self.responses_received) / len(self.questions_asked)
    
    def get_unanswered_questions(self) -> List[ContextualQuestion]:
        """Get questions that were not answered."""
        answered_ids = {r.question_id for r in self.responses_received}
        return [q for q in self.questions_asked if q.id not in answered_ids]


class DiagnosticResult(TimestampedModel):
    """Result of diagnostic analysis."""
    
    analysis_id: str = Field(description="Unique analysis identifier")
    success: bool = Field(description="Whether diagnostic completed successfully")
    
    problems_identified: List[str] = Field(
        default_factory=list,
        description="Problems identified in the codebase"
    )
    
    root_causes: List[str] = Field(
        default_factory=list,
        description="Potential root causes of issues"
    )
    
    solution_suggestions: List[str] = Field(
        default_factory=list,
        description="Suggested solutions"
    )
    
    confidence_score: float = Field(
        ge=0.0,
        le=1.0,
        description="Confidence in the diagnostic results"
    )
    
    analysis_duration_seconds: float = Field(
        ge=0.0,
        description="Time taken for analysis in seconds"
    )
    
    files_analyzed: int = Field(
        ge=0,
        description="Number of files analyzed"
    )
    
    @computed_field
    @property
    def severity_level(self) -> str:
        """Get overall severity level of identified problems."""
        if len(self.problems_identified) >= 5:
            return "high"
        elif len(self.problems_identified) >= 2:
            return "medium"
        elif len(self.problems_identified) >= 1:
            return "low"
        else:
            return "none"


class TemplateResult(BaseAgentModel):
    """Result of template rendering operation."""
    
    rendered_content: str = Field(
        description="The rendered template content"
    )
    
    template_name: str = Field(
        description="Name of the template that was rendered"
    )
    
    variables_used: List[str] = Field(
        default_factory=list,
        description="List of variables that were used in rendering"
    )
    
    missing_variables: List[str] = Field(
        default_factory=list,
        description="List of variables that were referenced but not provided"
    )
    
    template_metadata: Dict[str, Any] = Field(
        default_factory=dict,
        description="Metadata about the template rendering process"
    )
