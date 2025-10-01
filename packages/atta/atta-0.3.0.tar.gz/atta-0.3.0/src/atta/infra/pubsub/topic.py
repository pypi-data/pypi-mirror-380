import asyncio
from asyncio import Lock, PriorityQueue, Task
from inspect import iscoroutine, ismethod
from itertools import count
from typing import Final, Literal
from weakref import WeakMethod

from pendulum import Duration

from atta.infra.pubsub.protocols import AsyncHandlerProtocol, HandlerProtocol
from atta.observability.logging import LoggingProtocol, get_logger
from atta.utils.lambda_check import is_pure_lambda

# -------------------------------
# Exceptions
# -------------------------------


class TopicError(Exception):
    """Base exception for topic-related errors."""


# -------------------------------
# Types
# -------------------------------

type Hash = int
type Number = int
type Priority = int
type PriorityQueueItem[T] = tuple[Priority, Number, T]

type StrongHandler[T] = HandlerProtocol[T] | AsyncHandlerProtocol[T]
type WeakHandler[T] = WeakMethod[HandlerProtocol[T] | AsyncHandlerProtocol[T]]
type Handler[T] = StrongHandler[T] | WeakHandler[T]

# -------------------------------
# Constants
# -------------------------------

CRITICAL: Final[int] = 0
HIGH: Final[int] = 1
NORMAL: Final[int] = 2
LOW: Final[int] = 3

# Timeout to wait in internal task to check for new events to dispatch
DEFAULT_TIMEOUT: Final[Duration] = Duration(milliseconds=100)
# Timeout to wait if queue is full
DEFAULT_PUBLISH_TIMEOUT: Final[Duration] = Duration(seconds=5)


# -------------------------------
# Topic class
# -------------------------------


