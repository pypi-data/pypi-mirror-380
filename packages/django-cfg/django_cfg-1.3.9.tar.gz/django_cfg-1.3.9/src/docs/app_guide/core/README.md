# 🏗️ Django-CFG Core System %%PRIORITY:HIGH%%

## 🎯 Quick Summary
- Core DjangoConfig class for type-safe configuration management
- Environment detection and smart defaults
- Automatic Django settings generation
- Integration system with startup display

## 📋 Table of Contents
1. [DjangoConfig Class](djangoconfig.md)
2. [Environment Detection](environment.md)
3. [Settings Generation](generation.md)
4. [Integration System](integration.md)

## 🔑 Key Concepts at a Glance
- **DjangoConfig**: Main configuration class inheriting from Pydantic BaseModel
- **Environment Modes**: DEVELOPMENT, PRODUCTION, TEST with auto-detection
- **Settings Generator**: Converts Pydantic config to Django settings dict
- **Integration Display**: Rich startup information with configurable modes

## 🚀 Quick Start
```python
from django_cfg import DjangoConfig
from django_cfg.models import DatabaseConfig, CacheConfig

class MyProjectConfig(DjangoConfig):
    project_name: str = "My Project"
    secret_key: str = "your-secret-key"
    
    # Database configuration
    databases: Dict[str, DatabaseConfig] = {
        "default": DatabaseConfig(
            engine="django.db.backends.postgresql",
            name="mydb",
            user="postgres",
            password="password",
            host="localhost",
            port=5432
        )
    }
    
    # Cache configuration
    cache_default: CacheConfig = CacheConfig(
        redis_url="redis://localhost:6379/0"
    )

config = MyProjectConfig()
```

## 🏷️ Metadata
**Tags**: `core, config, environment, generation`
**Status**: %%ACTIVE%%
**Complexity**: %%MODERATE%%
**Max Lines**: 400 (this file: 50 lines)
**DEPENDS_ON**: [pydantic, django]
**USED_BY**: [all-django-cfg-projects]

---

## 📁 Core Components

### DjangoConfig Class
The main configuration class that all projects inherit from. Provides:
- Type-safe configuration with Pydantic 2
- Environment-aware smart defaults
- Automatic validation and error handling
- Django settings generation

### Environment Detection
Automatic detection of development, production, and test environments:
- Environment variables (DJANGO_ENV, ENV)
- Domain patterns (localhost = dev, staging.* = staging)
- Debug settings (DEBUG=True = dev)

### Settings Generation
Converts Pydantic configuration to Django settings dictionary:
- Database configuration
- Cache configuration
- Middleware stack
- Installed apps
- Security settings

### Integration System
Rich startup information display:
- Configurable display modes (NONE, SHORT, FULL)
- Apps and endpoints overview
- System health status
- Management commands
- Update notifications

---

Navigate to specific components for detailed documentation and examples.
