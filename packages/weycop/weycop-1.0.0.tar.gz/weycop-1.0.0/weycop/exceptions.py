"""
Exception classes for WeyCP Client
"""

import json
from typing import Optional, Dict, Any, Union


class WeycopError(Exception):
    """
    Base exception for WeyCP client errors
    
    Provides structured error information including:
    - Error message
    - HTTP status code (if applicable)
    - Raw response data
    - Request details for debugging
    """
    
    def __init__(
        self, 
        message: str, 
        status_code: Optional[int] = None,
        response_data: Optional[Dict[str, Any]] = None,
        request_info: Optional[Dict[str, Any]] = None
    ):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.response_data = response_data or {}
        self.request_info = request_info or {}
    
    def __str__(self) -> str:
        """Enhanced string representation for debugging"""
        parts = [self.message]
        
        if self.status_code:
            parts.append(f"Status: {self.status_code}")
        
        if self.response_data.get('error'):
            error_detail = self.response_data['error']
            if isinstance(error_detail, dict):
                if 'detail' in error_detail:
                    parts.append(f"Detail: {error_detail['detail']}")
                if 'code' in error_detail:
                    parts.append(f"Code: {error_detail['code']}")
            else:
                parts.append(f"Error: {error_detail}")
        
        return " | ".join(parts)
    
    def get_debug_info(self) -> Dict[str, Any]:
        """Get comprehensive debugging information"""
        return {
            "error_type": self.__class__.__name__,
            "message": self.message,
            "status_code": self.status_code,
            "response_data": self.response_data,
            "request_info": self.request_info
        }


class AuthenticationError(WeycopError):
    """
    Raised when API key authentication fails
    
    Common causes:
    - Invalid API key
    - Expired API key
    - API key not provided
    - Insufficient permissions
    """
    
    def __init__(self, message: str = None, **kwargs):
        if not message:
            message = "Authentication failed. Please check your API key."
        super().__init__(message, **kwargs)
        
        # Add helpful suggestions based on response
        if self.response_data.get('error', {}).get('detail'):
            detail = self.response_data['error']['detail']
            if 'not provided' in detail.lower():
                self.message += " Hint: Make sure to include the Authorization header."
            elif 'invalid' in detail.lower():
                self.message += " Hint: Verify your API key is correct and active."


class RateLimitError(WeycopError):
    """
    Raised when rate limit is exceeded
    
    Includes information about:
    - Rate limit details
    - Reset time
    - Suggested retry delay
    """
    
    def __init__(self, message: str = None, retry_after: Optional[int] = None, **kwargs):
        if not message:
            message = "Rate limit exceeded."
        super().__init__(message, **kwargs)
        self.retry_after = retry_after
        
        # Extract rate limit info from headers or response
        if self.response_data:
            limits = self.response_data.get('rate_limit', {})
            if limits.get('reset_time'):
                self.message += f" Rate limit resets at: {limits['reset_time']}"
            if limits.get('remaining'):
                self.message += f" Requests remaining: {limits['remaining']}"
        
        if retry_after:
            self.message += f" Retry after: {retry_after} seconds"


class APIError(WeycopError):
    """
    General API error for non-specific server errors
    
    Includes full response context for debugging
    """
    
    def __init__(self, message: str, **kwargs):
        super().__init__(message, **kwargs)
        
        # Enhance message with response details
        if self.response_data:
            if 'detail' in self.response_data:
                detail = self.response_data['detail']
                if isinstance(detail, list) and len(detail) > 0:
                    # Handle FastAPI validation errors
                    error_details = []
                    for error in detail:
                        if isinstance(error, dict):
                            loc = error.get('loc', [])
                            msg = error.get('msg', 'Unknown error')
                            if loc:
                                error_details.append(f"{'.'.join(map(str, loc))}: {msg}")
                            else:
                                error_details.append(msg)
                    if error_details:
                        self.message += f" Validation errors: {'; '.join(error_details)}"
                elif isinstance(detail, str):
                    self.message += f" Detail: {detail}"


class ModelNotFoundError(WeycopError):
    """
    Raised when requested model is not available
    
    Includes suggestions for available models
    """
    
    def __init__(self, model_name: str = None, available_models: Optional[list] = None, **kwargs):
        message = f"Model '{model_name}' not found." if model_name else "Requested model not found."
        super().__init__(message, **kwargs)
        self.model_name = model_name
        self.available_models = available_models or []
        
        if self.available_models:
            self.message += f" Available models: {', '.join(self.available_models)}"
        
        # Extract available models from response if provided
        if self.response_data.get('available_models'):
            models = self.response_data['available_models']
            if isinstance(models, list):
                self.message += f" Available models: {', '.join(models)}"


