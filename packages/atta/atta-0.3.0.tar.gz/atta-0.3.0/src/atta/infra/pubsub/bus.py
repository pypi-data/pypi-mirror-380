"""Service Bus - Central message routing with pattern matching.

Workflow:
    1. subscribe(handler, "user.created") → creates topic, adds handler
    2. subscribe(handler, "user.*") → pattern handler, matches existing + future topics
    3. publish(event, "user.created") → routes to specific topic + matching patterns
    4. unsubscribe(handler) → removes from all topics, cleans up empty ones

Pattern Handler Logic:
    - Pattern handlers stored separately from topic handlers
    - When new topic created → pattern handlers auto-applied if matched
    - Avoids async task scheduling for pattern matching
    - Direct subscription keeps message flow synchronous
    - Pattern removal cascades to all matching topics
"""

import fnmatch
import re
from asyncio import Lock
from collections import defaultdict
from typing import Any, Final

from atta.infra.pubsub.topic import Handler, Topic
from atta.observability.logging import LoggingProtocol, get_logger
from atta.utils.singleton import SingletonMeta

# -------------------------------
# Types
# -------------------------------

type TopicName = str
type HandlerId = int
type Pattern = str


# -------------------------------
# Functions
# -------------------------------


def is_pattern(text: str) -> bool:
    """Check if string contains wildcard patterns.

    Args:
        text: String to check for wildcards

    Returns:
        True if contains * or + wildcards (+ matches one or more segments)
    """
    return "*" in text or "+" in text


# Topic validation regex pattern
_TOPIC_PATTERN = re.compile(
    r"^(?=.*[a-zA-Z0-9_-]+)(?:[a-zA-Z0-9_-]+|[*+])(?:\.(?:[a-zA-Z0-9_-]+|[*+]))*$"
)


def validate_and_normalize_topic(topic_name: str) -> str:
    """Validate, normalize and prepare topic name for use.

    Valid topic format:
        - Must contain at least one real segment (not just wildcards)
        - Segments separated by dots
        - Real segments: alphanumeric, underscore, dash [a-zA-Z0-9_-]+
        - Wildcards: * (zero or more chars), + (one segment)
        - Cannot start/end with dots or have consecutive dots

    Examples:
        Valid: "user.created", "order.*", "*.error", "api.v1.users"
        Invalid: "user.", ".user", "user..name", "*", "+", "*.+"

    Args:
        topic_name: Topic name or pattern to validate

    Returns:
        Normalized topic name or pattern

    Raises:
        ValueError: If topic name is invalid
    """
    if not topic_name or not topic_name.strip():
        raise ValueError("Topic name cannot be empty")

    normalized = topic_name.strip()

    # Comprehensive regex validation
    if not _TOPIC_PATTERN.match(normalized):
        raise ValueError(
            f"Invalid topic name: '{normalized}'. "
            "Topics must contain alphanumeric segments separated by dots, "
            "with optional wildcards (* or +), and cannot start/end with dots."
        )

    # Additional validation for patterns
    if is_pattern(normalized):
        # Normalize duplicate wildcards
        normalized = normalized.replace("**", "*")
        normalized = normalized.replace("++", "+")

    return normalized


# Pattern cache for performance optimization
_compiled_patterns: dict[str, re.Pattern[str]] = {}


def _clear_pattern_cache(pattern: str | None = None) -> None:
    """Clear pattern cache for specific pattern or all patterns.

    Args:
        pattern: Specific pattern to clear, or None to clear all
    """
    if pattern:
        _compiled_patterns.pop(pattern, None)
    else:
        _compiled_patterns.clear()


def match_topic_to_pattern(topic_name: str, pattern: str) -> bool:
    """Check if topic name matches topic pattern.

    Pattern syntax:
        * = zero or more any characters
        + = exactly one topic segment (non-empty, no dots)

    Examples:
        "user.*" matches: "user.created", "user.admin.updated"
        "user.+" matches: "user.created" (NOT "user.admin.updated")
        "first.*.second" matches: "first.middle.second", "first.second"
        "first.+.second" matches: "first.middle.second" (NOT "first.second")

    Args:
        topic_name: Topic name to test
        pattern: Topic pattern

    Returns:
        True if topic matches pattern
    """
    if pattern not in _compiled_patterns:
        try:
            # Convert semantic pattern to regex
            regex_pattern = _convert_topic_pattern_to_regex(pattern)
            _compiled_patterns[pattern] = re.compile(regex_pattern)
        except re.error:
            # Fallback to basic fnmatch for simple patterns
            return fnmatch.fnmatch(topic_name, pattern)

    return bool(_compiled_patterns[pattern].match(topic_name))


