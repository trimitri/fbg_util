"""Some function decorators."""

from typing import Any, Callable


def static_variable(variable_name: str,
                    initial_value: Any) -> Callable[[Callable], Callable]:
    """A decorator to add a static variable to a function."""
    def decorator(function):
        setattr(function, variable_name, initial_value)
        return function
    return decorator
