"""
Main Validation Service for Django App Agent Module.

This service orchestrates comprehensive code validation including
syntax, Django best practices, security, and quality analysis.
"""

from typing import List, Dict, Any, Optional
import asyncio

from pydantic import BaseModel, Field

from ...core.config import AgentConfig
from ...models.responses import GeneratedFile, QualityMetrics
from ..base import BaseService, ServiceDependencies
from .models import ValidationRequest, ValidationResult, ValidationIssue
from .syntax_validator import SyntaxValidator
from .django_validator import DjangoValidator
from .security_validator import SecurityValidator
from .quality_validator import QualityValidator


class ValidationService(BaseService[ValidationRequest, ValidationResult]):
    """
    Comprehensive code validation and quality analysis service.
    
    Provides validation for:
    - Python syntax and AST analysis
    - Django best practices and conventions
    - Security vulnerabilities and patterns
    - Code quality metrics and standards
    - Performance considerations
    - Type hint completeness
    """
    
    def __init__(self, config: AgentConfig):
        """Initialize validation service."""
        super().__init__("validation", config)
        self.config = config
        
        # Initialize validators
        self.syntax_validator = SyntaxValidator()
        self.django_validator = DjangoValidator()
        self.security_validator = SecurityValidator()
        self.quality_validator = QualityValidator()
    
    async def process(
        self,
        request: ValidationRequest,
        dependencies: ServiceDependencies
    ) -> ValidationResult:
        """
        Process comprehensive code validation.
        
        Args:
            request: Validation request with files and rules
            dependencies: Service dependencies
            
        Returns:
            ValidationResult with issues and quality metrics
        """
        dependencies.log_operation(
            "Starting code validation",
            files_count=len(request.files),
            validation_rules=request.validation_rules,
            strict_mode=request.strict_mode
        )
        
        all_issues = []
        
        try:
            # Validate each file
            for file in request.files:
                file_issues = await self._validate_file(file, request, dependencies)
                all_issues.extend(file_issues)
            
            # Calculate quality metrics
            quality_metrics = await self.quality_validator.calculate_quality_metrics(
                request.files, dependencies
            )
            
            # Determine if validation passed
            error_count = len([issue for issue in all_issues if issue.severity == "error"])
            is_valid = error_count == 0 or not request.strict_mode
            
            # Create summary
            summary = self._create_validation_summary(all_issues, quality_metrics)
            
            result = ValidationResult(
                is_valid=is_valid,
                quality_metrics=quality_metrics,
                issues=all_issues,
                summary=summary
            )
            
            dependencies.log_operation(
                "Validation completed",
                is_valid=is_valid,
                total_issues=len(all_issues),
                error_count=error_count,
                warning_count=result.warning_count,
                info_count=result.info_count,
                overall_quality_score=quality_metrics.overall_score
            )
            
            return result
            
        except Exception as e:
            dependencies.log_error("Validation process failed", e)
            raise
    
    async def _validate_file(
        self,
        file: GeneratedFile,
        request: ValidationRequest,
        dependencies: ServiceDependencies
    ) -> List[ValidationIssue]:
        """Validate a single file with all applicable validators."""
        issues = []
        
        dependencies.log_operation(f"Validating file: {file.path}")
        
        # Run validators based on requested rules
        validation_tasks = []
        
        if "syntax" in request.validation_rules:
            validation_tasks.append(
                self.syntax_validator.validate_syntax(file, dependencies)
            )
        
        if "django_best_practices" in request.validation_rules:
            validation_tasks.append(
                self.django_validator.validate_django_practices(file, dependencies)
            )
        
        if "security" in request.validation_rules:
            validation_tasks.append(
                self.security_validator.validate_security(file, dependencies)
            )
        
        if "quality" in request.validation_rules:
            validation_tasks.append(
                self.quality_validator.validate_quality(file, dependencies)
            )
        
        # Run all validations concurrently
        if validation_tasks:
            validation_results = await asyncio.gather(*validation_tasks, return_exceptions=True)
            
            for result in validation_results:
                if isinstance(result, Exception):
                    dependencies.log_error(f"Validator failed for {file.path}", result)
                    issues.append(ValidationIssue(
                        severity="error",
                        category="validation",
                        message=f"Validation failed: {result}",
                        file_path=file.path,
                        line_number=1,
                        rule_id="validation_error"
                    ))
                else:
                    issues.extend(result)
        
        return issues
    
    def _create_validation_summary(
        self,
        issues: List[ValidationIssue],
        quality_metrics: QualityMetrics
    ) -> Dict[str, Any]:
        """Create validation summary statistics."""
        # Group issues by category and severity
        by_category = {}
        by_severity = {"error": 0, "warning": 0, "info": 0}
        
        for issue in issues:
            # Count by category
            if issue.category not in by_category:
                by_category[issue.category] = 0
            by_category[issue.category] += 1
            
            # Count by severity
            if issue.severity in by_severity:
                by_severity[issue.severity] += 1
        
        # Calculate pass rates
        total_checks = len(issues) if issues else 1
        error_rate = by_severity["error"] / total_checks * 100
        warning_rate = by_severity["warning"] / total_checks * 100
        
        return {
            "total_issues": len(issues),
            "issues_by_severity": by_severity,
            "issues_by_category": by_category,
            "error_rate_percentage": error_rate,
            "warning_rate_percentage": warning_rate,
            "quality_score": quality_metrics.overall_score,
            "type_safety_score": quality_metrics.type_safety_score,
            "documentation_coverage": quality_metrics.documentation_coverage,
            "maintainability_score": quality_metrics.maintainability_score,
            "recommendations": self._generate_recommendations(issues, quality_metrics)
        }
    
    def _generate_recommendations(
        self,
        issues: List[ValidationIssue],
        quality_metrics: QualityMetrics
    ) -> List[str]:
        """Generate actionable recommendations based on validation results."""
        recommendations = []
        
        # Analyze issue patterns
        error_count = len([i for i in issues if i.severity == "error"])
        warning_count = len([i for i in issues if i.severity == "warning"])
        
        if error_count > 0:
            recommendations.append(f"Fix {error_count} critical error(s) before deployment")
        
        if warning_count > 5:
            recommendations.append(f"Address {warning_count} warning(s) to improve code quality")
        
        # Quality-based recommendations
        if quality_metrics.type_safety_score < 7.0:
            recommendations.append("Add type hints to improve type safety")
        
        if quality_metrics.documentation_coverage < 6.0:
            recommendations.append("Add docstrings to classes and functions")
        
        if quality_metrics.code_complexity > 7.0:
            recommendations.append("Reduce code complexity by breaking down large functions")
        
        # Security recommendations
        security_issues = [i for i in issues if i.category == "security"]
        if security_issues:
            recommendations.append("Review and address security-related issues")
        
        # Django-specific recommendations
        django_issues = [i for i in issues if i.category == "django"]
        if len(django_issues) > 3:
            recommendations.append("Follow Django best practices more consistently")
        
        return recommendations[:5]  # Limit to top 5 recommendations
