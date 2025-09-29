"""
Report Service for Django App Agent Module.

This service generates comprehensive reports for application generation
processes, including detailed logs, metrics, and documentation.
"""

from typing import List, Dict, Any, Optional
from pathlib import Path
from datetime import datetime, timezone
import json

from pydantic import BaseModel, Field, ConfigDict

from .base import BaseService, ServiceDependencies
from ..models.responses import AppGenerationResult, QualityMetrics, GeneratedFile
from ..core.exceptions import FileSystemError


class ReportRequest(BaseModel):
    """Request for report generation."""
    
    model_config = ConfigDict(extra='forbid', validate_assignment=True)
    
    generation_result: AppGenerationResult = Field(description="Application generation result")
    report_formats: List[str] = Field(
        default_factory=lambda: ["markdown", "json"],
        description="Report formats to generate"
    )
    include_code_samples: bool = Field(default=True, description="Whether to include code samples")
    include_metrics: bool = Field(default=True, description="Whether to include quality metrics")
    output_directory: Optional[Path] = Field(default=None, description="Custom output directory")


class ReportResult(BaseModel):
    """Result of report generation."""
    
    model_config = ConfigDict(extra='forbid', validate_assignment=True)
    
    generated_reports: List[str] = Field(description="Paths to generated report files")
    report_summary: Dict[str, Any] = Field(description="Summary of the report generation")
    total_size_bytes: int = Field(default=0, description="Total size of generated reports")


