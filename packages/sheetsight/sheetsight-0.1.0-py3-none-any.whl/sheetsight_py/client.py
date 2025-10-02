"""
Sheetsight Python client implementation
"""

import json
from typing import Optional
from urllib.parse import urljoin

import httpx

from .exceptions import APIError, AuthenticationError, SheetsightError, TimeoutError
from .types import GlobalSearchOptions, GlobalSearchResponse


class SheetsightClient:
    """
    Simple client for the Sheetsight search API
    
    This client provides a minimal interface to the Sheetsight global search functionality.
    It handles API key authentication and returns typed responses.
    """
    
    DEFAULT_BASE_URL = "https://sheetsight.ai"
    DEFAULT_TIMEOUT = 30.0
    
    def __init__(
        self,
        api_key: str,
        base_url: Optional[str] = None,
        timeout: Optional[float] = None
    ):
        """
        Initialize the Sheetsight client
        
        Args:
            api_key: Your Sheetsight API key (get from https://sheetsight.ai/dashboard)
            base_url: Base URL for the Sheetsight API (defaults to https://sheetsight.ai)
            timeout: Request timeout in seconds (defaults to 30)
        """
        if not api_key:
            raise ValueError("API key is required")
            
        self.api_key = api_key
        self.base_url = base_url or self.DEFAULT_BASE_URL
        self.timeout = timeout or self.DEFAULT_TIMEOUT
        
        # Create HTTP client with default headers
        self._client = httpx.Client(
            timeout=self.timeout,
            headers={
                "Content-Type": "application/json",
                "x-api-key": self.api_key,
            }
        )
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
    
    def close(self):
        """Close the underlying HTTP client"""
        self._client.close()
    
    def global_search(
        self,
        search_query: str,
        options: Optional[GlobalSearchOptions] = None
    ) -> GlobalSearchResponse:
        """
        Perform a global search across all Sheetsight content
        
        Args:
            search_query: The search query string
            options: Optional search parameters (maxResults, groupByPart, etc.)
            
        Returns:
            GlobalSearchResponse with search results grouped by parts
            
        Raises:
            AuthenticationError: If API key is invalid
            APIError: If API returns an error
            TimeoutError: If request times out
            SheetsightError: For other client errors
        """
        if not search_query or not search_query.strip():
            raise ValueError("Search query cannot be empty")
        
        # Build request payload
        payload = {"searchQuery": search_query.strip()}
        
        # Add optional parameters if provided
        if options:
            if "maxResults" in options:
                payload["maxResults"] = options["maxResults"]
            if "maxMatchesPerPart" in options:
                payload["maxMatchesPerPart"] = options["maxMatchesPerPart"]
            if "includePartInfo" in options:
                payload["includePartInfo"] = options["includePartInfo"]
            if "groupByPart" in options:
                payload["groupByPart"] = options["groupByPart"]
        
        # Make API request
        url = urljoin(self.base_url, "/api/search")
        
        try:
            response = self._client.post(url, json=payload)
            
            # Handle different error cases
            if response.status_code == 401:
                raise AuthenticationError("Invalid API key")
            elif response.status_code == 429:
                raise APIError("Rate limit exceeded", response.status_code)
            elif response.status_code >= 400:
                try:
                    error_data = response.json()
                    error_message = error_data.get("error", f"HTTP {response.status_code}")
                except json.JSONDecodeError:
                    error_message = f"HTTP {response.status_code}: {response.text}"
                
                raise APIError(error_message, response.status_code, error_data if 'error_data' in locals() else None)
            
            # Parse successful response
            try:
                return response.json()
            except json.JSONDecodeError as e:
                raise SheetsightError(f"Invalid JSON response: {e}")
                
        except httpx.TimeoutException:
            raise TimeoutError("Request timed out")
        except httpx.RequestError as e:
            raise SheetsightError(f"Request failed: {e}")
    
    def search(
        self,
        query: str,
        max_results: int = 20,
        group_by_part: bool = True,
        **kwargs
    ) -> GlobalSearchResponse:
        """
        Convenience method for global search with simplified parameters
        
        Args:
            query: The search query string
            max_results: Maximum number of results to return (default: 20)
            group_by_part: Whether to group results by part (default: True)
            **kwargs: Additional options passed to global_search
            
        Returns:
            GlobalSearchResponse with search results
        """
        options: GlobalSearchOptions = {
            "maxResults": max_results,
            "groupByPart": group_by_part,
            **kwargs
        }
        
        return self.global_search(query, options)


