from pydantic import BaseModel, Field
from enum import Enum
from typing import Dict, List, Optional, Union, Literal, Any
from openai._types import NotGiven, NOT_GIVEN
from openai.types.shared.chat_model import ChatModel

class Verdict(str, Enum):
    FACTUALLY_TRUE = "factually true"
    FACTUALLY_FALSE = "factually false"
    PARTIALLY_TRUE = "partially true"
    PARTIALLY_FALSE = "partially false"
    NOT_ENOUGH_INFO = "not enough info"

# Available evaluation metrics for post-normalization quality audits
AVAILABLE_EVAL_METRICS = [
    "G-Eval",
    "Bias",
    "Hallucinations",
    "Hallucination Coverage",
    "Factual Accuracy",
    "Relevance",
    "Coherence"
]

# Type alias for evaluation metrics
EvaluationMetric = Literal[
    "G-Eval",
    "Bias",
    "Hallucinations",
    "Hallucination Coverage",
    "Factual Accuracy",
    "Relevance",
    "Coherence"
]

StructuredOutputModels = [
    # OpenAI models
    "gpt-5-2025-08-07", "gpt-5-nano-2025-08-07", "o3-2025-04-16", "o4-mini-2025-04-16",
    "gpt-4o-2024-08-06", "gpt-4o-mini-2024-07-18", "gpt-4o-2024-11-20",
    "gpt-4o-mini", "gpt-4o", "gpt-4", "gpt-4-turbo",
    # Gemini models
    "gemini-2.5-pro", "gemini-2.5-flash", "gemini-1.5-pro", "gemini-1.5-flash",
    # xAI models (Grok supports structured outputs)
    "grok-3", "grok-4-0709", "grok-3-mini",
    # Together AI models (some support structured outputs)
    "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
    # Anthropic models (limited structured output support)
    "claude-sonnet-4-20250514"
]

# Comprehensive list of all available models (fallback if backend is unavailable)
ALL_AVAILABLE_MODELS = [
    # OpenAI models
    "gpt-5-2025-08-07", "gpt-5-nano-2025-08-07", "o3-2025-04-16", "o4-mini-2025-04-16",
    "gpt-4o-2024-08-06", "gpt-4o-mini-2024-07-18", "gpt-4o-2024-11-20",
    "gpt-4o-mini", "gpt-4o", "gpt-4", "gpt-4-turbo", "gpt-3.5-turbo",
    # Gemini models
    "gemini-2.5-pro", "gemini-2.5-flash", "gemini-1.5-pro", "gemini-1.5-flash", "gemini-1.0-pro",
    # xAI models
    "grok-3", "grok-4-0709", "grok-3-mini", "grok-beta", "grok-2",
    # Together AI models
    "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free", "meta-llama/Llama-3.1-70B-Instruct",
    "meta-llama/Llama-3.1-8B-Instruct", "meta-llama/Llama-3-70B-Instruct",
    # Anthropic models
    "claude-sonnet-4-20250514", "claude-3-5-sonnet-20241022", "claude-3-haiku-20240307",
    "claude-3-opus-20240229", "claude-3-sonnet-20240229",
]

# Global cache for available models
_AVAILABLE_MODELS_CACHE = set()


def _get_available_models(client) -> List[str]:
    """Fetch available models from the backend."""
    try:
        models_resource = client.models
        models_data = models_resource.list()

        # Extract model IDs from the response
        available_models = []
        for provider_data in models_data.get("models_list", []):
            for model_data in provider_data.get("available_models", []):
                model_id = model_data.get("model_id")
                if model_id:
                    available_models.append(model_id)

        return available_models
    except Exception:
        # Fallback to the hardcoded list if backend is unavailable
        return ALL_AVAILABLE_MODELS


def validate_model(model: Union[str, ChatModel], client) -> None:
    """Validate that the model is available in CheckThat AI."""
    from ._exceptions import InvalidModelError

    if isinstance(model, str):
        model_str = model
    else:
        model_str = str(model)

    # Get available models (cached for performance)
    global _AVAILABLE_MODELS_CACHE
    if not _AVAILABLE_MODELS_CACHE:
        _AVAILABLE_MODELS_CACHE = set(_get_available_models(client))

    if model_str not in _AVAILABLE_MODELS_CACHE:
        available_models_str = "\n  - ".join(sorted(_AVAILABLE_MODELS_CACHE))
        raise InvalidModelError(
            f"Invalid model '{model_str}'. "
            f"To list available models and their API strings, use: client.models.list()",
            model=model_str
        )


def validate_response_format_for_structured_output(
    response_format: Any,
    model: Union[str, ChatModel],
    stream: Union[bool, NotGiven]
) -> None:
    """Validate response_format compatibility with model and stream settings."""
    from ._exceptions import InvalidResponseFormatError

    # Only validate if response_format is provided
    if response_format is NOT_GIVEN:
        return

    # Convert model to string for validation
    if isinstance(model, str):
        model_str = model
    else:
        model_str = str(model)

    # Check if streaming is enabled with structured output
    if stream is not NOT_GIVEN and stream is not False:
        raise InvalidResponseFormatError(
            f"Structured output (response_format) is not compatible with streaming. "
            f"Please set stream=False when using response_format.",
            model=model_str,
            stream=stream
        )

    # Check if model supports structured output
    if model_str not in StructuredOutputModels:
        supported_models_str = "\n  - ".join(sorted(StructuredOutputModels))
        raise InvalidResponseFormatError(
            f"Model '{model_str}' does not support structured output (response_format). "
            f"Supported models for structured output include:\n  - {supported_models_str}",
            model=model_str,
            stream=stream
        )

class OpenAIMessage(BaseModel):
    role: Literal["system", "user", "assistant", "tool"]
    content: Union[str, List[Dict[str, Any]]]
    name: Optional[str] = None
    tool_calls: Optional[List[Dict[str, Any]]] = None
    tool_call_id: Optional[str] = None


__all__ = [
    "EvaluationMetric",
    "AVAILABLE_EVAL_METRICS",
    "OpenAIMessage",
    "StructuredOutputModels",
    "ALL_AVAILABLE_MODELS",
    "validate_model",
    "validate_response_format_for_structured_output",
]