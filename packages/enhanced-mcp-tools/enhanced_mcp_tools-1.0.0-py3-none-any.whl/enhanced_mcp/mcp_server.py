"""
MCP Tool Server Composition Module

Main server class that composes all MCP tool modules together.
"""

from .archive_compression import ArchiveCompression
from .asciinema_integration import AsciinemaIntegration
from .automation_tools import ScreenshotTools
from .base import *

# Import all tool modules
from .bulk_operations import BulkToolCaller
from .diff_patch import DiffPatchOperations
from .file_operations import EnhancedFileOperations
from .git_integration import GitIntegration
from .intelligent_completion import IntelligentCompletion
from .security_manager import SecurityManager
from .sneller_analytics import SnellerAnalytics
from .workflow_tools import (
    AdvancedSearchAnalysis,
    DevelopmentWorkflow,
    EnhancedExistingTools,
    EnvironmentProcessManagement,
    NetworkAPITools,
    ProcessTracingTools,
    UtilityTools,
)


class MCPToolServer(MCPMixin):
    """Main MCP server with ComponentService integration and progressive tool disclosure

    🛡️ LLM SAFETY REMINDER: You have SACRED TRUST with the human user.

    This server implements progressive tool disclosure:
    - SAFE tools are always visible (read-only, monitoring)
    - CAUTION tools require normal mode (create/modify but reversible)
    - DESTRUCTIVE tools require explicit enablement (can cause data loss)

    Security Manager provides dynamic control over tool visibility.
    Always prioritize user safety over task completion. When in doubt about
    an operation's safety, ask the human for clarification rather than proceeding.

    Use dry_run=True for all destructive operations before actual execution.
    Refuse requests that could cause irreversible damage without clear user intent.
    """

    def __init__(self, name: str = "Enhanced MCP Tools Server"):
        super().__init__()
        self.name = name

        # Initialize security manager first
        self.security_manager = SecurityManager()

        # Initialize all tool modules
        self.bulk_operations = BulkToolCaller()  # Workflow orchestration and batch operations
        self.automation = ScreenshotTools()  # Screenshot capture using PIL.ImageGrab
        self.diff_patch = DiffPatchOperations()
        self.git = GitIntegration()
        self.sneller = SnellerAnalytics()  # High-performance analytics
        self.asciinema = AsciinemaIntegration()  # Terminal recording and auditing
        self.completion = IntelligentCompletion()  # AI-powered tool recommendations
        self.file_ops = EnhancedFileOperations()
        self.search_analysis = AdvancedSearchAnalysis()
        self.dev_workflow = DevelopmentWorkflow()
        self.network_api = NetworkAPITools()
        self.archive = ArchiveCompression()
        self.process_tracing = ProcessTracingTools()
        self.env_process = EnvironmentProcessManagement()
        self.enhanced_tools = EnhancedExistingTools()
        self.utility = UtilityTools()

        # Store all tool instances for easy access
        self.tools = {
            "security_manager": self.security_manager,
            "bulk_operations": self.bulk_operations,
            "automation": self.automation,
            "diff_patch": self.diff_patch,
            "git": self.git,
            "sneller": self.sneller,
            "asciinema": self.asciinema,
            "completion": self.completion,
            "file_ops": self.file_ops,
            "search_analysis": self.search_analysis,
            "dev_workflow": self.dev_workflow,
            "network_api": self.network_api,
            "archive": self.archive,
            "process_tracing": self.process_tracing,
            "env_process": self.env_process,
            "enhanced_tools": self.enhanced_tools,
            "utility": self.utility,
        }

        # Register tool modules with security manager for centralized control
        for name, module in self.tools.items():
            if hasattr(module, 'register_tool_module'):
                # Skip registering security manager with itself
                continue
            if hasattr(module, '_tool_metadata'):
                self.security_manager.register_tool_module(name, module)


