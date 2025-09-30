#!/usr/bin/env python3
"""
Comprehensive demo examples for AWS Content MCP Server

This script demonstrates all the capabilities of the AWS Content MCP Server
with real-world examples that users can expect when using the server.
"""

import asyncio
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from aws_content_mcp.server import handle_call_tool


async def demo_search_aws_content():
    """Demo: Search for AWS content across different categories"""
    print("🔍 DEMO: Searching AWS Content")
    print("=" * 60)
    
    examples = [
        ("lambda", "products", "Search for Lambda in AWS products"),
        ("serverless", "blogs", "Search for serverless content in blogs"),
        ("ec2 pricing", "pricing", "Search for EC2 pricing information"),
        ("machine learning", "solutions", "Search for ML solutions"),
        ("kubernetes", "all", "Search for Kubernetes across all content")
    ]
    
    for query, content_type, description in examples:
        print(f"\n📋 {description}")
        print(f"   Query: '{query}' | Type: '{content_type}'")
        
        try:
            result = await handle_call_tool("search_aws_content", {
                "query": query,
                "content_type": content_type
            })
            
            if result and len(result) > 0:
                response = result[0].text
                # Show first 200 characters
                preview = response[:200] + "..." if len(response) > 200 else response
                print(f"   ✅ Result: {preview}")
            else:
                print("   ⚠️  No results returned")
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
    
    print("\n" + "=" * 60)


async def demo_get_full_content():
    """Demo: Get full content from AWS URLs"""
    print("\n📄 DEMO: Getting Full AWS Content")
    print("=" * 60)
    
    # Example URLs (these would work with real AWS URLs)
    example_urls = [
        "https://aws.amazon.com/lambda/",
        "https://aws.amazon.com/ec2/",
        "https://aws.amazon.com/s3/",
    ]
    
    for url in example_urls:
        print(f"\n📋 Fetching content from: {url}")
        
        try:
            result = await handle_call_tool("get_full_aws_content", {
                "url": url
            })
            
            if result and len(result) > 0:
                response = result[0].text
                # Show first 300 characters
                preview = response[:300] + "..." if len(response) > 300 else response
                print(f"   ✅ Content preview: {preview}")
            else:
                print("   ⚠️  No content returned")
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
    
    print("\n" + "=" * 60)


async def demo_analyze_blog_ideas():
    """Demo: Analyze blog ideas for duplicates"""
    print("\n💡 DEMO: Analyzing Blog Ideas")
    print("=" * 60)
    
    blog_topics = [
        "Serverless Architecture Best Practices",
        "Machine Learning on AWS",
        "Container Security with ECS",
        "Cost Optimization Strategies",
        "Multi-Region Deployment Patterns"
    ]
    
    for topic in blog_topics:
        print(f"\n📋 Analyzing blog idea: '{topic}'")
        
        try:
            result = await handle_call_tool("analyze_aws_blog_ideas", {
                "topic": topic,
                "check_duplicates": True
            })
            
            if result and len(result) > 0:
                response = result[0].text
                # Show first 400 characters
                preview = response[:400] + "..." if len(response) > 400 else response
                print(f"   ✅ Analysis: {preview}")
            else:
                print("   ⚠️  No analysis returned")
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
    
    print("\n" + "=" * 60)


async def demo_service_overview():
    """Demo: Get AWS service overview"""
    print("\n🏗️  DEMO: AWS Service Overview")
    print("=" * 60)
    
    print("\n📋 Getting comprehensive AWS service overview...")
    
    try:
        result = await handle_call_tool("get_aws_service_overview", {})
        
        if result and len(result) > 0:
            response = result[0].text
            # Show first 500 characters
            preview = response[:500] + "..." if len(response) > 500 else response
            print(f"   ✅ Service overview: {preview}")
        else:
            print("   ⚠️  No overview returned")
            
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    print("\n" + "=" * 60)


async def demo_compare_content():
    """Demo: Compare AWS content"""
    print("\n⚖️  DEMO: Comparing AWS Content")
    print("=" * 60)
    
    # Example comparisons
    comparisons = [
        ("https://aws.amazon.com/lambda/", "https://aws.amazon.com/ec2/", "Lambda vs EC2"),
        ("https://aws.amazon.com/s3/", "https://aws.amazon.com/efs/", "S3 vs EFS"),
    ]
    
    for url1, url2, description in comparisons:
        print(f"\n📋 {description}")
        print(f"   Comparing: {url1}")
        print(f"        vs:  {url2}")
        
        try:
            result = await handle_call_tool("compare_aws_content", {
                "url1": url1,
                "url2": url2
            })
            
            if result and len(result) > 0:
                response = result[0].text
                # Show first 300 characters
                preview = response[:300] + "..." if len(response) > 300 else response
                print(f"   ✅ Comparison: {preview}")
            else:
                print("   ⚠️  No comparison returned")
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
    
    print("\n" + "=" * 60)


async def demo_error_handling():
    """Demo: Error handling capabilities"""
    print("\n🚨 DEMO: Error Handling")
    print("=" * 60)
    
    error_cases = [
        ("search_aws_content", {}, "Missing required query parameter"),
        ("get_full_aws_content", {"url": "https://example.com"}, "Non-AWS URL"),
        ("get_full_aws_content", {}, "Missing URL parameter"),
        ("invalid_tool", {}, "Invalid tool name"),
        ("compare_aws_content", {"url1": "https://aws.amazon.com/lambda/"}, "Missing url2 parameter")
    ]
    
    for tool_name, args, description in error_cases:
        print(f"\n📋 Testing: {description}")
        print(f"   Tool: {tool_name} | Args: {args}")
        
        try:
            result = await handle_call_tool(tool_name, args)
            
            if result and len(result) > 0:
                response = result[0].text
                print(f"   ✅ Error handled: {response}")
            else:
                print("   ⚠️  No error message returned")
                
        except Exception as e:
            print(f"   ❌ Unexpected error: {e}")
    
    print("\n" + "=" * 60)


async def main():
    """Run all demo examples"""
    print("🎯 AWS Content MCP Server - Comprehensive Demo")
    print("=" * 80)
    print("This demo shows all capabilities of the AWS Content MCP Server")
    print("Note: Some examples may show 'No content found' due to AWS website structure")
    print("=" * 80)
    
    demos = [
        demo_search_aws_content,
        demo_get_full_content,
        demo_analyze_blog_ideas,
        demo_service_overview,
        demo_compare_content,
        demo_error_handling
    ]
    
    for demo in demos:
        try:
            await demo()
            await asyncio.sleep(1)  # Brief pause between demos
        except Exception as e:
            print(f"❌ Demo {demo.__name__} failed: {e}")
    
    print("\n🎉 Demo completed!")
    print("\n📚 Usage Summary:")
    print("   • search_aws_content: Find AWS content by query and type")
    print("   • get_full_aws_content: Extract complete content from AWS URLs")
    print("   • analyze_aws_blog_ideas: Check for duplicate blog topics")
    print("   • get_aws_service_overview: Get comprehensive service listings")
    print("   • compare_aws_content: Compare similarity between AWS content")
    print("\n🚀 Ready for PyPI publication!")


if __name__ == "__main__":
    asyncio.run(main())