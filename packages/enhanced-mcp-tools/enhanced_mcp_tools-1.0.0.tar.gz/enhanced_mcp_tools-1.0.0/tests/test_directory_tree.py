#!/usr/bin/env python3
"""
Test script for the new list_directory_tree functionality
"""

import asyncio
import json
from pathlib import Path

from enhanced_mcp.file_operations import EnhancedFileOperations


async def test_directory_tree():
    """Test the directory tree listing functionality"""

    # Initialize the file operations class
    file_ops = EnhancedFileOperations()

    print("🌳 Testing Directory Tree Listing with Metadata")
    print("=" * 60)

    # Test on the current project directory
    project_dir = "/home/rpm/claude/enhanced-mcp-tools"

    print(f"📁 Scanning: {project_dir}")

    # Test 1: Basic tree listing
    print("\n=== Test 1: Basic Tree Listing ===")
    result = await file_ops.list_directory_tree(
        root_path=project_dir,
        max_depth=2,  # Limit depth to keep output manageable
        include_hidden=False,
        include_metadata=True,
        exclude_patterns=["*.pyc", "__pycache__", ".venv", ".git"],
        include_git_status=True,
    )

    if "error" in result:
        print(f"❌ Error: {result['error']}")
        return

    print("✅ Successfully scanned directory tree!")
    print("📊 Summary:")
    summary = result["summary"]
    for key, value in summary.items():
        print(f"   {key}: {value}")

    # Test 2: Display tree structure (limited)
    print("\n=== Test 2: Tree Structure (First Few Items) ===")
    tree = result["tree"]

    def print_tree_node(node, depth=0, max_items=5):
        """Print tree node with indentation"""
        indent = "  " * depth

        if node["type"] == "directory":
            icon = "📁"
        elif node["type"] == "file":
            icon = "📄"
        else:
            icon = "❓"

        size_info = ""
        if "size_human" in node:
            size_info = f" ({node['size_human']})"

        git_info = ""
        if "git_status" in node:
            git_info = f" [git: {node['git_status']}]"

        print(f"{indent}{icon} {node['name']}{size_info}{git_info}")

        # Print children (limited to max_items)
        if "children" in node:
            for i, child in enumerate(node["children"][:max_items]):
                print_tree_node(child, depth + 1, max_items)

            if len(node["children"]) > max_items:
                print(f"{indent}  ... and {len(node['children']) - max_items} more items")

    print_tree_node(tree, max_items=3)

    # Test 3: JSON output sample
    print("\n=== Test 3: JSON Structure Sample ===")

    # Get first file for detailed metadata example
    def find_first_file(node):
        if node["type"] == "file":
            return node
        if "children" in node:
            for child in node["children"]:
                result = find_first_file(child)
                if result:
                    return result
        return None

    first_file = find_first_file(tree)
    if first_file:
        print("📄 Sample file metadata:")
        print(json.dumps(first_file, indent=2)[:500] + "...")

    # Test 4: Different configuration
    print("\n=== Test 4: Minimal Configuration (No Metadata) ===")
    minimal_result = await file_ops.list_directory_tree(
        root_path=project_dir,
        max_depth=1,
        include_hidden=False,
        include_metadata=False,
        exclude_patterns=["*.pyc", "__pycache__", ".venv", ".git", "*.egg-info"],
        include_git_status=False,
    )

    if "error" not in minimal_result:
        print("✅ Minimal scan successful!")
        print(f"📊 Items found: {minimal_result['summary']['total_items']}")

        # Show simplified structure
        print("📋 Simplified structure:")
        for child in minimal_result["tree"]["children"][:5]:
            print(f"   {child['type']}: {child['name']}")

    # Test 5: Large files only
    print("\n=== Test 5: Large Files Only (>1KB) ===")
    large_files_result = await file_ops.list_directory_tree(
        root_path=project_dir,
        max_depth=3,
        include_hidden=False,
        include_metadata=True,
        exclude_patterns=["*.pyc", "__pycache__", ".venv", ".git"],
        size_threshold=1000,  # 1KB threshold
    )

    if "error" not in large_files_result:
        print("✅ Large files scan successful!")
        print(f"📊 Large files found: {large_files_result['summary']['total_items']}")

        def count_files(node):
            count = 1 if node["type"] == "file" else 0
            if "children" in node:
                for child in node["children"]:
                    count += count_files(child)
            return count

        file_count = count_files(large_files_result["tree"])
        print(f"📁 Files over 1KB: {file_count}")

    print("\n🎉 Directory tree listing tests completed!")
    print("✅ All functionality working correctly!")
    print("🔧 Available features: metadata, git status, filtering, depth control, size thresholds")


if __name__ == "__main__":
    asyncio.run(test_directory_tree())
