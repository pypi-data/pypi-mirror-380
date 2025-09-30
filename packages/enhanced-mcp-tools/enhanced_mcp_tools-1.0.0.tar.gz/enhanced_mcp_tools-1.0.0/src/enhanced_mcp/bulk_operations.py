"""
Bulk Tool Caller Module

Provides secure batch operations and workflow orchestration for Enhanced MCP Tools.
Integrates with SecurityManager for safety controls and ComponentService for progressive disclosure.
"""

from .base import *
import traceback
import copy
from typing import Callable, Awaitable, Tuple
from dataclasses import dataclass, field
from enum import Enum


class BulkOperationStatus(Enum):
    """Status of bulk operations"""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"
    DRY_RUN = "dry_run"


class BulkOperationMode(Enum):
    """Mode for bulk operation execution"""
    SEQUENTIAL = "sequential"      # Execute one at a time
    PARALLEL = "parallel"         # Execute concurrently
    STAGED = "staged"             # Execute in dependency-aware stages
    INTERACTIVE = "interactive"   # Prompt for confirmation between steps


@dataclass
class BulkOperation:
    """Individual operation within a bulk workflow"""
    id: str
    tool_name: str
    arguments: Dict[str, Any]
    description: str = ""
    depends_on: List[str] = field(default_factory=list)
    security_level: str = SecurityLevel.SAFE
    requires_confirmation: bool = False
    dry_run_safe: bool = True
    status: BulkOperationStatus = BulkOperationStatus.PENDING
    result: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
    execution_time: Optional[float] = None
    rollback_operation: Optional['BulkOperation'] = None


@dataclass
class BulkWorkflow:
    """Collection of operations forming a workflow"""
    id: str
    name: str
    description: str
    operations: List[BulkOperation]
    mode: BulkOperationMode = BulkOperationMode.SEQUENTIAL
    dry_run: bool = True
    status: BulkOperationStatus = BulkOperationStatus.PENDING
    created_at: datetime = field(default_factory=datetime.now)
    total_operations: int = 0
    completed_operations: int = 0
    failed_operations: int = 0
    rollback_available: bool = False


