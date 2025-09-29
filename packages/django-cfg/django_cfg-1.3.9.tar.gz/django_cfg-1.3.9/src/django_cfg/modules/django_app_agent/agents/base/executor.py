"""
Agent execution management for Django App Agent Module.

This module provides execution management and orchestration for AI agents,
including result handling, error management, and performance tracking.
"""

from typing import TypeVar, Generic, Optional, Dict, Any, List, Union, Callable, Awaitable
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
import asyncio

from pydantic import BaseModel, Field, ConfigDict

from ...core.config import AgentConfig
from ...core.exceptions import AgentExecutionError, ValidationError
from ...models.base import TimestampedModel
from ...utils.logging import StructuredLogger, get_logger
from .context import AgentDependencies, AgentContext
from .agent import DjangoAgent

# Type variables
OutputT = TypeVar('OutputT')
DepsT = TypeVar('DepsT', bound=AgentDependencies)


class ExecutionStatus(str, Enum):
    """Status of agent execution."""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class ExecutionResult(BaseModel, Generic[OutputT]):
    """Result of agent execution."""
    
    model_config = ConfigDict(
        extra='forbid',
        validate_assignment=True,
        arbitrary_types_allowed=True
    )
    
    # Execution metadata
    execution_id: str = Field(description="Unique execution identifier")
    agent_name: str = Field(description="Name of the agent that was executed")
    status: ExecutionStatus = Field(description="Execution status")
    
    # Timing information
    start_time: datetime = Field(description="Execution start time")
    end_time: Optional[datetime] = Field(default=None, description="Execution end time")
    
    # Results
    output: Optional[OutputT] = Field(default=None, description="Agent output")
    error: Optional[str] = Field(default=None, description="Error message if failed")
    
    # Performance metrics
    execution_time_seconds: float = Field(default=0.0, description="Total execution time")
    token_usage: Dict[str, int] = Field(default_factory=dict, description="Token usage by provider")
    api_calls_count: int = Field(default=0, description="Number of API calls made")
    
    # Context information
    correlation_id: str = Field(description="Correlation ID for tracing")
    operation_name: str = Field(description="Name of the operation")
    
    @property
    def is_successful(self) -> bool:
        """Check if execution was successful."""
        return self.status == ExecutionStatus.COMPLETED and self.output is not None
    
    @property
    def is_failed(self) -> bool:
        """Check if execution failed."""
        return self.status == ExecutionStatus.FAILED
    
    def get_summary(self) -> Dict[str, Any]:
        """Get execution summary."""
        return {
            "execution_id": self.execution_id,
            "agent_name": self.agent_name,
            "status": self.status.value,
            "is_successful": self.is_successful,
            "execution_time_seconds": self.execution_time_seconds,
            "total_tokens": sum(self.token_usage.values()),
            "api_calls": self.api_calls_count,
            "has_output": self.output is not None,
            "has_error": self.error is not None,
        }


@dataclass
class ExecutionPlan:
    """Plan for executing multiple agents in sequence or parallel."""
    
    name: str
    agents: List[DjangoAgent] = field(default_factory=list)
    dependencies: Dict[str, List[str]] = field(default_factory=dict)
    parallel_groups: List[List[str]] = field(default_factory=list)
    timeout_seconds: float = 300.0
    
    def add_agent(self, agent: DjangoAgent, depends_on: Optional[List[str]] = None) -> None:
        """Add agent to execution plan."""
        self.agents.append(agent)
        if depends_on:
            self.dependencies[agent.agent_name] = depends_on
    
    def add_parallel_group(self, agent_names: List[str]) -> None:
        """Add group of agents that can run in parallel."""
        self.parallel_groups.append(agent_names)
    
    def validate(self) -> List[str]:
        """Validate execution plan."""
        errors = []
        agent_names = {agent.agent_name for agent in self.agents}
        
        # Check dependencies reference existing agents
        for agent_name, deps in self.dependencies.items():
            if agent_name not in agent_names:
                errors.append(f"Agent '{agent_name}' in dependencies not found in plan")
            
            for dep in deps:
                if dep not in agent_names:
                    errors.append(f"Dependency '{dep}' for '{agent_name}' not found in plan")
        
        # Check parallel groups reference existing agents
        for group in self.parallel_groups:
            for agent_name in group:
                if agent_name not in agent_names:
                    errors.append(f"Agent '{agent_name}' in parallel group not found in plan")
        
        return errors


