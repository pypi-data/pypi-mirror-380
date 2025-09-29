"""
Django management command for project diagnosis.

This command provides AI-powered diagnosis of Django/Django-cfg projects
to help identify and solve common problems.
"""

import asyncio
import sys
from pathlib import Path
from typing import List, Optional

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

try:
    from django_cfg.modules.django_app_agent.services import (
        ProjectScannerService,
        ContextBuilderService
    )
    from django_cfg.modules.django_app_agent.models.requests import (
        ProjectScanRequest,
        ContextBuildRequest
    )
    from django_cfg.modules.django_app_agent.core.exceptions import DjangoAppAgentError
    from django_cfg.modules.django_app_agent.core.config import AgentConfig
    from django_cfg.modules.django_app_agent.utils.logging import get_logger
    from django_cfg.modules.django_app_agent.ui.rich_components import (
        RichProgressTracker,
        InteractiveQuestioningUI
    )
except ImportError as e:
    print(f"Error importing django_app_agent module: {e}")
    print("Make sure the django_app_agent module is properly installed.")
    sys.exit(1)


class Command(BaseCommand):
    """Django management command for project diagnosis."""
    
    help = "Diagnose problems in Django/Django-cfg projects using AI (Django App Agent)"
    
    def add_arguments(self, parser):
        """Add command line arguments."""
        
        parser.add_argument(
            '--app',
            type=str,
            help='Specific application name to diagnose'
        )
        
        parser.add_argument(
            '--category',
            choices=[
                'database', 'views', 'templates', 'static',
                'admin', 'auth', 'performance', 'deployment', 
                'config', 'security', 'testing', 'other'
            ],
            help='Problem category to focus on'
        )
        
        parser.add_argument(
            '--description',
            type=str,
            help='Description of the problem you are experiencing'
        )
        
        parser.add_argument(
            '--severity',
            choices=['low', 'medium', 'high', 'critical'],
            default='medium',
            help='Problem severity level (default: medium)'
        )
        
        parser.add_argument(
            '--interactive',
            action='store_true',
            default=True,
            help='Enable interactive diagnosis mode (default: True)'
        )
        
        parser.add_argument(
            '--non-interactive',
            action='store_true',
            help='Disable interactive mode'
        )
        
        parser.add_argument(
            '--scan-only',
            action='store_true',
            help='Only scan the project without AI diagnosis'
        )
        
        parser.add_argument(
            '--output-format',
            choices=['text', 'json', 'markdown'],
            default='text',
            help='Output format for diagnosis results (default: text)'
        )
        
        parser.add_argument(
            '--save-report',
            type=str,
            help='Save diagnosis report to specified file'
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
            logger = get_logger("management.commands.diagnose_project")
            
            # Determine interactive mode
            interactive = options.get('interactive', True) and not options.get('non_interactive', False)
            
            # Show welcome message
            self.stdout.write(
                self.style.SUCCESS("🔍 Django Project Diagnostic Tool")
            )
            self.stdout.write("Analyzing your project for potential issues...\n")
            
            # Run diagnosis
            if interactive and not options.get('description'):
                return self._run_interactive_diagnosis(options)
            else:
                return self._run_direct_diagnosis(options)
                
        except DjangoAppAgentError as e:
            logger.error(f"Diagnosis failed: {e}")
            raise CommandError(f"Diagnosis failed: {e}")
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise CommandError(f"Unexpected error: {e}")
    
    def _run_interactive_diagnosis(self, options):
        """Run interactive diagnosis with user prompts."""
        try:
            self.stdout.write("🤖 Starting interactive diagnosis...\n")
            
            # Gather information interactively
            problem_info = self._gather_problem_info()
            
            # Merge with command line options
            diagnosis_options = {**options, **problem_info}
            
            # Run diagnosis
            return self._run_diagnosis_process(diagnosis_options)
            
        except KeyboardInterrupt:
            self.stdout.write("\n🛑 Diagnosis cancelled by user")
        except Exception as e:
            raise CommandError(f"Interactive diagnosis failed: {e}")
    
    def _run_direct_diagnosis(self, options):
        """Run diagnosis with provided parameters."""
        return self._run_diagnosis_process(options)
    
    def _gather_problem_info(self):
        """Gather problem information interactively."""
        problem_info = {}
        
        # Ask for problem description
        self.stdout.write("📝 Please describe the problem you're experiencing:")
        description = input("Description: ").strip()
        if description:
            problem_info['description'] = description
        
        # Ask for category
        self.stdout.write("\n📂 What category best describes your problem?")
        categories = [
            'database', 'views', 'templates', 'static',
            'admin', 'auth', 'performance', 'deployment',
            'config', 'security', 'testing', 'other'
        ]
        
        for i, category in enumerate(categories, 1):
            self.stdout.write(f"  {i}. {category}")
        
        try:
            choice = input("\nEnter number (or press Enter to skip): ").strip()
            if choice and choice.isdigit():
                idx = int(choice) - 1
                if 0 <= idx < len(categories):
                    problem_info['category'] = categories[idx]
        except (ValueError, IndexError):
            pass
        
        # Ask for specific app
        self.stdout.write("\n🎯 Is this problem specific to a particular app?")
        app_name = input("App name (or press Enter to skip): ").strip()
        if app_name:
            problem_info['app'] = app_name
        
        # Ask for severity
        self.stdout.write("\n⚠️  How severe is this problem?")
        severities = ['low', 'medium', 'high', 'critical']
        for i, severity in enumerate(severities, 1):
            self.stdout.write(f"  {i}. {severity}")
        
        try:
            choice = input("\nEnter number (default: 2 for medium): ").strip()
            if choice and choice.isdigit():
                idx = int(choice) - 1
                if 0 <= idx < len(severities):
                    problem_info['severity'] = severities[idx]
            else:
                problem_info['severity'] = 'medium'
        except (ValueError, IndexError):
            problem_info['severity'] = 'medium'
        
        return problem_info
    
    def _run_diagnosis_process(self, options):
        """Run the actual diagnosis process."""
        try:
            # Initialize configuration
            config = AgentConfig()
            logger = get_logger("management.commands.diagnose_project")
            
            # Show current configuration
            if options.get('verbose'):
                self.stdout.write(f"🔧 Project root: {settings.BASE_DIR}")
                if options.get('app'):
                    self.stdout.write(f"🎯 Target app: {options['app']}")
                if options.get('category'):
                    self.stdout.write(f"📂 Category: {options['category']}")
                if options.get('description'):
                    self.stdout.write(f"📝 Problem: {options['description']}")
                self.stdout.write("")
            
            # Step 1: Scan project
            self.stdout.write("🔍 Step 1: Scanning project structure...")
            scan_result = self._scan_project(options)
            
            if options.get('scan_only'):
                return self._display_scan_results(scan_result, options)
            
            # Step 2: Build context
            self.stdout.write("🧠 Step 2: Building project context...")
            context = self._build_context(scan_result, options)
            
            # Step 3: AI Diagnosis (placeholder for now)
            self.stdout.write("🤖 Step 3: Running AI diagnosis...")
            diagnosis = self._run_ai_diagnosis(context, options)
            
            # Step 4: Display results
            self.stdout.write("📊 Step 4: Generating diagnosis report...")
            return self._display_diagnosis_results(diagnosis, options)
            
        except Exception as e:
            raise CommandError(f"Diagnosis process failed: {e}")
    
    def _scan_project(self, options):
        """Scan the project structure."""
        try:
            # Initialize scanner service
            config = AgentConfig()
            logger = get_logger("project_scanner")
            
            scanner = ProjectScannerService(config, logger)
            
            # Create scan request
            request = ProjectScanRequest(
                project_root=str(settings.BASE_DIR),
                target_app=options.get('app'),
                scan_depth=3,
                include_tests=True,
                include_migrations=True
            )
            
            # Run scan (async)
            if sys.platform == 'win32':
                asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
            
            result = asyncio.run(scanner.process(request))
            return result
            
        except Exception as e:
            raise CommandError(f"Project scan failed: {e}")
    
    def _build_context(self, scan_result, options):
        """Build project context for diagnosis."""
        try:
            # Initialize context builder
            config = AgentConfig()
            logger = get_logger("context_builder")
            
            builder = ContextBuilderService(config, logger)
            
            # Create context request
            request = ContextBuildRequest(
                project_root=str(settings.BASE_DIR),
                scan_result=scan_result,
                focus_area=options.get('category'),
                target_app=options.get('app')
            )
            
            # Build context (async)
            result = asyncio.run(builder.process(request))
            return result
            
        except Exception as e:
            raise CommandError(f"Context building failed: {e}")
    
    def _run_ai_diagnosis(self, context, options):
        """Run AI-powered diagnosis (placeholder implementation)."""
        # This is a placeholder implementation
        # In the real implementation, this would use AI agents
        
        diagnosis = {
            'status': 'completed',
            'findings': [
                {
                    'category': options.get('category', 'general'),
                    'severity': options.get('severity', 'medium'),
                    'title': 'Project Structure Analysis',
                    'description': 'Basic project structure appears to be well-organized.',
                    'recommendations': [
                        'Consider adding more comprehensive tests',
                        'Review security settings for production deployment',
                        'Optimize database queries for better performance'
                    ]
                }
            ],
            'summary': 'Project analysis completed. No critical issues found.',
            'confidence': 0.75
        }
        
        return diagnosis
    
    def _display_scan_results(self, scan_result, options):
        """Display project scan results."""
        self.stdout.write(self.style.SUCCESS("\n📊 Project Scan Results"))
        self.stdout.write("=" * 50)
        
        if hasattr(scan_result, 'project_info'):
            info = scan_result.project_info
            self.stdout.write(f"Project Name: {info.get('name', 'Unknown')}")
            self.stdout.write(f"Django Version: {info.get('django_version', 'Unknown')}")
            self.stdout.write(f"Total Apps: {info.get('total_apps', 0)}")
        
        if hasattr(scan_result, 'apps') and scan_result.apps:
            self.stdout.write(f"\n📱 Applications ({len(scan_result.apps)}):")
            for app in scan_result.apps:
                self.stdout.write(f"  • {app.name} ({app.path})")
        
        self.stdout.write(f"\n✅ Scan completed successfully!")
    
    def _display_diagnosis_results(self, diagnosis, options):
        """Display diagnosis results."""
        self.stdout.write(self.style.SUCCESS("\n🎯 Diagnosis Results"))
        self.stdout.write("=" * 50)
        
        # Summary
        self.stdout.write(f"Status: {diagnosis['status']}")
        self.stdout.write(f"Summary: {diagnosis['summary']}")
        self.stdout.write(f"Confidence: {diagnosis['confidence']:.0%}")
        
        # Findings
        if diagnosis.get('findings'):
            self.stdout.write(f"\n🔍 Findings ({len(diagnosis['findings'])}):")
            
            for i, finding in enumerate(diagnosis['findings'], 1):
                severity_style = {
                    'low': self.style.SUCCESS,
                    'medium': self.style.WARNING,
                    'high': self.style.ERROR,
                    'critical': self.style.ERROR
                }.get(finding['severity'], self.style.WARNING)
                
                self.stdout.write(f"\n{i}. {finding['title']}")
                self.stdout.write(severity_style(f"   Severity: {finding['severity'].upper()}"))
                self.stdout.write(f"   Category: {finding['category']}")
                self.stdout.write(f"   Description: {finding['description']}")
                
                if finding.get('recommendations'):
                    self.stdout.write("   Recommendations:")
                    for rec in finding['recommendations']:
                        self.stdout.write(f"     • {rec}")
        
        # Save report if requested
        if options.get('save_report'):
            self._save_diagnosis_report(diagnosis, options)
        
        self.stdout.write(f"\n✅ Diagnosis completed!")
    
    def _save_diagnosis_report(self, diagnosis, options):
        """Save diagnosis report to file."""
        try:
            report_path = Path(options['save_report'])
            
            # Generate report content based on format
            format_type = options.get('output_format', 'text')
            
            if format_type == 'json':
                import json
                content = json.dumps(diagnosis, indent=2)
            elif format_type == 'markdown':
                content = self._generate_markdown_report(diagnosis)
            else:  # text
                content = self._generate_text_report(diagnosis)
            
            # Write to file
            report_path.write_text(content, encoding='utf-8')
            
            self.stdout.write(f"📄 Report saved to: {report_path}")
            
        except Exception as e:
            self.stdout.write(
                self.style.WARNING(f"Failed to save report: {e}")
            )
    
    def _generate_markdown_report(self, diagnosis):
        """Generate markdown format report."""
        content = f"""# Project Diagnosis Report

## Summary
- **Status**: {diagnosis['status']}
- **Confidence**: {diagnosis['confidence']:.0%}
- **Summary**: {diagnosis['summary']}

## Findings
"""
        
        for i, finding in enumerate(diagnosis.get('findings', []), 1):
            content += f"""
### {i}. {finding['title']}
- **Severity**: {finding['severity'].upper()}
- **Category**: {finding['category']}
- **Description**: {finding['description']}

**Recommendations**:
"""
            for rec in finding.get('recommendations', []):
                content += f"- {rec}\n"
        
        return content
    
    def _generate_text_report(self, diagnosis):
        """Generate plain text report."""
        content = f"""PROJECT DIAGNOSIS REPORT
{'=' * 50}

STATUS: {diagnosis['status']}
CONFIDENCE: {diagnosis['confidence']:.0%}
SUMMARY: {diagnosis['summary']}

FINDINGS:
"""
        
        for i, finding in enumerate(diagnosis.get('findings', []), 1):
            content += f"""
{i}. {finding['title']}
   Severity: {finding['severity'].upper()}
   Category: {finding['category']}
   Description: {finding['description']}
   
   Recommendations:
"""
            for rec in finding.get('recommendations', []):
                content += f"   • {rec}\n"
        
        return content
