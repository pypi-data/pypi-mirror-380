"""Response classes for EmailVerify SDK."""

from typing import Dict, Any, Optional, List


class BaseResponse:
    """Base class for all EmailVerify API responses."""
    def __init__(self, data=None):
        self.__dict__ = data

    def __str__(self) -> str:
            return str(self.__class__.__name__) + "=" + str(self.__dict__)

class ValidateResponse(BaseResponse):
    """Response for single email validation."""

class BalanceResponse(BaseResponse):
    """Response for account balance checking."""

class BatchValidateResponse(BaseResponse):
    """Response for batch validation submission."""

class BatchResultEmail:
    """Single email result in batch."""

class BatchResultResponse(BaseResponse):
    """Response for batch validation results."""
    
class FinderResponse(BaseResponse):
    """Response for email finder."""