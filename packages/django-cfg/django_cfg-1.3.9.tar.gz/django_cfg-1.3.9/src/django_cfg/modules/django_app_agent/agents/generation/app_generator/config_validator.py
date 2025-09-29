"""
Configuration validation for the App Generator Agent.

This module handles API key validation and model configuration
using django-cfg integration.
"""

import os
from typing import Optional

from pydantic_ai.models.openai import OpenAIModel

from ....core.config import AgentConfig, AIProvider
from ....core.exceptions import ConfigurationError


class ConfigValidator:
    """Validates and configures API keys and AI models."""
    
    def __init__(self):
        """Initialize the config validator."""
        self.model: Optional[OpenAIModel] = None
    
    def validate_and_configure(self, config) -> OpenAIModel:
        """
        Validate API keys and configure AI model.
        
        Args:
            config: Configuration object (AgentConfig or other)
            
        Returns:
            Configured OpenAI model
            
        Raises:
            ConfigurationError: If no valid API keys found
        """
        try:
            # Get configuration from django-cfg
            print(f"🔍 Debug config type: {type(config)}")
            print(f"🔍 Debug config: {config}")
            
            if isinstance(config, AgentConfig):
                # Use provided AgentConfig
                agent_config = config
                print("✅ Using provided AgentConfig")
            else:
                # Load from django-cfg
                print("🔄 Loading from django-cfg...")
                agent_config = AgentConfig.from_django_cfg()
                print(f"✅ Loaded AgentConfig: {type(agent_config)}")
            
            print(f"🔍 AgentConfig attributes: {dir(agent_config)}")
            
            # Get API keys from configuration
            openai_key = self._get_api_key(agent_config, AIProvider.OPENAI)
            openrouter_key = self._get_api_key(agent_config, AIProvider.OPENROUTER)
            
            print(f"🔍 API keys via get_api_key: OpenAI={bool(openai_key)}, OpenRouter={bool(openrouter_key)}")
            
            # Fallback to direct access
            if not openai_key and not openrouter_key:
                openai_key, openrouter_key = self._get_keys_direct_access(agent_config)
            
            # Debug: Print what we found
            print(f"🔍 Final API Keys from django-cfg:")
            print(f"  OpenAI: {'✅ Found' if openai_key else '❌ Missing'}")
            print(f"  OpenRouter: {'✅ Found' if openrouter_key else '❌ Missing'}")
            
            if not openai_key and not openrouter_key:
                raise ConfigurationError(
                    "❌ AI Agent Configuration Error: No API keys found in django-cfg!\n\n"
                    "🔑 Required: Either OpenAI or OpenRouter API key must be configured.\n\n"
                    "📝 How to fix in django-cfg config:\n"
                    "   api_keys:\n"
                    "     openai: 'your-openai-key'\n"
                    "     openrouter: 'your-openrouter-key'\n\n"
                    "🚀 Without API keys, AI agents cannot generate intelligent code!\n"
                    "   You'll only get basic template-based generation.",
                    config_key="api_keys"
                )
            
            # Configure and return the model
            return self._configure_model(openai_key, openrouter_key)
                
        except Exception as e:
            print(f"❌ Error loading API keys from django-cfg: {e}")
            raise ConfigurationError(
                f"Failed to load API keys from django-cfg configuration: {e}\n\n"
                "🔧 Make sure django-cfg is properly configured with API keys.",
                config_key="api_keys",
                cause=e
            )
    
    def _get_api_key(self, agent_config: AgentConfig, provider: AIProvider) -> Optional[str]:
        """Get API key for specific provider."""
        if hasattr(agent_config, 'get_api_key'):
            return agent_config.get_api_key(provider)
        return None
    
    def _get_keys_direct_access(self, agent_config: AgentConfig) -> tuple[Optional[str], Optional[str]]:
        """Get API keys via direct access as fallback."""
        openai_key = None
        openrouter_key = None
        
        print("🔄 Trying direct access to api_keys...")
        if hasattr(agent_config, 'api_keys') and agent_config.api_keys:
            print(f"🔍 api_keys type: {type(agent_config.api_keys)}")
            print(f"🔍 api_keys content: {agent_config.api_keys}")
            
            if hasattr(agent_config.api_keys, 'get'):
                openai_key = agent_config.api_keys.get('openai', '')
                openrouter_key = agent_config.api_keys.get('openrouter', '')
            else:
                openai_key = getattr(agent_config.api_keys, 'openai', '')
                openrouter_key = getattr(agent_config.api_keys, 'openrouter', '')
            
            print(f"🔍 Direct access results: OpenAI={bool(openai_key)}, OpenRouter={bool(openrouter_key)}")
        
        return openai_key, openrouter_key
    
    def _configure_model(self, openai_key: Optional[str], openrouter_key: Optional[str]) -> OpenAIModel:
        """Configure AI model with available API key."""
        if openrouter_key:
            print("🚀 Using OpenRouter API via django-cfg")
            print(f"🔍 OpenRouter key length: {len(openrouter_key)}")
            print(f"🔍 OpenRouter key prefix: {openrouter_key[:20]}...")
            
            # Set environment variables for OpenRouter
            os.environ['OPENAI_API_KEY'] = openrouter_key
            os.environ['OPENAI_BASE_URL'] = 'https://openrouter.ai/api/v1'
            # OpenRouter требует специальные заголовки
            os.environ['OPENAI_DEFAULT_HEADERS'] = '{"HTTP-Referer": "https://djangocfg.com", "X-Title": "Django CFG App Agent"}'
            
            self.model = OpenAIModel('gpt-4o-mini')
            
        elif openai_key:
            print("🚀 Using OpenAI API via django-cfg")
            
            # Set environment variable for OpenAI
            os.environ['OPENAI_API_KEY'] = openai_key
            # Remove base URL for standard OpenAI
            if 'OPENAI_BASE_URL' in os.environ:
                del os.environ['OPENAI_BASE_URL']
            
            self.model = OpenAIModel('gpt-4o-mini')
        
        return self.model
