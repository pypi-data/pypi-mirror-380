# CheckThat AI Python SDK

[![PyPI version](https://badge.fury.io/py/checkthat-ai.svg)](https://badge.fury.io/py/checkthat-ai)
[![Python Support](https://img.shields.io/pypi/pyversions/checkthat-ai.svg)](https://pypi.org/project/checkthat-ai/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python SDK for the [CheckThat AI](https://checkthat-ai.com) platform's unified LLM API with built-in fact-checking and claim normalization capabilities.

## Features

- 🔄 **Unified LLM Access**: Access **all the latest models** from OpenAI, Anthropic, Google Gemini, xAI, and Together AI through a single API
- 🔍 **Claim Normalization**: Standardize and structure claims for analysis
- ✅ **Fact-Checking**: Built-in claim verification and evidence sourcing
- 🔌 **OpenAI Compatible**: Drop-in replacement for OpenAI Python SDK
- ⚡ **Async Support**: Full async/await support for high-performance applications
- 🛡️ **Type Safety**: Complete type hints for better development experience
- 🆕 **Always Up-to-Date**: Access to the newest models as soon as they're released

## Installation

```bash
pip install checkthat-ai
```

## Quick Start

### Basic Usage

```python
import os
from checkthat_ai import CheckThatAI

# Initialize the client - API key is required
api_key = os.environ.get("OPENAI_API_KEY")  # Must provide an API key
client = CheckThatAI(api_key=api_key)

# IMPORTANT: Always check available models first
models = client.models.list()
print("Available models:", models)

# Use exactly like OpenAI's client with latest models
response = client.chat.completions.create(
    model="gpt-5-2025-08-07",  # Use latest models
    messages=[
        {"role": "user", "content": "What is the capital of France?"}
    ]
)

print(response.choices[0].message.content)
```

### Async Usage

```python
import asyncio
from checkthat_ai import AsyncCheckThatAI

async def main():
    client = AsyncCheckThatAI(api_key="your-api-key")
    
    # Check available models first
    models = await client.models.list()
    
    response = await client.chat.completions.create(
        model="gpt-5-2025-08-07",  # Use latest available models
        messages=[
            {"role": "user", "content": "What is the capital of France?"}
        ]
    )
    
    print(response.choices[0].message.content)

asyncio.run(main())
```

### Streaming Responses

```python
# First, check what models support streaming
models = client.models.list()

response = client.chat.completions.create(
    model="gpt-5-2025-08-07",  # Use latest models
    messages=[{"role": "user", "content": "Tell me a story"}],
    stream=True
)

for chunk in response:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

### Complete Working Example

Here's a comprehensive example showing various SDK features:

```python
import os
import asyncio
from typing import List
from pydantic import BaseModel, Field
from checkthat_ai import CheckThatAI, AsyncCheckThatAI

# Define structured response models
class FactualResponse(BaseModel):
    answer: str = Field(description="The main answer to the question")
    confidence: float = Field(description="Confidence score between 0 and 1")
    sources: List[str] = Field(description="List of authoritative sources")
    key_claims: List[str] = Field(description="Main claims made in the response")

def basic_example():
    """Basic structured output example."""
    client = CheckThatAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    # Always check available models first
    models = client.models.list()
    print("Available models:", len(models["models_list"]), "providers")
    
    # Using the parse() method with latest models for structured output
    completion = client.chat.completions.parse(
        model="gpt-5-2025-08-07",  # Use latest available models
        messages=[
            {"role": "user", "content": "What is the primary cause of climate change?"}
        ],
        response_format=FactualResponse
    )
    
    # Access the parsed response directly
    parsed = completion.choices[0].message.parsed
    print(f"Answer: {parsed.answer}")
    print(f"Confidence: {parsed.confidence}")
    print(f"Sources: {', '.join(parsed.sources)}")

def enhanced_example():
    """Example with claim refinement."""
    client = CheckThatAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    completion = client.chat.completions.parse(
        model="o4-mini-2025-04-16",  # Use latest efficient models
        messages=[{
            "role": "user", 
            "content": "Explain the health effects of air pollution in urban areas"
        }],
        response_format=FactualResponse,
        refine_claims=True,  # Enable claim refinement
        refine_model="gpt-5-2025-08-07",  # Use best model for refinement
        refine_threshold=0.7
    )
    
    parsed = completion.choices[0].message.parsed
    print(f"Enhanced response with {len(parsed.key_claims)} refined claims")

async def async_example():
    """Async usage example."""
    client = AsyncCheckThatAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    # Check available models asynchronously
    models = await client.models.list()
    
    completion = await client.chat.completions.parse(
        model="claude-sonnet-4-20250514",  # Use latest Anthropic models
        messages=[{
            "role": "user",
            "content": "What are the latest developments in renewable energy?"
        }],
        response_format=FactualResponse,
        refine_claims=True
    )
    
    parsed = completion.choices[0].message.parsed
    print(f"Async response: {parsed.answer[:100]}...")

if __name__ == "__main__":
    basic_example()
    enhanced_example()
    asyncio.run(async_example())
```

### Structured Output Generation

Generate structured, type-safe responses using Pydantic models with the dedicated `parse()` method:

```python
from checkthat_ai import CheckThatAI
from pydantic import BaseModel, Field
from typing import List

class MathStep(BaseModel):
    step_number: int = Field(description="The step number")
    explanation: str = Field(description="What happens in this step")
    equation: str = Field(description="The mathematical equation")

class MathSolution(BaseModel):
    problem: str = Field(description="The original problem")
    steps: List[MathStep] = Field(description="Step-by-step solution")
    final_answer: str = Field(description="The final answer")

client = CheckThatAI(api_key="your-api-key")

# Use the parse() method for structured outputs
response = client.chat.completions.parse(
    model="gpt-5-2025-08-07",  # Use latest models that support structured outputs
    messages=[
        {"role": "system", "content": "You are a helpful math tutor."},
        {"role": "user", "content": "Solve: 2x + 5 = 13"}
    ],
    response_format=MathSolution  # Pydantic model for structured output
)

# Access the parsed response directly
solution = response.choices[0].message.parsed
print(f"Problem: {solution.problem}")
print(f"Answer: {solution.final_answer}")
for step in solution.steps:
    print(f"Step {step.step_number}: {step.explanation}")
```

### CheckThat AI Features

The SDK includes several enhancements beyond standard OpenAI compatibility:

#### Claim Refinement
Iteratively improve response accuracy through claim refinement:

```python
response = client.chat.completions.parse(
    model="gpt-5-2025-08-07",  # Use latest models for refinement
    messages=[...],
    response_format=YourModel,
    refine_claims=True,      # Enable refinement
    refine_model="gpt-5-2025-08-07",   # Use best model for refinement process
    refine_threshold=0.7,    # Quality threshold (0.0-1.0)
    refine_max_iters=3       # Maximum refinement iterations
)
```

#### Available Evaluation Metrics
The SDK supports various quality evaluation metrics:

- **G-Eval**: General evaluation framework
- **Bias**: Bias detection and analysis
- **Hallucinations**: Hallucination detection
- **Hallucination Coverage**: Coverage analysis of hallucinations
- **Factual Accuracy**: Fact-checking accuracy
- **Relevance**: Content relevance assessment
- **Coherence**: Response coherence evaluation

```python
# Access available metrics programmatically
from checkthat_ai._types import AVAILABLE_EVAL_METRICS
print("Available metrics:", AVAILABLE_EVAL_METRICS)
```

#### Alternative: JSON Schema Format

You can also use JSON schema format directly with the regular `create()` method:

```python
response = client.chat.completions.create(
    model="o4-mini-2025-04-16",  # Use latest models
    messages=[...],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "math_solution",
            "schema": {
                "type": "object",
                "properties": {
                    "problem": {"type": "string"},
                    "final_answer": {"type": "string"}
                },
                "required": ["problem", "final_answer"]
            }
        }
    }
)

# Parse the JSON response manually
import json
solution_data = json.loads(response.choices[0].message.content)
```

#### Structured Output Features

- **Type Safety**: Full Pydantic model validation with the `parse()` method
- **IDE Support**: Auto-completion and type hints
- **Flexible Schemas**: Support for nested objects, lists, and optional fields
- **Two Approaches**: Use `parse()` for Pydantic models or `create()` with JSON schema
- **Simple Integration**: Automatic JSON schema generation from Pydantic models
- **Async Support**: Available for both sync and async clients
- **Backend Routing**: Automatically routed to appropriate structured output processing
- **Claim Refinement**: Optional iterative improvement of generated content

### Backend Implementation Guide

The SDK automatically handles Pydantic model conversion, so the backend needs to implement **two endpoints** with routing logic:

#### 1. Two Endpoints: `/chat/completions`

```python
# Backend routing logic
def chat_completions_handler(request):
    if 'response_format' in request:
        # Structured output request - route to appropriate handler
        if request.get('parse_mode', False):  # Using parse() method
            return handle_structured_output_parse(request)
        else:  # Using create() with JSON schema
            return handle_structured_output_create(request)
    else:
        # Regular chat request
        return handle_regular_chat(request)
```

#### 2. Structured Output Request Format

For `parse()` method, the backend receives:

```json
{
    "model": "gpt-5-2025-08-07",
    "messages": [
        {"role": "user", "content": "What is 2+2?"}
    ],
    "response_format": {
        "type": "json_schema",
        "json_schema": {
            "name": "my_response",
            "schema": {
                "type": "object",
                "properties": {
                    "answer": {"type": "string"},
                    "confidence": {"type": "number"}
                },
                "required": ["answer", "confidence"]
            }
        }
    },
    "refine_claims": true,
    "refine_model": "gpt-5-2025-08-07",
    "api_key": "user-provided-key"
}
```

#### 3. Response Format

Return standard ChatCompletion format:

```json
{
    "id": "chatcmpl-...",
    "object": "chat.completion",
    "created": 1234567890,
    "model": "gpt-5-2025-08-07",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "{\"answer\": \"4\", \"confidence\": 0.95}"
            },
            "finish_reason": "stop"
        }
    ],
    "usage": {...}
}
```

#### 4. Key Backend Requirements

- **JSON Schema Validation**: Validate and enforce the provided schema
- **Model Support**: Route to appropriate LLM that supports structured outputs
- **Error Handling**: Return appropriate errors for invalid schemas
- **API Key Routing**: Extract `api_key` from request and route to appropriate provider
- **Claim Refinement**: Support optional `refine_claims` and related parameters
- **CheckThat Features**: Handle CheckThat-specific parameters like evaluation metrics

#### 5. CORS Configuration

For same-host development, configure CORS to allow your frontend origin:

```python
# Example CORS configuration (FastAPI/Flask)
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # React dev server
        "http://localhost:8080",  # Vue dev server
        "http://127.0.0.1:3000", # Alternative localhost
        "http://127.0.0.1:8080", # Alternative localhost
        "http://localhost:5173",  # Vite dev server
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)
```

For production, specify your actual domain:

```python
allow_origins=[
    "https://yourdomain.com",
    "https://www.yourdomain.com",
    "https://api.yourdomain.com",  # If using separate API subdomain
]
```

## Supported Models

The SDK provides access to **all the latest models** from multiple providers:

- **OpenAI**: GPT-5, GPT-5 nano, o3, o4-mini, GPT-4o, and more
- **Anthropic**: Claude Sonnet 4, Sonnet Opus 4.1, Claude 3.5 Sonnet, and more
- **Google**: Gemini 2.5 Pro, Gemini 2.5 Flash, Gemini 1.5 Pro, and more
- **xAI**: Grok 4, Grok 3, Grok 3 Mini, and more
- **Together AI**: Llama 3.3 70B, Deepseek R1 Distill Llama 70B, and more

### ⚠️ Important: Always Check Available Models

**Before using any model, query the `/v1/models` endpoint to get the current list of available models:**

```python
# Get the most up-to-date list of available models
models = client.models.list()
print("Available models:")
for provider in models["models_list"]:
    print(f"\n{provider['provider']}:")
    for model in provider["available_models"]:
        print(f"  - {model['name']} ({model['model_id']})")
