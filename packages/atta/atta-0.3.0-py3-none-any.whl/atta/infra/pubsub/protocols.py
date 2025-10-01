from typing import Any, Protocol


class AsyncHandlerProtocol[T](Protocol):
    """Protocol for async event handlers.

    Defines the interface for async event handlers that process events of type T.
    """

    async def __call__(self, event: T) -> None:
        """Handle an event.

        Args:
            event: Event to process.
        """
        ...


class HandlerProtocol[T](Protocol):
    """Protocol for sync event handlers.

    Defines the interface for async event handlers that process events of type T.
    """

    def __call__(self, event: T) -> None:
        """Handle an event.

        Args:
            event: Event to process.
        """
        ...


class PubSubProtocol(Protocol):
    """Protocol for PubSub implementations."""

    async def subscribe(self, *args: Any, **kwargs: Any) -> None: ...

    async def unsubscribe(self, *args: Any, **kwargs: Any) -> None: ...

    async def publish(self, *args: Any, **kwargs: Any) -> None: ...