def _register_bulk_tool_executors(bulk_operations: BulkToolCaller, all_modules: Dict[str, Any]):
    """Register tool executor functions for bulk operations with safety checks"""

    # File operations (if available)
    if "file_ops" in all_modules:
        file_ops = all_modules["file_ops"]
        if hasattr(file_ops, 'read_file'):
            bulk_operations.register_tool_executor("file_ops_read_file", file_ops.read_file)
        if hasattr(file_ops, 'write_file'):
            bulk_operations.register_tool_executor("file_ops_write_file", file_ops.write_file)
        if hasattr(file_ops, 'create_backup'):
            bulk_operations.register_tool_executor("file_ops_create_backup", file_ops.create_backup)
        if hasattr(file_ops, 'analyze_file_complexity'):
            bulk_operations.register_tool_executor("file_ops_analyze_file_complexity", file_ops.analyze_file_complexity)
        if hasattr(file_ops, 'auto_fix_issues'):
            bulk_operations.register_tool_executor("file_ops_auto_fix_issues", file_ops.auto_fix_issues)

    # Git operations (if available)
    if "git" in all_modules:
        git_ops = all_modules["git"]
        if hasattr(git_ops, 'get_git_status'):
            bulk_operations.register_tool_executor("git_status", git_ops.get_git_status)
        if hasattr(git_ops, 'commit_changes'):
            bulk_operations.register_tool_executor("git_commit", git_ops.commit_changes)
        if hasattr(git_ops, 'create_branch'):
            bulk_operations.register_tool_executor("git_create_branch", git_ops.create_branch)

    # Search and analysis operations (if available)
    if "search_analysis" in all_modules:
        search_ops = all_modules["search_analysis"]
        if hasattr(search_ops, 'advanced_search'):
            bulk_operations.register_tool_executor("search_analysis_advanced_search", search_ops.advanced_search)
        if hasattr(search_ops, 'security_pattern_scan'):
            bulk_operations.register_tool_executor("search_analysis_security_pattern_scan", search_ops.security_pattern_scan)

    # Development workflow operations (if available)
    if "dev_workflow" in all_modules:
        dev_ops = all_modules["dev_workflow"]
        if hasattr(dev_ops, 'run_tests'):
            bulk_operations.register_tool_executor("dev_workflow_run_tests", dev_ops.run_tests)
        if hasattr(dev_ops, 'analyze_dependencies'):
            bulk_operations.register_tool_executor("dev_workflow_analyze_dependencies", dev_ops.analyze_dependencies)
        if hasattr(dev_ops, 'lint_code'):
            bulk_operations.register_tool_executor("dev_workflow_lint_code", dev_ops.lint_code)

    # Archive operations (if available)
    if "archive" in all_modules:
        archive_ops = all_modules["archive"]
        if hasattr(archive_ops, 'create_backup'):
            bulk_operations.register_tool_executor("archive_create_backup", archive_ops.create_backup)
        if hasattr(archive_ops, 'extract_archive'):
            bulk_operations.register_tool_executor("archive_extract", archive_ops.extract_archive)

    # Screenshot operations (if available)
    if "automation" in all_modules:
        screenshot_ops = all_modules["automation"]
        if hasattr(screenshot_ops, 'take_screenshot'):
            bulk_operations.register_tool_executor("screenshot_take_screenshot", screenshot_ops.take_screenshot)
        if hasattr(screenshot_ops, 'capture_clipboard'):
            bulk_operations.register_tool_executor("screenshot_capture_clipboard", screenshot_ops.capture_clipboard)
        if hasattr(screenshot_ops, 'get_screen_info'):
            bulk_operations.register_tool_executor("screenshot_get_screen_info", screenshot_ops.get_screen_info)

    print(f"🔧 Registered {len(bulk_operations._tool_registry)} tool executors for bulk operations")