```

Model availability depends on:
- Your API keys and provider access
- Current provider service status  
- Regional availability
- Your subscription tier with each provider

*The CheckThat AI platform stays up-to-date with the latest model releases from all supported providers.*

## API Reference

### CheckThatAI Client

```python
client = CheckThatAI(
    api_key="your-api-key",           # Required: Your API key (must be provided)
    base_url="https://api.checkthat-ai.com/v1",  # Optional: Custom base URL
    timeout=30.0,                     # Optional: Request timeout
    max_retries=3,                    # Optional: Max retry attempts
)
```

### Chat Completions

Compatible with OpenAI's chat completions API, with additional CheckThat AI features:

```python
# Regular chat completion
response = client.chat.completions.create(
    model="gpt-5-2025-08-07",  # Use latest models
    messages=[...],
    temperature=0.7,
    max_tokens=1000,
    stream=False,
    # ... other OpenAI parameters
)

# Structured output with parse() method
response = client.chat.completions.parse(
    model="claude-sonnet-4-20250514",  # Use latest available models
    messages=[...],
    response_format=YourPydanticModel,
    refine_claims=True,  # CheckThat AI enhancement
    refine_model="gpt-5-2025-08-07",  # Best model for refinement
    # ... other parameters
)
```

### Model Information

```python
# List all available models with details
models = client.models.list()
for provider_data in models["models_list"]:
    print(f"Provider: {provider_data['provider']}")
    for model in provider_data["available_models"]:
        print(f"  {model['name']}: {model['model_id']}")