class AgentExecutor:
    """Executor for managing and running Django App Agent AI agents."""
    
    def __init__(self, config: AgentConfig):
        """Initialize agent executor.
        
        Args:
            config: Agent configuration
        """
        self.config = config
        self.logger = get_logger("agent_executor")
        self._active_executions: Dict[str, ExecutionResult] = {}
    
    async def execute_single(
        self,
        agent: DjangoAgent[DepsT, OutputT],
        prompt: str,
        deps: DepsT,
        execution_id: Optional[str] = None,
        timeout_seconds: Optional[float] = None
    ) -> ExecutionResult[OutputT]:
        """Execute a single agent.
        
        Args:
            agent: Agent to execute
            prompt: Input prompt
            deps: Agent dependencies
            execution_id: Optional execution ID
            timeout_seconds: Optional timeout override
            
        Returns:
            Execution result
        """
        import uuid
        
        if execution_id is None:
            execution_id = str(uuid.uuid4())
        
        start_time = datetime.now(timezone.utc)
        
        # Create execution result
        result = ExecutionResult[OutputT](
            execution_id=execution_id,
            agent_name=agent.agent_name,
            status=ExecutionStatus.PENDING,
            start_time=start_time,
            correlation_id=deps.correlation_id,
            operation_name=deps.operation_name
        )
        
        # Track active execution
        self._active_executions[execution_id] = result
        
        try:
            # Update status to running
            result.status = ExecutionStatus.RUNNING
            
            # Create execution context
            context = AgentContext()
            
            # Determine timeout
            timeout = timeout_seconds or 300.0
            
            self.logger.info(
                f"Starting execution of agent {agent.agent_name}",
                execution_id=execution_id,
                agent_name=agent.agent_name,
                timeout_seconds=timeout
            )
            
            # Execute agent with timeout
            output = await asyncio.wait_for(
                agent.run(prompt, deps, context),
                timeout=timeout
            )
            
            # Update result with success
            end_time = datetime.now(timezone.utc)
            result.status = ExecutionStatus.COMPLETED
            result.output = output
            result.end_time = end_time
            result.execution_time_seconds = (end_time - start_time).total_seconds()
            result.token_usage = context.token_usage.copy()
            result.api_calls_count = context.api_calls_count
            
            self.logger.info(
                f"Completed execution of agent {agent.agent_name}",
                execution_id=execution_id,
                execution_time_seconds=result.execution_time_seconds,
                success=True
            )
            
            return result
            
        except asyncio.TimeoutError:
            error_msg = f"Agent {agent.agent_name} execution timed out after {timeout} seconds"
            result.status = ExecutionStatus.FAILED
            result.error = error_msg
            result.end_time = datetime.now(timezone.utc)
            result.execution_time_seconds = (result.end_time - start_time).total_seconds()
            
            self.logger.error(
                error_msg,
                execution_id=execution_id,
                agent_name=agent.agent_name,
                timeout_seconds=timeout
            )
            
            return result
            
        except Exception as e:
            error_msg = f"Agent {agent.agent_name} execution failed: {e}"
            result.status = ExecutionStatus.FAILED
            result.error = error_msg
            result.end_time = datetime.now(timezone.utc)
            result.execution_time_seconds = (result.end_time - start_time).total_seconds()
            
            self.logger.error(
                error_msg,
                execution_id=execution_id,
                agent_name=agent.agent_name,
                error=str(e),
                error_type=type(e).__name__
            )
            
            return result
            
        finally:
            # Remove from active executions
            self._active_executions.pop(execution_id, None)
    
    async def execute_plan(
        self,
        plan: ExecutionPlan,
        prompt: str,
        deps: AgentDependencies,
        execution_id: Optional[str] = None
    ) -> Dict[str, ExecutionResult]:
        """Execute multiple agents according to a plan.
        
        Args:
            plan: Execution plan
            prompt: Input prompt for all agents
            deps: Base dependencies (will be copied for each agent)
            execution_id: Optional execution ID
            
        Returns:
            Dictionary mapping agent names to execution results
        """
        import uuid
        
        if execution_id is None:
            execution_id = str(uuid.uuid4())
        
        # Validate plan
        validation_errors = plan.validate()
        if validation_errors:
            raise ValidationError(
                f"Invalid execution plan: {'; '.join(validation_errors)}",
                validation_type="execution_plan"
            )
        
        self.logger.info(
            f"Starting execution plan '{plan.name}'",
            execution_id=execution_id,
            agents_count=len(plan.agents),
            parallel_groups=len(plan.parallel_groups)
        )
        
        results: Dict[str, ExecutionResult] = {}
        agent_map = {agent.agent_name: agent for agent in plan.agents}
        
        try:
            # Execute agents in dependency order
            executed = set()
            
            while len(executed) < len(plan.agents):
                # Find agents ready to execute (dependencies satisfied)
                ready_agents = []
                
                for agent in plan.agents:
                    if agent.agent_name in executed:
                        continue
                    
                    # Check if dependencies are satisfied
                    agent_deps = plan.dependencies.get(agent.agent_name, [])
                    if all(dep in executed for dep in agent_deps):
                        ready_agents.append(agent)
                
                if not ready_agents:
                    # Check for circular dependencies
                    remaining = [a.agent_name for a in plan.agents if a.agent_name not in executed]
                    raise AgentExecutionError(
                        f"Circular dependency detected or no agents ready to execute. Remaining: {remaining}",
                        agent_name="executor",
                        agent_operation="execute_plan"
                    )
                
                # Execute ready agents (potentially in parallel)
                tasks = []
                for agent in ready_agents:
                    # Create agent-specific dependencies
                    agent_deps = AgentDependencies(
                        config=deps.config,
                        logger=deps.logger,
                        project_context=deps.project_context,
                        infrastructure_context=deps.infrastructure_context,
                        correlation_id=f"{execution_id}_{agent.agent_name}",
                        operation_name=f"{deps.operation_name}_{agent.agent_name}",
                        project_root=deps.project_root,
                        output_directory=deps.output_directory,
                        execution_metadata=deps.execution_metadata.copy()
                    )
                    
                    task = self.execute_single(
                        agent,
                        prompt,
                        agent_deps,
                        f"{execution_id}_{agent.agent_name}",
                        plan.timeout_seconds
                    )
                    tasks.append((agent.agent_name, task))
                
                # Wait for all ready agents to complete
                for agent_name, task in tasks:
                    result = await task
                    results[agent_name] = result
                    executed.add(agent_name)
                    
                    if not result.is_successful:
                        self.logger.warning(
                            f"Agent {agent_name} failed in execution plan",
                            execution_id=execution_id,
                            error=result.error
                        )
            
            self.logger.info(
                f"Completed execution plan '{plan.name}'",
                execution_id=execution_id,
                successful_agents=sum(1 for r in results.values() if r.is_successful),
                failed_agents=sum(1 for r in results.values() if r.is_failed)
            )
            
            return results
            
        except Exception as e:
            self.logger.error(
                f"Execution plan '{plan.name}' failed",
                execution_id=execution_id,
                error=str(e),
                error_type=type(e).__name__
            )
            raise
    
    def get_active_executions(self) -> Dict[str, ExecutionResult]:
        """Get currently active executions."""
        return self._active_executions.copy()
    
    def cancel_execution(self, execution_id: str) -> bool:
        """Cancel an active execution.
        
        Args:
            execution_id: ID of execution to cancel
            
        Returns:
            True if execution was cancelled, False if not found
        """
        if execution_id in self._active_executions:
            result = self._active_executions[execution_id]
            result.status = ExecutionStatus.CANCELLED
            result.end_time = datetime.now(timezone.utc)
            result.execution_time_seconds = (result.end_time - result.start_time).total_seconds()
            
            self.logger.info(
                f"Cancelled execution {execution_id}",
                execution_id=execution_id,
                agent_name=result.agent_name
            )
            
            return True
        
        return False
    
    def get_execution_summary(self) -> Dict[str, Any]:
        """Get summary of executor state."""
        active = self.get_active_executions()
        
        return {
            "active_executions_count": len(active),
            "active_agents": [r.agent_name for r in active.values()],
            "executor_config": {
                "debug_mode": self.config.debug_mode,
                "log_level": self.config.log_level.value,
            }
        }
