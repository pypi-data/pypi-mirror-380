"""
Main Intelligent Questioning Service for Django App Agent Module.

This service orchestrates the intelligent questioning process by coordinating
with specialized AI agents to generate context-aware questions based on
project analysis and user requirements.
"""

from typing import List, Dict, Any, Optional
from pathlib import Path

from pydantic import BaseModel, Field

from ...core.config import AgentConfig
from ...models.context import ProjectContext
from ..base import BaseService, ServiceDependencies
from ..context_builder import ContextBuilderService, ContextBuildRequest
from .models import QuestioningRequest, QuestioningResult, QuestioningSession, ContextualQuestion
from .question_generator import QuestionGenerator
from .response_processor import ResponseProcessor
from .session_manager import SessionManager


class QuestioningService(BaseService[QuestioningRequest, QuestioningResult]):
    """
    Intelligent questioning service for context-aware requirement gathering.
    
    This service:
    1. Analyzes project context and user intent
    2. Generates targeted questions using AI agents
    3. Manages interactive questioning sessions
    4. Processes responses to refine generation requests
    5. Provides insights and recommendations
    """
    
    def __init__(self, config: AgentConfig):
        """Initialize questioning service."""
        super().__init__("questioning", config)
        self.config = config
        
        # Initialize components
        self.context_builder = ContextBuilderService(config)
        self.question_generator = QuestionGenerator(config=config)
        self.response_processor = ResponseProcessor(config=config)
        self.session_manager = SessionManager(config=config)
    
    async def process(
        self,
        request: QuestioningRequest,
        dependencies: ServiceDependencies
    ) -> QuestioningResult:
        """
        Process intelligent questioning request.
        
        Args:
            request: Questioning request with user intent and project info
            dependencies: Service dependencies
            
        Returns:
            QuestioningResult with session and refined request
        """
        dependencies.log_operation(
            "Starting intelligent questioning process",
            user_intent=request.user_intent,
            project_root=str(request.project_root),
            max_questions=request.max_questions
        )
        
        try:
            # 1. Build comprehensive project context
            project_context = await self._build_project_context(request, dependencies)
            
            # 2. Generate context-aware questions using AI agents
            questions = await self.question_generator.generate_questions(
                request, project_context, dependencies
            )
            
            # 3. Create questioning session
            session = await self.session_manager.create_session(
                request, questions, project_context, dependencies
            )
            
            # 4. For this implementation, we'll simulate the questioning process
            # In a real implementation, this would be interactive
            simulated_session = await self._simulate_questioning_process(
                session, dependencies
            )
            
            # 5. Process responses and build refined request
            refined_request = await self.response_processor.process_responses(
                simulated_session, dependencies
            )
            
            # 6. Gather AI insights
            insights = await self.session_manager.gather_agent_insights(
                simulated_session, dependencies
            )
            
            # 7. Calculate confidence score
            confidence_score = self.session_manager.calculate_confidence_score(simulated_session)
            
            # 8. Generate recommendations
            recommendations = self._generate_recommendations(simulated_session, insights)
            
            result = QuestioningResult(
                session=simulated_session,
                refined_request=refined_request,
                confidence_score=confidence_score,
                insights=insights,
                recommendations=recommendations
            )
            
            dependencies.log_operation(
                "Questioning process completed",
                session_id=simulated_session.session_id,
                confidence_score=confidence_score,
                refined_app_name=refined_request.app_name,
                features_count=len(refined_request.features)
            )
            
            return result
            
        except Exception as e:
            dependencies.log_error("Questioning process failed", e)
            raise
    
    async def _build_project_context(
        self,
        request: QuestioningRequest,
        dependencies: ServiceDependencies
    ) -> ProjectContext:
        """Build comprehensive project context for question generation."""
        dependencies.log_operation("Building project context for questioning")
        
        # Create context build request
        context_request = ContextBuildRequest(
            project_root=request.project_root,
            target_app_name=None,  # We don't have an app name yet
            generation_request=request.generation_request,
            include_code_samples=True,
            max_context_size=30000,  # Smaller context for questioning
            focus_areas=request.focus_areas
        )
        
        # Build context using context builder service
        context_result = await self.context_builder.process(context_request, dependencies)
        
        return context_result.project_context
    
    async def _simulate_questioning_process(
        self,
        session: QuestioningSession,
        dependencies: ServiceDependencies
    ) -> QuestioningSession:
        """
        Simulate the questioning process for demonstration.
        
        In a real implementation, this would be replaced by actual
        user interaction through the UI.
        """
        dependencies.log_operation(
            "Simulating questioning process",
            session_id=session.session_id,
            questions_count=len(session.questions)
        )
        
        # Simulate responses based on question types and user intent
        for question in session.questions[:min(5, len(session.questions))]:  # Limit to 5 questions for demo
            simulated_answer = self._generate_simulated_answer(question, session.user_intent)
            confidence = self._calculate_simulated_confidence(question, simulated_answer)
            
            # Add response to session
            await self.session_manager.add_response(
                session.session_id,
                question.id,
                simulated_answer,
                confidence,
                dependencies
            )
        
        # Mark session as completed
        await self.session_manager.complete_session(session.session_id, dependencies)
        
        return session
    
    def _generate_simulated_answer(
        self,
        question: ContextualQuestion,
        user_intent: str
    ) -> str:
        """Generate simulated answer based on question and user intent."""
        intent_lower = user_intent.lower()
        question_lower = question.text.lower()
        
        # Generate contextual answers based on question type
        if question.question_type == "yes_no":
            # Determine yes/no based on question content and user intent
            if any(word in question_lower for word in ["auth", "login", "user"]):
                return "yes" if any(word in intent_lower for word in ["user", "auth", "login"]) else "no"
            elif any(word in question_lower for word in ["api", "integration"]):
                return "yes" if any(word in intent_lower for word in ["api", "integration", "external"]) else "no"
            elif any(word in question_lower for word in ["admin", "management"]):
                return "yes" if any(word in intent_lower for word in ["admin", "manage", "dashboard"]) else "no"
            else:
                return "yes"  # Default to yes for other questions
        
        elif question.question_type == "choice" and question.options:
            # Select most relevant option based on user intent
            for option in question.options:
                if any(word in option.lower() for word in intent_lower.split()):
                    return option
            return question.options[0]  # Default to first option
        
        else:  # text question
            # Generate contextual text response
            if "purpose" in question_lower:
                return f"Application for {user_intent}"
            elif "data" in question_lower:
                return "Business data and user information"
            elif "users" in question_lower:
                return "Small to medium team (10-50 users)"
            else:
                return f"Based on the requirement: {user_intent}"
    
    def _calculate_simulated_confidence(
        self,
        question: ContextualQuestion,
        answer: str
    ) -> float:
        """Calculate simulated confidence score."""
        # Higher confidence for specific answers, lower for generic ones
        if question.question_type == "yes_no":
            return 0.9
        elif question.question_type == "choice":
            return 0.8
        elif len(answer) > 20:  # Detailed text answer
            return 0.7
        else:
            return 0.6
    
    def _generate_recommendations(
        self,
        session: QuestioningSession,
        insights: Dict[str, Any]
    ) -> List[str]:
        """Generate development recommendations based on session and insights."""
        recommendations = []
        
        # Add recommendations from insights
        if "recommendations" in insights:
            recommendations.extend(insights["recommendations"])
        
        # Add confidence-based recommendations
        confidence_score = self.session_manager.calculate_confidence_score(session)
        
        if confidence_score > 0.8:
            recommendations.append("High confidence in requirements - proceed with development")
        elif confidence_score > 0.6:
            recommendations.append("Moderate confidence - consider prototype or MVP approach")
        else:
            recommendations.append("Low confidence - additional requirement gathering recommended")
        
        # Add architectural recommendations based on patterns
        if insights.get("pattern_detection", {}).get("api_focused"):
            recommendations.append("Consider API-first architecture with comprehensive serializers")
        
        if insights.get("pattern_detection", {}).get("user_centric"):
            recommendations.append("Implement robust authentication and user management features")
        
        if insights.get("pattern_detection", {}).get("data_intensive"):
            recommendations.append("Focus on efficient data models and database optimization")
        
        return recommendations[:5]  # Limit to top 5 recommendations
