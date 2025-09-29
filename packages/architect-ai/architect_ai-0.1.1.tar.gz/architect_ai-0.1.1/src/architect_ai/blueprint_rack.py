from typing import Dict, List, Optional
import logging

from .blueprint import Blueprint
from .logging_utils import log_structured

logger = logging.getLogger(__name__)


# =============================================================================
# BLUEPRINT RACK EXCEPTIONS
# =============================================================================


class BlueprintRackError(Exception):
    """Base exception for BlueprintRack-related errors."""

    def __init__(self, message: str, **context):
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
        super().__init__(
            f"Blueprint with name '{name}' already exists", name=name, **context
        )


class BlueprintRack:
    def __init__(self, blueprints: Optional[List[Blueprint]] = None):
        """
        The BlueprintRack class acts as a container for all the blueprints that will be available to the Architect.

        Args:
            blueprints: A list of Blueprint objects to add to the BlueprintRack.
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
            blueprint: The Blueprint object to add to the BlueprintRack.
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
            blueprints: A list of Blueprint objects to add to the BlueprintRack.
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
            name: The name of the Blueprint object to find.

        Returns:
            Optional[Blueprint]: The Blueprint object if found, otherwise None.
        """
        blueprint = self.blueprints.get(name)
        if blueprint:
            log_structured(logger, "debug", "Found blueprint by name", name=name)
        else:
            log_structured(
                logger,
                "warning",
                "Blueprint not found by name",
                name=name,
                available_blueprints=list(self.blueprints.keys()),
            )
        return blueprint

    def remove_blueprint(self, name: str) -> None:
        """
        Removes a Blueprint object from the BlueprintRack.

        Args:
            name: The name of the Blueprint object to remove.
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
        Creates a string representation of a Blueprint object formatted for consumption by an Large Language Model.

        Args:
            name: The name of the Blueprint object to open.

        Returns:
            str: A string representation of the Blueprint object
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
            blueprints: A list of Blueprint objects to add to the BlueprintRack.
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
