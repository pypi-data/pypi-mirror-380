"""
Prompt management for the App Generator Agent.

This module handles all AI prompts for different Django features
and provides intelligent prompt generation based on requirements.
"""

from .models import FileGenerationRequest
from ....models.enums import AppFeature


class PromptManager:
    """Manages AI prompts for different Django features."""
    
    def get_system_prompt(self) -> str:
        """Get the system prompt for the AI agent."""
        return """You are an expert Django developer with deep knowledge of Django best practices, 
design patterns, and modern Python development.

Your task is to generate high-quality Django application files based on user requirements.

Guidelines:
1. Follow Django best practices and conventions
2. Use proper Python type hints
3. Include comprehensive docstrings
4. Add appropriate error handling
5. Follow PEP 8 style guidelines
6. Use modern Django features (Django 5.x)
7. Include proper imports and dependencies
8. Generate production-ready code
9. Add meaningful comments where needed
10. Consider security best practices

For django-cfg applications, also:
- Use django-cfg patterns and conventions
- Leverage django-cfg modules when appropriate
- Follow the infrastructural layer approach
- Use proper configuration management

Always generate complete, working code that can be used immediately."""

    def create_feature_prompt(self, request: FileGenerationRequest) -> str:
        """Create a detailed prompt for generating a specific feature."""
        feature_prompts = {
            AppFeature.MODELS: self._get_models_prompt(request),
            AppFeature.VIEWS: self._get_views_prompt(request),
            AppFeature.ADMIN: self._get_admin_prompt(request),
            AppFeature.URLS: self._get_urls_prompt(request),
            AppFeature.FORMS: self._get_forms_prompt(request),
            AppFeature.API: self._get_api_prompt(request),
            AppFeature.TESTS: self._get_tests_prompt(request),
            AppFeature.TASKS: self._get_tasks_prompt(request),
            AppFeature.SIGNALS: self._get_signals_prompt(request),
        }
        
        return feature_prompts.get(request.feature, self._get_generic_prompt(request))
    
    def _get_models_prompt(self, request: FileGenerationRequest) -> str:
        """Get prompt for generating models.py."""
        return f"""Generate a Django models.py file for the '{request.app_name}' application.

Application Details:
- Name: {request.app_name}
- Description: {request.description}
- Type: {request.app_type.value}
- Complexity: {request.complexity.value}

Requirements:
1. Create relevant models based on the application description
2. Use appropriate field types and relationships
3. Include proper Meta classes with ordering, verbose names
4. Add __str__ methods for all models
5. Use abstract base models where appropriate
6. Include created_at/updated_at timestamps
7. Add proper model validation
8. Include relevant indexes for performance
9. Use proper related_name for relationships
10. Add comprehensive docstrings

For django-cfg apps, also consider:
- Using django-cfg base models if appropriate
- Following django-cfg naming conventions
- Including proper configuration fields

Generate complete, production-ready models with proper imports."""

    def _get_views_prompt(self, request: FileGenerationRequest) -> str:
        """Get prompt for generating views.py."""
        return f"""Generate a Django views.py file for the '{request.app_name}' application.

Application Details:
- Name: {request.app_name}
- Description: {request.description}
- Type: {request.app_type.value}
- Complexity: {request.complexity.value}

Requirements:
1. Create appropriate view classes/functions based on the app purpose
2. Use class-based views where appropriate
3. Include proper permission checks
4. Add error handling and validation
5. Use proper HTTP status codes
6. Include pagination for list views
7. Add proper context data
8. Use Django's built-in mixins
9. Include proper docstrings
10. Add type hints

Generate complete, secure views with proper imports and error handling."""

    def _get_admin_prompt(self, request: FileGenerationRequest) -> str:
        """Get prompt for generating admin.py."""
        return f"""Generate a Django admin.py file for the '{request.app_name}' application.

Application Details:
- Name: {request.app_name}
- Description: {request.description}
- Type: {request.app_type.value}
- Complexity: {request.complexity.value}

Requirements:
1. Register all models with appropriate admin classes
2. Configure list_display, list_filter, search_fields
3. Add proper fieldsets for complex models
4. Include inline admin for related models
5. Add custom admin actions where useful
6. Use proper admin permissions
7. Include admin-specific methods
8. Add proper docstrings
9. Configure admin ordering and pagination
10. Add custom admin templates if needed

Generate a complete admin configuration with good UX."""

    def _get_urls_prompt(self, request: FileGenerationRequest) -> str:
        """Get prompt for generating urls.py."""
        return f"""Generate a Django urls.py file for the '{request.app_name}' application.

Application Details:
- Name: {request.app_name}
- Description: {request.description}
- Type: {request.app_type.value}
- Complexity: {request.complexity.value}

Requirements:
1. Create appropriate URL patterns for the application
2. Use proper URL naming conventions
3. Include namespace for the app
4. Add URL patterns for all major views
5. Use path() instead of url() (modern Django)
6. Include proper parameter types in URLs
7. Add API endpoints if this is an API app
8. Consider SEO-friendly URLs
9. Include proper docstrings
10. Group related URLs logically

Generate complete URL configuration with proper imports."""

    def _get_forms_prompt(self, request: FileGenerationRequest) -> str:
        """Get prompt for generating forms.py."""
        return f"""Generate a Django forms.py file for the '{request.app_name}' application.

Application Details:
- Name: {request.app_name}
- Description: {request.description}
- Type: {request.app_type.value}
- Complexity: {request.complexity.value}

Requirements:
1. Create ModelForm classes for main models
2. Add proper field validation
3. Include custom clean methods
4. Use appropriate widgets
5. Add form styling classes
6. Include proper error messages
7. Add form helpers if using crispy forms
8. Include proper docstrings
9. Add custom form fields if needed
10. Consider accessibility

Generate complete, user-friendly forms with proper validation."""

    def _get_api_prompt(self, request: FileGenerationRequest) -> str:
        """Get prompt for generating API files (serializers.py)."""
        return f"""Generate Django REST Framework serializers.py for the '{request.app_name}' application.

Application Details:
- Name: {request.app_name}
- Description: {request.description}
- Type: {request.app_type.value}
- Complexity: {request.complexity.value}

Requirements:
1. Create ModelSerializer classes for main models
2. Include proper field validation
3. Add custom serializer methods
4. Use nested serializers for relationships
5. Include proper read-only fields
6. Add custom create/update methods
7. Include proper docstrings
8. Add API versioning considerations
9. Use proper field representations
10. Include permission-aware serialization

Generate complete REST API serializers with proper validation."""

    def _get_tests_prompt(self, request: FileGenerationRequest) -> str:
        """Get prompt for generating tests.py."""
        return f"""Generate comprehensive Django tests.py for the '{request.app_name}' application.

Application Details:
- Name: {request.app_name}
- Description: {request.description}
- Type: {request.app_type.value}
- Complexity: {request.complexity.value}

Requirements:
1. Create test classes for models, views, forms
2. Use Django's TestCase and test client
3. Include proper test data setup
4. Test all major functionality
5. Add negative test cases
6. Test permissions and security
7. Include API tests if applicable
8. Use proper assertions
9. Add performance tests for complex operations
10. Include integration tests

Generate comprehensive test coverage with proper test organization."""

    def _get_tasks_prompt(self, request: FileGenerationRequest) -> str:
        """Get prompt for generating tasks.py (Celery/background tasks)."""
        return f"""Generate Django tasks.py for background processing in the '{request.app_name}' application.

Application Details:
- Name: {request.app_name}
- Description: {request.description}
- Type: {request.app_type.value}
- Complexity: {request.complexity.value}

Requirements:
1. Create Celery tasks for background processing
2. Include proper error handling and retries
3. Add task monitoring and logging
4. Use proper task signatures
5. Include task result handling
6. Add periodic tasks if needed
7. Include proper docstrings
8. Add task progress tracking
9. Use proper task queues
10. Include task testing utilities

Generate production-ready background tasks with proper error handling."""

    def _get_signals_prompt(self, request: FileGenerationRequest) -> str:
        """Get prompt for generating signals.py."""
        return f"""Generate Django signals.py for the '{request.app_name}' application.

Application Details:
- Name: {request.app_name}
- Description: {request.description}
- Type: {request.app_type.value}
- Complexity: {request.complexity.value}

Requirements:
1. Create appropriate signal handlers
2. Use proper signal decorators
3. Include error handling in signals
4. Add proper logging
5. Consider signal performance impact
6. Include proper docstrings
7. Use weak references where appropriate
8. Add signal testing
9. Consider signal ordering
10. Include proper cleanup

Generate efficient signal handlers with proper error handling."""

    def _get_generic_prompt(self, request: FileGenerationRequest) -> str:
        """Get generic prompt for other features."""
        return f"""Generate a Django file for the '{request.feature.value}' feature in the '{request.app_name}' application.

Application Details:
- Name: {request.app_name}
- Description: {request.description}
- Feature: {request.feature.value}
- Type: {request.app_type.value}
- Complexity: {request.complexity.value}

Generate appropriate, production-ready code following Django best practices."""
