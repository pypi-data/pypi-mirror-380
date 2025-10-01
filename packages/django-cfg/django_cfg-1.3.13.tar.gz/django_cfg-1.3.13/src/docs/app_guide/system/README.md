# ⚙️ System Architecture Guide %%PRIORITY:HIGH%%

## 🎯 Quick Summary
- **System-level components** and infrastructure patterns
- **Registry system** for organized component imports
- **Event-driven architecture** with Django signals
- **Background processing** with Dramatiq integration
- **Caching strategies** and middleware patterns

## 📋 Table of Contents
1. [Registry System](registry-system.md) - Component organization and import patterns
2. [Django Signals](signals.md) - Event-driven processing and signal patterns
3. [Background Tasks](background-tasks.md) - Dramatiq integration and task patterns
4. [Caching System](caching.md) - Multi-level caching with Redis and memory backends
5. [Middleware](middleware.md) - Django middleware patterns and integration

## 🔑 Key Concepts at a Glance
- **Registry System**: Centralized component organization with 80+ registered components
- **Event-Driven Processing**: Django signals for model lifecycle management
- **Background Processing**: Dramatiq with Redis for scalable task execution
- **Multi-Level Caching**: Redis, memory, and database caching strategies
- **Middleware Integration**: Request/response processing and feature activation

## 🚀 Quick Start

### Registry Usage
```python
# Import framework components from registry
from django_cfg import DjangoConfig, get_logger, DjangoTelegram

# App-specific components via direct import
from myapp.services import MyAppService
```

### Signal Implementation
```python
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=MyModel)
def handle_model_change(sender, instance, created, **kwargs):
    if created:
        # Process new instance
        pass
```

### Background Tasks
```python
import dramatiq

@dramatiq.actor(queue_name="myapp")
def process_data(data_id):
    # Background processing
    pass
```

### Caching
```python
from django.core.cache import cache

# Cache with TTL
cache.set("key", value, timeout=3600)
result = cache.get("key")
```

## 🏷️ Metadata
**Tags**: `system, architecture, registry, signals, tasks, caching, middleware`
**Status**: %%ACTIVE%%
**Complexity**: %%HIGH%%
**USED_BY**: [system-architects, senior-developers, infrastructure-teams]
