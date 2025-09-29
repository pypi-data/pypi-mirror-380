"""
Helper utilities for the CheckThat AI SDK.
"""

from typing import Any, Dict
import logging


def setup_logging(level: int = logging.INFO) -> None:
    """Setup logging for the CheckThat AI SDK."""
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )


def merge_dicts(base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
    """
    Recursively merge two dictionaries.
    Values from override will take precedence.
    """
    result = base.copy()

    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = merge_dicts(result[key], value)
        else:
            result[key] = value

    return result


def validate_api_key(api_key: str) -> bool:
    """
    Basic validation for API key format.
    This is a simple check and should be enhanced based on actual requirements.
    """
    if not api_key or not isinstance(api_key, str):
        return False

    # Basic length check
    return len(api_key.strip()) > 10
