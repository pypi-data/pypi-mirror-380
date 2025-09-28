"""Usage examples for AWS Content MCP Server"""

import asyncio
import json
from aws_content_mcp.content_fetcher import AWSContentFetcher


async def example_search_content():
    """Example: Search for AWS content"""
    print("=== Searching for AWS Lambda content ===")
    
    async with AWSContentFetcher() as fetcher:
        results = await fetcher.search_aws_content("lambda", "all")
        
        print(f"Found {len(results)} results:")
        for i, result in enumerate(results[:5], 1):
            print(f"{i}. {result['title']}")
            print(f"   Type: {result['type']}")
            print(f"   URL: {result['url']}")
            print(f"   Excerpt: {result.get('excerpt', 'No excerpt')[:100]}...")
            print()


async def example_get_full_content():
    """Example: Get full content from AWS URL"""
    print("=== Getting full content from AWS Lambda page ===")
    
    async with AWSContentFetcher() as fetcher:
        # This would work with a real AWS URL
        url = "https://aws.amazon.com/lambda/"
        content = await fetcher.get_full_content(url)
        
        if "error" not in content:
            print(f"Title: {content['title']}")
            print(f"Word Count: {content['word_count']}")
            print(f"Content Preview: {content['content'][:200]}...")
        else:
            print(f"Error: {content['error']}")


async def example_analyze_blog_ideas():
    """Example: Analyze blog ideas for duplicates"""
    print("=== Analyzing blog idea: 'Serverless Architecture' ===")
    
    async with AWSContentFetcher() as fetcher:
        # Search for existing content on the topic
        results = await fetcher.search_aws_content("serverless architecture", "blogs")
        
        print(f"Found {len(results)} existing blog posts on this topic:")
        for result in results[:3]:
            print(f"- {result['title']}")
            print(f"  URL: {result['url']}")
            
            # Get full content for similarity analysis
            full_content = await fetcher.get_full_content(result['url'])
            if "content" in full_content:
                print(f"  Word Count: {full_content['word_count']}")
                print(f"  Preview: {full_content['content'][:150]}...")
            print()


async def example_service_overview():
    """Example: Get AWS service overview"""
    print("=== Getting AWS Service Overview ===")
    
    async with AWSContentFetcher() as fetcher:
        overview = await fetcher.get_aws_service_overview()
        
        if "error" not in overview:
            print(f"Total Services: {overview['total_services']}")
            print("Categories:")
            for category, services in list(overview['services_by_category'].items())[:3]:
                print(f"  {category}: {len(services)} services")
                for service in services[:3]:
                    print(f"    - {service['name']}")
        else:
            print(f"Error: {overview['error']}")


async def example_compare_content():
    """Example: Compare two pieces of AWS content"""
    print("=== Comparing AWS content ===")
    
    async with AWSContentFetcher() as fetcher:
        # These would be real AWS URLs in practice
        url1 = "https://aws.amazon.com/lambda/"
        url2 = "https://aws.amazon.com/ec2/"
        
        content1 = await fetcher.get_full_content(url1)
        content2 = await fetcher.get_full_content(url2)
        
        if "error" not in content1 and "error" not in content2:
            similarity = await fetcher.analyze_content_similarity(
                content1['content'], content2['content']
            )
            
            print(f"Content 1: {content1['title']}")
            print(f"Content 2: {content2['title']}")
            print(f"Similarity: {similarity:.2%}")
            
            if similarity > 0.7:
                print("High similarity - content covers very similar topics")
            elif similarity > 0.4:
                print("Moderate similarity - some overlapping topics")
            else:
                print("Low similarity - content covers different topics")


async def main():
    """Run all examples"""
    examples = [
        example_search_content,
        example_get_full_content,
        example_analyze_blog_ideas,
        example_service_overview,
        example_compare_content
    ]
    
    for example in examples:
        try:
            await example()
            print("\n" + "="*50 + "\n")
        except Exception as e:
            print(f"Error in {example.__name__}: {e}")
            print("\n" + "="*50 + "\n")


if __name__ == "__main__":
    # Note: These examples will work better with actual network access
    # and real AWS URLs. For testing, you might want to mock the HTTP responses.
    print("AWS Content MCP Server - Usage Examples")
    print("Note: These examples require network access to aws.amazon.com")
    print()
    
    asyncio.run(main())