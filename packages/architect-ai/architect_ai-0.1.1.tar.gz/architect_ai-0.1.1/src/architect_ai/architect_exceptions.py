"""Exceptions for the new architect system."""


class ExecutableFailedToStartError(Exception):
    """Raised when a concurrent executable fails to start."""
    pass


class BuildGenerationError(Exception):
    """Raised when build plan generation fails."""
    pass
