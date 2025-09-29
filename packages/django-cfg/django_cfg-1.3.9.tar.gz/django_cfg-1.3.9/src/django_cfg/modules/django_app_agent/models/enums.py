"""
Enumerations for Django App Agent Module.

This module defines all enums used throughout the system:
- Application features and types
- Generation stages and complexity levels
- Question types and impact levels
- Validation severities and statuses
"""

from enum import Enum, IntEnum
from typing import List, Set


class AppFeature(str, Enum):
    """Features that can be included in generated Django applications."""
    
    # Core Django features
    MODELS = "models"
    VIEWS = "views"
    URLS = "urls"
    ADMIN = "admin"
    FORMS = "forms"
    TEMPLATES = "templates"
    STATIC = "static"
    
    # API and serialization
    API = "api"
    SERIALIZERS = "serializers"
    VIEWSETS = "viewsets"
    FILTERS = "filters"
    PAGINATION = "pagination"
    
    # Testing and quality
    TESTS = "tests"
    FIXTURES = "fixtures"
    
    # Background processing
    TASKS = "tasks"
    SIGNALS = "signals"
    
    # Security and permissions
    SECURITY = "security"
    PERMISSIONS = "permissions"
    AUTHENTICATION = "authentication"
    
    # Configuration and management
    CONFIG = "config"
    MANAGEMENT_COMMANDS = "management_commands"
    MIDDLEWARE = "middleware"
    CONTEXT_PROCESSORS = "context_processors"
    
    # Database and migrations
    MIGRATIONS = "migrations"
    ROUTERS = "routers"
    
    # Documentation and development
    DOCS = "docs"
    SERVICES = "services"  # Service layer pattern
    
    # Django-CFG specific
    CFG_CONFIG = "cfg_config"
    CFG_MODULES = "cfg_modules"
    
    @classmethod
    def get_core_features(cls) -> Set["AppFeature"]:
        """Get core features that are typically included."""
        return {cls.MODELS, cls.VIEWS, cls.ADMIN, cls.URLS}
    
    @classmethod
    def get_advanced_features(cls) -> Set["AppFeature"]:
        """Get advanced features for complex applications."""
        return {
            cls.API, cls.SERIALIZERS, cls.VIEWSETS, cls.TESTS, cls.FORMS, 
            cls.SIGNALS, cls.MANAGEMENT_COMMANDS, cls.PERMISSIONS, cls.MIDDLEWARE,
            cls.TASKS, cls.SECURITY, cls.AUTHENTICATION, cls.SERVICES
        }
    
    @classmethod
    def get_ui_features(cls) -> Set["AppFeature"]:
        """Get UI-related features."""
        return {cls.TEMPLATES, cls.STATIC, cls.FORMS}
    
    @classmethod
    def get_api_features(cls) -> Set["AppFeature"]:
        """Get API-related features."""
        return {cls.API, cls.SERIALIZERS, cls.VIEWSETS, cls.FILTERS, cls.PAGINATION}
    
    @classmethod
    def get_django_cfg_features(cls) -> Set["AppFeature"]:
        """Get django-cfg specific features."""
        return {cls.CFG_CONFIG, cls.CFG_MODULES, cls.CONFIG, cls.SERVICES}
    
    def get_dependencies(self) -> Set["AppFeature"]:
        """Get features that this feature depends on."""
        dependencies = {
            # API features depend on models and views
            self.API: {self.MODELS, self.VIEWS},
            self.SERIALIZERS: {self.MODELS},
            self.VIEWSETS: {self.MODELS, self.VIEWS, self.SERIALIZERS},
            self.FILTERS: {self.MODELS, self.API},
            self.PAGINATION: {self.API},
            
            # Admin and forms depend on models
            self.ADMIN: {self.MODELS},
            self.FORMS: {self.MODELS},
            
            # Testing depends on models
            self.TESTS: {self.MODELS},
            
            # Signals and permissions depend on models
            self.SIGNALS: {self.MODELS},
            self.PERMISSIONS: {self.MODELS},
            self.AUTHENTICATION: {self.MODELS, self.PERMISSIONS},
            
            # Security depends on authentication and permissions
            self.SECURITY: {self.AUTHENTICATION, self.PERMISSIONS},
            
            # Tasks may depend on models
            self.TASKS: {self.MODELS},
            
            # Services depend on models
            self.SERVICES: {self.MODELS},
            
            # Django-CFG features
            self.CFG_MODULES: {self.CFG_CONFIG},
        }
        return dependencies.get(self, set())
    
    def supports_app_type(self, app_type: 'AppType') -> bool:
        """Check if this feature is supported by the given app type."""
        if app_type == AppType.DJANGO:
            # Django supports all features except django-cfg specific ones
            django_cfg_only = {self.CFG_CONFIG, self.CFG_MODULES}
            return self not in django_cfg_only
        elif app_type == AppType.DJANGO_CFG:
            # Django-CFG supports all features
            return True
        return False


