"""
AI Agents for Django App Agent Module.

This module contains specialized AI agents for:
- Code generation and analysis
- Intelligent questioning
- Quality validation
- Diagnostic problem solving
- Orchestration and coordination
"""

from .base import DjangoAgent, AgentExecutor, AgentContext
from .interfaces import AgentRegistry, AgentClientFactory

# TODO: Import specialized agents when they are implemented
# from .generation import AppGeneratorAgent
# from .analysis import CodeAnalysisAgent, ProjectAnalysisAgent
# from .validation import QualityValidationAgent, SecurityValidationAgent
# from .dialogue import DialogueAgent, QuestioningAgent
# from .diagnostic import DiagnosticAgent, ProblemSolverAgent

__all__ = [
    # Base classes
    "DjangoAgent",
    "AgentExecutor", 
    "AgentContext",
    "AgentRegistry",
    "AgentClientFactory",
    
    # TODO: Add specialized agents when implemented
    # "AppGeneratorAgent",
    # "CodeAnalysisAgent",
    # "ProjectAnalysisAgent",
    # "QualityValidationAgent",
    # "SecurityValidationAgent",
    # "DialogueAgent",
    # "QuestioningAgent",
    # "DiagnosticAgent",
    # "ProblemSolverAgent",
]
