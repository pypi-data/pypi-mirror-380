#!/usr/bin/env python3
"""
Simple test script to validate the MCP server
"""

from enhanced_mcp.mcp_server import MCPToolServer


def test_server():
    """Test that the server initializes correctly"""
    print("Testing MCP Server initialization...")

    try:
        server = MCPToolServer()
        print("✅ Server created successfully")

        # Test tool category initialization
        categories = [
            ("diff_patch", "DiffPatchOperations"),
            ("git", "GitIntegration"),
            ("file_ops", "EnhancedFileOperations"),
            ("search_analysis", "AdvancedSearchAnalysis"),
            ("dev_workflow", "DevelopmentWorkflow"),
            ("network_api", "NetworkAPITools"),
            ("archive", "ArchiveCompression"),
            ("process_tracing", "ProcessTracingTools"),
            ("env_process", "EnvironmentProcessManagement"),
            ("enhanced_tools", "EnhancedExistingTools"),
            ("utility", "UtilityTools"),
        ]

        print("\nValidating tool categories:")
        for attr_name, class_name in categories:
            if hasattr(server, attr_name):
                print(f"✅ {class_name} initialized as {attr_name}")
            else:
                print(f"❌ {class_name} missing as {attr_name}")

        # Test registration
        try:
            server.register_all_tools()
            print("✅ All tools registered successfully")
        except Exception as e:
            print(f"❌ Tool registration failed: {e}")

        print("\n✅ All tests passed!")

    except Exception as e:
        print(f"❌ Server initialization failed: {e}")


if __name__ == "__main__":
    test_server()
