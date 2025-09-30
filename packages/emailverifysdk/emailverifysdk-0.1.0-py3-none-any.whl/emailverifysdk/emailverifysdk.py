"""
EmailVerify.io Python SDK

Official Python SDK for EmailVerify.io API services.
"""

import requests
from typing import List, Optional, Dict, Any
from urllib.parse import urljoin

from .exceptions import (
    EmailVerifyAPIException,
    EmailVerifyClientException,
    EmailVerifyNetworkException,
    EmailVerifyTimeoutException
)
from .responses import (
    ValidateResponse,
    BalanceResponse,
    BatchValidateResponse,
    BatchResultResponse,
    FinderResponse
)

class EmailVerify:
    """
    EmailVerify.io SDK client.
    
    This class provides a Python interface to the EmailVerify.io API services
    including email validation, batch processing, account balance checking,
    and email finding functionality.
    """
    
    BASE_URL = "https://app.emailverify.io/api/v1"
    
    def __init__(self, api_key: str):
        """
        Initialize EmailVerify SDK client.
        
        Args:
            api_key: Your EmailVerify.io API key
        
        Raises:
            EmailVerifyClientException: If API key is empty or invalid format
        """
        if not api_key or not api_key.strip():
            raise EmailVerifyClientException("API key cannot be empty")
        
        self.api_key = api_key
        self.base_url = self.BASE_URL  # Allow runtime override
        self.session = requests.Session()
        
        # Set default headers
        self.session.headers.update({
            'User-Agent': 'EmailVerify-Python-SDK/0.1.0',
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        })
    
    def _safe_json(self, response):
        """Safely parse JSON, fallback to raw text."""
        try:
            return response.json()
        except ValueError:
            return {"raw": response.text}

    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()
    
    def close(self):
        """Close the session."""
        if self.session:
            self.session.close()
    
    def _make_request(self, method: str, endpoint: str, params: Dict[str, Any] = None, 
                     json_data: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Make an HTTP request to the EmailVerify API.
        
        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint (without base URL)
            params: Query parameters
            json_data: JSON data for POST requests
            
        Returns:
            Parsed JSON response
            
        Raises:
            EmailVerifyException: For various API and network errors
        """
        # Fix URL joining - remove leading slash from endpoint to preserve base path
        clean_endpoint = endpoint.lstrip('/')
        url = urljoin(self.base_url.rstrip('/') + '/', clean_endpoint)
        
        # Add API key to parameters
        if params is None:
            params = {}
        params['key'] = self.api_key
        
        try:
            response = self.session.request(
                method=method,
                url=url,
                params=params,
                json=json_data
            )
            
            if response.status_code >= 400:
                response_data = self._safe_json(response)
                error_message = None

                if isinstance(response_data, dict):
                    error_message = response_data.get("error") or response_data.get("message")

                if not error_message:
                    error_message = f"API request failed with status {response.status_code}"

                raise EmailVerifyAPIException(
                    error_message,
                    status_code=response.status_code,
                    response_data=response_data
                )

            # Parse JSON response
            try:
                return response.json()
            except ValueError as e:
                raise EmailVerifyAPIException(f"Invalid JSON response: {e}")
                
        except requests.exceptions.Timeout:
            raise EmailVerifyTimeoutException("Request timed out.")
        except requests.exceptions.ConnectionError as e:
            raise EmailVerifyNetworkException(f"Network connection error: {e}")
        except requests.exceptions.RequestException as e:
            raise EmailVerifyNetworkException(f"Request error: {e}")
    
    def validate(self, email: str) -> ValidateResponse:
        """
        Validate a single email address.
        
        Args:
            email: Email address to validate
            
        Returns:
            ValidateResponse object with validation results
            
        Raises:
            EmailVerifyClientException: If email is empty
            EmailVerifyException: For API errors
        """
        if not email or not email.strip():
            raise EmailVerifyClientException("Email is required")
        
        params = {'email': email.strip()}
        data = self._make_request('GET', '/validate', params=params)
        return ValidateResponse(data)
    
    def check_balance(self) -> BalanceResponse:
        """
        Check account balance and API status.
        
        Returns:
            BalanceResponse object with balance information
            
        Raises:
            EmailVerifyException: For API errors
        """
        data = self._make_request('GET', '/check-account-balance')
        return BalanceResponse(data)
    
    def validate_batch(self, emails: List[str], title: str = "Batch Validation") -> BatchValidateResponse:
        """
        Submit a batch of emails for validation (up to 5000 emails).
        
        Args:
            emails: List of email addresses to validate
            title: Optional title for the batch job
            
        Returns:
            BatchValidateResponse object with submission results
            
        Raises:
            EmailVerifyClientException: If emails list is empty or too large
            EmailVerifyException: For API errors
        """

        if not title:
            raise EmailVerifyClientException("Title is required")

        if not emails:
            raise EmailVerifyClientException("Email list cannot be empty")
        
        if len(emails) > 5000:
            raise EmailVerifyClientException("Maximum 5000 emails allowed per batch")
        
        # Format emails for API
        email_batch = [{"address": email.strip()} for email in emails if email.strip()]
        
        if not email_batch:
            raise EmailVerifyClientException("No valid email addresses provided")
        
        json_data = {
            "title": title,
            "key": self.api_key,
            "email_batch": email_batch
        }
        
        data = self._make_request('POST', '/validate-batch', json_data=json_data)
        return BatchValidateResponse(data)
    
    def get_batch_result(self, task_id) -> BatchResultResponse:
        """
        Get the results of a batch validation task.
        
        Args:
            task_id: The task ID returned from validate_batch() (should be int, str allowed)
            
        Returns:
            BatchResultResponse object with validation results
            
        Raises:
            EmailVerifyClientException: If task_id is empty
            EmailVerifyException: For API errors
        """
        if isinstance(task_id, str):
            if not task_id.strip():
                raise EmailVerifyClientException("Task ID is required")
            try:
                task_id_int = int(task_id.strip())
            except ValueError:
                raise EmailVerifyClientException("Task ID must be an integer")
        elif isinstance(task_id, int):
            task_id_int = task_id
        else:
            raise EmailVerifyClientException("Task ID must be an integer or string representing an integer")
        params = {'task_id': task_id_int}
        data = self._make_request('GET', '/get-result-bulk-verification-task', params=params)
        return BatchResultResponse(data)
    
    def find_email(self, name: str, domain: str) -> FinderResponse:
        """
        Find an email address using name and domain.
        
        Args:
            name: The person's name (e.g., "John")
            domain: The domain to search (e.g., "example.com")
            
        Returns:
            FinderResponse object with finder results
            
        Raises:
            EmailVerifyClientException: If name or domain is empty
            EmailVerifyException: For API errors
        """
        if not name or not name.strip():
            raise EmailVerifyClientException("Name is required")
        
        if not domain or not domain.strip():
            raise EmailVerifyClientException("Domain is required")

        params = {
            'name': name.strip(),
            'domain': domain.strip()
        }
        
        data = self._make_request('GET', '/finder', params=params)
        return FinderResponse(data)
