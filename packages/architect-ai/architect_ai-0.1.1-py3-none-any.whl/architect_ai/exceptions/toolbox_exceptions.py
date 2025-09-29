"""Toolbox-related exception classes for architect_ai package."""

from typing import Optional


class ToolBoxError(Exception):
    """Base exception for ToolBox-related errors."""
    
    def __init__(self, message: str, **context):
        super().__init__(message)
        self.context = context


class ToolValidationError(ToolBoxError):
    """Raised when tool validation fails."""
    
    def __init__(self, issue: str, tool_type: Optional[str] = None, tool_name: Optional[str] = None, **context):
        super().__init__(
            f"Tool validation failed: {issue}",
            issue=issue,
            tool_type=tool_type,
            tool_name=tool_name,
            **context
        )


class DuplicateToolError(ToolBoxError):
    """Raised when attempting to add a tool with a name that already exists."""
    
    def __init__(self, tool_name: str, **context):
        super().__init__(
            f"Tool with name '{tool_name}' already exists",
            tool_name=tool_name,
            **context
        )
