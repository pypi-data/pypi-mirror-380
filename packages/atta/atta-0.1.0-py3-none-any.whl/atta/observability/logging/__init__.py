import logging
from typing import cast

from atta.observability.logging.protocol import LoggingProtocol


def get_logger(name: str) -> LoggingProtocol:
    """Get logger for telemetry."""
    return cast(LoggingProtocol, logging.getLogger(name))


__all__ = ["LoggingProtocol", "get_logger"]
