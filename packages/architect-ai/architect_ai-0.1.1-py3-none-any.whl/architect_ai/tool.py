"""Tool interfaces for architect_ai package."""

from abc import ABC, abstractmethod
from typing import Dict, Tuple, Any, Optional, List, Callable, TYPE_CHECKING
from .execution_mode import ExecutionMode

if TYPE_CHECKING:
    from .concurrent_executable import ConcurrentExecutable

def wrap_tool_func(func: Callable, parameters: Dict[str, Any], concurrent_executables: Optional[List["ConcurrentExecutable"]] = None) -> Callable:
    def wrapped_func():
        return func(parameters, concurrent_executables)
    return wrapped_func

class Tool(ABC):
    """Tool that runs during build plan execution with parameters and precallable results."""

    @abstractmethod
    def use(self, parameters: Dict[str, Any], concurrent_executables: Optional[List["ConcurrentExecutable"]] = None) -> Any:
        """
        Execute the tool with parameters and precallable results.

        Args:
            parameters: Tool parameters from the build plan
            precallables: Results from concurrent executables (optional)
        
        Returns:
            The result of the tool execution.
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def execution_mode(self) -> ExecutionMode:
        """
        Defines how this tool should be executed.
        
        Returns:
            ExecutionType.ASYNCIO: For I/O-bound operations
            ExecutionType.THREAD: For CPU-bound operations  
            ExecutionType.PROCESS: For heavy CPU-bound operations
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def name(self) -> str:
        """Unique identifier for this tool."""
        raise NotImplementedError

    @property
    @abstractmethod
    def usage_context(self) -> str:
        """Description of when this tool should be used."""
        raise NotImplementedError

    @property
    @abstractmethod
    def purpose(self) -> str:
        """Description of what this tool accomplishes."""
        raise NotImplementedError

    @property
    @abstractmethod
    def parameter_instructions(self) -> Dict[str, Tuple[str, str]]:
        """Map of parameter names to (DataType, description) tuples."""
        raise NotImplementedError

    @property
    @abstractmethod
    def output_descriptions(self) -> Dict[str, Tuple[str, str]]:
        """Map of output names to (DataType, description) tuples."""
        raise NotImplementedError

