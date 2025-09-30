#!/usr/bin/env python3
"""Simple test for MCP server functionality"""

import asyncio
import json
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from aws_content_mcp.server import handle_list_tools, handle_call_tool


async def test_server_functions():
    """Test the server functions directly"""
    
    print("🧪 Testing AWS Content MCP Server Functions...")
    print("=" * 50)
    
    # Test 1: List tools
    print("\n1. Testing handle_list_tools...")
    try:
        tools = await handle_list_tools()
        print(f"✅ Found {len(tools)} tools:")
        for tool in tools:
            print(f"   - {tool.name}: {tool.description[:60]}...")
    except Exception as e:
        print(f"❌ Error listing tools: {e}")
        return False
    
    # Test 2: Test search with mock (since we don't have internet access in test)
    print("\n2. Testing search_aws_content (will show error due to network)...")
    try:
        result = await handle_call_tool("search_aws_content", {
            "query": "lambda",
            "content_type": "products"
        })
        print(f"✅ Search function executed, result type: {type(result)}")
        if result and len(result) > 0:
            print(f"   Response preview: {result[0].text[:100]}...")
    except Exception as e:
        print(f"❌ Error in search: {e}")
    
    # Test 3: Test invalid tool
    print("\n3. Testing invalid tool...")
    try:
        result = await handle_call_tool("invalid_tool", {})
        print(f"✅ Invalid tool handled gracefully")
        if result and len(result) > 0:
            print(f"   Response: {result[0].text}")
    except Exception as e:
        print(f"❌ Error handling invalid tool: {e}")
    
    # Test 4: Test missing parameters
    print("\n4. Testing missing parameters...")
    try:
        result = await handle_call_tool("search_aws_content", {})
        print(f"✅ Missing parameters handled gracefully")
        if result and len(result) > 0:
            print(f"   Response: {result[0].text}")
    except Exception as e:
        print(f"❌ Error handling missing parameters: {e}")
    
    print("\n" + "=" * 50)
    print("🎉 Function testing completed!")
    return True


if __name__ == "__main__":
    asyncio.run(test_server_functions())