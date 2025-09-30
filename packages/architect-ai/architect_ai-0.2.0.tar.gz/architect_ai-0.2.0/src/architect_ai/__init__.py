"""
Architect AI - An AI-powered architecture planning system.
"""

from .architect import Architect
from .blueprint import Blueprint
from .blueprint_rack import (
    BlueprintRack,
    # Blueprint rack exceptions
    BlueprintRackError,
    BlueprintValidationError,
    DuplicateBlueprintError,
)
from .tool import Tool
from .concurrent_executable import ConcurrentExecutable
from .execution_mode import ExecutionMode
from .toolbox import ToolBox
from .client import Client
from .build import Build
# Note: concurrency_wrapper module doesn't exist in current system
from .exceptions import (
    # Architect exceptions
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
    # Tool exceptions
    ToolError,
    PrecallableToolNotFoundError,
    PrecallableToolExecutionError,
    PrecallableToolRuntimeError,
    # Toolbox exceptions
    ToolBoxError,
    ToolValidationError,
    DuplicateToolError,
)

__version__ = "0.1.0"
__all__ = [
    # Core classes
    "Architect",
    "Blueprint", 
    "BlueprintRack",
    "Tool",
    "ConcurrentExecutable",
    "ExecutionMode",
    "ToolBox",
    "Client",
    "Build",
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
    # Blueprint rack exceptions
    "BlueprintRackError",
    "BlueprintValidationError",
    "DuplicateBlueprintError",
    # Tool exceptions
    "ToolError",
    "PrecallableToolNotFoundError",
    "PrecallableToolExecutionError", 
    "PrecallableToolRuntimeError",
    # Toolbox exceptions
    "ToolBoxError",
    "ToolValidationError",
    "DuplicateToolError",
]
