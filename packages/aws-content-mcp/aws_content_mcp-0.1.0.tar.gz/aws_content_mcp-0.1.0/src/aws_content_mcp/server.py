"""AWS Content MCP Server - Main server implementation"""

import asyncio
import logging
from typing import Any, Sequence
from mcp.server import Server
from mcp.server.models import InitializationOptions
from mcp.server.stdio import stdio_server
from mcp.types import (
    Resource,
    Tool,
    TextContent,
    ImageContent,
    EmbeddedResource,
    LoggingLevel
)
from pydantic import AnyUrl
import json

from .content_fetcher import AWSContentFetcher

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("aws-content-mcp")

# Create the server instance
server = Server("aws-content-mcp")


@server.list_tools()
async def handle_list_tools() -> list[Tool]:
    """List available tools for AWS content retrieval"""
    return [
        Tool(
            name="search_aws_content",
            description="Search for AWS content including blogs, products, solutions, and pricing information",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search query for AWS content"
                    },
                    "content_type": {
                        "type": "string",
                        "enum": ["all", "blogs", "products", "solutions", "pricing"],
                        "default": "all",
                        "description": "Type of content to search for"
                    }
                },
                "required": ["query"]
            }
        ),
        Tool(
            name="get_full_aws_content",
            description="Get full detailed content from a specific AWS URL with complete analysis",
            inputSchema={
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "AWS URL to fetch full content from"
                    }
                },
                "required": ["url"]
            }
        ),
        Tool(
            name="analyze_aws_blog_ideas",
            description="Analyze AWS blog ideas for duplication and provide detailed content analysis",
            inputSchema={
                "type": "object",
                "properties": {
                    "topic": {
                        "type": "string",
                        "description": "Blog topic or idea to analyze"
                    },
                    "check_duplicates": {
                        "type": "boolean",
                        "default": True,
                        "description": "Whether to check for duplicate content"
                    }
                },
                "required": ["topic"]
            }
        ),
        Tool(
            name="get_aws_service_overview",
            description="Get comprehensive overview of all AWS services organized by category",
            inputSchema={
                "type": "object",
                "properties": {},
                "additionalProperties": False
            }
        ),
        Tool(
            name="compare_aws_content",
            description="Compare two pieces of AWS content for similarity and differences",
            inputSchema={
                "type": "object",
                "properties": {
                    "url1": {
                        "type": "string",
                        "description": "First AWS URL to compare"
                    },
                    "url2": {
                        "type": "string",
                        "description": "Second AWS URL to compare"
                    }
                },
                "required": ["url1", "url2"]
            }
        )
    ]


