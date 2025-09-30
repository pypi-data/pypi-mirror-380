"""
Security Manager Module

Provides dynamic tool visibility management and security controls for Enhanced MCP Tools.
This module implements the SACRED TRUST safety framework with progressive disclosure.
"""

from .base import *


class SecurityManager(MCPMixin, MCPBase):
    """Security management tools for dynamic tool control

    🟢 SAFE: All tools in this module are for managing security settings

    This module provides LLM assistants and users with tools to:
    - View available tools by security level
    - Enable/disable destructive tools with confirmation
    - Control progressive tool disclosure
    - Monitor tool usage and safety
    """

    def __init__(self):
        MCPMixin.__init__(self)
        MCPBase.__init__(self)

        # Track references to all tool modules for centralized control
        self._tool_modules: Dict[str, MCPBase] = {}

        # Register security management tools
        self.register_tagged_tool(
            "list_tools_by_security",
            security_level=SecurityLevel.SAFE,
            category=ToolCategory.UTILITY,
            tags=["security", "listing", "readonly"],
            description="List tools categorized by security level"
        )

        self.register_tagged_tool(
            "enable_destructive_tools",
            security_level=SecurityLevel.CAUTION,
            category=ToolCategory.UTILITY,
            tags=["security", "control", "destructive"],
            requires_confirmation=True,
            description="Enable visibility of destructive tools (requires confirmation)"
        )

        self.register_tagged_tool(
            "set_safe_mode",
            security_level=SecurityLevel.SAFE,
            category=ToolCategory.UTILITY,
            tags=["security", "safe_mode", "control"],
            description="Enable/disable safe mode (show only safe tools)"
        )

        self.register_tagged_tool(
            "get_tool_info",
            security_level=SecurityLevel.SAFE,
            category=ToolCategory.UTILITY,
            tags=["information", "metadata", "readonly"],
            description="Get detailed information about a specific tool"
        )

        self.register_tagged_tool(
            "security_status",
            security_level=SecurityLevel.SAFE,
            category=ToolCategory.UTILITY,
            tags=["security", "status", "readonly"],
            description="Get current security status and tool visibility settings"
        )

    def register_tool_module(self, name: str, module: MCPBase):
        """Register a tool module for centralized security control"""
        self._tool_modules[name] = module

    @mcp_tool(
        name="list_tools_by_security",
        description="🟢 SAFE: List all tools categorized by security level and visibility status"
    )
    async def list_tools_by_security(self, ctx: Context = None) -> Dict[str, Any]:
        """List tools organized by security level with visibility status"""
        try:
            result = {
                "security_levels": {},
                "total_tools": 0,
                "visible_tools": 0,
                "hidden_tools": 0
            }

            for module_name, module in self._tool_modules.items():
                if not hasattr(module, '_tool_metadata'):
                    continue

                for tool_name, metadata in module._tool_metadata.items():
                    level = metadata.security_level
                    if level not in result["security_levels"]:
                        result["security_levels"][level] = {
                            "tools": [],
                            "count": 0,
                            "visible_count": 0
                        }

                    # Determine if tool is currently visible
                    is_visible = True
                    if hasattr(module, '_security_state'):
                        state = module._security_state
                        if state.get("safe_mode", True) and level != SecurityLevel.SAFE:
                            is_visible = False
                        elif level == SecurityLevel.DESTRUCTIVE and not state.get("destructive_tools_enabled", False):
                            is_visible = False

                    tool_info = {
                        "name": tool_name,
                        "module": module_name,
                        "category": metadata.category,
                        "tags": metadata.tags,
                        "requires_confirmation": metadata.requires_confirmation,
                        "description": metadata.description,
                        "visible": is_visible
                    }

                    result["security_levels"][level]["tools"].append(tool_info)
                    result["security_levels"][level]["count"] += 1
                    result["total_tools"] += 1

                    if is_visible:
                        result["security_levels"][level]["visible_count"] += 1
                        result["visible_tools"] += 1
                    else:
                        result["hidden_tools"] += 1

            if ctx:
                await ctx.info(f"Listed {result['total_tools']} tools across {len(result['security_levels'])} security levels")

            return result

        except Exception as e:
            await self.log_error(f"Failed to list tools by security: {e}", ctx)
            return {"error": str(e)}

    @mcp_tool(
        name="enable_destructive_tools",
        description="🟡 CAUTION: Enable or disable visibility of destructive tools. Requires explicit confirmation."
    )
    async def enable_destructive_tools(
        self,
        enabled: bool,
        confirm_destructive: bool = False,
        ctx: Context = None
    ) -> Dict[str, Any]:
        """Enable/disable destructive tools with safety confirmation

        Args:
            enabled: Whether to enable destructive tools
            confirm_destructive: REQUIRED confirmation flag for enabling destructive tools
        """
        try:
            if enabled and not confirm_destructive:
                return {
                    "error": "SAFETY CONFIRMATION REQUIRED",
                    "message": "To enable destructive tools, you must set confirm_destructive=True",
                    "destructive_tools_remain_hidden": True,
                    "safety_notice": "🛡️ SACRED TRUST: Destructive tools can cause data loss. Only enable if you understand the risks."
                }

            affected_modules = []
            total_destructive_tools = 0

            for module_name, module in self._tool_modules.items():
                if hasattr(module, 'enable_destructive_tools'):
                    module.enable_destructive_tools(enabled)
                    affected_modules.append(module_name)

                    # Count destructive tools in this module
                    if hasattr(module, '_tool_metadata'):
                        destructive_count = len([
                            tool for tool, meta in module._tool_metadata.items()
                            if meta.security_level == SecurityLevel.DESTRUCTIVE
                        ])
                        total_destructive_tools += destructive_count

            action = "enabled" if enabled else "disabled"
            status_message = f"Destructive tools {action} across {len(affected_modules)} modules"

            if ctx:
                if enabled:
                    await ctx.warning(f"⚠️ {total_destructive_tools} destructive tools are now visible. Use with extreme caution!")
                else:
                    await ctx.info(f"🛡️ {total_destructive_tools} destructive tools are now hidden for safety")

            return {
                "success": True,
                "destructive_tools_enabled": enabled,
                "affected_modules": affected_modules,
                "total_destructive_tools": total_destructive_tools,
                "message": status_message,
                "safety_reminder": "🛡️ Always use dry_run=True for destructive operations first!"
            }

        except Exception as e:
            await self.log_error(f"Failed to enable destructive tools: {e}", ctx)
            return {"error": str(e)}

    @mcp_tool(
        name="set_safe_mode",
        description="🟢 SAFE: Enable or disable safe mode (when enabled, only safe tools are visible)"
    )
    async def set_safe_mode(self, safe_mode: bool = True, ctx: Context = None) -> Dict[str, Any]:
        """Enable/disable safe mode across all tool modules"""
        try:
            affected_modules = []
            total_safe_tools = 0
            total_hidden_tools = 0

            for module_name, module in self._tool_modules.items():
                if hasattr(module, 'set_safe_mode'):
                    module.set_safe_mode(safe_mode)
                    affected_modules.append(module_name)

                    # Count tools by security level
                    if hasattr(module, '_tool_metadata'):
                        for tool, meta in module._tool_metadata.items():
                            if meta.security_level == SecurityLevel.SAFE:
                                total_safe_tools += 1
                            elif safe_mode:
                                total_hidden_tools += 1

            mode_status = "enabled" if safe_mode else "disabled"

            if ctx:
                if safe_mode:
                    await ctx.info(f"🛡️ Safe mode enabled: {total_safe_tools} safe tools visible, {total_hidden_tools} tools hidden")
                else:
                    await ctx.info(f"🔓 Safe mode disabled: All non-destructive tools now visible")

            return {
                "success": True,
                "safe_mode": safe_mode,
                "affected_modules": affected_modules,
                "visible_safe_tools": total_safe_tools,
                "hidden_tools": total_hidden_tools if safe_mode else 0,
                "message": f"Safe mode {mode_status}"
            }

        except Exception as e:
            await self.log_error(f"Failed to set safe mode: {e}", ctx)
            return {"error": str(e)}

    @mcp_tool(
        name="get_tool_info",
        description="🟢 SAFE: Get detailed metadata and security information for a specific tool"
    )
    async def get_tool_info(self, tool_name: str, ctx: Context = None) -> Dict[str, Any]:
        """Get comprehensive information about a specific tool"""
        try:
            # Search across all modules for the tool
            for module_name, module in self._tool_modules.items():
                if hasattr(module, '_tool_metadata'):
                    metadata = module.get_tool_metadata(tool_name)
                    if metadata:
                        # Check if tool is currently visible
                        is_visible = True
                        if hasattr(module, '_security_state'):
                            state = module._security_state
                            if state.get("safe_mode", True) and metadata.security_level != SecurityLevel.SAFE:
                                is_visible = False
                            elif metadata.security_level == SecurityLevel.DESTRUCTIVE and not state.get("destructive_tools_enabled", False):
                                is_visible = False

                        return {
                            "found": True,
                            "tool_name": tool_name,
                            "module": module_name,
                            "security_level": metadata.security_level,
                            "category": metadata.category,
                            "tags": metadata.tags,
                            "requires_confirmation": metadata.requires_confirmation,
                            "description": metadata.description,
                            "currently_visible": is_visible,
                            "safety_info": {
                                "is_safe": metadata.security_level == SecurityLevel.SAFE,
                                "is_destructive": metadata.security_level == SecurityLevel.DESTRUCTIVE,
                                "confirmation_required": metadata.requires_confirmation
                            }
                        }

            return {
                "found": False,
                "tool_name": tool_name,
                "message": f"Tool '{tool_name}' not found in any registered modules"
            }

        except Exception as e:
            await self.log_error(f"Failed to get tool info: {e}", ctx)
            return {"error": str(e)}

    @mcp_tool(
        name="security_status",
        description="🟢 SAFE: Get current security configuration and tool visibility status"
    )
    async def security_status(self, ctx: Context = None) -> Dict[str, Any]:
        """Get comprehensive security status across all modules"""
        try:
            status = {
                "modules": {},
                "global_stats": {
                    "total_tools": 0,
                    "visible_tools": 0,
                    "safe_tools": 0,
                    "caution_tools": 0,
                    "destructive_tools": 0,
                    "destructive_tools_visible": 0
                }
            }

            for module_name, module in self._tool_modules.items():
                module_status = {
                    "has_security_controls": hasattr(module, '_security_state'),
                    "security_state": {},
                    "tools": {
                        "total": 0,
                        "visible": 0,
                        "by_security_level": {}
                    }
                }

                if hasattr(module, '_security_state'):
                    module_status["security_state"] = module._security_state.copy()

                if hasattr(module, '_tool_metadata'):
                    for tool_name, metadata in module._tool_metadata.items():
                        level = metadata.security_level
                        module_status["tools"]["total"] += 1
                        status["global_stats"]["total_tools"] += 1

                        if level not in module_status["tools"]["by_security_level"]:
                            module_status["tools"]["by_security_level"][level] = {"total": 0, "visible": 0}

                        module_status["tools"]["by_security_level"][level]["total"] += 1

                        # Update global stats
                        if level == SecurityLevel.SAFE:
                            status["global_stats"]["safe_tools"] += 1
                        elif level == SecurityLevel.CAUTION:
                            status["global_stats"]["caution_tools"] += 1
                        elif level == SecurityLevel.DESTRUCTIVE:
                            status["global_stats"]["destructive_tools"] += 1

                        # Check if tool is visible
                        is_visible = True
                        if hasattr(module, '_security_state'):
                            state = module._security_state
                            if state.get("safe_mode", True) and level != SecurityLevel.SAFE:
                                is_visible = False
                            elif level == SecurityLevel.DESTRUCTIVE and not state.get("destructive_tools_enabled", False):
                                is_visible = False

                        if is_visible:
                            module_status["tools"]["visible"] += 1
                            module_status["tools"]["by_security_level"][level]["visible"] += 1
                            status["global_stats"]["visible_tools"] += 1

                            if level == SecurityLevel.DESTRUCTIVE:
                                status["global_stats"]["destructive_tools_visible"] += 1

                status["modules"][module_name] = module_status

            # Add safety summary
            status["safety_summary"] = {
                "destructive_tools_enabled": status["global_stats"]["destructive_tools_visible"] > 0,
                "safe_mode_active": any(
                    module.get("security_state", {}).get("safe_mode", False)
                    for module in status["modules"].values()
                ),
                "protection_level": "HIGH" if status["global_stats"]["destructive_tools_visible"] == 0 else "MEDIUM"
            }

            return status

        except Exception as e:
            await self.log_error(f"Failed to get security status: {e}", ctx)
            return {"error": str(e)}