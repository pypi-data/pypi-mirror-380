from abc import ABC, abstractmethod
from typing import Dict, Tuple, Any


class Blueprint(ABC):
    """Base interface that all user-defined blueprints must implement."""

    @abstractmethod
    def fill(self, parameters: Dict[str, Any]) -> None:
        """
        Fill in the blueprint with the provided parameters.

        Args:
            parameters: A dictionary of parameters to use to fill in the blueprint.
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def name(self) -> str:
        """Unique identifier for this blueprint."""
        raise NotImplementedError

    @property
    @abstractmethod
    def usage_context(self) -> str:
        """Description of when this blueprint should be used."""
        raise NotImplementedError

    @property
    @abstractmethod
    def purpose(self) -> str:
        """Description of what this blueprint is used for."""
        raise NotImplementedError

    @property
    @abstractmethod
    def parameter_instructions(self) -> Dict[str, Tuple[str, str]]:
        """Map of parameter names to (DataType, description) tuples."""
        raise NotImplementedError

    @property
    @abstractmethod
    def parameter_to_value_map(self) -> Dict[str, Any]:
        """Map of parameter names to their filled values."""
        raise NotImplementedError
