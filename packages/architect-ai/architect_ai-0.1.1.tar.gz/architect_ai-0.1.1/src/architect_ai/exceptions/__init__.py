"""Exception classes for architect_ai package."""

from .tool_exceptions import (
    ToolError,
    PrecallableToolNotFoundError,
    PrecallableToolExecutionError,
    PrecallableToolRuntimeError,
)

from .architect_exceptions import (
    ArchitectError,
    PrecallableToolError,
    BuildPlanParsingError,
    BlueprintNotFoundError,
    ToolExecutionModeError,
    ToolExecutionError,
    ReferenceResolutionError,
    InvalidReferencePathError,
    StageValidationError,
    BuildPlanGenerationError,
    ToolPicklingError,
)

from .toolbox_exceptions import (
    ToolBoxError,
    ToolValidationError,
    DuplicateToolError,
)

__all__ = [
    # Tool exceptions
    "ToolError",
    "PrecallableToolNotFoundError",
    "PrecallableToolExecutionError",
    "PrecallableToolRuntimeError",
    
    # Architect exceptions
    "ArchitectError",
    "PrecallableToolError",
    "BuildPlanParsingError",
    "BlueprintNotFoundError",
    "ToolExecutionModeError",
    "ToolExecutionError",
    "ReferenceResolutionError",
    "InvalidReferencePathError",
    "StageValidationError",
    "BuildPlanGenerationError",
    "ToolPicklingError",
    
    # Toolbox exceptions
    "ToolBoxError",
    "ToolValidationError",
    "DuplicateToolError",
]
