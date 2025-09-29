"""
Syntax Validator for Django App Agent.

This module provides Python syntax validation and AST analysis
for generated code files.
"""

from typing import List, Dict, Any, Optional
import ast
import re

from pydantic import BaseModel, Field

from ...models.responses import GeneratedFile
from ..base import ServiceDependencies
from .models import ValidationIssue


class SyntaxValidator(BaseModel):
    """Validates Python syntax and performs AST analysis."""
    
    syntax_rules: Dict[str, Dict[str, Any]] = Field(
        default_factory=lambda: {
            "valid_python": {
                "description": "Code must be valid Python syntax",
                "severity": "error"
            },
            "no_syntax_errors": {
                "description": "No syntax errors allowed",
                "severity": "error"
            },
            "proper_indentation": {
                "description": "Code must use consistent indentation",
                "severity": "warning"
            },
            "no_unused_imports": {
                "description": "No unused imports allowed",
                "severity": "warning"
            }
        },
        description="Syntax validation rules"
    )

    async def validate_syntax(
        self,
        file: GeneratedFile,
        dependencies: ServiceDependencies
    ) -> List[ValidationIssue]:
        """Validate Python syntax for a single file."""
        issues = []
        
        if file.file_type != "python":
            return issues
        
        try:
            # Parse the AST
            tree = ast.parse(file.content)
            
            # Check for syntax issues
            issues.extend(self._check_ast_structure(file, tree, dependencies))
            issues.extend(self._check_imports(file, tree, dependencies))
            issues.extend(self._check_indentation(file, dependencies))
            
        except SyntaxError as e:
            issues.append(ValidationIssue(
                severity="error",
                category="syntax",
                message=f"Syntax error: {e.msg}",
                file_path=file.path,
                line_number=e.lineno or 1,
                column=e.offset,
                rule_id="syntax_error",
                suggestion="Fix the syntax error according to Python grammar rules"
            ))
        except Exception as e:
            issues.append(ValidationIssue(
                severity="error",
                category="syntax",
                message=f"Failed to parse file: {e}",
                file_path=file.path,
                line_number=1,
                rule_id="parse_error"
            ))
        
        return issues
    
    def _check_ast_structure(
        self,
        file: GeneratedFile,
        tree: ast.AST,
        dependencies: ServiceDependencies
    ) -> List[ValidationIssue]:
        """Check AST structure for common issues."""
        issues = []
        
        # Check for empty classes/functions
        for node in ast.walk(tree):
            if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
                if len(node.body) == 1 and isinstance(node.body[0], ast.Pass):
                    issues.append(ValidationIssue(
                        severity="warning",
                        category="syntax",
                        message=f"Empty {type(node).__name__.lower()} '{node.name}' with only 'pass'",
                        file_path=file.path,
                        line_number=node.lineno,
                        rule_id="empty_definition",
                        suggestion=f"Add implementation or docstring to {node.name}"
                    ))
        
        return issues
    
    def _check_imports(
        self,
        file: GeneratedFile,
        tree: ast.AST,
        dependencies: ServiceDependencies
    ) -> List[ValidationIssue]:
        """Check import statements for issues."""
        issues = []
        
        # Collect all imports and their usage
        imports = set()
        used_names = set()
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    import_name = alias.asname or alias.name
                    imports.add(import_name)
            elif isinstance(node, ast.ImportFrom):
                for alias in node.names:
                    import_name = alias.asname or alias.name
                    imports.add(import_name)
            elif isinstance(node, ast.Name):
                used_names.add(node.id)
            elif isinstance(node, ast.Attribute):
                # Handle attribute access like 'models.Model'
                if isinstance(node.value, ast.Name):
                    used_names.add(node.value.id)
        
        # Check for unused imports
        unused_imports = imports - used_names
        for unused in unused_imports:
            # Skip common Django imports that might be used in templates
            if unused not in ['models', 'admin', 'forms', 'serializers']:
                issues.append(ValidationIssue(
                    severity="warning",
                    category="syntax",
                    message=f"Unused import: {unused}",
                    file_path=file.path,
                    line_number=1,  # Would need more sophisticated tracking for exact line
                    rule_id="unused_import",
                    suggestion=f"Remove unused import '{unused}' or use it in the code"
                ))
        
        return issues
    
    def _check_indentation(
        self,
        file: GeneratedFile,
        dependencies: ServiceDependencies
    ) -> List[ValidationIssue]:
        """Check for consistent indentation."""
        issues = []
        lines = file.content.split('\n')
        
        # Check for mixed tabs and spaces
        has_tabs = any('\t' in line for line in lines)
        has_spaces = any(line.startswith('    ') for line in lines)
        
        if has_tabs and has_spaces:
            issues.append(ValidationIssue(
                severity="warning",
                category="syntax",
                message="Mixed tabs and spaces for indentation",
                file_path=file.path,
                line_number=1,
                rule_id="mixed_indentation",
                suggestion="Use consistent indentation (preferably 4 spaces)"
            ))
        
        # Check for inconsistent indentation levels
        indent_levels = set()
        for i, line in enumerate(lines, 1):
            if line.strip():  # Skip empty lines
                leading_spaces = len(line) - len(line.lstrip(' '))
                if leading_spaces > 0:
                    indent_levels.add(leading_spaces)
        
        # Check if indentation follows 4-space rule
        non_standard_indents = [level for level in indent_levels if level % 4 != 0]
        if non_standard_indents:
            issues.append(ValidationIssue(
                severity="info",
                category="syntax",
                message=f"Non-standard indentation levels found: {non_standard_indents}",
                file_path=file.path,
                line_number=1,
                rule_id="non_standard_indent",
                suggestion="Use 4-space indentation consistently"
            ))
        
        return issues
