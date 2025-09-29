from typing import Dict, List, Optional
import logging

from .blueprint import Blueprint
from .logging_utils import log_structured

logger = logging.getLogger(__name__)


class BlueprintRackError(Exception):
    """
    Base exception for BlueprintRack-related errors.
    
    Args:
        message (str): Error message
        **context: Additional context information for the error
        
    Returns:
        None: Exception class for blueprint rack errors
    """

    def __init__(self, message: str, **context):
        """
        Initialize the blueprint rack error with message and context.
        
        Args:
            message (str): Error message
            **context: Additional context information
            
        Returns:
            None: Initializes the exception instance
        """
        super().__init__(message)
        self.context = context


class BlueprintValidationError(BlueprintRackError):
    """Raised when blueprint validation fails."""

    def __init__(
        self,
        issue: str,
        blueprint_type: Optional[str] = None,
        name: Optional[str] = None,
        **context,
    ):
        """
        Initialize the blueprint validation error.
        
        Args:
            issue (str): Description of the validation issue
            blueprint_type (Optional[str]): Type of blueprint that failed validation
            name (Optional[str]): Name of blueprint that failed validation
            **context: Additional context information
            
        Returns:
            None: Initializes the validation error instance
        """
        super().__init__(
            f"Blueprint validation failed: {issue}",
            issue=issue,
            blueprint_type=blueprint_type,
            name=name,
            **context,
        )


class DuplicateBlueprintError(BlueprintRackError):
    """Raised when attempting to add a blueprint with a name that already exists."""

    def __init__(self, name: str, **context):
        """
        Initialize the duplicate blueprint error.
        
        Args:
            name (str): Name of the duplicate blueprint
            **context: Additional context information
            
        Returns:
            None: Initializes the duplicate blueprint error instance
        """
        super().__init__(
            f"Blueprint with name '{name}' already exists", name=name, **context
        )


