"""
Sector8 SDK Enhanced Error Handling

Provides helpful, actionable error messages with debugging context
and suggested solutions for common issues.
"""

import os
import sys
from typing import Dict, Any, Optional, List
from dataclasses import dataclass


@dataclass
class ErrorContext:
    """Context information for debugging errors."""
    
    error_code: str
    error_message: str
    suggested_solutions: List[str]
    debug_info: Dict[str, Any]
    documentation_url: Optional[str] = None
    support_contact: Optional[str] = None


class Sector8Error(Exception):
    """Base exception class for Sector8 SDK with enhanced debugging."""
    
    def __init__(
        self, 
        message: str, 
        error_code: str = None,
        solutions: List[str] = None,
        debug_info: Dict[str, Any] = None,
        original_error: Exception = None
    ):
        super().__init__(message)
        self.message = message
        self.error_code = error_code or "SECTOR8_GENERAL_ERROR"
        self.solutions = solutions or []
        self.debug_info = debug_info or {}
        self.original_error = original_error
        
    def get_context(self) -> ErrorContext:
        """Get enhanced error context for debugging."""
        return ErrorContext(
            error_code=self.error_code,
            error_message=self.message,
            suggested_solutions=self.solutions,
            debug_info=self.debug_info,
            documentation_url="https://docs.sector8.ai/troubleshooting",
            support_contact="support@sector8.ai"
        )
    
    def print_debug_info(self) -> None:
        """Print formatted debugging information."""
        context = self.get_context()
        
        print(f"\n🚨 Sector8 SDK Error: {context.error_code}")
        print("=" * 60)
        print(f"Message: {context.error_message}")
        
        if context.suggested_solutions:
            print("\n💡 Suggested Solutions:")
            for i, solution in enumerate(context.suggested_solutions, 1):
                print(f"   {i}. {solution}")
        
        if context.debug_info:
            print("\n🔍 Debug Information:")
            for key, value in context.debug_info.items():
                print(f"   {key}: {value}")
        
        if context.documentation_url:
            print(f"\n📖 Documentation: {context.documentation_url}")
        
        if context.support_contact:
            print(f"📧 Support: {context.support_contact}")
        
        print("=" * 60)


class ConfigurationError(Sector8Error):
    """Enhanced configuration errors with specific guidance."""
    
    @classmethod
    def missing_api_key(cls) -> 'ConfigurationError':
        """Error when API key is missing."""
        return cls(
            message="API key is required but not provided",
            error_code="SECTOR8_MISSING_API_KEY",
            solutions=[
                "Set the SECTOR8_API_KEY environment variable",
                "Pass api_key parameter to sector8.setup()",
                "Run sector8.configure_wizard() for guided setup",
                "Check that your .env file contains SECTOR8_API_KEY"
            ],
            debug_info={
                "environment_variables": {
                    "SECTOR8_API_KEY": "Not Set" if not os.getenv('SECTOR8_API_KEY') else "Set",
                    "API_KEY": "Not Set" if not os.getenv('API_KEY') else "Set"
                },
                "suggested_command": "export SECTOR8_API_KEY='your-api-key-here'"
            }
        )
    
    @classmethod
    def invalid_api_key(cls, api_key: str = None) -> 'ConfigurationError':
        """Error when API key format is invalid."""
        return cls(
            message="API key format appears to be invalid",
            error_code="SECTOR8_INVALID_API_KEY",
            solutions=[
                "Verify your API key from the Sector8 dashboard",
                "Ensure no extra spaces or characters in the API key", 
                "Check that you're using the correct API key for your environment",
                "Contact support if you believe this is an error"
            ],
            debug_info={
                "api_key_length": len(api_key) if api_key else 0,
                "api_key_format": "Hidden for security",
                "expected_length": "40+ characters"
            }
        )
    
    @classmethod 
    def invalid_base_url(cls, url: str) -> 'ConfigurationError':
        """Error when base URL is invalid."""
        return cls(
            message=f"Invalid base URL: {url}",
            error_code="SECTOR8_INVALID_BASE_URL",
            solutions=[
                "Use a valid URL starting with http:// or https://",
                "Check for typos in the URL",
                "Verify the endpoint is accessible",
                "Use default URL by omitting base_url parameter"
            ],
            debug_info={
                "provided_url": url,
                "default_production_url": "https://api.sector8.ai",
                "url_format": "https://your-domain.com"
            }
        )


