# Changelog

All notable changes to the CheckThat AI Python SDK will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2025-09-28

### Added
- **Claim Refinement System**: New iterative claim refinement capabilities with configurable parameters
  - `refine_claims`: Enable/disable claim refinement
  - `refine_model`: Specify model for refinement process
  - `refine_threshold`: Set quality threshold (0.0-1.0)
  - `refine_max_iters`: Maximum refinement iterations
- **Enhanced Structured Output Support**: Improved `parse()` method for Pydantic models
- **Evaluation Metrics**: Support for quality evaluation metrics including:
  - G-Eval
  - Bias detection
  - Hallucination detection
  - Factual accuracy assessment
  - Relevance scoring
  - Coherence evaluation
- **Latest Model Support**: Access to all 2025 models from supported providers
  - OpenAI: GPT-5, GPT-5 nano, o3, o4-mini
  - Anthropic: Claude Sonnet 4, Sonnet Opus 4.1
  - Google: Gemini 2.5 Pro, Gemini 2.5 Flash
  - xAI: Grok 4, Grok 3, Grok 3 Mini
  - Together AI: Llama 3.3 70B, Deepseek R1 Distill Llama 70B
- **Enhanced Error Handling**: Custom exception types for better error management
  - `InvalidModelError`: For unsupported models
  - `InvalidResponseFormatError`: For structured output format errors
- **Comprehensive Examples**: New examples demonstrating claim refinement and evaluation features

### Enhanced
- **Model Discovery**: Improved `/v1/models` endpoint integration with detailed model information
- **Documentation**: Comprehensive README updates with working examples
- **Type Safety**: Enhanced type hints throughout the codebase
- **API Compatibility**: Maintained full OpenAI SDK compatibility while adding new features

### Changed
- **Project Description**: Updated to emphasize claim refinement capabilities
- **Keywords**: Added new keywords for better discoverability: "claim-refinement", "structured-output", "xai", "together"
- **Python Support**: Added Python 3.13 support
- **Classifiers**: Added new PyPI classifiers for text processing and quality assurance

### Technical
- Enhanced backend request handling for claim refinement parameters
- Improved structured output processing with automatic Pydantic model conversion
- Better model validation and availability checking
- Enhanced async support for all new features

## [0.1.0] - 2025-09-01

### Added
- Initial release of CheckThat AI Python SDK
- Basic OpenAI-compatible API client
- Support for multiple LLM providers (OpenAI, Anthropic, Google, xAI, Together AI)
- Basic chat completions functionality
- Async support
- Type hints and type safety
- Basic error handling

[0.2.0]: https://github.com/nikhil-kadapala/checkthat-ai/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/nikhil-kadapala/checkthat-ai/releases/tag/v0.1.0