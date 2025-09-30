"""Tests for MCP server"""

import pytest
import asyncio
from unittest.mock import Mock, patch, AsyncMock
from aws_content_mcp.server import handle_list_tools, handle_call_tool


@pytest.mark.asyncio
async def test_list_tools():
    """Test listing available tools"""
    tools = await handle_list_tools()
    
    assert isinstance(tools, list)
    assert len(tools) == 5
    
    tool_names = [tool.name for tool in tools]
    expected_tools = [
        "search_aws_content",
        "get_full_aws_content", 
        "analyze_aws_blog_ideas",
        "get_aws_service_overview",
        "compare_aws_content"
    ]
    
    for expected_tool in expected_tools:
        assert expected_tool in tool_names


@pytest.mark.asyncio
async def test_search_aws_content_tool():
    """Test search_aws_content tool"""
    with patch('aws_content_mcp.server.AWSContentFetcher') as mock_fetcher_class:
        mock_fetcher = AsyncMock()
        mock_fetcher.__aenter__.return_value = mock_fetcher
        mock_fetcher.__aexit__.return_value = None
        mock_fetcher.search_aws_content.return_value = [
            {
                "title": "Test Blog Post",
                "url": "https://aws.amazon.com/blog/test",
                "type": "blog",
                "excerpt": "Test excerpt",
                "source": "AWS Blog"
            }
        ]
        mock_fetcher_class.return_value = mock_fetcher
        
        result = await handle_call_tool("search_aws_content", {"query": "test"})
        
        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0].type == "text"
        assert "Test Blog Post" in result[0].text


@pytest.mark.asyncio
async def test_get_full_aws_content_tool():
    """Test get_full_aws_content tool"""
    with patch('aws_content_mcp.server.AWSContentFetcher') as mock_fetcher_class:
        mock_fetcher = AsyncMock()
        mock_fetcher.__aenter__.return_value = mock_fetcher
        mock_fetcher.__aexit__.return_value = None
        mock_fetcher.get_full_content.return_value = {
            "url": "https://aws.amazon.com/test",
            "title": "Test Page",
            "content": "Test content",
            "markdown_content": "# Test Page\nTest content",
            "word_count": 2,
            "extracted_at": "2024-01-01T00:00:00"
        }
        mock_fetcher_class.return_value = mock_fetcher
        
        result = await handle_call_tool("get_full_aws_content", {
            "url": "https://aws.amazon.com/test"
        })
        
        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0].type == "text"
        assert "Test Page" in result[0].text


@pytest.mark.asyncio
async def test_invalid_tool():
    """Test calling invalid tool"""
    result = await handle_call_tool("invalid_tool", {})
    
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0].type == "text"
    assert "Unknown tool" in result[0].text


@pytest.mark.asyncio
async def test_missing_required_parameter():
    """Test calling tool with missing required parameter"""
    result = await handle_call_tool("search_aws_content", {})
    
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0].type == "text"
    assert "Error" in result[0].text