class AppComplexity(str, Enum):
    """Complexity levels for application generation."""
    
    SIMPLE = "simple"
    MODERATE = "moderate"
    ADVANCED = "advanced"
    ENTERPRISE = "enterprise"
    
    def get_recommended_features(self) -> Set[AppFeature]:
        """Get recommended features for this complexity level."""
        feature_sets = {
            self.SIMPLE: {
                AppFeature.MODELS,
                AppFeature.VIEWS,
                AppFeature.URLS
            },
            self.MODERATE: {
                AppFeature.MODELS,
                AppFeature.VIEWS,
                AppFeature.ADMIN,
                AppFeature.URLS,
                AppFeature.TESTS,
                AppFeature.FORMS
            },
            self.ADVANCED: {
                AppFeature.MODELS,
                AppFeature.VIEWS,
                AppFeature.ADMIN,
                AppFeature.API,
                AppFeature.SERIALIZERS,
                AppFeature.TESTS,
                AppFeature.FORMS,
                AppFeature.URLS,
                AppFeature.TEMPLATES,
                AppFeature.SIGNALS,
                AppFeature.PERMISSIONS
            },
            self.ENTERPRISE: {
                AppFeature.MODELS,
                AppFeature.VIEWS,
                AppFeature.ADMIN,
                AppFeature.API,
                AppFeature.SERIALIZERS,
                AppFeature.VIEWSETS,
                AppFeature.FILTERS,
                AppFeature.PAGINATION,
                AppFeature.TESTS,
                AppFeature.FORMS,
                AppFeature.URLS,
                AppFeature.TEMPLATES,
                AppFeature.SIGNALS,
                AppFeature.PERMISSIONS,
                AppFeature.AUTHENTICATION,
                AppFeature.SECURITY,
                AppFeature.MANAGEMENT_COMMANDS,
                AppFeature.MIDDLEWARE,
                AppFeature.TASKS,
                AppFeature.SERVICES,
                AppFeature.DOCS
            }
        }
        return feature_sets.get(self, set())
    
    def get_estimated_time_minutes(self) -> int:
        """Get estimated generation time in minutes."""
        time_estimates = {
            self.SIMPLE: 2,
            self.MODERATE: 5,
            self.ADVANCED: 8,
            self.ENTERPRISE: 12
        }
        return time_estimates.get(self, 5)
    
    def get_max_questions(self) -> int:
        """Get maximum number of questions for this complexity."""
        question_limits = {
            self.SIMPLE: 5,
            self.MODERATE: 10,
            self.ADVANCED: 15,
            self.ENTERPRISE: 20
        }
        return question_limits.get(self, 10)


class AppType(str, Enum):
    """Types of Django applications that can be generated."""
    
    DJANGO = "django"
    DJANGO_CFG = "django_cfg"
    
    def get_base_patterns(self) -> Set[str]:
        """Get base architectural patterns for this app type."""
        patterns = {
            self.DJANGO: {
                "class_based_views",
                "model_forms",
                "django_admin"
            },
            self.DJANGO_CFG: {
                "service_layer",
                "pydantic_models",
                "async_views",
                "type_safety"
            }
        }
        return patterns.get(self, set())
    
    def supports_feature(self, feature: AppFeature) -> bool:
        """Check if this app type supports a specific feature."""
        # Django-CFG supports all features
        if self == self.DJANGO_CFG:
            return True
        
        # Standard Django has some limitations
        unsupported_for_django = {
            # All features are supported in standard Django
        }
        return feature not in unsupported_for_django


class QuestionType(str, Enum):
    """Types of questions in the intelligent questioning system."""
    
    YES_NO = "yes_no"
    MULTIPLE_CHOICE = "multiple_choice"
    TEXT_INPUT = "text_input"
    NUMERIC_INPUT = "numeric_input"
    SELECTION = "selection"
    RANKING = "ranking"
    
    def get_validation_pattern(self) -> str:
        """Get validation pattern for this question type."""
        patterns = {
            self.YES_NO: r"^(yes|no|y|n)$",
            self.NUMERIC_INPUT: r"^\d+(\.\d+)?$",
            self.TEXT_INPUT: r"^.{1,500}$",  # 1-500 characters
        }
        return patterns.get(self, r"^.*$")
    
    def requires_options(self) -> bool:
        """Check if this question type requires predefined options."""
        return self in {self.MULTIPLE_CHOICE, self.SELECTION, self.RANKING}


class ImpactLevel(str, Enum):
    """Impact levels for questions and decisions."""
    
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"
    
    def get_priority_score(self) -> int:
        """Get numeric priority score for sorting."""
        scores = {
            self.LOW: 1,
            self.MEDIUM: 2,
            self.HIGH: 3,
            self.CRITICAL: 4
        }
        return scores.get(self, 1)
    
    def should_ask_early(self) -> bool:
        """Check if questions with this impact should be asked early."""
        return self in {self.HIGH, self.CRITICAL}


