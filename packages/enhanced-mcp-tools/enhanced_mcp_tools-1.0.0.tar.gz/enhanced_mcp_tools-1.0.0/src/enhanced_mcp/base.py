"""
Base module with common imports and utilities for Enhanced MCP Tools
"""

# Standard library imports
import ast
import asyncio
import json
import os
import re
import shutil
import subprocess
import sys
import time
import uuid
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Literal, Optional, Union

# Third-party imports with fallbacks
try:
    import aiofiles
except ImportError:
    aiofiles = None

try:
    import psutil
except ImportError:
    psutil = None

try:
    import requests
except ImportError:
    requests = None

# FastMCP imports - these are REQUIRED for MCP functionality
try:
    from fastmcp import Context, FastMCP
    from fastmcp.contrib.mcp_mixin import MCPMixin, mcp_prompt, mcp_resource, mcp_tool
    from mcp.types import ToolAnnotations

    # Try to import ComponentService - it may not be available in all FastMCP versions
    try:
        from fastmcp.services.component_service import ComponentService
        COMPONENT_SERVICE_AVAILABLE = True
    except ImportError:
        # Create a mock ComponentService for compatibility
        class ComponentService:
            def __init__(self, app):
                self.app = app
                self._hidden_tools = set()

            def create_tag_filter(self, tag, tools):
                pass

            def show_tool(self, tool_name):
                self._hidden_tools.discard(tool_name)

            def hide_tool(self, tool_name):
                self._hidden_tools.add(tool_name)

        COMPONENT_SERVICE_AVAILABLE = False

    # Verify that MCPMixin has the required register_all method
    if not hasattr(MCPMixin, "register_all"):
        raise ImportError(
            "MCPMixin is missing register_all method - FastMCP version may be incompatible"
        )

    FASTMCP_AVAILABLE = True

except ImportError as e:
    # FastMCP is REQUIRED - no silent fallbacks that break functionality
    import sys

    print(f"🚨 CRITICAL: FastMCP import failed: {e}")
    print("📋 Enhanced MCP Tools requires FastMCP to function.")
    print("🔧 Please install with: pip install fastmcp")
    print("   Or check your FastMCP installation and version compatibility.")

    # Still define the imports to prevent NameError, but mark as unavailable
    Context = None
    FastMCP = None
    MCPMixin = object  # This will cause clear errors instead of silent failures
    mcp_tool = lambda **kwargs: lambda func: func
    mcp_resource = lambda **kwargs: lambda func: func
    mcp_prompt = lambda **kwargs: lambda func: func
    ToolAnnotations = None
    FASTMCP_AVAILABLE = False

    # Don't exit here - let individual modules handle the error appropriately


# Security-focused tool categorization system
class SecurityLevel:
    """Security level constants for tool categorization"""
    SAFE = "safe"           # Read-only operations, no risk of data loss
    CAUTION = "caution"     # Operations that create/modify but reversible
    DESTRUCTIVE = "destructive"  # Operations that can cause data loss
    SYSTEM = "system"       # System-level operations requiring highest privilege

class ToolCategory:
    """Tool category constants for functional grouping"""
    FILE_OPS = "file_operations"
    SEARCH = "search_analysis"
    DEV_WORKFLOW = "dev_workflow"
    GIT = "git_integration"
    ARCHIVE = "archive_compression"
    NETWORK = "network_api"
    PROCESS = "process_management"
    MONITORING = "monitoring"
    BULK_OPS = "bulk_operations"
    AUTOMATION = "automation"
    UTILITY = "utility"

class TaggedTool:
    """Enhanced tool metadata with security and categorization tags"""
    def __init__(self,
                 name: str,
                 security_level: str = SecurityLevel.SAFE,
                 category: str = ToolCategory.UTILITY,
                 tags: Optional[List[str]] = None,
                 requires_confirmation: bool = False,
                 description: str = ""):
        self.name = name
        self.security_level = security_level
        self.category = category
        self.tags = tags or []
        self.requires_confirmation = requires_confirmation
        self.description = description

        # Auto-tag based on security level
        if security_level == SecurityLevel.DESTRUCTIVE:
            self.requires_confirmation = True
            if "destructive" not in self.tags:
                self.tags.append("destructive")

