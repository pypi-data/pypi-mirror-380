"""
Django Best Practices Validator.

This module validates Django-specific patterns, conventions,
and best practices in generated code.
"""

from typing import List, Dict, Any, Optional
import ast
import re

from pydantic import BaseModel, Field

from ...models.responses import GeneratedFile
from ..base import ServiceDependencies
from .models import ValidationIssue


class DjangoValidator(BaseModel):
    """Validates Django best practices and conventions."""
    
    django_rules: Dict[str, Dict[str, Any]] = Field(
        default_factory=lambda: {
            "model_meta_class": {
                "description": "Models should have proper Meta class",
                "severity": "warning"
            },
            "model_string_representation": {
                "description": "Models should have __str__ method",
                "severity": "warning"
            },
            "admin_registration": {
                "description": "Admin classes should be properly registered",
                "severity": "info"
            },
            "url_naming": {
                "description": "URL patterns should have names",
                "severity": "warning"
            },
            "view_docstrings": {
                "description": "Views should have docstrings",
                "severity": "info"
            },
            "form_validation": {
                "description": "Forms should have proper validation",
                "severity": "warning"
            }
        },
        description="Django validation rules"
    )

    async def validate_django_practices(
        self,
        file: GeneratedFile,
        dependencies: ServiceDependencies
    ) -> List[ValidationIssue]:
        """Validate Django best practices for a single file."""
        issues = []
        
        if file.file_type != "python":
            return issues
        
        try:
            tree = ast.parse(file.content)
            
            # Determine file type and apply appropriate validations
            if "models.py" in file.path:
                issues.extend(self._validate_models(file, tree, dependencies))
            elif "admin.py" in file.path:
                issues.extend(self._validate_admin(file, tree, dependencies))
            elif "views.py" in file.path:
                issues.extend(self._validate_views(file, tree, dependencies))
            elif "urls.py" in file.path:
                issues.extend(self._validate_urls(file, tree, dependencies))
            elif "forms.py" in file.path:
                issues.extend(self._validate_forms(file, tree, dependencies))
            elif "serializers.py" in file.path:
                issues.extend(self._validate_serializers(file, tree, dependencies))
            
        except SyntaxError:
            # Skip Django validation if syntax is invalid
            pass
        except Exception as e:
            dependencies.log_error(f"Django validation failed for {file.path}", e)
        
        return issues
    
    def _validate_models(
        self,
        file: GeneratedFile,
        tree: ast.AST,
        dependencies: ServiceDependencies
    ) -> List[ValidationIssue]:
        """Validate Django model best practices."""
        issues = []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                # Check if it's a model class
                is_model = any(
                    isinstance(base, ast.Attribute) and 
                    isinstance(base.value, ast.Name) and
                    base.value.id == "models" and
                    base.attr == "Model"
                    for base in node.bases
                ) or any(
                    isinstance(base, ast.Name) and
                    "Model" in base.id
                    for base in node.bases
                )
                
                if is_model:
                    issues.extend(self._check_model_class(file, node))
        
        return issues
    
    def _check_model_class(
        self,
        file: GeneratedFile,
        node: ast.ClassDef
    ) -> List[ValidationIssue]:
        """Check individual model class for best practices."""
        issues = []
        
        # Check for __str__ method
        has_str_method = any(
            isinstance(item, ast.FunctionDef) and item.name == "__str__"
            for item in node.body
        )
        
        if not has_str_method:
            issues.append(ValidationIssue(
                severity="warning",
                category="django",
                message=f"Model '{node.name}' should have a __str__ method",
                file_path=file.path,
                line_number=node.lineno,
                rule_id="model_str_method",
                suggestion=f"Add a __str__ method to {node.name} that returns a meaningful string representation"
            ))
        
        # Check for Meta class
        has_meta_class = any(
            isinstance(item, ast.ClassDef) and item.name == "Meta"
            for item in node.body
        )
        
        if not has_meta_class:
            issues.append(ValidationIssue(
                severity="info",
                category="django",
                message=f"Model '{node.name}' could benefit from a Meta class",
                file_path=file.path,
                line_number=node.lineno,
                rule_id="model_meta_class",
                suggestion=f"Consider adding a Meta class to {node.name} for verbose_name, ordering, etc."
            ))
        
        return issues
    
    def _validate_admin(
        self,
        file: GeneratedFile,
        tree: ast.AST,
        dependencies: ServiceDependencies
    ) -> List[ValidationIssue]:
        """Validate Django admin best practices."""
        issues = []
        
        # Check for admin registrations
        has_registrations = False
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                # Check for admin.site.register() calls
                if (isinstance(node.func, ast.Attribute) and
                    isinstance(node.func.value, ast.Attribute) and
                    isinstance(node.func.value.value, ast.Name) and
                    node.func.value.value.id == "admin" and
                    node.func.value.attr == "site" and
                    node.func.attr == "register"):
                    has_registrations = True
            elif isinstance(node, ast.FunctionDef):
                # Check for @admin.register decorator
                for decorator in node.decorator_list:
                    if (isinstance(decorator, ast.Call) and
                        isinstance(decorator.func, ast.Attribute) and
                        isinstance(decorator.func.value, ast.Name) and
                        decorator.func.value.id == "admin" and
                        decorator.func.attr == "register"):
                        has_registrations = True
        
        if not has_registrations:
            issues.append(ValidationIssue(
                severity="info",
                category="django",
                message="No admin registrations found",
                file_path=file.path,
                line_number=1,
                rule_id="admin_registration",
                suggestion="Register models with admin.site.register() or @admin.register decorator"
            ))
        
        return issues
    
    def _validate_views(
        self,
        file: GeneratedFile,
        tree: ast.AST,
        dependencies: ServiceDependencies
    ) -> List[ValidationIssue]:
        """Validate Django view best practices."""
        issues = []
        
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                # Check for docstrings
                if not ast.get_docstring(node):
                    issues.append(ValidationIssue(
                        severity="info",
                        category="django",
                        message=f"View '{node.name}' should have a docstring",
                        file_path=file.path,
                        line_number=node.lineno,
                        rule_id="view_docstring",
                        suggestion=f"Add a docstring to {node.name} explaining its purpose"
                    ))
        
        return issues
    
    def _validate_urls(
        self,
        file: GeneratedFile,
        tree: ast.AST,
        dependencies: ServiceDependencies
    ) -> List[ValidationIssue]:
        """Validate Django URL patterns best practices."""
        issues = []
        
        # Check for named URL patterns
        content = file.content
        path_patterns = re.findall(r'path\([^)]+\)', content)
        
        for pattern in path_patterns:
            if 'name=' not in pattern:
                issues.append(ValidationIssue(
                    severity="warning",
                    category="django",
                    message="URL pattern should have a name",
                    file_path=file.path,
                    line_number=1,  # Would need more sophisticated line tracking
                    rule_id="url_naming",
                    suggestion="Add name='...' parameter to path() for reverse URL lookup"
                ))
        
        return issues
    
    def _validate_forms(
        self,
        file: GeneratedFile,
        tree: ast.AST,
        dependencies: ServiceDependencies
    ) -> List[ValidationIssue]:
        """Validate Django form best practices."""
        issues = []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                # Check if it's a form class
                is_form = any(
                    isinstance(base, ast.Attribute) and
                    base.attr in ["Form", "ModelForm"]
                    for base in node.bases
                )
                
                if is_form:
                    # Check for clean methods
                    has_clean_methods = any(
                        isinstance(item, ast.FunctionDef) and 
                        (item.name.startswith("clean_") or item.name == "clean")
                        for item in node.body
                    )
                    
                    if not has_clean_methods:
                        issues.append(ValidationIssue(
                            severity="info",
                            category="django",
                            message=f"Form '{node.name}' could benefit from validation methods",
                            file_path=file.path,
                            line_number=node.lineno,
                            rule_id="form_validation",
                            suggestion=f"Consider adding clean_* methods to {node.name} for field validation"
                        ))
        
        return issues
    
    def _validate_serializers(
        self,
        file: GeneratedFile,
        tree: ast.AST,
        dependencies: ServiceDependencies
    ) -> List[ValidationIssue]:
        """Validate DRF serializer best practices."""
        issues = []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                # Check if it's a serializer class
                is_serializer = any(
                    isinstance(base, ast.Attribute) and
                    "Serializer" in base.attr
                    for base in node.bases
                )
                
                if is_serializer:
                    # Check for Meta class in ModelSerializer
                    has_meta = any(
                        isinstance(item, ast.ClassDef) and item.name == "Meta"
                        for item in node.body
                    )
                    
                    if "ModelSerializer" in str(node.bases) and not has_meta:
                        issues.append(ValidationIssue(
                            severity="warning",
                            category="django",
                            message=f"ModelSerializer '{node.name}' should have a Meta class",
                            file_path=file.path,
                            line_number=node.lineno,
                            rule_id="serializer_meta",
                            suggestion=f"Add Meta class to {node.name} with model and fields"
                        ))
        
        return issues
