"""
Custom exceptions for the Chart Beautifier SDK.
"""


class ChartBeautifierError(Exception):
    """Base exception for all Chart Beautifier SDK errors."""
    pass


class ValidationError(ChartBeautifierError):
    """Raised when input validation fails."""
    pass


class APIError(ChartBeautifierError):
    """Raised when API requests fail."""
    
    def __init__(self, message: str, status_code: int = None, response_data: dict = None):
        super().__init__(message)
        self.status_code = status_code
        self.response_data = response_data or {}


class AuthenticationError(APIError):
    """Raised when authentication fails."""
    pass


class RateLimitError(APIError):
    """Raised when rate limit is exceeded."""
    pass