class GenerationStage(str, Enum):
    """Stages in the application generation process."""
    
    INITIALIZATION = "initialization"
    ANALYSIS = "analysis"
    QUESTIONING = "questioning"
    PLANNING = "planning"
    GENERATION = "generation"
    VALIDATION = "validation"
    INTEGRATION = "integration"
    FINALIZATION = "finalization"
    COMPLETED = "completed"
    FAILED = "failed"
    
    def get_next_stage(self) -> "GenerationStage":
        """Get the next stage in the process."""
        stage_order = [
            self.INITIALIZATION,
            self.ANALYSIS,
            self.QUESTIONING,
            self.PLANNING,
            self.GENERATION,
            self.VALIDATION,
            self.INTEGRATION,
            self.FINALIZATION,
            self.COMPLETED
        ]
        
        try:
            current_index = stage_order.index(self)
            if current_index < len(stage_order) - 1:
                return stage_order[current_index + 1]
        except ValueError:
            pass
        
        return self.COMPLETED
    
    def is_terminal(self) -> bool:
        """Check if this is a terminal stage."""
        return self in {self.COMPLETED, self.FAILED}
    
    def get_progress_percentage(self) -> float:
        """Get progress percentage for this stage."""
        progress_map = {
            self.INITIALIZATION: 5.0,
            self.ANALYSIS: 15.0,
            self.QUESTIONING: 25.0,
            self.PLANNING: 35.0,
            self.GENERATION: 70.0,
            self.VALIDATION: 85.0,
            self.INTEGRATION: 95.0,
            self.FINALIZATION: 98.0,
            self.COMPLETED: 100.0,
            self.FAILED: 0.0
        }
        return progress_map.get(self, 0.0)


class ValidationSeverity(str, Enum):
    """Severity levels for validation issues."""
    
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"
    
    def is_blocking(self) -> bool:
        """Check if this severity level blocks generation."""
        return self in {self.ERROR, self.CRITICAL}
    
    def get_priority(self) -> int:
        """Get numeric priority for sorting (higher = more severe)."""
        priorities = {
            self.INFO: 1,
            self.WARNING: 2,
            self.ERROR: 3,
            self.CRITICAL: 4
        }
        return priorities.get(self, 1)


class AgentRole(str, Enum):
    """Roles for different AI agents in the system."""
    
    ORCHESTRATOR = "orchestrator"
    ANALYZER = "analyzer"
    GENERATOR = "generator"
    VALIDATOR = "validator"
    DIALOGUE = "dialogue"
    DIAGNOSTIC = "diagnostic"
    
    def get_description(self) -> str:
        """Get human-readable description of the agent role."""
        descriptions = {
            self.ORCHESTRATOR: "Coordinates and manages the overall generation process",
            self.ANALYZER: "Analyzes project structure and identifies patterns",
            self.GENERATOR: "Generates application code and files",
            self.VALIDATOR: "Validates generated code quality and compliance",
            self.DIALOGUE: "Conducts intelligent questioning sessions",
            self.DIAGNOSTIC: "Diagnoses problems and suggests solutions"
        }
        return descriptions.get(self, "Unknown agent role")
    
    def get_required_capabilities(self) -> Set[str]:
        """Get required capabilities for this agent role."""
        capabilities = {
            self.ORCHESTRATOR: {"workflow_management", "agent_coordination"},
            self.ANALYZER: {"code_analysis", "pattern_recognition"},
            self.GENERATOR: {"code_generation", "template_processing"},
            self.VALIDATOR: {"code_validation", "quality_assessment"},
            self.DIALOGUE: {"natural_language", "question_generation"},
            self.DIAGNOSTIC: {"problem_analysis", "solution_generation"}
        }
        return capabilities.get(self, set())


class FileType(str, Enum):
    """Types of files that can be generated."""
    
    MODEL = "model"
    VIEW = "view"
    FORM = "form"
    ADMIN = "admin"
    URL = "url"
    TEST = "test"
    TEMPLATE = "template"
    STATIC = "static"
    MIGRATION = "migration"
    MANAGEMENT = "management"
    SIGNAL = "signal"
    MIDDLEWARE = "middleware"
    CONFIG = "config"
    INIT = "init"
    
    def get_file_extension(self) -> str:
        """Get typical file extension for this file type."""
        extensions = {
            self.MODEL: ".py",
            self.VIEW: ".py",
            self.FORM: ".py",
            self.ADMIN: ".py",
            self.URL: ".py",
            self.TEST: ".py",
            self.TEMPLATE: ".html",
            self.STATIC: ".css",
            self.MIGRATION: ".py",
            self.MANAGEMENT: ".py",
            self.SIGNAL: ".py",
            self.MIDDLEWARE: ".py",
            self.CONFIG: ".py",
            self.INIT: ".py"
        }
        return extensions.get(self, ".py")
    
    def get_typical_directory(self) -> str:
        """Get typical directory for this file type."""
        directories = {
            self.MODEL: "models",
            self.VIEW: "views",
            self.FORM: "forms",
            self.ADMIN: "",  # Root of app
            self.URL: "",   # Root of app
            self.TEST: "tests",
            self.TEMPLATE: "templates",
            self.STATIC: "static",
            self.MIGRATION: "migrations",
            self.MANAGEMENT: "management/commands",
            self.SIGNAL: "signals",
            self.MIDDLEWARE: "middleware",
            self.CONFIG: "",
            self.INIT: ""
        }
        return directories.get(self, "")