class ComponentServiceMixin:
    """Mixin to add ComponentService integration to existing MCPMixin classes

    This enhances existing tool modules with:
    - Tag-based tool filtering and categorization
    - Progressive tool disclosure based on security levels
    - Dynamic tool visibility management
    - Integration with SACRED TRUST safety framework
    """

    def __init__(self):
        super().__init__()
        self._tool_metadata: Dict[str, TaggedTool] = {}
        self._component_service: Optional[ComponentService] = None
        self._security_state = {
            "destructive_tools_enabled": False,
            "confirmation_required": True,
            "safe_mode": True
        }

    def register_tagged_tool(self,
                           tool_name: str,
                           security_level: str = SecurityLevel.SAFE,
                           category: str = ToolCategory.UTILITY,
                           tags: Optional[List[str]] = None,
                           requires_confirmation: bool = None,
                           description: str = ""):
        """Register tool metadata for enhanced management"""
        if requires_confirmation is None:
            requires_confirmation = (security_level == SecurityLevel.DESTRUCTIVE)

        self._tool_metadata[tool_name] = TaggedTool(
            name=tool_name,
            security_level=security_level,
            category=category,
            tags=tags or [],
            requires_confirmation=requires_confirmation,
            description=description
        )

    def get_tool_metadata(self, tool_name: str) -> Optional[TaggedTool]:
        """Get metadata for a specific tool"""
        return self._tool_metadata.get(tool_name)

    def get_tools_by_security_level(self, level: str) -> List[str]:
        """Get all tools matching a security level"""
        return [name for name, meta in self._tool_metadata.items()
                if meta.security_level == level]

    def get_tools_by_category(self, category: str) -> List[str]:
        """Get all tools in a category"""
        return [name for name, meta in self._tool_metadata.items()
                if meta.category == category]

    def get_destructive_tools(self) -> List[str]:
        """Get all destructive tools that require confirmation"""
        return self.get_tools_by_security_level(SecurityLevel.DESTRUCTIVE)

    def enable_destructive_tools(self, enabled: bool = True):
        """Enable/disable visibility of destructive tools"""
        self._security_state["destructive_tools_enabled"] = enabled
        if self._component_service:
            # Update ComponentService filters
            self._update_component_filters()

    def set_safe_mode(self, safe_mode: bool = True):
        """Enable/disable safe mode (hides all but safe tools)"""
        self._security_state["safe_mode"] = safe_mode
        if safe_mode:
            self._security_state["destructive_tools_enabled"] = False
        if self._component_service:
            self._update_component_filters()

    def _update_component_filters(self):
        """Update ComponentService filters based on current security state"""
        if not self._component_service:
            return

        visible_tools = []

        if self._security_state["safe_mode"]:
            # Safe mode: only show safe tools
            visible_tools = self.get_tools_by_security_level(SecurityLevel.SAFE)
        else:
            # Normal mode: show safe and caution tools always
            visible_tools.extend(self.get_tools_by_security_level(SecurityLevel.SAFE))
            visible_tools.extend(self.get_tools_by_security_level(SecurityLevel.CAUTION))

            # Add destructive tools only if enabled
            if self._security_state["destructive_tools_enabled"]:
                visible_tools.extend(self.get_tools_by_security_level(SecurityLevel.DESTRUCTIVE))

        # Apply filters to ComponentService
        for tool_name, metadata in self._tool_metadata.items():
            if tool_name in visible_tools:
                self._component_service.show_tool(tool_name)
            else:
                self._component_service.hide_tool(tool_name)

    def setup_component_service(self, app: FastMCP, prefix: str = None):
        """Initialize ComponentService with progressive disclosure"""
        if not COMPONENT_SERVICE_AVAILABLE:
            print(f"⚠️ ComponentService not available - using compatibility mode for {self.__class__.__name__}")
            # Return a mock service
            self._component_service = ComponentService(app)
            return self._component_service

        self._component_service = ComponentService(app)

        # Setup tag-based filters for each category
        categories = set(meta.category for meta in self._tool_metadata.values())
        for category in categories:
            tools_in_category = self.get_tools_by_category(category)
            prefixed_tools = [f"{prefix}_{tool}" if prefix else tool
                            for tool in tools_in_category]
            self._component_service.create_tag_filter(category, prefixed_tools)

        # Setup security level filters
        for level in [SecurityLevel.SAFE, SecurityLevel.CAUTION,
                     SecurityLevel.DESTRUCTIVE, SecurityLevel.SYSTEM]:
            tools_in_level = self.get_tools_by_security_level(level)
            prefixed_tools = [f"{prefix}_{tool}" if prefix else tool
                            for tool in tools_in_level]
            if prefixed_tools:
                self._component_service.create_tag_filter(f"security_{level}", prefixed_tools)

        # Apply initial filters
        self._update_component_filters()

        return self._component_service


