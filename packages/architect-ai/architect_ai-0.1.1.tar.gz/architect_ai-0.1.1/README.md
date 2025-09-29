# Architect AI

A flexible AI-powered system for orchestrating workflows through custom tools and blueprints. The Architect automatically generates and executes build plans to accomplish user goals by combining available tools.

## Installation

```bash
pip install architect-ai
```

## Quick Start

### 1. Initialize the Client

```python
from architect_ai import Client, ClientType
import asyncio

# Basic client setup
client = Client(
    client_type=ClientType.OPENAI,
    client_api_key="your-api-key",
    use_async=False,
    model_name="gpt-4",
    token_limit=1000  # Optional: limit response tokens for JSON parsing security
)

# Async client with event loop
event_loop = asyncio.new_event_loop()
async_client = Client(
    client_type=ClientType.OPENAI,
    client_api_key="your-api-key", 
    use_async=True,
    model_name="gpt-4",
    asyncio_event_loop=event_loop
)
```

### 2. Create a Tool

```python
from architect_ai import Tool, ExecutionMode
from typing import Dict, Any, Tuple

class CalculatorTool(Tool):
    @property
    def name(self) -> str:
        return "calculator"
    
    @property
    def execution_mode(self) -> ExecutionMode:
        return ExecutionMode.IMMEDIATE  # IMMEDIATE, THREAD, ASYNCIO, PROCESS
    
    @property
    def usage_context(self) -> str:
        return "For basic mathematical calculations"
    
    @property
    def purpose(self) -> str:
        return "Performs addition, subtraction, multiplication, division"
    
    @property
    def parameter_instructions(self) -> Dict[str, Tuple[str, str]]:
        return {
            "operation": ("str", "The math operation: add, subtract, multiply, divide"),
            "a": ("float", "First number"),
            "b": ("float", "Second number")
        }
    
    @property
    def output_descriptions(self) -> Dict[str, Tuple[str, str]]:
        return {
            "result": ("float", "The calculation result"),
            "operation_performed": ("str", "Description of what was calculated")
        }
    
    def use(self, parameters: Dict[str, Any], concurrent_executables=None):
        op = parameters["operation"]
        a, b = float(parameters["a"]), float(parameters["b"])
        
        if op == "add":
            result = a + b
        elif op == "multiply":
            result = a * b
        else:
            result = 0
            
        return {
            "result": result,
            "operation_performed": f"{a} {op} {b} = {result}"
        }
```

### 3. Create a Blueprint

```python
from architect_ai import Blueprint
from typing import Dict, Any, Tuple

class ResultBlueprint(Blueprint):
    def __init__(self):
        self.params = {}
    
    @property
    def name(self) -> str:
        return "calculation_result"
    
    @property
    def usage_context(self) -> str:
        return "For storing mathematical calculation results"
    
    @property
    def purpose(self) -> str:
        return "Documents the final calculation and context"
    
    @property
    def parameter_instructions(self) -> Dict[str, Tuple[str, str]]:
        return {
            "final_answer": ("float", "The final calculated result"),
            "steps": ("str", "Description of calculation steps"),
            "user_request": ("str", "The original user question")
        }
    
    @property
    def parameter_to_value_map(self) -> Dict[str, Any]:
        return self.params
    
    def fill(self, parameters: Dict[str, Any]) -> None:
        self.params = parameters
        print(f"Calculation completed: {parameters}")
```

### 4. Create a Concurrent Executable

```python
from architect_ai import ConcurrentExecutable, ExecutionMode
from concurrent.futures import ThreadPoolExecutor
import asyncio

# From a tool (recommended)
tool = CalculatorTool()
executor = ThreadPoolExecutor(max_workers=4)

executable = ConcurrentExecutable.from_tool(
    tool=tool,
    parameters={"operation": "add", "a": 5, "b": 3},
    thread_pool_executor=executor
)

# Manual creation
def my_function(params, concurrent_executables=None):
    return {"result": params["x"] * 2}

executable = ConcurrentExecutable(
    name="doubler",
    execution_mode=ExecutionMode.THREAD,
    func=my_function,
    func_args={"x": 10},
    thread_pool_executor=executor
)
```

