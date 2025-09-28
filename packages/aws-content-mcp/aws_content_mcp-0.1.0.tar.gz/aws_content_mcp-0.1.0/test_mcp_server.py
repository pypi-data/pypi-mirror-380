#!/usr/bin/env python3
"""Test script for AWS Content MCP Server"""

import asyncio
import json
import subprocess
import sys
from typing import Dict, Any


async def test_mcp_server():
    """Test the MCP server by sending JSON-RPC requests"""
    
    print("🧪 Testing AWS Content MCP Server...")
    print("=" * 50)
    
    # Test 1: List tools
    print("\n1. Testing tools/list...")
    list_tools_request = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/list"
    }
    
    result = await send_mcp_request(list_tools_request)
    if result and "result" in result:
        tools = result["result"]["tools"]
        print(f"✅ Found {len(tools)} tools:")
        for tool in tools:
            print(f"   - {tool['name']}: {tool['description'][:60]}...")
    else:
        print("❌ Failed to list tools")
        return False
    
    # Test 2: Search AWS content
    print("\n2. Testing search_aws_content...")
    search_request = {
        "jsonrpc": "2.0",
        "id": 2,
        "method": "tools/call",
        "params": {
            "name": "search_aws_content",
            "arguments": {
                "query": "lambda",
                "content_type": "products"
            }
        }
    }
    
    result = await send_mcp_request(search_request)
    if result and "result" in result:
        content = result["result"]["content"]
        if content and len(content) > 0:
            print(f"✅ Search successful, got response: {content[0]['text'][:100]}...")
        else:
            print("⚠️  Search returned empty content")
    else:
        print("❌ Search failed")
    
    # Test 3: Get AWS service overview
    print("\n3. Testing get_aws_service_overview...")
    overview_request = {
        "jsonrpc": "2.0",
        "id": 3,
        "method": "tools/call",
        "params": {
            "name": "get_aws_service_overview",
            "arguments": {}
        }
    }
    
    result = await send_mcp_request(overview_request)
    if result and "result" in result:
        content = result["result"]["content"]
        if content and len(content) > 0:
            print(f"✅ Service overview successful, got response: {content[0]['text'][:100]}...")
        else:
            print("⚠️  Service overview returned empty content")
    else:
        print("❌ Service overview failed")
    
    # Test 4: Analyze blog ideas
    print("\n4. Testing analyze_aws_blog_ideas...")
    blog_request = {
        "jsonrpc": "2.0",
        "id": 4,
        "method": "tools/call",
        "params": {
            "name": "analyze_aws_blog_ideas",
            "arguments": {
                "topic": "serverless computing",
                "check_duplicates": True
            }
        }
    }
    
    result = await send_mcp_request(blog_request)
    if result and "result" in result:
        content = result["result"]["content"]
        if content and len(content) > 0:
            print(f"✅ Blog analysis successful, got response: {content[0]['text'][:100]}...")
        else:
            print("⚠️  Blog analysis returned empty content")
    else:
        print("❌ Blog analysis failed")
    
    print("\n" + "=" * 50)
    print("🎉 MCP Server testing completed!")
    return True


async def send_mcp_request(request: Dict[str, Any]) -> Dict[str, Any]:
    """Send a JSON-RPC request to the MCP server"""
    try:
        # Start the MCP server process
        process = subprocess.Popen(
            ["aws-content-mcp"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Send the request
        request_json = json.dumps(request) + "\n"
        stdout, stderr = process.communicate(input=request_json, timeout=30)
        
        if stderr:
            print(f"⚠️  Server stderr: {stderr}")
        
        if stdout:
            # Parse the response
            try:
                response = json.loads(stdout.strip())
                return response
            except json.JSONDecodeError as e:
                print(f"❌ Failed to parse JSON response: {e}")
                print(f"Raw stdout: {stdout}")
                return {}
        else:
            print("❌ No response from server")
            return {}
            
    except subprocess.TimeoutExpired:
        print("❌ Request timed out")
        process.kill()
        return {}
    except Exception as e:
        print(f"❌ Error sending request: {e}")
        return {}


if __name__ == "__main__":
    asyncio.run(test_mcp_server())