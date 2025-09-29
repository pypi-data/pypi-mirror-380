"""Architect-related exception classes for architect_ai package."""

from typing import Optional


class ArchitectError(Exception):
    """Base exception for all Architect-related errors."""
    
    def __init__(self, message: str, correlation_id: Optional[str] = None, **context):
        super().__init__(message)
        self.correlation_id = correlation_id
        self.context = context
    
    def __str__(self):
        base = super().__str__()
        if self.correlation_id:
            base += f" [correlation_id: {self.correlation_id}]"
        return base


class PrecallableToolError(ArchitectError):
    """Raised when precallable tool startup fails."""
    
    def __init__(self, message: str, tool_count: Optional[int] = None, **context):
        super().__init__(
            f"Precallable tool error: {message}",
            tool_count=tool_count,
            **context
        )


class BuildPlanParsingError(ArchitectError):
    """Raised when build plan JSON parsing fails."""
    
    def __init__(self, json_error: str, build_plan_preview: Optional[str] = None, **context):
        super().__init__(
            f"Failed to parse build plan JSON: {json_error}",
            json_error=json_error,
            build_plan_preview=build_plan_preview,
            **context
        )


class BlueprintNotFoundError(ArchitectError):
    """Raised when a requested blueprint is not found in the blueprint rack."""
    
    def __init__(self, blueprint_name: str, **context):
        super().__init__(
            f"Blueprint '{blueprint_name}' not found in blueprint rack",
            blueprint_name=blueprint_name,
            **context
        )


class ToolExecutionModeError(ArchitectError):
    """Raised when there's a mismatch between tool execution mode and implementation."""
    
    def __init__(self, tool_name: str, execution_mode: str, issue: str, **context):
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
        super().__init__(
            f"Failed to resolve reference '{reference_path}': {issue}",
            **context
        )
        self.reference_path = reference_path
        self.issue = issue


class InvalidReferencePathError(ReferenceResolutionError):
    """Raised when a reference path has invalid format."""
    
    def __init__(self, reference_path: str, **context):
        super().__init__(
            reference_path,
            "Invalid reference path format",
            **context
        )


class StageValidationError(ReferenceResolutionError):
    """Raised when stage reference validation fails (e.g., forward references)."""
    
    def __init__(self, reference_path: str, current_stage: int, referenced_stage: int, **context):
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
        super().__init__(
            f"Failed to generate build plan after {max_attempts} attempts",
            max_attempts=max_attempts,
            **context
        )


class ToolPicklingError(ArchitectError):
    """Raised when a PROCESS-mode tool instance cannot be pickled for execution."""
    
    def __init__(self, tool_name: str, original_error: Optional[Exception] = None, **context):
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
        super().__init__(
            f"Tool '{tool_name}' not found in toolbox while executing stage '{stage_name}'",
            tool_name=tool_name,
            stage_name=stage_name,
            available_tools=available_tools or [],
            **context
        )