### 5. Put it all together with Architect

```python
from architect_ai import Architect, ToolBox, BlueprintRack
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import asyncio

# Setup components
toolbox = ToolBox([CalculatorTool()])
blueprint_rack = BlueprintRack([ResultBlueprint()])

# Create executors
thread_pool = ThreadPoolExecutor(max_workers=4)
process_pool = ProcessPoolExecutor(max_workers=2)
event_loop = asyncio.new_event_loop()

# Initialize Architect
architect = Architect(
    client=client,
    model_name="gpt-4",
    toolbox=toolbox,
    blueprint_rack=blueprint_rack,
    asyncio_event_loop=event_loop,
    thread_pool_executor=thread_pool,
    process_pool_executor=process_pool
)

# Execute a request
build, concurrent_executables = architect.generate_response(
    customer_request="Calculate 15 * 7 and document the result",
    conversation_history="",
    additional_context_prompt="Show your work step by step"
)

# Access results
print("Build plan:", build.build_plan)
print("Stage outputs:", build.stage_outputs)
print("Filled blueprints:", build.filled_blueprints)
```

## Important Constraints & Notes

### ⚠️ Tool and Blueprint Naming
- **Tool names must not end in a number** (e.g., avoid `calculator1`, `processor2`)
- **Blueprint names have the same naming restrictions** as tools
- Use descriptive names like `calculator_tool` or `math_processor` instead

### ⚠️ Execution Mode Contracts
- **Tools cannot be async and not have use defined as async** - If `execution_mode = ExecutionMode.ASYNCIO`, the `use()` method must be `async def use(...)`
- **If it's a process, you cannot reference concurrent executables** - PROCESS mode tools receive `None` for concurrent_executables parameter
- **Precallable tools cannot be called in immediate mode** - They run before build execution starts

### ⚠️ Reference Parsing
- **Regex will stop parsing symbols after the last period when it encounters something not a number, underscore or letter** - References like `$ref.stage_1.tool.result.value!` will parse as `$ref.stage_1.tool.result.value`
- **Specify list and nested access** using dot notation: `$ref.stage_1.tool.data.items[0].name`
- **Note that strings can have multiple references embedded**: `"Result: $ref.stage_1.calc.result and $ref.stage_2.format.output"`

### ⚠️ Token Warning
When using the `token_limit` parameter in Client initialization, be aware this limits the LLM's response length. Set too low and build plans may be truncated. Use for JSON parsing security when needed.

## Execution Modes

- **IMMEDIATE**: Executes synchronously in main thread
- **THREAD**: Executes in thread pool (for I/O bound operations) 
- **ASYNCIO**: Executes asynchronously (requires async use method)
- **PROCESS**: Executes in separate process (for CPU-bound tasks, no concurrent executable access)

## Reference System

Build plans use `$ref.stage_X.tool_name.output_param` to reference previous outputs:

```json
{
  "stage_1": {
    "calculator": {
      "operation": "multiply",
      "a": 15,
      "b": 7
    }
  },
  "stage_2": {
    "formatter": {
      "result": "$ref.stage_1.calculator.result",
      "operation": "$ref.stage_1.calculator.operation_performed"
    }
  },
  "calculation_result": {
    "final_answer": "$ref.stage_1.calculator.result",
    "steps": "$ref.stage_2.formatter.formatted_output",
    "user_request": "Calculate 15 * 7"
  }
}
```

## Error Handling

The Architect automatically retries failed build plans. Tools should handle exceptions gracefully and return meaningful error information in outputs.

## Performance Tips

1. **Keep tools focused** - Single responsibility per tool
2. **Use appropriate execution modes** - IMMEDIATE for simple ops, THREAD for I/O, PROCESS for CPU-heavy tasks
3. **Minimize build plan size** - Smaller plans generate faster
4. **Leverage parallel stages** - Tools in same stage run concurrently

## Package Information

- **Version**: 0.1.0
- **License**: MIT
- **Python**: >=3.9
- **Dependencies**: openai>=1.0.0, psutil>=5.9.0

For more examples and advanced usage, see the `/examples` directory.