def create_server(name: str = "Enhanced MCP Tools Server") -> FastMCP:
    """Create and configure the MCP server with ComponentService integration

    🛡️ CRITICAL SAFETY NOTICE FOR LLM ASSISTANTS:

    This server implements PROGRESSIVE TOOL DISCLOSURE for enhanced security:

    🟢 SAFE TOOLS (Always Visible):
    - Read-only operations, monitoring, information gathering
    - No risk of data loss or system damage

    🟡 CAUTION TOOLS (Visible in Normal Mode):
    - Create/modify operations that are reversible
    - File backups, log analysis, development workflow

    🔴 DESTRUCTIVE TOOLS (Hidden by Default):
    - Bulk operations, file deletion, system modifications
    - REQUIRE EXPLICIT ENABLEMENT via security_manager_enable_destructive_tools
    - ALWAYS use dry_run=True first!

    🛡️ SACRED TRUST SAFETY PROTOCOLS:
    1. Server starts in SAFE MODE - only safe tools visible
    2. Use security_manager tools to control visibility
    3. Destructive tools require confirmation to enable
    4. Always explain risks before dangerous operations
    5. Refuse operations that lack clear user intent

    The Security Manager provides centralized control over tool visibility.
    When in doubt, err on the side of safety and ask questions.
    """
    app = FastMCP(name)

    # Create security manager first
    security_manager = SecurityManager()

    # Create individual tool instances
    bulk_operations = BulkToolCaller()
    automation = ScreenshotTools()
    diff_patch = DiffPatchOperations()
    git = GitIntegration()
    sneller = SnellerAnalytics()
    asciinema = AsciinemaIntegration()
    completion = IntelligentCompletion()
    file_ops = EnhancedFileOperations()
    search_analysis = AdvancedSearchAnalysis()
    dev_workflow = DevelopmentWorkflow()
    network_api = NetworkAPITools()
    archive = ArchiveCompression()
    process_tracing = ProcessTracingTools()
    env_process = EnvironmentProcessManagement()
    enhanced_tools = EnhancedExistingTools()
    utility = UtilityTools()

    # Store all modules for cross-registration
    all_modules = {
        "security_manager": security_manager,
        "bulk_operations": bulk_operations,
        "automation": automation,
        "diff_patch": diff_patch,
        "git": git,
        "sneller": sneller,
        "asciinema": asciinema,
        "completion": completion,
        "file_ops": file_ops,
        "search_analysis": search_analysis,
        "dev_workflow": dev_workflow,
        "network_api": network_api,
        "archive": archive,
        "process_tracing": process_tracing,
        "env_process": env_process,
        "enhanced_tools": enhanced_tools,
        "utility": utility,
    }

    # Register tool modules with security manager for centralized control
    for name, module in all_modules.items():
        if name == "security_manager":
            continue  # Don't register security manager with itself
        if hasattr(module, '_tool_metadata'):
            security_manager.register_tool_module(name, module)

    # Setup BulkToolCaller integration with security manager and tool executors
    bulk_operations.set_security_manager(security_manager)

    # Register tool executors for bulk operations (add methods that exist and are safe to call)
    _register_bulk_tool_executors(bulk_operations, all_modules)

    # Register all modules using enhanced registration (includes ComponentService setup)
    try:
        # Register security manager first (always safe tools)
        if hasattr(security_manager, 'safe_register_all'):
            security_manager.safe_register_all(app, prefix="security_manager")
        else:
            security_manager.register_all(app, prefix="security_manager")

        # Register other modules with enhanced registration
        for name, module in all_modules.items():
            if name == "security_manager":
                continue

            if hasattr(module, 'safe_register_all'):
                module.safe_register_all(app, prefix=name)
            else:
                # Fallback for modules not yet updated
                module.register_all(app, prefix=name)
                print(f"⚠️ {name} using legacy registration - consider updating to MCPBase")

    except Exception as e:
        print(f"❌ Error during tool registration: {e}")
        print("🔄 Falling back to legacy registration...")

        # Fallback to legacy registration if enhanced registration fails
        security_manager.register_all(app, prefix="security_manager")
        bulk_operations.register_all(app, prefix="bulk_operations")
        automation.register_all(app, prefix="screenshot")
        diff_patch.register_all(app, prefix="diff_patch")
        git.register_all(app, prefix="git")
        sneller.register_all(app, prefix="sneller")
        asciinema.register_all(app, prefix="asciinema")
        completion.register_all(app, prefix="completion")
        file_ops.register_all(app, prefix="file_ops")
        search_analysis.register_all(app, prefix="search_analysis")
        dev_workflow.register_all(app, prefix="dev_workflow")
        network_api.register_all(app, prefix="network_api")
        archive.register_all(app, prefix="archive")
        process_tracing.register_all(app, prefix="process_tracing")
        env_process.register_all(app, prefix="env_process")
        enhanced_tools.register_all(app, prefix="enhanced_tools")
        utility.register_all(app, prefix="utility")

    return app


