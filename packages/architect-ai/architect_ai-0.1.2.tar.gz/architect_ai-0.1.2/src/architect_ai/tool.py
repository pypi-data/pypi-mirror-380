"""Tool interfaces for architect_ai package."""

from abc import ABC, abstractmethod
from typing import Dict, Tuple, Any, Optional, List, Callable, TYPE_CHECKING
from .execution_mode import ExecutionMode

if TYPE_CHECKING:
    from .concurrent_executable import ConcurrentExecutable

def wrap_tool_func(func: Callable, parameters: Dict[str, Any], concurrent_executables: Optional[List["ConcurrentExecutable"]] = None) -> Callable:
    """
    Wrap a tool function with predefined parameters and concurrent executables for deferred execution.
    
    Args:
        func (Callable): The tool function to wrap
        parameters (Dict[str, Any]): Parameters to pass to the function
        concurrent_executables (Optional[List[ConcurrentExecutable]]): Available concurrent executables
        
    Returns:
        Callable: Wrapped function that can be called without parameters
    """
    def wrapped_func():
        return func(parameters, concurrent_executables)
    return wrapped_func

class Tool(ABC):
    """Tool that runs during build plan execution with parameters and precallable results."""

    @abstractmethod
    def use(self, parameters: Dict[str, Any], concurrent_executables: Optional[List["ConcurrentExecutable"]] = None) -> Any:
        """
        Execute the tool with parameters and concurrent executables.

        Args:
            parameters (Dict[str, Any]): Tool parameters from the build plan
            concurrent_executables (Optional[List[ConcurrentExecutable]]): Available concurrent executables
        
        Returns:
            Any: The result of the tool execution
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def execution_mode(self) -> ExecutionMode:
        """
        Defines how this tool should be executed.
        
        Args:
            None
            
        Returns:
            ExecutionMode: Execution mode for this tool (ASYNCIO for I/O-bound, THREAD for CPU-bound, PROCESS for heavy CPU-bound)
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Unique identifier for this tool.
        
        Args:
            None
            
        Returns:
            str: The unique name of this tool
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def usage_context(self) -> str:
        """
        Description of when this tool should be used.
        
        Args:
            None
            
        Returns:
            str: Context description for when to use this tool
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def purpose(self) -> str:
        """
        Description of what this tool accomplishes.
        
        Args:
            None
            
        Returns:
            str: Purpose description of what this tool does
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def parameter_instructions(self) -> Dict[str, Tuple[str, str]]:
        """
        Map of parameter names to data type and description tuples.
        
        Args:
            None
            
        Returns:
            Dict[str, Tuple[str, str]]: Map of parameter names to (DataType, description) tuples
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def output_descriptions(self) -> Dict[str, Tuple[str, str]]:
        """
        Map of output names to data type and description tuples.
        
        Args:
            None
            
        Returns:
            Dict[str, Tuple[str, str]]: Map of output names to (DataType, description) tuples
        """
        raise NotImplementedError

