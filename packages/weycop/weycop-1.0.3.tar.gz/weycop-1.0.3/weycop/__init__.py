"""
WeyCP Client - Python SDK for WeyCP API
OpenAI-compatible client for chat completions
"""

__version__ = "1.0.3"
__author__ = "WeyCP Team"
__email__ = "apps@weycop.com"

from .client import WeycopClient, AsyncWeycopClient
from .models import Message, ChatCompletion, Usage, Choice, HealthStatus
from .exceptions import (
    WeycopError, AuthenticationError, RateLimitError, 
    APIError, ModelNotFoundError, TimeoutError, 
    ValidationError, ServiceUnavailableError, QuotaExceededError,
    create_error_from_response
)

__all__ = [
    # Client classes
    "WeycopClient",
    "AsyncWeycopClient",
    
    # Data models
    "Message",
    "ChatCompletion", 
    "Usage",
    "Choice",
    "HealthStatus",
    
    # Exceptions
    "WeycopError",
    "AuthenticationError", 
    "RateLimitError",
    "APIError",
    "ModelNotFoundError",
    "TimeoutError",
    "ValidationError",
    "ServiceUnavailableError",
    "QuotaExceededError",
    "create_error_from_response",
]