class BulkToolCaller(MCPMixin, MCPBase):
    """Advanced bulk operation and workflow orchestration system

    🟡 CAUTION: This module provides powerful batch operation capabilities

    Features:
    - Safe batch operations with comprehensive dry-run support
    - Workflow orchestration with dependency management
    - Integration with SecurityManager for safety controls
    - Rollback capabilities for reversible operations
    - Common development workflow templates
    - Real-time progress monitoring
    """

    def __init__(self):
        MCPMixin.__init__(self)
        MCPBase.__init__(self)

        # Track active workflows and operations
        self._workflows: Dict[str, BulkWorkflow] = {}
        self._operation_history: List[BulkOperation] = []
        self._tool_registry: Dict[str, Callable] = {}
        self._security_manager = None

        # Register bulk operation tools
        self.register_tagged_tool(
            "create_bulk_workflow",
            security_level=SecurityLevel.SAFE,
            category=ToolCategory.BULK_OPS,
            tags=["workflow", "orchestration", "planning"],
            description="Create a new bulk operation workflow with dependency management"
        )

        self.register_tagged_tool(
            "execute_bulk_workflow",
            security_level=SecurityLevel.CAUTION,
            category=ToolCategory.BULK_OPS,
            tags=["execution", "batch", "workflow"],
            requires_confirmation=True,
            description="Execute a bulk workflow with safety controls and monitoring"
        )

        self.register_tagged_tool(
            "dry_run_bulk_workflow",
            security_level=SecurityLevel.SAFE,
            category=ToolCategory.BULK_OPS,
            tags=["validation", "dry_run", "safety"],
            description="Perform comprehensive dry run validation of bulk workflow"
        )

        self.register_tagged_tool(
            "create_code_analysis_workflow",
            security_level=SecurityLevel.SAFE,
            category=ToolCategory.DEV_WORKFLOW,
            tags=["template", "analysis", "code_quality"],
            description="Create workflow for comprehensive code analysis"
        )

        self.register_tagged_tool(
            "create_fix_and_test_workflow",
            security_level=SecurityLevel.CAUTION,
            category=ToolCategory.DEV_WORKFLOW,
            tags=["template", "fix", "test", "development"],
            requires_confirmation=True,
            description="Create workflow for automated fixing and testing"
        )

        self.register_tagged_tool(
            "rollback_workflow",
            security_level=SecurityLevel.DESTRUCTIVE,
            category=ToolCategory.BULK_OPS,
            tags=["rollback", "recovery", "destructive"],
            requires_confirmation=True,
            description="Rollback changes from a completed workflow (where possible)"
        )

        self.register_tagged_tool(
            "list_workflows",
            security_level=SecurityLevel.SAFE,
            category=ToolCategory.BULK_OPS,
            tags=["listing", "status", "monitoring"],
            description="List all workflows and their current status"
        )

        self.register_tagged_tool(
            "get_workflow_status",
            security_level=SecurityLevel.SAFE,
            category=ToolCategory.BULK_OPS,
            tags=["status", "monitoring", "progress"],
            description="Get detailed status and progress of a specific workflow"
        )

    def set_security_manager(self, security_manager):
        """Set reference to security manager for safety controls"""
        self._security_manager = security_manager

    def register_tool_executor(self, tool_name: str, executor: Callable):
        """Register a tool executor function for bulk operations"""
        self._tool_registry[tool_name] = executor

    async def _validate_tool_safety(self, operation: BulkOperation, ctx: Context = None) -> Tuple[bool, str]:
        """Validate if a tool operation is safe to execute"""
        try:
            # Check if tool exists in registry
            if operation.tool_name not in self._tool_registry:
                return False, f"Tool '{operation.tool_name}' not found in registry"

            # Check security level constraints
            if operation.security_level == SecurityLevel.DESTRUCTIVE:
                if self._security_manager:
                    # Check if destructive tools are enabled
                    if hasattr(self._security_manager, '_tool_modules'):
                        for module in self._security_manager._tool_modules.values():
                            if hasattr(module, '_security_state'):
                                state = module._security_state
                                if not state.get("destructive_tools_enabled", False):
                                    return False, "Destructive tools are not enabled - use security_manager to enable"

            return True, "Operation validated"

        except Exception as e:
            return False, f"Validation error: {str(e)}"

    async def _execute_single_operation(self, operation: BulkOperation, dry_run: bool = True, ctx: Context = None) -> BulkOperation:
        """Execute a single operation with safety controls"""
        start_time = time.time()
        operation.status = BulkOperationStatus.DRY_RUN if dry_run else BulkOperationStatus.RUNNING

        try:
            # Validate operation safety
            is_safe, safety_message = await self._validate_tool_safety(operation, ctx)
            if not is_safe:
                operation.status = BulkOperationStatus.FAILED
                operation.error = f"Safety validation failed: {safety_message}"
                return operation

            # Get tool executor
            executor = self._tool_registry.get(operation.tool_name)
            if not executor:
                operation.status = BulkOperationStatus.FAILED
                operation.error = f"No executor found for tool '{operation.tool_name}'"
                return operation

            # Prepare arguments
            args = operation.arguments.copy()
            if dry_run and operation.dry_run_safe:
                args["dry_run"] = True

            # Add context if executor supports it
            if "ctx" in executor.__code__.co_varnames:
                args["ctx"] = ctx

            # Execute the operation
            if dry_run:
                if ctx:
                    await ctx.info(f"DRY RUN: Would execute {operation.tool_name} with args: {args}")
                operation.result = {"dry_run": True, "would_execute": True, "args": args}
                operation.status = BulkOperationStatus.DRY_RUN
            else:
                operation.result = await executor(**args)
                operation.status = BulkOperationStatus.COMPLETED

                if ctx:
                    await ctx.info(f"✅ Completed: {operation.description or operation.tool_name}")

        except Exception as e:
            operation.status = BulkOperationStatus.FAILED
            operation.error = str(e)
            operation.result = {"error": str(e), "traceback": traceback.format_exc()}

            if ctx:
                await ctx.error(f"❌ Failed: {operation.description or operation.tool_name} - {str(e)}")

        finally:
            operation.execution_time = time.time() - start_time

        return operation

    async def _resolve_dependencies(self, operations: List[BulkOperation]) -> List[List[BulkOperation]]:
        """Resolve operation dependencies and return execution stages"""
        # Create dependency graph
        op_map = {op.id: op for op in operations}
        stages = []
        completed = set()

        while len(completed) < len(operations):
            current_stage = []

            for op in operations:
                if op.id in completed:
                    continue

                # Check if all dependencies are completed
                deps_met = all(dep_id in completed for dep_id in op.depends_on)
                if deps_met:
                    current_stage.append(op)

            if not current_stage:
                # Circular dependency or other issue
                remaining_ops = [op for op in operations if op.id not in completed]
                raise ValueError(f"Cannot resolve dependencies for operations: {[op.id for op in remaining_ops]}")

            stages.append(current_stage)
            completed.update(op.id for op in current_stage)

        return stages

    @mcp_tool(
        name="create_bulk_workflow",
        description="🟢 SAFE: Create a new bulk operation workflow with dependency management"
    )
    async def create_bulk_workflow(
        self,
        name: str,
        description: str,
        operations: List[Dict[str, Any]],
        mode: str = "sequential",
        ctx: Context = None
    ) -> Dict[str, Any]:
        """Create a new bulk workflow

        Args:
            name: Workflow name
            description: Workflow description
            operations: List of operations with tool_name, arguments, etc.
            mode: Execution mode (sequential, parallel, staged, interactive)
        """
        try:
            workflow_id = str(uuid.uuid4())

            # Convert operation dicts to BulkOperation objects
            bulk_operations = []
            for i, op_data in enumerate(operations):
                op_id = op_data.get("id", f"op_{i}")

                operation = BulkOperation(
                    id=op_id,
                    tool_name=op_data["tool_name"],
                    arguments=op_data.get("arguments", {}),
                    description=op_data.get("description", ""),
                    depends_on=op_data.get("depends_on", []),
                    security_level=op_data.get("security_level", SecurityLevel.SAFE),
                    requires_confirmation=op_data.get("requires_confirmation", False),
                    dry_run_safe=op_data.get("dry_run_safe", True)
                )
                bulk_operations.append(operation)

            # Create workflow
            workflow = BulkWorkflow(
                id=workflow_id,
                name=name,
                description=description,
                operations=bulk_operations,
                mode=BulkOperationMode(mode),
                total_operations=len(bulk_operations)
            )

            self._workflows[workflow_id] = workflow

            if ctx:
                await ctx.info(f"Created workflow '{name}' with {len(bulk_operations)} operations")

            return {
                "success": True,
                "workflow_id": workflow_id,
                "name": name,
                "total_operations": len(bulk_operations),
                "mode": mode,
                "requires_destructive_confirmation": any(
                    op.security_level == SecurityLevel.DESTRUCTIVE for op in bulk_operations
                ),
                "safety_reminder": "🛡️ Always run dry_run_bulk_workflow before execution!"
            }

        except Exception as e:
            await self.log_error(f"Failed to create bulk workflow: {e}", ctx)
            return {"error": str(e)}

    @mcp_tool(
        name="dry_run_bulk_workflow",
        description="🟢 SAFE: Perform comprehensive dry run validation of bulk workflow"
    )
    async def dry_run_bulk_workflow(
        self,
        workflow_id: str,
        ctx: Context = None
    ) -> Dict[str, Any]:
        """Perform dry run validation of a workflow"""
        try:
            if workflow_id not in self._workflows:
                return {"error": f"Workflow '{workflow_id}' not found"}

            workflow = self._workflows[workflow_id]

            if ctx:
                await ctx.info(f"🧪 Starting dry run for workflow: {workflow.name}")

            # Resolve dependencies for staged execution
            if workflow.mode == BulkOperationMode.STAGED:
                stages = await self._resolve_dependencies(workflow.operations)
                stage_count = len(stages)
            else:
                stages = [workflow.operations]
                stage_count = 1

            dry_run_results = []
            safety_issues = []

            for stage_idx, stage_operations in enumerate(stages):
                if ctx and stage_count > 1:
                    await ctx.info(f"🔍 Validating stage {stage_idx + 1}/{stage_count}")

                for operation in stage_operations:
                    # Validate each operation
                    is_safe, safety_message = await self._validate_tool_safety(operation, ctx)

                    result = await self._execute_single_operation(operation, dry_run=True, ctx=ctx)
                    dry_run_results.append({
                        "id": result.id,
                        "tool_name": result.tool_name,
                        "description": result.description,
                        "status": result.status.value,
                        "safety_valid": is_safe,
                        "safety_message": safety_message,
                        "would_execute": result.result.get("would_execute", False) if result.result else False,
                        "execution_time_estimate": result.execution_time
                    })

                    if not is_safe:
                        safety_issues.append({
                            "operation_id": result.id,
                            "issue": safety_message
                        })

            # Calculate workflow statistics
            total_ops = len(workflow.operations)
            safe_ops = len([r for r in dry_run_results if r["safety_valid"]])
            destructive_ops = len([
                op for op in workflow.operations
                if op.security_level == SecurityLevel.DESTRUCTIVE
            ])

            return {
                "success": True,
                "workflow_id": workflow_id,
                "workflow_name": workflow.name,
                "dry_run_status": "completed",
                "total_operations": total_ops,
                "safe_operations": safe_ops,
                "destructive_operations": destructive_ops,
                "safety_issues": safety_issues,
                "execution_stages": stage_count,
                "operations": dry_run_results,
                "ready_for_execution": len(safety_issues) == 0,
                "safety_summary": {
                    "all_operations_safe": len(safety_issues) == 0,
                    "destructive_tools_required": destructive_ops > 0,
                    "confirmation_required": any(op.requires_confirmation for op in workflow.operations)
                }
            }

        except Exception as e:
            await self.log_error(f"Dry run failed: {e}", ctx)
            return {"error": str(e)}

    @mcp_tool(
        name="execute_bulk_workflow",
        description="🟡 CAUTION: Execute a bulk workflow with safety controls and monitoring"
    )
    async def execute_bulk_workflow(
        self,
        workflow_id: str,
        dry_run: bool = True,
        confirm_destructive: bool = False,
        continue_on_error: bool = False,
        ctx: Context = None
    ) -> Dict[str, Any]:
        """Execute a bulk workflow with comprehensive safety controls

        Args:
            workflow_id: ID of the workflow to execute
            dry_run: If True, perform dry run only (RECOMMENDED FIRST)
            confirm_destructive: Required confirmation for destructive operations
            continue_on_error: Whether to continue if an operation fails
        """
        try:
            if workflow_id not in self._workflows:
                return {"error": f"Workflow '{workflow_id}' not found"}

            workflow = self._workflows[workflow_id]

            # Safety checks
            destructive_ops = [op for op in workflow.operations if op.security_level == SecurityLevel.DESTRUCTIVE]
            if destructive_ops and not dry_run and not confirm_destructive:
                return {
                    "error": "SAFETY CONFIRMATION REQUIRED",
                    "message": "Workflow contains destructive operations. Set confirm_destructive=True to proceed",
                    "destructive_operations": [op.id for op in destructive_ops],
                    "safety_notice": "🛡️ SACRED TRUST: Destructive operations can cause data loss. Only proceed if you understand the risks."
                }

            workflow.status = BulkOperationStatus.DRY_RUN if dry_run else BulkOperationStatus.RUNNING
            workflow.dry_run = dry_run

            if ctx:
                mode_str = "DRY RUN" if dry_run else "EXECUTION"
                await ctx.info(f"🚀 Starting {mode_str} for workflow: {workflow.name}")

            # Resolve execution order based on mode
            if workflow.mode == BulkOperationMode.STAGED:
                stages = await self._resolve_dependencies(workflow.operations)
            else:
                stages = [workflow.operations]

            execution_results = []

            for stage_idx, stage_operations in enumerate(stages):
                if len(stages) > 1 and ctx:
                    await ctx.info(f"📋 Executing stage {stage_idx + 1}/{len(stages)}")

                if workflow.mode == BulkOperationMode.PARALLEL:
                    # Execute operations in parallel
                    tasks = [
                        self._execute_single_operation(op, dry_run=dry_run, ctx=ctx)
                        for op in stage_operations
                    ]
                    stage_results = await asyncio.gather(*tasks, return_exceptions=True)
                else:
                    # Execute operations sequentially
                    stage_results = []
                    for operation in stage_operations:
                        if workflow.mode == BulkOperationMode.INTERACTIVE and not dry_run:
                            if ctx:
                                await ctx.info(f"🤔 About to execute: {operation.description or operation.tool_name}")
                                await ctx.info("Continue? (This would prompt in interactive mode)")

                        result = await self._execute_single_operation(operation, dry_run=dry_run, ctx=ctx)
                        stage_results.append(result)

                        # Update workflow counters
                        if result.status == BulkOperationStatus.COMPLETED:
                            workflow.completed_operations += 1
                        elif result.status == BulkOperationStatus.FAILED:
                            workflow.failed_operations += 1

                            if not continue_on_error and not dry_run:
                                if ctx:
                                    await ctx.error(f"❌ Stopping workflow due to failed operation: {result.id}")
                                break

                execution_results.extend([
                    result for result in stage_results
                    if not isinstance(result, Exception)
                ])

            # Update workflow status
            if all(result.status in [BulkOperationStatus.COMPLETED, BulkOperationStatus.DRY_RUN]
                   for result in execution_results):
                workflow.status = BulkOperationStatus.DRY_RUN if dry_run else BulkOperationStatus.COMPLETED
            else:
                workflow.status = BulkOperationStatus.FAILED

            # Generate summary
            success_count = len([r for r in execution_results if r.status == BulkOperationStatus.COMPLETED])
            failed_count = len([r for r in execution_results if r.status == BulkOperationStatus.FAILED])

            return {
                "success": workflow.status != BulkOperationStatus.FAILED,
                "workflow_id": workflow_id,
                "workflow_name": workflow.name,
                "execution_mode": "dry_run" if dry_run else "live",
                "status": workflow.status.value,
                "total_operations": len(workflow.operations),
                "completed_operations": success_count,
                "failed_operations": failed_count,
                "execution_stages": len(stages),
                "results": [
                    {
                        "id": r.id,
                        "tool_name": r.tool_name,
                        "status": r.status.value,
                        "execution_time": r.execution_time,
                        "error": r.error
                    }
                    for r in execution_results
                ],
                "next_steps": "Review results and run with dry_run=False if satisfied" if dry_run else "Workflow execution completed"
            }

        except Exception as e:
            await self.log_error(f"Workflow execution failed: {e}", ctx)
            return {"error": str(e)}

    @mcp_tool(
        name="create_code_analysis_workflow",
        description="🟢 SAFE: Create workflow for comprehensive code analysis"
    )
    async def create_code_analysis_workflow(
        self,
        name: str,
        target_path: str,
        include_patterns: Optional[List[str]] = None,
        exclude_patterns: Optional[List[str]] = None,
        ctx: Context = None
    ) -> Dict[str, Any]:
        """Create a comprehensive code analysis workflow template"""
        try:
            operations = [
                {
                    "id": "git_status",
                    "tool_name": "git_status",
                    "arguments": {"path": target_path},
                    "description": "Check Git repository status",
                    "security_level": SecurityLevel.SAFE
                },
                {
                    "id": "search_todos",
                    "tool_name": "search_analysis_advanced_search",
                    "arguments": {
                        "path": target_path,
                        "patterns": ["TODO", "FIXME", "HACK", "XXX"],
                        "file_patterns": include_patterns or ["*.py", "*.js", "*.ts", "*.go", "*.rs"]
                    },
                    "description": "Find TODO and FIXME comments",
                    "security_level": SecurityLevel.SAFE,
                    "depends_on": ["git_status"]
                },
                {
                    "id": "analyze_complexity",
                    "tool_name": "file_ops_analyze_file_complexity",
                    "arguments": {"path": target_path},
                    "description": "Analyze code complexity",
                    "security_level": SecurityLevel.SAFE,
                    "depends_on": ["git_status"]
                },
                {
                    "id": "security_scan",
                    "tool_name": "search_analysis_security_pattern_scan",
                    "arguments": {
                        "path": target_path,
                        "scan_types": ["secrets", "sql_injection", "xss", "hardcoded_passwords"]
                    },
                    "description": "Scan for security issues",
                    "security_level": SecurityLevel.SAFE,
                    "depends_on": ["analyze_complexity"]
                },
                {
                    "id": "dependency_analysis",
                    "tool_name": "dev_workflow_analyze_dependencies",
                    "arguments": {"path": target_path},
                    "description": "Analyze project dependencies",
                    "security_level": SecurityLevel.SAFE,
                    "depends_on": ["security_scan"]
                }
            ]

            result = await self.create_bulk_workflow(
                name=name,
                description=f"Comprehensive code analysis for {target_path}",
                operations=operations,
                mode="staged",
                ctx=ctx
            )

            if result.get("success"):
                result["template_type"] = "code_analysis"
                result["analysis_scope"] = {
                    "target_path": target_path,
                    "include_patterns": include_patterns,
                    "exclude_patterns": exclude_patterns
                }

            return result

        except Exception as e:
            await self.log_error(f"Failed to create code analysis workflow: {e}", ctx)
            return {"error": str(e)}

    @mcp_tool(
        name="create_fix_and_test_workflow",
        description="🟡 CAUTION: Create workflow for automated fixing and testing"
    )
    async def create_fix_and_test_workflow(
        self,
        name: str,
        target_files: List[str],
        backup_enabled: bool = True,
        run_tests: bool = True,
        ctx: Context = None
    ) -> Dict[str, Any]:
        """Create an automated fix and test workflow template"""
        try:
            operations = []

            if backup_enabled:
                operations.append({
                    "id": "create_backup",
                    "tool_name": "archive_create_backup",
                    "arguments": {
                        "source_paths": target_files,
                        "backup_name": f"pre_fix_backup_{int(time.time())}"
                    },
                    "description": "Create backup before making changes",
                    "security_level": SecurityLevel.CAUTION
                })

            # Add file fixing operations
            for i, file_path in enumerate(target_files):
                operations.append({
                    "id": f"fix_file_{i}",
                    "tool_name": "file_ops_auto_fix_issues",
                    "arguments": {
                        "file_path": file_path,
                        "fix_types": ["formatting", "imports", "basic_issues"],
                        "dry_run": True
                    },
                    "description": f"Auto-fix issues in {file_path}",
                    "security_level": SecurityLevel.CAUTION,
                    "depends_on": ["create_backup"] if backup_enabled else []
                })

            if run_tests:
                operations.append({
                    "id": "run_tests",
                    "tool_name": "dev_workflow_run_tests",
                    "arguments": {"test_type": "unit", "coverage": True},
                    "description": "Run tests to verify fixes",
                    "security_level": SecurityLevel.SAFE,
                    "depends_on": [f"fix_file_{i}" for i in range(len(target_files))]
                })

            result = await self.create_bulk_workflow(
                name=name,
                description=f"Automated fix and test workflow for {len(target_files)} files",
                operations=operations,
                mode="staged",
                ctx=ctx
            )

            if result.get("success"):
                result["template_type"] = "fix_and_test"
                result["backup_enabled"] = backup_enabled
                result["test_enabled"] = run_tests
                result["target_files"] = target_files
                result["safety_notice"] = "🛡️ Always run dry_run_bulk_workflow first to validate changes!"

            return result

        except Exception as e:
            await self.log_error(f"Failed to create fix and test workflow: {e}", ctx)
            return {"error": str(e)}

    @mcp_tool(
        name="rollback_workflow",
        description="🔴 DESTRUCTIVE: Rollback changes from a completed workflow (where possible)"
    )
    async def rollback_workflow(
        self,
        workflow_id: str,
        confirm_rollback: bool = False,
        ctx: Context = None
    ) -> Dict[str, Any]:
        """Rollback changes from a completed workflow"""
        try:
            if not confirm_rollback:
                return {
                    "error": "ROLLBACK CONFIRMATION REQUIRED",
                    "message": "Rollback operations can cause data loss. Set confirm_rollback=True to proceed",
                    "safety_notice": "🛡️ SACRED TRUST: Rollback operations are destructive. Only proceed if you understand the risks."
                }

            if workflow_id not in self._workflows:
                return {"error": f"Workflow '{workflow_id}' not found"}

            workflow = self._workflows[workflow_id]

            if workflow.status != BulkOperationStatus.COMPLETED:
                return {"error": "Can only rollback completed workflows"}

            # Check if rollback operations are available
            rollback_ops = [op for op in workflow.operations if op.rollback_operation]
            if not rollback_ops:
                return {"error": "No rollback operations available for this workflow"}

            if ctx:
                await ctx.warning(f"🔄 Starting rollback for workflow: {workflow.name}")

            rollback_results = []
            for operation in reversed(rollback_ops):  # Rollback in reverse order
                if operation.rollback_operation:
                    result = await self._execute_single_operation(
                        operation.rollback_operation,
                        dry_run=False,
                        ctx=ctx
                    )
                    rollback_results.append(result)

            success_count = len([r for r in rollback_results if r.status == BulkOperationStatus.COMPLETED])

            return {
                "success": success_count == len(rollback_results),
                "workflow_id": workflow_id,
                "rollback_operations": len(rollback_results),
                "successful_rollbacks": success_count,
                "results": [
                    {
                        "id": r.id,
                        "tool_name": r.tool_name,
                        "status": r.status.value,
                        "error": r.error
                    }
                    for r in rollback_results
                ]
            }

        except Exception as e:
            await self.log_error(f"Rollback failed: {e}", ctx)
            return {"error": str(e)}

    @mcp_tool(
        name="list_workflows",
        description="🟢 SAFE: List all workflows and their current status"
    )
    async def list_workflows(self, ctx: Context = None) -> Dict[str, Any]:
        """List all workflows with status information"""
        try:
            workflows = []
            for workflow_id, workflow in self._workflows.items():
                workflows.append({
                    "id": workflow_id,
                    "name": workflow.name,
                    "description": workflow.description,
                    "status": workflow.status.value,
                    "mode": workflow.mode.value,
                    "total_operations": workflow.total_operations,
                    "completed_operations": workflow.completed_operations,
                    "failed_operations": workflow.failed_operations,
                    "created_at": workflow.created_at.isoformat(),
                    "rollback_available": workflow.rollback_available
                })

            return {
                "success": True,
                "total_workflows": len(workflows),
                "workflows": workflows,
                "status_summary": {
                    "pending": len([w for w in workflows if w["status"] == "pending"]),
                    "running": len([w for w in workflows if w["status"] == "running"]),
                    "completed": len([w for w in workflows if w["status"] == "completed"]),
                    "failed": len([w for w in workflows if w["status"] == "failed"])
                }
            }

        except Exception as e:
            await self.log_error(f"Failed to list workflows: {e}", ctx)
            return {"error": str(e)}

    @mcp_tool(
        name="get_workflow_status",
        description="🟢 SAFE: Get detailed status and progress of a specific workflow"
    )
    async def get_workflow_status(
        self,
        workflow_id: str,
        include_operation_details: bool = False,
        ctx: Context = None
    ) -> Dict[str, Any]:
        """Get detailed status of a specific workflow"""
        try:
            if workflow_id not in self._workflows:
                return {"error": f"Workflow '{workflow_id}' not found"}

            workflow = self._workflows[workflow_id]

            result = {
                "success": True,
                "workflow_id": workflow_id,
                "name": workflow.name,
                "description": workflow.description,
                "status": workflow.status.value,
                "mode": workflow.mode.value,
                "total_operations": workflow.total_operations,
                "completed_operations": workflow.completed_operations,
                "failed_operations": workflow.failed_operations,
                "progress_percentage": (workflow.completed_operations / workflow.total_operations * 100) if workflow.total_operations > 0 else 0,
                "created_at": workflow.created_at.isoformat(),
                "rollback_available": workflow.rollback_available
            }

            if include_operation_details:
                result["operations"] = [
                    {
                        "id": op.id,
                        "tool_name": op.tool_name,
                        "description": op.description,
                        "status": op.status.value,
                        "security_level": op.security_level,
                        "execution_time": op.execution_time,
                        "error": op.error,
                        "depends_on": op.depends_on
                    }
                    for op in workflow.operations
                ]

            return result

        except Exception as e:
            await self.log_error(f"Failed to get workflow status: {e}", ctx)
            return {"error": str(e)}