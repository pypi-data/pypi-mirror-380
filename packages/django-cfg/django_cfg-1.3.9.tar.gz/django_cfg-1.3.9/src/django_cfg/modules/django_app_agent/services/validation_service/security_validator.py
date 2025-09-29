"""
Security Validator for Django App Agent.

This module validates security patterns and identifies potential
security vulnerabilities in generated Django code.
"""

from typing import List, Dict, Any, Optional
import ast
import re

from pydantic import BaseModel, Field

from ...models.responses import GeneratedFile
from ..base import ServiceDependencies
from .models import ValidationIssue


class SecurityValidator(BaseModel):
    """Validates security patterns and identifies vulnerabilities."""
    
    security_rules: Dict[str, Dict[str, Any]] = Field(
        default_factory=lambda: {
            "sql_injection": {
                "description": "Prevent SQL injection vulnerabilities",
                "severity": "error"
            },
            "xss_protection": {
                "description": "Ensure XSS protection in templates",
                "severity": "error"
            },
            "csrf_protection": {
                "description": "CSRF protection should be enabled",
                "severity": "warning"
            },
            "secure_settings": {
                "description": "Security settings should be properly configured",
                "severity": "warning"
            },
            "input_validation": {
                "description": "User input should be properly validated",
                "severity": "warning"
            },
            "authentication_required": {
                "description": "Sensitive views should require authentication",
                "severity": "warning"
            }
        },
        description="Security validation rules"
    )

    async def validate_security(
        self,
        file: GeneratedFile,
        dependencies: ServiceDependencies
    ) -> List[ValidationIssue]:
        """Validate security patterns for a single file."""
        issues = []
        
        if file.file_type != "python":
            return issues
        
        try:
            tree = ast.parse(file.content)
            
            # Apply security checks
            issues.extend(self._check_sql_injection(file, tree, dependencies))
            issues.extend(self._check_authentication(file, tree, dependencies))
            issues.extend(self._check_input_validation(file, tree, dependencies))
            issues.extend(self._check_dangerous_functions(file, tree, dependencies))
            
        except SyntaxError:
            # Skip security validation if syntax is invalid
            pass
        except Exception as e:
            dependencies.log_error(f"Security validation failed for {file.path}", e)
        
        return issues
    
    def _check_sql_injection(
        self,
        file: GeneratedFile,
        tree: ast.AST,
        dependencies: ServiceDependencies
    ) -> List[ValidationIssue]:
        """Check for potential SQL injection vulnerabilities."""
        issues = []
        
        # Look for raw SQL usage
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                # Check for raw() method calls
                if (isinstance(node.func, ast.Attribute) and
                    node.func.attr == "raw"):
                    issues.append(ValidationIssue(
                        severity="warning",
                        category="security",
                        message="Raw SQL query detected - ensure parameters are properly escaped",
                        file_path=file.path,
                        line_number=node.lineno,
                        rule_id="raw_sql_usage",
                        suggestion="Use Django ORM or parameterized queries instead of raw SQL"
                    ))
                
                # Check for extra() method with potentially unsafe parameters
                if (isinstance(node.func, ast.Attribute) and
                    node.func.attr == "extra"):
                    issues.append(ValidationIssue(
                        severity="warning",
                        category="security",
                        message="QuerySet.extra() usage detected - ensure SQL is safe",
                        file_path=file.path,
                        line_number=node.lineno,
                        rule_id="extra_sql_usage",
                        suggestion="Prefer Django ORM methods over extra() when possible"
                    ))
        
        # Check for string formatting in SQL-like contexts
        content = file.content
        if re.search(r'["\'].*%s.*["\'].*%', content):
            issues.append(ValidationIssue(
                severity="warning",
                category="security",
                message="String formatting in SQL-like context detected",
                file_path=file.path,
                line_number=1,
                rule_id="string_format_sql",
                suggestion="Use parameterized queries instead of string formatting"
            ))
        
        return issues
    
    def _check_authentication(
        self,
        file: GeneratedFile,
        tree: ast.AST,
        dependencies: ServiceDependencies
    ) -> List[ValidationIssue]:
        """Check for proper authentication patterns."""
        issues = []
        
        # Check views for authentication decorators/mixins
        if "views.py" in file.path:
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    # Check for authentication decorators
                    has_auth_decorator = any(
                        (isinstance(dec, ast.Name) and dec.id == "login_required") or
                        (isinstance(dec, ast.Attribute) and dec.attr == "login_required")
                        for dec in node.decorator_list
                    )
                    
                    # Skip views that clearly don't need authentication
                    if not has_auth_decorator and not self._is_public_view(node.name):
                        issues.append(ValidationIssue(
                            severity="info",
                            category="security",
                            message=f"View '{node.name}' may need authentication",
                            file_path=file.path,
                            line_number=node.lineno,
                            rule_id="missing_authentication",
                            suggestion=f"Consider adding @login_required decorator to {node.name} if it handles sensitive data"
                        ))
                
                elif isinstance(node, ast.ClassDef):
                    # Check class-based views for LoginRequiredMixin
                    has_login_mixin = any(
                        isinstance(base, ast.Name) and base.id == "LoginRequiredMixin"
                        for base in node.bases
                    )
                    
                    if not has_login_mixin and not self._is_public_view(node.name):
                        issues.append(ValidationIssue(
                            severity="info",
                            category="security",
                            message=f"View class '{node.name}' may need authentication",
                            file_path=file.path,
                            line_number=node.lineno,
                            rule_id="missing_login_mixin",
                            suggestion=f"Consider adding LoginRequiredMixin to {node.name} if it handles sensitive data"
                        ))
        
        return issues
    
    def _check_input_validation(
        self,
        file: GeneratedFile,
        tree: ast.AST,
        dependencies: ServiceDependencies
    ) -> List[ValidationIssue]:
        """Check for proper input validation."""
        issues = []
        
        # Check forms for validation methods
        if "forms.py" in file.path:
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    is_form = any(
                        isinstance(base, ast.Attribute) and
                        base.attr in ["Form", "ModelForm"]
                        for base in node.bases
                    )
                    
                    if is_form:
                        # Check for clean methods
                        has_validation = any(
                            isinstance(item, ast.FunctionDef) and
                            (item.name.startswith("clean_") or item.name == "clean")
                            for item in node.body
                        )
                        
                        if not has_validation:
                            issues.append(ValidationIssue(
                                severity="info",
                                category="security",
                                message=f"Form '{node.name}' lacks custom validation",
                                file_path=file.path,
                                line_number=node.lineno,
                                rule_id="missing_form_validation",
                                suggestion=f"Consider adding clean_* methods to {node.name} for input validation"
                            ))
        
        return issues
    
    def _check_dangerous_functions(
        self,
        file: GeneratedFile,
        tree: ast.AST,
        dependencies: ServiceDependencies
    ) -> List[ValidationIssue]:
        """Check for usage of potentially dangerous functions."""
        issues = []
        
        dangerous_functions = {
            "eval": "Use of eval() can execute arbitrary code",
            "exec": "Use of exec() can execute arbitrary code", 
            "compile": "Use of compile() with user input can be dangerous",
            "__import__": "Dynamic imports can be security risks"
        }
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                func_name = None
                
                if isinstance(node.func, ast.Name):
                    func_name = node.func.id
                elif isinstance(node.func, ast.Attribute):
                    func_name = node.func.attr
                
                if func_name in dangerous_functions:
                    issues.append(ValidationIssue(
                        severity="error",
                        category="security",
                        message=f"Dangerous function '{func_name}' detected: {dangerous_functions[func_name]}",
                        file_path=file.path,
                        line_number=node.lineno,
                        rule_id="dangerous_function",
                        suggestion=f"Avoid using {func_name}() or ensure input is properly sanitized"
                    ))
        
        return issues
    
    def _is_public_view(self, view_name: str) -> bool:
        """Check if a view is likely meant to be public."""
        public_patterns = [
            "index", "home", "landing", "about", "contact",
            "login", "logout", "register", "signup",
            "public", "api", "health", "status"
        ]
        
        view_lower = view_name.lower()
        return any(pattern in view_lower for pattern in public_patterns)
