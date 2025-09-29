from enum import Enum


class ExecutionMode(Enum):  
    """Defines the type of concurrent execution."""

    IMMEDIATE = "immediate"
    ASYNCIO = "asyncio"
    THREAD = "thread"
    PROCESS = "process"