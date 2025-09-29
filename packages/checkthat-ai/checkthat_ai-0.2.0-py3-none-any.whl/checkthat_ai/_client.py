import os
import logging
from typing import Optional, Union, Mapping

import httpx
from openai import OpenAI, AsyncOpenAI
from openai._exceptions import OpenAIError
from openai._base_client import DEFAULT_MAX_RETRIES
from openai._types import NOT_GIVEN
from httpx import Timeout

from .resources.chat import Chat
from .resources.chat import AsyncChat
from .resources.models import Models
from .resources.models import AsyncModels

log: logging.Logger = logging.getLogger(__name__)

class CheckThatAI(OpenAI):
    f"""
    CheckThat AI Python SDK - OpenAI Compatible API Client

    This SDK provides an OpenAI-compatible interface for accessing multiple LLM providers
    through a unified API. An API key is always required for authentication.

    API Key Requirement:
    - Set provider_name_API_KEY as an environment variable where provider_name is one of the following: OPENAI, ANTHROPIC, GEMINI, XAI, TOGETHER, and
    - Pass the environment variable as the api_key parameter directly to the client

    The API key will be passed through to the backend and will be routed to the appropriate
    LLM provider (OpenAI, Anthropic, Gemini, xAI, TogetherAI) based on the selected model.

    Example:
        # Using environment variable
        import os
        api_key = os.environ["OPENAI_API_KEY"]
        
        client = CheckThatAI(
            api_key=api_key,
            base_url="https://api.checkthat-ai.com/v1" # Optional, defaults to https://api.checkthat-ai.com/v1
        )
    """
    chat: Chat
    models: Models

    def __init__(
        self,
        api_key: str = None,
        base_url: Optional[str] = None,
        timeout: Union[float, Timeout, None] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Optional[Mapping[str, str]] = None,
        default_query: Optional[Mapping[str, object]] = None,
        http_client: Optional[httpx.Client] = None,
        **kwargs
    ):
        # If no API key is provided, raise the same error as OpenAI client
        if api_key is None:
            raise OpenAIError(
                "The api_key client option must be set either by passing api_key to the client or by setting one of the following environment variables: OPENAI_API_KEY, ANTHROPIC_API_KEY, GEMINI_API_KEY, XAI_API_KEY, TOGETHER_API_KEY"
            )

        if base_url is None:
            base_url = "https://api.checkthat-ai.com/v1"
            log.debug("base_url not provided, using default: %s", base_url)

        super().__init__(
            api_key=api_key,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
            default_headers=default_headers,
            default_query=default_query,
            http_client=http_client,
            **kwargs,
        )

        self.chat = Chat(self)
        self.models = Models(self)
        log.info("CheckThatAI client initialized")


class AsyncCheckThatAI(AsyncOpenAI):
    """
    Async CheckThat AI Python SDK - OpenAI Compatible Client

    This SDK provides an OpenAI-compatible interface for accessing multiple LLM providers
    through a unified API. An API key is always required for authentication.

    API Key Requirement:
    - Set provider_name_API_KEY as an environment variable where provider_name is one of the following: OPENAI, ANTHROPIC, GEMINI, XAI, TOGETHER, and
    - Pass the environment variable as the api_key parameter directly to the client

    The API key will be passed through to the backend and will be routed to the appropriate
    LLM provider (OpenAI, Anthropic, Gemini, xAI, TogetherAI) based on the selected model.

    Example:
        # Using environment variable
        import os
        api_key = os.environ["OPENAI_API_KEY"]

        client = AsyncCheckThatAI(
            api_key=api_key,
            base_url="https://api.checkthat-ai.com/v1" # Optional, defaults to https://api.checkthat-ai.com/v1
        )
    """
    chat: AsyncChat
    models: AsyncModels

    def __init__(
        self,
        api_key: str = None,
        base_url: Optional[str] = None,
        timeout: Union[float, Timeout, None] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Optional[Mapping[str, str]] = None,
        default_query: Optional[Mapping[str, object]] = None,
        http_client: Optional[httpx.AsyncClient] = None,
        **kwargs
    ):
        # If no API key is provided, raise the same error as OpenAI client
        if api_key is None:
            raise OpenAIError(
                "The api_key client option must be set either by passing api_key to the client or by setting one of the following environment variables: OPENAI_API_KEY, ANTHROPIC_API_KEY, GEMINI_API_KEY, XAI_API_KEY, TOGETHER_API_KEY"
            )

        if base_url is None:
            base_url = "https://api.checkthat-ai.com/v1"
            log.debug("base_url not provided, using default: %s", base_url)

        super().__init__(
            api_key=api_key,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
            default_headers=default_headers,
            default_query=default_query,
            http_client=http_client,
            **kwargs,
        )

        self.chat = AsyncChat(self)
        self.models = AsyncModels(self)
        log.info("AsyncCheckThatAI client initialized")