class AuthenticationError(Sector8Error):
    """Enhanced authentication errors."""
    
    @classmethod
    def token_expired(cls) -> 'AuthenticationError':
        """Error when authentication token is expired."""
        return cls(
            message="Authentication token has expired",
            error_code="SECTOR8_TOKEN_EXPIRED",
            solutions=[
                "The SDK will automatically refresh the token",
                "If the problem persists, check your API key",
                "Verify your system clock is correct",
                "Contact support if using a custom authentication"
            ],
            debug_info={
                "token_refresh": "Automatic",
                "system_time": str(sys.version),
                "retry_behavior": "SDK handles automatically"
            }
        )
    
    @classmethod
    def unauthorized_access(cls, status_code: int = None) -> 'AuthenticationError':
        """Error when API returns unauthorized."""
        return cls(
            message="Unauthorized access - API key may be invalid or inactive",
            error_code="SECTOR8_UNAUTHORIZED",
            solutions=[
                "Verify your API key is correct and active",
                "Check that your account has the required permissions",
                "Ensure you're connecting to the correct environment",
                "Contact support to verify your account status"
            ],
            debug_info={
                "http_status": status_code,
                "authentication_method": "API Key",
                "account_verification": "Contact support@sector8.ai"
            }
        )


class NetworkError(Sector8Error):
    """Enhanced network and connectivity errors."""
    
    @classmethod
    def connection_failed(cls, url: str, original_error: Exception = None) -> 'NetworkError':
        """Error when network connection fails."""
        return cls(
            message=f"Failed to connect to Sector8 API at {url}",
            error_code="SECTOR8_CONNECTION_FAILED",
            solutions=[
                "Check your internet connection",
                "Verify the API endpoint URL is correct",
                "Check if you're behind a corporate firewall",
                "Try again in a few moments (temporary network issue)",
                "Contact your network administrator if behind a proxy"
            ],
            debug_info={
                "endpoint_url": url,
                "original_error": str(original_error) if original_error else None,
                "network_test": "Try: ping api.sector8.ai",
                "proxy_check": "Check HTTP_PROXY and HTTPS_PROXY environment variables"
            },
            original_error=original_error
        )
    
    @classmethod
    def timeout_error(cls, timeout_seconds: int, url: str) -> 'NetworkError':
        """Error when request times out."""
        return cls(
            message=f"Request timed out after {timeout_seconds} seconds",
            error_code="SECTOR8_REQUEST_TIMEOUT",
            solutions=[
                f"Increase timeout (current: {timeout_seconds}s)",
                "Check your network connection speed",
                "Verify API endpoint is responding",
                "Try reducing request payload size",
                "Contact support if timeouts persist"
            ],
            debug_info={
                "timeout_seconds": timeout_seconds,
                "endpoint_url": url,
                "suggested_timeout": "60-120 seconds for most requests",
                "network_latency": "Test with: curl -w '%{time_total}' " + url
            }
        )


class ValidationError(Sector8Error):
    """Enhanced validation errors for request data."""
    
    @classmethod
    def invalid_request_data(cls, field_errors: Dict[str, str]) -> 'ValidationError':
        """Error when request data validation fails."""
        field_descriptions = []
        solutions = ["Fix the following validation errors:"]
        
        for field, error in field_errors.items():
            field_descriptions.append(f"{field}: {error}")
            solutions.append(f"• {field}: {error}")
        
        return cls(
            message="Request data validation failed",
            error_code="SECTOR8_VALIDATION_ERROR",
            solutions=solutions,
            debug_info={
                "invalid_fields": field_errors,
                "validation_reference": "See API documentation for field requirements"
            }
        )
    
    @classmethod
    def missing_required_fields(cls, missing_fields: List[str]) -> 'ValidationError':
        """Error when required fields are missing."""
        return cls(
            message=f"Missing required fields: {', '.join(missing_fields)}",
            error_code="SECTOR8_MISSING_REQUIRED_FIELDS",
            solutions=[
                f"Provide values for: {', '.join(missing_fields)}",
                "Check the API documentation for required parameters",
                "Verify your request includes all mandatory fields"
            ],
            debug_info={
                "missing_fields": missing_fields,
                "total_missing": len(missing_fields)
            }
        )


class RateLimitError(Sector8Error):
    """Enhanced rate limiting errors."""
    
    @classmethod
    def rate_limit_exceeded(cls, retry_after: int = None, limit: str = None) -> 'RateLimitError':
        """Error when API rate limit is exceeded."""
        solutions = [
            "Wait before making another request",
            "Implement exponential backoff in your application",
            "Consider upgrading your plan for higher limits",
            "Batch multiple operations into single requests where possible"
        ]
        
        if retry_after:
            solutions.insert(0, f"Retry after {retry_after} seconds")
        
        return cls(
            message="API rate limit exceeded",
            error_code="SECTOR8_RATE_LIMIT_EXCEEDED",
            solutions=solutions,
            debug_info={
                "retry_after_seconds": retry_after,
                "rate_limit": limit,
                "backoff_strategy": "Exponential backoff recommended"
            }
        )


