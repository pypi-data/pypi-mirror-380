"""
Custom exceptions for PyGhost library
"""


class GhostAPIError(Exception):
    """Base exception for all Ghost API related errors"""

    def __init__(self, message, status_code=None, response=None):
        self.message = message
        self.status_code = status_code
        self.response = response
        super().__init__(self.message)


class AuthenticationError(GhostAPIError):
    """Raised when authentication fails"""
    pass


class ValidationError(GhostAPIError):
    """Raised when request validation fails"""
    pass


class NotFoundError(GhostAPIError):
    """Raised when a resource is not found"""
    pass


class RateLimitError(GhostAPIError):
    """Raised when rate limit is exceeded"""
    pass
