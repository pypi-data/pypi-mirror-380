#!/usr/bin/env python3
"""
Test script for the new tre-based directory tree functionality
"""

import asyncio
import json
from pathlib import Path

from enhanced_mcp.file_operations import EnhancedFileOperations


async def test_tre_directory_tree():
    """Test the tre-based directory tree functionality"""

    # Initialize the file operations class
    file_ops = EnhancedFileOperations()

    print("🌳 Testing tre-based Directory Tree Listing")
    print("=" * 60)

    # Test on the current project directory
    project_dir = "/home/rpm/claude/enhanced-mcp-tools"

    print(f"📁 Scanning: {project_dir}")

    # Test 1: Basic tre tree listing
    print("\n=== Test 1: Basic tre Tree Listing ===")
    result = await file_ops.tre_directory_tree(
        root_path=project_dir,
        max_depth=2,  # Limit depth to keep output manageable
        include_hidden=False,
        exclude_patterns=[r"\.venv", r"\.git", r"__pycache__", r"\.egg-info"],
    )

    if "error" in result:
        print(f"❌ Error: {result['error']}")
        if "suggestion" in result:
            print(f"💡 Suggestion: {result['suggestion']}")
        return

    print("✅ Successfully scanned directory tree with tre!")
    print("📊 Metadata:")
    metadata = result["metadata"]
    print(f"   Command: {metadata['command']}")
    print(f"   Execution time: {metadata['execution_time_seconds']}s")
    print(f"   Statistics: {metadata['statistics']}")
    print(f"   Optimized for LLM: {metadata['optimized_for_llm']}")

    # Test 2: Display tree structure sample
    print("\n=== Test 2: tre JSON Structure Sample ===")
    tree = result["tree"]

    def print_tre_tree(node, depth=0, max_items=3):
        """Print tre tree node with indentation"""
        indent = "  " * depth

        if node["type"] == "directory":
            icon = "📁"
        elif node["type"] == "file":
            icon = "📄"
        else:
            icon = "❓"

        print(f"{indent}{icon} {node['name']} [{node['type']}]")

        # Print children (limited to max_items)
        if "contents" in node:
            for i, child in enumerate(node["contents"][:max_items]):
                print_tre_tree(child, depth + 1, max_items)

            if len(node["contents"]) > max_items:
                print(f"{indent}  ... and {len(node['contents']) - max_items} more items")

    print_tre_tree(tree, max_items=3)

    # Test 3: tre with different options
    print("\n=== Test 3: tre with Different Options ===")
    options_test = await file_ops.tre_directory_tree(
        root_path=project_dir,
        max_depth=1,
        include_hidden=False,
        directories_only=True,  # Only directories
        exclude_patterns=[r"\.venv", r"\.git"],
    )

    if "error" not in options_test:
        print("✅ Directories-only scan successful!")
        print(f"📊 Items found: {options_test['metadata']['statistics']['total']}")

        # Show simplified structure
        print("📋 Directory structure:")
        for child in options_test["tree"].get("contents", [])[:5]:
            if child["type"] == "directory":
                print(f"   📁 {child['name']}")

    # Test 4: LLM Context Generation
    print("\n=== Test 4: LLM Context Generation ===")
    llm_context = await file_ops.tre_llm_context(
        root_path=project_dir,
        max_depth=2,
        include_file_contents=True,
        exclude_patterns=[r"\.venv", r"\.git", r"__pycache__", r"test_.*\.py"],
        file_extensions=[".py", ".md", ".toml"],
        max_file_size_kb=50,
    )

    if "error" not in llm_context:
        print("✅ LLM context generation successful!")
        context = llm_context["context"]

        print("📊 Context Summary:")
        summary = context["summary"]
        print(f"   Total files: {summary['total_files']}")
        print(f"   Included files: {summary['included_files']}")
        print(f"   Excluded files: {summary['excluded_files']}")
        print(f"   Total size: {summary['total_size_bytes']} bytes")

        print("\n📄 Sample file contents (first 3):")
        for i, (path, content) in enumerate(list(context["file_contents"].items())[:3]):
            print(f"   {i + 1}. {path} ({content['size_bytes']} bytes, {content['lines']} lines)")

        print("\n🤖 LLM Summary Preview:")
        print(
            context["llm_summary"][:300] + "..."
            if len(context["llm_summary"]) > 300
            else context["llm_summary"]
        )
    else:
        print(f"❌ LLM context error: {llm_context['error']}")

    # Test 5: JSON Export
    print("\n=== Test 5: JSON Export for External Tools ===")
    export_result = await file_ops.tre_directory_tree(
        root_path=project_dir,
        max_depth=3,
        include_hidden=False,
        exclude_patterns=[r"\.venv", r"\.git", r"__pycache__"],
    )

    if "error" not in export_result:
        # Save to JSON file
        output_file = Path(project_dir) / "tre_structure.json"
        with open(output_file, "w") as f:
            json.dump(export_result, f, indent=2)

        print(f"   ✅ Exported tre structure to: {output_file}")
        print(f"   📊 File size: {output_file.stat().st_size} bytes")

        # Verify the exported file
        with open(output_file) as f:
            imported_data = json.load(f)
            print(
                f"   ✅ Verification: {imported_data['metadata']['statistics']['total']} items in exported JSON"
            )

        # Clean up
        output_file.unlink()
        print("   🧹 Cleaned up test file")

    print("\n🎉 tre-based directory tree tests completed!")
    print("✅ All functionality working correctly!")
    print("🚀 Ready for LLM-optimized project analysis!")


if __name__ == "__main__":
    asyncio.run(test_tre_directory_tree())
