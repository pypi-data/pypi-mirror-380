"""
Main CLI Interface for Django App Agent Module.

This module provides the primary command-line interface using Click
with Rich integration for beautiful terminal output.
"""

from typing import Optional, List, Dict, Any
from pathlib import Path
import asyncio
import sys

import click
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt, Confirm
from rich.table import Table

from ..core.config import AgentConfig
from ..models.requests import AppGenerationRequest
from ..models.enums import AppType, AppComplexity, AppFeature
from ..services.app_generator import AppGeneratorService
from ..services.project_scanner import ProjectScannerService
from ..services.base import create_service_dependencies
from ..utils.logging import get_logger
from .rich_components import RichProgressTracker, RichQuestionInterface, RichErrorDisplay


class DjangoAppAgentCLI:
    """
    Main CLI interface for Django App Agent.
    
    Provides commands for:
    - Interactive application generation
    - Project scanning and analysis
    - Batch processing
    - Configuration management
    """
    
    def __init__(self):
        """Initialize CLI interface."""
        self.console = Console()
        self.logger = get_logger("cli")
        self.config = None
        self.progress_tracker = RichProgressTracker(self.console)
        self.question_interface = RichQuestionInterface(self.console)
        self.error_display = RichErrorDisplay(self.console)
    
    def _load_config(self) -> AgentConfig:
        """Load agent configuration."""
        if self.config is None:
            try:
                # In real implementation, this would load from django-cfg
                self.config = AgentConfig()
            except Exception as e:
                self.error_display.show_error(
                    "Configuration Error",
                    f"Failed to load configuration: {e}",
                    suggestions=["Check django-cfg setup", "Verify API keys"]
                )
                sys.exit(1)
        return self.config
    
    def _show_welcome(self):
        """Show welcome message."""
        welcome_text = Text()
        welcome_text.append("🚀 Django App Agent", style="bold blue")
        welcome_text.append("\nAI-Powered Django Application Generator", style="italic")
        
        panel = Panel(
            welcome_text,
            title="Welcome",
            border_style="blue",
            padding=(1, 2)
        )
        self.console.print(panel)
        self.console.print()
    
    def _show_app_types(self) -> AppType:
        """Show application type selection."""
        self.console.print("[bold]Select Application Type:[/bold]")
        
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Option", style="cyan", width=10)
        table.add_column("Type", style="green")
        table.add_column("Description")
        
        table.add_row("1", "Django", "Standard Django application")
        table.add_row("2", "Django-CFG", "Django-CFG enhanced application with configuration management")
        
        self.console.print(table)
        self.console.print()
        
        while True:
            choice = Prompt.ask("Choose application type", choices=["1", "2"], default="2")
            if choice == "1":
                return AppType.DJANGO
            elif choice == "2":
                return AppType.DJANGO_CFG
    
    def _show_complexity_levels(self) -> AppComplexity:
        """Show complexity level selection."""
        self.console.print("[bold]Select Complexity Level:[/bold]")
        
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Option", style="cyan", width=10)
        table.add_column("Level", style="green")
        table.add_column("Description")
        table.add_column("Est. Time", style="yellow")
        
        table.add_row("1", "Basic", "Simple app with core features", "~5 min")
        table.add_row("2", "Moderate", "Standard app with common features", "~15 min")
        table.add_row("3", "Advanced", "Complex app with advanced features", "~30 min")
        table.add_row("4", "Enterprise", "Full-featured enterprise application", "~60 min")
        
        self.console.print(table)
        self.console.print()
        
        choice = Prompt.ask("Choose complexity level", choices=["1", "2", "3", "4"], default="2")
        
        complexity_map = {
            "1": AppComplexity.SIMPLE,
            "2": AppComplexity.MODERATE,
            "3": AppComplexity.ADVANCED,
            "4": AppComplexity.ENTERPRISE
        }
        
        return complexity_map[choice]
    
    def _select_features(self, complexity: AppComplexity) -> List[AppFeature]:
        """Interactive feature selection."""
        recommended = complexity.get_recommended_features()
        
        self.console.print(f"[bold]Select Features for {complexity.value.title()} Application:[/bold]")
        self.console.print(f"[dim]Recommended features are pre-selected[/dim]")
        self.console.print()
        
        # Show available features
        all_features = list(AppFeature)
        selected_features = set(recommended)
        
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Feature", style="green")
        table.add_column("Selected", style="cyan", width=10)
        table.add_column("Description")
        
        for feature in all_features:
            selected = "✓" if feature in selected_features else " "
            description = self._get_feature_description(feature)
            style = "green" if feature in selected_features else "dim"
            table.add_row(feature.value, selected, description, style=style)
        
        self.console.print(table)
        self.console.print()
        
        # Allow customization
        if Confirm.ask("Customize feature selection?", default=False):
            selected_features = self._customize_features(all_features, selected_features)
        
        return list(selected_features)
    
    def _customize_features(self, all_features: List[AppFeature], current: set) -> set:
        """Allow user to customize feature selection."""
        selected = current.copy()
        
        self.console.print("[bold]Feature Customization:[/bold]")
        self.console.print("[dim]Type feature name to toggle, 'done' to finish[/dim]")
        self.console.print()
        
        while True:
            # Show current selection
            self.console.print("[bold]Current selection:[/bold]")
            for feature in all_features:
                status = "✓" if feature in selected else " "
                style = "green" if feature in selected else "dim"
                self.console.print(f"  [{status}] {feature.value}", style=style)
            
            self.console.print()
            
            choice = Prompt.ask(
                "Feature to toggle (or 'done')",
                default="done"
            ).lower()
            
            if choice == "done":
                break
            
            # Find matching feature
            matching_feature = None
            for feature in all_features:
                if feature.value.lower() == choice or feature.value.lower().startswith(choice):
                    matching_feature = feature
                    break
            
            if matching_feature:
                if matching_feature in selected:
                    selected.remove(matching_feature)
                    self.console.print(f"[red]Removed {matching_feature.value}[/red]")
                else:
                    selected.add(matching_feature)
                    self.console.print(f"[green]Added {matching_feature.value}[/green]")
            else:
                self.console.print(f"[red]Feature '{choice}' not found[/red]")
            
            self.console.print()
        
        return selected
    
    def _get_feature_description(self, feature: AppFeature) -> str:
        """Get description for a feature."""
        descriptions = {
            AppFeature.MODELS: "Database models and ORM",
            AppFeature.VIEWS: "View functions and classes",
            AppFeature.URLS: "URL routing configuration",
            AppFeature.ADMIN: "Django admin interface",
            AppFeature.FORMS: "Form classes and validation",
            AppFeature.TEMPLATES: "HTML templates",
            AppFeature.API: "REST API with DRF",
            AppFeature.TESTS: "Unit and integration tests",
            AppFeature.TASKS: "Background tasks (Celery/Dramatiq)",
            AppFeature.DOCS: "Auto-generated documentation",
            AppFeature.CONFIG: "Configuration management",
            AppFeature.SECURITY: "Security and permissions",
            AppFeature.SIGNALS: "Django signals",
            AppFeature.MANAGEMENT_COMMANDS: "Custom management commands",
            AppFeature.MIDDLEWARE: "Custom middleware",
            AppFeature.CONTEXT_PROCESSORS: "Template context processors",
        }
        return descriptions.get(feature, "Additional feature")
    
    async def _run_generation(self, request: AppGenerationRequest) -> None:
        """Run application generation process."""
        config = self._load_config()
        
        # Initialize services
        generator_service = AppGeneratorService(config)
        
        # Create dependencies
        deps = create_service_dependencies(
            config=config,
            service_name="cli_generation",
            project_root=Path.cwd()
        )
        
        # Start progress tracking
        with self.progress_tracker.track_generation(request.app_name) as progress:
            try:
                # Run generation
                result = await generator_service.process(request, deps)
                
                # Show results
                if result.status == "success":
                    self._show_success_result(result)
                else:
                    self._show_error_result(result)
                    
            except Exception as e:
                self.error_display.show_error(
                    "Generation Failed",
                    str(e),
                    suggestions=["Check configuration", "Verify permissions", "Try again"]
                )
    
    def _show_success_result(self, result) -> None:
        """Show successful generation result."""
        self.console.print()
        
        success_panel = Panel(
            f"✅ Successfully generated application '[bold green]{result.app_name}[/bold green]'\n"
            f"📁 Files created: {len(result.generated_files)}\n"
            f"⏱️  Duration: {result.duration_seconds:.1f} seconds",
            title="Generation Complete",
            border_style="green",
            padding=(1, 2)
        )
        self.console.print(success_panel)
        
        # Show quality metrics if available
        if result.quality_metrics:
            metrics = result.quality_metrics
            
            metrics_table = Table(title="Quality Metrics", show_header=True)
            metrics_table.add_column("Metric", style="cyan")
            metrics_table.add_column("Score", style="green")
            
            metrics_table.add_row("Code Readability", f"{metrics.code_readability_score:.2f}/1.0")
            metrics_table.add_row("Maintainability", f"{metrics.maintainability_score:.2f}/1.0")
            metrics_table.add_row("Type Hints", f"{metrics.type_hint_completeness:.2f}/1.0")
            metrics_table.add_row("Pydantic Compliance", f"{metrics.pydantic_compliance_score:.2f}/1.0")
            metrics_table.add_row("Test Coverage", f"{metrics.test_coverage_percentage:.1f}%")
            
            self.console.print(metrics_table)
        
        # Show next steps
        self.console.print()
        self.console.print("[bold]Next Steps:[/bold]")
        self.console.print("1. Add the app to your INSTALLED_APPS")
        self.console.print("2. Run migrations: [cyan]python manage.py makemigrations && python manage.py migrate[/cyan]")
        self.console.print("3. Include URLs in your main urls.py")
        self.console.print("4. Start development!")
    
    def _show_error_result(self, result) -> None:
        """Show error generation result."""
        self.error_display.show_error(
            "Generation Failed",
            result.message,
            errors=result.errors,
            warnings=result.warnings
        )