@server.call_tool()
async def handle_call_tool(name: str, arguments: dict[str, Any] | None) -> list[TextContent]:
    """Handle tool calls for AWS content operations"""
    
    if arguments is None:
        arguments = {}
    
    try:
        async with AWSContentFetcher() as fetcher:
            
            if name == "search_aws_content":
                query = arguments.get("query", "")
                content_type = arguments.get("content_type", "all")
                
                if not query:
                    return [TextContent(
                        type="text",
                        text="Error: Query parameter is required for searching AWS content."
                    )]
                
                results = await fetcher.search_aws_content(query, content_type)
                
                if not results:
                    return [TextContent(
                        type="text",
                        text=f"No AWS content found for query: '{query}' in category: '{content_type}'"
                    )]
                
                # Format results
                formatted_results = []
                formatted_results.append(f"Found {len(results)} AWS content items for '{query}':\n")
                
                for i, result in enumerate(results, 1):
                    formatted_results.append(f"{i}. **{result['title']}**")
                    formatted_results.append(f"   Type: {result['type'].title()}")
                    formatted_results.append(f"   URL: {result['url']}")
                    formatted_results.append(f"   Source: {result['source']}")
                    if result.get('excerpt'):
                        formatted_results.append(f"   Summary: {result['excerpt']}")
                    formatted_results.append("")
                
                return [TextContent(
                    type="text",
                    text="\n".join(formatted_results)
                )]
            
            elif name == "get_full_aws_content":
                url = arguments.get("url", "")
                
                if not url:
                    return [TextContent(
                        type="text",
                        text="Error: URL parameter is required for fetching full content."
                    )]
                
                if "aws.amazon.com" not in url:
                    return [TextContent(
                        type="text",
                        text="Error: URL must be from aws.amazon.com domain."
                    )]
                
                content = await fetcher.get_full_content(url)
                
                if "error" in content:
                    return [TextContent(
                        type="text",
                        text=f"Error fetching content: {content['error']}"
                    )]
                
                # Format the full content response
                response_parts = []
                response_parts.append(f"# {content['title']}\n")
                response_parts.append(f"**URL:** {content['url']}")
                response_parts.append(f"**Word Count:** {content['word_count']}")
                
                if content.get('publication_date'):
                    response_parts.append(f"**Published:** {content['publication_date']}")
                
                if content.get('meta_description'):
                    response_parts.append(f"**Description:** {content['meta_description']}")
                
                response_parts.append(f"**Extracted:** {content['extracted_at']}\n")
                response_parts.append("## Content\n")
                response_parts.append(content['markdown_content'])
                
                return [TextContent(
                    type="text",
                    text="\n".join(response_parts)
                )]
            
            elif name == "analyze_aws_blog_ideas":
                topic = arguments.get("topic", "")
                check_duplicates = arguments.get("check_duplicates", True)
                
                if not topic:
                    return [TextContent(
                        type="text",
                        text="Error: Topic parameter is required for blog analysis."
                    )]
                
                # Search for existing blog content
                blog_results = await fetcher.search_aws_content(topic, "blogs")
                
                analysis_parts = []
                analysis_parts.append(f"# Blog Idea Analysis: '{topic}'\n")
                
                if check_duplicates and blog_results:
                    analysis_parts.append(f"## Potential Duplicates Found ({len(blog_results)} items)\n")
                    
                    for i, blog in enumerate(blog_results, 1):
                        analysis_parts.append(f"{i}. **{blog['title']}**")
                        analysis_parts.append(f"   URL: {blog['url']}")
                        if blog.get('excerpt'):
                            analysis_parts.append(f"   Summary: {blog['excerpt']}")
                        analysis_parts.append("")
                    
                    # Get detailed content for similarity analysis
                    if blog_results:
                        analysis_parts.append("## Detailed Content Analysis\n")
                        
                        for blog in blog_results[:3]:  # Analyze top 3 results
                            detailed_content = await fetcher.get_full_content(blog['url'])
                            if 'content' in detailed_content:
                                analysis_parts.append(f"### {blog['title']}")
                                analysis_parts.append(f"**Word Count:** {detailed_content.get('word_count', 'Unknown')}")
                                analysis_parts.append(f"**URL:** {blog['url']}")
                                
                                # Extract key topics/themes
                                content_preview = detailed_content['content'][:500] + "..."
                                analysis_parts.append(f"**Content Preview:** {content_preview}")
                                analysis_parts.append("")
                
                else:
                    analysis_parts.append("## No Duplicate Content Found")
                    analysis_parts.append(f"Your blog idea '{topic}' appears to be unique in AWS blog content.")
                    analysis_parts.append("This could be a great opportunity for original content!")
                
                # Provide recommendations
                analysis_parts.append("\n## Recommendations\n")
                if blog_results:
                    analysis_parts.append("- Consider a unique angle or specific use case")
                    analysis_parts.append("- Focus on recent developments or updates")
                    analysis_parts.append("- Add practical examples or case studies")
                    analysis_parts.append("- Target a specific audience or industry")
                else:
                    analysis_parts.append("- This appears to be an underexplored topic")
                    analysis_parts.append("- Great opportunity for thought leadership")
                    analysis_parts.append("- Consider comprehensive coverage of the topic")
                
                return [TextContent(
                    type="text",
                    text="\n".join(analysis_parts)
                )]
            
            elif name == "get_aws_service_overview":
                overview = await fetcher.get_aws_service_overview()
                
                if "error" in overview:
                    return [TextContent(
                        type="text",
                        text=f"Error getting AWS service overview: {overview['error']}"
                    )]
                
                response_parts = []
                response_parts.append("# AWS Services Overview\n")
                response_parts.append(f"**Total Services:** {overview['total_services']}")
                response_parts.append(f"**Last Updated:** {overview['extracted_at']}\n")
                
                for category, services in overview['services_by_category'].items():
                    response_parts.append(f"## {category} ({len(services)} services)\n")
                    
                    for service in services[:10]:  # Limit to first 10 per category
                        response_parts.append(f"- **{service['name']}** - {service['url']}")
                    
                    if len(services) > 10:
                        response_parts.append(f"  ... and {len(services) - 10} more services")
                    
                    response_parts.append("")
                
                return [TextContent(
                    type="text",
                    text="\n".join(response_parts)
                )]
            
            elif name == "compare_aws_content":
                url1 = arguments.get("url1", "")
                url2 = arguments.get("url2", "")
                
                if not url1 or not url2:
                    return [TextContent(
                        type="text",
                        text="Error: Both url1 and url2 parameters are required for comparison."
                    )]
                
                if "aws.amazon.com" not in url1 or "aws.amazon.com" not in url2:
                    return [TextContent(
                        type="text",
                        text="Error: Both URLs must be from aws.amazon.com domain."
                    )]
                
                # Fetch both contents
                content1 = await fetcher.get_full_content(url1)
                content2 = await fetcher.get_full_content(url2)
                
                if "error" in content1 or "error" in content2:
                    return [TextContent(
                        type="text",
                        text=f"Error fetching content: {content1.get('error', '')} {content2.get('error', '')}"
                    )]
                
                # Calculate similarity
                similarity = await fetcher.analyze_content_similarity(
                    content1['content'], content2['content']
                )
                
                comparison_parts = []
                comparison_parts.append("# AWS Content Comparison\n")
                comparison_parts.append(f"**Similarity Score:** {similarity:.2%}\n")
                
                comparison_parts.append("## Content 1")
                comparison_parts.append(f"**Title:** {content1['title']}")
                comparison_parts.append(f"**URL:** {content1['url']}")
                comparison_parts.append(f"**Word Count:** {content1['word_count']}")
                comparison_parts.append("")
                
                comparison_parts.append("## Content 2")
                comparison_parts.append(f"**Title:** {content2['title']}")
                comparison_parts.append(f"**URL:** {content2['url']}")
                comparison_parts.append(f"**Word Count:** {content2['word_count']}")
                comparison_parts.append("")
                
                comparison_parts.append("## Analysis")
                if similarity > 0.7:
                    comparison_parts.append("- **High similarity** - Content covers very similar topics")
                elif similarity > 0.4:
                    comparison_parts.append("- **Moderate similarity** - Some overlapping topics")
                else:
                    comparison_parts.append("- **Low similarity** - Content covers different topics")
                
                return [TextContent(
                    type="text",
                    text="\n".join(comparison_parts)
                )]
            
            else:
                return [TextContent(
                    type="text",
                    text=f"Unknown tool: {name}"
                )]
    
    except Exception as e:
        logger.error(f"Error in tool {name}: {e}")
        return [TextContent(
            type="text",
            text=f"Error executing {name}: {str(e)}"
        )]


async def main():
    """Main entry point for the server"""
    # Run the server using stdin/stdout streams
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="aws-content-mcp",
                server_version="0.1.0",
                capabilities=server.get_capabilities(),
            ),
        )


def cli_main():
    """CLI entry point that handles the async main function"""
    import sys
    if len(sys.argv) > 1 and sys.argv[1] in ['--help', '-h']:
        print("AWS Content MCP Server")
        print("")
        print("A Model Context Protocol server for retrieving AWS content from aws.amazon.com")
        print("")
        print("Usage:")
        print("  aws-content-mcp                 # Run as MCP server")
        print("  aws-content-mcp --help          # Show this help")
        print("")
        print("This server provides tools for:")
        print("  - Searching AWS content (blogs, products, solutions, pricing)")
        print("  - Getting full content from AWS URLs")
        print("  - Analyzing blog ideas for duplicates")
        print("  - Comparing AWS content")
        print("  - Getting AWS service overviews")
        print("")
        print("Configure in your MCP client:")
        print('  {"command": "uvx", "args": ["aws-content-mcp"]}')
        return
    
    asyncio.run(main())


if __name__ == "__main__":
    asyncio.run(main())