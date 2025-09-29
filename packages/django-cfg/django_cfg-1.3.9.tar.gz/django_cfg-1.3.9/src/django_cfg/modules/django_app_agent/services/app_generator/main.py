"""
Main Application Generator Service for Django App Agent Module.

This service orchestrates the complete application generation process,
coordinating validation, structure creation, AI generation, and quality validation.
"""

from typing import Dict, Any
from pathlib import Path
from datetime import datetime, timezone
import uuid

from ..base import BaseService, ServiceDependencies
from ...models.requests import AppGenerationRequest
from ...models.responses import AppGenerationResult, QualityMetrics, ValidationIssue
from ...models.enums import ValidationSeverity
from ...core.config import AgentConfig

from .context import GenerationContext
from .validation import GenerationValidator
from .structure import StructureGenerator
from .ai_integration import AIGenerationManager


class AppGeneratorService(BaseService[AppGenerationRequest, AppGenerationResult]):
    """
    Main service for generating Django applications with AI assistance.
    
    This service coordinates the entire generation process:
    1. Validation of requirements and compatibility
    2. Basic structure creation
    3. AI-powered code generation
    4. Quality validation and metrics calculation
    """
    
    def __init__(self, config: AgentConfig):
        """Initialize the application generator service."""
        super().__init__("app_generator", config)
        self.config = config
        
        # Initialize sub-components
        self.validator = GenerationValidator()
        self.structure_generator = StructureGenerator()
        self.ai_manager = AIGenerationManager(config)
    
    async def process(
        self, 
        request: AppGenerationRequest, 
        dependencies: ServiceDependencies
    ) -> AppGenerationResult:
        """
        Process application generation request.
        
        Args:
            request: Application generation request
            dependencies: Service dependencies for logging and operations
            
        Returns:
            AppGenerationResult with generation details and metrics
        """
        start_time = datetime.now(timezone.utc)
        generation_id = str(uuid.uuid4())
        
        try:
            dependencies.log_operation(
                f"Starting application generation for '{request.app_name}'",
                app_name=request.app_name,
                app_type=request.app_type.value,
                features=[f.value for f in request.features]
            )
            
            # Create generation context
            context = await self._create_generation_context(request, dependencies)
            
            # Validate generation requirements
            await self.validator.validate_generation_requirements(context, dependencies)
            
            # Generate basic app structure
            await self.structure_generator.generate_app_structure(context, dependencies)
            
            # Generate feature files using templates (fallback)
            await self.structure_generator.generate_feature_files(context, dependencies)
            
            # Run AI agents for intelligent code generation
            await self.ai_manager.run_ai_generation(context, dependencies)
            
            # Validate generated code
            quality_metrics = await self.validator.validate_generated_code(context, dependencies)
            
            # Calculate execution time
            end_time = datetime.now(timezone.utc)
            execution_time = (end_time - start_time).total_seconds()
            
            # Extract AI dialogue for reporting
            ai_dialogue = self._extract_ai_dialogue(context)
            
            # Create successful result
            return AppGenerationResult(
                app_name=request.app_name,
                generation_id=generation_id,
                success=True,
                total_execution_time_seconds=execution_time,
                files_count=len(context.generated_files),
                lines_of_code=sum(len(f.content.splitlines()) for f in context.generated_files),
                quality_score=quality_metrics.overall_score,
                type_safety_score=quality_metrics.type_safety_score,
                pattern_consistency_score=quality_metrics.pattern_consistency,
                test_coverage_percentage=quality_metrics.test_coverage,
                integration_successful=True,
                generated_files=context.generated_files,
                patterns_followed=["django_best_practices", "pep8", "type_hints"],
                dependencies_resolved=["django", "django_cfg"],
                errors=[],
                warnings=[],
                report_directory=context.target_directory / request.app_name / "@report",
                generation_report_path=context.target_directory / request.app_name / "@report" / "generation_report.md"
            )
            
        except Exception as e:
            # Calculate execution time even on failure
            end_time = datetime.now(timezone.utc)
            execution_time = (end_time - start_time).total_seconds()
            
            # Create error result
            error_message = str(e)
            if len(error_message) > 500:
                error_message = error_message[:497] + "..."
            
            error_issue = ValidationIssue(
                file_path="generation_process",
                line_number=1,
                severity=ValidationSeverity.ERROR,
                message=error_message,
                rule_id="generation_error"
            )
            
            return AppGenerationResult(
                app_name=request.app_name if 'request' in locals() else "unknown",
                generation_id=generation_id,
                success=False,
                total_execution_time_seconds=execution_time,
                files_count=0,
                lines_of_code=0,
                quality_score=0.0,
                type_safety_score=0.0,
                pattern_consistency_score=0.0,
                test_coverage_percentage=0.0,
                integration_successful=False,
                generated_files=[],
                patterns_followed=[],
                dependencies_resolved=[],
                errors=[error_issue],
                warnings=[],
                report_directory=Path("/tmp"),
                generation_report_path=Path("/tmp/error.md")
            )
    
    async def _create_generation_context(
        self,
        request: AppGenerationRequest,
        dependencies: ServiceDependencies
    ) -> GenerationContext:
        """Create generation context from request."""
        # Determine target directory
        if request.output_directory:
            target_directory = Path(request.output_directory)
        else:
            target_directory = Path.cwd() / "apps"
        
        # Create template variables
        template_variables = {
            "app_name": request.app_name,
            "description": request.description,
            "app_type": request.app_type.value,
            "complexity": request.complexity.value,
            "features": [f.value for f in request.features],
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
        
        return GenerationContext(
            request=request,
            target_directory=target_directory,
            template_variables=template_variables
        )
    
    def _extract_ai_dialogue(self, context: GenerationContext) -> list[Dict[str, Any]]:
        """Extract AI dialogue from generation context."""
        dialogue = []
        
        # Extract from agent outputs
        generation_output = context.agent_outputs.get("generation", {})
        if generation_output:
            dialogue.append({
                "agent": "generation_agent",
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "message": generation_output.get("message", ""),
                "status": generation_output.get("status", "unknown"),
                "files_generated": generation_output.get("ai_files_count", 0),
                "recommendations": generation_output.get("recommendations", [])
            })
        
        return dialogue