# Get specific model information
model_info = client.models.retrieve("gpt-5-2025-08-07")
print(f"Model details: {model_info}")
```

***sample response***

```json
{
  "models_list": [
    {
      "provider": "OpenAI",
      "available_models": [
        {
          "name": "GPT-5",
          "model_id": "gpt-5-2025-08-07"
        },
        {
          "name": "GPT-4o",
          "model_id": "gpt-4o-2024-11-20"
        },
        {
          "name": "o4-mini",
          "model_id": "o4-mini-2025-04-16"
        }
      ]
    },
    {
      "provider": "Anthropic", 
      "available_models": [
        {
          "name": "Claude Sonnet 4",
          "model_id": "claude-sonnet-4-20250514"
        },
        {
          "name": "Claude 3.7 Sonnet",
          "model_id": "claude-3-7-sonnet-20241022"
        }
      ]
    }
  ]
}
```

## Authentication

CheckThat AI requires you to provide API keys for the LLM providers you want to use. Set your API keys as environment variables:

```bash
# Set the API key for your chosen provider
export OPENAI_API_KEY="your-openai-key"
export ANTHROPIC_API_KEY="your-anthropic-key" 
export GEMINI_API_KEY="your-gemini-key"
export XAI_API_KEY="your-xai-key"
export TOGETHER_API_KEY="your-together-key"
```

Then pass the appropriate API key to the client:

```python
import os

