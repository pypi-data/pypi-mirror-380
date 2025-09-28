"""
AiCV Python SDK Client

Main client class for interacting with the AiCV API.
"""

import httpx
from typing import Optional, Dict, Any, Union
from .exceptions import AiCVError, AuthenticationError, APIError, ValidationError


class AiCVClient:
    """
    Main client for interacting with the AiCV API.
    
    This client provides methods to get resume suggestions based on job requirements.
    """
    
    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.aicv.chat",
        timeout: float = 600.0,
        **kwargs
    ):
        """
        Initialize the AiCV client.
        
        Args:
            api_key: Your AiCV API key
            base_url: Base URL for the API (default: https://api.aicv.chat)
            timeout: Request timeout in seconds (default: 600.0)
            **kwargs: Additional arguments passed to httpx.Client
        """
        if not api_key:
            raise ValidationError("API key is required")
        
        self.api_key = api_key
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        
        # Set up default headers
        headers = {
            "accept": "application/json",
            "X-API-Key": api_key,
            "Content-Type": "application/json",
            "User-Agent": f"aicv-python/{__import__('aicv').__version__}"
        }
        
        # Create httpx client (SSL verification is enabled by default - recommended for security)
        self.client = httpx.Client(
            base_url=self.base_url,
            headers=headers,
            timeout=timeout,
            **kwargs
        )
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()
    
    def close(self):
        """Close the HTTP client."""
        if hasattr(self, 'client'):
            self.client.close()
    
    def _make_request(
        self,
        method: str,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Make an HTTP request to the API.
        
        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            endpoint: API endpoint
            data: Request body data
            params: Query parameters
            **kwargs: Additional arguments for httpx
            
        Returns:
            Response data as dictionary
            
        Raises:
            AuthenticationError: If authentication fails
            APIError: If API returns an error
            AiCVError: For other client errors
        """
        try:
            response = self.client.request(
                method=method,
                url=endpoint,
                json=data,
                params=params,
                **kwargs
            )
            
            # Handle authentication errors
            if response.status_code == 401:
                raise AuthenticationError("Invalid API key or authentication failed")
            
            # Handle other HTTP errors
            if response.status_code >= 400:
                try:
                    error_data = response.json()
                    error_message = error_data.get('message', f'HTTP {response.status_code} error')
                except:
                    error_message = f'HTTP {response.status_code} error'
                raise APIError(error_message, status_code=response.status_code)
            
            # Return JSON response
            return response.json()
            
        except httpx.RequestError as e:
            raise AiCVError(f"Request failed: {str(e)}")
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 401:
                raise AuthenticationError("Invalid API key or authentication failed")
            raise APIError(f"HTTP {e.response.status_code} error: {e.response.text}")
    
    def get_resume_suggestions(
        self,
        resume_text: str,
        job_title: str,
        job_description: str
    ) -> Dict[str, Any]:
        """
        Get resume suggestions based on job requirements.
        
        Args:
            resume_text: The resume text to analyze
            job_title: Target job title
            job_description: Job description for comparison
            
        Returns:
            Resume suggestions as dictionary
        """
        if not resume_text.strip():
            raise ValidationError("Resume text cannot be empty")
        
        if not job_title.strip():
            raise ValidationError("Job title is required")
        
        if not job_description.strip():
            raise ValidationError("Job description is required")
        
        data = {
            "resume_text": resume_text,
            "job_title": job_title,
            "job_description": job_description
        }
        
        return self._make_request("POST", "/api/v1/resume/suggestions/from-text", data=data)
