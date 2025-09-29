"""
Agent Interfaces for Django App Agent Module.

This module defines abstract interfaces for all AI agents, designed for
easy extraction into separate web services while maintaining clean
separation of concerns between services and agents.
"""

from typing import Dict, Any, List, Optional, Protocol, runtime_checkable
from abc import ABC, abstractmethod
from pathlib import Path

from pydantic import BaseModel, Field, ConfigDict

from ..models.context import ProjectContext
from ..models.requests import AppGenerationRequest


class AgentRequest(BaseModel):
    """Base request for all agent operations."""
    
    model_config = ConfigDict(extra='forbid', validate_assignment=True)
    
    operation_id: str = Field(description="Unique operation identifier")
    correlation_id: str = Field(description="Correlation ID for tracing")
    agent_name: str = Field(description="Name of the target agent")
    operation_type: str = Field(description="Type of operation to perform")
    context: Dict[str, Any] = Field(default_factory=dict, description="Operation context")
    parameters: Dict[str, Any] = Field(default_factory=dict, description="Operation parameters")


class AgentResponse(BaseModel):
    """Base response from all agent operations."""
    
    model_config = ConfigDict(extra='forbid', validate_assignment=True)
    
    operation_id: str = Field(description="Operation identifier")
    agent_name: str = Field(description="Name of the responding agent")
    success: bool = Field(description="Whether operation was successful")
    result: Dict[str, Any] = Field(default_factory=dict, description="Operation result")
    error: Optional[str] = Field(default=None, description="Error message if failed")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata")
    execution_time_ms: int = Field(default=0, description="Execution time in milliseconds")


# Specific request/response types for different agent operations

class QuestionGenerationRequest(AgentRequest):
    """Request for question generation agents."""
    
    user_intent: str = Field(description="User's stated intent")
    project_context: ProjectContext = Field(description="Project analysis context")
    max_questions: int = Field(default=5, description="Maximum questions to generate")
    focus_areas: List[str] = Field(default_factory=list, description="Areas to focus on")


class QuestionGenerationResponse(AgentResponse):
    """Response from question generation agents."""
    
    questions: List[Dict[str, Any]] = Field(default_factory=list, description="Generated questions")
    insights: Dict[str, Any] = Field(default_factory=dict, description="Agent insights")
    confidence_score: float = Field(default=0.0, description="Confidence in questions")


class CodeGenerationRequest(AgentRequest):
    """Request for code generation agents."""
    
    generation_request: AppGenerationRequest = Field(description="App generation request")
    project_context: ProjectContext = Field(description="Project context")
    development_context: Dict[str, Any] = Field(description="Development context from questioning")
    template_variables: Dict[str, Any] = Field(default_factory=dict, description="Template variables")


class CodeGenerationResponse(AgentResponse):
    """Response from code generation agents."""
    
    generated_files: List[Dict[str, Any]] = Field(default_factory=list, description="Generated files")
    quality_metrics: Dict[str, Any] = Field(default_factory=dict, description="Quality metrics")
    recommendations: List[str] = Field(default_factory=list, description="Recommendations")


class ValidationRequest(AgentRequest):
    """Request for validation agents."""
    
    files_to_validate: List[Dict[str, Any]] = Field(description="Files to validate")
    validation_rules: List[str] = Field(description="Validation rules to apply")
    project_context: ProjectContext = Field(description="Project context")


class ValidationResponse(AgentResponse):
    """Response from validation agents."""
    
    validation_issues: List[Dict[str, Any]] = Field(default_factory=list, description="Found issues")
    quality_score: float = Field(default=0.0, description="Overall quality score")
    suggestions: List[str] = Field(default_factory=list, description="Improvement suggestions")


# Abstract interfaces for different agent types

@runtime_checkable
class AgentInterface(Protocol):
    """Protocol for all AI agents."""
    
    async def execute(self, request: AgentRequest) -> AgentResponse:
        """Execute agent operation."""
        ...
    
    def get_capabilities(self) -> List[str]:
        """Get list of agent capabilities."""
        ...
    
    def get_status(self) -> Dict[str, Any]:
        """Get agent status information."""
        ...