# Use the API key for your chosen provider
api_key = os.getenv("OPENAI_API_KEY")  # or whichever provider you're using
client = CheckThatAI(api_key=api_key)
```

The SDK will route your requests to the appropriate LLM provider based on the model you select.

## Error Handling

The SDK uses OpenAI-compatible exception types and adds CheckThat-specific errors:

```python
from openai import OpenAIError, RateLimitError, APITimeoutError
from checkthat_ai._exceptions import InvalidModelError, InvalidResponseFormatError

try:
    response = client.chat.completions.create(
        model="gpt-5-2025-08-07",  # Use latest models
        messages=[{"role": "user", "content": "Hello!"}]
    )
except InvalidModelError as e:
    print(f"Invalid model: {e}")
    # List available models
    models = client.models.list()
    print("Available models:")
    for provider in models["models_list"]:
        print(f"{provider['provider']}: {len(provider['available_models'])} models")
except InvalidResponseFormatError as e:
    print(f"Response format error: {e}")
except RateLimitError:
    print("Rate limit exceeded")
except APITimeoutError:
    print("Request timed out")
except OpenAIError as e:
    print(f"API error: {e}")
```

## Examples

For comprehensive examples demonstrating advanced features like claim refinement and evaluation metrics, check the [`examples/`](examples/) directory:

- [`enhanced_structured_output_example.py`](examples/enhanced_structured_output_example.py) - Complete demo of all SDK features

## Contributing

We welcome contributions! Please see our [Contributing Guide](https://github.com/nikhil-kadapala/checkthat-ai/blob/main/CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- 📧 Email: kadapalanikhil@gmail.com
- 🐛 Issues: [GitHub Issues](https://github.com/nikhil-kadapala/checkthat-ai/issues)
- 🌐 Website: [checkthat-ai.com](https://checkthat-ai.com)

## Changelog

See [CHANGELOG.md](https://github.com/nikhil-kadapala/checkthat-ai/releases) for a history of changes.