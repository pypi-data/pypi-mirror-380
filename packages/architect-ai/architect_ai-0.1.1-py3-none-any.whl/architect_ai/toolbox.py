from typing import Dict, List, Optional

from .tool import Tool


class ToolBox:
    def __init__(self, tools: Optional[List[Tool]] = None):
        """
        The ToolBox class acts as a container for all the tools that will be available to the Architect.

        Args:
            tools: A list of Tool objects to add to the ToolBox.
        """
        self.tools: Dict[str, Tool] = {}
        if tools:
            self._validate_and_add_tools(tools)

    def add_tool(self, tool: Tool) -> None:
        """
        Adds a Tool object to the ToolBox.

        Args:
            tool: The Tool object to add to the ToolBox.
        """
        if not hasattr(tool, "name"):
            raise ValueError("Tool must have a name attribute")
        if tool.name in self.tools:
            raise ValueError(f"Tool with name '{tool.name}' already exists")
        self.tools[tool.name] = tool

    def set_tool_list(self, tools: List[Tool]) -> None:
        """
        Sets the list of Tool objects to the ToolBox, removing any existing tools.

        Args:
            tools: A list of Tool objects to set in the ToolBox.
        """
        self.tools = {}
        self._validate_and_add_tools(tools)

    def find_by_name(self, name: str) -> Optional[Tool]:
        """
        Finds a Tool object by its name.

        Args:
            name: The name of the Tool object to find.

        Returns:
            Tool: The Tool object if found, otherwise None.
        """
        return self.tools.get(name)

    def remove_tool(self, name: str) -> None:
        """
        Removes a Tool object from the ToolBox.

        Args:
            name: The name of the Tool object to remove.
        """
        if name in self.tools:
            del self.tools[name]

    def open_tool(self, name: str) -> Optional[str]:
        """
        Creates a string representation of a Tool object formatted for consumption by an Large Language Model.

        Args:
            name: The name of the Tool object to open.

        Returns:
            str: A string representation of the Tool object
        """
        tool: Optional[Tool] = self.tools.get(name)
        if not tool:
            return None
        tool_details: str = f"TOOL NAME: {tool.name}\n"
        tool_details += f"Usage Context: {tool.usage_context}\n"
        tool_details += f"Purpose: {tool.purpose}\n"
        tool_details += "Parameter Instructions:\n"
        for param_name, (data_type, description) in tool.parameter_instructions.items():
            tool_details += f"  {param_name} ({data_type}): {description}\n"
        tool_details += "\nOutput Descriptions:\n"
        for output_name, (data_type, description) in tool.output_descriptions.items():
            tool_details += f"  {output_name} ({data_type}): {description}\n"
        return tool_details

    def open_all_tools(self) -> str:
        """
        Opens each tool and appends the details to a single string.

        Returns:
            str: A string representation of all the Tool objects in the ToolBox.
        """
        all_tool_details: str = "TOOLS:\n--------------------------------\n"
        for name in self.tools.keys():
            tool_details: Optional[str] = self.open_tool(name)
            if tool_details:
                all_tool_details += tool_details + "\n"
        return all_tool_details

    def _validate_and_add_tools(self, tools: List[Tool]) -> None:
        """
        Validates the tools and adds them to the ToolBox.

        Args:
            tools: A list of Tool objects to add to the ToolBox.
        """
        for tool in tools:
            if not hasattr(tool, "name"):
                raise ValueError("Tool must have a name attribute")
            if tool.name in self.tools:
                raise ValueError(
                    f"Tool with name '{tool.name}' already exists"
                )
            self.tools[tool.name] = tool
