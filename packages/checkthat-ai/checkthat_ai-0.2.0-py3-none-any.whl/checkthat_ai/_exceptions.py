from openai import (
    APIError,
    APIConnectionError,
    APIResponseValidationError,
    APIStatusError,
    APITimeoutError,
    AuthenticationError,
    BadRequestError,
    ConflictError,
    InternalServerError,
    NotFoundError,
    PermissionDeniedError,
    RateLimitError,
    UnprocessableEntityError,
)

__all__ = [
    "APIError",
    "APIConnectionError",
    "APIResponseValidationError",
    "APIStatusError",
    "APITimeoutError",
    "AuthenticationError",
    "BadRequestError",
    "ConflictError",
    "InternalServerError",
    "NotFoundError",
    "PermissionDeniedError",
    "RateLimitError",
    "UnprocessableEntityError",
    # Custom CheckThat AI exceptions
    "InvalidModelError",
    "InvalidResponseFormatError",
]


class InvalidModelError(APIError):
    """Raised when an invalid model is specified."""
    def __init__(self, message: str, *, model: str = None) -> None:
        super().__init__(message, request=None, body={"error": {"code": "invalid_model", "param": "model", "type": "invalid_request_error"}})
        self.model = model
        self.status_code = 400  # Bad Request


class InvalidResponseFormatError(APIError):
    """Raised when response_format is used with incompatible parameters."""
    def __init__(self, message: str, *, model: str = None, stream: bool = None) -> None:
        super().__init__(message, request=None, body={"error": {"code": "invalid_response_format", "param": "response_format", "type": "invalid_request_error"}})
        self.model = model
        self.stream = stream
        self.status_code = 400  # Bad Request
