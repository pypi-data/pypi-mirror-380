"""
Django management command for Django App Agent information.

This command provides information about the Django App Agent module,
its capabilities, configuration, and available commands.
"""

import sys
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

try:
    from django_cfg.modules.django_app_agent.core.config import AgentConfig
    from django_cfg.modules.django_app_agent.utils.logging import get_logger
    from django_cfg.modules.django_app_agent.models.enums import AppFeature, AppComplexity, AppType
    from django_cfg.modules.django_app_agent import __version__
except ImportError as e:
    print(f"Error importing django_app_agent module: {e}")
    print("Make sure the django_app_agent module is properly installed.")
    sys.exit(1)


class Command(BaseCommand):
    """Django management command for Django App Agent information."""
    
    help = "Show information about Django App Agent module and its capabilities"
    
    def add_arguments(self, parser):
        """Add command line arguments."""
        
        parser.add_argument(
            '--features',
            action='store_true',
            help='Show available application features'
        )
        
        parser.add_argument(
            '--config',
            action='store_true',
            help='Show current configuration'
        )
        
        parser.add_argument(
            '--commands',
            action='store_true',
            help='Show available app_agent commands'
        )
        
        parser.add_argument(
            '--examples',
            action='store_true',
            help='Show usage examples'
        )
        
        parser.add_argument(
            '--all',
            action='store_true',
            help='Show all information'
        )
    
    def handle(self, *args, **options):
        """Handle the command execution."""
        
        try:
            # Show header
            self._show_header()
            
            # Determine what to show
            show_all = options.get('all', False)
            
            if show_all or not any([
                options.get('features'),
                options.get('config'),
                options.get('commands'),
                options.get('examples')
            ]):
                # Show everything if no specific options or --all
                self._show_overview()
                self._show_features()
                self._show_commands()
                self._show_config()
                self._show_examples()
            else:
                # Show specific sections
                if options.get('features') or show_all:
                    self._show_features()
                
                if options.get('config') or show_all:
                    self._show_config()
                
                if options.get('commands') or show_all:
                    self._show_commands()
                
                if options.get('examples') or show_all:
                    self._show_examples()
            
            # Show footer
            self._show_footer()
            
        except Exception as e:
            raise CommandError(f"Failed to show information: {e}")
    
    def _show_header(self):
        """Show header information."""
        self.stdout.write(
            self.style.SUCCESS("🤖 Django App Agent - AI-Powered Application Generation")
        )
        self.stdout.write("=" * 70)
        
        try:
            version = __version__
        except:
            version = "Unknown"
        
        self.stdout.write(f"Version: {version}")
        self.stdout.write(f"Project: {getattr(settings, 'BASE_DIR', 'Unknown')}")
        self.stdout.write("")
    
    def _show_overview(self):
        """Show module overview."""
        self.stdout.write(self.style.HTTP_INFO("📋 Overview"))
        self.stdout.write("-" * 20)
        
        overview = """
Django App Agent is an AI-powered module for generating Django applications
with intelligent questioning, context analysis, and code generation capabilities.

Key Features:
• 🎯 Interactive AI-driven app generation
• 🧠 Intelligent questioning system
• 🏗️ Multiple application types (Django, Django-CFG)
• 📊 Quality validation and reporting
• 🎨 Rich terminal interface
• 🔧 Extensible architecture with agent isolation

The module supports 25+ application features and can generate everything
from simple CRUD apps to complex enterprise applications with APIs,
authentication, and advanced functionality.
        """
        
        self.stdout.write(overview.strip())
        self.stdout.write("")
    
    def _show_features(self):
        """Show available application features."""
        self.stdout.write(self.style.HTTP_INFO("🎯 Available Application Features"))
        self.stdout.write("-" * 40)
        
        # Group features by category
        feature_groups = {
            "Core Django": [
                AppFeature.MODELS, AppFeature.VIEWS, AppFeature.URLS,
                AppFeature.ADMIN, AppFeature.FORMS, AppFeature.TEMPLATES, AppFeature.STATIC
            ],
            "API & Serialization": [
                AppFeature.API, AppFeature.SERIALIZERS, AppFeature.VIEWSETS,
                AppFeature.FILTERS, AppFeature.PAGINATION
            ],
            "Testing & Quality": [
                AppFeature.TESTS, AppFeature.FIXTURES
            ],
            "Background Processing": [
                AppFeature.TASKS, AppFeature.SIGNALS
            ],
            "Security & Auth": [
                AppFeature.SECURITY, AppFeature.AUTHENTICATION, AppFeature.PERMISSIONS
            ],
            "Configuration & Management": [
                AppFeature.CONFIG, AppFeature.MANAGEMENT_COMMANDS,
                AppFeature.MIDDLEWARE, AppFeature.CONTEXT_PROCESSORS
            ],
            "Database": [
                AppFeature.MIGRATIONS, AppFeature.ROUTERS
            ],
            "Documentation": [
                AppFeature.DOCS, AppFeature.SERVICES
            ],
            "Django-CFG Specific": [
                AppFeature.CFG_CONFIG, AppFeature.CFG_MODULES
            ]
        }
        
        for group_name, features in feature_groups.items():
            self.stdout.write(f"\n{group_name}:")
            for feature in features:
                self.stdout.write(f"  • {feature.value}")
        
        self.stdout.write(f"\nTotal: {len(list(AppFeature))} features available")
        self.stdout.write("")
    
    def _show_commands(self):
        """Show available app_agent commands."""
        self.stdout.write(self.style.HTTP_INFO("💻 Available Commands"))
        self.stdout.write("-" * 25)
        
        commands = [
            {
                'name': 'app_agent_generate',
                'description': 'Generate Django applications with AI assistance',
                'usage': 'python manage.py app_agent_generate [app_name] [description] [options]'
            },
            {
                'name': 'app_agent_diagnose',
                'description': 'Diagnose problems in Django/Django-cfg projects',
                'usage': 'python manage.py app_agent_diagnose [options]'
            },
            {
                'name': 'app_agent_info',
                'description': 'Show information about Django App Agent (this command)',
                'usage': 'python manage.py app_agent_info [options]'
            }
        ]
        
        for cmd in commands:
            self.stdout.write(f"\n🔧 {cmd['name']}")
            self.stdout.write(f"   {cmd['description']}")
            self.stdout.write(f"   Usage: {cmd['usage']}")
        
        self.stdout.write("")
    
    def _show_config(self):
        """Show current configuration."""
        self.stdout.write(self.style.HTTP_INFO("⚙️ Configuration"))
        self.stdout.write("-" * 20)
        
        try:
            config = AgentConfig()
            
            self.stdout.write("Configuration Status: ✅ Loaded")
            
            # Show complexity levels
            self.stdout.write(f"\nComplexity Levels:")
            for complexity in AppComplexity:
                features = complexity.get_recommended_features()
                time_est = complexity.get_estimated_time_minutes()
                max_questions = complexity.get_max_questions()
                
                self.stdout.write(f"  • {complexity.value}:")
                self.stdout.write(f"    - Features: {len(features)}")
                self.stdout.write(f"    - Est. time: {time_est} minutes")
                self.stdout.write(f"    - Max questions: {max_questions}")
            
            # Show app types
            self.stdout.write(f"\nApplication Types:")
            for app_type in AppType:
                self.stdout.write(f"  • {app_type.value}")
            
        except Exception as e:
            self.stdout.write(f"Configuration Status: ❌ Error loading config: {e}")
        
        self.stdout.write("")
    
    def _show_examples(self):
        """Show usage examples."""
        self.stdout.write(self.style.HTTP_INFO("📚 Usage Examples"))
        self.stdout.write("-" * 25)
        
        examples = [
            {
                'title': 'Interactive Generation (Recommended)',
                'command': 'python manage.py app_agent_generate',
                'description': 'Start interactive mode with AI questioning'
            },
            {
                'title': 'Quick Blog App',
                'command': 'python manage.py app_agent_generate blog "A simple blog application"',
                'description': 'Generate a blog app with default settings'
            },
            {
                'title': 'E-commerce with Specific Features',
                'command': 'python manage.py app_agent_generate shop "E-commerce shop" --features models,admin,api,tests --complexity advanced',
                'description': 'Generate advanced e-commerce app with specific features'
            },
            {
                'title': 'Django-CFG Module',
                'command': 'python manage.py app_agent_generate analytics "Analytics module" --app-type django_cfg --complexity enterprise',
                'description': 'Generate enterprise-level django-cfg module'
            },
            {
                'title': 'Project Diagnosis',
                'command': 'python manage.py app_agent_diagnose',
                'description': 'Interactive diagnosis of project issues'
            },
            {
                'title': 'Specific App Diagnosis',
                'command': 'python manage.py app_agent_diagnose --app users --category auth --description "Login issues"',
                'description': 'Diagnose authentication issues in users app'
            }
        ]
        
        for example in examples:
            self.stdout.write(f"\n📝 {example['title']}")
            self.stdout.write(f"   Command: {example['command']}")
            self.stdout.write(f"   Description: {example['description']}")
        
        self.stdout.write("")
    
    def _show_footer(self):
        """Show footer information."""
        self.stdout.write("=" * 70)
        self.stdout.write("For more information:")
        self.stdout.write("• Documentation: https://docs.django-cfg.com/app-agent/")
        self.stdout.write("• Help: python manage.py app_agent_generate --help")
        self.stdout.write("• Help: python manage.py app_agent_diagnose --help")
        self.stdout.write("")
        self.stdout.write("🚀 Ready to generate amazing Django applications with AI!")
