"""
Base classes for Django App Agent AI agents.

This module provides foundational classes for all AI agents:
- DjangoAgent: Base class with django-cfg integration
- AgentContext: Context management for agent execution
- AgentExecutor: Execution management and orchestration
"""

from .agent import DjangoAgent, SimpleTextAgent, create_simple_agent
from .context import AgentContext, AgentDependencies, create_agent_dependencies
from .executor import AgentExecutor, ExecutionResult, ExecutionStatus

__all__ = [
    "DjangoAgent",
    "SimpleTextAgent",
    "create_simple_agent",
    "AgentContext", 
    "AgentDependencies",
    "create_agent_dependencies",
    "AgentExecutor",
    "ExecutionResult",
    "ExecutionStatus",
]
