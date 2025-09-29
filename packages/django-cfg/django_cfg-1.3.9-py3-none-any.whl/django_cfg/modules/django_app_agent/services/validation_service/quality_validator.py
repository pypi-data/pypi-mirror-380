"""
Code Quality Validator for Django App Agent.

This module validates code quality metrics, patterns,
and maintainability aspects of generated code.
"""

from typing import List, Dict, Any, Optional
import ast
import re

from pydantic import BaseModel, Field

from ...models.responses import GeneratedFile, QualityMetrics
from ..base import ServiceDependencies
from .models import ValidationIssue


class QualityValidator(BaseModel):
    """Validates code quality and maintainability patterns."""
    
    quality_rules: Dict[str, Dict[str, Any]] = Field(
        default_factory=lambda: {
            "function_complexity": {
                "description": "Functions should not be overly complex",
                "severity": "warning",
                "max_complexity": 10
            },
            "line_length": {
                "description": "Lines should not exceed reasonable length",
                "severity": "warning",
                "max_length": 120
            },
            "docstring_coverage": {
                "description": "Classes and functions should have docstrings",
                "severity": "info"
            },
            "type_hints": {
                "description": "Functions should have type hints",
                "severity": "info"
            },
            "naming_conventions": {
                "description": "Follow Python naming conventions",
                "severity": "warning"
            },
            "code_duplication": {
                "description": "Avoid code duplication",
                "severity": "warning"
            }
        },
        description="Code quality validation rules"
    )

    async def validate_quality(
        self,
        file: GeneratedFile,
        dependencies: ServiceDependencies
    ) -> List[ValidationIssue]:
        """Validate code quality for a single file."""
        issues = []
        
        if file.file_type != "python":
            return issues
        
        try:
            tree = ast.parse(file.content)
            
            # Apply quality checks
            issues.extend(self._check_complexity(file, tree, dependencies))
            issues.extend(self._check_line_length(file, dependencies))
            issues.extend(self._check_docstrings(file, tree, dependencies))
            issues.extend(self._check_type_hints(file, tree, dependencies))
            issues.extend(self._check_naming_conventions(file, tree, dependencies))
            issues.extend(self._check_code_duplication(file, tree, dependencies))
            
        except SyntaxError:
            # Skip quality validation if syntax is invalid
            pass
        except Exception as e:
            dependencies.log_error(f"Quality validation failed for {file.path}", e)
        
        return issues
    
    async def calculate_quality_metrics(
        self,
        files: List[GeneratedFile],
        dependencies: ServiceDependencies
    ) -> QualityMetrics:
        """Calculate comprehensive quality metrics."""
        total_lines = 0
        total_functions = 0
        functions_with_docstrings = 0
        functions_with_type_hints = 0
        classes_with_docstrings = 0
        total_classes = 0
        complexity_scores = []
        
        for file in files:
            if file.file_type != "python":
                continue
                
            try:
                tree = ast.parse(file.content)
                lines = file.content.split('\n')
                total_lines += len([line for line in lines if line.strip()])
                
                for node in ast.walk(tree):
                    if isinstance(node, ast.FunctionDef):
                        total_functions += 1
                        
                        # Check docstring
                        if ast.get_docstring(node):
                            functions_with_docstrings += 1
                        
                        # Check type hints
                        if self._has_type_hints(node):
                            functions_with_type_hints += 1
                        
                        # Calculate complexity
                        complexity = self._calculate_cyclomatic_complexity(node)
                        complexity_scores.append(complexity)
                    
                    elif isinstance(node, ast.ClassDef):
                        total_classes += 1
                        if ast.get_docstring(node):
                            classes_with_docstrings += 1
                            
            except SyntaxError:
                continue
        
        # Calculate metrics
        docstring_coverage = 0.0
        if total_functions + total_classes > 0:
            docstring_coverage = (functions_with_docstrings + classes_with_docstrings) / (total_functions + total_classes) * 100
        
        type_hint_coverage = 0.0
        if total_functions > 0:
            type_hint_coverage = functions_with_type_hints / total_functions * 100
        
        avg_complexity = sum(complexity_scores) / len(complexity_scores) if complexity_scores else 0
        
        # Calculate overall scores
        overall_score = (docstring_coverage * 0.2 + type_hint_coverage * 0.3 + 
                        max(0, 100 - avg_complexity * 10) * 0.5) / 10
        
        return QualityMetrics(
            overall_score=min(10.0, max(0.0, overall_score)),
            type_safety_score=min(10.0, type_hint_coverage / 10),
            pattern_consistency=8.5,  # Would need more sophisticated analysis
            code_complexity=max(0.0, 10.0 - avg_complexity),
            test_coverage=0.0,  # Would need test analysis
            documentation_coverage=min(100.0, docstring_coverage),  # Keep as percentage
            performance_score=8.0,  # Would need performance analysis
            security_score=8.5,  # Would need security analysis
            maintainability_score=min(10.0, max(0.0, overall_score))
        )
    
    def _check_complexity(
        self,
        file: GeneratedFile,
        tree: ast.AST,
        dependencies: ServiceDependencies
    ) -> List[ValidationIssue]:
        """Check cyclomatic complexity of functions."""
        issues = []
        max_complexity = self.quality_rules["function_complexity"]["max_complexity"]
        
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                complexity = self._calculate_cyclomatic_complexity(node)
                
                if complexity > max_complexity:
                    issues.append(ValidationIssue(
                        severity="warning",
                        category="quality",
                        message=f"Function '{node.name}' has high complexity ({complexity})",
                        file_path=file.path,
                        line_number=node.lineno,
                        rule_id="high_complexity",
                        suggestion=f"Consider breaking down {node.name} into smaller functions"
                    ))
        
        return issues
    
    def _check_line_length(
        self,
        file: GeneratedFile,
        dependencies: ServiceDependencies
    ) -> List[ValidationIssue]:
        """Check for overly long lines."""
        issues = []
        max_length = self.quality_rules["line_length"]["max_length"]
        
        lines = file.content.split('\n')
        for i, line in enumerate(lines, 1):
            if len(line) > max_length:
                issues.append(ValidationIssue(
                    severity="info",
                    category="quality",
                    message=f"Line {i} exceeds {max_length} characters ({len(line)})",
                    file_path=file.path,
                    line_number=i,
                    rule_id="line_too_long",
                    suggestion="Break long lines for better readability"
                ))
        
        return issues
    
    def _check_docstrings(
        self,
        file: GeneratedFile,
        tree: ast.AST,
        dependencies: ServiceDependencies
    ) -> List[ValidationIssue]:
        """Check for missing docstrings."""
        issues = []
        
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                if not ast.get_docstring(node):
                    node_type = "Class" if isinstance(node, ast.ClassDef) else "Function"
                    issues.append(ValidationIssue(
                        severity="info",
                        category="quality",
                        message=f"{node_type} '{node.name}' lacks docstring",
                        file_path=file.path,
                        line_number=node.lineno,
                        rule_id="missing_docstring",
                        suggestion=f"Add a docstring to {node.name} explaining its purpose"
                    ))
        
        return issues
    
    def _check_type_hints(
        self,
        file: GeneratedFile,
        tree: ast.AST,
        dependencies: ServiceDependencies
    ) -> List[ValidationIssue]:
        """Check for missing type hints."""
        issues = []
        
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                if not self._has_type_hints(node):
                    issues.append(ValidationIssue(
                        severity="info",
                        category="quality",
                        message=f"Function '{node.name}' lacks type hints",
                        file_path=file.path,
                        line_number=node.lineno,
                        rule_id="missing_type_hints",
                        suggestion=f"Add type hints to {node.name} parameters and return value"
                    ))
        
        return issues
    
    def _check_naming_conventions(
        self,
        file: GeneratedFile,
        tree: ast.AST,
        dependencies: ServiceDependencies
    ) -> List[ValidationIssue]:
        """Check Python naming conventions."""
        issues = []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                # Class names should be PascalCase
                if not re.match(r'^[A-Z][a-zA-Z0-9]*$', node.name):
                    issues.append(ValidationIssue(
                        severity="warning",
                        category="quality",
                        message=f"Class '{node.name}' should use PascalCase",
                        file_path=file.path,
                        line_number=node.lineno,
                        rule_id="class_naming",
                        suggestion=f"Rename {node.name} to follow PascalCase convention"
                    ))
            
            elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                # Function names should be snake_case
                if not re.match(r'^[a-z_][a-z0-9_]*$', node.name) and not node.name.startswith('__'):
                    issues.append(ValidationIssue(
                        severity="warning",
                        category="quality",
                        message=f"Function '{node.name}' should use snake_case",
                        file_path=file.path,
                        line_number=node.lineno,
                        rule_id="function_naming",
                        suggestion=f"Rename {node.name} to follow snake_case convention"
                    ))
        
        return issues
    
    def _check_code_duplication(
        self,
        file: GeneratedFile,
        tree: ast.AST,
        dependencies: ServiceDependencies
    ) -> List[ValidationIssue]:
        """Check for code duplication patterns."""
        issues = []
        
        # Simple duplication check - look for identical function bodies
        function_bodies = {}
        
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                # Convert function body to string for comparison
                body_str = ast.dump(node.body)
                
                if body_str in function_bodies:
                    issues.append(ValidationIssue(
                        severity="warning",
                        category="quality",
                        message=f"Function '{node.name}' has duplicate body with '{function_bodies[body_str]}'",
                        file_path=file.path,
                        line_number=node.lineno,
                        rule_id="code_duplication",
                        suggestion=f"Consider extracting common logic from {node.name} and {function_bodies[body_str]}"
                    ))
                else:
                    function_bodies[body_str] = node.name
        
        return issues
    
    def _calculate_cyclomatic_complexity(self, node: ast.AST) -> int:
        """Calculate cyclomatic complexity of a function."""
        complexity = 1  # Base complexity
        
        for child in ast.walk(node):
            if isinstance(child, (ast.If, ast.While, ast.For, ast.AsyncFor)):
                complexity += 1
            elif isinstance(child, ast.ExceptHandler):
                complexity += 1
            elif isinstance(child, (ast.And, ast.Or)):
                complexity += 1
            elif isinstance(child, ast.comprehension):
                complexity += 1
        
        return complexity
    
    def _has_type_hints(self, node: ast.FunctionDef) -> bool:
        """Check if function has type hints."""
        # Check return annotation
        has_return_hint = node.returns is not None
        
        # Check parameter annotations
        has_param_hints = any(arg.annotation is not None for arg in node.args.args)
        
        return has_return_hint or has_param_hints
