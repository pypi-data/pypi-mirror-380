"""
Django management command for AI-powered app generation.

This command serves as a thin wrapper that:
1. Loads django-cfg configuration
2. Delegates to django_app_agent module
3. Provides Django-native CLI interface
"""

import asyncio
import sys
from pathlib import Path
from typing import List, Optional

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

try:
    from django_cfg.modules.django_app_agent.services.base import create_service_dependencies
    from django_cfg.modules.django_app_agent.ui.cli import DjangoAppAgentCLI
    from django_cfg.modules.django_app_agent.models.requests import (
        AppGenerationRequest,
        AppFeature,
        AppComplexity,
        AppType
    )
    from django_cfg.modules.django_app_agent.models.enums import AppFeature as AppFeatureEnum
    from django_cfg.modules.django_app_agent.core.exceptions import DjangoAppAgentError
    from django_cfg.modules.django_app_agent.core.config import AgentConfig
    from django_cfg.modules.django_app_agent.utils.logging import get_logger
except ImportError as e:
    print(f"Error importing django_app_agent module: {e}")
    print("Make sure the django_app_agent module is properly installed.")
    sys.exit(1)


class Command(BaseCommand):
    """Django management command for AI-powered app generation."""
    
    help = "Generate Django applications using AI assistance (Django App Agent)"
    
    def add_arguments(self, parser):
        """Add command line arguments."""
        
        # Positional arguments
        parser.add_argument(
            'app_name',
            nargs='?',
            type=str,
            help='Name of the application to generate'
        )
        
        parser.add_argument(
            'description',
            nargs='?',
            type=str,
            help='Description of the application'
        )
        
        # Optional arguments
        parser.add_argument(
            '--features',
            type=str,
            help='Comma-separated list of features (e.g., models,admin,views,api,tests)'
        )
        
        parser.add_argument(
            '--complexity',
            choices=['simple', 'moderate', 'advanced', 'enterprise'],
            default='moderate',
            help='Application complexity level (default: moderate)'
        )
        
        parser.add_argument(
            '--app-type',
            choices=['django', 'django_cfg'],
            default='django_cfg',
            help='Type of application to generate (default: django_cfg)'
        )
        
        parser.add_argument(
            '--output-dir',
            type=str,
            help='Custom output directory for the application'
        )
        
        parser.add_argument(
            '--max-questions',
            type=int,
            default=20,
            help='Maximum number of interactive questions (default: 20)'
        )
        
        parser.add_argument(
            '--no-questions',
            action='store_true',
            help='Skip interactive questioning'
        )
        
        parser.add_argument(
            '--interactive',
            action='store_true',
            default=True,
            help='Enable interactive mode (default: True)'
        )
        
        parser.add_argument(
            '--non-interactive',
            action='store_true',
            help='Disable interactive mode'
        )
        
        parser.add_argument(
            '--quality-threshold',
            type=float,
            default=0.8,
            help='Quality threshold for generated code (0.0-1.0, default: 0.8)'
        )
        
        parser.add_argument(
            '--model',
            type=str,
            help='Specific AI model to use (e.g., gpt-4o, claude-3-5-sonnet)'
        )
        
        parser.add_argument(
            '--verbose',
            action='store_true',
            help='Enable verbose output'
        )
    
    def handle(self, *args, **options):
        """Handle the command execution."""
        
        try:
            # Initialize logger
            logger = get_logger("management.commands.generate_app")
            
            # Determine interactive mode
            interactive = options.get('interactive', True) and not options.get('non_interactive', False)
            if options.get('no_questions'):
                interactive = False
            
            # If no arguments provided and interactive mode, use CLI
            if not options.get('app_name') and interactive:
                self.stdout.write(
                    self.style.SUCCESS("🚀 Starting Django App Agent CLI...")
                )
                return self._run_interactive_cli(options)
            
            # Validate required arguments for non-interactive mode
            if not options.get('app_name'):
                raise CommandError("app_name is required when not in interactive mode")
            
            if not options.get('description'):
                raise CommandError("description is required when not in interactive mode")
            
            # Parse features
            features = []
            if options.get('features'):
                feature_names = [f.strip() for f in options['features'].split(',')]
                for feature_name in feature_names:
                    try:
                        features.append(AppFeatureEnum(feature_name.lower()))
                    except ValueError:
                        self.stdout.write(
                            self.style.WARNING(f"Unknown feature: {feature_name}")
                        )
            
            # Create generation request
            request = AppGenerationRequest(
                app_name=options['app_name'],
                description=options['description'],
                app_type=AppType(options.get('app_type', 'django_cfg')),
                complexity=AppComplexity(options.get('complexity', 'moderate')),
                features=features,
                output_directory=options.get('output_dir'),
                max_questions=options.get('max_questions', 20),
                rich_interface=interactive,
                verbose_output=options.get('verbose', False)
            )
            
            # Run generation
            return self._run_generation(request, options)
            
        except DjangoAppAgentError as e:
            logger.error(f"App generation failed: {e}")
            raise CommandError(f"App generation failed: {e}")
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise CommandError(f"Unexpected error: {e}")
    
    def _run_interactive_cli(self, options):
        """Run the interactive CLI interface."""
        try:
            # Initialize CLI
            cli = DjangoAppAgentCLI()
            
            # Run async CLI
            if sys.platform == 'win32':
                asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
            
            result = asyncio.run(cli.run_interactive())
            
            if result and result.status == "success":
                self.stdout.write(
                    self.style.SUCCESS(
                        f"✅ Application '{result.app_name}' generated successfully!"
                    )
                )
                self.stdout.write(f"Generated {len(result.generated_files)} files")
                if result.report_path:
                    self.stdout.write(f"Report saved to: {result.report_path}")
            else:
                self.stdout.write(
                    self.style.ERROR("❌ Application generation failed")
                )
                if result and result.errors:
                    for error in result.errors:
                        self.stdout.write(f"  • {error}")
                        
        except KeyboardInterrupt:
            self.stdout.write("\n🛑 Generation cancelled by user")
        except Exception as e:
            raise CommandError(f"CLI execution failed: {e}")
    
    def _run_generation(self, request: AppGenerationRequest, options):
        """Run the generation process."""
        try:
            # Initialize configuration from django-cfg
            config = AgentConfig.from_django_cfg()
            logger = get_logger("management.commands.generate_app")
            
            # Import and initialize services
            from django_cfg.modules.django_app_agent.services import AppGeneratorService
            from django_cfg.modules.django_app_agent.agents import AgentRegistry, AgentClientFactory
            
            # Set up agent registry
            registry = AgentRegistry()
            
            # For now, we'll use a placeholder since actual agents aren't implemented yet
            # In production, this would initialize real agents
            local_client = {}  # AgentClientFactory.create_local_client(agents, config, logger)
            # Note: Using placeholder since actual agents aren't implemented yet
            # registry.register_agent("local", local_client, "client")
            
            # Initialize service
            service = AppGeneratorService(config)
            
            # Create service dependencies
            
            dependencies = create_service_dependencies(
                config=config,
                service_name="app_generator",
                project_root=Path.cwd(),
                output_directory=Path.cwd() / "apps"
            )
            
            # Show progress
            self.stdout.write(f"🔧 Generating application '{request.app_name}'...")
            self.stdout.write(f"   Type: {request.app_type.value}")
            self.stdout.write(f"   Complexity: {request.complexity.value}")
            self.stdout.write(f"   Features: {', '.join([f.value for f in request.features])}")
            
            # Run generation (async)
            if sys.platform == 'win32':
                asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
            
            result = asyncio.run(service.process(request, dependencies))
            
            # Display results
            if result.success:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"✅ Application '{request.app_name}' generated successfully!"
                    )
                )
                self.stdout.write(f"Generated {len(result.generated_files)} files")
                
                if options.get('verbose'):
                    self.stdout.write("\n📁 Generated files:")
                    for file in result.generated_files:
                        self.stdout.write(f"  • {file.relative_path}")
                
                if result.generation_report_path:
                    self.stdout.write(f"📊 Report saved to: {result.generation_report_path}")
                    
                self.stdout.write(f"📈 Quality score: {result.quality_score:.2f}")
                self.stdout.write(f"🔒 Type safety: {result.type_safety_score:.2f}")
                self.stdout.write(f"📏 Pattern consistency: {result.pattern_consistency_score:.2f}")
                self.stdout.write(f"🧪 Test coverage: {result.test_coverage_percentage:.1f}%")
            else:
                self.stdout.write(
                    self.style.ERROR(f"❌ Generation failed")
                )
                if result.errors:
                    for error in result.errors:
                        self.stdout.write(f"  • {error.message}")
                        
        except Exception as e:
            raise CommandError(f"Generation process failed: {e}")
    
    def _show_help(self):
        """Show extended help information."""
        help_text = """
🚀 Django App Agent - AI-Powered Application Generation

USAGE:
    python manage.py app_agent_generate [APP_NAME] [DESCRIPTION] [OPTIONS]

EXAMPLES:
    # Interactive mode (recommended)
    python manage.py app_agent_generate
    
    # Direct generation
    python manage.py app_agent_generate blog "A simple blog application"
    
    # With specific features
    python manage.py app_agent_generate shop "E-commerce shop" --features models,admin,api,tests
    
    # Advanced configuration
    python manage.py app_agent_generate cms "Content management" \\
        --complexity advanced \\
        --app-type django_cfg \\
        --max-questions 15 \\
        --verbose

FEATURES:
    Available features: models, views, urls, admin, forms, templates, static,
    api, serializers, viewsets, filters, pagination, tests, fixtures,
    security, authentication, permissions, tasks, signals, middleware,
    management_commands, docs, services, cfg_config, cfg_modules

COMPLEXITY LEVELS:
    simple     - Basic CRUD with minimal features
    moderate   - Standard app with common features  
    advanced   - Full-featured app with API and tests
    enterprise - Complete app with security and advanced features

For more information, visit: https://docs.django-cfg.com/app-agent/
        """
        self.stdout.write(help_text)
