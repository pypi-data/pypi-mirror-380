"""
Tests for custom exceptions.
"""

import pytest
from chart_beautifier.exceptions import (
    ChartBeautifierError,
    ValidationError,
    APIError,
    AuthenticationError,
    RateLimitError
)


class TestExceptions:
    """Test cases for custom exceptions."""
    
    def test_chart_beautifier_error_inheritance(self):
        """Test that all custom exceptions inherit from ChartBeautifierError."""
        assert issubclass(ValidationError, ChartBeautifierError)
        assert issubclass(APIError, ChartBeautifierError)
        assert issubclass(AuthenticationError, APIError)
        assert issubclass(RateLimitError, APIError)
    
    def test_validation_error(self):
        """Test ValidationError creation."""
        error = ValidationError("Invalid input")
        assert str(error) == "Invalid input"
        assert isinstance(error, ChartBeautifierError)
    
    def test_api_error_with_status_code(self):
        """Test APIError with status code and response data."""
        error = APIError(
            "API request failed", 
            status_code=404, 
            response_data={"error": "Not found"}
        )
        assert str(error) == "API request failed"
        assert error.status_code == 404
        assert error.response_data == {"error": "Not found"}
    
    def test_api_error_without_optional_params(self):
        """Test APIError without optional parameters."""
        error = APIError("API request failed")
        assert str(error) == "API request failed"
        assert error.status_code is None
        assert error.response_data == {}
    
    def test_authentication_error(self):
        """Test AuthenticationError creation."""
        error = AuthenticationError("Invalid credentials", status_code=401)
        assert str(error) == "Invalid credentials"
        assert error.status_code == 401
        assert isinstance(error, APIError)
    
    def test_rate_limit_error(self):
        """Test RateLimitError creation."""
        error = RateLimitError("Rate limit exceeded", status_code=429)
        assert str(error) == "Rate limit exceeded"
        assert error.status_code == 429
        assert isinstance(error, APIError)