class ReportService(BaseService[ReportRequest, ReportResult]):
    """
    Service for generating comprehensive reports of application generation processes.
    
    Provides:
    - Markdown reports with detailed information
    - JSON reports for programmatic access
    - Code sample inclusion
    - Quality metrics visualization
    - Process documentation
    """
    
    def __init__(self, config):
        """Initialize report service."""
        super().__init__("report", config)
    
    async def process(
        self, 
        request: ReportRequest, 
        dependencies: ServiceDependencies
    ) -> ReportResult:
        """
        Process report generation request.
        
        Args:
            request: Report generation request
            dependencies: Service dependencies
            
        Returns:
            ReportResult with generated reports
        """
        dependencies.log_operation(
            f"Generating reports for app '{request.generation_result.app_name}'",
            formats=request.report_formats,
            include_code_samples=request.include_code_samples,
            include_metrics=request.include_metrics
        )
        
        try:
            generated_reports = []
            total_size = 0
            
            # Determine output directory
            output_dir = request.output_directory or dependencies.get_output_path()
            report_dir = output_dir / request.generation_result.app_name / "@report"
            report_dir.mkdir(parents=True, exist_ok=True)
            
            # Generate reports in requested formats
            for format_type in request.report_formats:
                if format_type == "markdown":
                    report_path = await self._generate_markdown_report(
                        request, report_dir, dependencies
                    )
                elif format_type == "json":
                    report_path = await self._generate_json_report(
                        request, report_dir, dependencies
                    )
                else:
                    dependencies.logger.warning(f"Unknown report format: {format_type}")
                    continue
                
                if report_path and report_path.exists():
                    generated_reports.append(str(report_path))
                    total_size += report_path.stat().st_size
            
            # Generate summary
            summary = {
                "app_name": request.generation_result.app_name,
                "generation_status": request.generation_result.status,
                "reports_generated": len(generated_reports),
                "formats": request.report_formats,
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "total_files_generated": len(request.generation_result.generated_files)
            }
            
            result = ReportResult(
                generated_reports=generated_reports,
                report_summary=summary,
                total_size_bytes=total_size
            )
            
            dependencies.log_operation(
                "Report generation completed successfully",
                reports_count=len(generated_reports),
                total_size_kb=total_size // 1024
            )
            
            return result
            
        except Exception as e:
            dependencies.log_error("Report generation failed", e)
            raise
    
    async def _generate_markdown_report(
        self,
        request: ReportRequest,
        output_dir: Path,
        dependencies: ServiceDependencies
    ) -> Optional[Path]:
        """Generate markdown report."""
        try:
            result = request.generation_result
            report_path = output_dir / "GENERATION_REPORT.md"
            
            # Build markdown content
            content = self._build_markdown_content(request, dependencies)
            
            # Write report
            report_path.write_text(content, encoding='utf-8')
            
            return report_path
            
        except Exception as e:
            dependencies.log_error("Failed to generate markdown report", e)
            return None
    
    async def _generate_json_report(
        self,
        request: ReportRequest,
        output_dir: Path,
        dependencies: ServiceDependencies
    ) -> Optional[Path]:
        """Generate JSON report."""
        try:
            result = request.generation_result
            report_path = output_dir / "generation_report.json"
            
            # Build JSON data
            report_data = {
                "metadata": {
                    "generated_at": datetime.now(timezone.utc).isoformat(),
                    "generator_version": "0.1.0",
                    "report_format": "json"
                },
                "application": {
                    "name": result.app_name,
                    "status": result.status,
                    "message": result.message,
                    "duration_seconds": result.duration_seconds
                },
                "generation_process": {
                    "files_generated": len(result.generated_files),
                    "errors": result.errors,
                    "warnings": result.warnings,
                    "ai_dialogue_log": result.ai_dialogue_log if request.include_code_samples else []
                },
                "quality_metrics": result.quality_metrics.model_dump() if result.quality_metrics and request.include_metrics else None,
                "generated_files": [
                    {
                        "path": f.path,
                        "type": f.file_type,
                        "description": f.description,
                        "size_bytes": f.size_bytes,
                        "content": f.content if request.include_code_samples else None
                    }
                    for f in result.generated_files
                ]
            }
            
            # Write JSON report
            with open(report_path, 'w', encoding='utf-8') as f:
                json.dump(report_data, f, indent=2, ensure_ascii=False)
            
            return report_path
            
        except Exception as e:
            dependencies.log_error("Failed to generate JSON report", e)
            return None
    
    def _build_markdown_content(
        self,
        request: ReportRequest,
        dependencies: ServiceDependencies
    ) -> str:
        """Build markdown report content."""
        result = request.generation_result
        
        content = f"""# Application Generation Report

## 📋 Summary

**Application Name**: `{result.app_name}`  
**Status**: {result.status.upper()}  
**Generated**: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}  
**Duration**: {result.duration_seconds:.2f} seconds  

{result.message}

## 📊 Generation Statistics

- **Files Generated**: {len(result.generated_files)}
- **Errors**: {len(result.errors)}
- **Warnings**: {len(result.warnings)}

"""
        
        # Add errors section if any
        if result.errors:
            content += "## ❌ Errors\n\n"
            for error in result.errors:
                content += f"- {error}\n"
            content += "\n"
        
        # Add warnings section if any
        if result.warnings:
            content += "## ⚠️ Warnings\n\n"
            for warning in result.warnings:
                content += f"- {warning}\n"
            content += "\n"
        
        # Add quality metrics if available and requested
        if result.quality_metrics and request.include_metrics:
            metrics = result.quality_metrics
            content += f"""## 📈 Quality Metrics

- **Code Readability**: {metrics.code_readability_score:.2f}/1.0
- **Maintainability**: {metrics.maintainability_score:.2f}/1.0
- **Type Hint Completeness**: {metrics.type_hint_completeness:.2f}/1.0
- **Pydantic Compliance**: {metrics.pydantic_compliance_score:.2f}/1.0
- **Test Coverage**: {metrics.test_coverage_percentage:.1f}%
- **Security Vulnerabilities**: {metrics.security_vulnerabilities_found}
- **Performance Issues**: {metrics.performance_bottlenecks_found}

"""
        
        # Add generated files section
        content += "## 📁 Generated Files\n\n"
        
        # Group files by type
        files_by_type = {}
        for file in result.generated_files:
            file_type = file.file_type
            if file_type not in files_by_type:
                files_by_type[file_type] = []
            files_by_type[file_type].append(file)
        
        for file_type, files in files_by_type.items():
            content += f"### {file_type.title()} Files\n\n"
            for file in files:
                content += f"- **{file.path}**"
                if file.description:
                    content += f" - {file.description}"
                content += f" ({file.size_bytes} bytes)\n"
            content += "\n"
        
        # Add code samples if requested
        if request.include_code_samples and result.generated_files:
            content += "## 💻 Code Samples\n\n"
            
            # Show a few key files
            key_files = [f for f in result.generated_files if f.file_type == "python"][:3]
            
            for file in key_files:
                content += f"### {file.path}\n\n"
                if file.description:
                    content += f"{file.description}\n\n"
                
                content += f"```python\n{file.content}\n```\n\n"
        
        # Add AI dialogue log if available and requested
        if result.ai_dialogue_log and request.include_code_samples:
            content += "## 🤖 AI Generation Process\n\n"
            
            for entry in result.ai_dialogue_log:
                agent = entry.get("agent", "Unknown")
                timestamp = entry.get("timestamp", "")
                output = entry.get("output", {})
                
                content += f"### {agent} Agent\n\n"
                content += f"**Timestamp**: {timestamp}\n\n"
                
                if isinstance(output, dict):
                    for key, value in output.items():
                        content += f"- **{key}**: {value}\n"
                else:
                    content += f"Output: {output}\n"
                
                content += "\n"
        
        # Add footer
        content += f"""---

**Report Generated**: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}  
**Generator**: Django App Agent v0.1.0  
**Format**: Markdown
"""
        
        return content
