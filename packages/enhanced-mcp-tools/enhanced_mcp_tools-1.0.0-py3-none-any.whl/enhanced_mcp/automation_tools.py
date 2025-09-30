"""
Screenshot Tools Module

Provides reliable screenshot capture capabilities using PIL.ImageGrab:
- Full screen and region screenshot capture
- Clipboard image capture
- Image analysis and processing
- Cross-platform compatibility

Uses PIL.ImageGrab which is more reliable and maintained than pyautogui.
"""

import asyncio
import base64
import io
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

from fastmcp import Context
from fastmcp.contrib.mcp_mixin import MCPMixin, mcp_tool

try:
    from PIL import Image, ImageGrab
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False
    Image = None
    ImageGrab = None


class ScreenshotTools(MCPMixin):
    """Screenshot and image capture tools using reliable PIL.ImageGrab

    These tools provide safe, read-only screenshot capabilities without requiring
    complex GUI automation libraries. Perfect for documentation, monitoring,
    and debugging workflows.
    """

    def __init__(self):
        super().__init__()

        if not PIL_AVAILABLE:
            print("⚠️ PIL not available - screenshot tools will be limited")

    @mcp_tool(
        name="take_screenshot",
        description="Capture a screenshot using PIL.ImageGrab",
    )
    async def take_screenshot(
        self,
        save_path: str = None,
        bbox: List[int] = None,
        format: str = "PNG",
        return_base64: bool = False,
        ctx: Context = None
    ) -> Dict[str, Any]:
        """Take a screenshot using PIL.ImageGrab

        Args:
            save_path: Optional path to save screenshot file
            bbox: Optional [left, top, right, bottom] bounding box for region capture
            format: Image format (PNG, JPEG, WEBP, etc.)
            return_base64: Whether to return image as base64 string
            ctx: MCP context for logging

        Returns:
            Dict with screenshot info and optional base64 data
        """
        if not PIL_AVAILABLE:
            return {"error": "PIL not available - install with: pip install pillow"}

        try:
            if ctx:
                await ctx.info(f"Taking screenshot - Bbox: {bbox}, Format: {format}")

            # Take screenshot using PIL.ImageGrab
            if bbox:
                if len(bbox) != 4:
                    return {"error": "Bbox must be [left, top, right, bottom]"}
                screenshot = ImageGrab.grab(bbox=tuple(bbox))
            else:
                screenshot = ImageGrab.grab()

            if screenshot is None:
                return {"error": "Failed to capture screenshot - no display available"}

            result = {
                "success": True,
                "size": screenshot.size,
                "mode": screenshot.mode,
                "format": format,
                "timestamp": time.time()
            }

            # Save to file if requested
            if save_path:
                save_path = Path(save_path)
                save_path.parent.mkdir(parents=True, exist_ok=True)
                screenshot.save(save_path, format=format)
                result["saved_path"] = str(save_path.absolute())
                result["file_size"] = save_path.stat().st_size

                if ctx:
                    await ctx.info(f"Screenshot saved to: {save_path}")

            # Return base64 if requested
            if return_base64:
                buffer = io.BytesIO()
                screenshot.save(buffer, format=format)
                base64_data = base64.b64encode(buffer.getvalue()).decode()
                result["base64_data"] = base64_data
                result["data_url"] = f"data:image/{format.lower()};base64,{base64_data}"
                result["base64_size"] = len(base64_data)

            return result

        except Exception as e:
            error_msg = f"Screenshot failed: {str(e)}"
            if ctx:
                await ctx.error(error_msg)
            return {"error": error_msg}

    @mcp_tool(
        name="capture_clipboard",
        description="Capture image from clipboard using PIL.ImageGrab",
    )
    async def capture_clipboard(
        self,
        save_path: str = None,
        format: str = "PNG",
        return_base64: bool = False,
        ctx: Context = None
    ) -> Dict[str, Any]:
        """Capture image from clipboard using PIL.ImageGrab

        Args:
            save_path: Optional path to save clipboard image file
            format: Image format (PNG, JPEG, WEBP, etc.)
            return_base64: Whether to return image as base64 string
            ctx: MCP context for logging

        Returns:
            Dict with clipboard image info and optional base64 data
        """
        if not PIL_AVAILABLE:
            return {"error": "PIL not available - install with: pip install pillow"}

        try:
            if ctx:
                await ctx.info(f"Capturing clipboard image - Format: {format}")

            # Capture clipboard image using PIL.ImageGrab
            clipboard_image = ImageGrab.grabclipboard()

            if clipboard_image is None:
                return {
                    "success": False,
                    "error": "No image found in clipboard",
                    "timestamp": time.time()
                }

            result = {
                "success": True,
                "size": clipboard_image.size,
                "mode": clipboard_image.mode,
                "format": format,
                "timestamp": time.time()
            }

            # Save to file if requested
            if save_path:
                save_path = Path(save_path)
                save_path.parent.mkdir(parents=True, exist_ok=True)
                clipboard_image.save(save_path, format=format)
                result["saved_path"] = str(save_path.absolute())
                result["file_size"] = save_path.stat().st_size

                if ctx:
                    await ctx.info(f"Clipboard image saved to: {save_path}")

            # Return base64 if requested
            if return_base64:
                buffer = io.BytesIO()
                clipboard_image.save(buffer, format=format)
                base64_data = base64.b64encode(buffer.getvalue()).decode()
                result["base64_data"] = base64_data
                result["data_url"] = f"data:image/{format.lower()};base64,{base64_data}"
                result["base64_size"] = len(base64_data)

            return result

        except Exception as e:
            error_msg = f"Clipboard capture failed: {str(e)}"
            if ctx:
                await ctx.error(error_msg)
            return {"error": error_msg}




    @mcp_tool(
        name="get_screen_info",
        description="Get screen resolution and display information",
    )
    async def get_screen_info(self, ctx: Context = None) -> Dict[str, Any]:
        """Get information about the current screen/display using PIL.ImageGrab

        Returns:
            Dict with screen information
        """
        if not PIL_AVAILABLE:
            return {"error": "PIL not available - install with: pip install pillow"}

        try:
            # Take a screenshot to get screen dimensions
            screenshot = ImageGrab.grab()
            if screenshot is None:
                return {"error": "Failed to capture screen - no display available"}

            result = {
                "success": True,
                "screen_width": screenshot.size[0],
                "screen_height": screenshot.size[1],
                "screen_size": screenshot.size,
                "image_mode": screenshot.mode,
                "timestamp": time.time()
            }

            if ctx:
                await ctx.info(f"Screen info: {screenshot.size[0]}x{screenshot.size[1]}")

            return result

        except Exception as e:
            error_msg = f"Failed to get screen info: {str(e)}"
            if ctx:
                await ctx.error(error_msg)
            return {"error": error_msg}