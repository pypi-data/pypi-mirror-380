"""Tests for AWS content fetcher"""

import pytest
import asyncio
from unittest.mock import Mock, patch, AsyncMock
from aws_content_mcp.content_fetcher import AWSContentFetcher


@pytest.mark.asyncio
async def test_search_aws_content():
    """Test searching AWS content"""
    async with AWSContentFetcher() as fetcher:
        # Mock the HTTP response
        with patch.object(fetcher.session, 'get') as mock_get:
            mock_response = Mock()
            mock_response.text = """
            <html>
                <body>
                    <article class="blog-post">
                        <h2 class="title">Test AWS Blog Post</h2>
                        <a href="/blog/test-post">Read more</a>
                        <p class="excerpt">This is a test blog post about AWS services.</p>
                    </article>
                </body>
            </html>
            """
            mock_response.raise_for_status = Mock()
            mock_get.return_value = mock_response
            
            results = await fetcher.search_aws_content("test", "blogs")
            
            assert isinstance(results, list)
            # Results might be empty due to simplified mock, but function should not error


@pytest.mark.asyncio
async def test_get_full_content():
    """Test getting full content from URL"""
    async with AWSContentFetcher() as fetcher:
        with patch.object(fetcher.session, 'get') as mock_get:
            mock_response = Mock()
            mock_response.text = """
            <html>
                <head>
                    <title>Test AWS Page</title>
                    <meta name="description" content="Test description">
                </head>
                <body>
                    <h1>Test AWS Page</h1>
                    <p>This is test content from AWS.</p>
                </body>
            </html>
            """
            mock_response.raise_for_status = Mock()
            mock_get.return_value = mock_response
            
            content = await fetcher.get_full_content("https://aws.amazon.com/test")
            
            assert "url" in content
            assert "title" in content
            assert "content" in content


@pytest.mark.asyncio
async def test_analyze_content_similarity():
    """Test content similarity analysis"""
    async with AWSContentFetcher() as fetcher:
        content1 = "AWS Lambda is a serverless computing service"
        content2 = "Lambda provides serverless computing on AWS"
        
        similarity = await fetcher.analyze_content_similarity(content1, content2)
        
        assert isinstance(similarity, float)
        assert 0.0 <= similarity <= 1.0


@pytest.mark.asyncio
async def test_get_aws_service_overview():
    """Test getting AWS service overview"""
    async with AWSContentFetcher() as fetcher:
        with patch.object(fetcher.session, 'get') as mock_get:
            mock_response = Mock()
            mock_response.text = """
            <html>
                <body>
                    <div class="category">
                        <h2>Compute</h2>
                        <a href="/products/ec2">Amazon EC2</a>
                        <a href="/products/lambda">AWS Lambda</a>
                    </div>
                </body>
            </html>
            """
            mock_response.raise_for_status = Mock()
            mock_get.return_value = mock_response
            
            overview = await fetcher.get_aws_service_overview()
            
            assert isinstance(overview, dict)
            assert "extracted_at" in overview