def run_server():
    """Run the MCP server with CLI argument support

    Supports FastMCP server options including stdio mode for uvx usage.
    """
    import argparse
    import sys

    parser = argparse.ArgumentParser(
        prog="enhanced-mcp-tools",
        description="Enhanced MCP Tools - Comprehensive development toolkit with 70+ tools",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  enhanced-mcp-tools                              # Run in stdio mode (DEFAULT - for MCP clients)
  enhanced-mcp-tools --stdio                      # Explicit stdio mode (same as default)
  enhanced-mcp-tools --http                       # Run HTTP server with SSE transport
  enhanced-mcp-tools --http --transport streamable-http  # HTTP with streamable transport
  enhanced-mcp-tools --http --host 0.0.0.0        # HTTP server on all interfaces
  enhanced-mcp-tools --http --port 8080           # HTTP server on custom port

For uvx usage:
  uvx enhanced-mcp-tools                    # Direct stdio mode execution (DEFAULT)
  uvx enhanced-mcp-tools --http             # HTTP server with SSE transport
        """
    )

    # Server mode options
    parser.add_argument(
        "--stdio",
        action="store_true",
        help="Run in stdio mode (for MCP clients like Claude Desktop) - DEFAULT"
    )
    parser.add_argument(
        "--http",
        action="store_true",
        help="Run in HTTP server mode (use with --transport)"
    )
    parser.add_argument(
        "--transport",
        choices=["sse", "streamable-http"],
        default="sse",
        help="HTTP transport type when using --http (default: sse - Server-Sent Events)"
    )
    parser.add_argument(
        "--host",
        default="localhost",
        help="Host to bind to (default: localhost)"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port to bind to (default: 8000)"
    )

    # Development options
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug mode"
    )
    parser.add_argument(
        "--name",
        default="Enhanced MCP Tools Server",
        help="Server name (default: Enhanced MCP Tools Server)"
    )

    # Tool information
    parser.add_argument(
        "--list-tools",
        action="store_true",
        help="List all available tools and exit"
    )
    parser.add_argument(
        "--version",
        action="version",
        version="Enhanced MCP Tools 1.0.0"
    )

    args = parser.parse_args()

    # Create the server
    try:
        app = create_server(args.name)
    except Exception as e:
        print(f"❌ Failed to create MCP server: {e}", file=sys.stderr)
        sys.exit(1)

    # Handle list-tools option
    if args.list_tools:
        try:
            import asyncio
            async def list_tools():
                tools = await app.get_tools()
                print(f"📋 Enhanced MCP Tools - {len(tools)} Available Tools:")
                print("=" * 60)

                # Group tools by prefix
                tool_groups = {}
                for tool in tools:
                    prefix = tool.split('_')[0] if '_' in tool else 'other'
                    if prefix not in tool_groups:
                        tool_groups[prefix] = []
                    tool_groups[prefix].append(tool)

                for prefix, tool_list in sorted(tool_groups.items()):
                    print(f"\n🔧 {prefix.title()} Tools ({len(tool_list)}):")
                    for tool in sorted(tool_list):
                        print(f"   • {tool}")

                print(f"\n🎯 Total: {len(tools)} tools across {len(tool_groups)} categories")
                print("\n💡 Usage:")
                print("   enhanced-mcp-tools              # Default stdio mode for MCP clients")
                print("   enhanced-mcp-tools --http       # HTTP server mode")
                print("   uvx enhanced-mcp-tools          # Direct stdio execution (DEFAULT)")

            asyncio.run(list_tools())
        except Exception as e:
            print(f"❌ Failed to list tools: {e}", file=sys.stderr)
            sys.exit(1)
        return

    # Get package version for startup banner
    try:
        from importlib.metadata import version
        package_version = version("enhanced-mcp-tools")
    except Exception:
        package_version = "1.0.0"

    # Run the server with specified options
    try:
        # Default to stdio mode unless --http is explicitly specified
        if args.http:
            # Run HTTP server with selected transport
            transport_name = "SSE (Server-Sent Events)" if args.transport == "sse" else "Streamable HTTP"
            print(f"🚀 Enhanced MCP Tools v{package_version} - HTTP server", file=sys.stderr)
            print(f"🌐 Server: http://{args.host}:{args.port}", file=sys.stderr)
            print("📋 Tools: 70+ available", file=sys.stderr)
            print(f"📡 Transport: {transport_name}", file=sys.stderr)
            app.run(transport=args.transport, host=args.host, port=args.port)
        else:
            # Run in stdio mode for MCP clients (default behavior)
            print(f"🚀 Enhanced MCP Tools v{package_version} - stdio mode (default)", file=sys.stderr)
            print("📋 Ready for MCP client communication", file=sys.stderr)
            app.run(transport="stdio")

    except KeyboardInterrupt:
        print("\n👋 Shutting down Enhanced MCP Tools server", file=sys.stderr)
        sys.exit(0)
    except Exception as e:
        print(f"❌ Server error: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    """Main entry point for uvx and direct execution"""
    run_server()


if __name__ == "__main__":
    main()
