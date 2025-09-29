"""
Question Generator for Intelligent Questioning Service.

This module handles the generation of context-aware questions
using AI agents and project analysis.
"""

from typing import List, Dict, Any, Optional
import uuid
import asyncio

from pydantic import BaseModel, Field

from ...core.config import AgentConfig
from ...models.context import ProjectContext
from ...agents.interfaces import (
    get_agent_client, AgentRequest, QuestionGenerationRequest, QuestionGenerationResponse
)
from ..base import ServiceDependencies
from .models import QuestioningRequest, ContextualQuestion


class QuestionGenerator(BaseModel):
    """Generates context-aware questions using AI agents."""
    
    config: AgentConfig = Field(description="Agent configuration")
    
    # Question generation strategies
    agent_types: List[str] = Field(
        default_factory=lambda: [
            "architecture_agent",
            "business_logic_agent", 
            "integration_agent",
            "security_agent",
            "performance_agent"
        ],
        description="Types of AI agents to use for question generation"
    )

    async def generate_questions(
        self,
        request: QuestioningRequest,
        project_context: ProjectContext,
        dependencies: ServiceDependencies
    ) -> List[ContextualQuestion]:
        """Generate context-aware questions using multiple AI agents."""
        dependencies.log_operation(
            "Generating questions via AI agents",
            max_questions=request.max_questions,
            focus_areas=request.focus_areas,
            agent_types=len(self.agent_types)
        )
        
        all_questions = []
        
        try:
            # Generate questions from each agent type
            generation_tasks = []
            for agent_type in self.agent_types:
                task = self._generate_questions_from_agent(
                    agent_type, request, project_context, dependencies
                )
                generation_tasks.append(task)
            
            # Run all agents concurrently
            agent_results = await asyncio.gather(*generation_tasks, return_exceptions=True)
            
            # Collect questions from all agents
            for i, result in enumerate(agent_results):
                if isinstance(result, Exception):
                    dependencies.log_error(f"Agent {self.agent_types[i]} failed", result)
                    continue
                
                all_questions.extend(result)
            
            # Optimize and filter questions
            optimized_questions = await self._optimize_question_flow(
                all_questions, request, dependencies
            )
            
            dependencies.log_operation(
                "Question generation completed",
                total_generated=len(all_questions),
                optimized_count=len(optimized_questions)
            )
            
            return optimized_questions
            
        except Exception as e:
            dependencies.log_error("Question generation failed", e)
            # Return fallback questions
            return self._generate_fallback_questions(request, project_context)
    
    async def _generate_questions_from_agent(
        self,
        agent_type: str,
        request: QuestioningRequest,
        project_context: ProjectContext,
        dependencies: ServiceDependencies
    ) -> List[ContextualQuestion]:
        """Generate questions from a specific AI agent."""
        try:
            # Get agent client
            agent_client = get_agent_client(agent_type, self.config)
            
            # Prepare agent request
            agent_request = QuestionGenerationRequest(
                user_intent=request.user_intent,
                project_context=project_context,
                generation_request=request.generation_request,
                max_questions=min(request.max_questions // len(self.agent_types) + 2, 8),
                focus_areas=request.focus_areas,
                agent_specialty=agent_type
            )
            
            # Call agent
            response = await agent_client.process(agent_request)
            
            if isinstance(response, QuestionGenerationResponse):
                # Convert agent response to ContextualQuestion objects
                questions = []
                for q in response.questions:
                    question = ContextualQuestion(
                        id=str(uuid.uuid4()),
                        text=q.get("text", ""),
                        question_type=q.get("type", "text"),
                        priority=q.get("priority", 5),
                        impact_level=q.get("impact_level", "medium"),
                        context_evidence=q.get("evidence", []),
                        architectural_implications=q.get("implications", []),
                        options=q.get("options"),
                        default_value=q.get("default"),
                        generated_by=agent_type,
                        generation_reasoning=q.get("reasoning", "")
                    )
                    questions.append(question)
                
                return questions
            
        except Exception as e:
            dependencies.log_error(f"Failed to generate questions from {agent_type}", e)
        
        return []
    
    async def _optimize_question_flow(
        self,
        questions: List[ContextualQuestion],
        request: QuestioningRequest,
        dependencies: ServiceDependencies
    ) -> List[ContextualQuestion]:
        """Optimize question flow and remove duplicates."""
        if not questions:
            return []
        
        # Remove duplicates based on similar text
        unique_questions = []
        seen_texts = set()
        
        for question in questions:
            # Simple deduplication based on text similarity
            text_key = question.text.lower().strip()
            if text_key not in seen_texts:
                seen_texts.add(text_key)
                unique_questions.append(question)
        
        # Sort by priority and impact
        priority_weights = {"critical": 4, "high": 3, "medium": 2, "low": 1}
        
        def question_score(q: ContextualQuestion) -> float:
            priority_score = (11 - q.priority) / 10  # Convert 1-10 to 1.0-0.1
            impact_score = priority_weights.get(q.impact_level, 2) / 4
            return priority_score * 0.6 + impact_score * 0.4
        
        sorted_questions = sorted(unique_questions, key=question_score, reverse=True)
        
        # Limit to max_questions
        limited_questions = sorted_questions[:request.max_questions]
        
        dependencies.log_operation(
            "Question optimization completed",
            original_count=len(questions),
            unique_count=len(unique_questions),
            final_count=len(limited_questions)
        )
        
        return limited_questions
    
    def _generate_fallback_questions(
        self,
        request: QuestioningRequest,
        project_context: ProjectContext
    ) -> List[ContextualQuestion]:
        """Generate fallback questions when AI agents fail."""
        fallback_questions = [
            {
                "text": "What is the primary purpose of this application?",
                "type": "text",
                "priority": 1,
                "impact_level": "critical",
                "reasoning": "Understanding the core purpose is essential for proper architecture"
            },
            {
                "text": "Will this application need user authentication?",
                "type": "yes_no",
                "priority": 2,
                "impact_level": "high",
                "reasoning": "Authentication affects security architecture and user management"
            },
            {
                "text": "What type of data will this application primarily handle?",
                "type": "choice",
                "priority": 3,
                "impact_level": "high",
                "options": ["User data", "Business data", "Content/Media", "Analytics", "Other"],
                "reasoning": "Data type influences model design and security requirements"
            },
            {
                "text": "Do you need an API for external integrations?",
                "type": "yes_no",
                "priority": 4,
                "impact_level": "medium",
                "reasoning": "API requirements affect architecture and serialization needs"
            },
            {
                "text": "What level of admin interface do you need?",
                "type": "choice",
                "priority": 5,
                "impact_level": "medium",
                "options": ["Basic Django admin", "Custom admin interface", "No admin needed"],
                "reasoning": "Admin interface complexity affects development time and features"
            }
        ]
        
        questions = []
        for i, q_data in enumerate(fallback_questions[:request.max_questions]):
            question = ContextualQuestion(
                id=str(uuid.uuid4()),
                text=q_data["text"],
                question_type=q_data["type"],
                priority=q_data["priority"],
                impact_level=q_data["impact_level"],
                context_evidence=["Fallback question due to AI agent unavailability"],
                architectural_implications=[],
                options=q_data.get("options"),
                default_value=q_data.get("default"),
                generated_by="fallback_generator",
                generation_reasoning=q_data["reasoning"]
            )
            questions.append(question)
        
        return questions
