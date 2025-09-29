import logging
import uuid
import asyncio
import time
from .client import Client
from .toolbox import ToolBox
from .blueprint_rack import BlueprintRack
from .concurrent_executable import ConcurrentExecutable
from .build import Build
from .blueprint import LazyBlueprint
from .exceptions.architect_exceptions import ExecutableFailedToStartError
from .logging_utils import log_structured as log_with_structure
from typing import List, Dict, Optional, Tuple
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


logger = logging.getLogger(__name__)


class Architect:
    """
    An expert systems architect that generates and executes build plans using available tools and blueprints.
    
    Args:
        client (Client): Client for communicating with AI model
        model_name (str): Name of the AI model to use
        toolbox (ToolBox): Collection of available tools
        blueprint_rack (BlueprintRack): Collection of available blueprints
        initial_concurrent_executables (Optional[List[ConcurrentExecutable]]): Initial executables to start
        asyncio_event_loop (Optional[asyncio.AbstractEventLoop]): Event loop for async operations
        thread_pool_executor (Optional[ThreadPoolExecutor]): Thread pool for concurrent execution
        process_pool_executor (Optional[ProcessPoolExecutor]): Process pool for concurrent execution
        
    Returns:
        Architect: Configured architect instance ready to generate responses
    """
    build_plan_generation_base_prompt = """
    You are an expert systems architect, named Arch, with 30 years of experience in the technology industry. Your primary objective is to generate a build plan that will outline exactly how to make use of the various tools at your disposal to meet the product owner's demands (the user with which you will be interacting is the product owner). You must also ensure that this information is documented correctly by filling in the parameters of any blueprints that are applicable to the customer's request. Each tool in your toolbox comes with a guide that details when to use it, what it does, and how to format the input parameters to get your desired output parameters. Each blueprint on the blueprint rack comes with a guide that details when to use it and how to correctly fill in the parameters to ensure that your work has been correctly documented. 

    The final deliverable will be a JSON representation of the build plan constructed such that there is no room for ambiguity. There are two types of "top level" keys that should be present in the JSON. First, there should be a series of numbered "stage" keys ('stage_1', 'stage_2', etc.) that each contain a list of tools and their respective input parameters. Each tool contained within a stage will be executed in parallel. Once all the tools in a stage have returned, the next stage will begin. Subsequent stages will have access to the outputs of the previous stages. Where possible, make full use of parallel execution to maximize efficiency, including multiple tools in the same stage. To include tool calls within a stage, you should use the following format:

    {{
        "stage_1": {{
            "tool_name_1": {{
                "input_param_1": "text_value_1",
                "input_param_2": 8,
            }}
            "tool_name_2": {{
                "input_param_1": "text_value_1",
            }}
        }}
        ...
    }}

    Tool calls in subsequent stages will often need to reference the outputs of the previous stages. To make use of this ability, you should use the format $ref.stage_name.tool_name.output_param_name anywhere within strings, lists, or nested structures. References can be mixed with regular values. See the following example:

    {{
        "stage_1": {{
            "tool_name_1": {{
                "input_param_1": "text_value_1",
            }}
        }}
        "stage_2": {{
            "tool_name_2": {{
                "input_param_1": "Processing result: $ref.stage_1.tool_name_1.output_param_1",
                "input_param_2": ["item1", 42, "$ref.stage_1.tool_name_1.output_param_2"],
                "input_param_3": "$ref.stage_1.tool_name_1.output_param_1"
            }}
        }}
    }}

    The other top level keys in the JSON object must be the names of the blueprint(s) that are applicable to the customer's request. These will be mapped to a list of input parameters for that respective blueprint. Again, each blueprint will come with instructions as to when to use it and how to correctly fill in the parameters. Here is an example of how the final JSON object should look. However, keep in mind that the number of stages and blueprints required will vary based on the customer's request.

    {{
        "stage_1": {{
            "tool_name_1": {{
                "input_param_1": "text_value_1",
            }}
            ...
        }}
        "stage_2": {{
            "tool_name_2": {{
                "input_param_1": "$ref.stage_1.tool_name_1.output_param_1"
            }}
            "tool_name_3": {{
                "input_param_1": "text_value_1",
            }}
            ...
        }}
        ...
        "blueprint_1": {{
            "input_param_1": "text_value_1",
            "input_param_2": "$ref.stage_2.tool_name_2.output_param_1"
        }}
        "blueprint_2": {{
            "input_param_1": "$ref.stage_2.tool_name_3.output_param_3",
            "input_param_2": "$ref.stage_1.tool_name_1.output_param_1"
        }}
        ...
    }}

    HERE IS YOUR TOOLBOX:
    --------------------------------
    {toolbox}
    --------------------------------

    HERE IS YOUR BLUEPRINT RACK:
    --------------------------------
    {blueprint_rack}
    --------------------------------

    CRITICAL INSTRUCTIONS:
    - NEVER use any input or output parameter names for tools or blueprints that are not explicitly listed in the toolbox or the blueprint rack, respectively.
    - NEVER produce an incomplete output or use any placeholders of your own invention. If you are unable to call a tool or fill a blueprint accurately, you still must make sure that your build plan will compile successfully.
    - Input parameters can be simple values, strings with embedded references, lists containing mixed values and references, or nested structures. References using $ref.stage.tool.output format will be resolved recursively.
    - NEVER try to index a variable like $ref.stage_1.tool_1.output_list[0:2] - references cannot be sliced.
    - ALWAYS use only the precise tool names from the toolbox. However, if the you must call the same tool multiple times in thesame stage, append _X to the tool name, where X is the index of the tool call.
    - ALWAYS use only the precise blueprint names from the blueprint rack. However, if the you must call the same blueprint multiple times in thesame stage, append _X to the blueprint name, where X is the index of the blueprint call.
    - Note that for string data type input parameters for tools or blueprints, you can include multiple references to the same or different tools embedded in the string. 
    - Additionally, you are allowed to references nested parameters of tool outputs by using dot notation like: $ref.stage_1.tool_1.output_param_1.nested_param_1.
    - You may also use the following syntax to reference a list index: $ref.stage_1.tool_1.output_param_1[0]. Negative indices are also allowed, but you MAY NOT splice or do any other complex operations.
    - You can do deep nested references like $ref.stage_1.tool_1.output_param_1.nested_param_1.nested_param_list_2[0].nested_param_3 if needed, but keep things simple when possible.
    - DO NOT include any fancy references using operations I have not approved you for, such as splicing.
    - NEVER include blueprints within stages. They can ONLY be top level keys no matter what.
    - NEVER reference the same stage within that stage (for example a tool in stage 2 cannot reference another tool in stage 2). You must separate the call into another stage.
    - NEVER include a blueprint inside of a stage. EVER!

    ADDITIONAL FORMATTING EXAMPLE FOR REFERENCE:
    --------------------------------
    {{
        "stage_1": {{
            "tool_name_1": {{
                "input_param_1": "text_value_1",
            }}
            ...
        }}
        "stage_2": {{
            "tool_name_2": {{
                "input_param_1": "$ref.stage_1.tool_name_1.output_param_1",
                "input_param_2": "$ref.stage_1.tool_name_1.output_param_list[0].nested_param_in_list_1[-1][1]"
            }}
            "tool_name_3": {{
                "input_param_1": "text_value_1",
            }}
            ...
        }}
        ...
        "blueprint_1": {{
            "input_param_1": "text_value_1",
            "input_param_2": "$ref.stage_2.tool_name_2.output_param_1"
        }}
        "blueprint_2": {{
            "input_param_1": "$ref.stage_2.tool_name_3.output_param_3",
            "input_param_2": "$ref.stage_1.tool_name_1.output_param_1"
        }}
        ...
    }}
    --------------------------------

    """

    build_plan_additional_context_prompt_wrapper = """
    URGENT UPDATE: The product owner has provided additional information! All new information should be utilized as needed, and any new instructions must be followed exactly. Do your best to fulfill all requirements, which will generally be possible, but in the event of a contradiction, these updates must take precedence over the original requirements:

    --------------------------------
    {additional_context_prompt}
    --------------------------------

    Regardless of any new information, you must still return a valid build plan that will compile successfully according to the previous formatting instructions.
    """

    build_plan_previous_attempt_error_message_prompt_wrapper = """
    CORRECTION NEEDED: The product owner has informed us that on the previous attempt to generate and executea build plan, the following error message was returned:
    --------------------------------
    {previous_attempt_error_message}
    --------------------------------
    
    This error message should be taken into account when generating the next build plan to avoid making the same mistake. Never include details from this message in the build plan, but use it to guide the structure of the build plan so that the same error doesn't happen again.
    """

    user_prompt_wrapper = """
    Hi, Arch. Product owner here. Generate a build plan for the following customer request:
    --------------------------------
    {customer_request}
    --------------------------------

    Here is the conversation history with the customer:
    --------------------------------
    {conversation_history}
    --------------------------------

    And once again here is the initial request that you should focus on fulfilling:
    --------------------------------
    {customer_request}
    --------------------------------
    """

    def __init__(
        self,
        client: Client,
        model_name: str,
        toolbox: ToolBox,
        blueprint_rack: BlueprintRack,
        initial_concurrent_executables: Optional[List[ConcurrentExecutable]] = None,
        asyncio_event_loop: Optional[asyncio.AbstractEventLoop] = None,
        thread_pool_executor: Optional[ThreadPoolExecutor] = None,
        process_pool_executor: Optional[ProcessPoolExecutor] = None,
        enable_streaming_execution: bool = False,
    ):
        """
        Initialize the Architect with required components and execution backends.
        
        Args:
            client (Client): Client class instance for communicating with an LLM provider
            model_name (str): Name of the AI model to use
            toolbox (ToolBox): Collection of available tools
            blueprint_rack (BlueprintRack): Collection of available blueprints
            initial_concurrent_executables (Optional[List[ConcurrentExecutable]]): Initial executables to start
            asyncio_event_loop (Optional[asyncio.AbstractEventLoop]): Event loop for async operations
            thread_pool_executor (Optional[ThreadPoolExecutor]): Thread pool for concurrent execution
            process_pool_executor (Optional[ProcessPoolExecutor]): Process pool for concurrent execution
            enable_streaming_execution (bool): Enable streaming JSON parsing and execution
            
        Returns:
            None: Initializes the architect instance
        """
        if not any([asyncio_event_loop, thread_pool_executor, process_pool_executor]):
            raise ValueError("At least one execution backend must be provided")
        self.client: Client = client
        self.toolbox: ToolBox = toolbox
        self.blueprint_rack: BlueprintRack = blueprint_rack
        self.concurrent_executables: List[ConcurrentExecutable] = (
            initial_concurrent_executables
            if initial_concurrent_executables is not None
            else []
        )
        self.initial_concurrent_executables_started: List[ConcurrentExecutable] = []
        self.architect_id = str(uuid.uuid4())
        self.asyncio_event_loop: Optional[asyncio.AbstractEventLoop] = (
            asyncio_event_loop
        )
        self.thread_pool_executor: Optional[ThreadPoolExecutor] = thread_pool_executor
        self.process_pool_executor: Optional[ProcessPoolExecutor] = (
            process_pool_executor
        )
        self.enable_streaming_execution: bool = enable_streaming_execution
        log_with_structure(
            logger,
            "debug",
            "Architect initalized",
            architect_id=self.architect_id,
            toolbox_count=len(self.toolbox.tools),
            blueprint_rack_count=len(self.blueprint_rack.blueprints),
            concurrent_executable_count=len(self.concurrent_executables),
        )

    def _start_concurrent_executables(self):
        """
        Start all concurrent executables and track which ones started successfully.
        
        Args:
            None
            
        Returns:
            None: Modifies initial_concurrent_executables_started list
        """
        for executable in self.concurrent_executables:
            try:
                executable.start()
                self.initial_concurrent_executables_started.append(executable)
            except ExecutableFailedToStartError as start_error:
                log_with_structure(
                    logger,
                    "error",
                    "Failed to start concurrent executable",
                    architect_id=self.architect_id,
                    executable_name=executable.name,
                    error=start_error,
                )
        log_with_structure(
            logger,
            "debug",
            "Concurrent executables started",
            architect_id=self.architect_id,
            executable_count=len(self.initial_concurrent_executables_started),
        )

    def _generate_build(
        self,
        customer_request: str,
        conversation_history: str,
        additional_context_prompt: str,
        build_correlation_id: str,
        start_time: float,
        previous_attempt_error_message: Optional[str] = None,
        number_of_concurrent_requests_per_call_to_client: int = 1,
    ) -> Build:
        """
        Generate a build plan using the AI client and available tools and blueprints.
        
        Args:
            customer_request (str): The customer's request to fulfill
            conversation_history (str): Previous conversation context
            additional_context_prompt (str): Additional context to include
            build_correlation_id (str): Unique ID for tracking this build
            start_time (float): Performance counter start time
            previous_attempt_error_message (Optional[str]): Error from previous attempt if retrying
            number_of_concurrent_requests_per_call_to_client (int): Number of concurrent requests to make
            
        Returns:
            Build: Generated build plan ready for execution
        """
        developer_prompt_base: str = self.build_plan_generation_base_prompt.format(
            toolbox=self.toolbox.open_all_tools(),
            blueprint_rack=self.blueprint_rack.open_all_blueprints(),
        )
        developer_prompt_additional_context: str = (
            self.build_plan_additional_context_prompt_wrapper.format(
                additional_context_prompt=additional_context_prompt,
            )
        )
        developer_prompt_previous_attempt_error_message: Optional[str] = (
            self.build_plan_previous_attempt_error_message_prompt_wrapper.format(
                previous_attempt_error_message=previous_attempt_error_message
            )
            if previous_attempt_error_message
            else None
        )
        user_prompt: str = self.user_prompt_wrapper.format(
            conversation_history=conversation_history,
            customer_request=customer_request,
        )
        messages: List[Dict[str, str]] = (
            self.client.create_messages_for_build_plan_generation(
                developer_prompt_base=developer_prompt_base,
                developer_prompt_additional_context=developer_prompt_additional_context,
                developer_prompt_previous_attempt_error_message=developer_prompt_previous_attempt_error_message,
                user_prompt=user_prompt,
            )
        )
        log_with_structure(
            logger,
            "info",
            "Starting build plan generation",
            architect_id=self.architect_id,
            build_correlation_id=build_correlation_id,
            time_since_generate_response_called=time.perf_counter() - start_time,
            previous_attempt_error_message=previous_attempt_error_message,
        )
        build_plan: str = ""
        plan: str = ""
        if self.enable_streaming_execution:
            build = Build(
                "",
                build_correlation_id,
                streaming_mode=True,
                toolbox=self.toolbox,
                blueprint_rack=self.blueprint_rack,
                concurrent_executables=self.initial_concurrent_executables_started,
                correlation_id=build_correlation_id,
                asyncio_event_loop=self.asyncio_event_loop,
                thread_pool_executor=self.thread_pool_executor,
                process_pool_executor=self.process_pool_executor
            )
            plan = self.client.send_build_plan_generation_request_streaming(
                messages,
                build.stream_stage_callback,
                build.stream_blueprint_callback,
                number_of_concurrent_requests_per_call_to_client,
            )
            build.build_plan = plan
            build.finalize_streaming_execution()
        else:
            plan = self.client.send_build_plan_generation_request(
                messages, number_of_concurrent_requests_per_call_to_client
            )
            build = Build(plan, build_correlation_id)
        build_plan = plan
        log_with_structure(
            logger,
            "info",
            "Build plan generated",
            architect_id=self.architect_id,
            build_correlation_id=build_correlation_id,
            time_since_generate_response_called=time.perf_counter() - start_time,
            build_plan=build_plan,
        )
        return build

    def generate_response(
        self,
        customer_request: str,
        conversation_history: str,
        additional_context_prompt: str,
        max_attempts_to_generate_build_plan: int = 1,
        number_of_concurrent_requests_per_call_to_client: int = 1,
    ) -> Tuple[Build, List[ConcurrentExecutable], List[LazyBlueprint]]:
        """
        Generate and execute a response to the customer request with retry logic.
        
        Args:
            customer_request (str): The customer's request to fulfill
            conversation_history (str): Previous conversation context
            additional_context_prompt (str): Additional context to include
            max_attempts_to_generate_build_plan (int): Maximum retry attempts
            number_of_concurrent_requests_per_call_to_client (int): Number of concurrent requests to make
            
        Returns:
            Tuple[Build, List[ConcurrentExecutable], List[LazyBlueprint]]: Build result, started executables, and lazy blueprints
        """
        build_correlation_id: str = str(uuid.uuid4())
        start_time: float = time.perf_counter()
        self._start_concurrent_executables()
        previous_attempt_error_message: Optional[str] = None
        for attempt in range(max_attempts_to_generate_build_plan):
            try:
                build: Build = self._generate_build(
                    customer_request,
                    conversation_history,
                    additional_context_prompt,
                    build_correlation_id,
                    start_time,
                    previous_attempt_error_message,
                    number_of_concurrent_requests_per_call_to_client,
                )
                log_with_structure(
                    logger,
                    "debug",
                    "Build plan ready",
                    architect_id=self.architect_id,
                    build_correlation_id=build_correlation_id,
                    build_plan_preview=build.build_plan[:200]
                )
                if not self.enable_streaming_execution:
                    build_start_time = time.perf_counter()
                    build.run(
                        self.toolbox,
                        self.blueprint_rack,
                        self.initial_concurrent_executables_started,
                        build_correlation_id,
                        self.asyncio_event_loop,
                        self.thread_pool_executor,
                        self.process_pool_executor
                    )
                    build_execution_time = time.perf_counter() - build_start_time
                    log_with_structure(
                        logger,
                        "debug",
                        f"Build execution completed in {build_execution_time} seconds",
                        architect_id=self.architect_id,
                        build_correlation_id=build_correlation_id,
                        build_execution_time_seconds=build_execution_time,
                        time_since_generate_response_called=time.perf_counter() - start_time,
                    )
                lazy_blueprints = build.get_lazy_blueprints() or []
                return build, self.initial_concurrent_executables_started, lazy_blueprints
            except Exception as build_error:
                log_with_structure(
                    logger,
                    "error",
                    "Failed to generate or execute build plan",
                    architect_id=self.architect_id,
                    build_correlation_id=build_correlation_id,
                    time_since_generate_response_called=time.perf_counter()
                    - start_time,
                    max_attempts_to_generate_build_plan=max_attempts_to_generate_build_plan,
                    current_attempt=attempt + 1,
                    exception_type=type(build_error).__name__,
                    exception_message=str(build_error),
                    error=build_error,
                )
                logger.error("Full build execution failure traceback:", exc_info=True)
                if attempt < max_attempts_to_generate_build_plan - 1:
                    log_with_structure(
                        logger,
                        "info",
                        "Retrying build plan generation",
                        architect_id=self.architect_id,
                        build_correlation_id=build_correlation_id,
                        time_since_generate_response_called=time.perf_counter()
                        - start_time,
                        max_attempts_to_generate_build_plan=max_attempts_to_generate_build_plan,
                        current_attempt=attempt + 1,
                        error=build_error,
                    )
                    previous_attempt_error_message = str(build_error)

        log_with_structure(
            logger,
            "error",
            "Failed to generate build plan after max attempts",
            architect_id=self.architect_id,
            build_correlation_id=build_correlation_id,
            time_since_generate_response_called=time.perf_counter() - start_time,
            max_attempts_to_generate_build_plan=max_attempts_to_generate_build_plan,
        )
        failed_build = Build("", build_correlation_id)
        return failed_build, self.initial_concurrent_executables_started, []
