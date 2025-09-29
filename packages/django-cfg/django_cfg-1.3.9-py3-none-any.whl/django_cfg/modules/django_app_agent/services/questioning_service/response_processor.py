"""
Response Processor for Intelligent Questioning Service.

This module handles processing user responses and building
refined generation requests based on the collected answers.
"""

from typing import List, Dict, Any, Optional, Set
from datetime import datetime, timezone

from pydantic import BaseModel, Field

from ...core.config import AgentConfig
from ...models.requests import AppGenerationRequest
from ...models.enums import AppType, AppComplexity, AppFeature
from ...models.context import ProjectContext
from ..base import ServiceDependencies
from .models import QuestioningSession, QuestionResponse, ContextualQuestion


class ResponseProcessor(BaseModel):
    """Processes user responses and builds refined generation requests."""
    
    config: AgentConfig = Field(description="Agent configuration")
    
    # Response interpretation rules
    feature_keywords: Dict[str, List[str]] = Field(
        default_factory=lambda: {
            "authentication": ["auth", "login", "user", "account", "permission"],
            "api": ["api", "rest", "endpoint", "integration", "external"],
            "admin": ["admin", "management", "backend", "dashboard"],
            "forms": ["form", "input", "validation", "submit"],
            "tests": ["test", "testing", "quality", "coverage"],
            "security": ["security", "secure", "protection", "safe"],
            "models": ["data", "database", "model", "entity"],
            "views": ["view", "page", "display", "interface"],
            "serializers": ["serialize", "json", "api", "data format"],
            "tasks": ["background", "async", "queue", "job", "task"]
        },
        description="Keywords for inferring features from responses"
    )

    async def process_responses(
        self,
        session: QuestioningSession,
        dependencies: ServiceDependencies
    ) -> AppGenerationRequest:
        """Process all responses and build refined generation request."""
        dependencies.log_operation(
            "Processing questioning responses",
            session_id=session.session_id,
            responses_count=len(session.responses),
            questions_count=len(session.questions)
        )
        
        try:
            # Extract insights from responses
            insights = await self._extract_insights(session, dependencies)
            
            # Build refined request
            refined_request = await self._build_refined_request(
                session, insights, dependencies
            )
            
            dependencies.log_operation(
                "Response processing completed",
                app_name=refined_request.app_name,
                app_type=refined_request.app_type.value,
                features_count=len(refined_request.features),
                complexity=refined_request.complexity.value
            )
            
            return refined_request
            
        except Exception as e:
            dependencies.log_error("Response processing failed", e)
            raise
    
    async def _extract_insights(
        self,
        session: QuestioningSession,
        dependencies: ServiceDependencies
    ) -> Dict[str, Any]:
        """Extract structured insights from user responses."""
        insights = {
            "inferred_features": set(),
            "app_characteristics": {},
            "user_preferences": {},
            "technical_requirements": {},
            "business_requirements": {},
            "confidence_indicators": []
        }
        
        # Process each response
        for response in session.responses:
            question = self._find_question_by_id(session.questions, response.question_id)
            if not question:
                continue
            
            # Extract feature implications
            features = self._infer_features_from_response(question, response)
            insights["inferred_features"].update(features)
            
            # Extract characteristics
            characteristics = self._extract_characteristics(question, response)
            insights["app_characteristics"].update(characteristics)
            
            # Track confidence
            insights["confidence_indicators"].append({
                "question_id": response.question_id,
                "confidence": response.confidence,
                "impact_level": question.impact_level
            })
        
        return insights
    
    async def _build_refined_request(
        self,
        session: QuestioningSession,
        insights: Dict[str, Any],
        dependencies: ServiceDependencies
    ) -> AppGenerationRequest:
        """Build refined generation request from insights."""
        # Start with original request if available
        base_request = session.project_context.generation_request
        
        # Determine app name
        app_name = self._determine_app_name(session, insights, base_request)
        
        # Determine app type
        app_type = self._determine_app_type(session, insights, base_request)
        
        # Determine complexity
        complexity = self._determine_complexity(session, insights, base_request)
        
        # Determine features
        features = self._determine_features(session, insights, base_request)
        
        # Build description
        description = self._build_description(session, insights, base_request)
        
        # Determine output directory
        output_dir = base_request.output_dir if base_request else str(session.project_context.project_root)
        
        refined_request = AppGenerationRequest(
            app_name=app_name,
            description=description,
            app_type=app_type,
            complexity=complexity,
            features=list(features),
            output_dir=output_dir,
            max_questions=0,  # No more questions needed
            quality_threshold=base_request.quality_threshold if base_request else 8.0
        )
        
        return refined_request
    
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
    
    def _infer_features_from_response(
        self,
        question: ContextualQuestion,
        response: QuestionResponse
    ) -> Set[AppFeature]:
        """Infer required features from a response."""
        features = set()
        answer_lower = response.answer.lower()
        
        # Check for feature keywords in the answer
        for feature_name, keywords in self.feature_keywords.items():
            if any(keyword in answer_lower for keyword in keywords):
                try:
                    feature = AppFeature(feature_name.upper())
                    features.add(feature)
                except ValueError:
                    # Feature name doesn't match enum
                    pass
        
        # Question-specific feature inference
        if question.question_type == "yes_no":
            if response.answer.lower() in ["yes", "y", "true", "1"]:
                # Infer features based on question content
                question_lower = question.text.lower()
                
                if "auth" in question_lower or "login" in question_lower:
                    features.add(AppFeature.AUTHENTICATION)
                elif "api" in question_lower:
                    features.add(AppFeature.API)
                    features.add(AppFeature.SERIALIZERS)
                elif "admin" in question_lower:
                    features.add(AppFeature.ADMIN)
                elif "form" in question_lower:
                    features.add(AppFeature.FORMS)
                elif "test" in question_lower:
                    features.add(AppFeature.TESTS)
        
        return features
    
    def _extract_characteristics(
        self,
        question: ContextualQuestion,
        response: QuestionResponse
    ) -> Dict[str, Any]:
        """Extract app characteristics from response."""
        characteristics = {}
        
        # Extract based on question type and content
        question_lower = question.text.lower()
        answer_lower = response.answer.lower()
        
        if "purpose" in question_lower or "what" in question_lower:
            characteristics["primary_purpose"] = response.answer
        
        if "data" in question_lower:
            characteristics["data_type"] = response.answer
        
        if "user" in question_lower and "how many" in question_lower:
            characteristics["expected_users"] = response.answer
        
        if "performance" in question_lower or "scale" in question_lower:
            characteristics["performance_requirements"] = response.answer
        
        return characteristics
    
    def _determine_app_name(
        self,
        session: QuestioningSession,
        insights: Dict[str, Any],
        base_request: Optional[AppGenerationRequest]
    ) -> str:
        """Determine application name."""
        if base_request and base_request.app_name:
            return base_request.app_name
        
        # Try to extract from user intent or responses
        intent_words = session.user_intent.lower().split()
        
        # Look for app-like words
        app_words = [word for word in intent_words if len(word) > 3 and word.isalpha()]
        
        if app_words:
            return "_".join(app_words[:2])  # Take first 2 meaningful words
        
        return "generated_app"
    
    def _determine_app_type(
        self,
        session: QuestioningSession,
        insights: Dict[str, Any],
        base_request: Optional[AppGenerationRequest]
    ) -> AppType:
        """Determine application type."""
        if base_request and base_request.app_type:
            return base_request.app_type
        
        # Check if django-cfg features are mentioned
        django_cfg_indicators = ["config", "module", "django-cfg", "cfg"]
        
        for response in session.responses:
            if any(indicator in response.answer.lower() for indicator in django_cfg_indicators):
                return AppType.DJANGO_CFG
        
        return AppType.DJANGO
    
    def _determine_complexity(
        self,
        session: QuestioningSession,
        insights: Dict[str, Any],
        base_request: Optional[AppGenerationRequest]
    ) -> AppComplexity:
        """Determine application complexity."""
        if base_request and base_request.complexity:
            return base_request.complexity
        
        feature_count = len(insights["inferred_features"])
        
        # Determine complexity based on features and responses
        complexity_indicators = {
            "enterprise": ["enterprise", "large scale", "complex", "advanced"],
            "intermediate": ["medium", "moderate", "standard", "typical"],
            "simple": ["simple", "basic", "minimal", "small"]
        }
        
        # Check responses for complexity indicators
        for response in session.responses:
            answer_lower = response.answer.lower()
            for complexity, indicators in complexity_indicators.items():
                if any(indicator in answer_lower for indicator in indicators):
                    try:
                        return AppComplexity(complexity.upper())
                    except ValueError:
                        pass
        
        # Fallback based on feature count
        if feature_count >= 8:
            return AppComplexity.ENTERPRISE
        elif feature_count >= 5:
            return AppComplexity.INTERMEDIATE
        else:
            return AppComplexity.SIMPLE
    
    def _determine_features(
        self,
        session: QuestioningSession,
        insights: Dict[str, Any],
        base_request: Optional[AppGenerationRequest]
    ) -> Set[AppFeature]:
        """Determine required features."""
        features = set(insights["inferred_features"])
        
        # Add base features if available
        if base_request and base_request.features:
            features.update(base_request.features)
        
        # Ensure core features are included
        core_features = {AppFeature.MODELS, AppFeature.VIEWS, AppFeature.URLS}
        features.update(core_features)
        
        return features
    
    def _build_description(
        self,
        session: QuestioningSession,
        insights: Dict[str, Any],
        base_request: Optional[AppGenerationRequest]
    ) -> str:
        """Build application description."""
        if base_request and base_request.description:
            return base_request.description
        
        # Build description from user intent and characteristics
        description_parts = [session.user_intent]
        
        if "primary_purpose" in insights["app_characteristics"]:
            purpose = insights["app_characteristics"]["primary_purpose"]
            description_parts.append(f"Primary purpose: {purpose}")
        
        return ". ".join(description_parts)