class TimeoutError(WeycopError):
    """
    Raised when request times out
    
    Includes timeout duration and suggestions
    """
    
    def __init__(self, message: str = None, timeout_duration: Optional[float] = None, **kwargs):
        if not message:
            message = "Request timed out."
        super().__init__(message, **kwargs)
        self.timeout_duration = timeout_duration
        
        if timeout_duration:
            self.message += f" Timeout duration: {timeout_duration}s"
        
        self.message += " Hint: Try increasing the timeout parameter or check your network connection."


class ValidationError(WeycopError):
    """
    Raised when request parameters are invalid
    
    Provides detailed field-level validation errors
    """
    
    def __init__(self, message: str = None, validation_errors: Optional[list] = None, **kwargs):
        if not message:
            message = "Request validation failed."
        super().__init__(message, **kwargs)
        self.validation_errors = validation_errors or []
        
        # Parse validation errors from response
        if self.response_data.get('detail') and isinstance(self.response_data['detail'], list):
            errors = []
            for error in self.response_data['detail']:
                if isinstance(error, dict):
                    field = '.'.join(map(str, error.get('loc', [])))
                    msg = error.get('msg', 'Invalid value')
                    errors.append(f"{field}: {msg}")
            if errors:
                self.message += f" Errors: {'; '.join(errors)}"


class ServiceUnavailableError(WeycopError):
    """
    Raised when the API service is temporarily unavailable
    
    Often indicates:
    - Server maintenance
    - Ollama service down
    - Database connection issues
    """
    
    def __init__(self, message: str = None, **kwargs):
        if not message:
            message = "Service temporarily unavailable. Please try again later."
        super().__init__(message, **kwargs)
        
        if self.response_data.get('service_status'):
            status = self.response_data['service_status']
            if 'ollama' in status and not status['ollama']:
                self.message += " Hint: AI model service appears to be down."
            if 'database' in status and not status['database']:
                self.message += " Hint: Database connection issue detected."


class QuotaExceededError(WeycopError):
    """
    Raised when token quota is exceeded
    
    Includes information about:
    - Current quota usage
    - Available extra tokens
    - Suggestions for purchasing more tokens
    """
    
    def __init__(self, message: str = None, quota_info: Optional[Dict[str, Any]] = None, **kwargs):
        if not message:
            message = "Token quota exceeded."
        super().__init__(message, **kwargs)
        self.quota_info = quota_info or {}
        
        # Enhance message with quota details
        if self.response_data.get('quota'):
            quota = self.response_data['quota']
            if quota.get('plan'):
                self.message += f" Plan: {quota['plan']}"
            if quota.get('monthly_allowance') and quota.get('monthly_used'):
                self.message += f" Used: {quota['monthly_used']:,}/{quota['monthly_allowance']:,} tokens"
            if quota.get('extra_available'):
                self.message += f" Extra tokens available: {quota['extra_available']:,}"
            else:
                self.message += " Consider purchasing additional tokens."


def create_error_from_response(
    response_status: int, 
    response_data: Dict[str, Any],
    request_info: Optional[Dict[str, Any]] = None
) -> WeycopError:
    """
    Factory function to create appropriate exception from HTTP response
    
    Args:
        response_status: HTTP status code
        response_data: Parsed response JSON data
        request_info: Information about the original request
    
    Returns:
        Appropriate WeycopError subclass
    """
    
    # Common error mapping
    error_map = {
        400: ValidationError,
        401: AuthenticationError,
        402: QuotaExceededError,  # Payment required - quota exceeded
        403: AuthenticationError,
        404: ModelNotFoundError,
        422: ValidationError,
        429: RateLimitError,
        503: ServiceUnavailableError,
        504: TimeoutError,
    }
    
    # Extract error message
    error_message = "API request failed"
    if isinstance(response_data, dict):
        if 'detail' in response_data:
            detail = response_data['detail']
            if isinstance(detail, str):
                error_message = detail
            elif isinstance(detail, list) and len(detail) > 0:
                error_message = "Validation error occurred"
        elif 'error' in response_data:
            error_data = response_data['error']
            if isinstance(error_data, str):
                error_message = error_data
            elif isinstance(error_data, dict) and 'message' in error_data:
                error_message = error_data['message']
        elif 'message' in response_data:
            error_message = response_data['message']
    
    # Create appropriate exception
    exception_class = error_map.get(response_status, APIError)
    
    # Special handling for specific error types
    if exception_class == ModelNotFoundError and request_info:
        model_name = request_info.get('model')
        available_models = response_data.get('available_models', [])
        return exception_class(
            model_name=model_name,
            available_models=available_models,
            message=error_message,
            status_code=response_status,
            response_data=response_data,
            request_info=request_info
        )
    
    elif exception_class == RateLimitError:
        retry_after = response_data.get('retry_after')
        return exception_class(
            message=error_message,
            retry_after=retry_after,
            status_code=response_status,
            response_data=response_data,
            request_info=request_info
        )
    
    else:
        return exception_class(
            message=error_message,
            status_code=response_status,
            response_data=response_data,
            request_info=request_info
        )