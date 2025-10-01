"""Configuration schema validation system."""

from typing import Any, Dict, List, Optional, Type, Union, Callable
from dataclasses import dataclass
import re


@dataclass
class ValidationResult:
    """Result of schema validation."""
    is_valid: bool
    errors: List[str]
    warnings: List[str]


class SchemaValidator:
    """Base class for schema validators."""

    def validate(self, value: Any, path: str = "") -> ValidationResult:
        """Validate value against schema."""
        raise NotImplementedError


class TypeValidator(SchemaValidator):
    """Validates value type."""

    def __init__(self, expected_type: Type, allow_none: bool = False):
        self.expected_type = expected_type
        self.allow_none = allow_none

    def validate(self, value: Any, path: str = "") -> ValidationResult:
        """Validate that value matches expected type."""
        if value is None and self.allow_none:
            return ValidationResult(True, [], [])

        if not isinstance(value, self.expected_type):
            error = f"Expected {self.expected_type.__name__}, got {type(value).__name__}"
            if path:
                error = f"{path}: {error}"
            return ValidationResult(False, [error], [])

        return ValidationResult(True, [], [])


class RangeValidator(SchemaValidator):
    """Validates numeric ranges."""

    def __init__(self, min_value: Optional[Union[int, float]] = None,
                 max_value: Optional[Union[int, float]] = None):
        self.min_value = min_value
        self.max_value = max_value

    def validate(self, value: Any, path: str = "") -> ValidationResult:
        """Validate that value is within range."""
        errors = []

        if not isinstance(value, (int, float)):
            error = f"Range validation requires numeric value, got {type(value).__name__}"
            if path:
                error = f"{path}: {error}"
            return ValidationResult(False, [error], [])

        if self.min_value is not None and value < self.min_value:
            error = f"Value {value} is below minimum {self.min_value}"
            if path:
                error = f"{path}: {error}"
            errors.append(error)

        if self.max_value is not None and value > self.max_value:
            error = f"Value {value} is above maximum {self.max_value}"
            if path:
                error = f"{path}: {error}"
            errors.append(error)

        return ValidationResult(len(errors) == 0, errors, [])


class PatternValidator(SchemaValidator):
    """Validates string patterns using regex."""

    def __init__(self, pattern: str, flags: int = 0):
        self.pattern = re.compile(pattern, flags)

    def validate(self, value: Any, path: str = "") -> ValidationResult:
        """Validate that string matches pattern."""
        if not isinstance(value, str):
            error = f"Pattern validation requires string value, got {type(value).__name__}"
            if path:
                error = f"{path}: {error}"
            return ValidationResult(False, [error], [])

        if not self.pattern.match(value):
            error = f"Value '{value}' does not match required pattern"
            if path:
                error = f"{path}: {error}"
            return ValidationResult(False, [error], [])

        return ValidationResult(True, [], [])


class ChoiceValidator(SchemaValidator):
    """Validates that value is one of allowed choices."""

    def __init__(self, choices: List[Any]):
        self.choices = choices

    def validate(self, value: Any, path: str = "") -> ValidationResult:
        """Validate that value is in allowed choices."""
        if value not in self.choices:
            error = f"Value '{value}' not in allowed choices: {self.choices}"
            if path:
                error = f"{path}: {error}"
            return ValidationResult(False, [error], [])

        return ValidationResult(True, [], [])


