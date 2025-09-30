"""
EmailVerify SDK - A Python SDK for EmailVerify.io API

This package provides a comprehensive Python interface for the EmailVerify.io
email validation service, offering single email validation, bulk validation and single finder capabilities

Example usage:
    from emailverifysdk import EmailVerify
    
    # Initialize the client
    email_verify = EmailVerify("<YOUR_API_KEY>")
    
    # Validate a single email
    result = email_verify.validate('test@example.com')
    print(f"Status: {result.status}")
    
    # Check account balance
    balance = email_verify.check_balance()
    print(f"Credits: {balance.total_available_credits}")
    
    # Batch validation
    batch_result = email_verify.validate_batch(['email1@example.com', 'email2@example.com'])
    print(f"Task ID: {batch_result.task_id}")
    
    # Get batch results
    results = email_verify.get_batch_result(batch_result.task_id)
    print(f"Progress: {results.progress_percent}%")
    
    # Find email
    finder_result = email_verify.find_email('John', 'example.com')
    print(f"Found: {finder_result.email}")
"""

__version__ = "0.1.0"
__author__ = "EmailVerify"
__description__ = "Python SDK for EmailVerify.io API - Email Verification made simple"

# Import main client class
from .emailverifysdk import EmailVerify

# Import all response classes
from .responses import (
    BaseResponse,
    ValidateResponse,
    BalanceResponse,
    BatchValidateResponse,
    BatchResultResponse,
    BatchResultEmail,
    FinderResponse
)

# Import all exception classes
from .exceptions import (
    EmailVerifyException,
    EmailVerifyAPIException,
    EmailVerifyClientException,
    EmailVerifyNetworkException,
    EmailVerifyTimeoutException
)

__all__ = [
    # Main client
    'EmailVerify',
    
    # Response classes
    'BaseResponse',
    'ValidateResponse',
    'BalanceResponse',
    'BatchValidateResponse',
    'BatchResultResponse',
    'BatchResultEmail',
    'FinderResponse',
    
    # Exception classes
    'EmailVerifyException',
    'EmailVerifyAPIException',
    'EmailVerifyClientException',
    'EmailVerifyNetworkException',
    'EmailVerifyTimeoutException',
]
