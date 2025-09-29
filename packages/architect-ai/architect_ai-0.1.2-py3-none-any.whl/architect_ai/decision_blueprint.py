#!/usr/bin/env python3
"""
DecisionBlueprint - A built-in blueprint for handling conditional logic across multiple architect calls.

This blueprint is used when the architect needs to make dynamic decisions based on tool outputs,
but cannot complete the full conditional flow in a single pass. It stores intermediate results
and descriptions that can be used by the caller to make subsequent architect calls.
"""

from typing import Dict, Tuple, Any, List
from .blueprint import Blueprint


class DecisionBlueprint(Blueprint):
    """
    A blueprint that stores intermediate results for conditional logic scenarios.
    
    This blueprint is designed for situations where the architect can perform some work
    but needs dynamic decision-making based on results. It stores intermediate results
    and descriptions that enable the caller to chain multiple architect calls together.
    
    Example usage:
    - User asks: "Multiply result of 4+5 by 2 if <8, by 4 if >8"  
    - First call: Architect adds 4+5=9, stores in DecisionBlueprint: ["The result of 4 + 5 was 9"]
    - Caller sees result, makes second call with context about the 9 and which path to take
    """
    
    def __init__(self):
        """
        Initialize the decision blueprint.
        
        Args:
            None
            
        Returns:
            None: Initializes the decision blueprint instance
        """
        self._intermediate_results: List[str] = []
        self._filled = False
    
    @property
    def name(self) -> str:
        """
        Unique identifier for this blueprint.
        
        Args:
            None
            
        Returns:
            str: The unique name of this blueprint
        """
        return "decision_blueprint"
    
    @property
    def usage_context(self) -> str:
        """
        Description of when this blueprint should be used.
        
        Args:
            None
            
        Returns:
            str: Context description for when to use this blueprint
        """
        return ("Use this blueprint when the plan needs to make dynamic decisions based on tool outputs "
                "but cannot complete the full conditional logic in a single pass. This enables chaining "
                "multiple architect calls by storing intermediate results.")
    
    @property
    def purpose(self) -> str:
        """
        Description of what this blueprint is used for.
        
        Args:
            None
            
        Returns:
            str: Purpose description of what this blueprint accomplishes
        """
        return ("Stores intermediate calculation results and descriptions for conditional logic scenarios "
                "that require multiple architect calls to complete. Acts as a handoff mechanism between "
                "architect invocations. This blueprint SHOULD NOT be used unless absolutely necessary for conditional logic scenarios.")
    
    @property
    def parameter_instructions(self) -> Dict[str, Tuple[str, str]]:
        """
        Map of parameter names to data type and description tuples.
        
        Args:
            None
            
        Returns:
            Dict[str, Tuple[str, str]]: Map of parameter names to (DataType, description) tuples
        """
        return {
            "intermediate_results": (
                "List[str]", 
                "List of string descriptions of results followed by those results. For example: ['The result of tool_1 with inputs x and y was $ref.stage_1.tool_1.output_param_1', 'The result of tool_2 with inputs a and b was $ref.stage_1.tool_2.output_param_1']"
            )
        }
    
    @property
    def parameter_to_value_map(self) -> Dict[str, Any]:
        """
        Map of parameter names to their filled values.
        
        Args:
            None
            
        Returns:
            Dict[str, Any]: Map of parameter names to their current values
        """
        if not self._filled:
            return {}
        return {
            "intermediate_results": self._intermediate_results.copy()
        }
    
    def fill(self, parameters: Dict[str, Any]) -> None:
        """
        Fill in the blueprint with the provided parameters.
        
        Args:
            parameters (Dict[str, Any]): Dictionary containing 'intermediate_results' key with list of strings
            
        Returns:
            None: Fills the blueprint with provided parameters
            
        Raises:
            ValueError: If required parameters are missing or invalid
        """
        if "intermediate_results" not in parameters:
            raise ValueError("DecisionBlueprint requires 'intermediate_results' parameter")
        
        intermediate_results = parameters["intermediate_results"]
        
        if not isinstance(intermediate_results, list):
            raise ValueError("intermediate_results must be a list of strings")
        for item_index, item in enumerate(intermediate_results):
            if not isinstance(item, str):
                raise ValueError(f"All intermediate_results must be strings, but item {item_index} is {type(item)}")
        self._intermediate_results = intermediate_results.copy()
        self._filled = True
    
    def get_intermediate_results(self) -> List[str]:
        """
        Get the stored intermediate results.
        
        Args:
            None
            
        Returns:
            List[str]: List of string descriptions of intermediate results
            
        Raises:
            RuntimeError: If blueprint hasn't been filled yet
        """
        if not self._filled:
            raise RuntimeError("DecisionBlueprint has not been filled yet")
        return self._intermediate_results.copy()
    
    def is_filled(self) -> bool:
        """
        Check if the blueprint has been filled with parameters.
        
        Args:
            None
            
        Returns:
            bool: True if blueprint has been filled, False otherwise
        """
        return self._filled
    
    def format_for_next_call(self) -> str:
        """
        Format the intermediate results as context for the next architect call.
        
        Args:
            None
            
        Returns:
            str: Formatted string suitable for additional_context_prompt
            
        Raises:
            RuntimeError: If blueprint hasn't been filled yet
        """
        if not self._filled:
            raise RuntimeError("DecisionBlueprint has not been filled yet")
        
        if not self._intermediate_results:
            return "Previous architect call completed with no intermediate results."
        
        context = "Previous architect call results:\n"
        for result_index, result in enumerate(self._intermediate_results, 1):
            context += f"{result_index}. {result}\n"
        
        context += "\nUse these results to continue with the conditional logic that was requested."
        return context
