"""
Custom exceptions for the Reeve Python SDK.
"""


class ReeveAPIError(Exception):
    """Base exception for all Reeve API errors."""

    def __init__(self, message: str, status_code: int = None, response: dict = None):
        self.message = message
        self.status_code = status_code
        self.response = response
        super().__init__(self.message)

    def __str__(self):
        if self.status_code:
            return f"[{self.status_code}] {self.message}"
        return self.message


class AuthenticationError(ReeveAPIError):
    """Raised when authentication fails (401 Unauthorized)."""

    def __init__(self, message: str = "Authentication failed", status_code: int = 401, response: dict = None):
        super().__init__(message, status_code, response)


class ValidationError(ReeveAPIError):
    """Raised when request validation fails (400 Bad Request)."""

    def __init__(self, message: str = "Validation error", status_code: int = 400, response: dict = None):
        super().__init__(message, status_code, response)


class NotFoundError(ReeveAPIError):
    """Raised when a resource is not found (404 Not Found)."""

    def __init__(self, message: str = "Resource not found", status_code: int = 404, response: dict = None):
        super().__init__(message, status_code, response)


class APIError(ReeveAPIError):
    """Raised for general API errors (5xx Server Errors)."""

    def __init__(self, message: str = "API error occurred", status_code: int = 500, response: dict = None):
        super().__init__(message, status_code, response)
