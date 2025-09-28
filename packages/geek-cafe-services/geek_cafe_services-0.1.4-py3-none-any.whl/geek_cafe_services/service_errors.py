# Service Errors
from typing import Optional

class ValidationError(Exception):
    """Validation error for service operations."""
    
    def __init__(self, message: str, field: Optional[str] = None):
        super().__init__(message)
        self.field = field


class AccessDeniedError(Exception):
    """Access denied error for service operations."""
    pass


class NotFoundError(Exception):
    """Resource not found error."""
    pass