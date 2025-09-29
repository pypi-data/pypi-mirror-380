from abc import ABC, abstractmethod
from typing import Dict, Tuple, Any, List, TYPE_CHECKING, Iterator, Optional
import re
import time
import concurrent.futures

if TYPE_CHECKING:
    from .build import Build
    from .concurrent_executable import ConcurrentExecutable


class Blueprint(ABC):
    """Base interface that all user-defined blueprints must implement."""

    @abstractmethod
    def fill(self, parameters: Dict[str, Any]) -> None:
        """
        Fill in the blueprint with the provided parameters.

        Args:
            parameters (Dict[str, Any]): A dictionary of parameters to use to fill in the blueprint
            
        Returns:
            None: Fills the blueprint with provided parameters
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Unique identifier for this blueprint.
        
        Args:
            None
            
        Returns:
            str: The unique name of this blueprint
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def usage_context(self) -> str:
        """
        Description of when this blueprint should be used.
        
        Args:
            None
            
        Returns:
            str: Context description for when to use this blueprint
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def purpose(self) -> str:
        """
        Description of what this blueprint is used for.
        
        Args:
            None
            
        Returns:
            str: Purpose description of what this blueprint accomplishes
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
    def parameter_to_value_map(self) -> Dict[str, Any]:
        """
        Map of parameter names to their filled values.
        
        Args:
            None
            
        Returns:
            Dict[str, Any]: Map of parameter names to their current values
        """
        raise NotImplementedError


class LazyBlueprint:
    """
    A wrapper for blueprints that enables lazy evaluation of parameters.
    
    Instead of immediately resolving $ref references and filling the blueprint,
    this class stores the raw parameters and resolves them on-demand when
    the user calls resolve().
    """
    
    def __init__(
        self,
        blueprint: Blueprint,
        raw_parameters: Dict[str, Any],
        stage_outputs: Dict[str, Dict[str, Any]],
        build_instance: "Build",
        instance_key: str
    ):
        """
        Initialize a lazy blueprint.
        
        Args:
            blueprint (Blueprint): The actual blueprint instance to fill
            raw_parameters (Dict[str, Any]): Parameters with potentially unresolved $ref references
            stage_outputs (Dict[str, Dict[str, Any]]): Dictionary of stage outputs containing ConcurrentExecutables
            build_instance (Build): Build instance to access _resolve_references method
            instance_key (str): The top-level plan key for this blueprint instance
            
        Returns:
            None: Initializes the lazy blueprint instance
        """
        self.blueprint = blueprint
        self.raw_parameters = raw_parameters
        self.stage_outputs = stage_outputs
        self.build_instance = build_instance
        self._instance_key = instance_key
        self._filled = False
        self._dependencies = self._extract_dependencies()
    
    def _extract_dependencies(self) -> List["ConcurrentExecutable"]:
        """
        Extract all ConcurrentExecutable dependencies from raw parameters.
        
        Args:
            None
            
        Returns:
            List[ConcurrentExecutable]: List of concurrent executables that this blueprint depends on
        """
        dependencies = []
        ref_pattern = r'\$ref\.(stage_\d+)\.([a-zA-Z0-9_]+(?:\[-?\d+\])*(?:\.[a-zA-Z0-9_]+(?:\[-?\d+\])*)*)'
        
        def find_refs_in_data(data):
            """
            Recursively find $ref references in nested data structures.
            
            Args:
                data: Data structure to search for references
                
            Returns:
                None: Appends found dependencies to the dependencies list
            """
            if isinstance(data, str):
                matches = re.findall(ref_pattern, data)
                for stage_name, tool_name_with_param in matches:
                    tool_name = tool_name_with_param.split('.')[0]
                    if (stage_name in self.stage_outputs and 
                        tool_name in self.stage_outputs[stage_name]):
                        stage_result = self.stage_outputs[stage_name][tool_name]
                        if hasattr(stage_result, 'fetch_results') and hasattr(stage_result, 'is_current_running'):
                            if stage_result not in dependencies:
                                dependencies.append(stage_result)
            elif isinstance(data, dict):
                for value in data.values():
                    find_refs_in_data(value)
            elif isinstance(data, list):
                for item in data:
                    find_refs_in_data(item)
        
        find_refs_in_data(self.raw_parameters)
        return dependencies
    
    def is_ready(self) -> bool:
        """
        Check if all dependencies are ready (all ConcurrentExecutables are complete).
        
        Args:
            None
            
        Returns:
            bool: True if blueprint can be resolved immediately, False otherwise
        """
        if self._filled:
            return True
            
        for dependency in self._dependencies:
            if not dependency.is_ready():
                return False
        
        return True
    
    def resolve(self) -> None:
        """
        Resolve all $ref references and fill the underlying blueprint.
        
        Args:
            None
            
        Returns:
            None: Fills the underlying blueprint with resolved parameters
            
        Raises:
            ValueError: If blueprint is already filled or resolution fails
        """
        if self._filled:
            raise ValueError(f"Blueprint '{self.blueprint.name}' is already filled")
        
        resolved_parameters = self.build_instance._resolve_references(
            self.raw_parameters, 
            self.stage_outputs
        )
        self.blueprint.fill(resolved_parameters)
        self._filled = True
    
    def is_filled(self) -> bool:
        """
        Check if the blueprint has been resolved and filled.
        
        Args:
            None
            
        Returns:
            bool: True if blueprint has been filled, False otherwise
        """
        return self._filled
    
    @property
    def name(self) -> str:
        """
        Get the name of the underlying blueprint.
        
        Args:
            None
            
        Returns:
            str: Name of the underlying blueprint
        """
        return self.blueprint.name

    @property
    def plan_key(self) -> str:
        """
        Return the unique top-level key used in the build plan for this instance.
        
        Args:
            None
        
        Returns:
            str: The plan key for this blueprint instance (e.g., 'result_blueprint_1').
        """
        return self._instance_key


def blueprints_as_completed(lazy_blueprints: List[LazyBlueprint], max_wait_seconds: Optional[float] = None) -> Iterator[LazyBlueprint]:
    """Yield `LazyBlueprint` instances as dependencies complete, with optional timeout.

    Args:
        lazy_blueprints (List[LazyBlueprint]): Blueprints to monitor for readiness.
        max_wait_seconds (Optional[float]): Maximum seconds to wait before raising `TimeoutError`.

    Returns:
        Iterator[LazyBlueprint]: Iterator of ready blueprints in completion order.
    """
    remaining_blueprints: List[LazyBlueprint] = []
    for lazy_blueprint in lazy_blueprints:
        if lazy_blueprint.is_ready():
            yield lazy_blueprint
        else:
            remaining_blueprints.append(lazy_blueprint)
    if not remaining_blueprints:
        return
    dependency_futures = set()
    for lazy_blueprint in remaining_blueprints:
        for dependency in lazy_blueprint._dependencies:
            if hasattr(dependency, 'running_future') and dependency.running_future is not None and hasattr(dependency.running_future, 'done'):
                dependency_futures.add(dependency.running_future)
    if not dependency_futures:
        return
    yielded_blueprints = set()
    start_time_seconds: float = time.perf_counter()
    while dependency_futures:
        remaining_timeout: Optional[float] = None
        if max_wait_seconds is not None:
            elapsed_seconds: float = time.perf_counter() - start_time_seconds
            remaining_timeout = max(0.0, max_wait_seconds - elapsed_seconds)
            if remaining_timeout == 0.0:
                raise TimeoutError("Blueprint gathering timed out")
        done, pending = concurrent.futures.wait(dependency_futures, timeout=remaining_timeout, return_when=concurrent.futures.FIRST_COMPLETED)
        if not done:
            raise TimeoutError("Blueprint gathering timed out")
        dependency_futures = pending
        for lazy_blueprint in remaining_blueprints:
            if lazy_blueprint not in yielded_blueprints and lazy_blueprint.is_ready():
                yielded_blueprints.add(lazy_blueprint)
                yield lazy_blueprint
