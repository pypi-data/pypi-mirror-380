#!/usr/bin/env python3
"""
Functional test for MCP tools
"""

import asyncio
import os
import tempfile
from pathlib import Path

from enhanced_mcp.mcp_server import MCPToolServer


async def test_functional():
    """Test actual tool functionality"""
    print("Testing MCP Tools Functionality")
    print("=" * 40)

    server = MCPToolServer()
    # Tools are automatically registered when the server is created

    # Test 1: Environment Info
    print("\n1. Testing environment_info...")
    try:
        result = await server.env_process.environment_info(["system", "python"])
        print(f"   ✅ Environment info: {len(result)} sections returned")
        print(f"   📊 Python version: {result.get('python', {}).get('version')}")
    except Exception as e:
        print(f"   ❌ Environment info failed: {e}")

    # Test 2: File backup
    print("\n2. Testing file_backup...")
    try:
        # Create a temporary file
        with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt") as f:
            f.write("Test content for backup")
            temp_file = f.name

        result = await server.file_ops.file_backup([temp_file])
        print(f"   ✅ File backup: {len(result)} backup(s) created")

        # Cleanup
        os.unlink(temp_file)
        for backup in result:
            if os.path.exists(backup):
                os.unlink(backup)

    except Exception as e:
        print(f"   ❌ File backup failed: {e}")

    # Test 3: HTTP Request
    print("\n3. Testing http_request...")
    try:
        result = await server.network_api.http_request(
            url="https://httpbin.org/json", method="GET", timeout=10
        )
        print(f"   ✅ HTTP request: Status {result.get('status_code')}")
        print(f"   📊 Response time: {result.get('elapsed_seconds', 0):.2f}s")
    except Exception as e:
        print(f"   ❌ HTTP request failed: {e}")

    # Test 4: Dependency Check
    print("\n4. Testing dependency_check...")
    try:
        result = await server.utility.dependency_check(".")
        deps = result.get("dependencies", {})
        print(f"   ✅ Dependency check: Found {len(deps)} dependency files")
        if "python" in deps:
            print(f"   📦 Python deps: {len(deps['python'])} found")
    except Exception as e:
        print(f"   ❌ Dependency check failed: {e}")

    print("\n" + "=" * 40)
    print("✅ Functional testing complete!")


if __name__ == "__main__":
    asyncio.run(test_functional())