# Click CLI commands
@click.group()
@click.version_option(version="0.1.0", prog_name="Django App Agent")
def cli():
    """🚀 Django App Agent - AI-Powered Django Application Generator"""
    pass


@cli.command()
@click.option('--app-name', prompt='Application name', help='Name of the Django application')
@click.option('--description', prompt='Description', help='Brief description of the application')
@click.option('--app-type', type=click.Choice(['django', 'django_cfg']), default='django_cfg', help='Application type')
@click.option('--complexity', type=click.Choice(['basic', 'moderate', 'advanced', 'enterprise']), default='moderate', help='Complexity level')
@click.option('--output-dir', type=click.Path(), help='Output directory')
@click.option('--interactive/--no-interactive', default=True, help='Interactive mode')
def generate(app_name: str, description: str, app_type: str, complexity: str, output_dir: Optional[str], interactive: bool):
    """Generate a new Django application with AI assistance."""
    
    cli_interface = DjangoAppAgentCLI()
    
    if interactive:
        cli_interface._show_welcome()
        
        # Interactive mode
        app_type_enum = cli_interface._show_app_types()
        complexity_enum = cli_interface._show_complexity_levels()
        features = cli_interface._select_features(complexity_enum)
        
    else:
        # Non-interactive mode
        app_type_enum = AppType.DJANGO_CFG if app_type == 'django_cfg' else AppType.DJANGO
        complexity_enum = AppComplexity(complexity)
        features = list(complexity_enum.get_recommended_features())
    
    # Create generation request
    request = AppGenerationRequest(
        app_name=app_name,
        description=description,
        app_type=app_type_enum,
        complexity=complexity_enum,
        features=features,
        output_directory=output_dir
    )
    
    # Run generation
    asyncio.run(cli_interface._run_generation(request))


