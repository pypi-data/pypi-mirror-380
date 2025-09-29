"""
Base Django Agent class with Pydantic AI integration.

This module provides the foundational DjangoAgent class that all
specialized agents inherit from, with proper django-cfg integration.
"""

from typing import TypeVar, Generic, Optional, Dict, Any, List, Type, Union
from abc import ABC, abstractmethod
import asyncio
import uuid
from contextlib import asynccontextmanager

from pydantic_ai import Agent, RunContext
from pydantic_ai.models import Model, KnownModelName

from ...core.config import AgentConfig, ModelConfig, AIProvider, DEFAULT_MODELS
from ...core.exceptions import (
    AgentExecutionError, 
    AuthenticationError, 
    RateLimitError,
    TimeoutError as AgentTimeoutError
)
from ...utils.logging import log_agent_operation, StructuredLogger
from .context import AgentDependencies, AgentContext

# Type variables for generic agent
OutputT = TypeVar('OutputT')
DepsT = TypeVar('DepsT', bound=AgentDependencies)


class DjangoAgent(Generic[DepsT, OutputT], ABC):
    """Base class for all Django App Agent AI agents.
    
    This class provides:
    - Integration with django-cfg configuration
    - Pydantic AI agent management
    - Error handling and retry logic
    - Logging and monitoring
    - Context management
    """
    
    def __init__(
        self,
        agent_name: str,
        config: AgentConfig,
        output_type: Type[OutputT] = str,
        deps_type: Type[DepsT] = AgentDependencies,
        model_override: Optional[str] = None,
        **agent_kwargs: Any
    ):
        """Initialize Django Agent.
        
        Args:
            agent_name: Name of the agent for logging and identification
            config: Agent configuration from django-cfg
            output_type: Expected output type from the agent
            deps_type: Dependencies type for dependency injection
            model_override: Optional model override for testing
            **agent_kwargs: Additional arguments for Pydantic AI Agent
        """
        self.agent_name = agent_name
        self.config = config
        self.output_type = output_type
        self.deps_type = deps_type
        
        # Get logger for this agent
        self.logger = StructuredLogger(f"agents.{agent_name}")
        
        # Determine model to use
        model_config = self._get_model_config(model_override)
        
        # Create Pydantic AI agent
        self._agent = Agent[DepsT, OutputT](
            model=model_config.provider.value + ":" + model_config.model_id,
            output_type=output_type,
            deps_type=deps_type,
            name=agent_name,
            retries=3,  # Default retries
            **agent_kwargs
        )
        
        # Register base instructions
        self._register_instructions()
        
        # Register tools
        self._register_tools()
    
    def _get_model_config(self, model_override: Optional[str] = None) -> ModelConfig:
        """Get model configuration for this agent."""
        if model_override:
            # Parse model override (e.g., "openai:gpt-4")
            if ":" in model_override:
                provider_str, model_id = model_override.split(":", 1)
                provider = AIProvider(provider_str)
            else:
                # Default to OpenRouter
                provider = AIProvider.OPENROUTER
                model_id = model_override
            
            return ModelConfig(
                provider=provider,
                model_id=model_id,
                tier="balanced",
                max_tokens=100000,
                temperature=0.1,
                timeout_seconds=300.0
            )
        
        # Get model config for this agent type
        model_config = self.config.get_model_config(self.agent_name)
        if model_config:
            return model_config
        
        # Fall back to default model
        default_key = "generation"  # Default task type
        if default_key in DEFAULT_MODELS:
            return DEFAULT_MODELS[default_key]
        
        # Ultimate fallback
        return ModelConfig(
            provider=AIProvider.OPENROUTER,
            model_id="anthropic/claude-3-haiku",
            tier="balanced",
            max_tokens=50000,
            temperature=0.1,
            timeout_seconds=180.0
        )
    
    @abstractmethod
    def _register_instructions(self) -> None:
        """Register agent instructions. Must be implemented by subclasses."""
        pass
    
    @abstractmethod
    def _register_tools(self) -> None:
        """Register agent tools. Must be implemented by subclasses."""
        pass
    
    @log_agent_operation("base_agent", "run")
    async def run(
        self,
        prompt: str,
        deps: DepsT,
        context: Optional[AgentContext] = None,
        **run_kwargs: Any
    ) -> OutputT:
        """Run the agent with the given prompt and dependencies.
        
        Args:
            prompt: Input prompt for the agent
            deps: Dependencies for the agent execution
            context: Optional execution context
            **run_kwargs: Additional arguments for agent.run()
            
        Returns:
            Agent output of type OutputT
            
        Raises:
            AgentExecutionError: If agent execution fails
            AuthenticationError: If API authentication fails
            RateLimitError: If rate limits are exceeded
            AgentTimeoutError: If execution times out
        """
        if context:
            context.update_progress(f"{self.agent_name}_execution", 0.0)
        
        try:
            # Validate API key
            model_config = self._get_model_config()
            if not self.config.has_api_key(model_config.provider):
                raise AuthenticationError(
                    f"No API key configured for {model_config.provider}",
                    provider=model_config.provider.value
                )
            
            deps.log_operation(f"Starting {self.agent_name} execution", prompt_length=len(prompt))
            
            # Run the agent with timeout
            result = await asyncio.wait_for(
                self._agent.run(prompt, deps=deps, **run_kwargs),
                timeout=model_config.timeout_seconds
            )
            
            if context:
                context.add_result({
                    "agent": self.agent_name,
                    "output_type": self.output_type.__name__,
                    "success": True
                })
                context.update_progress(f"{self.agent_name}_completed", 100.0)
            
            deps.log_operation(f"Completed {self.agent_name} execution successfully")
            
            return result.output
            
        except asyncio.TimeoutError as e:
            error_msg = f"Agent {self.agent_name} execution timed out"
            deps.log_error(error_msg, e)
            if context:
                context.add_error(error_msg)
            raise AgentTimeoutError(
                error_msg,
                operation=f"{self.agent_name}_execution",
                timeout_seconds=model_config.timeout_seconds
            )
            
        except Exception as e:
            error_msg = f"Agent {self.agent_name} execution failed: {e}"
            deps.log_error(error_msg, e)
            if context:
                context.add_error(error_msg)
            
            # Map specific exceptions
            if "authentication" in str(e).lower() or "api key" in str(e).lower():
                raise AuthenticationError(
                    error_msg,
                    provider=model_config.provider.value,
                    cause=e
                )
            elif "rate limit" in str(e).lower():
                raise RateLimitError(
                    error_msg,
                    provider=model_config.provider.value,
                    cause=e
                )
            else:
                raise AgentExecutionError(
                    error_msg,
                    agent_name=self.agent_name,
                    agent_operation="run",
                    cause=e
                )
    
    async def run_sync(
        self,
        prompt: str,
        deps: DepsT,
        context: Optional[AgentContext] = None,
        **run_kwargs: Any
    ) -> OutputT:
        """Synchronous wrapper for run method."""
        return await self.run(prompt, deps, context, **run_kwargs)
    
    @asynccontextmanager
    async def execution_context(
        self,
        operation_name: str,
        correlation_id: Optional[str] = None
    ):
        """Context manager for agent execution with proper cleanup."""
        if correlation_id is None:
            correlation_id = str(uuid.uuid4())
        
        context = AgentContext()
        
        try:
            with self.logger.operation_context(operation_name, correlation_id):
                yield context
        finally:
            context.mark_completed()
    
    def get_instructions(self) -> str:
        """Get the current instructions for this agent."""
        return getattr(self, '_instructions', f"You are {self.agent_name}, a specialized AI agent.")
    
    def validate_dependencies(self, deps: DepsT) -> List[str]:
        """Validate that dependencies are properly configured.
        
        Args:
            deps: Dependencies to validate
            
        Returns:
            List of validation errors (empty if valid)
        """
        errors = []
        
        # Check API key availability
        model_config = self._get_model_config()
        if not deps.config.has_api_key(model_config.provider):
            errors.append(f"No API key configured for {model_config.provider}")
        
        # Check project context if required
        if self._requires_project_context() and not deps.has_project_context():
            errors.append("Project context is required but not provided")
        
        return errors
    
    def _requires_project_context(self) -> bool:
        """Check if this agent requires project context. Override in subclasses."""
        return False
    
    @property
    def agent(self) -> Agent[DepsT, OutputT]:
        """Get the underlying Pydantic AI agent."""
        return self._agent
    
    def __repr__(self) -> str:
        """String representation of the agent."""
        return f"{self.__class__.__name__}(name='{self.agent_name}', output_type={self.output_type.__name__})"


