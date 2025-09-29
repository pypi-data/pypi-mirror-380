# 🧪 Django-CFG Testing Framework Guide

## 🎯 Quick Summary
- **🚨 CRITICAL: Business logic only** - Don't test `__str__`, verbose_name, Django framework
- **Django TestCase-based testing** with comprehensive test organization
- **App-specific testing** patterns for focused development
- **Real test examples** from django-cfg apps (agents, accounts, knowbase, payments)
- **Dramatiq mocking patterns** for background task testing
- **Type-safe testing** with Pydantic models and proper validation
- **🚨 CRITICAL: One test class per file** - Never accumulate multiple test classes in one file
- **File size limits**: 400 lines per test file, 150 lines per test class
- **No inline imports**: All imports at the top of test files
- **Database isolation**: Always specify `databases = ['default']` for multi-database projects
- **🚨 CRITICAL**: New apps MUST be registered in `tests/settings.py` → `project_apps` list

## 🚀 Quick Start

```bash
# 🚀 RECOMMENDED: Use the standard test runner (KISS principle)
cd /path/to/django-cfg
poetry run python run_tests.py

# Alternative: Run specific app tests
cd /path/to/django-cfg/src
poetry run python -m django test django_cfg.apps.payments.tests --settings=tests.settings
```

**Why use `run_tests.py`?**
- ✅ Simple one-command solution
- ✅ Automatic test discovery for all Django-CFG apps
- ✅ Correct settings by default (no database routing issues)
- ✅ Proper Django setup and teardown
- ✅ Follows KISS principle (Keep It Simple, Stupid)

## 📋 Documentation Structure

### 🎯 Core Philosophy & Concepts
- [Code-First Testing Philosophy](./code-first-philosophy.md) - Tests follow actual implementation, not assumptions
- [Key Concepts](./key-concepts.md) - Essential testing principles at a glance

### 🚀 Practical Testing Implementation
- [App-Specific Testing](./app-specific-testing.md) - Test individual apps independently
- [Testing Architecture](./testing-architecture.md) - System design and configuration for testing
- [Real Test Examples](./real-examples.md) - Working examples from Django-CFG apps
- [Django-CFG Testing Checklist](./django-cfg-testing-checklist.md) - Complete checklist for developers

### 🎭 Advanced Testing Patterns
- [Test Organization Patterns](./test-organization-patterns.md) - Factory and Mixin patterns
- [Testing Best Practices](./testing-best-practices.md) - Do's, Don'ts, and anti-patterns
- [Dramatiq Testing](./dramatiq-testing.md) - Background task testing patterns
- [Performance & Quality Gates](./performance-quality.md) - SLA validation and CI/CD integration
- [Universal Testing Principles](./universal-principles.md) - Documentation and maintenance principles

## ⚡ Quick Start Commands
```bash
# 🚨 FIRST: Register your app in tests/settings.py!
# Add "django_cfg.apps.your_new_app" to project_apps list

# 🚀 RECOMMENDED: Use standard test runner
cd /path/to/django-cfg
poetry run python run_tests.py

# Test entire payments app
cd /path/to/django-cfg/src
poetry run python -m django test django_cfg.apps.payments.tests \
    --settings=tests.settings \
    --verbosity=2

# Test specific module
poetry run python -m django test django_cfg.apps.payments.tests.test_services \
    --settings=tests.settings \
    --verbosity=2

# Non-interactive testing (prevents hanging)
poetry run python -m django test django_cfg.apps.payments.tests \
    --settings=tests.settings \
    --verbosity=1 \
    --keepdb \
    --parallel auto \
    --noinput

# Test with coverage
coverage run --source='src/django_cfg/apps/payments' \
    -m django test django_cfg.apps.payments.tests \
    --settings=tests.settings

coverage report --show-missing
```

## 🔑 Key Principle
**CRITICAL**: Tests must be written based on actual implementation, not assumptions.

```python
# ❌ WRONG: Assuming method names
result = MyService.get_payment_by_id("123")  # Method doesn't exist!

# ✅ RIGHT: Using actual method names
result = MyService.get_payment_details("123")  # Actual method
```

**Tags**: `testing, django, quality-assurance, coverage, performance, django-cfg`