# Common utility functions that multiple modules will use
class MCPBase(ComponentServiceMixin):
    """Enhanced base class with ComponentService integration

    Combines common MCP functionality with security-focused tool management.
    All tool modules should inherit from this to get progressive disclosure.
    """

    def __init__(self):
        # Check if FastMCP is properly available when instantiating
        if not FASTMCP_AVAILABLE:
            raise RuntimeError(
                "🚨 Enhanced MCP Tools requires FastMCP but it's not available.\n"
                "Please install with: pip install fastmcp"
            )
        super().__init__()

    def verify_mcp_ready(self) -> bool:
        """Verify that this instance is ready for MCP registration"""
        if not FASTMCP_AVAILABLE:
            return False
        if not hasattr(self, "register_all"):
            return False
        return True

    def safe_register_all(self, app: "FastMCP", prefix: str = None) -> bool:
        """Enhanced registration with ComponentService integration"""
        if not self.verify_mcp_ready():
            print(
                f"❌ Cannot register {self.__class__.__name__}: FastMCP not available or class not properly configured"
            )
            return False

        try:
            # Setup ComponentService before tool registration
            if hasattr(self, '_tool_metadata') and self._tool_metadata:
                self.setup_component_service(app, prefix)
                print(f"🔧 Configured ComponentService for {self.__class__.__name__}")

            # Register tools as usual
            if prefix:
                self.register_all(app, prefix=prefix)
                print(f"✅ Registered {self.__class__.__name__} tools with prefix '{prefix}'")
            else:
                self.register_all(app)
                print(f"✅ Registered {self.__class__.__name__} tools")

            # Apply initial security filters
            if hasattr(self, '_component_service') and self._component_service:
                # Start in safe mode by default (synchronous version)
                self._security_state["safe_mode"] = True
                self._security_state["destructive_tools_enabled"] = False
                self._update_component_filters()
                safe_count = len(self.get_tools_by_security_level(SecurityLevel.SAFE))
                destructive_count = len(self.get_tools_by_security_level(SecurityLevel.DESTRUCTIVE))
                print(f"🛡️ Safe mode enabled: {safe_count} safe tools visible, {destructive_count} destructive tools hidden")

            return True
        except Exception as e:
            print(f"❌ Failed to register {self.__class__.__name__}: {e}")
            return False

    async def log_info(self, message: str, ctx: Optional[Context] = None):
        """Helper to log info messages"""
        if ctx:
            await ctx.info(message)
        else:
            print(f"INFO: {message}")

    async def log_warning(self, message: str, ctx: Optional[Context] = None):
        """Helper to log warning messages"""
        if ctx:
            await ctx.warning(message)
        else:
            print(f"WARNING: {message}")

    async def log_error(self, message: str, ctx: Optional[Context] = None):
        """Helper to log error messages"""
        if ctx:
            await ctx.error(message)
        else:
            print(f"ERROR: {message}")

    async def log_critical(self, message: str, exception: Exception = None, ctx: Optional[Context] = None):
        """Helper to log critical error messages - alias for log_critical_error"""
        await self.log_critical_error(message, exception, ctx)

    async def log_critical_error(
        self, message: str, exception: Exception = None, ctx: Optional[Context] = None
    ):
        """Helper to log critical error messages with enhanced detail

        For critical tool failures that prevent completion but don't corrupt data.
        Uses ctx.error() as the highest severity in current FastMCP.
        """
        if exception:
            error_detail = (
                f"CRITICAL: {message} | Exception: {type(exception).__name__}: {str(exception)}"
            )
        else:
            error_detail = f"CRITICAL: {message}"

        if ctx:
            await ctx.error(error_detail)
        else:
            print(f"CRITICAL ERROR: {error_detail}")

    async def log_emergency(
        self, message: str, exception: Exception = None, ctx: Optional[Context] = None
    ):
        """Helper to log emergency-level errors

        RESERVED FOR TRUE EMERGENCIES: data corruption, security breaches, system instability.
        Currently uses ctx.error() with EMERGENCY prefix since FastMCP doesn't have emergency().
        If FastMCP adds emergency() method in future, this will be updated.
        """
        if exception:
            error_detail = (
                f"EMERGENCY: {message} | Exception: {type(exception).__name__}: {str(exception)}"
            )
        else:
            error_detail = f"EMERGENCY: {message}"

        if ctx:
            # Check if emergency method exists (future-proofing)
            if hasattr(ctx, "emergency"):
                await ctx.emergency(error_detail)
            else:
                # Fallback to error with EMERGENCY prefix
                await ctx.error(error_detail)
        else:
            print(f"🚨 EMERGENCY: {error_detail}")

        # Could also implement additional emergency actions here:
        # - Write to emergency log file
        # - Send alerts
        # - Trigger backup/recovery procedures


# Export common dependencies for use by other modules
__all__ = [
    # Standard library
    "os",
    "sys",
    "re",
    "ast",
    "json",
    "time",
    "uuid",
    "shutil",
    "asyncio",
    "subprocess",
    # Typing
    "Optional",
    "Any",
    "Union",
    "Literal",
    "Dict",
    "List",
    # Path and datetime
    "Path",
    "datetime",
    "defaultdict",
    # Third-party
    "aiofiles",
    "psutil",
    "requests",
    # FastMCP
    "MCPMixin",
    "mcp_tool",
    "mcp_resource",
    "mcp_prompt",
    "FastMCP",
    "Context",
    "ToolAnnotations",
    "ComponentService",
    "FASTMCP_AVAILABLE",
    "COMPONENT_SERVICE_AVAILABLE",
    # Enhanced classes
    "MCPBase",
    "ComponentServiceMixin",
    "SecurityLevel",
    "ToolCategory",
    "TaggedTool",
]
