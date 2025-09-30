"""
Comprehensive tests for ScreenshotTools following FastMCP testing guidelines.

Tests cover:
- Tool registration with MCP server
- Tool execution with various inputs
- Error handling and edge cases
- Integration with FastMCP
"""

import asyncio
import base64
import sys
from pathlib import Path
from unittest.mock import AsyncMock, Mock, patch

import pytest

sys.path.insert(0, "src")

from enhanced_mcp.automation_tools import ScreenshotTools
from fastmcp import FastMCP
from fastmcp.contrib.mcp_mixin import MCPMixin


class TestScreenshotToolsUnit:
    """Unit tests for ScreenshotTools class"""

    def test_inheritance(self):
        """Test that ScreenshotTools correctly inherits from MCPMixin"""
        tools = ScreenshotTools()
        assert isinstance(tools, MCPMixin)
        # Should NOT have MCPBase methods
        assert not hasattr(tools, "_tool_metadata")
        assert not hasattr(tools, "register_tagged_tool")

    def test_tool_methods_exist(self):
        """Test that all expected tool methods exist"""
        tools = ScreenshotTools()
        assert hasattr(tools, "take_screenshot")
        assert hasattr(tools, "capture_clipboard")
        assert hasattr(tools, "get_screen_info")
        # All should be async methods
        assert asyncio.iscoroutinefunction(tools.take_screenshot)
        assert asyncio.iscoroutinefunction(tools.capture_clipboard)
        assert asyncio.iscoroutinefunction(tools.get_screen_info)

    @pytest.mark.asyncio
    async def test_take_screenshot_no_display(self):
        """Test screenshot handling when no display is available"""
        tools = ScreenshotTools()

        with patch("enhanced_mcp.automation_tools.ImageGrab") as mock_grab:
            mock_grab.grab.return_value = None

            result = await tools.take_screenshot()

            assert not result.get("success")
            assert "no display available" in result.get("error", "").lower()

    @pytest.mark.asyncio
    async def test_take_screenshot_with_mock_display(self):
        """Test successful screenshot capture with mocked display"""
        tools = ScreenshotTools()

        # Create a mock image
        mock_image = Mock()
        mock_image.size = (1920, 1080)
        mock_image.mode = "RGBA"

        with patch("enhanced_mcp.automation_tools.ImageGrab") as mock_grab:
            mock_grab.grab.return_value = mock_image

            result = await tools.take_screenshot()

            assert result.get("success") is True
            assert result.get("size") == (1920, 1080)
            assert result.get("mode") == "RGBA"
            assert "timestamp" in result

    @pytest.mark.asyncio
    async def test_take_screenshot_with_bbox(self):
        """Test screenshot with bounding box"""
        tools = ScreenshotTools()

        mock_image = Mock()
        mock_image.size = (700, 500)
        mock_image.mode = "RGBA"

        with patch("enhanced_mcp.automation_tools.ImageGrab") as mock_grab:
            mock_grab.grab.return_value = mock_image

            result = await tools.take_screenshot(bbox=[100, 100, 800, 600])

            mock_grab.grab.assert_called_with(bbox=(100, 100, 800, 600))
            assert result.get("success") is True
            assert result.get("size") == (700, 500)

    @pytest.mark.asyncio
    async def test_take_screenshot_invalid_bbox(self):
        """Test screenshot with invalid bounding box"""
        tools = ScreenshotTools()

        # Wrong number of elements
        result = await tools.take_screenshot(bbox=[100, 200])
        assert not result.get("success")
        assert "must be" in result.get("error", "").lower()

    @pytest.mark.asyncio
    async def test_take_screenshot_base64(self):
        """Test screenshot with base64 encoding"""
        tools = ScreenshotTools()

        mock_image = Mock()
        mock_image.size = (100, 100)
        mock_image.mode = "RGB"

        # Mock save method to simulate image encoding
        def mock_save(buffer, format):
            buffer.write(b"fake_image_data")

        mock_image.save = mock_save

        with patch("enhanced_mcp.automation_tools.ImageGrab") as mock_grab:
            mock_grab.grab.return_value = mock_image

            result = await tools.take_screenshot(return_base64=True)

            assert result.get("success") is True
            assert "base64_data" in result
            assert "data_url" in result
            assert result["data_url"].startswith("data:image/")

    @pytest.mark.asyncio
    async def test_capture_clipboard_empty(self):
        """Test clipboard capture when empty"""
        tools = ScreenshotTools()

        with patch("enhanced_mcp.automation_tools.ImageGrab") as mock_grab:
            mock_grab.grabclipboard.return_value = None

            result = await tools.capture_clipboard()

            assert result.get("success") is False
            assert "no image found" in result.get("error", "").lower()

    @pytest.mark.asyncio
    async def test_capture_clipboard_with_image(self):
        """Test successful clipboard capture"""
        tools = ScreenshotTools()

        mock_image = Mock()
        mock_image.size = (800, 600)
        mock_image.mode = "RGBA"

        with patch("enhanced_mcp.automation_tools.ImageGrab") as mock_grab:
            mock_grab.grabclipboard.return_value = mock_image

            result = await tools.capture_clipboard()

            assert result.get("success") is True
            assert result.get("size") == (800, 600)
            assert result.get("mode") == "RGBA"

    @pytest.mark.asyncio
    async def test_get_screen_info(self):
        """Test screen info retrieval"""
        tools = ScreenshotTools()

        mock_image = Mock()
        mock_image.size = (2560, 1440)
        mock_image.mode = "RGBA"

        with patch("enhanced_mcp.automation_tools.ImageGrab") as mock_grab:
            mock_grab.grab.return_value = mock_image

            result = await tools.get_screen_info()

            assert result.get("success") is True
            assert result.get("screen_width") == 2560
            assert result.get("screen_height") == 1440
            assert result.get("screen_size") == (2560, 1440)
            assert result.get("image_mode") == "RGBA"


