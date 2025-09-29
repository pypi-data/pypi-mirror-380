"""
Rich UI Components for Django App Agent Module.

This module provides beautiful terminal UI components using Rich library
for progress tracking, question interfaces, error display, and status updates.
"""

from typing import Dict, List, Optional, Any, Generator, ContextManager
from contextlib import contextmanager
from datetime import datetime, timedelta
import time

from rich.console import Console
from rich.panel import Panel
from rich.progress import (
    Progress, SpinnerColumn, TextColumn, BarColumn, 
    TimeElapsedColumn, TimeRemainingColumn, MofNCompleteColumn
)
from rich.prompt import Prompt, Confirm, IntPrompt
from rich.syntax import Syntax
from rich.table import Table
from rich.tree import Tree
from rich.layout import Layout
from rich.live import Live
from rich.text import Text
from rich.align import Align
from rich.columns import Columns
from rich.status import Status

from ..models.requests import AppGenerationRequest
from ..models.responses import AppGenerationResult
from ..models.enums import AppType, AppComplexity, AppFeature


class RichTheme:
    """Consistent color theme for Rich UI components."""
    
    PRIMARY = "bright_blue"
    SECONDARY = "bright_green"
    ACCENT = "bright_yellow"
    SUCCESS = "bright_green"
    WARNING = "bright_yellow"
    ERROR = "bright_red"
    INFO = "bright_cyan"
    MUTED = "dim white"
    CODE = "bright_magenta"


class RichProgressTracker:
    """Rich progress tracking for long-running operations."""
    
    def __init__(self, console: Console):
        """Initialize progress tracker."""
        self.console = console
        self.theme = RichTheme()
    
    @contextmanager
    def track_generation(self, app_name: str) -> ContextManager['GenerationProgress']:
        """Track application generation progress."""
        progress = GenerationProgress(self.console, app_name)
        try:
            yield progress
        finally:
            progress.complete()
    
    @contextmanager
    def track_scanning(self) -> ContextManager['ScanningProgress']:
        """Track project scanning progress."""
        progress = ScanningProgress(self.console)
        try:
            yield progress
        finally:
            progress.complete()


class GenerationProgress:
    """Progress tracker for application generation."""
    
    def __init__(self, console: Console, app_name: str):
        """Initialize generation progress."""
        self.console = console
        self.app_name = app_name
        self.start_time = datetime.now()
        
        # Create progress components
        self.progress = Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            MofNCompleteColumn(),
            TimeElapsedColumn(),
            TimeRemainingColumn(),
            console=console,
            transient=False
        )
        
        # Define generation phases
        self.phases = [
            "🔍 Analyzing project structure",
            "🧠 Building development context", 
            "❓ Processing requirements",
            "📋 Creating app manifest",
            "🏗️ Generating code files",
            "✅ Validating code quality",
            "📊 Calculating metrics",
            "📄 Creating documentation"
        ]
        
        self.current_phase = 0
        self.task_id = None
    
    def start(self):
        """Start progress tracking."""
        self.progress.start()
        self.task_id = self.progress.add_task(
            f"Generating {self.app_name}...",
            total=len(self.phases)
        )
        
        # Show initial phase
        self.update_phase(0)
    
    def update_phase(self, phase_index: int, message: Optional[str] = None):
        """Update current phase."""
        if phase_index < len(self.phases):
            self.current_phase = phase_index
            description = message or self.phases[phase_index]
            
            self.progress.update(
                self.task_id,
                description=description,
                completed=phase_index
            )
    
    def next_phase(self, message: Optional[str] = None):
        """Move to next phase."""
        self.update_phase(self.current_phase + 1, message)
    
    def complete(self):
        """Complete progress tracking."""
        if self.task_id:
            self.progress.update(
                self.task_id,
                description="✅ Generation completed!",
                completed=len(self.phases)
            )
        
        self.progress.stop()
        
        # Show completion summary
        duration = datetime.now() - self.start_time
        self._show_completion_summary(duration)
    
    def _show_completion_summary(self, duration: timedelta):
        """Show completion summary."""
        summary_text = Text()
        summary_text.append("🎉 Application generation completed!\n", style="bold green")
        summary_text.append(f"⏱️  Total time: {duration.total_seconds():.1f} seconds\n", style="cyan")
        summary_text.append(f"📱 App: {self.app_name}", style="blue")
        
        panel = Panel(
            summary_text,
            title="Generation Complete",
            border_style="green",
            padding=(1, 2)
        )
        
        self.console.print(panel)


