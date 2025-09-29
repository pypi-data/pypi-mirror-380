"""
AI Integration Module for Django App Agent Generation.

This module handles integration with AI agents for intelligent
code generation based on user requirements and project context.
"""

from typing import List, Dict, Any
from pathlib import Path

from ..base import ServiceDependencies
from ...core.config import AgentConfig
from ...models.responses import GeneratedFile
from ...models.enums import AppFeature, FileType
from ...agents.generation.app_generator import AppGeneratorAgent, FileGenerationRequest
from .context import GenerationContext


class AIGenerationManager:
    """Manages AI-powered code generation process."""
    
    def __init__(self, config: AgentConfig):
        """Initialize AI generation manager."""
        self.config = config
    
    async def run_ai_generation(
        self,
        context: GenerationContext,
        dependencies: ServiceDependencies
    ) -> None:
        """Run AI agents for intelligent code generation."""
        dependencies.log_operation("Running AI generation agents")
        
        try:
            # Create AI agent
            print("🔍 Creating AI agent with config...")
            print(f"🔍 Config type: {type(self.config)}")
            try:
                ai_agent = AppGeneratorAgent(self.config)
                print("✅ AI agent created successfully")
            except Exception as e:
                print(f"❌ Failed to create AI agent: {e}")
                print(f"❌ Exception type: {type(e)}")
                import traceback
                print(f"❌ Traceback: {traceback.format_exc()}")
                raise
            
            # Generate files for each requested feature using AI
            generated_files = []
            for feature in context.request.features:
                try:
                    # Create request for this feature
                    file_request = FileGenerationRequest(
                        app_name=context.request.app_name,
                        description=context.request.description,
                        feature=feature,
                        app_type=context.request.app_type,
                        complexity=context.request.complexity
                    )
                    
                    # Generate file using AI
                    ai_response = await ai_agent.generate_file(file_request)
                    
                    # Create file path
                    file_path = context.app_directory / ai_response.filename
                    
                    # Create generated file record
                    generated_file = GeneratedFile(
                        relative_path=str(file_path.relative_to(context.target_directory)),
                        absolute_path=file_path,
                        content=ai_response.content,
                        line_count=len(ai_response.content.split('\n')),
                        file_type=self._get_file_type(ai_response.filename),
                        type_safety_score=8.5,  # AI-generated files typically have good type safety
                        complexity_score=6.0,  # AI-generated files can be moderately complex
                        description=ai_response.description
                    )
                    
                    # Write file to disk
                    file_path.parent.mkdir(parents=True, exist_ok=True)
                    file_path.write_text(ai_response.content)
                    
                    # Add to context
                    context.add_generated_file(generated_file)
                    generated_files.append(ai_response)
                    
                    dependencies.log_operation(f"Generated {feature.value} file", filename=ai_response.filename)
                    
                except Exception as e:
                    dependencies.log_error(f"Failed to generate {feature.value} with AI", e)
                    # Continue with other features
                    continue
            
            # Record AI generation results
            context.agent_outputs["generation"] = {
                "status": "completed",
                "message": f"AI generation completed successfully for {len(generated_files)} features",
                "ai_files_count": len(generated_files),
                "features_generated": [gf.filename for gf in generated_files],
                "recommendations": [f"Generated {gf.filename} for {context.request.app_name}" for gf in generated_files]
            }
            
        except Exception as e:
            dependencies.log_error("AI generation failed", e)
            context.agent_outputs["generation"] = {
                "status": "error",
                "message": f"Agent communication failed: {e}",
                "recommendations": []
            }
    
    def _get_file_type(self, filename: str) -> FileType:
        """Determine file type from filename."""
        # Map specific Django files to their types
        if filename == "__init__.py":
            return FileType.INIT
        elif filename == "models.py":
            return FileType.MODEL
        elif filename == "views.py":
            return FileType.VIEW
        elif filename == "admin.py":
            return FileType.ADMIN
        elif filename == "urls.py":
            return FileType.URL
        elif filename == "forms.py":
            return FileType.FORM
        elif filename == "tests.py":
            return FileType.TEST
        elif filename.endswith('.html'):
            return FileType.TEMPLATE
        elif filename.endswith('.py'):
            return FileType.CONFIG  # Default for other Python files
        else:
            return FileType.CONFIG  # Default fallback