class BaseAgentInterface(ABC):
    """Abstract base class for all agent interfaces."""
    
    def __init__(self, agent_name: str):
        """Initialize agent interface."""
        self.agent_name = agent_name
    
    @abstractmethod
    async def execute(self, request: AgentRequest) -> AgentResponse:
        """Execute agent operation."""
        pass
    
    @abstractmethod
    def get_capabilities(self) -> List[str]:
        """Get list of agent capabilities."""
        pass
    
    def get_status(self) -> Dict[str, Any]:
        """Get agent status information."""
        return {
            "agent_name": self.agent_name,
            "status": "active",
            "capabilities": self.get_capabilities()
        }


class QuestioningAgentInterface(BaseAgentInterface):
    """Interface for questioning/dialogue agents."""
    
    @abstractmethod
    async def generate_questions(self, request: QuestionGenerationRequest) -> QuestionGenerationResponse:
        """Generate contextual questions."""
        pass
    
    async def execute(self, request: AgentRequest) -> AgentResponse:
        """Execute questioning operation."""
        if request.operation_type == "generate_questions":
            # Convert generic request to specific request
            question_request = QuestionGenerationRequest(**request.model_dump())
            return await self.generate_questions(question_request)
        else:
            return AgentResponse(
                operation_id=request.operation_id,
                agent_name=self.agent_name,
                success=False,
                error=f"Unsupported operation: {request.operation_type}"
            )


class CodeGenerationAgentInterface(BaseAgentInterface):
    """Interface for code generation agents."""
    
    @abstractmethod
    async def generate_code(self, request: CodeGenerationRequest) -> CodeGenerationResponse:
        """Generate application code."""
        pass
    
    async def execute(self, request: AgentRequest) -> AgentResponse:
        """Execute code generation operation."""
        if request.operation_type == "generate_code":
            code_request = CodeGenerationRequest(**request.model_dump())
            return await self.generate_code(code_request)
        else:
            return AgentResponse(
                operation_id=request.operation_id,
                agent_name=self.agent_name,
                success=False,
                error=f"Unsupported operation: {request.operation_type}"
            )


class ValidationAgentInterface(BaseAgentInterface):
    """Interface for validation agents."""
    
    @abstractmethod
    async def validate_code(self, request: ValidationRequest) -> ValidationResponse:
        """Validate generated code."""
        pass
    
    async def execute(self, request: AgentRequest) -> AgentResponse:
        """Execute validation operation."""
        if request.operation_type == "validate_code":
            validation_request = ValidationRequest(**request.model_dump())
            return await self.validate_code(validation_request)
        else:
            return AgentResponse(
                operation_id=request.operation_id,
                agent_name=self.agent_name,
                success=False,
                error=f"Unsupported operation: {request.operation_type}"
            )


# Agent registry for managing agent instances

class AgentRegistry:
    """Registry for managing agent instances and routing requests."""
    
    def __init__(self):
        """Initialize agent registry."""
        self._agents: Dict[str, AgentInterface] = {}
        self._agent_types: Dict[str, str] = {}
    
    def register_agent(self, agent_name: str, agent: AgentInterface, agent_type: str):
        """Register an agent instance."""
        self._agents[agent_name] = agent
        self._agent_types[agent_name] = agent_type
    
    def unregister_agent(self, agent_name: str):
        """Unregister an agent instance."""
        self._agents.pop(agent_name, None)
        self._agent_types.pop(agent_name, None)
    
    def get_agent(self, agent_name: str) -> Optional[AgentInterface]:
        """Get agent instance by name."""
        return self._agents.get(agent_name)
    
    def list_agents(self) -> Dict[str, Dict[str, Any]]:
        """List all registered agents."""
        return {
            name: {
                "type": self._agent_types.get(name, "unknown"),
                "capabilities": agent.get_capabilities(),
                "status": agent.get_status()
            }
            for name, agent in self._agents.items()
        }
    
    def get_agents_by_type(self, agent_type: str) -> List[str]:
        """Get agent names by type."""
        return [
            name for name, atype in self._agent_types.items()
            if atype == agent_type
        ]
    
    async def execute_agent_request(self, request: AgentRequest) -> AgentResponse:
        """Execute request on specified agent."""
        agent = self.get_agent(request.agent_name)
        
        if not agent:
            return AgentResponse(
                operation_id=request.operation_id,
                agent_name=request.agent_name,
                success=False,
                error=f"Agent '{request.agent_name}' not found"
            )
        
        try:
            return await agent.execute(request)
        except Exception as e:
            return AgentResponse(
                operation_id=request.operation_id,
                agent_name=request.agent_name,
                success=False,
                error=f"Agent execution failed: {e}"
            )