class ScanningProgress:
    """Progress tracker for project scanning."""
    
    def __init__(self, console: Console):
        """Initialize scanning progress."""
        self.console = console
        self.status = Status("🔍 Scanning project...", console=console)
    
    def start(self):
        """Start scanning progress."""
        self.status.start()
    
    def update(self, message: str):
        """Update scanning status."""
        self.status.update(f"🔍 {message}")
    
    def complete(self):
        """Complete scanning."""
        self.status.stop()


class RichQuestionInterface:
    """Rich interface for interactive questioning."""
    
    def __init__(self, console: Console):
        """Initialize question interface."""
        self.console = console
        self.theme = RichTheme()
    
    def ask_app_details(self) -> Dict[str, Any]:
        """Ask for basic application details."""
        self.console.print()
        self._show_header("Application Details", "Let's gather some basic information about your app")
        
        # App name
        app_name = self._ask_app_name()
        
        # Description
        description = self._ask_description()
        
        # App type
        app_type = self._ask_app_type()
        
        # Complexity
        complexity = self._ask_complexity()
        
        return {
            "app_name": app_name,
            "description": description,
            "app_type": app_type,
            "complexity": complexity
        }
    
    def ask_features(self, complexity: AppComplexity) -> List[AppFeature]:
        """Ask for feature selection."""
        self._show_header("Feature Selection", f"Select features for your {complexity.value} application")
        
        recommended = complexity.get_recommended_features()
        all_features = list(AppFeature)
        
        # Show recommended features
        self._show_recommended_features(recommended)
        
        # Ask if user wants to customize
        if Confirm.ask("\n[bold]Customize feature selection?[/bold]", default=False):
            return self._customize_features(all_features, recommended)
        else:
            return list(recommended)
    
    def ask_contextual_questions(self, questions: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Ask contextual questions based on project analysis."""
        self._show_header("Contextual Questions", "Based on your project, we have some specific questions")
        
        answers = {}
        
        for i, question in enumerate(questions, 1):
            self.console.print(f"\n[bold cyan]Question {i}/{len(questions)}:[/bold cyan]")
            
            # Show question context if available
            if question.get("context"):
                self._show_question_context(question["context"])
            
            # Ask the question
            answer = self._ask_question(question)
            answers[question["id"]] = answer
            
            # Show progress
            progress_bar = "█" * (i * 20 // len(questions)) + "░" * (20 - (i * 20 // len(questions)))
            self.console.print(f"[dim]Progress: [{progress_bar}] {i}/{len(questions)}[/dim]")
        
        return answers
    
    def _show_header(self, title: str, subtitle: str = ""):
        """Show section header."""
        header_text = Text()
        header_text.append(title, style=f"bold {self.theme.PRIMARY}")
        if subtitle:
            header_text.append(f"\n{subtitle}", style=self.theme.MUTED)
        
        panel = Panel(
            header_text,
            border_style=self.theme.PRIMARY,
            padding=(1, 2)
        )
        
        self.console.print(panel)
    
    def _ask_app_name(self) -> str:
        """Ask for application name."""
        while True:
            app_name = Prompt.ask(
                "[bold]Application name[/bold]",
                default="my_app"
            )
            
            # Basic validation
            if app_name.replace("_", "").isalnum() and app_name[0].isalpha():
                return app_name
            else:
                self.console.print("[red]❌ Invalid name. Use letters, numbers, and underscores only.[/red]")
    
    def _ask_description(self) -> str:
        """Ask for application description."""
        return Prompt.ask(
            "[bold]Brief description[/bold]",
            default="A Django application"
        )
    
    def _ask_app_type(self) -> AppType:
        """Ask for application type."""
        self.console.print("\n[bold]Application Type:[/bold]")
        
        table = Table(show_header=False, box=None, padding=(0, 2))
        table.add_column("Option", style="cyan")
        table.add_column("Description")
        
        table.add_row("1", "🐍 Django - Standard Django application")
        table.add_row("2", "⚙️  Django-CFG - Enhanced with configuration management")
        
        self.console.print(table)
        
        choice = Prompt.ask("Choose type", choices=["1", "2"], default="2")
        return AppType.DJANGO if choice == "1" else AppType.DJANGO_CFG
    
    def _ask_complexity(self) -> AppComplexity:
        """Ask for complexity level."""
        self.console.print("\n[bold]Complexity Level:[/bold]")
        
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Option", style="cyan", width=8)
        table.add_column("Level", style="green")
        table.add_column("Description")
        table.add_column("Time", style="yellow")
        
        table.add_row("1", "Basic", "Simple app with core features", "~5 min")
        table.add_row("2", "Moderate", "Standard app with common features", "~15 min")
        table.add_row("3", "Advanced", "Complex app with advanced features", "~30 min")
        table.add_row("4", "Enterprise", "Full-featured enterprise app", "~60 min")
        
        self.console.print(table)
        
        choice = Prompt.ask("Choose complexity", choices=["1", "2", "3", "4"], default="2")
        
        complexity_map = {
            "1": AppComplexity.SIMPLE,
            "2": AppComplexity.MODERATE,
            "3": AppComplexity.ADVANCED,
            "4": AppComplexity.ENTERPRISE
        }
        
        return complexity_map[choice]
    
    def _show_recommended_features(self, features: set):
        """Show recommended features."""
        self.console.print("\n[bold green]Recommended Features:[/bold green]")
        
        columns = []
        for feature in sorted(features, key=lambda x: x.value):
            feature_text = Text()
            feature_text.append("✓ ", style="green")
            feature_text.append(feature.value.replace("_", " ").title(), style="white")
            columns.append(Panel(feature_text, padding=(0, 1), border_style="dim"))
        
        self.console.print(Columns(columns, equal=True, expand=True))
    
    def _customize_features(self, all_features: List[AppFeature], recommended: set) -> List[AppFeature]:
        """Allow feature customization."""
        selected = recommended.copy()
        
        self.console.print("\n[bold]Feature Customization:[/bold]")
        self.console.print("[dim]Type feature name to toggle, 'done' to finish[/dim]")
        
        while True:
            # Show current selection in columns
            self._show_feature_grid(all_features, selected)
            
            choice = Prompt.ask(
                "\nFeature to toggle (or 'done')",
                default="done"
            ).lower()
            
            if choice == "done":
                break
            
            # Find matching feature
            matching_feature = self._find_feature(choice, all_features)
            
            if matching_feature:
                if matching_feature in selected:
                    selected.remove(matching_feature)
                    self.console.print(f"[red]➖ Removed {matching_feature.value}[/red]")
                else:
                    selected.add(matching_feature)
                    self.console.print(f"[green]➕ Added {matching_feature.value}[/green]")
            else:
                self.console.print(f"[red]❌ Feature '{choice}' not found[/red]")
        
        return list(selected)
    
    def _show_feature_grid(self, all_features: List[AppFeature], selected: set):
        """Show features in a grid layout."""
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Feature", style="white")
        table.add_column("Status", width=8, style="center")
        table.add_column("Description", style="dim")
        
        for feature in all_features:
            status = "✓" if feature in selected else " "
            status_style = "green" if feature in selected else "dim"
            description = self._get_feature_description(feature)
            
            table.add_row(
                feature.value.replace("_", " ").title(),
                status,
                description,
                style=status_style
            )
        
        self.console.print(table)
    
    def _find_feature(self, search: str, features: List[AppFeature]) -> Optional[AppFeature]:
        """Find feature by partial name match."""
        search = search.lower()
        
        # Exact match first
        for feature in features:
            if feature.value.lower() == search:
                return feature
        
        # Partial match
        for feature in features:
            if search in feature.value.lower():
                return feature
        
        return None
    
    def _get_feature_description(self, feature: AppFeature) -> str:
        """Get feature description."""
        descriptions = {
            AppFeature.MODELS: "Database models and ORM",
            AppFeature.VIEWS: "View functions and classes",
            AppFeature.URLS: "URL routing configuration",
            AppFeature.ADMIN: "Django admin interface",
            AppFeature.FORMS: "Form classes and validation",
            AppFeature.TEMPLATES: "HTML templates",
            AppFeature.API: "REST API with DRF",
            AppFeature.TESTS: "Unit and integration tests",
            AppFeature.TASKS: "Background tasks",
            AppFeature.DOCS: "Documentation",
            AppFeature.CONFIG: "Configuration management",
            AppFeature.SECURITY: "Security and permissions",
        }
        return descriptions.get(feature, "Additional feature")
    
    def _show_question_context(self, context: Dict[str, Any]):
        """Show context for a question."""
        if context.get("code_snippet"):
            code_panel = Panel(
                Syntax(context["code_snippet"], "python", theme="monokai"),
                title="📄 Relevant Code",
                border_style="dim"
            )
            self.console.print(code_panel)
        
        if context.get("explanation"):
            self.console.print(f"[dim]{context['explanation']}[/dim]")
    
    def _ask_question(self, question: Dict[str, Any]) -> Any:
        """Ask a single question."""
        question_type = question.get("type", "text")
        
        if question_type == "yes_no":
            return Confirm.ask(question["text"], default=question.get("default", True))
        
        elif question_type == "choice":
            choices = question.get("choices", [])
            if choices:
                self.console.print(f"\n[bold]{question['text']}[/bold]")
                for i, choice in enumerate(choices, 1):
                    self.console.print(f"  {i}. {choice}")
                
                choice_num = IntPrompt.ask(
                    "Choose option",
                    choices=[str(i) for i in range(1, len(choices) + 1)],
                    default="1"
                )
                return choices[int(choice_num) - 1]
        
        else:  # text
            return Prompt.ask(question["text"], default=question.get("default", ""))


class RichErrorDisplay:
    """Rich error display with helpful suggestions."""
    
    def __init__(self, console: Console):
        """Initialize error display."""
        self.console = console
        self.theme = RichTheme()
    
    def show_error(
        self,
        title: str,
        message: str,
        errors: Optional[List[str]] = None,
        warnings: Optional[List[str]] = None,
        suggestions: Optional[List[str]] = None
    ):
        """Show comprehensive error information."""
        # Main error panel
        error_text = Text()
        error_text.append("❌ ", style=self.theme.ERROR)
        error_text.append(message, style="white")
        
        error_panel = Panel(
            error_text,
            title=f"[bold red]{title}[/bold red]",
            border_style=self.theme.ERROR,
            padding=(1, 2)
        )
        
        self.console.print(error_panel)
        
        # Show detailed errors
        if errors:
            self._show_error_list("Errors", errors, self.theme.ERROR)
        
        # Show warnings
        if warnings:
            self._show_error_list("Warnings", warnings, self.theme.WARNING)
        
        # Show suggestions
        if suggestions:
            self._show_suggestions(suggestions)
    
    def _show_error_list(self, title: str, items: List[str], style: str):
        """Show list of errors or warnings."""
        self.console.print(f"\n[bold {style}]{title}:[/bold {style}]")
        
        for item in items:
            self.console.print(f"  • {item}", style=style)
    
    def _show_suggestions(self, suggestions: List[str]):
        """Show helpful suggestions."""
        self.console.print(f"\n[bold {self.theme.INFO}]💡 Suggestions:[/bold {self.theme.INFO}]")
        
        for suggestion in suggestions:
            self.console.print(f"  • {suggestion}", style=self.theme.INFO)


class RichStatusDisplay:
    """Rich status display for various operations."""
    
    def __init__(self, console: Console):
        """Initialize status display."""
        self.console = console
        self.theme = RichTheme()
    
    def show_generation_result(self, result: AppGenerationResult):
        """Show application generation result."""
        if result.status == "success":
            self._show_success_result(result)
        else:
            self._show_failure_result(result)
    
    def _show_success_result(self, result: AppGenerationResult):
        """Show successful generation result."""
        # Success header
        success_text = Text()
        success_text.append("🎉 Success! ", style="bold green")
        success_text.append(f"Generated '{result.app_name}' application", style="white")
        
        header_panel = Panel(
            success_text,
            border_style="green",
            padding=(1, 2)
        )
        
        self.console.print(header_panel)
        
        # Statistics table
        stats_table = Table(title="Generation Statistics", show_header=True)
        stats_table.add_column("Metric", style="cyan")
        stats_table.add_column("Value", style="green")
        
        stats_table.add_row("Files Generated", str(len(result.generated_files)))
        stats_table.add_row("Duration", f"{result.duration_seconds:.1f} seconds")
        
        if result.quality_metrics:
            stats_table.add_row("Code Quality", f"{result.quality_metrics.code_readability_score:.2f}/1.0")
            stats_table.add_row("Test Coverage", f"{result.quality_metrics.test_coverage_percentage:.1f}%")
        
        self.console.print(stats_table)
        
        # Next steps
        self._show_next_steps(result.app_name)
    
    def _show_failure_result(self, result: AppGenerationResult):
        """Show failed generation result."""
        error_text = Text()
        error_text.append("❌ Generation Failed\n", style="bold red")
        error_text.append(result.message, style="white")
        
        error_panel = Panel(
            error_text,
            border_style="red",
            padding=(1, 2)
        )
        
        self.console.print(error_panel)
        
        # Show errors if any
        if result.errors:
            self.console.print("\n[bold red]Errors:[/bold red]")
            for error in result.errors:
                self.console.print(f"  • {error}", style="red")
    
    def _show_next_steps(self, app_name: str):
        """Show next steps after successful generation."""
        self.console.print("\n[bold]🚀 Next Steps:[/bold]")
        
        steps = [
            f"1. Add '{app_name}' to your INSTALLED_APPS",
            "2. Run migrations: [cyan]python manage.py makemigrations && python manage.py migrate[/cyan]",
            "3. Include URLs in your main urls.py",
            "4. Start development! 🎯"
        ]
        
        for step in steps:
            self.console.print(f"   {step}")
        
        self.console.print()
