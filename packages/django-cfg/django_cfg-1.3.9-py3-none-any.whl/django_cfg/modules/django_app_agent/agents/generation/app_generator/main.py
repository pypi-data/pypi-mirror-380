"""
Main App Generator Agent class.

This module contains the primary agent class that orchestrates
Django application generation using AI.
"""

from typing import List
import asyncio

from pydantic_ai import Agent, RunContext

from ...base import DjangoAgent, AgentDependencies
from ....models.requests import AppGenerationRequest
from ....core.exceptions import GenerationError

from .models import FileGenerationRequest, GeneratedFileResponse
from .config_validator import ConfigValidator
from .prompt_manager import PromptManager


class AppGeneratorAgent(DjangoAgent):
    """AI agent for generating Django application files."""
    
    def __init__(self, config):
        """Initialize the app generator agent."""
        # Initialize components
        self.config_validator = ConfigValidator()
        self.prompt_manager = PromptManager()
        
        # Validate API keys and configure model first
        self.model = self.config_validator.validate_and_configure(config)
        
        # Initialize Pydantic AI agent
        self.pydantic_agent = Agent(
            model=self.model,
            retries=2
        )
        
        # Now call super init which will call _register_instructions
        super().__init__("app_generator", config)
    
    async def generate_file(
        self, 
        request: FileGenerationRequest
    ) -> GeneratedFileResponse:
        """Generate a specific file for the Django application."""
        try:
            # Create detailed prompt for the specific feature
            prompt = self.prompt_manager.create_feature_prompt(request)
            
            # Run AI generation
            result = await self.pydantic_agent.run(prompt)
            
            return result.data
            
        except Exception as e:
            raise GenerationError(
                f"Failed to generate {request.feature.value} file: {e}",
                app_name=request.app_name,
                generation_stage=f"generate_{request.feature.value}_file"
            )

    async def generate_multiple_files(
        self,
        app_request: AppGenerationRequest
    ) -> List[GeneratedFileResponse]:
        """Generate multiple files for an application."""
        results = []
        
        for feature in app_request.features:
            request = FileGenerationRequest(
                app_name=app_request.app_name,
                description=app_request.description,
                feature=feature,
                app_type=app_request.app_type,
                complexity=app_request.complexity
            )
            
            try:
                result = await self.generate_file(request)
                results.append(result)
            except Exception as e:
                self.logger.error(f"Failed to generate {feature.value}: {e}")
                # Continue with other features
                continue
        
        return results
    
    def _register_instructions(self) -> None:
        """Register agent instructions."""
        @self.pydantic_agent.system_prompt
        async def agent_instructions(ctx: RunContext[AgentDependencies]) -> str:
            return self.prompt_manager.get_system_prompt()
    
    def _register_tools(self) -> None:
        """Register agent tools."""
        # No additional tools needed for basic file generation
        pass