class ServiceError(Sector8Error):
    """Enhanced service and server errors."""
    
    @classmethod
    def service_unavailable(cls, status_code: int = None) -> 'ServiceError':
        """Error when service is temporarily unavailable."""
        return cls(
            message="Sector8 API service is temporarily unavailable",
            error_code="SECTOR8_SERVICE_UNAVAILABLE",
            solutions=[
                "Wait a few moments and try again",
                "Check https://status.sector8.ai for service status",
                "Implement retry logic with exponential backoff",
                "Contact support if the issue persists"
            ],
            debug_info={
                "http_status": status_code,
                "service_status": "Check https://status.sector8.ai",
                "retry_strategy": "Exponential backoff recommended"
            }
        )
    
    @classmethod
    def internal_server_error(cls, status_code: int = None, request_id: str = None) -> 'ServiceError':
        """Error when server encounters an internal error."""
        return cls(
            message="Internal server error occurred",
            error_code="SECTOR8_INTERNAL_SERVER_ERROR",
            solutions=[
                "This is a temporary server issue - please try again",
                "If the problem persists, contact support with the request ID",
                "Check https://status.sector8.ai for any known issues"
            ],
            debug_info={
                "http_status": status_code,
                "request_id": request_id,
                "support_info": "Include request_id when contacting support"
            }
        )


def handle_api_error(response_status: int, response_body: str = None, request_url: str = None) -> Sector8Error:
    """
    Convert API response errors into helpful Sector8Error instances.
    
    Args:
        response_status: HTTP status code
        response_body: Response body content
        request_url: The URL that was requested
        
    Returns:
        Appropriate Sector8Error subclass with helpful context
    """
    if response_status == 401:
        return AuthenticationError.unauthorized_access(response_status)
    elif response_status == 403:
        return AuthenticationError(
            message="Forbidden - insufficient permissions",
            error_code="SECTOR8_FORBIDDEN",
            solutions=[
                "Check that your API key has the required permissions",
                "Verify you're accessing the correct resource",
                "Contact support to verify your account permissions"
            ]
        )
    elif response_status == 429:
        # Try to extract retry-after from response
        return RateLimitError.rate_limit_exceeded()
    elif response_status >= 500:
        return ServiceError.internal_server_error(response_status)
    elif response_status == 503:
        return ServiceError.service_unavailable(response_status)
    else:
        return Sector8Error(
            message=f"API request failed with status {response_status}",
            error_code="SECTOR8_API_ERROR",
            solutions=[
                "Check the API documentation for correct request format",
                "Verify your request parameters are correct",
                "Try the request again if it was a temporary issue"
            ],
            debug_info={
                "http_status": response_status,
                "response_body": response_body[:200] if response_body else None,
                "request_url": request_url
            }
        )


class TimeoutError(NetworkError):
    """Timeout error for network requests."""
    pass


class ServiceUnavailableError(ServiceError):
    """Service unavailable error."""
    pass


class SecurityError(Sector8Error):
    """Security-related error."""
    pass


class TelemetryError(Sector8Error):
    """Telemetry-related error."""
    pass


def print_startup_diagnostics() -> None:
    """Print helpful diagnostics for debugging startup issues."""
    print("Sector8 SDK Diagnostics")
    print("=" * 40)
    
    # Check environment variables
    api_key = os.getenv('SECTOR8_API_KEY')
    print(f"SECTOR8_API_KEY: {'Set' if api_key else 'Not Set'}")
    
    if api_key:
        print(f"API Key Length: {len(api_key)} characters")
    
    # Check base URL
    base_url = os.getenv('SECTOR8_BASE_URL', 'https://api.sector8.ai')
    print(f"Base URL: {base_url}")
    
    # Check Python version
    python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    print(f"Python Version: {python_version}")
    
    # Check required packages
    try:
        import aiohttp
        print(f"aiohttp: Available - {aiohttp.__version__}")
    except ImportError:
        print("aiohttp: Not installed (pip install aiohttp)")
    
    print("=" * 40)
    print("Run 'sector8.configure_wizard()' for guided setup")
    print("Documentation: https://docs.sector8.ai")
    print("Support: support@sector8.ai")