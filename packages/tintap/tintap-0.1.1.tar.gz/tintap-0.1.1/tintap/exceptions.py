"""
tintap SDK exceptions

Custom exception classes for the tintap Python SDK.
"""


class TintapError(Exception):
    """Base exception class for all tintap SDK errors."""
    pass


class TintapAPIError(TintapError):
    """Exception raised for API-related errors."""
    
    def __init__(self, message, status_code=None, response=None):
        super().__init__(message)
        self.status_code = status_code
        self.response = response


class TintapConnectionError(TintapError):
    """Exception raised for connection-related errors."""
    pass


class TintapAuthError(TintapAPIError):
    """Exception raised for authentication errors."""
    pass


class TintapRateLimitError(TintapAPIError):
    """Exception raised when rate limits are exceeded."""
    pass


class TintapValidationError(TintapError):
    """Exception raised for input validation errors."""
    pass