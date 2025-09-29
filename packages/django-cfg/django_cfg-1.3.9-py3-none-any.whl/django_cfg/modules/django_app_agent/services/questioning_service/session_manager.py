"""
Session Manager for Intelligent Questioning Service.

This module manages questioning sessions, including creation,
progress tracking, and completion handling.
"""

from typing import List, Dict, Any, Optional
import uuid
from datetime import datetime, timezone

from pydantic import BaseModel, Field

from ...core.config import AgentConfig
from ...models.context import ProjectContext
from ..base import ServiceDependencies
from .models import (
    QuestioningRequest, QuestioningSession, ContextualQuestion,
    QuestionResponse, QuestioningResult
)


class SessionManager(BaseModel):
    """Manages questioning sessions and their lifecycle."""
    
    config: AgentConfig = Field(description="Agent configuration")
    
    # Session storage (in production, this would be a database)
    active_sessions: Dict[str, QuestioningSession] = Field(
        default_factory=dict,
        description="Active questioning sessions"
    )

    async def create_session(
        self,
        request: QuestioningRequest,
        questions: List[ContextualQuestion],
        project_context: ProjectContext,
        dependencies: ServiceDependencies
    ) -> QuestioningSession:
        """Create a new questioning session."""
        session_id = str(uuid.uuid4())
        
        session = QuestioningSession(
            session_id=session_id,
            questions=questions,
            project_context=project_context,
            user_intent=request.user_intent,
            created_at=datetime.now(timezone.utc)
        )
        
        # Store session
        self.active_sessions[session_id] = session
        
        dependencies.log_operation(
            "Questioning session created",
            session_id=session_id,
            questions_count=len(questions),
            user_intent=request.user_intent
        )
        
        return session
    
    async def add_response(
        self,
        session_id: str,
        question_id: str,
        answer: str,
        confidence: float,
        dependencies: ServiceDependencies
    ) -> Optional[QuestioningSession]:
        """Add a response to an existing session."""
        session = self.active_sessions.get(session_id)
        if not session:
            dependencies.log_error(f"Session not found: {session_id}")
            return None
        
        # Validate question exists
        question = self._find_question_by_id(session.questions, question_id)
        if not question:
            dependencies.log_error(f"Question not found: {question_id}")
            return None
        
        # Create response
        response = QuestionResponse(
            question_id=question_id,
            answer=answer,
            confidence=confidence,
            timestamp=datetime.now(timezone.utc)
        )
        
        # Add to session
        session.responses.append(response)
        session.current_question_index = len(session.responses)
        
        # Check if session is completed
        if len(session.responses) >= len(session.questions):
            session.is_completed = True
            session.completed_at = datetime.now(timezone.utc)
        
        dependencies.log_operation(
            "Response added to session",
            session_id=session_id,
            question_id=question_id,
            completion_percentage=session.completion_percentage,
            is_completed=session.is_completed
        )
        
        return session
    
    async def get_session(
        self,
        session_id: str,
        dependencies: ServiceDependencies
    ) -> Optional[QuestioningSession]:
        """Get an existing session."""
        session = self.active_sessions.get(session_id)
        
        if not session:
            dependencies.log_error(f"Session not found: {session_id}")
        
        return session
    
    async def get_next_question(
        self,
        session_id: str,
        dependencies: ServiceDependencies
    ) -> Optional[ContextualQuestion]:
        """Get the next unanswered question in a session."""
        session = self.active_sessions.get(session_id)
        if not session:
            return None
        
        if session.is_completed:
            return None
        
        # Find next unanswered question
        answered_question_ids = {r.question_id for r in session.responses}
        
        for question in session.questions:
            if question.id not in answered_question_ids:
                return question
        
        return None
    
    async def complete_session(
        self,
        session_id: str,
        dependencies: ServiceDependencies
    ) -> Optional[QuestioningSession]:
        """Mark a session as completed."""
        session = self.active_sessions.get(session_id)
        if not session:
            return None
        
        session.is_completed = True
        session.completed_at = datetime.now(timezone.utc)
        
        dependencies.log_operation(
            "Session completed",
            session_id=session_id,
            total_responses=len(session.responses),
            completion_percentage=session.completion_percentage
        )
        
        return session
    
    async def cleanup_session(
        self,
        session_id: str,
        dependencies: ServiceDependencies
    ) -> bool:
        """Remove a session from active sessions."""
        if session_id in self.active_sessions:
            del self.active_sessions[session_id]
            dependencies.log_operation(f"Session cleaned up: {session_id}")
            return True
        
        return False
    
    def calculate_confidence_score(
        self,
        session: QuestioningSession
    ) -> float:
        """Calculate overall confidence score for a session."""
        if not session.responses:
            return 0.0
        
        # Weight confidence by question impact
        impact_weights = {"critical": 1.0, "high": 0.8, "medium": 0.6, "low": 0.4}
        
        weighted_confidence = 0.0
        total_weight = 0.0
        
        for response in session.responses:
            question = self._find_question_by_id(session.questions, response.question_id)
            if question:
                weight = impact_weights.get(question.impact_level, 0.6)
                weighted_confidence += response.confidence * weight
                total_weight += weight
        
        return weighted_confidence / total_weight if total_weight > 0 else 0.0
    
    async def gather_agent_insights(
        self,
        session: QuestioningSession,
        dependencies: ServiceDependencies
    ) -> Dict[str, Any]:
        """Gather insights from AI agents based on session responses."""
        insights = {
            "response_analysis": {},
            "pattern_detection": {},
            "recommendations": [],
            "confidence_assessment": {}
        }
        
        try:
            # Analyze response patterns
            insights["response_analysis"] = self._analyze_response_patterns(session)
            
            # Detect architectural patterns
            insights["pattern_detection"] = self._detect_architectural_patterns(session)
            
            # Generate recommendations
            insights["recommendations"] = self._generate_recommendations(session)
            
            # Assess confidence
            insights["confidence_assessment"] = {
                "overall_confidence": self.calculate_confidence_score(session),
                "low_confidence_areas": self._identify_low_confidence_areas(session),
                "high_confidence_areas": self._identify_high_confidence_areas(session)
            }
            
        except Exception as e:
            dependencies.log_error("Failed to gather agent insights", e)
        
        return insights
    
    def _find_question_by_id(
        self,
        questions: List[ContextualQuestion],
        question_id: str
    ) -> Optional[ContextualQuestion]:
        """Find question by ID."""
        for question in questions:
            if question.id == question_id:
                return question
        return None
    
    def _analyze_response_patterns(
        self,
        session: QuestioningSession
    ) -> Dict[str, Any]:
        """Analyze patterns in user responses."""
        patterns = {
            "response_length_avg": 0.0,
            "confidence_avg": 0.0,
            "yes_no_ratio": 0.0,
            "detailed_responses": 0
        }
        
        if not session.responses:
            return patterns
        
        # Calculate averages
        total_length = sum(len(r.answer) for r in session.responses)
        total_confidence = sum(r.confidence for r in session.responses)
        
        patterns["response_length_avg"] = total_length / len(session.responses)
        patterns["confidence_avg"] = total_confidence / len(session.responses)
        
        # Count yes/no responses
        yes_no_count = sum(
            1 for r in session.responses 
            if r.answer.lower() in ["yes", "no", "y", "n", "true", "false"]
        )
        patterns["yes_no_ratio"] = yes_no_count / len(session.responses)
        
        # Count detailed responses (>20 characters)
        patterns["detailed_responses"] = sum(
            1 for r in session.responses if len(r.answer) > 20
        )
        
        return patterns
    
    def _detect_architectural_patterns(
        self,
        session: QuestioningSession
    ) -> Dict[str, Any]:
        """Detect architectural patterns from responses."""
        patterns = {
            "api_focused": False,
            "admin_heavy": False,
            "user_centric": False,
            "data_intensive": False
        }
        
        # Analyze responses for architectural indicators
        all_answers = " ".join(r.answer.lower() for r in session.responses)
        
        patterns["api_focused"] = "api" in all_answers or "integration" in all_answers
        patterns["admin_heavy"] = "admin" in all_answers or "management" in all_answers
        patterns["user_centric"] = "user" in all_answers or "authentication" in all_answers
        patterns["data_intensive"] = "data" in all_answers or "database" in all_answers
        
        return patterns
    
    def _generate_recommendations(
        self,
        session: QuestioningSession
    ) -> List[str]:
        """Generate development recommendations based on responses."""
        recommendations = []
        
        # Analyze confidence levels
        avg_confidence = sum(r.confidence for r in session.responses) / len(session.responses) if session.responses else 0
        
        if avg_confidence < 0.7:
            recommendations.append("Consider additional planning phase due to low confidence in requirements")
        
        # Analyze response patterns
        detailed_count = sum(1 for r in session.responses if len(r.answer) > 50)
        if detailed_count > len(session.responses) * 0.7:
            recommendations.append("User provided detailed requirements - consider iterative development approach")
        
        return recommendations
    
    def _identify_low_confidence_areas(
        self,
        session: QuestioningSession
    ) -> List[str]:
        """Identify areas where user expressed low confidence."""
        low_confidence_areas = []
        
        for response in session.responses:
            if response.confidence < 0.6:
                question = self._find_question_by_id(session.questions, response.question_id)
                if question:
                    low_confidence_areas.append(question.text)
        
        return low_confidence_areas
    
    def _identify_high_confidence_areas(
        self,
        session: QuestioningSession
    ) -> List[str]:
        """Identify areas where user expressed high confidence."""
        high_confidence_areas = []
        
        for response in session.responses:
            if response.confidence > 0.8:
                question = self._find_question_by_id(session.questions, response.question_id)
                if question:
                    high_confidence_areas.append(question.text)
        
        return high_confidence_areas
