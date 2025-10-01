"""Core interpolation engine for variable substitution."""

import os
import re
from abc import ABC, abstractmethod
from typing import Any, Dict, Set, Optional, List
from ..core.exceptions import InterpolationError, CircularReferenceError


class VariableResolver(ABC):
    """Abstract base class for variable resolvers."""

    @abstractmethod
    def resolve(self, variable: str) -> Optional[str]:
        """Resolve a variable to its value."""
        pass

    @abstractmethod
    def get_name(self) -> str:
        """Get resolver name for debugging."""
        pass


class InterpolationEngine:
    """Engine for resolving variable interpolation in configuration values."""

    # Pattern for variable references: ${VAR_NAME} or ${VAR_NAME:default}
    VARIABLE_PATTERN = re.compile(r'\$\{([^}]+)\}')

    def __init__(self, resolvers: Optional[List[VariableResolver]] = None):
        """
        Initialize interpolation engine.

        Args:
            resolvers: List of variable resolvers to use
        """
        self.resolvers = resolvers or []
        self._resolution_stack: Set[str] = set()

    def add_resolver(self, resolver: VariableResolver) -> None:
        """Add a variable resolver."""
        self.resolvers.append(resolver)

    def interpolate(self, value: Any, path: str = "") -> Any:
        """
        Interpolate variables in a value.

        Args:
            value: Value to interpolate
            path: Path for error reporting

        Returns:
            Value with variables interpolated
        """
        if isinstance(value, str):
            return self._interpolate_string(value, path)
        elif isinstance(value, dict):
            return {k: self.interpolate(v, f"{path}.{k}" if path else k)
                   for k, v in value.items()}
        elif isinstance(value, list):
            return [self.interpolate(item, f"{path}[{i}]" if path else f"[{i}]")
                   for i, item in enumerate(value)]
        else:
            return value

    def _interpolate_string(self, text: str, path: str = "") -> str:
        """Interpolate variables in a string."""
        def replace_variable(match):
            var_expr = match.group(1)
            return self._resolve_variable(var_expr, path)

        try:
            result = self.VARIABLE_PATTERN.sub(replace_variable, text)
            return result
        except InterpolationError:
            raise
        except Exception as e:
            raise InterpolationError(f"Interpolation failed: {e}", path=path)

    def _resolve_variable(self, var_expr: str, path: str = "") -> str:
        """
        Resolve a variable expression.

        Args:
            var_expr: Variable expression (e.g., "VAR_NAME" or "VAR_NAME:default")
            path: Path for error reporting

        Returns:
            Resolved variable value
        """
        # Parse variable name and default value
        if ':' in var_expr:
            var_name, default_value = var_expr.split(':', 1)
        else:
            var_name = var_expr
            default_value = None

        var_name = var_name.strip()

        # Check for circular references
        if var_name in self._resolution_stack:
            raise CircularReferenceError(var_name, path)

        # Add to resolution stack
        self._resolution_stack.add(var_name)

        try:
            # Try to resolve with each resolver
            for resolver in self.resolvers:
                value = resolver.resolve(var_name)
                if value is not None:
                    # Recursively interpolate the resolved value
                    return self._interpolate_string(value, path)

            # No resolver found a value
            if default_value is not None:
                return self._interpolate_string(default_value, path)
            else:
                raise InterpolationError(
                    f"Variable '{var_name}' not found and no default provided",
                    variable=var_name,
                    path=path
                )

        finally:
            # Remove from resolution stack
            self._resolution_stack.discard(var_name)

    def clear_resolution_stack(self) -> None:
        """Clear the resolution stack (for error recovery)."""
        self._resolution_stack.clear()

    def has_variables(self, text: str) -> bool:
        """Check if text contains variable references."""
        if not isinstance(text, str):
            return False
        return bool(self.VARIABLE_PATTERN.search(text))

    def extract_variables(self, text: str) -> List[str]:
        """Extract all variable names from text."""
        if not isinstance(text, str):
            return []

        variables = []
        for match in self.VARIABLE_PATTERN.finditer(text):
            var_expr = match.group(1)
            # Extract variable name (before any default value)
            var_name = var_expr.split(':', 1)[0].strip()
            if var_name not in variables:
                variables.append(var_name)

        return variables