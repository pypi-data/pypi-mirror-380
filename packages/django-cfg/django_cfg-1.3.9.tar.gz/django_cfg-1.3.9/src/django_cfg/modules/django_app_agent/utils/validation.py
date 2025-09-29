"""
Validation utilities for Django App Agent Module.

This module provides comprehensive validation functions for:
- Django app names and identifiers
- File paths and names
- Python code validation
- Input sanitization
"""

import re
import keyword
from typing import List, Optional, Tuple
from pathlib import Path

from ..core.exceptions import ValidationError


# Regular expressions for validation
APP_NAME_PATTERN = re.compile(r'^[a-z][a-z0-9_]*$')
PYTHON_IDENTIFIER_PATTERN = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*$')
SAFE_FILENAME_PATTERN = re.compile(r'^[a-zA-Z0-9._-]+$')

# Reserved Django app names
RESERVED_APP_NAMES = {
    'admin', 'auth', 'contenttypes', 'sessions', 'messages', 'staticfiles',
    'django', 'test', 'tests', 'migrations', 'management', 'locale',
    'fixtures', 'templates', 'static', 'media'
}

# Reserved Python keywords and builtins
RESERVED_PYTHON_NAMES = set(keyword.kwlist) | {
    'True', 'False', 'None', '__builtins__', '__name__', '__file__',
    'int', 'str', 'list', 'dict', 'tuple', 'set', 'bool', 'float'
}


def validate_app_name(name: str, *, check_reserved: bool = True) -> str:
    """Validate Django application name.
    
    Args:
        name: Application name to validate
        check_reserved: Whether to check against reserved names
        
    Returns:
        Validated and normalized app name
        
    Raises:
        ValidationError: If name is invalid
    """
    if not name:
        raise ValidationError(
            "App name cannot be empty",
            validation_type="app_name",
            field_name="name",
            field_value=name
        )
    
    # Normalize name
    normalized_name = name.strip().lower()
    
    # Check length
    if len(normalized_name) < 2:
        raise ValidationError(
            "App name must be at least 2 characters long",
            validation_type="app_name",
            field_name="name",
            field_value=name
        )
    
    if len(normalized_name) > 50:
        raise ValidationError(
            "App name must be no more than 50 characters long",
            validation_type="app_name",
            field_name="name",
            field_value=name
        )
    
    # Check pattern
    if not APP_NAME_PATTERN.match(normalized_name):
        raise ValidationError(
            "App name must start with a letter and contain only lowercase letters, numbers, and underscores",
            validation_type="app_name",
            field_name="name",
            field_value=name
        )
    
    # Check reserved names
    if check_reserved and normalized_name in RESERVED_APP_NAMES:
        raise ValidationError(
            f"'{normalized_name}' is a reserved Django app name",
            validation_type="app_name",
            field_name="name",
            field_value=name
        )
    
    # Check Python keywords
    if normalized_name in RESERVED_PYTHON_NAMES:
        raise ValidationError(
            f"'{normalized_name}' is a reserved Python keyword",
            validation_type="app_name",
            field_name="name",
            field_value=name
        )
    
    return normalized_name


def validate_python_identifier(identifier: str, *, context: str = "identifier") -> str:
    """Validate Python identifier (variable, class, function name).
    
    Args:
        identifier: Identifier to validate
        context: Context for error messages
        
    Returns:
        Validated identifier
        
    Raises:
        ValidationError: If identifier is invalid
    """
    if not identifier:
        raise ValidationError(
            f"Python {context} cannot be empty",
            validation_type="python_identifier",
            field_name=context,
            field_value=identifier
        )
    
    # Check pattern
    if not PYTHON_IDENTIFIER_PATTERN.match(identifier):
        raise ValidationError(
            f"Python {context} must start with a letter or underscore and contain only letters, numbers, and underscores",
            validation_type="python_identifier",
            field_name=context,
            field_value=identifier
        )
    
    # Check keywords
    if keyword.iskeyword(identifier):
        raise ValidationError(
            f"'{identifier}' is a reserved Python keyword",
            validation_type="python_identifier",
            field_name=context,
            field_value=identifier
        )
    
    # Check builtins
    if identifier in RESERVED_PYTHON_NAMES:
        raise ValidationError(
            f"'{identifier}' is a reserved Python name",
            validation_type="python_identifier",
            field_name=context,
            field_value=identifier
        )
    
    return identifier