class SimpleTextAgent(DjangoAgent[AgentDependencies, str]):
    """Simple text-based agent for basic operations."""
    
    def __init__(
        self,
        agent_name: str,
        config: AgentConfig,
        instructions: str,
        **kwargs: Any
    ):
        """Initialize simple text agent.
        
        Args:
            agent_name: Name of the agent
            config: Agent configuration
            instructions: Instructions for the agent
            **kwargs: Additional arguments
        """
        self._instructions = instructions
        super().__init__(agent_name, config, str, AgentDependencies, **kwargs)
    
    def _register_instructions(self) -> None:
        """Register instructions for the agent."""
        @self._agent.instructions
        async def agent_instructions(ctx: RunContext[AgentDependencies]) -> str:
            return self._instructions
    
    def _register_tools(self) -> None:
        """Register tools for the agent."""
        # Simple text agent has no tools by default
        pass


# Utility function for creating simple agents
def create_simple_agent(
    name: str,
    instructions: str,
    config: AgentConfig,
    **kwargs: Any
) -> SimpleTextAgent:
    """Create a simple text-based agent.
    
    Args:
        name: Agent name
        instructions: Agent instructions
        config: Agent configuration
        **kwargs: Additional arguments
        
    Returns:
        Configured SimpleTextAgent
    """
    return SimpleTextAgent(name, config, instructions, **kwargs)