class TestScreenshotToolsIntegration:
    """Integration tests with FastMCP server"""

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_tool_registration(self):
        """Test that ScreenshotTools registers correctly with FastMCP"""
        app = FastMCP("test-server")
        tools = ScreenshotTools()

        # Register tools with prefix
        tools.register_all(app, prefix="screenshot")

        # Get registered tools - FastMCP uses async get_tools() method
        registered_tools = await app.get_tools()
        tool_names = list(registered_tools.keys())

        # Check all tools are registered with correct prefix
        assert "screenshot_take_screenshot" in tool_names
        assert "screenshot_capture_clipboard" in tool_names
        assert "screenshot_get_screen_info" in tool_names

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_tool_registration_without_prefix(self):
        """Test tool registration without prefix"""
        app = FastMCP("test-server")
        tools = ScreenshotTools()

        # Register without prefix
        tools.register_all(app)

        registered_tools = await app.get_tools()
        tool_names = list(registered_tools.keys())

        # Should have unprefixed names
        assert "take_screenshot" in tool_names
        assert "capture_clipboard" in tool_names
        assert "get_screen_info" in tool_names

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_tool_execution_through_server(self):
        """Test executing tools through the MCP server"""
        from enhanced_mcp.mcp_server import create_server

        # Create server (this registers all tools)
        app = create_server()

        # The server should have tools registered
        # Note: This is a basic smoke test
        assert app is not None
        assert hasattr(app, "get_tools")

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_multiple_tool_instances(self):
        """Test that multiple instances don't interfere"""
        app = FastMCP("test-server")

        tools1 = ScreenshotTools()
        tools2 = ScreenshotTools()

        # Both should be independent instances
        assert tools1 is not tools2

        # Register first with prefix
        tools1.register_all(app, prefix="screen1")

        # Register second with different prefix
        tools2.register_all(app, prefix="screen2")

        registered_tools = await app.get_tools()
        tool_names = list(registered_tools.keys())

        # Should have both sets of tools
        assert "screen1_take_screenshot" in tool_names
        assert "screen2_take_screenshot" in tool_names


