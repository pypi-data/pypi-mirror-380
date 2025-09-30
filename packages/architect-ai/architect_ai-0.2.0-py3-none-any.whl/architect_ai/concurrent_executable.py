import asyncio
from typing import Any, Callable, Optional, Dict, List
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import logging
from .tool import Tool
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
        """
        Initialize a concurrent executable wrapper for different execution modes.
        
        Args:
            name (str): Name identifier for this executable
            execution_mode (ExecutionMode): Mode of execution (ASYNCIO, THREAD, PROCESS, IMMEDIATE)
            func (Callable): Function to execute
            func_args (Optional[Dict[str, Any]]): Arguments to pass to the function
            func_initial_concurrent_executables (Optional[List[ConcurrentExecutable]]): Initial concurrent executables
            asyncio_event_loop (Optional[asyncio.AbstractEventLoop]): Event loop for asyncio execution
            thread_pool_executor (Optional[ThreadPoolExecutor]): Thread pool for thread execution
            process_pool_executor (Optional[ProcessPoolExecutor]): Process pool for process execution
            
        Returns:
            None: Initializes the concurrent executable instance
        """
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
        """
        Create a ConcurrentExecutable from a Tool instance.
        
        Args:
            tool (Tool): Tool instance to wrap
            parameters (Dict[str, Any]): Parameters to pass to the tool
            initial_concurrent_executables (Optional[List[ConcurrentExecutable]]): Initial concurrent executables
            asyncio_event_loop (Optional[asyncio.AbstractEventLoop]): Event loop for asyncio execution
            thread_pool_executor (Optional[ThreadPoolExecutor]): Thread pool for thread execution
            process_pool_executor (Optional[ProcessPoolExecutor]): Process pool for process execution
            
        Returns:
            ConcurrentExecutable: New instance wrapping the tool
        """
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
        """
        Validate that the required executors are provided for the execution mode.
        
        Args:
            None
            
        Returns:
            None: Validates initialization parameters
            
        Raises:
            ValueError: If required executor is missing for the execution mode
        """
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
        """
        Start the concurrent executable based on its execution mode.
        
        Args:
            None
            
        Returns:
            None: Starts the executable and sets running state
            
        Raises:
            ValueError: If already running or invalid execution mode or missing executor
        """
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
        except Exception as start_error:
            logger.warning(f"Failed to start ConcurrentExecutable '{self.name}': {type(start_error).__name__}: {start_error}")
            logger.warning(f"Full start failure traceback for '{self.name}':", exc_info=True)
            self.is_current_running = False
            raise

    def is_ready(self) -> bool:
        """
        Check if the concurrent executable is ready with computation complete.
        
        Args:
            None
            
        Returns:
            bool: True if computation is complete and results are ready, False otherwise
        """
        if not self.is_current_running:
            return False
        if self.execution_mode == ExecutionMode.IMMEDIATE:
            return True
        elif self.execution_mode in [ExecutionMode.THREAD, ExecutionMode.PROCESS, ExecutionMode.ASYNCIO]:
            if self.running_future is not None:
                return self.running_future.done()
            return False
        else:
            return False

    def fetch_results(self) -> Any:
        """
        Fetch the results from the completed concurrent executable.
        
        Args:
            None
            
        Returns:
            Any: Results from the completed execution
            
        Raises:
            ValueError: If executable is not running or execution fails
        """
        if not self.is_current_running:
            raise ValueError("Concurrent executable is not running")
        try:
            logger.debug(
                f"Fetching results for '{self.name}' in mode {self.execution_mode}; has_future={self.running_future is not None}"
            )
            if (
                self.execution_mode
                in [ExecutionMode.THREAD, ExecutionMode.PROCESS, ExecutionMode.ASYNCIO]
                and self.running_future is not None
            ):
                logger.debug(f"Waiting on future.result() for '{self.name}'")
                return self.running_future.result(timeout=60)
            elif self.execution_mode == ExecutionMode.IMMEDIATE:
                return self.running_future
            else:
                raise ValueError(
                    f"Invalid execution mode: {self.execution_mode} or no available task/future"
                )
        except Exception as fetch_error:
            logger.error(
                f"ConcurrentExecutable '{self.name}' failed with exception: {type(fetch_error).__name__}: {fetch_error}"
            )
            logger.error("Full traceback:", exc_info=True)
            raise ValueError(f"Failed to fetch results: {fetch_error}") from fetch_error

    async def fetch_results_async(self) -> Any:
        """
        Asynchronously fetch results without blocking the event loop.
        
        Args:
            None
            
        Returns:
            Any: Results from the completed execution
        """
        if not self.is_current_running:
            raise ValueError("Concurrent executable is not running")
        if self.execution_mode in [ExecutionMode.THREAD, ExecutionMode.PROCESS, ExecutionMode.ASYNCIO] and self.running_future is not None:
            wrapped = asyncio.wrap_future(self.running_future)
            return await asyncio.wait_for(wrapped, timeout=60)
        if self.execution_mode == ExecutionMode.IMMEDIATE:
            return self.running_future
        raise ValueError(f"Invalid execution mode: {self.execution_mode} or no available task/future")

    def stop(self) -> None:
        """
        Stop the running concurrent executable and clean up resources.
        
        Args:
            None
            
        Returns:
            None: Stops the executable and cleans up state
            
        Raises:
            ValueError: If executable is not currently running
        """
        try:
            if self.is_current_running:
                self.running_future.cancel()
                self.is_current_running = False
                logger.debug(f"ConcurrentExecutable '{self.name}' stopped successfully")
            else:
                raise ValueError("Concurrent executable is not running")
        except Exception:
            self.is_current_running = False
            self.running_future = None
        finally:
            self.running_future = None
            self.is_current_running = False
