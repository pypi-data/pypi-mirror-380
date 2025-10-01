"""
Lambda detection utility.
"""

from collections.abc import Callable
from inspect import ismethod
from typing import Any


def is_pure_lambda(handler: Callable[..., Any]) -> bool:
    """
    Check if handler is a pure lambda function.

    Pure lambdas create new objects on each access, making unsubscription impossible.

    Args:
        handler: A callable to check

    Returns:
        True if the handler is a pure lambda function
    """
    return (
        callable(handler)
        and hasattr(handler, "__name__")
        and handler.__name__ == "<lambda>"
        and not ismethod(handler)
    )
