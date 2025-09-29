# ArchitectAI

## Introduction

ArchitectAI is an LLM orchestration package designed to give users the ability to build robust solutions while taking full advantage of the various methods of concurrency available within Python.

## What ArchitectAI Does Different

Popular LLM orchestration tools rely on an agent-based paradigm. The flaw in this approach is each agent in a sequence generally requires an additional call to the LLM to determine whether to call the next agent. Conversely, ArchitectAI determines the full execution sequence within a single LLM call, including functions that are to be executed in parallel and those that will be executed in sequence. Parallel calls are always started concurrently, but those functions can run in the background until they are referenced by a subsequent stage, which results in the output being fetched and used as input into that stage.

## The Trade-Off

The benefit of an agentic system is that agents can dynamically decide which of their child nodes to invoke based on all of the previous output, whereas ArchitectAI is unable to dynamically change the function call order based on the results of previous calls. However, good system design is able to negate this issue in most cases, and if necessary, functions can be defined to handle previous stage input (using a user defined LLM call within that function if needed) and make a decision about what action to take based on that input. With ArchitectAI, you will have to work a little harder to achieve the same level of branching offered by tools like LangGraph, but it is still possible and generally more optimal once the solution has been engineered.

## Use Cases

ArchitectAI excels in scenarios where:

- **Performance is critical** - Single LLM call reduces latency and token costs
- **Parallel processing is valuable** - Multiple I/O operations, data processing, or API calls can run concurrently
- **Predictable workflows** - The execution flow can be determined upfront rather than requiring dynamic decisions
- **Resource optimization** - Background processing while waiting for LLM responses maximizes efficiency
- **Complex data pipelines** - Multi-stage processing with dependencies between stages
- **Cost-sensitive applications** - Fewer LLM calls mean lower operational costs

## Installation

```bash
pip install architect-ai
```

## Core Concepts

### Tools
Tools are the building blocks of your workflows. Each tool defines what it does, when to use it, what inputs it accepts, and what outputs it produces. Tools can run in different execution modes (immediate, threaded, async, or process-based) depending on their computational requirements.

### Blueprints
Blueprints capture and document the results of your workflows. They provide structured storage for outputs and ensure consistent documentation of execution results.

### Build Plans
ArchitectAI generates JSON build plans that specify the complete execution sequence. Tools within the same stage execute in parallel, while stages execute sequentially. Later stages can reference outputs from earlier stages using a powerful reference system.

### Execution Modes
- **Immediate**: Synchronous execution in the main thread
- **Thread**: Concurrent execution for I/O-bound operations  
- **Asyncio**: Asynchronous execution for high-concurrency scenarios
- **Process**: Isolated execution for CPU-intensive tasks

### Lazy Evaluation
Tools start executing immediately when a stage begins, but their results are only fetched when referenced by subsequent stages or blueprints. This maximizes parallel processing efficiency.

## Important Constraints & Warnings

### ⚠️ Naming Requirements
- **Tool names must not end in a number** - Use `calculator_tool` instead of `calculator1`
- **Blueprint names have the same restrictions** - Follow consistent naming patterns
- Use descriptive, suffix-free names to avoid conflicts with internal indexing

### ⚠️ Execution Mode Contracts
- **Async tools must have async use methods** - If `execution_mode = ExecutionMode.ASYNCIO`, the `use()` method must be `async def`
- **Process tools cannot reference concurrent executables** - PROCESS mode tools run in isolation and cannot access concurrent executable results
- **Precallable tools cannot be called in immediate mode** - They must run in background execution modes

### ⚠️ Reference System Behavior
- **Reference parsing stops at non-alphanumeric characters** - `$ref.stage_1.tool.result.value!` parses as `$ref.stage_1.tool.result.value`
- **Support for list and nested access** - Use `$ref.stage_1.tool.data.items[0].name` for nested object access
- **Multiple embedded references allowed** - Strings can contain multiple references: `"Result: $ref.stage_1.calc.result and $ref.stage_2.format.output"`

### ⚠️ API and Performance Notes  
- **Token limit warning** - The `token_limit` parameter restricts LLM response length; set carefully to avoid truncated build plans
- **Execution continues on errors** - Individual tool failures don't halt the entire workflow; errors are captured and logged

## Architecture Benefits

### Single LLM Call Efficiency
Rather than multiple round-trips between your application and the LLM service, ArchitectAI generates the complete execution plan in one call. This reduces:
- **Latency** - Fewer network round-trips
- **Token costs** - No repeated context in multiple calls  
- **Complexity** - Predictable execution flow

### Intelligent Concurrency
ArchitectAI automatically identifies opportunities for parallel execution and manages the complexity of different execution modes. Tools run concurrently within stages, but results are fetched lazily only when needed.

### Flexible Tool Ecosystem
Build reusable tools that can be combined in different ways. Tools encapsulate specific functionality while remaining composable across different workflows.

## Performance Characteristics

### Optimal Scenarios
- **High I/O workloads** - Network requests, file operations, database queries benefit from concurrent execution
- **Multi-stage pipelines** - Complex workflows with clear dependencies between processing steps  
- **Resource-intensive tasks** - CPU-bound operations can be isolated in separate processes

### Considerations
- **Dynamic branching** - Requires more upfront planning compared to agent-based systems
- **Complex conditional logic** - May need to be embedded within individual tools rather than handled at the orchestration level
- **Learning curve** - Understanding execution modes and reference systems requires initial investment

## Getting Started

ArchitectAI requires defining your tools and blueprints, then letting the LLM orchestrate their execution. The system handles concurrency, dependency resolution, and result management automatically.

## Package Information

- **Version**: 0.1.1  
- **License**: MIT
- **Python**: >=3.9
- **Dependencies**: openai>=1.0.0, psutil>=5.9.0

For detailed examples and API documentation, see the documentation and examples directory.