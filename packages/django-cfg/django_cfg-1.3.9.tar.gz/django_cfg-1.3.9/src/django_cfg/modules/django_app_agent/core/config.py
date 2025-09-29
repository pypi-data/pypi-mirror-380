"""
Configuration management for Django App Agent Module.

This module provides type-safe configuration management with:
- Integration with django-cfg BaseCfgModule
- Pydantic 2 models for all configuration
- Environment variable support
- Validation and default values
- AI model configuration
"""

from typing import Optional, Dict, Any, List, Literal
from pathlib import Path
from pydantic import BaseModel, Field, ConfigDict, field_validator
from enum import Enum

from django_cfg.modules.base import BaseCfgModule
from .exceptions import ConfigurationError


class LogLevel(str, Enum):
    """Logging levels."""
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


class AIProvider(str, Enum):
    """AI service providers."""
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    OPENROUTER = "openrouter"


class ModelTier(str, Enum):
    """AI model performance tiers."""
    FAST = "fast"        # Fast, cheaper models for simple tasks
    BALANCED = "balanced"  # Balanced performance and cost
    PREMIUM = "premium"   # Best quality, higher cost


class ModelConfig(BaseModel):
    """Configuration for AI models."""
    
    model_config = ConfigDict(
        extra='forbid',
        validate_assignment=True,
        str_strip_whitespace=True
    )
    
    provider: AIProvider = Field(description="AI service provider")
    model_id: str = Field(description="Model identifier")
    tier: ModelTier = Field(description="Model performance tier")
    max_tokens: int = Field(gt=0, le=200000, description="Maximum tokens per request")
    temperature: float = Field(ge=0.0, le=2.0, default=0.1, description="Model temperature")
    timeout_seconds: float = Field(gt=0, default=300.0, description="Request timeout")
    
    @field_validator('model_id')
    @classmethod
    def validate_model_id(cls, v: str) -> str:
        """Validate model ID format."""
        if not v or len(v.strip()) == 0:
            raise ValueError("Model ID cannot be empty")
        return v.strip()


class APIKeyConfig(BaseModel):
    """API key configuration."""
    
    model_config = ConfigDict(
        extra='forbid',
        validate_assignment=True,
        str_strip_whitespace=True
    )
    
    openai: Optional[str] = Field(default=None, description="OpenAI API key")
    anthropic: Optional[str] = Field(default=None, description="Anthropic API key")
    openrouter: Optional[str] = Field(default=None, description="OpenRouter API key")
    
    def get_key(self, provider: AIProvider) -> Optional[str]:
        """Get API key for provider."""
        return getattr(self, provider.value, None)
    
    def has_key(self, provider: AIProvider) -> bool:
        """Check if API key exists for provider."""
        key = self.get_key(provider)
        return key is not None and len(key.strip()) > 0


class UIConfig(BaseModel):
    """User interface configuration."""
    
    model_config = ConfigDict(
        extra='forbid',
        validate_assignment=True
    )
    
    enable_rich_interface: bool = Field(default=True, description="Enable Rich CLI interface")
    show_progress_bars: bool = Field(default=True, description="Show progress bars")
    enable_colors: bool = Field(default=True, description="Enable colored output")
    verbose_output: bool = Field(default=False, description="Enable verbose output")
    max_console_width: int = Field(gt=40, le=200, default=120, description="Maximum console width")


class GenerationConfig(BaseModel):
    """Code generation configuration."""
    
    model_config = ConfigDict(
        extra='forbid',
        validate_assignment=True
    )
    
    max_questions: int = Field(gt=0, le=50, default=20, description="Maximum questions to ask")
    questioning_timeout_minutes: int = Field(gt=0, le=60, default=15, description="Questioning timeout")
    quality_threshold: float = Field(ge=0.0, le=10.0, default=8.0, description="Minimum quality score")
    enable_caching: bool = Field(default=True, description="Enable response caching")
    cache_ttl_seconds: int = Field(gt=0, default=3600, description="Cache TTL in seconds")
    max_concurrent_generations: int = Field(gt=0, le=10, default=3, description="Max concurrent generations")
    
    @field_validator('quality_threshold')
    @classmethod
    def validate_quality_threshold(cls, v: float) -> float:
        """Validate quality threshold is reasonable."""
        if v < 5.0:
            raise ValueError("Quality threshold should be at least 5.0 for production use")
        return v


