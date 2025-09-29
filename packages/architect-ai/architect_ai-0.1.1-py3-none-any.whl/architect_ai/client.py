"""Client wrapper for API calls."""

import asyncio
import logging
from typing import List, Dict, Any, Optional
from concurrent.futures import Future
from openai import AsyncOpenAI, OpenAI
from enum import Enum
from openai.types.chat import ChatCompletion
from concurrent.futures import wait, FIRST_COMPLETED

from .logging_utils import log_structured as log_with_structure

logger = logging.getLogger(__name__)


class ClientType(Enum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"


class Client:
    """Wrapper for an LLM API client with build plan generation methods."""

    def __init__(
        self, client_type: ClientType, client_api_key: str, use_async: bool, model_name: str, asyncio_event_loop: Optional[asyncio.AbstractEventLoop] = None, token_limit: Optional[int] = None
    ):
        """Initialize with AsyncOpenAI client."""
        if use_async and asyncio_event_loop is None:
            raise ValueError("Asyncio event loop is required for asyncio execution")
        self.client_type = client_type
        self.client_api_key = client_api_key
        self.model_name = model_name
        self.use_async = use_async
        self.asyncio_event_loop = asyncio_event_loop
        self.token_limit = token_limit
        self.connected_client = self.initialize_connected_client(use_async)
        log_with_structure(logger, "debug", "Client initialized", client_type=client_type.value, use_async=use_async, model_name=model_name, token_limit=token_limit)

    def initialize_connected_client(self, use_async: bool) -> Any:
        """Initialize the connected client."""
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
        """Create messages for build plan generation."""
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
        """Send request to connected OpenAI client."""
        log_with_structure(logger, "debug", "Sending request to OpenAI", use_async=self.use_async, model=self.model_name)
        if self.use_async:
            if asyncio_event_loop is None:
                raise ValueError("Asyncio event loop is required for asyncio execution")
            log_with_structure(logger, "debug", "Creating async OpenAI request")
            # Build API call parameters
            api_params = {
                "model": self.model_name,
                "messages": messages,
                "temperature": 0.1,
                "response_format": { "type": "json_object" }
            }
            if self.token_limit is not None:
                api_params["max_tokens"] = self.token_limit
            
            async_response: Future[ChatCompletion] = asyncio.run_coroutine_threadsafe(
                self.connected_client.chat.completions.create(**api_params),
                asyncio_event_loop
            )
            log_with_structure(logger, "debug", "Waiting for async OpenAI response")
            result = async_response.result().choices[0].message.content or ""
            log_with_structure(logger, "debug", "Received async OpenAI response", response_length=len(result))
            return result
        else:
            log_with_structure(logger, "debug", "Creating sync OpenAI request")
            # Build API call parameters
            api_params = {
                "model": self.model_name,
                "messages": messages,
                "temperature": 0.1,
                "response_format": { "type": "json_object" }
            }
            if self.token_limit is not None:
                api_params["max_tokens"] = self.token_limit
                
            sync_response: ChatCompletion = self.connected_client.chat.completions.create(**api_params)
            result = sync_response.choices[0].message.content or ""
            log_with_structure(logger, "debug", "Received sync OpenAI response", response_length=len(result))
            return result

    def send_request_to_connected_client(self, messages: List[Dict[str, str]], asyncio_event_loop: Optional[asyncio.AbstractEventLoop] = None) -> str:
        """Send request to connected client."""
        if self.client_type == ClientType.OPENAI:
            return self.send_request_to_connected_openai_client(messages, asyncio_event_loop)
        else:
            raise ValueError(f"Unsupported client type: {self.client_type}")

    async def send_request_to_connected_client_async(self, messages: List[Dict[str, str]]) -> str:
        """Send request to connected client asynchronously."""
        log_with_structure(logger, "debug", "Sending async request to connected client")
        if self.client_type == ClientType.OPENAI:
            # Build API call parameters
            api_params = {
                "model": self.model_name,
                "messages": messages,
                "temperature": 0.1,
                "response_format": { "type": "json_object" }
            }
            if self.token_limit is not None:
                api_params["max_tokens"] = self.token_limit
                
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
        """Send build plan generation request to OpenAI."""
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
        for i in range(number_of_concurrent_requests):
            log_with_structure(logger, "debug", "Creating concurrent request", request_index=i)
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

