from types import TracebackType
from typing import Any, Protocol, Self, runtime_checkable

type ExceptionInfo = (
    bool
    | tuple[type[BaseException], BaseException, TracebackType | None]
    | tuple[None, None, None]
    | BaseException
)


@runtime_checkable
class LoggingProtocol(Protocol):
    """Unified logger interface supporting both stdlib and structlog backends.

    All methods enforce keyword-only arguments for structured logging consistency.
    Supports both direct logging and context binding (structlog-style).
    """

    def debug(
        self,
        msg: str,
        /,
        *,
        _: Any = None,
        exc_info: ExceptionInfo | None = None,
        stack_info: bool = False,
        stacklevel: int = 1,
        extra: dict[str, Any] | None = None,
        **context: Any,
    ) -> None:
        """Log debug message with structured context.

        Args:
            msg: Log message, supports {key} formatting (positional-only)
            exc_info: Exception info to include
            stack_info: Include stack info in log record
            stacklevel: Stack level for caller detection
            extra: Extra context dict (prefer **context)
            **context: Structured context data (keyword-only)
        """
        ...

    def info(
        self,
        msg: str,
        /,
        *,
        _: Any = None,
        exc_info: ExceptionInfo | None = None,
        stack_info: bool = False,
        stacklevel: int = 1,
        extra: dict[str, Any] | None = None,
        **context: Any,
    ) -> None:
        """Log info message with structured context.

        Args:
            msg: Log message, supports {key} formatting (positional-only)
            exc_info: Exception info to include
            stack_info: Include stack info in log record
            stacklevel: Stack level for caller detection
            extra: Extra context dict (prefer **context)
            **context: Structured context data (keyword-only)
        """
        ...

    def warning(
        self,
        msg: str,
        /,
        *,
        _: Any = None,
        exc_info: ExceptionInfo | None = None,
        stack_info: bool = False,
        stacklevel: int = 1,
        extra: dict[str, Any] | None = None,
        **context: Any,
    ) -> None:
        """Log warning message with structured context.

        Args:
            msg: Log message, supports {key} formatting (positional-only)
            exc_info: Exception info to include
            stack_info: Include stack info in log record
            stacklevel: Stack level for caller detection
            extra: Extra context dict (prefer **context)
            **context: Structured context data (keyword-only)
        """
        ...

    def error(
        self,
        msg: str,
        /,
        *,
        _: Any = None,
        exc_info: ExceptionInfo | None = None,
        stack_info: bool = False,
        stacklevel: int = 1,
        extra: dict[str, Any] | None = None,
        **context: Any,
    ) -> None:
        """Log error message with structured context.

        Args:
            msg: Log message, supports {key} formatting (positional-only)
            exc_info: Exception info to include
            stack_info: Include stack info in log record
            stacklevel: Stack level for caller detection
            extra: Extra context dict (prefer **context)
            **context: Structured context data (keyword-only)
        """
        ...

    def critical(
        self,
        msg: str,
        /,
        *,
        _: Any = None,
        exc_info: ExceptionInfo | None = None,
        stack_info: bool = False,
        stacklevel: int = 1,
        extra: dict[str, Any] | None = None,
        **context: Any,
    ) -> None:
        """Log critical message with structured context.

        Args:
            msg: Log message, supports {key} formatting (positional-only)
            exc_info: Exception info to include
            stack_info: Include stack info in log record
            stacklevel: Stack level for caller detection
            extra: Extra context dict (prefer **context)
            **context: Structured context data (keyword-only)
        """
        ...

    def exception(
        self,
        msg: str,
        /,
        *,
        _: Any = None,
        exc_info: ExceptionInfo | None = None,
        stack_info: bool = False,
        stacklevel: int = 1,
        extra: dict[str, Any] | None = None,
        **context: Any,
    ) -> None:
        """Log exception with traceback and structured context.

        Args:
            msg: Log message, supports {key} formatting (positional-only)
            exc_info: Exception info to include (defaults to True for exceptions)
            stack_info: Include stack info in log record
            stacklevel: Stack level for caller detection
            extra: Extra context dict (prefer **context)
            **context: Structured context data (keyword-only)
        """
        ...

    def bind(self, **context: Any) -> Self:
        """Create logger with permanent context (structlog-style).

        Args:
            **context: Permanent context to bind to new logger

        Returns:
            New logger instance with bound context
        """
        ...

    def with_context(self, **context: Any) -> Self:
        """Alias for bind() for consistency.

        Args:
            **context: Permanent context to bind to new logger

        Returns:
            New logger instance with bound context
        """
        ...