class Schema:
    """Configuration schema definition and validation."""

    def __init__(self, schema_def: Union[Dict[str, Any], Type, List[SchemaValidator]]):
        """
        Initialize schema with definition.

        Args:
            schema_def: Schema definition as dict, type, or list of validators
        """
        self.schema_def = schema_def
        self._validators = self._build_validators(schema_def)

    def _build_validators(self, schema_def: Any) -> List[SchemaValidator]:
        """Build validators from schema definition."""
        validators = []

        if isinstance(schema_def, type):
            # Simple type validation
            validators.append(TypeValidator(schema_def))
        elif isinstance(schema_def, list) and all(isinstance(v, SchemaValidator) for v in schema_def):
            # List of validators
            validators.extend(schema_def)
        elif isinstance(schema_def, dict):
            # Dict schema handled in validate method
            pass
        else:
            raise ValueError(f"Invalid schema definition: {schema_def}")

        return validators

    def validate(self, data: Any, path: str = "") -> ValidationResult:
        """Validate data against schema."""
        all_errors = []
        all_warnings = []

        if isinstance(self.schema_def, dict):
            return self._validate_dict(data, self.schema_def, path)
        else:
            # Run all validators
            for validator in self._validators:
                result = validator.validate(data, path)
                all_errors.extend(result.errors)
                all_warnings.extend(result.warnings)

        return ValidationResult(len(all_errors) == 0, all_errors, all_warnings)

    def _validate_dict(self, data: Any, schema: Dict[str, Any], path: str = "") -> ValidationResult:
        """Validate dictionary data against dict schema."""
        all_errors = []
        all_warnings = []

        if not isinstance(data, dict):
            error = f"Expected dictionary, got {type(data).__name__}"
            if path:
                error = f"{path}: {error}"
            return ValidationResult(False, [error], [])

        # Validate each field in schema
        for key, field_schema in schema.items():
            field_path = f"{path}.{key}" if path else key

            if key not in data:
                # Check if field is required
                if self._is_required_field(field_schema):
                    all_errors.append(f"{field_path}: Required field missing")
                continue

            field_value = data[key]

            if isinstance(field_schema, dict):
                # Nested dictionary
                result = self._validate_dict(field_value, field_schema, field_path)
            elif isinstance(field_schema, type):
                # Simple type validation
                validator = TypeValidator(field_schema)
                result = validator.validate(field_value, field_path)
            elif isinstance(field_schema, Schema):
                # Nested schema
                result = field_schema.validate(field_value, field_path)
            elif isinstance(field_schema, list):
                # List of validators or mixed validators
                result = ValidationResult(True, [], [])
                # Flatten the list in case of nested lists (from required() function)
                flattened_validators = []
                for item in field_schema:
                    if isinstance(item, list):
                        flattened_validators.extend(item)
                    else:
                        flattened_validators.append(item)

                for validator_item in flattened_validators:
                    if isinstance(validator_item, SchemaValidator):
                        val_result = validator_item.validate(field_value, field_path)
                        result.errors.extend(val_result.errors)
                        result.warnings.extend(val_result.warnings)
                    elif isinstance(validator_item, type):
                        # Simple type validator
                        type_validator = TypeValidator(validator_item)
                        val_result = type_validator.validate(field_value, field_path)
                        result.errors.extend(val_result.errors)
                        result.warnings.extend(val_result.warnings)
                result.is_valid = len(result.errors) == 0
            else:
                # Unsupported field schema
                all_warnings.append(f"{field_path}: Unsupported schema type {type(field_schema)}")
                continue

            all_errors.extend(result.errors)
            all_warnings.extend(result.warnings)

        return ValidationResult(len(all_errors) == 0, all_errors, all_warnings)

    def _is_required_field(self, field_schema: Any) -> bool:
        """Check if field is required (simple heuristic)."""
        # This is a simple implementation - could be enhanced with explicit required/optional markers
        return not (isinstance(field_schema, list) and
                   any(isinstance(v, TypeValidator) and v.allow_none for v in field_schema
                       if isinstance(v, TypeValidator)))


# Convenience functions for common validators
def required(validator_type: Union[Type, SchemaValidator]) -> List[SchemaValidator]:
    """Mark field as required with given validator."""
    if isinstance(validator_type, type):
        return [TypeValidator(validator_type, allow_none=False)]
    return [validator_type]


def optional(validator_type: Union[Type, SchemaValidator]) -> List[SchemaValidator]:
    """Mark field as optional with given validator."""
    if isinstance(validator_type, type):
        return [TypeValidator(validator_type, allow_none=True)]
    return [validator_type]


def range_check(min_val: Optional[Union[int, float]] = None,
                max_val: Optional[Union[int, float]] = None) -> RangeValidator:
    """Create range validator."""
    return RangeValidator(min_val, max_val)


def pattern(regex: str, flags: int = 0) -> PatternValidator:
    """Create pattern validator."""
    return PatternValidator(regex, flags)


def choice(*choices) -> ChoiceValidator:
    """Create choice validator."""
    return ChoiceValidator(list(choices))