class BlueprintRack:
    def __init__(self, blueprints: Optional[List[Blueprint]] = None):
        """
        Initialize the BlueprintRack as a container for blueprints available to the Architect.

        Args:
            blueprints (Optional[List[Blueprint]]): A list of Blueprint objects to add to the BlueprintRack
            
        Returns:
            None: Initializes the blueprint rack instance
        """
        self.blueprints: Dict[str, Blueprint] = {}
        if blueprints:
            log_structured(
                logger,
                "info",
                "Initializing BlueprintRack",
                blueprint_count=len(blueprints),
            )
            self._validate_and_add_blueprints(blueprints)
        else:
            log_structured(logger, "info", "Initialized empty BlueprintRack")

    def add_blueprint(self, blueprint: Blueprint) -> None:
        """
        Adds a Blueprint object to the BlueprintRack.

        Args:
            blueprint (Blueprint): The Blueprint object to add to the BlueprintRack
            
        Returns:
            None: Adds the blueprint to the rack
        """
        if not hasattr(blueprint, "name"):
            log_structured(
                logger,
                "error",
                "Failed to add blueprint - missing name attribute",
                blueprint_type=type(blueprint).__name__,
            )
            raise BlueprintValidationError(
                "Blueprint must have a name attribute",
                blueprint_type=type(blueprint).__name__,
            )
        if blueprint.name in self.blueprints:
            log_structured(
                logger,
                "error",
                "Failed to add blueprint - name already exists",
                name=blueprint.name,
            )
            raise DuplicateBlueprintError(blueprint.name)
        self.blueprints[blueprint.name] = blueprint
        log_structured(
            logger, "debug", "Added blueprint to BlueprintRack", name=blueprint.name
        )

    def set_blueprint_list(self, blueprints: List[Blueprint]) -> None:
        """
        Sets the list of Blueprint objects to the BlueprintRack, removing any existing blueprints.

        Args:
            blueprints (List[Blueprint]): A list of Blueprint objects to add to the BlueprintRack
            
        Returns:
            None: Replaces all existing blueprints with the provided list
        """
        old_count = len(self.blueprints)
        self.blueprints = {}
        self._validate_and_add_blueprints(blueprints)
        log_structured(
            logger,
            "info",
            "Updated blueprint list in BlueprintRack",
            old_count=old_count,
            new_count=len(blueprints),
        )

    def find_by_name(self, name: str) -> Optional[Blueprint]:
        """
        Finds a Blueprint object by its name.

        Args:
            name (str): The name of the Blueprint object to find

        Returns:
            Optional[Blueprint]: The Blueprint object if found, otherwise None
        """
        blueprint = self.blueprints.get(name)
        if blueprint:
            log_structured(logger, "debug", "Found blueprint by name", name=name)
            return blueprint
        attempted_name = name
        parsed_name = None
        if '_' in name and name.rsplit('_', 1)[-1].isdigit():
            parsed_name = name.rsplit('_', 1)[0]
            fallback = self.blueprints.get(parsed_name)
            if fallback:
                log_structured(
                    logger,
                    "info",
                    f"Blueprint not found by exact name '{attempted_name}'; using parsed base name '{parsed_name}'",
                    attempted_name=attempted_name,
                    resolved_name=parsed_name,
                    available_blueprints=list(self.blueprints.keys()),
                )
                return fallback
        log_structured(
            logger,
            "warning",
            f"Blueprint not found by name '{attempted_name}' (parsed base '{parsed_name}')",
            name=attempted_name,
            parsed_name=parsed_name,
            available_blueprints=list(self.blueprints.keys()),
        )
        return None

    def remove_blueprint(self, name: str) -> None:
        """
        Removes a Blueprint object from the BlueprintRack.

        Args:
            name (str): The name of the Blueprint object to remove
            
        Returns:
            None: Removes the blueprint from the rack
        """
        if name in self.blueprints:
            del self.blueprints[name]
            log_structured(
                logger, "debug", "Removed blueprint from BlueprintRack", name=name
            )
        else:
            log_structured(
                logger,
                "warning",
                "Attempted to remove non-existent blueprint",
                name=name,
            )

    def open_blueprint(self, name: str) -> Optional[str]:
        """
        Creates a string representation of a Blueprint object formatted for consumption by a Large Language Model.

        Args:
            name (str): The name of the Blueprint object to open

        Returns:
            Optional[str]: A string representation of the Blueprint object, or None if not found
        """
        blueprint: Optional[Blueprint] = self.blueprints.get(name)
        if not blueprint:
            return None
        blueprint_details: str = f"BLUEPRINT NAME: {blueprint.name}\n"
        blueprint_details += f"Usage Context: {blueprint.usage_context}\n"
        blueprint_details += f"Purpose: {blueprint.purpose}\n"
        blueprint_details += "Parameter Instructions:\n"
        for param_name, (
            data_type,
            description,
        ) in blueprint.parameter_instructions.items():
            blueprint_details += f"  {param_name} ({data_type}): {description}\n"
        return blueprint_details

    def open_all_blueprints(self) -> str:
        """
        Opens all Blueprint objects and appends the details to a single string.

        Args:
            None
            
        Returns:
            str: A string representation of all Blueprint objects
        """
        all_blueprint_details: str = "BLUEPRINTS:\n--------------------------------\n"
        for name in self.blueprints.keys():
            blueprint_details: Optional[str] = self.open_blueprint(name)
            if blueprint_details:
                all_blueprint_details += (
                    blueprint_details + "\n--------------------------------\n"
                )
        return all_blueprint_details

    def _validate_and_add_blueprints(self, blueprints: List[Blueprint]) -> None:
        """
        Validates and adds a list of Blueprint objects to the BlueprintRack.

        Args:
            blueprints (List[Blueprint]): A list of Blueprint objects to add to the BlueprintRack
            
        Returns:
            None: Validates and adds blueprints to the rack
            
        Raises:
            BlueprintValidationError: If blueprint validation fails
            DuplicateBlueprintError: If blueprint name already exists
        """
        for blueprint in blueprints:
            if not hasattr(blueprint, "name"):
                log_structured(
                    logger,
                    "error",
                    "Blueprint validation failed - missing name attribute",
                    blueprint_type=type(blueprint).__name__,
                )
                raise BlueprintValidationError(
                    "Blueprint must have a name attribute",
                    blueprint_type=type(blueprint).__name__,
                )
            if blueprint.name in self.blueprints:
                log_structured(
                    logger,
                    "error",
                    "Blueprint validation failed - duplicate name",
                    name=blueprint.name,
                )
                raise DuplicateBlueprintError(blueprint.name)
            self.blueprints[blueprint.name] = blueprint
        log_structured(
            logger,
            "info",
            "Successfully validated and added blueprints",
            count=len(blueprints),
        )
