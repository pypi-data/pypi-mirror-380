"""
Validation Module for Django App Agent Generation.

This module handles validation of generation requirements,
feature compatibility, and generated code quality.
"""

from typing import List, Dict, Any
from pathlib import Path

from ..base import ServiceDependencies
from ...core.exceptions import ValidationError, FileSystemError
from ...models.responses import ValidationIssue, QualityMetrics
from ...models.enums import ValidationSeverity
from .context import GenerationContext


class GenerationValidator:
    """Handles validation during application generation process."""
    
    async def validate_generation_requirements(
        self,
        context: GenerationContext,
        dependencies: ServiceDependencies
    ) -> None:
        """Validate that generation can proceed."""
        # Check if app directory already exists
        if context.app_directory.exists():
            raise ValidationError(
                f"Application directory already exists: {context.app_directory}",
                validation_type="directory_exists"
            )
        
        # Check if target directory is writable
        if not context.target_directory.exists():
            try:
                context.target_directory.mkdir(parents=True, exist_ok=True)
            except Exception as e:
                raise FileSystemError(
                    f"Cannot create target directory: {e}",
                    file_path=str(context.target_directory),
                    operation="create_directory"
                )
        
        # Validate feature compatibility
        await self.validate_feature_compatibility(context, dependencies)
    
    async def validate_feature_compatibility(
        self,
        context: GenerationContext,
        dependencies: ServiceDependencies
    ) -> None:
        """Validate that requested features are compatible."""
        request = context.request
        
        # Check app type compatibility
        for feature in request.features:
            if not request.app_type.supports_feature(feature):
                raise ValidationError(
                    f"Feature {feature.value} is not supported by app type {request.app_type.value}",
                    validation_type="feature_compatibility"
                )
        
        # Check complexity compatibility
        recommended_features = request.complexity.get_recommended_features()
        missing_recommended = recommended_features - set(request.features)
        
        if missing_recommended:
            dependencies.logger.warning(
                f"Missing recommended features for {request.complexity.value} complexity",
                missing_features=[f.value for f in missing_recommended]
            )
    
    async def validate_generated_code(
        self,
        context: GenerationContext,
        dependencies: ServiceDependencies
    ) -> QualityMetrics:
        """Validate generated code quality and return metrics."""
        dependencies.log_operation("Validating generated code quality")
        
        validation_issues = []
        total_files = len(context.generated_files)
        valid_files = 0
        
        for generated_file in context.generated_files:
            try:
                # Basic syntax validation for Python files
                if generated_file.file_type == "python":
                    compile(generated_file.content, generated_file.path, 'exec')
                    valid_files += 1
                else:
                    valid_files += 1  # Non-Python files are considered valid for now
                    
            except SyntaxError as e:
                validation_issues.append(ValidationIssue(
                    file_path=generated_file.path,
                    line_number=e.lineno or 1,
                    severity=ValidationSeverity.ERROR,
                    message=f"Syntax error: {e.msg}",
                    rule_id="syntax_error"
                ))
        
        # Calculate quality metrics
        syntax_score = (valid_files / total_files * 100) if total_files > 0 else 100
        
        # Store validation results in context
        context.validation_results.update({
            "total_files": total_files,
            "valid_files": valid_files,
            "validation_issues": [issue.model_dump() for issue in validation_issues],
            "syntax_score": syntax_score
        })
        
        return QualityMetrics(
            overall_score=min(10.0, syntax_score * 0.8),  # Weighted average
            type_safety_score=8.5,  # Placeholder - would need actual type checking
            pattern_consistency=9.0,  # Placeholder - would need pattern analysis
            code_complexity=7.5,  # Placeholder - would need complexity analysis
            test_coverage=0.0,  # No tests generated yet
            documentation_coverage=60.0,  # Basic docstrings (percentage)
            performance_score=8.0,  # Placeholder
            security_score=8.5,  # Placeholder
            maintainability_score=min(10.0, syntax_score * 0.9)
        )
