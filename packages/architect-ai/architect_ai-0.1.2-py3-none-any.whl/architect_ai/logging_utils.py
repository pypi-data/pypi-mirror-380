"""
Shared logging utilities for the architect_ai package.
"""
import logging
from typing import Optional


def log_structured(
    logger: logging.Logger,
    level: str,
    message: str,
    correlation_id: Optional[str] = None,
    perf_time: Optional[float] = None,
    **kwargs,
) -> None:
    """
    Helper function for structured logging using extra parameters.
    
    Args:
        logger (logging.Logger): The logger instance to use
        level (str): The log level ('debug', 'info', 'warning', 'error', 'critical')
        message (str): The log message
        correlation_id (Optional[str]): Optional correlation ID for request tracing
        perf_time (Optional[float]): Optional performance timing in seconds
        **kwargs: Additional structured data to include in the log
        
    Returns:
        None: Logs the structured message with extra data
    """
    RESERVED_ATTRS = {
        'name', 'msg', 'args', 'levelname', 'levelno', 'pathname', 'filename',
        'module', 'lineno', 'funcName', 'created', 'msecs', 'relativeCreated',
        'thread', 'threadName', 'processName', 'process', 'getMessage',
        'exc_info', 'exc_text', 'stack_info'
    }
    extra_data = {}
    for key, value in kwargs.items():
        if key in RESERVED_ATTRS:
            extra_data[f"data_{key}"] = value
        else:
            extra_data[key] = value
    if correlation_id:
        extra_data["correlation_id"] = correlation_id
    if perf_time is not None:
        extra_data["perf_time"] = round(perf_time, 3)
    getattr(logger, level)(message, extra=extra_data)
