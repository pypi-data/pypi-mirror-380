"""Variable resolver implementations."""

import os
from typing import Optional, Dict, Any, List
from .engine import VariableResolver


class EnvironmentResolver(VariableResolver):
    """Resolver for environment variables."""

    def resolve(self, variable: str) -> Optional[str]:
        """Resolve variable from environment."""
        return os.environ.get(variable)

    def get_name(self) -> str:
        """Get resolver name."""
        return "environment"


class ConfigResolver(VariableResolver):
    """Resolver for configuration variables."""

    def __init__(self, config_data: Dict[str, Any]):
        """
        Initialize with configuration data.

        Args:
            config_data: Configuration dictionary to resolve from
        """
        self.config_data = config_data

    def resolve(self, variable: str) -> Optional[str]:
        """Resolve variable from configuration data."""
        # Support dot notation for nested access
        keys = variable.split('.')
        current = self.config_data

        try:
            for key in keys:
                if isinstance(current, dict) and key in current:
                    current = current[key]
                else:
                    return None

            # Convert to string if not already
            if current is not None and not isinstance(current, str):
                return str(current)

            return current

        except (KeyError, TypeError):
            return None

    def get_name(self) -> str:
        """Get resolver name."""
        return "config"

    def update_config(self, config_data: Dict[str, Any]) -> None:
        """Update the configuration data."""
        self.config_data = config_data


class StaticResolver(VariableResolver):
    """Resolver for static variable mappings."""

    def __init__(self, variables: Dict[str, str]):
        """
        Initialize with static variable mappings.

        Args:
            variables: Dictionary of variable name to value mappings
        """
        self.variables = variables.copy()

    def resolve(self, variable: str) -> Optional[str]:
        """Resolve variable from static mappings."""
        return self.variables.get(variable)

    def get_name(self) -> str:
        """Get resolver name."""
        return "static"

    def set_variable(self, name: str, value: str) -> None:
        """Set a static variable."""
        self.variables[name] = value

    def remove_variable(self, name: str) -> None:
        """Remove a static variable."""
        self.variables.pop(name, None)


class ChainResolver(VariableResolver):
    """Resolver that chains multiple resolvers together."""

    def __init__(self, resolvers: List[VariableResolver]):
        """
        Initialize with list of resolvers.

        Args:
            resolvers: List of resolvers to chain (tried in order)
        """
        self.resolvers = resolvers.copy()

    def resolve(self, variable: str) -> Optional[str]:
        """Resolve variable using first resolver that finds it."""
        for resolver in self.resolvers:
            value = resolver.resolve(variable)
            if value is not None:
                return value
        return None

    def get_name(self) -> str:
        """Get resolver name."""
        resolver_names = [resolver.get_name() for resolver in self.resolvers]
        return f"chain({', '.join(resolver_names)})"

    def add_resolver(self, resolver: VariableResolver) -> None:
        """Add a resolver to the chain."""
        self.resolvers.append(resolver)

    def prepend_resolver(self, resolver: VariableResolver) -> None:
        """Prepend a resolver to the chain (higher priority)."""
        self.resolvers.insert(0, resolver)


class FunctionResolver(VariableResolver):
    """Resolver that supports function-like variable expressions."""

    def __init__(self):
        """Initialize function resolver."""
        self._functions = {
            'upper': lambda x: x.upper(),
            'lower': lambda x: x.lower(),
            'strip': lambda x: x.strip(),
            'len': lambda x: str(len(x)),
        }

    def resolve(self, variable: str) -> Optional[str]:
        """
        Resolve function expressions like func(arg).

        Args:
            variable: Variable expression potentially containing function call

        Returns:
            Result of function application or None
        """
        # Simple function parsing: func(arg)
        if '(' in variable and variable.endswith(')'):
            func_name = variable[:variable.index('(')]
            arg_str = variable[variable.index('(') + 1:-1]

            if func_name in self._functions:
                try:
                    return self._functions[func_name](arg_str)
                except Exception:
                    return None

        return None

    def get_name(self) -> str:
        """Get resolver name."""
        return "function"

    def register_function(self, name: str, func: callable) -> None:
        """Register a custom function."""
        self._functions[name] = func