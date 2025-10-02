#!/usr/bin/env python3
"""
Basic tests for Sheetsight client
"""

import pytest
from unittest.mock import Mock, patch
import httpx

from sheetsight_py import (
    SheetsightClient,
    AuthenticationError,
    APIError,
    TimeoutError,
    SheetsightError
)


def test_client_initialization():
    """Test client initialization"""
    client = SheetsightClient(api_key="test_key")
    assert client.api_key == "test_key"
    assert client.base_url == "https://sheetsight.ai"
    assert client.timeout == 30.0
    client.close()


def test_client_initialization_with_custom_params():
    """Test client initialization with custom parameters"""
    client = SheetsightClient(
        api_key="test_key",
        base_url="https://custom.api.com",
        timeout=60.0
    )
    assert client.api_key == "test_key"
    assert client.base_url == "https://custom.api.com"
    assert client.timeout == 60.0
    client.close()


def test_client_initialization_without_api_key():
    """Test client initialization fails without API key"""
    with pytest.raises(ValueError, match="API key is required"):
        SheetsightClient(api_key="")


def test_context_manager():
    """Test client as context manager"""
    with SheetsightClient(api_key="test_key") as client:
        assert client.api_key == "test_key"


@patch('httpx.Client.post')
def test_global_search_success(mock_post):
    """Test successful global search"""
    # Mock response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "query": "ESP32",
        "total_results": 5,
        "total_parts": 2,
        "processing_time_ms": 150,
        "grouped_results": [],
        "metadata": {
            "vector_search_results": 10,
            "parts_with_matches": 2,
            "avg_matches_per_part": 2.5
        }
    }
    mock_post.return_value = mock_response
    
    with SheetsightClient(api_key="test_key") as client:
        result = client.global_search("ESP32")
        
        assert result["query"] == "ESP32"
        assert result["total_results"] == 5
        assert result["total_parts"] == 2
        
        # Verify request was made correctly
        mock_post.assert_called_once()
        call_args = mock_post.call_args
        assert call_args[0][0] == "https://sheetsight.ai/api/search"
        assert call_args[1]["json"]["searchQuery"] == "ESP32"


@patch('httpx.Client.post')
def test_global_search_with_options(mock_post):
    """Test global search with options"""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"query": "test", "total_results": 0, "total_parts": 0, "processing_time_ms": 100, "grouped_results": [], "metadata": {"vector_search_results": 0, "parts_with_matches": 0, "avg_matches_per_part": 0}}
    mock_post.return_value = mock_response
    
    options = {
        "maxResults": 10,
        "groupByPart": False,
        "timeoutMs": 8000
    }
    
    with SheetsightClient(api_key="test_key") as client:
        client.global_search("test query", options)
        
        call_args = mock_post.call_args
        payload = call_args[1]["json"]
        assert payload["maxResults"] == 10
        assert payload["groupByPart"] == False
        assert payload["timeoutMs"] == 8000


@patch('httpx.Client.post')
def test_search_convenience_method(mock_post):
    """Test convenience search method"""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"query": "test", "total_results": 0, "total_parts": 0, "processing_time_ms": 100, "grouped_results": [], "metadata": {"vector_search_results": 0, "parts_with_matches": 0, "avg_matches_per_part": 0}}
    mock_post.return_value = mock_response
    
    with SheetsightClient(api_key="test_key") as client:
        client.search("test query", max_results=15, group_by_part=False)
        
        call_args = mock_post.call_args
        payload = call_args[1]["json"]
        assert payload["maxResults"] == 15
        assert payload["groupByPart"] == False


@patch('httpx.Client.post')
def test_authentication_error(mock_post):
    """Test authentication error handling"""
    mock_response = Mock()
    mock_response.status_code = 401
    mock_post.return_value = mock_response
    
    with SheetsightClient(api_key="invalid_key") as client:
        with pytest.raises(AuthenticationError, match="Invalid API key"):
            client.global_search("test")


@patch('httpx.Client.post')
def test_api_error(mock_post):
    """Test API error handling"""
    mock_response = Mock()
    mock_response.status_code = 400
    mock_response.json.return_value = {"error": "Bad request"}
    mock_post.return_value = mock_response
    
    with SheetsightClient(api_key="test_key") as client:
        with pytest.raises(APIError, match="Bad request"):
            client.global_search("test")


@patch('httpx.Client.post')
def test_timeout_error(mock_post):
    """Test timeout error handling"""
    mock_post.side_effect = httpx.TimeoutException("Request timed out")
    
    with SheetsightClient(api_key="test_key") as client:
        with pytest.raises(TimeoutError, match="Request timed out"):
            client.global_search("test")


def test_empty_search_query():
    """Test empty search query validation"""
    with SheetsightClient(api_key="test_key") as client:
        with pytest.raises(ValueError, match="Search query cannot be empty"):
            client.global_search("")
        
        with pytest.raises(ValueError, match="Search query cannot be empty"):
            client.global_search("   ")


