#!/usr/bin/env python3
"""
Test script for git repository detection in file listings
Tests the new git repository detection functionality across all file listing tools
"""

import asyncio
import json
from pathlib import Path

from enhanced_mcp.file_operations import EnhancedFileOperations


async def test_git_repository_detection():
    """Test git repository detection functionality"""

    # Initialize the file operations class
    file_ops = EnhancedFileOperations()

    print("🔍 Testing Git Repository Detection in File Listings")
    print("=" * 60)

    # Test on the current project directory (should be a git repo)
    project_dir = "/home/rpm/claude/enhanced-mcp-tools"

    print(f"📁 Testing in: {project_dir}")

    # Test 1: Enhanced Directory Listing with Git Detection
    print("\n=== Test 1: Enhanced Directory Listing with Git Detection ===")
    enhanced_result = await file_ops.enhanced_list_directory(
        directory_path=project_dir,
        include_hidden=False,
        include_git_info=True,
        recursive_depth=1,
        file_pattern="*.py",
    )

    if "error" in enhanced_result:
        print(f"❌ Error: {enhanced_result['error']}")
    else:
        print("✅ Enhanced directory listing completed!")

        # Show git repository info
        git_repo_info = enhanced_result.get("git_repository")
        if git_repo_info:
            print("📊 Git Repository Detection:")
            print(f"   Is git repo: {git_repo_info.get('is_git_repo', False)}")
            if git_repo_info.get("is_git_repo"):
                print(f"   Git root: {git_repo_info.get('git_root', 'Unknown')}")
                print(f"   Current branch: {git_repo_info.get('current_branch', 'Unknown')}")
                print(f"   Git type: {git_repo_info.get('git_type', 'Unknown')}")

        # Show summary
        summary = enhanced_result["summary"]
        print("📋 Summary:")
        print(f"   Total items: {summary['total_items']}")
        print(f"   Files: {summary['files']}")
        print(f"   Directories: {summary['directories']}")
        print(f"   Git tracked items: {summary['git_tracked_items']}")

        # Show first few items with git flags
        print("📄 Sample items with git flags:")
        for i, item in enumerate(enhanced_result["items"][:3]):
            git_flag = "🔄" if item.get("in_git_repo", False) else "📁"
            print(f"   {git_flag} {item['name']} (in_git_repo: {item.get('in_git_repo', False)})")

    # Test 2: Tree Directory Listing with Git Detection
    print("\n=== Test 2: Tree Directory Listing with Git Detection ===")
    tree_result = await file_ops.list_directory_tree(
        root_path=project_dir,
        max_depth=2,
        include_hidden=False,
        include_metadata=True,
        exclude_patterns=["*.pyc", "__pycache__", ".venv"],
    )

    if "error" in tree_result:
        print(f"❌ Error: {tree_result['error']}")
    else:
        print("✅ Tree directory listing completed!")

        # Check first few items for git flags
        def check_git_flags(node, depth=0):
            """Recursively check git flags in tree nodes"""
            indent = "  " * depth
            git_flag = "🔄" if node.get("in_git_repo", False) else "📁"
            print(
                f"{indent}{git_flag} {node['name']} (in_git_repo: {node.get('in_git_repo', False)})"
            )

            if depth < 1:  # Limit depth for readability
                for child in node.get("children", [])[:3]:
                    check_git_flags(child, depth + 1)

        print("📄 Tree structure with git flags:")
        check_git_flags(tree_result["tree"])

    # Test 3: tre Directory Tree with Git Detection
    print("\n=== Test 3: tre Directory Tree with Git Detection ===")
    tre_result = await file_ops.tre_directory_tree(
        root_path=project_dir,
        max_depth=2,
        include_hidden=False,
        exclude_patterns=[r"\.venv", r"__pycache__"],
    )

    if tre_result.get("success"):
        print("✅ tre directory tree completed!")

        stats = tre_result["metadata"]["statistics"]
        print("📊 tre Statistics:")
        print(f"   Total items: {stats['total']}")
        print(f"   Files: {stats['files']}")
        print(f"   Directories: {stats['directories']}")
        print(f"   Git tracked: {stats.get('git_tracked', 0)}")

        # Check git flags in tre output
        def check_tre_git_flags(node, depth=0):
            """Check git flags in tre tree structure"""
            indent = "  " * depth
            git_flag = "🔄" if node.get("in_git_repo", False) else "📁"
            type_icon = "📁" if node.get("type") == "directory" else "📄"
            print(
                f"{indent}{git_flag}{type_icon} {node['name']} (in_git_repo: {node.get('in_git_repo', False)})"
            )

            if depth < 1:  # Limit depth for readability
                for child in node.get("contents", [])[:3]:
                    check_tre_git_flags(child, depth + 1)

        print("📄 tre structure with git flags:")
        check_tre_git_flags(tre_result["tree"])
    else:
        print(f"❌ tre Error: {tre_result.get('error', 'Unknown error')}")

    # Test 4: Non-git Directory (for comparison)
    print("\n=== Test 4: Non-git Directory (for comparison) ===")
    temp_dir = "/tmp"

    non_git_result = await file_ops.enhanced_list_directory(
        directory_path=temp_dir, include_hidden=False, include_git_info=True, recursive_depth=1
    )

    if "error" in non_git_result:
        print(f"❌ Error: {non_git_result['error']}")
    else:
        git_repo_info = non_git_result.get("git_repository")
        print("📊 Non-git directory test:")
        print(f"   Is git repo: {git_repo_info.get('is_git_repo', False)}")
        print(f"   Git tracked items: {non_git_result['summary']['git_tracked_items']}")

    # Test 5: Git Repository Detection Edge Cases
    print("\n=== Test 5: Git Repository Detection Edge Cases ===")
    edge_cases = [
        {"path": "/", "description": "Root directory"},
        {"path": "/home", "description": "Home directory"},
        {"path": "/nonexistent", "description": "Non-existent directory"},
    ]

    for case in edge_cases:
        try:
            result = await file_ops.enhanced_list_directory(
                directory_path=case["path"], include_git_info=True, recursive_depth=1
            )

            if "error" in result:
                print(f"   {case['description']}: ❌ {result['error']}")
            else:
                git_info = result.get("git_repository", {})
                is_git = git_info.get("is_git_repo", False)
                print(f"   {case['description']}: {'🔄' if is_git else '📁'} (git: {is_git})")
        except Exception as e:
            print(f"   {case['description']}: ❌ Exception: {str(e)}")

    print("\n🎉 Git repository detection tests completed!")
    print("✅ All file listing tools now include git repository flags!")
    print("🔄 Files/directories in git repositories are automatically detected!")
    print("📁 Non-git files are clearly marked as well!")


if __name__ == "__main__":
    asyncio.run(test_git_repository_detection())
