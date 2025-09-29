"""
Base Pydantic 2 models for Django App Agent Module.

This module provides base classes and common patterns for all models:
- Strict validation configuration
- Timestamp handling
- Common field patterns
- Serialization utilities
"""

from typing import Any, Dict, Optional, ClassVar
from datetime import datetime, timezone
from pydantic import BaseModel, Field, ConfigDict, field_validator
from uuid import uuid4


class BaseAgentModel(BaseModel):
    """Base model for all Django App Agent data structures.
    
    Provides:
    - Strict validation (no extra fields, assignment validation)
    - Consistent configuration across all models
    - Common utility methods
    - Proper JSON serialization
    """
    
    model_config = ConfigDict(
        # Strict validation - no extra fields allowed
        extra='forbid',
        # Validate on assignment (not just initialization)
        validate_assignment=True,
        # Strip whitespace from strings
        str_strip_whitespace=True,
        # Use enum values in serialization
        use_enum_values=True,
        # Validate default values
        validate_default=True,
        # Allow arbitrary types for complex objects
        arbitrary_types_allowed=False,
        # Frozen models are immutable (can be overridden)
        frozen=False,
    )
    
    def model_dump_safe(self) -> Dict[str, Any]:
        """Safe model dump that handles all edge cases.
        
        Returns:
            Dictionary representation safe for JSON serialization
        """
        return self.model_dump(
            mode='json',
            exclude_none=False,
            by_alias=True
        )
    
    def model_dump_minimal(self) -> Dict[str, Any]:
        """Minimal model dump excluding None values and defaults.
        
        Returns:
            Minimal dictionary representation
        """
        return self.model_dump(
            mode='json',
            exclude_none=True,
            exclude_defaults=True,
            by_alias=True
        )
    
    @classmethod
    def model_validate_safe(cls, data: Any) -> "BaseAgentModel":
        """Safe model validation with better error handling.
        
        Args:
            data: Data to validate
            
        Returns:
            Validated model instance
            
        Raises:
            ValidationError: With enhanced error context
        """
        from ..core.exceptions import ValidationError
        
        try:
            return cls.model_validate(data)
        except Exception as e:
            raise ValidationError(
                f"Failed to validate {cls.__name__}: {e}",
                validation_type="model_validation",
                field_name=cls.__name__,
                field_value=str(data)[:200],  # Truncate for logging
                cause=e
            )


class TimestampedModel(BaseAgentModel):
    """Base model with automatic timestamp handling.
    
    Provides:
    - Automatic created_at timestamp
    - Optional updated_at timestamp
    - UTC timezone handling
    """
    
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="Creation timestamp in UTC"
    )
    updated_at: Optional[datetime] = Field(
        default=None,
        description="Last update timestamp in UTC"
    )
    
    def mark_updated(self) -> None:
        """Mark the model as updated with current timestamp."""
        self.updated_at = datetime.now(timezone.utc)
    
    @field_validator('created_at', 'updated_at')
    @classmethod
    def validate_timezone(cls, v: Optional[datetime]) -> Optional[datetime]:
        """Ensure timestamps are timezone-aware (UTC)."""
        if v is None:
            return v
        
        if v.tzinfo is None:
            # Assume UTC if no timezone info
            return v.replace(tzinfo=timezone.utc)
        
        # Convert to UTC if different timezone
        return v.astimezone(timezone.utc)


class IdentifiableModel(TimestampedModel):
    """Base model with unique identifier.
    
    Provides:
    - Automatic UUID generation
    - Unique identification across system
    - Correlation tracking
    """
    
    id: str = Field(
        default_factory=lambda: str(uuid4()),
        description="Unique identifier"
    )
    
    @field_validator('id')
    @classmethod
    def validate_id_format(cls, v: str) -> str:
        """Validate ID format (UUID or custom format)."""
        if not v or len(v.strip()) == 0:
            raise ValueError("ID cannot be empty")
        
        # Allow UUID format or custom format
        return v.strip()


class ConfigurableModel(BaseAgentModel):
    """Base model for configuration objects.
    
    Provides:
    - Validation of configuration values
    - Environment variable integration
    - Default value handling
    """
    
    # Class variable to track required fields
    _required_fields: ClassVar[set[str]] = set()
    
    @classmethod
    def get_required_fields(cls) -> set[str]:
        """Get set of required field names."""
        return cls._required_fields.copy()
    
    def validate_required_fields(self) -> list[str]:
        """Validate that all required fields have values.
        
        Returns:
            List of missing required fields
        """
        missing_fields = []
        
        for field_name in self.get_required_fields():
            if hasattr(self, field_name):
                value = getattr(self, field_name)
                if value is None or (isinstance(value, str) and not value.strip()):
                    missing_fields.append(field_name)
            else:
                missing_fields.append(field_name)
        
        return missing_fields


class ValidationMixin:
    """Mixin providing common validation utilities."""
    
    @staticmethod
    def validate_non_empty_string(v: str, field_name: str = "field") -> str:
        """Validate that string is not empty after stripping."""
        if not isinstance(v, str):
            raise ValueError(f"{field_name} must be a string")
        
        stripped = v.strip()
        if not stripped:
            raise ValueError(f"{field_name} cannot be empty")
        
        return stripped
    
    @staticmethod
    def validate_positive_number(v: float, field_name: str = "field") -> float:
        """Validate that number is positive."""
        if not isinstance(v, (int, float)):
            raise ValueError(f"{field_name} must be a number")
        
        if v <= 0:
            raise ValueError(f"{field_name} must be positive")
        
        return float(v)
    
    @staticmethod
    def validate_percentage(v: float, field_name: str = "field") -> float:
        """Validate that number is a valid percentage (0-100)."""
        if not isinstance(v, (int, float)):
            raise ValueError(f"{field_name} must be a number")
        
        if not 0 <= v <= 100:
            raise ValueError(f"{field_name} must be between 0 and 100")
        
        return float(v)
    
    @staticmethod
    def validate_score(v: float, field_name: str = "field", max_score: float = 10.0) -> float:
        """Validate that number is a valid score (0-max_score)."""
        if not isinstance(v, (int, float)):
            raise ValueError(f"{field_name} must be a number")
        
        if not 0 <= v <= max_score:
            raise ValueError(f"{field_name} must be between 0 and {max_score}")
        
        return float(v)


class ErrorModel(BaseAgentModel):
    """Base model for error information."""
    
    error_type: str = Field(description="Type of error")
    message: str = Field(description="Human-readable error message")
    code: Optional[str] = Field(default=None, description="Machine-readable error code")
    details: Dict[str, Any] = Field(default_factory=dict, description="Additional error details")
    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="Error timestamp"
    )
    
    @field_validator('error_type', 'message')
    @classmethod
    def validate_required_strings(cls, v: str) -> str:
        """Validate required string fields."""
        return ValidationMixin.validate_non_empty_string(v)


class MetricsModel(BaseAgentModel, ValidationMixin):
    """Base model for metrics and measurements."""
    
    def validate_all_scores(self) -> list[str]:
        """Validate all score fields in the model.
        
        Returns:
            List of validation errors
        """
        errors = []
        
        # Get all fields that end with '_score'
        for field_name, field_info in self.model_fields.items():
            if field_name.endswith('_score'):
                try:
                    value = getattr(self, field_name)
                    if value is not None:
                        self.validate_score(value, field_name)
                except ValueError as e:
                    errors.append(str(e))
        
        return errors
