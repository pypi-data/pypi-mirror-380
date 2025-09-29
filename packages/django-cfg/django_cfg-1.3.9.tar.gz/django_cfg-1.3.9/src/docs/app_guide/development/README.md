# 🔧 Development Guide %%PRIORITY:HIGH%%

## 🎯 Quick Summary
- **Development workflow** and tools for Django-CFG applications
- **Testing strategies** with comprehensive framework coverage
- **Dependency management** with Poetry and version strategies
- **Best practices** for efficient Django-CFG development

## 📋 Table of Contents
1. [Development Workflow](development-workflow.md) - CLI tools, commands, and development process
2. [Poetry Dependencies](poetry-dependencies.md) - Dependency management and version strategies
3. [Code Organization](code-organization.md) - File decomposition, LLM-friendly naming, and structure patterns

## 🔑 Key Concepts at a Glance
- **CLI Automation**: Click-based CLI with automatic project setup
- **Management Commands**: 20+ built-in commands for debugging and administration
- **Testing Framework**: Django TestCase-based testing with comprehensive patterns
- **Poetry Management**: Modern dependency management with conservative versioning
- **Quality Gates**: Coverage, linting, and performance requirements
- **Code Organization**: 500-line file limit with smart decomposition strategies
- **LLM-Friendly Code**: Self-documenting names and logical structure patterns

## 🚀 Quick Start

### Project Creation
```bash
# Create new Django-CFG project
django-cfg create-project "My Project"

# Install dependencies
poetry install --with dev,test

# Run development server
python manage.py runserver_ngrok 8000
```

### Testing
```bash
# Run all tests
python manage.py test

# Run with coverage
coverage run --source='.' manage.py test
coverage report --fail-under=95
```

### Dependency Management
```bash
# Add new dependency
poetry add requests

# Add development dependency
poetry add --group dev pytest

# Update dependencies
poetry update
```

## 🏷️ Metadata
**Tags**: `development, workflow, testing, poetry, dependencies, django-cfg`
**Status**: %%ACTIVE%%
**Complexity**: %%MODERATE%%
**USED_BY**: [developers, qa-engineers, devops]
