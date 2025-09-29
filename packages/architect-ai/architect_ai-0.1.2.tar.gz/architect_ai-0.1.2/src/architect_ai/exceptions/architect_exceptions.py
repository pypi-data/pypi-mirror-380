"""Architect-related exception classes for architect_ai package."""

from typing import Optional


class ArchitectError(Exception):
    """Base exception for all Architect-related errors."""
    
    def __init__(self, message: str, correlation_id: Optional[str] = None, **context):
        """
        Initialize the architect error with message, correlation ID and context.
        
        Args:
            message (str): Error message
            correlation_id (Optional[str]): Optional correlation ID for request tracing
            **context: Additional context information
            
        Returns:
            None: Initializes the architect error instance
        """
        super().__init__(message)
        self.correlation_id = correlation_id
        self.context = context
    
    def __str__(self):
        """
        Return string representation of the error with correlation ID if available.
        
        Args:
            None
            
        Returns:
            str: String representation of the error
        """
        base = super().__str__()
        if self.correlation_id:
            base += f" [correlation_id: {self.correlation_id}]"
        return base


class PrecallableToolError(ArchitectError):
    """Raised when precallable tool startup fails."""
    
    def __init__(self, message: str, tool_count: Optional[int] = None, **context):
        """
        Initialize the precallable tool error.
        
        Args:
            message (str): Error message
            tool_count (Optional[int]): Number of tools that failed
            **context: Additional context information
            
        Returns:
            None: Initializes the precallable tool error instance
        """
        super().__init__(
            f"Precallable tool error: {message}",
            tool_count=tool_count,
            **context
        )


class BuildPlanParsingError(ArchitectError):
    """Raised when build plan JSON parsing fails."""
    
    def __init__(self, json_error: str, build_plan_preview: Optional[str] = None, **context):
        """
        Initialize the build plan parsing error.
        
        Args:
            json_error (str): JSON parsing error message
            build_plan_preview (Optional[str]): Preview of the build plan that failed to parse
            **context: Additional context information
            
        Returns:
            None: Initializes the build plan parsing error instance
        """
        super().__init__(
            f"Failed to parse build plan JSON: {json_error}",
            json_error=json_error,
            build_plan_preview=build_plan_preview,
            **context
        )


class BlueprintNotFoundError(ArchitectError):
    """Raised when a requested blueprint is not found in the blueprint rack."""
    
    def __init__(self, blueprint_name: str, **context):
        """
        Initialize the blueprint not found error.
        
        Args:
            blueprint_name (str): Name of the blueprint that was not found
            **context: Additional context information
            
        Returns:
            None: Initializes the blueprint not found error instance
        """
        super().__init__(
            f"Blueprint '{blueprint_name}' not found in blueprint rack",
            blueprint_name=blueprint_name,
            **context
        )


class ToolExecutionModeError(ArchitectError):
    """Raised when there's a mismatch between tool execution mode and implementation."""
    
    def __init__(self, tool_name: str, execution_mode: str, issue: str, **context):
        """
        Initialize the tool execution mode error.
        
        Args:
            tool_name (str): Name of the tool with execution mode issue
            execution_mode (str): The problematic execution mode
            issue (str): Description of the execution mode issue
            **context: Additional context information
            
        Returns:
            None: Initializes the tool execution mode error instance
        """
        super().__init__(
            f"Tool '{tool_name}' execution mode '{execution_mode}' error: {issue}",
            tool_name=tool_name,
            execution_mode=execution_mode,
            issue=issue,
            **context
        )


class ToolExecutionError(ArchitectError):
    """Raised when tool execution fails during stage execution."""
    
    def __init__(self, tool_name: str, stage_name: str, original_error: Exception, **context):
        """
        Initialize the tool execution error.
        
        Args:
            tool_name (str): Name of the tool that failed to execute
            stage_name (str): Name of the stage where execution failed
            original_error (Exception): The original exception that caused the failure
            **context: Additional context information
            
        Returns:
            None: Initializes the tool execution error instance
        """
        super().__init__(
            f"Tool execution failed for '{tool_name}' in stage '{stage_name}': {original_error}",
            tool_name=tool_name,
            stage_name=stage_name,
            original_error=str(original_error),
            original_error_type=type(original_error).__name__,
            **context
        )


