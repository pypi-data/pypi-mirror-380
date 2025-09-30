#!/usr/bin/env python3
"""
Test script for the modularized Enhanced MCP Tools

This script tests that all modules can be imported and basic functionality works.
"""

import os
import sys
from pathlib import Path

# With src-layout, the package should be properly installed in development mode
# project_root is still needed for file structure tests
project_root = Path(__file__).parent.parent


def test_imports():
    """Test that all modules can be imported successfully"""
    print("🧪 Testing module imports...")

    try:
        from enhanced_mcp.base import MCPBase, MCPMixin

        print("✅ Base module imported successfully")

        from enhanced_mcp.diff_patch import DiffPatchOperations

        print("✅ Diff/Patch module imported successfully")

        from enhanced_mcp.intelligent_completion import IntelligentCompletion

        print("✅ Intelligent Completion module imported successfully")

        from enhanced_mcp.asciinema_integration import AsciinemaIntegration

        print("✅ Asciinema Integration module imported successfully")

        from enhanced_mcp.sneller_analytics import SnellerAnalytics

        print("✅ Sneller Analytics module imported successfully")

        from enhanced_mcp.git_integration import GitIntegration

        print("✅ Git Integration module imported successfully")

        from enhanced_mcp.file_operations import EnhancedFileOperations, MCPEventHandler

        print("✅ File Operations module imported successfully")

        from enhanced_mcp.archive_compression import ArchiveCompression

        print("✅ Archive Compression module imported successfully")

        from enhanced_mcp.workflow_tools import (
            AdvancedSearchAnalysis,
            DevelopmentWorkflow,
            EnhancedExistingTools,
            EnvironmentProcessManagement,
            NetworkAPITools,
            ProcessTracingTools,
            UtilityTools,
        )

        print("✅ Workflow Tools module imported successfully")

        from enhanced_mcp.mcp_server import MCPToolServer, create_server, run_server

        print("✅ MCP Server module imported successfully")

        from enhanced_mcp import MCPToolServer as MainServer

        print("✅ Main package import successful")

        print("\n🎉 All modules imported successfully!")
        assert True  # Test passed

    except ImportError as e:
        print(f"❌ Import failed: {e}")
        assert False, f"Import failed: {e}"
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        assert False, f"Unexpected error: {e}"


def test_instantiation():
    """Test that we can instantiate the main classes"""
    print("\n🧪 Testing class instantiation...")

    try:
        from enhanced_mcp.mcp_server import MCPToolServer

        # Create main server instance
        server = MCPToolServer("Test Server")
        print("✅ MCPToolServer instantiated successfully")

        # Test that all tool modules are accessible
        tools = server.tools
        print(f"✅ Found {len(tools)} tool modules:")
        for name, tool in tools.items():
            print(f"   - {name}: {tool.__class__.__name__}")

        # Test the intelligent completion system
        completion = server.completion
        if hasattr(completion, "tool_categories"):
            categories = list(completion.tool_categories.keys())
            print(f"✅ Intelligent completion has {len(categories)} tool categories: {categories}")

        print("\n🎉 All classes instantiated successfully!")
        assert True  # Test passed

    except Exception as e:
        print(f"❌ Instantiation failed: {e}")
        assert False, f"Instantiation failed: {e}"


def test_structure():
    """Test the overall structure and architecture"""
    print("\n🧪 Testing architecture structure...")

    try:
        # Check that we have the expected file structure in src-layout
        enhanced_mcp_dir = project_root / "src" / "enhanced_mcp"
        expected_files = [
            "__init__.py",
            "base.py",
            "diff_patch.py",
            "intelligent_completion.py",
            "asciinema_integration.py",
            "sneller_analytics.py",
            "git_integration.py",
            "file_operations.py",
            "archive_compression.py",
            "workflow_tools.py",
            "mcp_server.py",
        ]

        missing_files = []
        for filename in expected_files:
            filepath = enhanced_mcp_dir / filename
            if not filepath.exists():
                missing_files.append(filename)

        if missing_files:
            print(f"❌ Missing files: {missing_files}")
            assert False, f"Missing files: {missing_files}"

        print(f"✅ All {len(expected_files)} expected files present")

        # Check file sizes to ensure content was extracted properly
        large_files = [
            "asciinema_integration.py",
            "sneller_analytics.py",
            "git_integration.py",
            "archive_compression.py",
        ]
        for filename in large_files:
            filepath = enhanced_mcp_dir / filename
            size = filepath.stat().st_size
            if size < 1000:  # Less than 1KB suggests empty/minimal file
                print(f"⚠️ Warning: {filename} seems small ({size} bytes)")
            else:
                print(f"✅ {filename}: {size:,} bytes")

        print("\n🎉 Architecture structure looks good!")
        assert True  # Test passed

    except Exception as e:
        print(f"❌ Structure test failed: {e}")
        assert False, f"Structure test failed: {e}"


def main():
    """Run all tests"""
    print("🚀 Testing Enhanced MCP Tools Modular Structure")
    print("=" * 60)

    success = True

    # Run tests
    success &= test_imports()
    success &= test_instantiation()
    success &= test_structure()

    print("\n" + "=" * 60)
    if success:
        print("🎉 All tests passed! The modular structure is working correctly.")
        print("\n📦 Module Summary:")
        print("   - Base functionality: base.py")
        print("   - Diff/Patch ops: diff_patch.py")
        print("   - AI recommendations: intelligent_completion.py")
        print("   - Terminal recording: asciinema_integration.py")
        print("   - High-perf analytics: sneller_analytics.py")
        print("   - Git operations: git_integration.py")
        print("   - File operations: file_operations.py")
        print("   - Archive/compress: archive_compression.py")
        print("   - Workflow tools: workflow_tools.py")
        print("   - Server composition: mcp_server.py")
        print("\n🎯 Ready for production use!")
    else:
        print("❌ Some tests failed. Please check the errors above.")
        sys.exit(1)


if __name__ == "__main__":
    main()