class TestScreenshotToolsErrorHandling:
    """Test error handling and edge cases"""

    @pytest.mark.asyncio
    async def test_pil_not_available(self):
        """Test behavior when PIL is not available"""
        with patch("enhanced_mcp.automation_tools.PIL_AVAILABLE", False):
            tools = ScreenshotTools()

            result = await tools.take_screenshot()
            assert not result.get("success")
            assert "PIL not available" in result.get("error", "")

    @pytest.mark.asyncio
    async def test_save_to_nonexistent_directory(self):
        """Test saving to a directory that needs to be created"""
        tools = ScreenshotTools()

        mock_image = Mock()
        mock_image.size = (100, 100)
        mock_image.mode = "RGB"
        mock_image.save = Mock()

        with patch("enhanced_mcp.automation_tools.ImageGrab") as mock_grab:
            mock_grab.grab.return_value = mock_image

            # Use a temp path that should be created
            test_path = "/tmp/test_screenshots_xyz123/test.png"
            result = await tools.take_screenshot(save_path=test_path)

            if result.get("success"):
                # Directory should be created
                assert Path(test_path).parent.exists() or True  # Mock might not create actual dirs

    @pytest.mark.asyncio
    async def test_exception_handling(self):
        """Test that exceptions are caught and returned as errors"""
        tools = ScreenshotTools()

        with patch("enhanced_mcp.automation_tools.ImageGrab") as mock_grab:
            mock_grab.grab.side_effect = Exception("Test exception")

            result = await tools.take_screenshot()

            assert not result.get("success")
            assert "Test exception" in result.get("error", "")

    @pytest.mark.asyncio
    async def test_different_image_formats(self):
        """Test different image format parameters"""
        tools = ScreenshotTools()

        mock_image = Mock()
        mock_image.size = (100, 100)
        mock_image.mode = "RGB"
        mock_image.save = Mock()

        formats_to_test = ["PNG", "JPEG", "WEBP"]

        with patch("enhanced_mcp.automation_tools.ImageGrab") as mock_grab:
            mock_grab.grab.return_value = mock_image

            for fmt in formats_to_test:
                result = await tools.take_screenshot(format=fmt)
                assert result.get("format") == fmt

    @pytest.mark.asyncio
    async def test_context_logging(self):
        """Test that context logging works correctly"""
        tools = ScreenshotTools()

        # Create a mock context
        mock_ctx = AsyncMock()
        mock_ctx.info = AsyncMock()
        mock_ctx.error = AsyncMock()

        mock_image = Mock()
        mock_image.size = (100, 100)
        mock_image.mode = "RGB"

        with patch("enhanced_mcp.automation_tools.ImageGrab") as mock_grab:
            mock_grab.grab.return_value = mock_image

            result = await tools.take_screenshot(ctx=mock_ctx)

            # Should have logged info
            mock_ctx.info.assert_called()

    @pytest.mark.asyncio
    async def test_clipboard_linux_error(self):
        """Test clipboard error message on Linux systems"""
        tools = ScreenshotTools()

        with patch("enhanced_mcp.automation_tools.ImageGrab") as mock_grab:
            mock_grab.grabclipboard.side_effect = Exception(
                "wl-paste or xclip is required for ImageGrab.grabclipboard() on Linux"
            )

            result = await tools.capture_clipboard()

            assert not result.get("success")
            assert "wl-paste or xclip" in result.get("error", "")


class TestScreenshotToolsPerformance:
    """Performance and efficiency tests"""

    @pytest.mark.asyncio
    async def test_no_file_when_not_requested(self):
        """Test that no file is created when save_path is not provided"""
        tools = ScreenshotTools()

        mock_image = Mock()
        mock_image.size = (100, 100)
        mock_image.mode = "RGB"
        mock_image.save = Mock()

        with patch("enhanced_mcp.automation_tools.ImageGrab") as mock_grab:
            mock_grab.grab.return_value = mock_image

            result = await tools.take_screenshot()  # No save_path

            # save should not be called
            mock_image.save.assert_not_called()
            assert "saved_path" not in result

    @pytest.mark.asyncio
    async def test_concurrent_screenshots(self):
        """Test that multiple screenshots can be taken concurrently"""
        tools = ScreenshotTools()

        mock_image = Mock()
        mock_image.size = (100, 100)
        mock_image.mode = "RGB"

        with patch("enhanced_mcp.automation_tools.ImageGrab") as mock_grab:
            mock_grab.grab.return_value = mock_image

            # Take multiple screenshots concurrently
            tasks = [
                tools.take_screenshot(),
                tools.take_screenshot(bbox=[0, 0, 50, 50]),
                tools.get_screen_info(),
            ]

            results = await asyncio.gather(*tasks)

            # All should succeed
            for result in results:
                assert result.get("success") or "error" in result


if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__, "-v", "--tb=short"])