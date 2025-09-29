import asyncio
from typing import Any, Callable, Optional, Dict, List
from concurrent.futures import Future, ProcessPoolExecutor, ThreadPoolExecutor
import logging
from .tool import Tool, wrap_tool_func
from .execution_mode import ExecutionMode

logger = logging.getLogger(__name__)


class ConcurrentExecutable:
    """
    Unified wrapper for handling asyncio tasks, threading operations, and multiprocessing operations.

    Provides a consistent API regardless of execution type.
    """

    def __init__(
        self,
        name: str,
        execution_mode: ExecutionMode,
        func: Callable,
        func_args: Optional[Dict[str, Any]] = None,
        func_initial_concurrent_executables: Optional[
            List["ConcurrentExecutable"]
        ] = None,
        asyncio_event_loop: Optional[asyncio.AbstractEventLoop] = None,
        thread_pool_executor: Optional[ThreadPoolExecutor] = None,
        process_pool_executor: Optional[ProcessPoolExecutor] = None,
    ):
        self.name = name
        self.execution_mode = execution_mode
        self.func = func
        self.func_args = func_args
        self.func_initial_concurrent_executables = func_initial_concurrent_executables
        self.asyncio_event_loop = asyncio_event_loop
        self.thread_pool_executor = thread_pool_executor
        self.process_pool_executor = process_pool_executor
        self.running_future: Any = None
        self.validate_initialization()
        self.is_current_running = False

    @classmethod
    def from_tool(
        cls,
        tool: Tool,
        parameters: Dict[str, Any],
        initial_concurrent_executables: Optional[List["ConcurrentExecutable"]] = None,
        asyncio_event_loop: Optional[asyncio.AbstractEventLoop] = None,
        thread_pool_executor: Optional[ThreadPoolExecutor] = None,
        process_pool_executor: Optional[ProcessPoolExecutor] = None,
    ) -> "ConcurrentExecutable":
        return cls(
            name=tool.name,
            execution_mode=tool.execution_mode,
            func=tool.use,
            func_args=parameters,
            func_initial_concurrent_executables=initial_concurrent_executables,
            asyncio_event_loop=asyncio_event_loop,
            thread_pool_executor=thread_pool_executor,
            process_pool_executor=process_pool_executor,
        )

    def validate_initialization(self) -> None:
        if self.execution_mode == ExecutionMode.ASYNCIO:
            if self.asyncio_event_loop is None:
                raise ValueError("Asyncio event loop is required for asyncio execution")
        elif self.execution_mode == ExecutionMode.THREAD:
            if self.thread_pool_executor is None:
                raise ValueError(
                    "Thread pool executor is required for thread execution"
                )
        elif self.execution_mode == ExecutionMode.PROCESS:
            if self.process_pool_executor is None:
                raise ValueError(
                    "Process pool executor is required for process execution"
                )

    def start(self) -> None:
        if self.is_current_running:
            raise ValueError("Concurrent executable is already running")
        
        try:
            logger.debug(f"Starting ConcurrentExecutable '{self.name}' with mode {self.execution_mode}")
            
            if self.execution_mode == ExecutionMode.ASYNCIO:
                if self.asyncio_event_loop is None:
                    raise ValueError("Asyncio event loop is required for asyncio execution")
                if self.func_args is None:
                    self.running_future = asyncio.run_coroutine_threadsafe(
                        self.func(), self.asyncio_event_loop
                    )
                else:
                    self.running_future = asyncio.run_coroutine_threadsafe(
                        self.func(self.func_args, self.func_initial_concurrent_executables),
                        self.asyncio_event_loop,
                    )
            elif self.execution_mode == ExecutionMode.THREAD:
                if self.thread_pool_executor is None:
                    raise ValueError(
                        "Thread pool executor is required for thread execution"
                    )
                if self.func_args is None:
                    self.running_future = self.thread_pool_executor.submit(self.func)
                else:
                    self.running_future = self.thread_pool_executor.submit(
                        self.func, self.func_args, self.func_initial_concurrent_executables
                    )
            elif self.execution_mode == ExecutionMode.PROCESS:
                if self.process_pool_executor is None:
                    raise ValueError(
                        "Process pool executor is required for process execution"
                    )
                if self.func_args is None:
                    self.running_future = self.process_pool_executor.submit(self.func)
                else:
                    self.running_future = self.process_pool_executor.submit(
                        self.func, self.func_args
                    )
            elif self.execution_mode == ExecutionMode.IMMEDIATE:
                if self.func_args is None:
                    self.running_future = self.func()
                else:
                    self.running_future = self.func(self.func_args, self.func_initial_concurrent_executables)
            else:
                raise ValueError(f"Invalid execution mode: {self.execution_mode}")
            
            self.is_current_running = True
            logger.debug(f"ConcurrentExecutable '{self.name}' started successfully")
            
        except Exception as e:
            logger.warning(f"Failed to start ConcurrentExecutable '{self.name}': {type(e).__name__}: {e}")
            logger.warning(f"Full start failure traceback for '{self.name}':", exc_info=True)
            self.is_current_running = False
            raise

    def fetch_results(self) -> Any:
        if not self.is_current_running:
            raise ValueError("Concurrent executable is not running")
        try:
            if (
                self.execution_mode
                in [ExecutionMode.THREAD, ExecutionMode.PROCESS, ExecutionMode.ASYNCIO]
                and self.running_future is not None
            ):
                return self.running_future.result()
            elif self.execution_mode == ExecutionMode.IMMEDIATE:
                return self.running_future
            else:
                raise ValueError(
                    f"Invalid execution mode: {self.execution_mode} or no available task/future"
                )
        except Exception as e:
            logger.error(
                f"ConcurrentExecutable '{self.name}' failed with exception: {type(e).__name__}: {e}"
            )
            logger.error(f"Full traceback:", exc_info=True)
            raise ValueError(f"Failed to fetch results: {e}") from e

    def stop(self) -> None:
        try:
            if self.is_current_running:
                self.running_future.cancel()
                self.is_current_running = False
                logger.debug(f"ConcurrentExecutable '{self.name}' stopped successfully")
            else:
                raise ValueError("Concurrent executable is not running")
        except Exception as e:
            self.is_current_running = False
            self.running_future = None
        finally:
            self.running_future = None
            self.is_current_running = False
