"""Build plan representation and execution logic."""

import importlib
try:
    json = importlib.import_module("ujson")
except Exception:
    import json as json
import logging
import asyncio
import re
from typing import Dict, Any, Optional, List
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

from .logging_utils import log_structured as log_with_structure
from .toolbox import ToolBox
from .blueprint_rack import BlueprintRack
from .concurrent_executable import ConcurrentExecutable
from .blueprint import LazyBlueprint
from .exceptions.architect_exceptions import (
    ToolNotFoundError,
    ReferenceResolutionError,
    InvalidReferencePathError,
    StageValidationError,
)

logger = logging.getLogger(__name__)


class Build:
    """Represents a build plan with execution capabilities."""
    
    def __init__(self, build_plan: str, build_correlation_id: str, streaming_mode: bool = False, **streaming_context):
        """Initialize build with plan and correlation ID.
        
        Args:
            build_plan (str): JSON string containing the build plan
            build_correlation_id (str): Unique identifier for this build instance
            streaming_mode (bool): Enable streaming execution mode
            **streaming_context: Additional context for streaming mode
            
        Returns:
            None: Constructor returns None
        """
        self.build_plan = build_plan
        self.build_correlation_id = build_correlation_id
        self._parsed_plan: Optional[Dict[str, Any]] = None
        self.filled_blueprints: Optional[List[Any]] = None
        self.lazy_blueprints: Optional[List[LazyBlueprint]] = None
        self.stage_outputs: Optional[Dict[str, Dict[str, Any]]] = None
        self.streaming_mode = streaming_mode
        self.streaming_context = streaming_context
        if streaming_mode:
            self.streaming_stage_outputs: Dict[str, Dict[str, Any]] = {}
            self.streaming_stage_futures: Dict[str, Any] = {}
    
    def get_parsed_plan(self) -> Dict[str, Any]:
        """Parse and return the build plan as a dictionary.
        
        Args:
            None
            
        Returns:
            Dict[str, Any]: Parsed build plan dictionary
        """
        if self._parsed_plan is None:
            try:
                self._parsed_plan = json.loads(self.build_plan)
            except Exception as json_decode_error:
                log_with_structure(
                    logger,
                    "error",
                    "Failed to parse build plan JSON",
                    build_correlation_id=self.build_correlation_id,
                    error=str(json_decode_error),
                    build_plan_text=self.build_plan,
                )
                raise BuildPlanParsingError(f"Invalid JSON in build plan: {json_decode_error}") from json_decode_error
        return self._parsed_plan
    
    def get_stages(self) -> Dict[str, Dict[str, Any]]:
        """Extract and return all stage configurations from the build plan.
        
        Args:
            None
            
        Returns:
            Dict[str, Dict[str, Any]]: Dictionary of stage configurations keyed by stage name
        """
        parsed_plan = self.get_parsed_plan()
        stages = {}
        for plan_key, plan_value in parsed_plan.items():
            if plan_key.startswith("stage_"):
                stages[plan_key] = plan_value
        return stages
    
    def get_blueprints(self) -> Dict[str, Dict[str, Any]]:
        """Extract and return all blueprint configurations from the build plan.
        
        Args:
            None
            
        Returns:
            Dict[str, Dict[str, Any]]: Dictionary of blueprint configurations keyed by blueprint name
        """
        parsed_plan = self.get_parsed_plan()
        blueprints = {}
        for plan_key, plan_value in parsed_plan.items():
            if not plan_key.startswith("stage_"):
                blueprints[plan_key] = plan_value
        return blueprints
    
    def get_lazy_blueprints(self) -> Optional[List[LazyBlueprint]]:
        """Return the lazy blueprints created during build execution.
        
        Args:
            None
            
        Returns:
            Optional[List[LazyBlueprint]]: List of lazy blueprints or None if not executed
        """
        return self.lazy_blueprints
    
    def execute(
        self,
        toolbox: ToolBox,
        blueprint_rack: BlueprintRack,
        concurrent_executables: Optional[List[Any]] = None,
        correlation_id: Optional[str] = None,
        asyncio_event_loop: Optional[asyncio.AbstractEventLoop] = None,
        thread_pool_executor: Optional[ThreadPoolExecutor] = None,
        process_pool_executor: Optional[ProcessPoolExecutor] = None,
    ) -> None:
        """Execute the build plan using provided resources and store results in instance variables.
        
        Args:
            toolbox (ToolBox): Collection of available tools for execution
            blueprint_rack (BlueprintRack): Collection of available blueprints
            concurrent_executables (Optional[List[Any]]): Optional list of concurrent executables
            correlation_id (Optional[str]): Optional correlation identifier
            asyncio_event_loop (Optional[asyncio.AbstractEventLoop]): Optional asyncio event loop
            thread_pool_executor (Optional[ThreadPoolExecutor]): Optional thread pool executor
            process_pool_executor (Optional[ProcessPoolExecutor]): Optional process pool executor
            
        Returns:
            None: Results are stored in instance variables filled_blueprints, lazy_blueprints, and stage_outputs
        """
        self._initialize_execution_state()
        self._collect_concurrent_results(concurrent_executables)
        stage_outputs = self._execute_all_stages(
            toolbox, concurrent_executables, correlation_id, 
            asyncio_event_loop, thread_pool_executor, process_pool_executor
        )
        lazy_blueprints = self._create_lazy_blueprints(blueprint_rack, stage_outputs)
        self._finalize_execution(lazy_blueprints, stage_outputs)
    
    def _initialize_execution_state(self) -> None:
        """Initialize execution state by clearing previous results.
        
        Args:
            None
            
        Returns:
            None: Clears filled_blueprints, lazy_blueprints, and stage_outputs instance variables
        """
        self.filled_blueprints = None
        self.lazy_blueprints = None
        self.stage_outputs = None

    def _collect_concurrent_results(self, concurrent_executables: Optional[List[Any]]) -> Dict[str, Any]:
        """Collect results from concurrent executables if available.
        
        Args:
            concurrent_executables (Optional[List[Any]]): Optional list of concurrent executables to collect results from
            
        Returns:
            Dict[str, Any]: Dictionary mapping executable names to their results
        """
        concurrent_results: Dict[str, Any] = {}
        if concurrent_executables:
            for executable in concurrent_executables:
                try:
                    if hasattr(executable, "is_current_running") and executable.is_current_running:
                        concurrent_results[executable.name] = executable.fetch_results()
                except Exception as execution_error:
                    log_with_structure(
                        logger,
                        "error",
                        "Failed to get concurrent executable result",
                        build_correlation_id=self.build_correlation_id,
                        executable_name=getattr(executable, "name", None),
                        exception_type=type(execution_error).__name__,
                        exception_message=str(execution_error),
                        error=execution_error,
                    )
        return concurrent_results

    def _execute_all_stages(
        self,
        toolbox: ToolBox,
        concurrent_executables: Optional[List[Any]],
        correlation_id: Optional[str],
        asyncio_event_loop: Optional[asyncio.AbstractEventLoop],
        thread_pool_executor: Optional[ThreadPoolExecutor],
        process_pool_executor: Optional[ProcessPoolExecutor],
    ) -> Dict[str, Dict[str, Any]]:
        """Execute all stages in sorted order and return their outputs.
        
        Args:
            toolbox (ToolBox): Collection of available tools
            concurrent_executables (Optional[List[Any]]): Optional concurrent executables
            correlation_id (Optional[str]): Optional correlation identifier
            asyncio_event_loop (Optional[asyncio.AbstractEventLoop]): Optional asyncio event loop
            thread_pool_executor (Optional[ThreadPoolExecutor]): Optional thread pool executor
            process_pool_executor (Optional[ProcessPoolExecutor]): Optional process pool executor
            
        Returns:
            Dict[str, Dict[str, Any]]: Dictionary mapping stage names to their tool outputs
        """
        stages = self.get_stages()
        stage_outputs: Dict[str, Dict[str, Any]] = {}
        for stage_name in sorted(stages.keys()):
            stage_config = stages[stage_name]
            stage_results = self._execute_stage(
                stage_name,
                stage_config,
                stage_outputs,
                concurrent_executables,
                toolbox,
                correlation_id,
                asyncio_event_loop,
                thread_pool_executor,
                process_pool_executor,
            )
            stage_outputs[stage_name] = stage_results
        return stage_outputs

    def _create_lazy_blueprints(
        self, blueprint_rack: BlueprintRack, stage_outputs: Dict[str, Dict[str, Any]]
    ) -> List[LazyBlueprint]:
        """Create lazy blueprints from blueprint configurations in the build plan.
        
        Args:
            blueprint_rack (BlueprintRack): Collection of available blueprints
            stage_outputs (Dict[str, Dict[str, Any]]): Results from executed stages
            
        Returns:
            List[LazyBlueprint]: List of created lazy blueprints
        """
        blueprint_configs = self.get_blueprints()
        lazy_blueprints: List[LazyBlueprint] = []
        for blueprint_name, blueprint_params in blueprint_configs.items():
            blueprint = self._find_blueprint_with_fallback(blueprint_rack, blueprint_name)
            if blueprint:
                lazy_blueprint = self._create_single_lazy_blueprint(
                    blueprint, blueprint_name, blueprint_params, stage_outputs
                )
                if lazy_blueprint:
                    lazy_blueprints.append(lazy_blueprint)
            else:
                self._log_blueprint_not_found(blueprint_name)
        return lazy_blueprints

    def _find_blueprint_with_fallback(self, blueprint_rack: BlueprintRack, blueprint_name: str):
        """Find blueprint by name with fallback to parsed name.
        
        Args:
            blueprint_rack (BlueprintRack): Collection of available blueprints
            blueprint_name (str): Name of blueprint to find
            
        Returns:
            Blueprint or None: Found blueprint instance or None if not found
        """
        blueprint = blueprint_rack.find_by_name(blueprint_name)
        if not blueprint:
            parsed_blueprint_name = self._parse_name_with_suffix(blueprint_name)
            if parsed_blueprint_name:
                log_with_structure(
                    logger,
                    "debug",
                    "Attempting to find blueprint with parsed name",
                    build_correlation_id=self.build_correlation_id,
                    original_blueprint_name=blueprint_name,
                    parsed_blueprint_name=parsed_blueprint_name
                )
                blueprint = blueprint_rack.find_by_name(parsed_blueprint_name)
                if blueprint:
                    log_with_structure(
                        logger,
                        "debug",
                        "Successfully found blueprint using parsed name",
                        build_correlation_id=self.build_correlation_id,
                        original_blueprint_name=blueprint_name,
                        parsed_blueprint_name=parsed_blueprint_name
                    )
        return blueprint

    def _create_single_lazy_blueprint(
        self, blueprint, blueprint_name: str, blueprint_params, stage_outputs: Dict[str, Dict[str, Any]]
    ) -> Optional[LazyBlueprint]:
        """Create a single lazy blueprint with error handling.
        
        Args:
            blueprint: Blueprint instance to wrap
            blueprint_name (str): Name of the blueprint
            blueprint_params: Parameters for the blueprint
            stage_outputs (Dict[str, Dict[str, Any]]): Stage execution results
            
        Returns:
            Optional[LazyBlueprint]: Created lazy blueprint or None if creation failed
        """
        try:
            lazy_blueprint = LazyBlueprint(
                blueprint=blueprint,
                raw_parameters=blueprint_params,
                stage_outputs=stage_outputs,
                build_instance=self,
                instance_key=blueprint_name
            )
            log_with_structure(
                logger,
                "debug",
                "Created lazy blueprint",
                build_correlation_id=self.build_correlation_id,
                blueprint_name=blueprint_name,
                dependency_count=len(lazy_blueprint._dependencies),
            )
            return lazy_blueprint
        except Exception as blueprint_error:
            log_with_structure(
                logger,
                "error",
                "Failed to create lazy blueprint",
                build_correlation_id=self.build_correlation_id,
                blueprint_name=blueprint_name,
                error=str(blueprint_error),
            )
            return None

    def _log_blueprint_not_found(self, blueprint_name: str) -> None:
        """Log warning when blueprint is not found.
        
        Args:
            blueprint_name (str): Name of the blueprint that was not found
            
        Returns:
            None: Logs warning message
        """
        log_with_structure(
            logger,
            "warning",
            "Blueprint not found",
            build_correlation_id=self.build_correlation_id,
            blueprint_name=blueprint_name,
        )

    def _finalize_execution(
        self, lazy_blueprints: List[LazyBlueprint], stage_outputs: Dict[str, Dict[str, Any]]
    ) -> None:
        """Finalize execution by setting results and resolving remaining executables.
        
        Args:
            lazy_blueprints (List[LazyBlueprint]): Created lazy blueprints
            stage_outputs (Dict[str, Dict[str, Any]]): Stage execution results
            
        Returns:
            None: Sets instance variables and finalizes stage outputs
        """
        self.lazy_blueprints = lazy_blueprints
        self.filled_blueprints = []
        self.stage_outputs = stage_outputs
        self._finalize_stage_outputs()

    def _finalize_stage_outputs(self):
        """Ensure all ConcurrentExecutables in stage_outputs are resolved to their results.
        
        Args:
            None
            
        Returns:
            None: Resolves ConcurrentExecutables in stage_outputs to their actual results
        """
        if self.stage_outputs is None:
            return
        for stage_name, stage_data in self.stage_outputs.items():
            for tool_name, tool_result in stage_data.items():
                if hasattr(tool_result, 'fetch_results') and hasattr(tool_result, 'is_current_running'):
                    resolved_result = self._fetch_executable_result(tool_result, tool_name, stage_name)
                    self.stage_outputs[stage_name][tool_name] = resolved_result
                    log_with_structure(
                        logger,
                        "debug",
                        "ConcurrentExecutable finalized in stage_outputs",
                        build_correlation_id=self.build_correlation_id,
                        stage_name=stage_name,
                        tool_name=tool_name,
                    )

    def run(
        self,
        toolbox: ToolBox,
        blueprint_rack: BlueprintRack,
        concurrent_executables: Optional[List[Any]] = None,
        correlation_id: Optional[str] = None,
        asyncio_event_loop: Optional[asyncio.AbstractEventLoop] = None,
        thread_pool_executor: Optional[ThreadPoolExecutor] = None,
        process_pool_executor: Optional[ProcessPoolExecutor] = None,
    ) -> None:
        """Execute the build plan - maintained for compatibility with architect.py.
        
        Args:
            toolbox (ToolBox): Collection of available tools for execution
            blueprint_rack (BlueprintRack): Collection of available blueprints
            concurrent_executables (Optional[List[Any]]): Optional list of concurrent executables
            correlation_id (Optional[str]): Optional correlation identifier
            asyncio_event_loop (Optional[asyncio.AbstractEventLoop]): Optional asyncio event loop
            thread_pool_executor (Optional[ThreadPoolExecutor]): Optional thread pool executor
            process_pool_executor (Optional[ProcessPoolExecutor]): Optional process pool executor
            
        Returns:
            None: Executes build plan and stores results in instance variables
        """
        self.filled_blueprints = None
        self.lazy_blueprints = None
        self.stage_outputs = None
        self.execute(
            toolbox, 
            blueprint_rack, 
            concurrent_executables, 
            correlation_id,
            asyncio_event_loop,
            thread_pool_executor,
            process_pool_executor
        )

    def _execute_stage(
        self,
        stage_name: str,
        stage_config: Dict[str, Any],
        stage_outputs: Dict[str, Dict[str, Any]],
        concurrent_executables: Optional[List[Any]],
        toolbox: ToolBox,
        correlation_id: Optional[str],
        asyncio_event_loop: Optional[asyncio.AbstractEventLoop] = None,
        thread_pool_executor: Optional[ThreadPoolExecutor] = None,
        process_pool_executor: Optional[ProcessPoolExecutor] = None,
    ) -> Dict[str, Any]:
        """Execute all tools in a stage in parallel using ConcurrentExecutables.
        
        Args:
            stage_name (str): Name of the stage to execute
            stage_config (Dict[str, Any]): Configuration for the stage
            stage_outputs (Dict[str, Dict[str, Any]]): Outputs from previously executed stages
            concurrent_executables (Optional[List[Any]]): Optional concurrent executables
            toolbox (ToolBox): Collection of available tools
            correlation_id (Optional[str]): Optional correlation identifier
            asyncio_event_loop (Optional[asyncio.AbstractEventLoop]): Optional asyncio event loop
            thread_pool_executor (Optional[ThreadPoolExecutor]): Optional thread pool executor
            process_pool_executor (Optional[ProcessPoolExecutor]): Optional process pool executor
            
        Returns:
            Dict[str, Any]: Dictionary mapping tool names to their ConcurrentExecutable instances
        """
        stage_executables, tool_names = self._create_stage_executables(
            stage_name, stage_config, stage_outputs, concurrent_executables,
            toolbox, asyncio_event_loop, thread_pool_executor, process_pool_executor
        )
        self._start_all_executables(stage_name, stage_executables)
        return self._prepare_stage_results(stage_name, stage_executables, tool_names)
    
    def _create_stage_executables(
        self,
        stage_name: str,
        stage_config: Dict[str, Any],
        stage_outputs: Dict[str, Dict[str, Any]],
        concurrent_executables: Optional[List[Any]],
        toolbox: ToolBox,
        asyncio_event_loop: Optional[asyncio.AbstractEventLoop],
        thread_pool_executor: Optional[ThreadPoolExecutor],
        process_pool_executor: Optional[ProcessPoolExecutor],
    ):
        """Create ConcurrentExecutables for all tools in a stage.
        
        Args:
            stage_name (str): Name of the stage
            stage_config (Dict[str, Any]): Stage configuration
            stage_outputs (Dict[str, Dict[str, Any]]): Previous stage outputs
            concurrent_executables (Optional[List[Any]]): Optional concurrent executables
            toolbox (ToolBox): Available tools
            asyncio_event_loop (Optional[asyncio.AbstractEventLoop]): Optional event loop
            thread_pool_executor (Optional[ThreadPoolExecutor]): Optional thread executor
            process_pool_executor (Optional[ProcessPoolExecutor]): Optional process executor
            
        Returns:
            Tuple: (stage_executables, tool_names) - lists of executables and their names
        """
        stage_executables: List[ConcurrentExecutable] = []
        tool_names: List[str] = []
        for tool_name, tool_params in stage_config.items():
            tool = self._find_tool_with_fallback(toolbox, tool_name, stage_name)
            resolved_params = self._resolve_references(tool_params, stage_outputs)
            executable = self._create_single_executable(
                tool, tool_name, resolved_params, concurrent_executables,
                asyncio_event_loop, thread_pool_executor, process_pool_executor, stage_name
            )
            stage_executables.append(executable)
            tool_names.append(tool_name)
        return stage_executables, tool_names

    def _find_tool_with_fallback(self, toolbox: ToolBox, tool_name: str, stage_name: str):
        """Find tool by name with fallback to parsed name.
        
        Args:
            toolbox (ToolBox): Collection of available tools
            tool_name (str): Name of tool to find
            stage_name (str): Name of current stage (for error reporting)
            
        Returns:
            Tool: Found tool instance
        """
        tool = toolbox.find_by_name(tool_name)
        if not tool:
            parsed_tool_name = self._parse_name_with_suffix(tool_name)
            if parsed_tool_name:
                log_with_structure(
                    logger,
                    "debug", 
                    "Attempting to find tool with parsed name",
                    build_correlation_id=self.build_correlation_id,
                    original_tool_name=tool_name,
                    parsed_tool_name=parsed_tool_name,
                    stage_name=stage_name
                )
                tool = toolbox.find_by_name(parsed_tool_name)
                if tool:
                    log_with_structure(
                        logger,
                        "debug",
                        "Successfully found tool using parsed name", 
                        build_correlation_id=self.build_correlation_id,
                        original_tool_name=tool_name,
                        parsed_tool_name=parsed_tool_name,
                        stage_name=stage_name
                    )
            if not tool:
                raise ToolNotFoundError(tool_name, stage_name, available_tools=list(toolbox.tools.keys()))
        return tool

    def _create_single_executable(
        self, tool, tool_name: str, resolved_params, concurrent_executables: Optional[List[Any]],
        asyncio_event_loop: Optional[asyncio.AbstractEventLoop],
        thread_pool_executor: Optional[ThreadPoolExecutor],
        process_pool_executor: Optional[ProcessPoolExecutor],
        stage_name: str
    ) -> ConcurrentExecutable:
        """Create a single ConcurrentExecutable from a tool with error handling.
        
        Args:
            tool: Tool instance to wrap
            tool_name (str): Name of the tool
            resolved_params: Resolved parameters for the tool
            concurrent_executables (Optional[List[Any]]): Optional concurrent executables
            asyncio_event_loop (Optional[asyncio.AbstractEventLoop]): Optional event loop
            thread_pool_executor (Optional[ThreadPoolExecutor]): Optional thread executor
            process_pool_executor (Optional[ProcessPoolExecutor]): Optional process executor
            stage_name (str): Name of current stage
            
        Returns:
            ConcurrentExecutable: Created executable instance
        """
        try:
            executable = ConcurrentExecutable.from_tool(
                tool=tool,
                parameters=resolved_params,
                initial_concurrent_executables=concurrent_executables,
                asyncio_event_loop=asyncio_event_loop,
                thread_pool_executor=thread_pool_executor,
                process_pool_executor=process_pool_executor,
            )
            log_with_structure(
                logger,
                "debug",
                "Created ConcurrentExecutable for tool",
                build_correlation_id=self.build_correlation_id,
                stage_name=stage_name,
                tool_name=tool_name,
                execution_mode=tool.execution_mode.value,
            )
            return executable
        except Exception as creation_error:
            log_with_structure(
                logger,
                "error",
                "Failed to create ConcurrentExecutable",
                build_correlation_id=self.build_correlation_id,
                stage_name=stage_name,
                tool_name=tool_name,
                error=str(creation_error),
            )
            raise

    def _start_all_executables(self, stage_name: str, stage_executables: List[ConcurrentExecutable]) -> None:
        """Start all ConcurrentExecutables in the stage.
        
        Args:
            stage_name (str): Name of the stage
            stage_executables (List[ConcurrentExecutable]): List of executables to start
            
        Returns:
            None: Starts all executables and logs results
        """
        for executable in stage_executables:
            try:
                executable.start()
                log_with_structure(
                    logger,
                    "debug",
                    "Started ConcurrentExecutable",
                    build_correlation_id=self.build_correlation_id,
                    stage_name=stage_name,
                    tool_name=executable.name,
                )
            except Exception as start_error:
                log_with_structure(
                    logger,
                    "error",
                    "Failed to start ConcurrentExecutable",
                    build_correlation_id=self.build_correlation_id,
                    stage_name=stage_name,
                    tool_name=executable.name,
                    error=str(start_error),
                )
    def _prepare_stage_results(
        self, stage_name: str, stage_executables: List[ConcurrentExecutable], tool_names: List[str]
    ) -> Dict[str, Any]:
        """Prepare stage results from running ConcurrentExecutables.
        
        Args:
            stage_name (str): Name of the stage
            stage_executables (List[ConcurrentExecutable]): List of started executables
            tool_names (List[str]): List of tool names corresponding to executables
            
        Returns:
            Dict[str, Any]: Dictionary mapping tool names to their executable instances
        """
        results: Dict[str, Any] = {}
        for executable, tool_name in zip(stage_executables, tool_names):
            results[tool_name] = executable
            log_with_structure(
                logger,
                "debug",
                "ConcurrentExecutable started and ready for lazy evaluation",
                build_correlation_id=self.build_correlation_id,
                stage_name=stage_name,
                tool_name=tool_name,
            )
        return results
    def _fetch_executable_result(self, executable: Any, tool_name: str, stage_name: str) -> Any:
        """Safely fetch results from a ConcurrentExecutable with error handling.
        
        Args:
            executable (Any): ConcurrentExecutable instance to fetch results from
            tool_name (str): Name of the tool for logging
            stage_name (str): Name of the stage for logging
            
        Returns:
            Any: Result from executable or error dictionary if failed
        """
        try:
            executable_result = executable.fetch_results()
            log_with_structure(
                logger,
                "debug",
                "ConcurrentExecutable result fetched on-demand",
                build_correlation_id=self.build_correlation_id,
                stage_name=stage_name,
                tool_name=tool_name,
            )
            return executable_result
        except Exception as fetch_error:
            log_with_structure(
                logger,
                "error",
                "ConcurrentExecutable failed when fetching results on-demand",
                build_correlation_id=self.build_correlation_id,
                stage_name=stage_name,
                tool_name=tool_name,
                exception_type=type(fetch_error).__name__,
                exception_message=str(fetch_error),
                error=fetch_error,
            )
            logger.error(f"Full ConcurrentExecutable failure traceback for {tool_name}:", exc_info=True)
            return {"error": str(fetch_error)}
    
    def _resolve_references(
        self,
        data: Any,
        stage_outputs: Dict[str, Dict[str, Any]],
        current_stage_num: Optional[int] = None,
    ) -> Any:
        """Resolve $ref references in data structures using stage_outputs, with optional stage validation.
        
        Args:
            data (Any): Data structure potentially containing $ref references
            stage_outputs (Dict[str, Dict[str, Any]]): Outputs from executed stages
            current_stage_num (Optional[int]): Current stage number for validation
            
        Returns:
            Any: Data structure with resolved references
        """
        if isinstance(data, str):
            return self._resolve_string_references(data, stage_outputs, current_stage_num)
        if isinstance(data, dict):
            return {dict_key: self._resolve_references(dict_value, stage_outputs, current_stage_num) for dict_key, dict_value in data.items()}
        if isinstance(data, list):
            return [self._resolve_references(list_item, stage_outputs, current_stage_num) for list_item in data]
        return data
    
    def _resolve_string_references(
        self, data: str, stage_outputs: Dict[str, Dict[str, Any]], current_stage_num: Optional[int]
    ) -> Any:
        """Handle reference resolution for string data types.
        
        Args:
            data (str): String potentially containing references
            stage_outputs (Dict[str, Dict[str, Any]]): Stage execution results
            current_stage_num (Optional[int]): Current stage number for validation
            
        Returns:
            Any: Resolved value (may be string or other type)
        """
        if data.startswith("$ref.") and " " not in data:
            return self._resolve_single_reference(data, stage_outputs, current_stage_num)
        if "$ref." in data:
            return self._resolve_embedded_references(data, stage_outputs, current_stage_num)
        return data
    def _resolve_single_reference(
        self, reference: str, stage_outputs: Dict[str, Dict[str, Any]], current_stage_num: Optional[int]
    ) -> Any:
        """Resolve a single $ref reference.
        
        Args:
            reference (str): Reference string to resolve
            stage_outputs (Dict[str, Dict[str, Any]]): Stage execution results
            current_stage_num (Optional[int]): Current stage number for validation
            
        Returns:
            Any: Resolved value from the referenced location
        """
        reference_parts = reference.split(".")
        if len(reference_parts) < 4:
            raise InvalidReferencePathError(f"Invalid reference path format: {reference}")
        stage_key = reference_parts[1]
        if not stage_key.startswith("stage_"):
            raise InvalidReferencePathError(f"Invalid stage token in reference: {reference}")
        try:
            reference_stage_number = int(stage_key.split("_")[1])
        except Exception:
            raise InvalidReferencePathError(f"Invalid stage number in reference: {reference}")
        if current_stage_num is not None:
            if reference_stage_number > current_stage_num:
                raise StageValidationError(reference, current_stage_num, reference_stage_number)
            if reference_stage_number == current_stage_num:
                raise StageValidationError(reference, current_stage_num, current_stage_num)
        tool_name = reference_parts[2]
        output_param = ".".join(reference_parts[3:])
        if stage_key not in stage_outputs or tool_name not in stage_outputs[stage_key]:
            raise ReferenceResolutionError(reference, "missing stage or tool")
        stage_result = stage_outputs[stage_key][tool_name]
        if hasattr(stage_result, 'fetch_results') and hasattr(stage_result, 'is_current_running'):
            # If we're in async context and the executable is ASYNCIO or a future, await it; else block here
            try:
                current_loop = asyncio.get_running_loop()
            except RuntimeError:
                current_loop = None
            if current_loop is not None and getattr(stage_result, 'execution_mode', None) == ExecutionMode.ASYNCIO:
                # We are in event loop; use async fetch via temporary task run
                async def _await_exec():
                    return await stage_result.fetch_results_async()
                stage_result = current_loop.run_until_complete(_await_exec())
            else:
                stage_result = self._fetch_executable_result(stage_result, tool_name, stage_key)
            stage_outputs[stage_key][tool_name] = stage_result
        return self._navigate_output_parameter(stage_result, output_param, reference)
    def _navigate_output_parameter(self, stage_result: Any, output_param: str, reference: str) -> Any:
        """Navigate nested object access with support for list indexing.
        
        Args:
            stage_result (Any): Result object to navigate
            output_param (str): Parameter path to navigate
            reference (str): Original reference for error reporting
            
        Returns:
            Any: Value at the specified parameter path
        """
        current_result = stage_result
        param_parts = output_param.split(".")
        for param_index, param_part in enumerate(param_parts):
            if '[' in param_part and param_part.endswith(']'):
                current_result = self._handle_bracket_notation(
                    current_result, param_part, param_parts, param_index, reference
                )
            else:
                if not isinstance(current_result, dict) or param_part not in current_result:
                    partial_path = ".".join(param_parts[:param_index+1])
                    raise ReferenceResolutionError(reference, f"output parameter '{partial_path}' not found")
                current_result = current_result[param_part]
        return current_result
    def _handle_bracket_notation(
        self, current_result: Any, param_part: str, param_parts: List[str], param_index: int, reference: str
    ) -> Any:
        """Handle bracket notation for list indexing in parameter navigation.
        
        Args:
            current_result (Any): Current navigation result
            param_part (str): Parameter part with bracket notation
            param_parts (List[str]): Full list of parameter parts
            param_index (int): Index of current parameter part
            reference (str): Original reference for error reporting
            
        Returns:
            Any: Result after applying bracket notation indexing
        """
        current_part = param_part
        first_bracket = current_part.find('[')
        base_name = current_part[:first_bracket] if first_bracket > 0 else ""
        if base_name:
            if not isinstance(current_result, dict) or base_name not in current_result:
                partial_path = ".".join(param_parts[:param_index]) + ("." if param_index > 0 else "") + base_name
                raise ReferenceResolutionError(reference, f"output parameter '{partial_path}' not found")
            current_result = current_result[base_name]
        bracket_part = current_part[first_bracket:] if first_bracket >= 0 else current_part
        while '[' in bracket_part and bracket_part.endswith(']'):
            start_index = bracket_part.find('[')
            end_index = bracket_part.find(']', start_index)
            if start_index == -1 or end_index == -1:
                break
            index_content = bracket_part[start_index+1:end_index]
            try:
                list_index = int(index_content)
                if not isinstance(current_result, (list, tuple)):
                    partial_path = ".".join(param_parts[:param_index+1])
                    raise ReferenceResolutionError(reference, f"output parameter '{partial_path}' is not subscriptable")
                current_result = current_result[list_index]
            except ValueError:
                partial_path = ".".join(param_parts[:param_index+1])
                raise ReferenceResolutionError(reference, f"invalid index '{index_content}' in '{partial_path}'")
            except IndexError:
                partial_path = ".".join(param_parts[:param_index+1])
                raise ReferenceResolutionError(reference, f"list index out of range in '{partial_path}'")
            bracket_part = bracket_part[end_index+1:]
            if not bracket_part:
                break
        return current_result
    def _resolve_embedded_references(
        self, data: str, stage_outputs: Dict[str, Dict[str, Any]], current_stage_num: Optional[int]
    ) -> str:
        """Handle embedded references within text strings.
        
        Args:
            data (str): String with embedded references
            stage_outputs (Dict[str, Dict[str, Any]]): Stage execution results
            current_stage_num (Optional[int]): Current stage number for validation
            
        Returns:
            str: String with all references resolved to their values
        """
        log_with_structure(
            logger,
            "debug",
            "Processing string with embedded references",
            build_correlation_id=self.build_correlation_id,
            original_text=data
        )
        reference_pattern = r'\$ref\.(stage_\d+)\.([a-zA-Z0-9_]+(?:\[-?\d+\])*(?:\.[a-zA-Z0-9_]+(?:\[-?\d+\])*)*)\.([a-zA-Z0-9_]+(?:\[-?\d+\])*(?:\.[a-zA-Z0-9_]+(?:\[-?\d+\])*)*)'
        def replace_reference_match(pattern_match):
            full_reference = f"$ref.{pattern_match.group(1)}.{pattern_match.group(2)}.{pattern_match.group(3)}"
            try:
                resolved_value = self._resolve_single_reference(full_reference, stage_outputs, current_stage_num)
                log_with_structure(
                    logger,
                    "debug",
                    "Successfully resolved embedded reference",
                    build_correlation_id=self.build_correlation_id,
                    original_text=data,
                    reference=full_reference,
                    resolved_value=str(resolved_value)
                )
                return str(resolved_value)
            except Exception as resolution_error:
                log_with_structure(
                    logger,
                    "error", 
                    "Failed to resolve embedded reference",
                    build_correlation_id=self.build_correlation_id,
                    original_text=data,
                    reference=full_reference,
                    error=str(resolution_error)
                )
                raise resolution_error
        try:
            result = re.sub(reference_pattern, replace_reference_match, data)
            log_with_structure(
                logger,
                "debug", 
                "Completed embedded reference processing",
                build_correlation_id=self.build_correlation_id,
                original_text=data,
                final_result=result
            )
            return result
        except Exception as processing_error:
            raise processing_error
    def _parse_name_with_suffix(self, name: str) -> Optional[str]:
        """Parse tool/blueprint name with _X suffix and return base name.
        
        Args:
            name (str): Tool or blueprint name potentially with numeric suffix
            
        Returns:
            Optional[str]: Base name without suffix or None if no valid suffix found
        """
        if '_' not in name:
            return None
        name_parts = name.rsplit('_', 1)
        if len(name_parts) != 2:
            return None
        base_name, suffix = name_parts
        if not suffix.isdigit():
            return None
        return base_name
    
    def __repr__(self) -> str:
        """Return string representation of Build instance.
        
        Args:
            None
            
        Returns:
            str: String representation showing correlation ID and plan length
        """
        return f"Build(correlation_id={self.build_correlation_id}, plan_length={len(self.build_plan)})"

    def stream_stage_callback(self, stage_name: str, stage_config: Dict[str, Any]) -> None:
        """
        Callback invoked when a complete stage is detected in streaming mode.
        
        Args:
            stage_name (str): Name of the detected stage
            stage_config (Dict[str, Any]): Configuration for the stage
            
        Returns:
            None: Starts execution of the detected stage
        """
        if not self.streaming_mode:
            return
        log_with_structure(
            logger,
            "info",
            f"Streaming stage detected: {stage_name}",
            build_correlation_id=self.build_correlation_id,
            stage_name=stage_name,
        )
        try:
            toolbox = self.streaming_context.get("toolbox")
            concurrent_executables = self.streaming_context.get("concurrent_executables")
            correlation_id = self.streaming_context.get("correlation_id")
            asyncio_event_loop = self.streaming_context.get("asyncio_event_loop")
            thread_pool_executor = self.streaming_context.get("thread_pool_executor")
            process_pool_executor = self.streaming_context.get("process_pool_executor")
            if toolbox:
                if not hasattr(self, "_streaming_stage_queue"):
                    self._streaming_stage_queue: List[tuple] = []
                # Defer execution to finalize to avoid blocking event loop; preserve order
                self._streaming_stage_queue.append((stage_name, stage_config))
        except Exception as stage_error:
            log_with_structure(
                logger,
                "error",
                "Failed to execute streaming stage",
                build_correlation_id=self.build_correlation_id,
                stage_name=stage_name,
                error=str(stage_error),
                error_type=type(stage_error).__name__,
            )

    # Removed _run_streaming_stage helper and prior-stage waiting; we execute stages immediately on detection

    def stream_blueprint_callback(self, blueprint_name: str, blueprint_params: Dict[str, Any]) -> None:
        """
        Callback invoked when a complete blueprint is detected in streaming mode.
        
        Args:
            blueprint_name (str): Name of the detected blueprint
            blueprint_params (Dict[str, Any]): Parameters for the blueprint
            
        Returns:
            None: Creates a lazy blueprint incrementally for the detected object
        """
        if not self.streaming_mode:
            return
        try:
            if not hasattr(self, "_streaming_lazy_blueprints"):
                self._streaming_lazy_blueprints: List[LazyBlueprint] = []
            blueprint_rack = self.streaming_context.get("blueprint_rack")
            if blueprint_rack:
                # Check without logging warnings
                blueprint = blueprint_rack.blueprints.get(blueprint_name)
                if not blueprint:
                    parsed_name = self._parse_name_with_suffix(blueprint_name)
                    blueprint = blueprint_rack.blueprints.get(parsed_name) if parsed_name else None
                if blueprint:
                    log_with_structure(
                        logger,
                        "info",
                        f"Streaming blueprint detected: {blueprint_name}",
                        build_correlation_id=self.build_correlation_id,
                        blueprint_name=blueprint_name,
                    )
                    lazy_blueprint = LazyBlueprint(
                        blueprint=blueprint,
                        raw_parameters=blueprint_params,
                        stage_outputs=self.streaming_stage_outputs,
                        build_instance=self,
                        instance_key=blueprint_name
                    )
                    self._streaming_lazy_blueprints.append(lazy_blueprint)
                else:
                    log_with_structure(
                        logger,
                        "debug",
                        "Ignoring non-blueprint top-level object during streaming",
                        build_correlation_id=self.build_correlation_id,
                        blueprint_name=blueprint_name,
                    )
        except Exception as blueprint_error:
            log_with_structure(
                logger,
                "error",
                "Failed to process streaming blueprint",
                build_correlation_id=self.build_correlation_id,
                blueprint_name=blueprint_name,
                error=str(blueprint_error),
            )

    def finalize_streaming_execution(self) -> None:
        """
        Finalize streaming execution by creating blueprints and setting final results.
        
        Args:
            None
            
        Returns:
            None: Sets stage_outputs and creates lazy blueprints
        """
        if not self.streaming_mode:
            return
        # Execute any deferred streaming stages now, in order, on the current thread
        if hasattr(self, "_streaming_stage_queue") and self._streaming_stage_queue:
            toolbox: ToolBox = self.streaming_context.get("toolbox")
            concurrent_executables = self.streaming_context.get("concurrent_executables")
            correlation_id = self.streaming_context.get("correlation_id")
            asyncio_event_loop = self.streaming_context.get("asyncio_event_loop")
            thread_pool_executor = self.streaming_context.get("thread_pool_executor")
            process_pool_executor = self.streaming_context.get("process_pool_executor")
            for stage_name, stage_config in self._streaming_stage_queue:
                stage_results = self._execute_stage(
                    stage_name,
                    stage_config,
                    self.streaming_stage_outputs,
                    concurrent_executables,
                    toolbox,
                    correlation_id,
                    asyncio_event_loop,
                    thread_pool_executor,
                    process_pool_executor,
                )
                self.streaming_stage_outputs[stage_name] = stage_results
            self._streaming_stage_queue.clear()
        self.stage_outputs = self.streaming_stage_outputs
        blueprint_rack = self.streaming_context.get("blueprint_rack")
        if blueprint_rack:
            if hasattr(self, "_streaming_lazy_blueprints") and self._streaming_lazy_blueprints:
                self._finalize_execution(self._streaming_lazy_blueprints, self.stage_outputs)
            else:
                # In streaming mode, avoid parsing the full plan at finalize time.
                # If no streamed blueprints were detected, finalize with an empty list.
                self._finalize_execution([], self.stage_outputs)


class BuildPlanParsingError(Exception):
    """Raised when build plan JSON cannot be parsed.
    
    Args:
        Exception: Standard exception base class
        
    Returns:
        None: Exception class for build plan parsing errors
    """
    pass