def validate_file_path(
    path: Path,
    *,
    must_exist: bool = False,
    must_be_dir: bool = False,
    must_be_file: bool = False,
    create_parents: bool = False
) -> Path:
    """Validate file or directory path.
    
    Args:
        path: Path to validate
        must_exist: Whether path must exist
        must_be_dir: Whether path must be a directory
        must_be_file: Whether path must be a file
        create_parents: Whether to create parent directories
        
    Returns:
        Validated path
        
    Raises:
        ValidationError: If path is invalid
    """
    if not isinstance(path, Path):
        try:
            path = Path(path)
        except Exception as e:
            raise ValidationError(
                f"Invalid path format: {e}",
                validation_type="file_path",
                field_name="path",
                field_value=str(path),
                cause=e
            )
    
    # Resolve path
    try:
        resolved_path = path.resolve()
    except Exception as e:
        raise ValidationError(
            f"Cannot resolve path: {e}",
            validation_type="file_path",
            field_name="path",
            field_value=str(path),
            cause=e
        )
    
    # Check existence
    if must_exist and not resolved_path.exists():
        raise ValidationError(
            f"Path does not exist: {resolved_path}",
            validation_type="file_path",
            field_name="path",
            field_value=str(path)
        )
    
    # Check type constraints
    if resolved_path.exists():
        if must_be_dir and not resolved_path.is_dir():
            raise ValidationError(
                f"Path is not a directory: {resolved_path}",
                validation_type="file_path",
                field_name="path",
                field_value=str(path)
            )
        
        if must_be_file and not resolved_path.is_file():
            raise ValidationError(
                f"Path is not a file: {resolved_path}",
                validation_type="file_path",
                field_name="path",
                field_value=str(path)
            )
    
    # Create parent directories if requested
    if create_parents and not resolved_path.parent.exists():
        try:
            resolved_path.parent.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            raise ValidationError(
                f"Cannot create parent directories: {e}",
                validation_type="file_path",
                field_name="path",
                field_value=str(path),
                cause=e
            )
    
    return resolved_path


def sanitize_filename(filename: str, *, max_length: int = 255) -> str:
    """Sanitize filename for safe file system usage.
    
    Args:
        filename: Filename to sanitize
        max_length: Maximum filename length
        
    Returns:
        Sanitized filename
        
    Raises:
        ValidationError: If filename cannot be sanitized
    """
    if not filename:
        raise ValidationError(
            "Filename cannot be empty",
            validation_type="filename",
            field_name="filename",
            field_value=filename
        )
    
    # Remove or replace unsafe characters
    sanitized = re.sub(r'[<>:"/\\|?*]', '_', filename)
    
    # Remove control characters
    sanitized = re.sub(r'[\x00-\x1f\x7f]', '', sanitized)
    
    # Trim whitespace
    sanitized = sanitized.strip()
    
    # Handle reserved Windows names
    reserved_windows = {
        'CON', 'PRN', 'AUX', 'NUL',
        'COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8', 'COM9',
        'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LPT7', 'LPT8', 'LPT9'
    }
    
    name_part = sanitized.split('.')[0].upper()
    if name_part in reserved_windows:
        sanitized = f"_{sanitized}"
    
    # Ensure not empty after sanitization
    if not sanitized:
        raise ValidationError(
            "Filename becomes empty after sanitization",
            validation_type="filename",
            field_name="filename",
            field_value=filename
        )
    
    # Check length
    if len(sanitized) > max_length:
        # Try to preserve extension
        if '.' in sanitized:
            name, ext = sanitized.rsplit('.', 1)
            max_name_length = max_length - len(ext) - 1
            if max_name_length > 0:
                sanitized = f"{name[:max_name_length]}.{ext}"
            else:
                sanitized = sanitized[:max_length]
        else:
            sanitized = sanitized[:max_length]
    
    return sanitized


def validate_description(description: str, *, min_length: int = 10, max_length: int = 500) -> str:
    """Validate application description.
    
    Args:
        description: Description to validate
        min_length: Minimum description length
        max_length: Maximum description length
        
    Returns:
        Validated description
        
    Raises:
        ValidationError: If description is invalid
    """
    if not description:
        raise ValidationError(
            "Description cannot be empty",
            validation_type="description",
            field_name="description",
            field_value=description
        )
    
    # Normalize whitespace
    normalized = ' '.join(description.split())
    
    # Check length
    if len(normalized) < min_length:
        raise ValidationError(
            f"Description must be at least {min_length} characters long",
            validation_type="description",
            field_name="description",
            field_value=description
        )
    
    if len(normalized) > max_length:
        raise ValidationError(
            f"Description must be no more than {max_length} characters long",
            validation_type="description",
            field_name="description",
            field_value=description
        )
    
    return normalized


def validate_existing_apps(
    app_name: str,
    existing_apps: List[str],
    *,
    case_sensitive: bool = False
) -> None:
    """Validate that app name doesn't conflict with existing apps.
    
    Args:
        app_name: New app name to check
        existing_apps: List of existing app names
        case_sensitive: Whether comparison should be case sensitive
        
    Raises:
        ValidationError: If app name conflicts with existing apps
    """
    if not case_sensitive:
        existing_lower = [app.lower() for app in existing_apps]
        if app_name.lower() in existing_lower:
            # Find the actual conflicting app name
            for existing_app in existing_apps:
                if existing_app.lower() == app_name.lower():
                    raise ValidationError(
                        f"App '{app_name}' conflicts with existing app '{existing_app}'",
                        validation_type="app_name_conflict",
                        field_name="app_name",
                        field_value=app_name
                    )
    else:
        if app_name in existing_apps:
            raise ValidationError(
                f"App '{app_name}' already exists",
                validation_type="app_name_conflict",
                field_name="app_name",
                field_value=app_name
            )


def validate_python_code(code: str, *, filename: str = "<generated>") -> Tuple[bool, Optional[str]]:
    """Validate Python code syntax.
    
    Args:
        code: Python code to validate
        filename: Filename for error reporting
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    try:
        compile(code, filename, 'exec')
        return True, None
    except SyntaxError as e:
        error_msg = f"Syntax error in {filename} at line {e.lineno}: {e.msg}"
        return False, error_msg
    except Exception as e:
        error_msg = f"Compilation error in {filename}: {e}"
        return False, error_msg