def _convert_topic_pattern_to_regex(pattern: str) -> str:
    """Convert topic pattern to regex.

    Args:
        pattern: Topic pattern with * and + wildcards

    Returns:
        Regex pattern string
    """
    # Handle one special case: .*.  should allow empty middle
    if ".*." in pattern:
        parts = pattern.split(".*.")
        if len(parts) == 2:
            prefix = re.escape(parts[0])
            suffix = re.escape(parts[1])
            return f"^{prefix}(?:\\..*)?{suffix}$"

    # Simple char-by-char for everything else
    result = ""
    for char in pattern:
        if char == "*":
            result += ".*"  # Zero or more any chars
        elif char == "+":
            result += "[^.]+"  # One or more non-dot chars (single segment)
        elif char == ".":
            result += r"\."  # Literal dot
        else:
            result += char  # Literal char
    return f"^{result}$"


# -------------------------------
# Bus
# -------------------------------


class ServiceBus[T](metaclass=SingletonMeta):
    def __init__(
        self, max_queue_size_per_topic: int = 128, max_topics: int = 1000
    ) -> None:
        self._max_queue_size_per_topic: Final[int] = max_queue_size_per_topic
        self._max_topics: Final[int] = max_topics
        self._topics: Final[dict[TopicName, Topic[T]]] = {}
        self._topics_lock: Final[Lock] = Lock()
        self._handlers_to_topics: Final[defaultdict[HandlerId, set[TopicName]]] = (
            defaultdict(set)
        )
        self._pattern_handlers: Final[defaultdict[Pattern, list[Handler[T]]]] = (
            defaultdict(list)
        )
        self._handlers_lock: Final[Lock] = Lock()
        self._logger: Final[LoggingProtocol] = get_logger("ServiceBus")

    async def subscribe(self, handler: Handler[T], topic_name: str) -> None:
        """Subscribe a handler to a topic.

        Args:
            handler: Handler to subscribe
            topic_name: Topic name or pattern to subscribe to
        """
        validated_topic = validate_and_normalize_topic(topic_name)

        try:
            if is_pattern(validated_topic):
                await self._handle_pattern_subscription(handler, validated_topic)
            else:
                await self._handle_topic_subscription(handler, validated_topic)
        except Exception as e:
            self._logger.error(
                f"Failed to subscribe handler {handler} to {validated_topic}: {e}",
                exc_info=e,
            )
            raise

    async def _handle_pattern_subscription(
        self, handler: Handler[T], pattern: str
    ) -> None:
        """Handle subscription to a pattern by registering it and subscribing to matching topics."""
        await self._register_pattern_handler(pattern, handler)
        await self._subscribe_pattern_to_existing_topics(handler, pattern)

    async def _register_pattern_handler(
        self, pattern: str, handler: Handler[T]
    ) -> None:
        """Register a handler for a pattern."""
        async with self._handlers_lock:
            if handler not in self._pattern_handlers[pattern]:
                self._pattern_handlers[pattern].append(handler)
                self._logger.debug(
                    f"Registered pattern handler {handler} for '{pattern}'"
                )
            else:
                self._logger.debug(
                    f"Handler {handler} already registered for pattern '{pattern}'"
                )

    async def _subscribe_pattern_to_existing_topics(
        self, handler: Handler[T], pattern: str
    ) -> None:
        """Subscribe pattern handler to all existing topics that match."""
        async with self._topics_lock:
            matching_topics = [
                topic_name
                for topic_name in self._topics
                if match_topic_to_pattern(topic_name, pattern)
            ]

        for topic_name in matching_topics:
            await self._subscribe_handler_to_topic(handler, topic_name)

    async def _handle_topic_subscription(
        self, handler: Handler[T], topic_name: str
    ) -> None:
        """Handle subscription to a specific topic with pattern handler integration."""
        await self._ensure_topic_exists(topic_name)
        await self._subscribe_handler_to_topic(handler, topic_name)
        await self._apply_pattern_handlers_to_existing_topic(
            topic_name, exclude_handler=handler
        )

    async def _subscribe_handler_to_topic(
        self, handler: Handler[T], topic_name: str
    ) -> None:
        """Subscribe a single handler to a topic and update tracking."""
        await self._topics[topic_name].subscribe(handler)  # type: ignore[arg-type]
        async with self._handlers_lock:
            self._handlers_to_topics[hash(handler)].add(topic_name)

    async def _apply_pattern_handlers_to_existing_topic(
        self, topic_name: str, exclude_handler: Handler[T] | None = None
    ) -> None:
        """Apply matching pattern handlers to an existing topic."""
        pattern_handlers = await self._get_pattern_handlers(topic_name)
        handlers_to_add = [h for h in pattern_handlers if h != exclude_handler]
        if handlers_to_add:
            await self._bulk_subscribe_handlers_to_topic(
                handlers_to_add, self._topics[topic_name], topic_name
            )

    async def _ensure_topic_exists(self, topic_name: str) -> None:
        """Ensure topic exists, create if needed."""
        # Check without lock first (fast path)
        if topic_name in self._topics:
            return

        # Double-check with lock (slow path when topic must be created)
        async with self._topics_lock:
            if topic_name not in self._topics:
                await self._setup_new_topic_locked(topic_name)

    async def _setup_new_topic_locked(self, topic_name: str) -> None:
        """Set up a new topic with pattern handlers (assumes topics_lock is held)."""
        await self._validate_topic_creation_locked(topic_name)

        try:
            topic = await self._create_bare_topic_locked(topic_name)
            await self._wire_pattern_handlers_to_topic(topic, topic_name)
        except Exception as e:
            # Clean up failed topic creation
            self._topics.pop(topic_name, None)
            self._logger.error(f"Failed to setup topic {topic_name}: {e}", exc_info=e)
            raise

    async def _validate_topic_creation_locked(self, topic_name: str) -> None:
        """Validate that a new topic can be created (assumes topics_lock is held)."""
        if len(self._topics) >= self._max_topics:
            raise RuntimeError(
                f"Maximum number of topics ({self._max_topics}) exceeded"
            )

    async def _create_bare_topic_locked(self, topic_name: str) -> Topic[T]:
        """Create and start topic only (assumes topics_lock is held)."""
        topic = Topic[T](topic_name, self._max_queue_size_per_topic)
        await topic.start()
        self._topics[topic_name] = topic
        self._logger.debug(f"Created topic: '{topic_name}'")
        return topic

    async def _wire_pattern_handlers_to_topic(
        self, topic: Topic[T], topic_name: str
    ) -> None:
        """Subscribe all matching pattern handlers to topic."""
        pattern_handlers = await self._get_pattern_handlers(topic_name)
        if pattern_handlers:
            await self._bulk_subscribe_handlers_to_topic(
                pattern_handlers, topic, topic_name
            )

    async def _bulk_subscribe_handlers_to_topic(
        self, handlers: list[Handler[T]], topic: Topic[T], topic_name: str
    ) -> None:
        """Subscribe multiple handlers to a topic and update tracking."""
        for handler in handlers:
            await topic.subscribe(handler)  # type: ignore[arg-type]
            async with self._handlers_lock:
                self._handlers_to_topics[hash(handler)].add(topic_name)

    async def _get_pattern_handlers(self, topic_name: str) -> list[Handler[T]]:
        """Get all pattern handlers that match the topic name."""
        async with self._handlers_lock:
            matched_handlers = []
            for pattern, handlers in self._pattern_handlers.items():
                if match_topic_to_pattern(topic_name, pattern):
                    matched_handlers.extend(handlers)
            return matched_handlers

    async def publish(self, event: T, topic_name: str) -> None:
        """Publish an event to a topic.

        Args:
            event: Event to publish
            topic_name: Topic to publish to
        """
        validated_topic = validate_and_normalize_topic(topic_name)

        try:
            await self._ensure_topic_exists(validated_topic)
            await self._publish_to_topic(event, validated_topic)
        except Exception as e:
            self._logger.error(
                f"Failed to publish event {event} to {validated_topic}: {e}", exc_info=e
            )
            raise

    async def _publish_to_topic(self, event: T, topic_name: str) -> None:
        """Publish event to a specific topic."""
        async with self._topics_lock:
            if topic_name in self._topics:
                await self._topics[topic_name].publish(event)

    async def unsubscribe(
        self, handler: Handler[T], from_topic: str | None = None
    ) -> None:
        """Unsubscribe a handler from topics.

        Args:
            handler: Handler to unsubscribe
            from_topic: Specific topic to unsubscribe from, or None for all topics
        """
        try:
            handler_id = hash(handler)

            # Determine scope: specific topic or all topics
            if from_topic:
                # Check if it's a pattern subscription
                if is_pattern(from_topic):
                    # For patterns, check if handler is subscribed to the pattern
                    if await self._handler_subscribed_to_pattern(handler, from_topic):
                        topics_to_process = [from_topic]
                    else:
                        topics_to_process = []
                else:
                    # For regular topics, check normal subscription
                    topics_to_process = (
                        [from_topic]
                        if await self._handler_subscribed_to_topic(
                            handler_id, from_topic
                        )
                        else []
                    )
            else:
                topics_to_process = await self._get_handler_topics(handler_id, None)
                # Also get pattern subscriptions for complete unsubscribe
                pattern_subscriptions = await self._get_handler_patterns(handler)
                topics_to_process.extend(pattern_subscriptions)

            if not topics_to_process:
                self._logger.debug(f"Handler {handler} not found for unsubscription")
                return

            # Process unsubscription for each topic
            for topic_name in topics_to_process:
                if is_pattern(topic_name):
                    await self._remove_pattern_handler(handler, topic_name)
                else:
                    await self._handle_topic_unsubscription(handler, topic_name)

            await self._cleanup_handler_tracking(handler_id)

        except Exception as e:
            self._logger.error(
                f"Failed to unsubscribe handler {handler}: {e}", exc_info=e
            )
            raise

    async def _handler_subscribed_to_topic(
        self, handler_id: HandlerId, topic_name: str
    ) -> bool:
        """Check if handler is subscribed to a specific topic."""
        async with self._handlers_lock:
            return (
                handler_id in self._handlers_to_topics
                and topic_name in self._handlers_to_topics[handler_id]
            )

    async def _handler_subscribed_to_pattern(
        self, handler: Handler[T], pattern: str
    ) -> bool:
        """Check if handler is subscribed to a specific pattern."""
        async with self._handlers_lock:
            return (
                pattern in self._pattern_handlers
                and handler in self._pattern_handlers[pattern]
            )

    async def _get_handler_patterns(self, handler: Handler[T]) -> list[str]:
        """Get all patterns a handler is subscribed to."""
        async with self._handlers_lock:
            return [
                pattern
                for pattern, handlers in self._pattern_handlers.items()
                if handler in handlers
            ]

    async def _get_handler_topics(
        self, handler_id: HandlerId, specific_topic: str | None
    ) -> list[TopicName]:
        """Get topics for a handler with proper locking."""
        async with self._handlers_lock:
            if handler_id not in self._handlers_to_topics:
                return []

            if specific_topic:
                return (
                    [specific_topic]
                    if specific_topic in self._handlers_to_topics[handler_id]
                    else []
                )
            else:
                return list(self._handlers_to_topics[handler_id])

    async def _handle_topic_unsubscription(
        self, handler: Handler[T], topic_name: str
    ) -> None:
        """Handle unsubscription from a specific topic with cleanup."""
        await self._unsubscribe_handler_from_topic(handler, topic_name)
        await self._remove_handler_topic_tracking(handler, topic_name)
        await self._cleanup_topic_if_empty(topic_name)

    async def _unsubscribe_handler_from_topic(
        self, handler: Handler[T], topic_name: str
    ) -> None:
        """Unsubscribe a handler from a topic."""
        async with self._topics_lock:
            if topic_name in self._topics:
                await self._topics[topic_name].unsubscribe(handler)

    async def _remove_handler_topic_tracking(
        self, handler: Handler[T], topic_name: str
    ) -> None:
        """Remove topic from handler tracking."""
        async with self._handlers_lock:
            handler_id = hash(handler)
            if (
                handler_id in self._handlers_to_topics
                and topic_name in self._handlers_to_topics[handler_id]
            ):
                self._handlers_to_topics[handler_id].remove(topic_name)

    async def _cleanup_handler_tracking(self, handler_id: HandlerId) -> None:
        """Clean up handler tracking if no topics left."""
        async with self._handlers_lock:
            if (
                handler_id in self._handlers_to_topics
                and not self._handlers_to_topics[handler_id]
            ):
                del self._handlers_to_topics[handler_id]

    async def _cleanup_topic_if_empty(self, topic_name: str) -> None:
        """Clean up topic if it has no more handlers to free memory."""
        try:
            has_handlers = await self._topic_has_handlers(topic_name)

            if not has_handlers:
                topic = await self._remove_empty_topic(topic_name)
                if topic:
                    await topic.stop()
                    await topic.close()
                    self._logger.debug(f"Cleaned up empty topic: `{topic_name}`")

        except Exception as e:
            self._logger.error(
                f"Failed to cleanup topic `{topic_name}`: {e}", exc_info=e
            )

    async def _topic_has_handlers(self, topic_name: str) -> bool:
        """Check if topic has any handlers."""
        async with self._handlers_lock:
            return any(
                topic_name in topic_list
                for topic_list in self._handlers_to_topics.values()
            )

    async def _remove_empty_topic(self, topic_name: str) -> Topic[T] | None:
        """Remove topic if it exists and return it for cleanup."""
        async with self._topics_lock:
            return self._topics.pop(topic_name, None)

    async def _remove_pattern_handler(self, handler: Handler[T], pattern: str) -> None:
        """Remove a specific handler for a pattern."""
        # Remove from pattern handlers
        async with self._handlers_lock:
            if (
                pattern in self._pattern_handlers
                and handler in self._pattern_handlers[pattern]
            ):
                self._pattern_handlers[pattern].remove(handler)
                # Clean up empty pattern list
                if not self._pattern_handlers[pattern]:
                    del self._pattern_handlers[pattern]
                    _clear_pattern_cache(pattern)

        # Unsubscribe from all matching topics
        await self._unsubscribe_handler_from_pattern_topics(handler, pattern)

    async def _remove_pattern_handlers(self, pattern: str) -> None:
        """Remove all handlers for a pattern without recursion."""
        handlers = await self._get_and_remove_pattern_handlers(pattern)

        if not handlers:
            return

        # Unsubscribe from all matching topics
        for handler in handlers:
            try:
                await self._unsubscribe_handler_from_pattern_topics(handler, pattern)
            except Exception as e:
                self._logger.error(
                    f"Failed to unsubscribe pattern handler {handler}: {e}", exc_info=e
                )

    async def _get_and_remove_pattern_handlers(self, pattern: str) -> list[Handler[T]]:
        """Get and remove pattern handlers atomically."""
        async with self._handlers_lock:
            if pattern not in self._pattern_handlers:
                return []

            handlers = list(self._pattern_handlers[pattern])
            del self._pattern_handlers[pattern]

            # Clean up compiled pattern cache
            _clear_pattern_cache(pattern)

            return handlers

    async def _unsubscribe_handler_from_pattern_topics(
        self, handler: Handler[T], pattern: str
    ) -> None:
        """Unsubscribe a handler from all topics that match the pattern."""
        handler_id = hash(handler)

        # Get matching topics with proper locking
        async with self._handlers_lock:
            if handler_id not in self._handlers_to_topics:
                return

            matching_topics = [
                topic_name
                for topic_name in self._handlers_to_topics[handler_id]
                if match_topic_to_pattern(topic_name, pattern)
            ]

        # Unsubscribe from each matching topic
        for topic_name in matching_topics:
            await self._handle_topic_unsubscription(handler, topic_name)

        # Clean up handler tracking if no topics left
        async with self._handlers_lock:
            if (
                handler_id in self._handlers_to_topics
                and not self._handlers_to_topics[handler_id]
            ):
                del self._handlers_to_topics[handler_id]

    async def close(self) -> None:
        """Close the service bus and all topics."""
        try:
            # Stop and close all topics
            for topic_name, topic in self._topics.items():
                try:
                    await topic.stop()
                    await topic.close()
                    self._logger.debug(f"Closed topic {topic_name}")
                except Exception as e:
                    self._logger.error(
                        f"Failed to close topic {topic_name}: {e}", exc_info=e
                    )

            # Clear all tracking data
            self._topics.clear()
            self._handlers_to_topics.clear()
            self._pattern_handlers.clear()

            # Clear pattern cache
            _clear_pattern_cache()

            self._logger.debug("Service bus closed")

        except Exception as e:
            self._logger.error(f"Error while closing service bus: {e}", exc_info=e)

    async def __aenter__(self) -> "ServiceBus[T]":
        return self

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        await self.close()