class AgentConfig(BaseModel):
    """Django App Agent Module configuration."""
    
    model_config = ConfigDict(
        extra='forbid',
        validate_assignment=True,
        str_strip_whitespace=True
    )
    
    # Core settings
    module_name: str = Field(default="django_app_agent", description="Module name")
    version: str = Field(default="0.1.0", description="Module version")
    debug_mode: bool = Field(default=False, description="Enable debug mode")
    log_level: LogLevel = Field(default=LogLevel.INFO, description="Logging level")
    
    # API configuration
    api_keys: APIKeyConfig = Field(default_factory=APIKeyConfig, description="API keys")
    preferred_models: Dict[str, ModelConfig] = Field(
        default_factory=dict,
        description="Preferred models for different tasks"
    )
    
    # UI configuration
    ui: UIConfig = Field(default_factory=UIConfig, description="UI settings")
    
    # Generation configuration
    generation: GenerationConfig = Field(default_factory=GenerationConfig, description="Generation settings")
    
    # File paths
    output_directory: Optional[Path] = Field(default=None, description="Default output directory")
    template_directory: Optional[Path] = Field(default=None, description="Template directory")
    cache_directory: Optional[Path] = Field(default=None, description="Cache directory")
    
    @classmethod
    def from_django_cfg(cls) -> "AgentConfig":
        """Load configuration from django-cfg."""
        try:
            cfg_module = BaseCfgModule()
            django_cfg_config = cfg_module.get_config()
            
            # Extract relevant configuration
            config_data: Dict[str, Any] = {}
            
            # API keys - extract string values from SecretStr
            if hasattr(django_cfg_config, 'api_keys'):
                api_keys_data = {}
                if hasattr(django_cfg_config.api_keys, 'openai') and django_cfg_config.api_keys.openai:
                    # Extract string value from SecretStr if needed
                    openai_key = django_cfg_config.api_keys.openai
                    api_keys_data['openai'] = str(openai_key) if hasattr(openai_key, 'get_secret_value') else openai_key
                if hasattr(django_cfg_config.api_keys, 'anthropic') and django_cfg_config.api_keys.anthropic:
                    # Extract string value from SecretStr if needed
                    anthropic_key = django_cfg_config.api_keys.anthropic
                    api_keys_data['anthropic'] = str(anthropic_key) if hasattr(anthropic_key, 'get_secret_value') else anthropic_key
                if hasattr(django_cfg_config.api_keys, 'openrouter') and django_cfg_config.api_keys.openrouter:
                    # Extract string value from SecretStr if needed
                    openrouter_key = django_cfg_config.api_keys.openrouter
                    api_keys_data['openrouter'] = str(openrouter_key) if hasattr(openrouter_key, 'get_secret_value') else openrouter_key
                
                config_data['api_keys'] = api_keys_data
            
            # Agent-specific settings
            if hasattr(django_cfg_config, 'agents') and django_cfg_config.agents:
                agent_config = django_cfg_config.agents
                
                if hasattr(agent_config, 'debug_mode'):
                    config_data['debug_mode'] = agent_config.debug_mode
                
                if hasattr(agent_config, 'max_questions'):
                    config_data['generation'] = config_data.get('generation', {})
                    config_data['generation']['max_questions'] = agent_config.max_questions
                
                if hasattr(agent_config, 'quality_threshold'):
                    config_data['generation'] = config_data.get('generation', {})
                    config_data['generation']['quality_threshold'] = agent_config.quality_threshold
            
            return cls(**config_data)
            
        except Exception as e:
            raise ConfigurationError(
                f"Failed to load configuration from django-cfg: {e}",
                cause=e
            )
    
    def get_api_key(self, provider: AIProvider) -> Optional[str]:
        """Get API key for provider."""
        return self.api_keys.get_key(provider)
    
    def has_api_key(self, provider: AIProvider) -> bool:
        """Check if API key exists for provider."""
        return self.api_keys.has_key(provider)
    
    def get_model_config(self, task_type: str) -> Optional[ModelConfig]:
        """Get model configuration for task type."""
        return self.preferred_models.get(task_type)
    
    def validate_configuration(self) -> List[str]:
        """Validate configuration and return list of issues."""
        issues: List[str] = []
        
        # Check API keys
        if not any(self.api_keys.has_key(provider) for provider in AIProvider):
            issues.append("No API keys configured for any AI provider")
        
        # Check directories
        if self.output_directory and not self.output_directory.exists():
            issues.append(f"Output directory does not exist: {self.output_directory}")
        
        if self.template_directory and not self.template_directory.exists():
            issues.append(f"Template directory does not exist: {self.template_directory}")
        
        # Check model configurations
        for task_type, model_config in self.preferred_models.items():
            if not self.has_api_key(model_config.provider):
                issues.append(f"No API key for {model_config.provider} (required for {task_type})")
        
        return issues


# Default model configurations
DEFAULT_MODELS: Dict[str, ModelConfig] = {
    "generation": ModelConfig(
        provider=AIProvider.OPENROUTER,
        model_id="anthropic/claude-3-haiku",
        tier=ModelTier.BALANCED,
        max_tokens=100000,
        temperature=0.1,
        timeout_seconds=300.0
    ),
    "analysis": ModelConfig(
        provider=AIProvider.OPENROUTER,
        model_id="openai/gpt-4o-mini",
        tier=ModelTier.FAST,
        max_tokens=50000,
        temperature=0.0,
        timeout_seconds=180.0
    ),
    "validation": ModelConfig(
        provider=AIProvider.OPENROUTER,
        model_id="anthropic/claude-3-haiku",
        tier=ModelTier.FAST,
        max_tokens=30000,
        temperature=0.0,
        timeout_seconds=120.0
    ),
    "dialogue": ModelConfig(
        provider=AIProvider.OPENROUTER,
        model_id="openai/gpt-4o-mini",
        tier=ModelTier.FAST,
        max_tokens=20000,
        temperature=0.2,
        timeout_seconds=60.0
    )
}


def get_default_config() -> AgentConfig:
    """Get default configuration with sensible defaults."""
    return AgentConfig(
        preferred_models=DEFAULT_MODELS.copy()
    )


def load_config() -> AgentConfig:
    """Load configuration from django-cfg or use defaults."""
    try:
        return AgentConfig.from_django_cfg()
    except ConfigurationError:
        # Fall back to default configuration
        return get_default_config()
