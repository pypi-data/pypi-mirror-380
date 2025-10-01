from typing import Any, TypeVar

# Type variable for the singleton class
_T = TypeVar("_T")


class SingletonMeta(type):
    """
    IMPORTANT: Not thread-safe!

    Singleton metaclass implementation.

    Creates at most one instance of any class using this metaclass.
    The instance is created on first call and reused for all subsequent calls.

    Warning:
        This implementation is NOT thread-safe. Use appropriate synchronization
        if the singleton will be accessed from multiple threads.

    Example:
        >>> class Database(metaclass=SingletonMeta):
        ...     def __init__(self, connection_string: str) -> None:
        ...         self.connection_string = connection_string
        >>>
        >>> db1 = Database("postgresql://localhost:5432")
        >>> db2 = Database("mysql://localhost:3306")  # Args ignored!
        >>> assert db1 is db2  # Same instance
    """

    def __init__(
        cls, name: str, bases: tuple[type, ...], namespace: dict[str, Any]
    ) -> None:
        """Initialize the metaclass.

        Args:
            name: Class name.
            bases: Base classes.
            namespace: Class namespace dictionary.
        """
        super().__init__(name, bases, namespace)
        cls._instance: Any | None = None

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        """Create or return existing singleton instance.

        Args:
            *args: Arguments passed to __init__ (only used on first call).
            **kwargs: Keyword arguments passed to __init__ (only used on first call).

        Returns:
            The singleton instance of the class.

        Note:
            Arguments are only used during the first call. Subsequent calls
            ignore all arguments and return the existing instance.
        """
        # Return existing instance if already created
        if cls._instance is not None:
            return cls._instance

        # Create and initialize new instance (first call only)
        cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

    def reset(cls) -> None:
        """Reset the singleton instance.

        After calling this method, the next call to the singleton class
        will create a new instance.

        Warning:
            This method should be used carefully, typically only in tests
            or during application shutdown.
        """
        cls._instance = None

    @property
    def instance(cls) -> Any | None:
        """Get the current singleton instance.

        Returns:
            The singleton instance if it exists, None otherwise.
        """
        return cls._instance

    @property
    def is_initialized(cls) -> bool:
        """Check if the singleton instance has been created and initialized.

        Returns:
            True if the singleton instance exists and is initialized, False otherwise.
        """
        return cls._instance is not None
