"""Tool-related exception classes for architect_ai package."""

from typing import List, Optional


class ToolError(Exception):
    """Base exception for tool-related errors."""
    
    def __init__(self, message: str, tool_name: Optional[str] = None, **context):
        super().__init__(message)
        self.tool_name = tool_name
        self.context = context


class PrecallableToolNotFoundError(ToolError):
    """Raised when a precallable tool is not found."""
    
    def __init__(self, tool_name: str, available_tools: Optional[List[str]] = None, **context):
        super().__init__(
            f"Precallable tool '{tool_name}' not found",
            tool_name=tool_name,
            available_tools=available_tools or [],
            **context
        )


class PrecallableToolExecutionError(ToolError):
    """Raised when getting result from precallable tool fails."""
    
    def __init__(self, tool_name: str, original_error: Exception, **context):
        super().__init__(
            f"Failed to get result from precallable tool '{tool_name}': {original_error}",
            tool_name=tool_name,
            original_error=str(original_error),
            original_error_type=type(original_error).__name__,
            **context
        )


class PrecallableToolRuntimeError(ToolError):
    """Raised when there's a runtime issue with precallable tools (e.g., no event loop)."""
    
    def __init__(self, issue: str, tool_name: Optional[str] = None, **context):
        super().__init__(
            f"Precallable tool runtime error: {issue}",
            tool_name=tool_name,
            issue=issue,
            **context
        )
