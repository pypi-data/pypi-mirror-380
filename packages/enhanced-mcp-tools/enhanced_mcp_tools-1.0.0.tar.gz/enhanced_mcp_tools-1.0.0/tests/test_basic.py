"""
Basic tests for the MCP server tools.
Run with: pytest tests/test_basic.py
"""

import os
import tempfile
from pathlib import Path

import pytest

# Import the implementations from enhanced_mcp
from enhanced_mcp.diff_patch import DiffPatchOperations
from enhanced_mcp.file_operations import EnhancedFileOperations
from enhanced_mcp.git_integration import GitIntegration
from enhanced_mcp.workflow_tools import AdvancedSearchAnalysis


class TestFileOperations:
    """Test file operation tools"""

    @pytest.mark.asyncio
    async def test_file_backup_simple(self):
        """Test simple file backup"""
        with tempfile.TemporaryDirectory() as tmp_dir:
            # Create test file
            test_file = Path(tmp_dir) / "test.txt"
            test_file.write_text("Test content")

            backup_dir = Path(tmp_dir) / "backups"

            # Perform backup
            file_tools = EnhancedFileOperations()
            backups = await file_tools.file_backup(
                [str(test_file)], backup_directory=str(backup_dir)
            )

            # Verify backup created
            assert len(backups) == 1
            assert os.path.exists(backups[0])

            # Verify content preserved
            with open(backups[0]) as f:
                assert f.read() == "Test content"


class TestSearchAnalysis:
    """Test search and analysis tools"""

    @pytest.mark.asyncio
    async def test_project_stats_resource(self):
        """Test project statistics resource"""
        # Use the current project directory
        search_tools = AdvancedSearchAnalysis()
        stats = await search_tools.analyze_codebase(".", ["loc"])

        # Verify basic structure
        assert "directory" in stats
        assert stats["directory"] == "."


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
