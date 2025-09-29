"""Client wrapper for API calls."""

import asyncio
import logging
from typing import List, Dict, Any, Optional, Set, Callable
from concurrent.futures import Future
from openai import AsyncOpenAI, OpenAI
from enum import Enum
from openai.types.chat import ChatCompletion
from concurrent.futures import wait, FIRST_COMPLETED
import importlib
try:
    json = importlib.import_module("ujson")
except Exception:
    import json as json

from .logging_utils import log_structured as log_with_structure

logger = logging.getLogger(__name__)


class ClientType(Enum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"


class Client:
    """Wrapper for an LLM API client with build plan generation methods."""

    def __init__(
        self, client_type: ClientType, client_api_key: str, use_async: bool, model_name: str, asyncio_event_loop: Optional[asyncio.AbstractEventLoop] = None, token_limit: Optional[int] = None, prompt_cache_key: Optional[str] = None
    ):
        """
        Initialize the client with API credentials and configuration.
        
        Args:
            client_type (ClientType): Type of client to use (OpenAI, Anthropic)
            client_api_key (str): API key for the client
            use_async (bool): Whether to use asynchronous operations
            model_name (str): Name of the model to use
            asyncio_event_loop (Optional[asyncio.AbstractEventLoop]): Event loop for async operations
            token_limit (Optional[int]): Maximum number of tokens to use
            prompt_cache_key (Optional[str]): Cache key for prompt caching optimization
            
        Returns:
            None: Initializes the client instance
        """
        if use_async and asyncio_event_loop is None:
            raise ValueError("Asyncio event loop is required for asyncio execution")
        self.client_type = client_type
        self.client_api_key = client_api_key
        self.model_name = model_name
        self.use_async = use_async
        self.asyncio_event_loop = asyncio_event_loop
        self.token_limit = token_limit
        self.prompt_cache_key = prompt_cache_key or "build_plan_generation"
        self.connected_client = self.initialize_connected_client(use_async)
        log_with_structure(logger, "debug", "Client initialized", client_type=client_type.value, use_async=use_async, model_name=model_name, token_limit=token_limit, prompt_cache_key=self.prompt_cache_key)

    def initialize_connected_client(self, use_async: bool) -> Any:
        """
        Initialize the appropriate client based on client type and async preference.
        
        Args:
            use_async (bool): Whether to create an async or sync client
            
        Returns:
            Any: AsyncOpenAI or OpenAI client instance based on configuration
        """
        if self.client_type == ClientType.OPENAI:
            return (
                AsyncOpenAI(api_key=self.client_api_key)
                if use_async
                else OpenAI(api_key=self.client_api_key)
            )
        else:
            raise ValueError(f"Unsupported client type: {self.client_type}")

    def create_messages_for_build_plan_generation(
        self,
        developer_prompt_base: str,
        developer_prompt_additional_context: Optional[str] = None,
        developer_prompt_previous_attempt_error_message: Optional[str] = None,
        user_prompt: str = "",
    ) -> List[Dict[str, str]]:
        """
        Create structured messages array for build plan generation API call.
        
        Args:
            developer_prompt_base (str): Base system prompt for the developer role
            developer_prompt_additional_context (Optional[str]): Additional context if provided
            developer_prompt_previous_attempt_error_message (Optional[str]): Error from previous attempt
            user_prompt (str): User's request prompt
            
        Returns:
            List[Dict[str, str]]: Formatted messages array for API call
        """
        log_with_structure(logger, "debug", "Creating messages for build plan generation", user_prompt_length=len(user_prompt))
        if self.client_type == ClientType.OPENAI:
            messages = [{"role": "developer", "content": developer_prompt_base}]
            if developer_prompt_additional_context:
                messages.append(
                    {
                        "role": "developer",
                        "content": developer_prompt_additional_context,
                    }
                )
            if developer_prompt_previous_attempt_error_message:
                messages.append(
                    {
                        "role": "developer",
                        "content": developer_prompt_previous_attempt_error_message,
                    }
                )
            if user_prompt:
                messages.append({"role": "user", "content": user_prompt})
            else:
                raise ValueError("User prompt is required")
        else:
            raise ValueError(f"Unsupported client type: {self.client_type}")
        log_with_structure(logger, "debug", "Messages created for build plan generation", message_count=len(messages))
        return messages

    def send_request_to_connected_openai_client(self, messages: List[Dict[str, str]], asyncio_event_loop: Optional[asyncio.AbstractEventLoop] = None) -> str:
        """
        Send request to OpenAI client using sync or async mode based on configuration.
        
        Args:
            messages (List[Dict[str, str]]): Formatted messages for API call
            asyncio_event_loop (Optional[asyncio.AbstractEventLoop]): Event loop for async operations
            
        Returns:
            str: Response content from OpenAI API
        """
        log_with_structure(logger, "debug", "Sending request to OpenAI", use_async=self.use_async, model=self.model_name)
        if self.use_async:
            if asyncio_event_loop is None:
                raise ValueError("Asyncio event loop is required for asyncio execution")
            log_with_structure(logger, "debug", "Creating async OpenAI request")
            api_params = {
                "model": self.model_name,
                "messages": messages,
                "temperature": 0.0,
                "response_format": { "type": "json_object" },
                "service_tier": "priority",
                "timeout": 60.0
            }
            if self.token_limit is not None:
                api_params["max_completion_tokens"] = self.token_limit
            if self.prompt_cache_key:
                api_params["prompt_cache_key"] = self.prompt_cache_key
            try:
                async_response: Future[ChatCompletion] = asyncio.run_coroutine_threadsafe(
                    self.connected_client.chat.completions.create(**api_params),
                    asyncio_event_loop
                )
            except TypeError as cache_error:
                if "prompt_cache_key" in str(cache_error) and self.prompt_cache_key:
                    log_with_structure(logger, "warning", "prompt_cache_key not supported, retrying without", error=str(cache_error))
                    api_params.pop("prompt_cache_key", None)
                    async_response: Future[ChatCompletion] = asyncio.run_coroutine_threadsafe(
                        self.connected_client.chat.completions.create(**api_params),
                        asyncio_event_loop
                    )
                else:
                    raise
            log_with_structure(logger, "debug", "Waiting for async OpenAI response")
            result = async_response.result().choices[0].message.content or ""
            log_with_structure(logger, "debug", "Received async OpenAI response", response_length=len(result))
            return result
        else:
            log_with_structure(logger, "debug", "Creating sync OpenAI request")
            api_params = {
                "model": self.model_name,
                "messages": messages,
                "temperature": 0.0,
                "response_format": { "type": "json_object" },
                "service_tier": "priority",
                "timeout": 60.0
            }
            if self.token_limit is not None:
                api_params["max_completion_tokens"] = self.token_limit
            sync_response: ChatCompletion = self.connected_client.chat.completions.create(**api_params)
            result = sync_response.choices[0].message.content or ""
            log_with_structure(logger, "debug", "Received sync OpenAI response", response_length=len(result))
            return result

    def send_request_to_connected_client(self, messages: List[Dict[str, str]], asyncio_event_loop: Optional[asyncio.AbstractEventLoop] = None) -> str:
        """
        Send request to the connected client based on client type.
        
        Args:
            messages (List[Dict[str, str]]): Formatted messages for API call
            asyncio_event_loop (Optional[asyncio.AbstractEventLoop]): Event loop for async operations
            
        Returns:
            str: Response content from the API
        """
        if self.client_type == ClientType.OPENAI:
            return self.send_request_to_connected_openai_client(messages, asyncio_event_loop)
        else:
            raise ValueError(f"Unsupported client type: {self.client_type}")

    async def send_request_to_connected_client_async(self, messages: List[Dict[str, str]]) -> str:
        """
        Send request to connected client using native async operations.
        
        Args:
            messages (List[Dict[str, str]]): Formatted messages for API call
            
        Returns:
            str: Response content from the API
        """
        log_with_structure(logger, "debug", "Sending async request to connected client")
        if self.client_type == ClientType.OPENAI:
            api_params = {
                "model": self.model_name,
                "messages": messages,
                "temperature": 0.0,
                "response_format": { "type": "json_object" },
                "service_tier": "priority",
                "timeout": 60.0
            }
            if self.token_limit is not None:
                api_params["max_completion_tokens"] = self.token_limit
            response: ChatCompletion = await self.connected_client.chat.completions.create(**api_params)
            result = response.choices[0].message.content or ""
            log_with_structure(logger, "debug", "Received async client response", response_length=len(result))
            return result
        else:
            raise ValueError(f"Unsupported client type: {self.client_type}")

    def send_build_plan_generation_request(
        self,
        messages: List[Dict[str, str]],
        number_of_concurrent_requests: int = 1,
    ) -> str:
        """
        Send build plan generation request with optional concurrent execution.
        
        Args:
            messages (List[Dict[str, str]]): Formatted messages for API call
            number_of_concurrent_requests (int): Number of concurrent requests to make
            
        Returns:
            str: First successful response from concurrent requests
        """
        log_with_structure(logger, "debug", "Starting build plan generation request", concurrent_requests=number_of_concurrent_requests)
        if number_of_concurrent_requests == 1:
            log_with_structure(logger, "debug", "Using single request mode")
            result = self.send_request_to_connected_client(messages, self.asyncio_event_loop)
            log_with_structure(logger, "debug", "Build plan generation request completed", result_length=len(result))
            return result
        log_with_structure(logger, "debug", "Using concurrent request mode")
        if self.asyncio_event_loop is None:
            raise ValueError("Asyncio event loop is required when number_of_concurrent_requests > 1")
        futures = []
        for request_index in range(number_of_concurrent_requests):
            log_with_structure(logger, "debug", "Creating concurrent request", request_index=request_index)
            future: Future[str] = asyncio.run_coroutine_threadsafe(
                self.send_request_to_connected_client_async(messages),
                self.asyncio_event_loop
            )
            futures.append(future)
        log_with_structure(logger, "debug", "Waiting for first concurrent request to complete")
        done, pending = wait(futures, return_when=FIRST_COMPLETED)
        log_with_structure(logger, "debug", "First concurrent request completed, cancelling others", pending_count=len(pending))
        for future in pending:
            future.cancel()
        completed_future = list(done)[0]
        result = completed_future.result()
        log_with_structure(logger, "debug", "Concurrent build plan generation completed", result_length=len(result))
        return result

    def send_build_plan_generation_request_streaming(
        self,
        messages: List[Dict[str, str]],
        stage_callback: Callable[[str, Dict[str, Any]], None],
        blueprint_callback: Optional[Callable[[str, Dict[str, Any]], None]] = None,
        number_of_concurrent_requests: int = 1,
    ) -> str:
        """
        Send streaming build plan generation request with stage-by-stage execution callbacks.
        
        Args:
            messages (List[Dict[str, str]]): Formatted messages for API call
            stage_callback (Callable[[str, Dict[str, Any]], None]): Called when complete stages are detected in stream
            blueprint_callback (Optional[Callable[[str, Dict[str, Any]], None]]): Called when complete blueprints are detected in stream
            number_of_concurrent_requests (int): Number of concurrent requests to make
            
        Returns:
            str: Complete response content from API
        """
        log_with_structure(logger, "debug", "Starting streaming build plan generation request", concurrent_requests=number_of_concurrent_requests)
        if number_of_concurrent_requests > 1:
            raise ValueError("Streaming mode does not support concurrent requests")
        if self.client_type != ClientType.OPENAI:
            raise ValueError("Streaming only supported for OpenAI client type")
        log_with_structure(logger, "debug", "Using streaming request mode")
        api_params = {
            "model": self.model_name,
            "messages": messages,
            "temperature": 0.0,
            "response_format": {"type": "json_object"},
            "stream": True,
            "service_tier": "priority",
            "timeout": 60.0
        }
        if self.token_limit is not None:
            api_params["max_completion_tokens"] = self.token_limit
        if self.use_async:
            if self.asyncio_event_loop is None:
                raise ValueError("Asyncio event loop is required for asyncio execution")
            return self._stream_async_request(api_params, stage_callback, blueprint_callback)
        else:
            return self._stream_sync_request(api_params, stage_callback, blueprint_callback)

    def _stream_sync_request(self, api_params: Dict[str, Any], stage_callback: Callable[[str, Dict[str, Any]], None], blueprint_callback: Optional[Callable[[str, Dict[str, Any]], None]]) -> str:
        """
        Handle streaming sync request with incremental JSON parsing.
        
        Args:
            api_params (Dict[str, Any]): API parameters for the request
            stage_callback (Callable[[str, Dict[str, Any]], None]): Callback for complete stages
            blueprint_callback (Optional[Callable[[str, Dict[str, Any]], None]]): Callback for complete blueprints
            
        Returns:
            str: Complete response content
        """
        full_content = ""
        parsed_stages: Set[str] = set()
        parsed_blueprints: Set[str] = set()
        stream = self.connected_client.chat.completions.create(**api_params)
        for chunk in stream:
            if chunk.choices[0].delta.content:
                content_piece = chunk.choices[0].delta.content
                full_content += content_piece
                if "}" in content_piece:
                    self._check_for_complete_objects(full_content, parsed_stages, stage_callback, parsed_blueprints, blueprint_callback)
        return full_content

    def _stream_async_request(self, api_params: Dict[str, Any], stage_callback: Callable[[str, Dict[str, Any]], None], blueprint_callback: Optional[Callable[[str, Dict[str, Any]], None]]) -> str:
        """
        Handle streaming async request with incremental JSON parsing.
        
        Args:
            api_params (Dict[str, Any]): API parameters for the request
            stage_callback (Callable[[str, Dict[str, Any]], None]): Callback for complete stages
            blueprint_callback (Optional[Callable[[str, Dict[str, Any]], None]]): Callback for complete blueprints
            
        Returns:
            str: Complete response content
        """
        async def stream_coroutine():
            full_content = ""
            parsed_stages: Set[str] = set()
            parsed_blueprints: Set[str] = set()
            stream = await self.connected_client.chat.completions.create(**api_params)
            async for chunk in stream:
                if chunk.choices[0].delta.content:
                    content_piece = chunk.choices[0].delta.content
                    full_content += content_piece
                    if "}" in content_piece:
                        self._check_for_complete_objects(full_content, parsed_stages, stage_callback, parsed_blueprints, blueprint_callback)
            return full_content
        if self.asyncio_event_loop is None:
            raise ValueError("Asyncio event loop is required for asyncio execution")
        future = asyncio.run_coroutine_threadsafe(stream_coroutine(), self.asyncio_event_loop)
        return future.result()

    def _check_for_complete_objects(self, content: str, parsed_stages: Set[str], stage_callback: Callable[[str, Dict[str, Any]], None], parsed_blueprints: Set[str], blueprint_callback: Optional[Callable[[str, Dict[str, Any]], None]]) -> None:
        """
        Check content for complete top-level objects (stages and blueprints) and trigger callbacks.
        
        Args:
            content (str): Current accumulated content
            parsed_stages (Set[str]): Set of already parsed stage names
            stage_callback (Callable[[str, Dict[str, Any]], None]): Callback to invoke for new complete stages
            parsed_blueprints (Set[str]): Set of already parsed blueprint names
            blueprint_callback (Optional[Callable[[str, Dict[str, Any]], None]]): Callback for new complete blueprints
            
        Returns:
            None: Calls callbacks for newly detected complete objects
        """
        found_objects = list(self._iter_top_level_objects(content))
        for key_name, obj_text in found_objects:
            if key_name.startswith("stage_"):
                if key_name in parsed_stages:
                    continue
                try:
                    wrapped = "{" + f'"{key_name}":' + obj_text + "}"
                    parsed = json.loads(wrapped)
                    parsed_stages.add(key_name)
                    stage_callback(key_name, parsed[key_name])
                    log_with_structure(logger, "debug", "Streaming stage detected, starting execution", stage_name=key_name)
                except Exception:
                    continue
            else:
                if blueprint_callback is None or key_name in parsed_blueprints:
                    continue
                try:
                    wrapped = "{" + f'"{key_name}":' + obj_text + "}"
                    parsed = json.loads(wrapped)
                    parsed_blueprints.add(key_name)
                    blueprint_callback(key_name, parsed[key_name])
                    log_with_structure(logger, "debug", "Streaming blueprint detected, processing", blueprint_name=key_name)
                except Exception:
                    continue

    def _iter_top_level_objects(self, content: str):
        """
        Iterate complete top-level JSON key/object pairs from a partial or complete JSON document.
        
        Args:
            content (str): Accumulated JSON text
        
        Yields:
            Tuple[str, str]: Key name and raw JSON object text for that key
        """
        content = content.strip()
        if not content or not content.startswith('{'):
            return
        position = 1
        content_length = len(content)
        while position < content_length:
            position = self._skip_whitespace(content, position)
            if position >= content_length or content[position] == '}':
                break
            key, position = self._parse_json_key(content, position)
            if key is None:
                break
            position = self._skip_to_value(content, position)
            if position >= content_length:
                break
            if content[position] != '{':
                position = self._skip_non_object_value(content, position)
                continue
            obj_value, position = self._parse_object_value(content, position)
            if obj_value is not None:
                yield key, obj_value

    def _skip_whitespace(self, content: str, position: int) -> int:
        """
        Skip whitespace characters from current position.
        
        Args:
            content (str): JSON content string
            position (int): Current position in content
            
        Returns:
            int: New position after skipping whitespace
        """
        while position < len(content) and content[position].isspace():
            position += 1
        return position

    def _parse_json_key(self, content: str, position: int) -> tuple:
        """
        Parse JSON key from current position.
        
        Args:
            content (str): JSON content string
            position (int): Current position in content
            
        Returns:
            tuple: (key_name, new_position) or (None, position) if parsing fails
        """
        if content[position] != '"':
            return None, position
        position += 1
        key_start = position
        while position < len(content) and content[position] != '"':
            if content[position] == '\\':
                position += 2
            else:
                position += 1
        if position >= len(content):
            return None, position
        key = content[key_start:position]
        position += 1
        return key, position

    def _skip_to_value(self, content: str, position: int) -> int:
        """
        Skip whitespace and colon to reach the value part.
        
        Args:
            content (str): JSON content string
            position (int): Current position in content
            
        Returns:
            int: Position at start of value or end of content
        """
        position = self._skip_whitespace(content, position)
        if position >= len(content) or content[position] != ':':
            return len(content)
        position += 1
        return self._skip_whitespace(content, position)

    def _skip_non_object_value(self, content: str, position: int) -> int:
        """
        Skip over non-object JSON values.
        
        Args:
            content (str): JSON content string
            position (int): Current position in content
            
        Returns:
            int: Position after the skipped value
        """
        nesting_depth = 0
        inside_string = False
        while position < len(content):
            current_char = content[position]
            if inside_string:
                if current_char == '"' and (position == 0 or content[position-1] != '\\'):
                    inside_string = False
            else:
                if current_char == '"':
                    inside_string = True
                elif current_char in ['{', '[']:
                    nesting_depth += 1
                elif current_char in ['}', ']']:
                    nesting_depth -= 1
                elif current_char == ',' and nesting_depth == 0:
                    position += 1
                    break
                elif current_char == '}' and nesting_depth == -1:
                    break
            position += 1
        return position

    def _parse_object_value(self, content: str, position: int) -> tuple:
        """
        Parse complete JSON object value from current position.
        
        Args:
            content (str): JSON content string
            position (int): Current position in content
            
        Returns:
            tuple: (object_text, new_position) or (None, position) if incomplete
        """
        obj_start = position
        brace_nesting = 0
        inside_string = False
        while position < len(content):
            current_char = content[position]
            if inside_string:
                if current_char == '"' and (position == 0 or content[position-1] != '\\'):
                    inside_string = False
            else:
                if current_char == '"':
                    inside_string = True
                elif current_char == '{':
                    brace_nesting += 1
                elif current_char == '}':
                    brace_nesting -= 1
                    if brace_nesting == 0:
                        obj_end = position + 1
                        obj_value = content[obj_start:obj_end]
                        position = self._skip_whitespace(content, obj_end)
                        if position < len(content) and content[position] == ',':
                            position += 1
                        return obj_value, position
            position += 1
        return None, position