@cli.command()
@click.option('--project-root', type=click.Path(exists=True), default='.', help='Project root directory')
@click.option('--output-format', type=click.Choice(['table', 'json']), default='table', help='Output format')
def scan(project_root: str, output_format: str):
    """Scan and analyze Django project structure."""
    
    cli_interface = DjangoAppAgentCLI()
    config = cli_interface._load_config()
    
    async def run_scan():
        scanner_service = ProjectScannerService(config)
        
        request = ProjectScanRequest(
            project_root=Path(project_root),
            scan_depth=3,
            analyze_dependencies=True,
            detect_patterns=True
        )
        
        deps = create_service_dependencies(
            config=config,
            service_name="cli_scan",
            project_root=Path(project_root)
        )
        
        with cli_interface.progress_tracker.track_scanning() as progress:
            result = await scanner_service.process(request, deps)
        
        # Display results
        if output_format == 'table':
            cli_interface._show_scan_table(result)
        else:
            cli_interface._show_scan_json(result)
    
    asyncio.run(run_scan())


@cli.command()
def config():
    """Show current configuration."""
    
    cli_interface = DjangoAppAgentCLI()
    config = cli_interface._load_config()
    
    # Show configuration in a nice table
    config_table = Table(title="Django App Agent Configuration", show_header=True)
    config_table.add_column("Setting", style="cyan")
    config_table.add_column("Value", style="green")
    
    # Add configuration rows (this would be populated from actual config)
    config_table.add_row("Version", "0.1.0")
    config_table.add_row("Default App Type", "django_cfg")
    config_table.add_row("AI Provider", "OpenRouter")
    
    cli_interface.console.print(config_table)


if __name__ == '__main__':
    cli()
