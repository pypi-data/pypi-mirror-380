"""
AiCV Python SDK Async Client

Async client class for interacting with the AiCV API with full async support.
"""

import asyncio
import httpx
from typing import Optional, Dict, Any, Union, List
from .exceptions import AiCVError, AuthenticationError, APIError, ValidationError


class AsyncAiCVClient:
    """
    Async client for interacting with the AiCV API.
    
    This client provides async methods to get resume suggestions based on job requirements.
    """
    
    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.aicv.chat",
        timeout: float = 600.0,
        max_retries: int = 3,
        retry_delay: float = 1.0,
        **kwargs
    ):
        """
        Initialize the async AiCV client.
        
        Args:
            api_key: Your AiCV API key
            base_url: Base URL for the API (default: https://api.aicv.chat)
            timeout: Request timeout in seconds (default: 600.0)
            max_retries: Maximum number of retries for failed requests (default: 3)
            retry_delay: Delay between retries in seconds (default: 1.0)
            **kwargs: Additional arguments passed to httpx.AsyncClient
        """
        if not api_key:
            raise ValidationError("API key is required")
        
        self.api_key = api_key
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        
        # Set up default headers
        headers = {
            "accept": "application/json",
            "X-API-Key": api_key,
            "Content-Type": "application/json",
            "User-Agent": f"aicv-python-async/{__import__('aicv').__version__}"
        }
        
        # Create async httpx client
        self.client = httpx.AsyncClient(
            base_url=self.base_url,
            headers=headers,
            timeout=timeout,
            **kwargs
        )
    
    async def __aenter__(self):
        """Async context manager entry."""
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.close()
    
    async def close(self):
        """Close the async HTTP client."""
        if hasattr(self, 'client'):
            await self.client.aclose()
    
    async def _make_request(
        self,
        method: str,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Make an async HTTP request to the API with retry logic.
        
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
        last_exception = None
        
        for attempt in range(self.max_retries + 1):
            try:
                response = await self.client.request(
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
                
            except (httpx.RequestError, httpx.HTTPStatusError, APIError, AuthenticationError) as e:
                last_exception = e
                
                # Don't retry authentication errors
                if isinstance(e, AuthenticationError):
                    raise e
                
                # Don't retry on last attempt
                if attempt == self.max_retries:
                    break
                
                # Wait before retry
                await asyncio.sleep(self.retry_delay * (attempt + 1))
        
        # Re-raise the last exception
        if isinstance(last_exception, httpx.RequestError):
            raise AiCVError(f"Request failed after {self.max_retries + 1} attempts: {str(last_exception)}")
        elif isinstance(last_exception, httpx.HTTPStatusError):
            raise APIError(f"HTTP {last_exception.response.status_code} error after {self.max_retries + 1} attempts: {last_exception.response.text}")
        else:
            raise last_exception
    
    async def get_resume_suggestions(
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
        
        return await self._make_request("POST", "/api/v1/resume/suggestions/from-text", data=data)
    
    async def batch_get_resume_suggestions(
        self,
        requests: List[Dict[str, str]]
    ) -> List[Dict[str, Any]]:
        """
        Get resume suggestions for multiple requests concurrently.
        
        Args:
            requests: List of request dictionaries with 'resume_text', 'job_title', 'job_description'
            
        Returns:
            List of resume suggestions dictionaries
        """
        if not requests:
            return []
        
        # Create tasks for concurrent execution
        tasks = []
        for req in requests:
            task = self.get_resume_suggestions(
                resume_text=req.get('resume_text', ''),
                job_title=req.get('job_title', ''),
                job_description=req.get('job_description', '')
            )
            tasks.append(task)
        
        # Execute all tasks concurrently
        try:
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            # Process results
            processed_results = []
            for i, result in enumerate(results):
                if isinstance(result, Exception):
                    processed_results.append({
                        'error': str(result),
                        'success': False,
                        'request_index': i
                    })
                else:
                    processed_results.append({
                        'result': result,
                        'success': True,
                        'request_index': i
                    })
            
            return processed_results
            
        except Exception as e:
            raise AiCVError(f"Batch request failed: {str(e)}")
    
    async def health_check(self) -> Dict[str, Any]:
        """
        Check the health of the AiCV API.
        
        Returns:
            Health status dictionary
        """
        try:
            response = await self.client.get("/api/v1/health")
            return response.json()
        except Exception as e:
            return {
                "status": "unhealthy",
                "error": str(e)
            }
    
    async def get_account_info(self) -> Dict[str, Any]:
        """
        Get account information.
        
        Returns:
            Account information dictionary
        """
        return await self._make_request("GET", "/api/v1/account")


# Convenience function for quick async usage
async def get_resume_suggestions_async(
    api_key: str,
    resume_text: str,
    job_title: str,
    job_description: str,
    **kwargs
) -> Dict[str, Any]:
    """
    Convenience function to get resume suggestions asynchronously.
    
    Args:
        api_key: Your AiCV API key
        resume_text: The resume text to analyze
        job_title: Target job title
        job_description: Job description for comparison
        **kwargs: Additional arguments for AsyncAiCVClient
        
    Returns:
        Resume suggestions as dictionary
    """
    async with AsyncAiCVClient(api_key=api_key, **kwargs) as client:
        return await client.get_resume_suggestions(
            resume_text=resume_text,
            job_title=job_title,
            job_description=job_description
        )
