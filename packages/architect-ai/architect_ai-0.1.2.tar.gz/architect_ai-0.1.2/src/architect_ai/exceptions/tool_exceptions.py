"""Tool-related exception classes for architect_ai package."""

from typing import List, Optional


class ToolError(Exception):
    """Base exception for tool-related errors."""
    
    def __init__(self, message: str, tool_name: Optional[str] = None, **context):
        """
        Initialize the tool error with message and context.
        
        Args:
            message (str): Error message
            tool_name (Optional[str]): Name of the tool that caused the error
            **context: Additional context information
            
        Returns:
            None: Initializes the tool error instance
        """
        super().__init__(message)
        self.tool_name = tool_name
        self.context = context


class PrecallableToolNotFoundError(ToolError):
    """Raised when a precallable tool is not found."""
    
    def __init__(self, tool_name: str, available_tools: Optional[List[str]] = None, **context):
        """
        Initialize the precallable tool not found error.
        
        Args:
            tool_name (str): Name of the tool that was not found
            available_tools (Optional[List[str]]): List of available tool names
            **context: Additional context information
            
        Returns:
            None: Initializes the precallable tool not found error instance
        """
        super().__init__(
            f"Precallable tool '{tool_name}' not found",
            tool_name=tool_name,
            available_tools=available_tools or [],
            **context
        )


class PrecallableToolExecutionError(ToolError):
    """Raised when getting result from precallable tool fails."""
    
    def __init__(self, tool_name: str, original_error: Exception, **context):
        """
        Initialize the precallable tool execution error.
        
        Args:
            tool_name (str): Name of the tool that failed to execute
            original_error (Exception): The original exception that caused the failure
            **context: Additional context information
            
        Returns:
            None: Initializes the precallable tool execution error instance
        """
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
        """
        Initialize the precallable tool runtime error.
        
        Args:
            issue (str): Description of the runtime issue
            tool_name (Optional[str]): Name of the tool with runtime issue
            **context: Additional context information
            
        Returns:
            None: Initializes the precallable tool runtime error instance
        """
        super().__init__(
            f"Precallable tool runtime error: {issue}",
            tool_name=tool_name,
            issue=issue,
            **context
        )