# Web service adapter for future extraction

class WebServiceAgentAdapter:
    """Adapter for communicating with agents via web service."""
    
    def __init__(self, base_url: str, api_key: Optional[str] = None):
        """Initialize web service adapter."""
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
    
    async def execute_agent_request(self, request: AgentRequest) -> AgentResponse:
        """Execute agent request via web service."""
        # This would implement HTTP client logic for web service communication
        # For now, it's a placeholder that shows the interface
        
        # In real implementation:
        # 1. Serialize request to JSON
        # 2. Send HTTP POST to {base_url}/agents/{agent_name}/execute
        # 3. Handle authentication with API key
        # 4. Deserialize response to AgentResponse
        # 5. Handle errors and retries
        
        return AgentResponse(
            operation_id=request.operation_id,
            agent_name=request.agent_name,
            success=False,
            error="Web service adapter not implemented yet"
        )
    
    async def list_agents(self) -> Dict[str, Dict[str, Any]]:
        """List agents available via web service."""
        # Would implement HTTP GET to {base_url}/agents
        return {}
    
    async def get_agent_status(self, agent_name: str) -> Dict[str, Any]:
        """Get agent status via web service."""
        # Would implement HTTP GET to {base_url}/agents/{agent_name}/status
        return {}


# Factory for creating agent clients (local or remote)

class AgentClientFactory:
    """Factory for creating agent clients (local or web service)."""
    
    @staticmethod
    def create_local_client(registry: AgentRegistry) -> 'LocalAgentClient':
        """Create client for local agent execution."""
        return LocalAgentClient(registry)
    
    @staticmethod
    def create_web_service_client(base_url: str, api_key: Optional[str] = None) -> 'WebServiceAgentClient':
        """Create client for web service agent execution."""
        return WebServiceAgentClient(base_url, api_key)


class LocalAgentClient:
    """Client for executing agents locally."""
    
    def __init__(self, registry: AgentRegistry):
        """Initialize local agent client."""
        self.registry = registry
    
    async def execute_request(self, request: AgentRequest) -> AgentResponse:
        """Execute agent request locally."""
        return await self.registry.execute_agent_request(request)
    
    async def list_agents(self) -> Dict[str, Dict[str, Any]]:
        """List available agents."""
        return self.registry.list_agents()


class WebServiceAgentClient:
    """Client for executing agents via web service."""
    
    def __init__(self, base_url: str, api_key: Optional[str] = None):
        """Initialize web service client."""
        self.adapter = WebServiceAgentAdapter(base_url, api_key)
    
    async def execute_request(self, request: AgentRequest) -> AgentResponse:
        """Execute agent request via web service."""
        return await self.adapter.execute_agent_request(request)
    
    async def list_agents(self) -> Dict[str, Dict[str, Any]]:
        """List available agents."""
        return await self.adapter.list_agents()


# Global registry instance (can be replaced with web service client)
_global_registry = AgentRegistry()


def get_agent_client() -> LocalAgentClient:
    """Get the global agent client (local by default)."""
    return LocalAgentClient(_global_registry)


def set_web_service_client(base_url: str, api_key: Optional[str] = None):
    """Switch to web service client globally."""
    # This would replace the global client with web service client
    # Implementation depends on how we want to handle the global state
    pass
