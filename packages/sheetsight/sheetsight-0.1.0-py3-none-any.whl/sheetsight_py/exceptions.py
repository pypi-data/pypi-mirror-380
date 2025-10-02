"""
Exception classes for Sheetsight Python client
"""


class SheetsightError(Exception):
    """Base exception for all Sheetsight client errors"""
    pass


class AuthenticationError(SheetsightError):
    """Raised when API key authentication fails"""
    pass


class APIError(SheetsightError):
    """Raised when API returns an error response"""
    
    def __init__(self, message: str, status_code: int = None, response_data: dict = None):
        super().__init__(message)
        self.status_code = status_code
        self.response_data = response_data


class TimeoutError(SheetsightError):
    """Raised when API request times out"""
    pass


