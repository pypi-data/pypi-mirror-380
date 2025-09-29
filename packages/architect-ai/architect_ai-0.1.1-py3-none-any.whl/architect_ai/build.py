"""Build plan representation and execution logic."""

import json
import logging
import asyncio
import re
from typing import Dict, Any, Optional, Tuple, List
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

from .logging_utils import log_structured as log_with_structure
from .toolbox import ToolBox
from .blueprint_rack import BlueprintRack
from .execution_mode import ExecutionMode
from .concurrent_executable import ConcurrentExecutable
from .exceptions.architect_exceptions import (
    ToolNotFoundError,
    ReferenceResolutionError,
    InvalidReferencePathError,
    StageValidationError,
)

logger = logging.getLogger(__name__)


class Build:
    """Represents a build plan with execution capabilities."""
    
    def __init__(self, build_plan: str, build_correlation_id: str):
        """Initialize build with plan and correlation ID."""
        self.build_plan = build_plan
        self.build_correlation_id = build_correlation_id
        self._parsed_plan: Optional[Dict[str, Any]] = None
        self.filled_blueprints: Optional[List[Any]] = None
        self.stage_outputs: Optional[Dict[str, Dict[str, Any]]] = None
    
    def get_parsed_plan(self) -> Dict[str, Any]:
        """Get the parsed JSON build plan."""
        if self._parsed_plan is None:
            try:
                self._parsed_plan = json.loads(self.build_plan)
            except json.JSONDecodeError as e:
                log_with_structure(
                    logger,
                    "error",
                    "Failed to parse build plan JSON",
                    build_correlation_id=self.build_correlation_id,
                    error=str(e),
                    build_plan_preview=self.build_plan[:500],
                )
                raise BuildPlanParsingError(f"Invalid JSON in build plan: {e}") from e
        
        return self._parsed_plan
    
    def get_stages(self) -> Dict[str, Dict[str, Any]]:
        """Get all stages from the build plan."""
        parsed = self.get_parsed_plan()
        stages = {}
        for key, value in parsed.items():
            if key.startswith("stage_"):
                stages[key] = value
        return stages
    
    def get_blueprints(self) -> Dict[str, Dict[str, Any]]:
        """Get all blueprint configurations from the build plan."""
        parsed = self.get_parsed_plan()
        blueprints = {}
        for key, value in parsed.items():
            if not key.startswith("stage_"):
                blueprints[key] = value
        return blueprints
    
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
        """Execute the build plan using the provided toolbox and blueprint rack.
        
        Results are stored in self.filled_blueprints and self.stage_outputs.
        """
        self.filled_blueprints = None
        self.stage_outputs = None
        # Collect results from concurrent executables (if any)
        concurrent_results: Dict[str, Any] = {}
        if concurrent_executables:
            for exe in concurrent_executables:
                try:
                    if hasattr(exe, "is_current_running") and exe.is_current_running:
                        concurrent_results[exe.name] = exe.fetch_results()
                except Exception as e:
                    log_with_structure(
                        logger,
                        "error",
                        "Failed to get concurrent executable result",
                        build_correlation_id=self.build_correlation_id,
                        executable_name=getattr(exe, "name", None),
                        exception_type=type(e).__name__,
                        exception_message=str(e),
                        error=e,
                    )
        
        stages = self.get_stages()
        stage_outputs: Dict[str, Dict[str, Any]] = {}
        
        # Execute stages in order
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
        
        # Fill blueprints from plan
        blueprint_configs = self.get_blueprints()
        filled_blueprints: List[Any] = []
        for blueprint_name, blueprint_params in blueprint_configs.items():
            blueprint = blueprint_rack.find_by_name(blueprint_name)
            if not blueprint:
                # Try parsing blueprint name with _X suffix (e.g., result_blueprint_2 -> result_blueprint)
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
            
            if blueprint:
                resolved_params = self._resolve_references(blueprint_params, stage_outputs)
                try:
                    blueprint.fill(resolved_params)
                    filled_blueprints.append(blueprint)
                except Exception as e:
                    log_with_structure(
                        logger,
                        "error",
                        "Failed to fill blueprint",
                        build_correlation_id=self.build_correlation_id,
                        blueprint_name=blueprint_name,
                        error=str(e),
                    )
            else:
                log_with_structure(
                    logger,
                    "warning",
                    "Blueprint not found",
                    build_correlation_id=self.build_correlation_id,
                    blueprint_name=blueprint_name,
                )
        
        self.filled_blueprints = filled_blueprints
        self.stage_outputs = stage_outputs
    
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
        """Execute the build plan - maintained for compatibility with architect.py."""
        self.filled_blueprints = None
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
        """Execute all tools in a stage in parallel using ConcurrentExecutables."""
        stage_executables: List[ConcurrentExecutable] = []
        tool_names: List[str] = []
        
        # Create ConcurrentExecutables for each tool in the stage
        for tool_name, tool_params in stage_config.items():
            tool = toolbox.find_by_name(tool_name)
            if not tool:
                # Try parsing tool name with _X suffix (e.g., addition_tool_2 -> addition_tool)
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
                    # Raise to match test expectations
                    raise ToolNotFoundError(tool_name, stage_name, available_tools=list(toolbox.tools.keys()))
            
            resolved_params = self._resolve_references(tool_params, stage_outputs)
            
            try:
                # Create ConcurrentExecutable from tool
                executable = ConcurrentExecutable.from_tool(
                    tool=tool,
                    parameters=resolved_params,
                    initial_concurrent_executables=concurrent_executables,
                    asyncio_event_loop=asyncio_event_loop,
                    thread_pool_executor=thread_pool_executor,
                    process_pool_executor=process_pool_executor,
                )
                stage_executables.append(executable)
                tool_names.append(tool_name)
                
                log_with_structure(
                    logger,
                    "debug",
                    "Created ConcurrentExecutable for tool",
                    build_correlation_id=self.build_correlation_id,
                    stage_name=stage_name,
                    tool_name=tool_name,
                    execution_mode=tool.execution_mode.value,
                )
            except Exception as e:
                log_with_structure(
                    logger,
                    "error",
                    "Failed to create ConcurrentExecutable",
                    build_correlation_id=self.build_correlation_id,
                    stage_name=stage_name,
                    tool_name=tool_name,
                    error=str(e),
                )
                raise
        
        # Start all ConcurrentExecutables in the stage
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
            except Exception as e:
                log_with_structure(
                    logger,
                    "error",
                    "Failed to start ConcurrentExecutable",
                    build_correlation_id=self.build_correlation_id,
                    stage_name=stage_name,
                    tool_name=executable.name,
                    error=str(e),
                )
        
        # Wait for all ConcurrentExecutables to complete and collect results
        results: Dict[str, Any] = {}
        for executable, tool_name in zip(stage_executables, tool_names):
            try:
                result = executable.fetch_results()
                results[tool_name] = result
                log_with_structure(
                    logger,
                    "debug",
                    "ConcurrentExecutable completed successfully",
                    build_correlation_id=self.build_correlation_id,
                    stage_name=stage_name,
                    tool_name=tool_name,
                )
            except Exception as e:
                log_with_structure(
                    logger,
                    "error",
                    "ConcurrentExecutable failed to complete",
                    build_correlation_id=self.build_correlation_id,
                    stage_name=stage_name,
                    tool_name=tool_name,
                    exception_type=type(e).__name__,
                    exception_message=str(e),
                    error=e,
                )
                logger.error(f"Full ConcurrentExecutable failure traceback for {tool_name}:", exc_info=True)
                results[tool_name] = {"error": str(e)}
        
        return results
    
    def _resolve_references(
        self,
        data: Any,
        stage_outputs: Dict[str, Dict[str, Any]],
        current_stage_num: Optional[int] = None,
    ) -> Any:
        """Resolve $ref references in data structures using stage_outputs, with optional stage validation."""
        def resolve_single(ref: str):
            # Expected format: $ref.stage_X.tool.param[.sub]
            parts = ref.split(".")
            if len(parts) < 4:
                raise InvalidReferencePathError(f"Invalid reference path format: {ref}")
            stage_key = parts[1]
            if not stage_key.startswith("stage_"):
                raise InvalidReferencePathError(f"Invalid stage token in reference: {ref}")
            try:
                ref_stage_num = int(stage_key.split("_")[1])
            except Exception:
                raise InvalidReferencePathError(f"Invalid stage number in reference: {ref}")
            if current_stage_num is not None:
                if ref_stage_num > current_stage_num:
                    raise StageValidationError(ref, current_stage_num, ref_stage_num)
                if ref_stage_num == current_stage_num:
                    raise StageValidationError(ref, current_stage_num, current_stage_num)
            tool_name = parts[2]
            output_param = ".".join(parts[3:])
            if stage_key not in stage_outputs or tool_name not in stage_outputs[stage_key]:
                raise ReferenceResolutionError(ref, "missing stage or tool")
            stage_result = stage_outputs[stage_key][tool_name]
            
            # Navigate nested object access with support for list indexing
            current_result = stage_result
            param_parts = output_param.split(".")
            
            for i, param_part in enumerate(param_parts):
                # Check if this part has bracket notation for list indexing
                if '[' in param_part and param_part.endswith(']'):
                    # Handle multiple consecutive brackets (e.g., matrix[1][2])
                    current_part = param_part
                    
                    # Extract base name (everything before the first bracket)
                    first_bracket = current_part.find('[')
                    base_name = current_part[:first_bracket] if first_bracket > 0 else ""
                    
                    # Navigate to base object first if there's a base name
                    if base_name:
                        if not isinstance(current_result, dict) or base_name not in current_result:
                            partial_path = ".".join(param_parts[:i]) + ("." if i > 0 else "") + base_name
                            raise ReferenceResolutionError(ref, f"output parameter '{partial_path}' not found")
                        current_result = current_result[base_name]
                    
                    # Process all consecutive brackets
                    bracket_part = current_part[first_bracket:] if first_bracket >= 0 else current_part
                    while '[' in bracket_part and bracket_part.endswith(']'):
                        # Find the next complete bracket pair
                        start_idx = bracket_part.find('[')
                        end_idx = bracket_part.find(']', start_idx)
                        
                        if start_idx == -1 or end_idx == -1:
                            break
                            
                        # Extract the index content
                        index_content = bracket_part[start_idx+1:end_idx]
                        
                        # Parse and apply the index
                        try:
                            index = int(index_content)
                            if not isinstance(current_result, (list, tuple)):
                                partial_path = ".".join(param_parts[:i+1])
                                raise ReferenceResolutionError(ref, f"output parameter '{partial_path}' is not subscriptable")
                            current_result = current_result[index]
                        except ValueError:
                            partial_path = ".".join(param_parts[:i+1])
                            raise ReferenceResolutionError(ref, f"invalid index '{index_content}' in '{partial_path}'")
                        except IndexError:
                            partial_path = ".".join(param_parts[:i+1])
                            raise ReferenceResolutionError(ref, f"list index out of range in '{partial_path}'")
                        
                        # Move to the remaining part after this bracket
                        bracket_part = bracket_part[end_idx+1:]
                        if not bracket_part:
                            break
                        
                else:
                    # Regular dictionary access
                    if not isinstance(current_result, dict) or param_part not in current_result:
                        partial_path = ".".join(param_parts[:i+1])
                        raise ReferenceResolutionError(ref, f"output parameter '{partial_path}' not found")
                    current_result = current_result[param_part]
            
            return current_result

        if isinstance(data, str):
            if data.startswith("$ref.") and " " not in data:
                # Simple case: entire string is a single reference
                return resolve_single(data)
            if "$ref." in data:
                # Complex case: embedded references within text
                log_with_structure(
                    logger,
                    "debug",
                    "Processing string with embedded references",
                    build_correlation_id=self.build_correlation_id,
                    original_text=data
                )
                # Use regex to find and replace all $ref patterns
                # Pattern explanation:
                # \$ref\. - literal "$ref."
                # (stage_\d+) - capture group 1: stage_1, stage_2, etc.
                # \.([a-zA-Z0-9_]+(?:\[-?\d+\])*(?:\.[a-zA-Z0-9_]+(?:\[-?\d+\])*)*) - capture group 2: tool name (with multiple bracket indexing)
                # \.([a-zA-Z0-9_]+(?:\[-?\d+\])*(?:\.[a-zA-Z0-9_]+(?:\[-?\d+\])*)*) - capture group 3: output param (word chars + dots + multiple brackets for nesting, stops at punctuation)
                ref_pattern = r'\$ref\.(stage_\d+)\.([a-zA-Z0-9_]+(?:\[-?\d+\])*(?:\.[a-zA-Z0-9_]+(?:\[-?\d+\])*)*)\.([a-zA-Z0-9_]+(?:\[-?\d+\])*(?:\.[a-zA-Z0-9_]+(?:\[-?\d+\])*)*)'
                
                def replace_ref(match):
                    # Reconstruct the full reference from regex groups
                    full_ref = f"$ref.{match.group(1)}.{match.group(2)}.{match.group(3)}"
                    try:
                        resolved_value = resolve_single(full_ref)
                        log_with_structure(
                            logger,
                            "debug",
                            "Successfully resolved embedded reference",
                            build_correlation_id=self.build_correlation_id,
                            original_text=data,
                            reference=full_ref,
                            resolved_value=str(resolved_value)
                        )
                        return str(resolved_value)
                    except Exception as e:
                        log_with_structure(
                            logger,
                            "error", 
                            "Failed to resolve embedded reference",
                            build_correlation_id=self.build_correlation_id,
                            original_text=data,
                            reference=full_ref,
                            error=str(e)
                        )
                        # Re-raise with the original reference for better error messages
                        raise e
                
                # Replace all references in the string
                try:
                    result = re.sub(ref_pattern, replace_ref, data)
                    log_with_structure(
                        logger,
                        "debug", 
                        "Completed embedded reference processing",
                        build_correlation_id=self.build_correlation_id,
                        original_text=data,
                        final_result=result
                    )
                    return result
                except Exception as e:
                    raise e
            return data
        if isinstance(data, dict):
            return {k: self._resolve_references(v, stage_outputs, current_stage_num) for k, v in data.items()}
        if isinstance(data, list):
            return [self._resolve_references(v, stage_outputs, current_stage_num) for v in data]
        return data
    
    def _parse_name_with_suffix(self, name: str) -> Optional[str]:
        """
        Parse tool/blueprint name with _X suffix and return base name.
        
        Examples:
        - "addition_tool_2" -> "addition_tool"
        - "result_blueprint_1" -> "result_blueprint"
        - "my_complex_name_0" -> "my_complex_name"  
        - "tool_abc" -> None (invalid suffix)
        - "tool" -> None (no suffix)
        
        Args:
            name: Tool/blueprint name potentially with _X suffix
            
        Returns:
            Base name if valid suffix found, None otherwise
        """
        if '_' not in name:
            return None
            
        # Split on last underscore only
        parts = name.rsplit('_', 1)
        if len(parts) != 2:
            return None
            
        base_name, suffix = parts
        
        # Verify suffix is digits only (0 and positive integers)
        if not suffix.isdigit():
            return None
            
        # Return base tool name
        return base_name
    
    def __repr__(self) -> str:
        return f"Build(correlation_id={self.build_correlation_id}, plan_length={len(self.build_plan)})"


class BuildPlanParsingError(Exception):
    """Raised when build plan JSON cannot be parsed."""
    pass
