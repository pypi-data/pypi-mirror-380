"""
Main Context Builder Service for Django App Agent Module.

This service builds comprehensive development context for AI agents,
coordinating project analysis, pattern identification, and context optimization.
"""

from typing import Dict, Any, List

from ..base import BaseService, ServiceDependencies
from ..project_scanner import ProjectScannerService, ProjectScanRequest
from ...models.context import ProjectContext
from ...core.exceptions import ValidationError

from .models import ContextBuildRequest, ContextResult
from .pattern_analyzer import PatternAnalyzer
from .code_extractor import CodeExtractor
from .context_generator import ContextGenerator


class ContextBuilderService(BaseService[ContextBuildRequest, ContextResult]):
    """
    Service for building comprehensive development context for AI agents.
    
    Capabilities:
    - Project structure analysis and pattern identification
    - Code sample extraction and context building
    - Integration point identification
    - Context optimization for AI consumption
    """
    
    def __init__(self, config):
        """Initialize context builder service."""
        super().__init__("context_builder", config)
        
        # Initialize sub-components
        self.pattern_analyzer = PatternAnalyzer()
        self.code_extractor = CodeExtractor()
        self.context_generator = ContextGenerator()
        
        # Initialize project scanner
        self.project_scanner = ProjectScannerService(config)
    
    async def process(
        self, 
        request: ContextBuildRequest, 
        dependencies: ServiceDependencies
    ) -> ContextResult:
        """
        Process context building request.
        
        Args:
            request: Context building request
            dependencies: Service dependencies for logging and operations
            
        Returns:
            ContextResult with comprehensive development context
        """
        try:
            dependencies.log_operation(
                f"Building development context for '{request.project_root}'",
                project_root=str(request.project_root),
                target_app=request.target_app_name
            )
            
            # Initialize result
            result = ContextResult(
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
            scan_request = ProjectScanRequest(
                project_root=request.project_root,
                analyze_dependencies=True,
                detect_patterns=True
            )
            
            scan_result = await self.project_scanner.process(scan_request, dependencies)
            result.project_context = scan_result.project_context
            
            # Identify relevant architectural patterns
            await self.pattern_analyzer.identify_relevant_patterns(
                request, scan_result, result, dependencies
            )
            
            # Build generation-specific context
            await self.context_generator.build_generation_context(
                request, result, dependencies
            )
            
            # Extract code samples if requested
            if request.include_code_samples:
                await self.code_extractor.extract_code_samples(
                    request, result, dependencies
                )
            
            # Identify integration points
            await self._identify_integration_points(request, result, dependencies)
            
            # Generate recommendations
            await self._generate_recommendations(request, result, dependencies)
            
            # Optimize context size if needed
            await self._optimize_context_size(request, result, dependencies)
            
            dependencies.log_operation(
                "Context building completed successfully",
                patterns_found=len(result.relevant_patterns),
                code_samples=len(result.code_samples),
                recommendations=len(result.recommendations)
            )
            
            return result
            
        except Exception as e:
            raise ValidationError(
                f"Failed to build development context: {e}",
                validation_type="context_building"
            )
    
    async def _identify_integration_points(
        self,
        request: ContextBuildRequest,
        result: ContextResult,
        dependencies: ServiceDependencies
    ) -> None:
        """Identify potential integration points with existing code."""
        integration_points = []
        
        if not request.generation_request:
            return
        
        # Check for potential integrations based on requested features
        for feature in request.generation_request.features:
            feature_name = feature.value
            
            if feature_name == "models":
                # Look for existing models that could be related
                for app in result.project_context.apps:
                    if app.models_count > 0:
                        integration_points.append({
                            "type": "model_relationships",
                            "app": app.name,
                            "description": f"Consider relationships with models in {app.name}",
                            "confidence": 0.7
                        })
            
            elif feature_name == "api":
                # Look for existing API patterns
                api_apps = [app for app in result.project_context.apps if "api" in app.name.lower()]
                for app in api_apps:
                    integration_points.append({
                        "type": "api_integration",
                        "app": app.name,
                        "description": f"Consider API consistency with {app.name}",
                        "confidence": 0.8
                    })
            
            elif feature_name == "admin":
                # Look for existing admin customizations
                admin_apps = [app for app in result.project_context.apps if app.admin_registered_models > 0]
                for app in admin_apps:
                    integration_points.append({
                        "type": "admin_consistency",
                        "app": app.name,
                        "description": f"Follow admin patterns from {app.name}",
                        "confidence": 0.6
                    })
        
        result.integration_points = integration_points
    
    async def _generate_recommendations(
        self,
        request: ContextBuildRequest,
        result: ContextResult,
        dependencies: ServiceDependencies
    ) -> None:
        """Generate development recommendations based on context."""
        recommendations = []
        
        # Analyze project patterns for recommendations
        if result.relevant_patterns:
            high_confidence_patterns = [p for p in result.relevant_patterns if p.confidence >= 0.8]
            if high_confidence_patterns:
                pattern_names = [p.name for p in high_confidence_patterns]
                recommendations.append(
                    f"Follow established patterns: {', '.join(pattern_names)}"
                )
        
        # Check for django-cfg specific recommendations
        if result.project_context.is_django_cfg_project:
            recommendations.extend([
                "Use django-cfg configuration patterns for settings",
                "Leverage django-cfg modules for better organization",
                "Consider using BaseCfgModule for configuration management"
            ])
        
        # Feature-specific recommendations
        if request.generation_request:
            for feature in request.generation_request.features:
                feature_name = feature.value
                
                if feature_name == "models":
                    recommendations.append("Use proper field types and validation")
                    recommendations.append("Add meaningful __str__ methods")
                    recommendations.append("Consider adding Meta class with ordering")
                
                elif feature_name == "api":
                    recommendations.append("Use DRF serializers for consistent API responses")
                    recommendations.append("Implement proper pagination")
                    recommendations.append("Add API documentation with drf-spectacular")
                
                elif feature_name == "tests":
                    recommendations.append("Aim for high test coverage")
                    recommendations.append("Use factory_boy for test data generation")
                    recommendations.append("Test both positive and negative scenarios")
        
        # Context size recommendations
        context_size = sum(len(str(v)) for v in result.code_samples.values())
        if context_size > request.max_context_size:
            recommendations.append("Consider reducing context size for better AI performance")
        
        result.recommendations = recommendations
    
    async def _optimize_context_size(
        self,
        request: ContextBuildRequest,
        result: ContextResult,
        dependencies: ServiceDependencies
    ) -> None:
        """Optimize context size to fit within limits."""
        # Calculate current context size
        context_size = 0
        context_size += len(str(result.project_context))
        context_size += sum(len(str(p)) for p in result.relevant_patterns)
        context_size += sum(len(sample) for sample in result.code_samples.values())
        
        if context_size <= request.max_context_size:
            return
        
        dependencies.log_operation(
            f"Optimizing context size from {context_size} to {request.max_context_size}"
        )
        
        # Prioritize and truncate content
        # 1. Keep most relevant patterns (highest confidence)
        result.relevant_patterns = sorted(
            result.relevant_patterns, 
            key=lambda p: p.confidence, 
            reverse=True
        )[:5]  # Keep top 5 patterns
        
        # 2. Truncate code samples
        max_sample_size = request.max_context_size // (len(result.code_samples) + 1) if result.code_samples else 1000
        
        for feature, sample in result.code_samples.items():
            if len(sample) > max_sample_size:
                result.code_samples[feature] = sample[:max_sample_size] + "\n# ... (truncated for context)"
        
        # 3. Limit integration points
        result.integration_points = result.integration_points[:10]
        
        # 4. Limit recommendations
        result.recommendations = result.recommendations[:15]