class ReferenceResolutionError(ArchitectError):
    """Raised when reference resolution fails."""
    
    def __init__(self, reference_path: str, issue: str, **context):
        """
        Initialize the reference resolution error.
        
        Args:
            reference_path (str): Path of the reference that failed to resolve
            issue (str): Description of the resolution issue
            **context: Additional context information
            
        Returns:
            None: Initializes the reference resolution error instance
        """
        super().__init__(
            f"Failed to resolve reference '{reference_path}': {issue}",
            **context
        )
        self.reference_path = reference_path
        self.issue = issue


class InvalidReferencePathError(ReferenceResolutionError):
    """Raised when a reference path has invalid format."""
    
    def __init__(self, reference_path: str, **context):
        """
        Initialize the invalid reference path error.
        
        Args:
            reference_path (str): The invalid reference path
            **context: Additional context information
            
        Returns:
            None: Initializes the invalid reference path error instance
        """
        super().__init__(
            reference_path,
            "Invalid reference path format",
            **context
        )


class StageValidationError(ReferenceResolutionError):
    """Raised when stage reference validation fails (e.g., forward references)."""
    
    def __init__(self, reference_path: str, current_stage: int, referenced_stage: int, **context):
        """
        Initialize the stage validation error.
        
        Args:
            reference_path (str): Path of the reference that failed validation
            current_stage (int): Current stage number
            referenced_stage (int): Stage number being referenced
            **context: Additional context information
            
        Returns:
            None: Initializes the stage validation error instance
        """
        super().__init__(
            reference_path,
            f"Stage {current_stage} cannot reference stage {referenced_stage}. Stages can only reference outputs from previous stages.",
            current_stage=current_stage,
            referenced_stage=referenced_stage,
            **context
        )


class BuildPlanGenerationError(ArchitectError):
    """Raised when build plan generation fails after maximum attempts."""
    
    def __init__(self, max_attempts: int, **context):
        """
        Initialize the build plan generation error.
        
        Args:
            max_attempts (int): Maximum number of attempts that were made
            **context: Additional context information
            
        Returns:
            None: Initializes the build plan generation error instance
        """
        super().__init__(
            f"Failed to generate build plan after {max_attempts} attempts",
            max_attempts=max_attempts,
            **context
        )


class ToolPicklingError(ArchitectError):
    """Raised when a PROCESS-mode tool instance cannot be pickled for execution."""
    
    def __init__(self, tool_name: str, original_error: Optional[Exception] = None, **context):
        """
        Initialize the tool pickling error.
        
        Args:
            tool_name (str): Name of the tool that failed to be pickled
            original_error (Optional[Exception]): The original pickling error
            **context: Additional context information
            
        Returns:
            None: Initializes the tool pickling error instance
        """
        super().__init__(
            f"Tool '{tool_name}' is not pickleable for PROCESS execution: {original_error}",
            tool_name=tool_name,
            original_error=str(original_error) if original_error else None,
            original_error_type=type(original_error).__name__ if original_error else None,
            **context
        )


class ToolNotFoundError(ArchitectError):
    """Raised when a referenced tool is not found in the toolbox during stage execution."""
    
    def __init__(self, tool_name: str, stage_name: str, available_tools: Optional[list] = None, **context):
        """
        Initialize the tool not found error.
        
        Args:
            tool_name (str): Name of the tool that was not found
            stage_name (str): Name of the stage where the tool was needed
            available_tools (Optional[list]): List of available tools
            **context: Additional context information
            
        Returns:
            None: Initializes the tool not found error instance
        """
        super().__init__(
            f"Tool '{tool_name}' not found in toolbox while executing stage '{stage_name}'",
            tool_name=tool_name,
            stage_name=stage_name,
            available_tools=available_tools or [],
            **context
        )


class ExecutableFailedToStartError(ArchitectError):
    """
    Raised when a concurrent executable fails to start.
    
    Args:
        message (str): Error message describing the failure
        
    Returns:
        None: Exception class for concurrent executable start failures
    """
    pass


class BuildGenerationError(ArchitectError):
    """
    Raised when build plan generation fails.
    
    Args:
        message (str): Error message describing the generation failure
        
    Returns:
        None: Exception class for build generation failures
    """
    pass