class Topic[T]:
    __slots__ = (
        "_counter",
        "_handler_cmd_lock",
        "_logger",
        "_name",
        "_priority_queue",
        "_strong_handlers",
        "_wait_for_timeout",
        "_weak_handlers",
        "_worker_running",
        "_worker_task",
    )

    def __init__(
        self,
        name: str,
        max_size: int = 128,
        wait_for_timeout: Duration = DEFAULT_TIMEOUT,
    ) -> None:
        self._name: Final[str] = name
        self._wait_for_timeout: Final[Duration] = wait_for_timeout
        self._logger: Final[LoggingProtocol] = get_logger(f"Topic[{name}]")
        self._priority_queue: Final[PriorityQueue[PriorityQueueItem[T]]] = (
            PriorityQueue(max_size)
        )
        self._strong_handlers: Final[list[StrongHandler[T]]] = []
        self._weak_handlers: Final[dict[Hash, WeakHandler[T]]] = {}
        self._counter: Final[count[int]] = count()
        self._worker_task: Task | None = None  # type: ignore[type-arg]
        self._worker_running: bool = False
        self._handler_cmd_lock: Lock = Lock()

    async def subscribe(self, handler: StrongHandler[T]) -> None:
        """
        Subscribe a handler/callback to the topic.

        Args:
            handler: Handler to subscribe.

        Raises:
            TopicError: If handler is a pure lambda (use a variable instead).
        """
        # Check for pure lambda functions
        if is_pure_lambda(handler):
            raise TopicError(
                "Pure lambda functions are not supported for subscription. "
                "Store the lambda in a variable first: handler = lambda x: ...; await topic.subscribe(handler)"
            )

        async with self._handler_cmd_lock:
            if ismethod(handler):
                handler_hash = hash(handler)
                if handler_hash in self._weak_handlers:
                    self._logger.debug(f"Handler {handler} already subscribed")
                    return

                # Store weak reference with consistent hash for O(1) unsubscribe
                weak_ref = WeakMethod(handler)
                self._weak_handlers[handler_hash] = weak_ref  # type: ignore[assignment]
                self._logger.debug(f"Subscribed weak handler: {weak_ref}")
            else:
                if handler in self._strong_handlers:
                    self._logger.debug(f"Handler {handler} already subscribed")
                    return

                # Functions and lambdas are kept as strong references
                self._strong_handlers.append(handler)
                self._logger.debug(f"Subscribed strong handler: {handler}")

    async def publish(
        self,
        event: T,
        priority: Literal[0, 1, 2, 3] = NORMAL,  # type: ignore[assignment]
        timeout: Duration = DEFAULT_PUBLISH_TIMEOUT,
    ) -> None:
        """
        Publish an event to the topic.

        Args:
            event: Event to publish.
            priority: Priority of the event (0-3).
            timeout: Timeout for the publish operation to wait if the queue is full.

        Info:
            - If the queue is shutdown or is full and the timeout has passed, the event is dropped.
        """

        try:
            # Counter ensures FIFO ordering within same priority level
            queue_item = (priority, next(self._counter), event)
            await asyncio.wait_for(
                self._priority_queue.put(queue_item), timeout=timeout.total_seconds()
            )
        except asyncio.QueueShutDown as e:
            self._logger.warning(
                f"Shutting down -> Dropping event {event}.", exc_info=e
            )
        except TimeoutError as e:
            self._logger.warning(
                f"Publish timeout {timeout} exceeded -> Dropping event {event}.",
                exc_info=e,
            )
        except Exception as e:
            self._logger.error(f"Failed to publish event {event}: {e}", exc_info=e)

    async def unsubscribe(self, handler: Handler[T]) -> None:
        """Unsubscribe a handler from the topic.

        Raises:
            TopicError: If handler is a pure lambda (use a variable instead).
        """
        # Check for pure lambda functions
        if is_pure_lambda(handler):
            raise TopicError(
                "Pure lambda functions are not supported for unsubscription. "
                "Store the lambda in a variable first: handler = lambda x: ...; await topic.subscribe(handler); await topic.unsubscribe(handler)"
            )

        async with self._handler_cmd_lock:
            if ismethod(handler):
                handler_hash = hash(handler)
                self._weak_handlers.pop(handler_hash, None)
                self._logger.debug(f"Unsubscribed weak handler: {handler}")
                return

            # Safe removal with error handling
            try:
                self._strong_handlers.remove(handler)  # type: ignore[arg-type]
                self._logger.debug(f"Unsubscribed strong handler: {handler}")
            except ValueError:
                self._logger.warning(f"Handler {handler} not found for unsubscription")

    async def _remove_dead_weak_handlers(self) -> None:
        """Remove handlers that are no longer reachable."""
        async with self._handler_cmd_lock:
            # Collect dead handler hashes first to avoid dict modification during iteration
            dead_handler_hashes = [
                handler_hash
                for handler_hash, weak_handler in self._weak_handlers.items()
                if weak_handler() is None
            ]

            for handler_hash in dead_handler_hashes:
                self._weak_handlers.pop(handler_hash, None)

    async def _dispatch_event(self, event: T) -> None:
        """Dispatch event to all active handlers."""
        active_handlers = [*self._strong_handlers]

        # Collect alive weak handlers
        for weak_handler in self._weak_handlers.values():
            if live_handler := weak_handler():
                active_handlers.append(live_handler)

        # If no handlers available, drop event
        if not active_handlers:
            self._logger.warning(f"No handlers available for event {event}, dropping")
            return

        # Create and execute handler tasks
        handler_tasks = [
            asyncio.create_task(self._call_handler(event, handler))
            for handler in active_handlers
        ]
        await asyncio.gather(*handler_tasks)

    async def _call_handler(self, event: T, handler: StrongHandler[T]) -> None:
        try:
            result = handler(event)
            if iscoroutine(result):
                await result
            self._logger.debug(f"Called handler {handler} with event {event}")
        except Exception as e:
            self._logger.error(
                f"Failed to call handler {handler} with event {event}: {e}", exc_info=e
            )

    async def _dispatch_events(self) -> None:
        """Main worker loop that processes events from the priority queue."""
        while self._worker_running:
            try:
                # Extract event from priority queue (ignore priority and counter)
                _priority, _sequence_num, event = await asyncio.wait_for(
                    self._priority_queue.get(),
                    timeout=self._wait_for_timeout.total_seconds(),
                )

                # Forward event to all active handlers
                await self._dispatch_event(event)
                self._priority_queue.task_done()

            except (TimeoutError, asyncio.QueueEmpty):
                continue
            except Exception as e:
                self._logger.error(f"Error processing event: {e}", exc_info=e)
            finally:
                await self._remove_dead_weak_handlers()

    async def start(self) -> None:
        """Start the topic worker task."""
        if self._worker_running:
            return  # Already running

        self._worker_running = True
        self._worker_task = asyncio.create_task(self._dispatch_events())
        self._logger.debug("Started worker task")

    async def stop(self) -> None:
        """Stop the topic worker task."""
        if self._worker_running:
            self._worker_running = False
            if self._worker_task:
                self._worker_task.cancel()
                try:
                    await self._worker_task
                except asyncio.CancelledError:
                    # Expected when cancelling the task
                    pass
                except Exception as e:
                    # Handle any other exceptions during task cleanup
                    self._logger.error(f"Error while stopping: {e}", exc_info=e)
            self._worker_task = None
            self._logger.debug("Stopped worker task")

    async def close(self) -> None:
        """Close the topic."""
        try:
            await self.stop()

            # Signal no new items should be processed
            async with self._handler_cmd_lock:
                self._strong_handlers.clear()
                self._weak_handlers.clear()
            self._logger.debug("Cleared handlers")

            # Try graceful shutdown first
            try:
                # Attempt graceful shutdown (wait for current operations)
                self._priority_queue.shutdown(immediate=False)

                # Wait a bit for graceful shutdown
                await asyncio.sleep(1.0)

            except Exception as e:
                self._logger.warning(f"Graceful shutdown failed: {e}")
            finally:
                # Force shutdown if graceful didn't work
                self._priority_queue.shutdown(immediate=True)

            self._logger.debug("Shutdown priority queue")
            self._logger.debug("Closed")
        except Exception as e:
            self._logger.error(f"Error while closing: {e}", exc_info=e)
