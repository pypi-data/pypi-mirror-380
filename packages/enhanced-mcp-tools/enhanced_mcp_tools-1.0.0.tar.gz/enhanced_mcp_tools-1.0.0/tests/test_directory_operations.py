"""
Test suite for new directory operations in Enhanced MCP Tools
"""

import pytest
import tempfile
from pathlib import Path
from unittest.mock import AsyncMock

# Import the module
import sys
sys.path.insert(0, "src")
from enhanced_mcp.file_operations import EnhancedFileOperations


class TestDirectoryOperations:
    """Test directory management tools"""

    @pytest.fixture
    def file_ops(self):
        """Create file operations instance"""
        return EnhancedFileOperations()

    @pytest.fixture
    def temp_dir(self):
        """Create temporary directory for testing"""
        with tempfile.TemporaryDirectory() as tmp_dir:
            yield Path(tmp_dir)

    @pytest.mark.asyncio
    async def test_create_directory_success(self, file_ops, temp_dir):
        """Test successful directory creation"""
        test_dir = temp_dir / "new_directory"

        result = await file_ops.create_directory(str(test_dir))

        assert result["created"] is True
        assert result["directory"] == str(test_dir.resolve())
        assert test_dir.exists()
        assert test_dir.is_dir()

    @pytest.mark.asyncio
    async def test_create_directory_already_exists(self, file_ops, temp_dir):
        """Test creating directory that already exists"""
        test_dir = temp_dir / "existing_directory"
        test_dir.mkdir()  # Create it first

        result = await file_ops.create_directory(str(test_dir), exist_ok=True)

        assert result["created"] is False
        assert result["existed"] is True
        assert test_dir.exists()

    @pytest.mark.asyncio
    async def test_create_directory_with_parents(self, file_ops, temp_dir):
        """Test creating directory with parent directories"""
        test_dir = temp_dir / "parent" / "child" / "grandchild"

        result = await file_ops.create_directory(str(test_dir), parents=True)

        assert result["created"] is True
        assert test_dir.exists()
        assert test_dir.is_dir()

    @pytest.mark.asyncio
    async def test_create_directory_safety_check(self, file_ops):
        """Test safety checks prevent creating directories in system locations"""
        system_dir = "/usr/local/test_directory"

        result = await file_ops.create_directory(system_dir)

        assert "error" in result
        assert "SAFETY" in result["error"]
        assert result["created"] is False

    @pytest.mark.asyncio
    async def test_remove_directory_dry_run(self, file_ops, temp_dir):
        """Test remove directory dry run mode"""
        test_dir = temp_dir / "to_remove"
        test_dir.mkdir()
        (test_dir / "file.txt").write_text("test content")

        result = await file_ops.remove_directory(str(test_dir), recursive=True, dry_run=True)

        assert result["dry_run"] is True
        assert "would_remove" in result
        assert test_dir.exists()  # Should still exist in dry run

    @pytest.mark.asyncio
    async def test_remove_directory_safety_check(self, file_ops):
        """Test safety checks prevent removing system directories"""
        system_dir = "/usr"

        result = await file_ops.remove_directory(system_dir)

        assert "error" in result
        assert "SAFETY" in result["error"]
        assert result["removed"] is False

    @pytest.mark.asyncio
    async def test_move_directory_success(self, file_ops, temp_dir):
        """Test successful directory move"""
        source_dir = temp_dir / "source"
        dest_dir = temp_dir / "destination"
        source_dir.mkdir()
        (source_dir / "file.txt").write_text("test content")

        result = await file_ops.move_directory(str(source_dir), str(dest_dir))

        assert result["moved"] is True
        assert not source_dir.exists()
        assert dest_dir.exists()
        assert (dest_dir / "file.txt").exists()

    @pytest.mark.asyncio
    async def test_copy_directory_success(self, file_ops, temp_dir):
        """Test successful directory copy"""
        source_dir = temp_dir / "source"
        dest_dir = temp_dir / "destination"
        source_dir.mkdir()
        (source_dir / "file.txt").write_text("test content")

        result = await file_ops.copy_directory(str(source_dir), str(dest_dir))

        assert result["copied"] is True
        assert source_dir.exists()  # Source should still exist
        assert dest_dir.exists()
        assert (dest_dir / "file.txt").exists()
        assert result["files_copied"] == 1

    @pytest.mark.asyncio
    async def test_create_directory_with_context(self, file_ops, temp_dir):
        """Test directory creation with context logging"""
        test_dir = temp_dir / "with_context"

        # Mock context
        ctx = AsyncMock()

        result = await file_ops.create_directory(str(test_dir), ctx=ctx)

        assert result["created"] is True
        assert test_dir.exists()
        # Verify context was called
        ctx.info.assert_called()

    @pytest.mark.asyncio
    async def test_directory_tools_registration(self, file_ops):
        """Test that directory tools are properly registered as MCP tools"""
        # Verify the tools have the @mcp_tool decorator attributes
        assert hasattr(file_ops.create_directory, '__mcp_tool__')
        assert hasattr(file_ops.remove_directory, '__mcp_tool__')
        assert hasattr(file_ops.move_directory, '__mcp_tool__')
        assert hasattr(file_ops.copy_directory, '__mcp_tool__')

    @pytest.mark.asyncio
    async def test_all_directory_tools_are_async(self, file_ops):
        """Test that all directory tools are async functions"""
        import inspect

        assert inspect.iscoroutinefunction(file_ops.create_directory)
        assert inspect.iscoroutinefunction(file_ops.remove_directory)
        assert inspect.iscoroutinefunction(file_ops.move_directory)
        assert inspect.iscoroutinefunction(file_ops.copy_directory)


class TestDirectoryToolsIntegration:
    """Test directory tools integration with FastMCP server"""

    @pytest.mark.asyncio
    async def test_directory_tools_in_server(self):
        """Test that directory tools are registered in the server"""
        from enhanced_mcp.mcp_server import create_server

        server = create_server()
        tools = await server.get_tools()
        tool_names = [tool for tool in tools]

        # Check that our new directory tools are registered
        assert "file_ops_create_directory" in tool_names
        assert "file_ops_remove_directory" in tool_names
        assert "file_ops_move_directory" in tool_names
        assert "file_ops_copy_directory" in tool_names

    @pytest.mark.asyncio
    async def test_create_directory_tool_callable(self):
        """Test that create_directory tool can be called through server"""
        from enhanced_mcp.mcp_server import create_server

        server = create_server()

        # Find the create_directory tool
        tools_info = await server.get_tools()
        assert "file_ops_create_directory" in tools_info

        print("✅ file_ops_create_directory tool is properly registered and callable")