"""
Exception classes for EmailVerify SDK.
"""

class EmailVerifyException(Exception):
    """Base exception for EmailVerify SDK."""
    pass

class EmailVerifyAPIException(EmailVerifyException):
    """API error exception."""
    
    def __init__(self, message, status_code=None, response_data=None):
        super().__init__(message)
        self.status_code = status_code
        self.response_data = response_data or {}


class EmailVerifyClientException(EmailVerifyException):
    """Client error exception."""
    pass
    

class EmailVerifyNetworkException(EmailVerifyException):
    """Network error exception."""
    pass


class EmailVerifyTimeoutException(EmailVerifyNetworkException):
    """Timeout error exception."""
    pass
