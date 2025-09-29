"""Toolbox-related exception classes for architect_ai package."""

from typing import Optional


class ToolBoxError(Exception):
    """Base exception for ToolBox-related errors."""
    
    def __init__(self, message: str, **context):
        """
        Initialize the toolbox error with message and context.
        
        Args:
            message (str): Error message
            **context: Additional context information
            
        Returns:
            None: Initializes the toolbox error instance
        """
        super().__init__(message)
        self.context = context


class ToolValidationError(ToolBoxError):
    """Raised when tool validation fails."""
    
    def __init__(self, issue: str, tool_type: Optional[str] = None, tool_name: Optional[str] = None, **context):
        """
        Initialize the tool validation error.
        
        Args:
            issue (str): Description of the validation issue
            tool_type (Optional[str]): Type of tool that failed validation
            tool_name (Optional[str]): Name of tool that failed validation
            **context: Additional context information
            
        Returns:
            None: Initializes the tool validation error instance
        """
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
        """
        Initialize the duplicate tool error.
        
        Args:
            tool_name (str): Name of the duplicate tool
            **context: Additional context information
            
        Returns:
            None: Initializes the duplicate tool error instance
        """
        super().__init__(
            f"Tool with name '{tool_name}' already exists",
            tool_name=tool_name,
            **context
        )
