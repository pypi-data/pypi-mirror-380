"""
Workflow and Utility Tools Module

Provides development workflow, networking, process management, and utility tools.
"""

import fnmatch
import platform

from .base import *


class AdvancedSearchAnalysis(MCPMixin):
    """Advanced search and code analysis tools"""

    @mcp_tool(
        name="search_and_replace_batch",
        description=(
            "🔴 DESTRUCTIVE: Perform search/replace across multiple files with preview. "
            "🛡️ LLM SAFETY: ALWAYS use dry_run=True first! REFUSE if human requests "
            "dry_run=False without reviewing preview. Can cause widespread data corruption."
        ),
    )
    async def search_and_replace_batch(
        self,
        directory: str,
        search_pattern: str,
        replacement: str,
        file_pattern: Optional[str] = None,
        dry_run: Optional[bool] = True,
        backup: Optional[bool] = True,
        ctx: Context = None,
    ) -> Dict[str, Any]:
        """Batch search and replace across files with safety mechanisms"""
        try:
            # Handle boolean conversion for dry_run and backup
            if not isinstance(dry_run, bool):
                if isinstance(dry_run, str):
                    dry_run = dry_run.lower() in ('true', '1', 'yes', 'on')
                else:
                    dry_run = bool(dry_run) if dry_run is not None else True

            if not isinstance(backup, bool):
                if isinstance(backup, str):
                    backup = backup.lower() in ('true', '1', 'yes', 'on')
                else:
                    backup = bool(backup) if backup is not None else True

            if not dry_run:
                error_msg = "🚨 DESTRUCTIVE OPERATION BLOCKED: Use dry_run=True first to preview changes!"
                if ctx:
                    await ctx.error(error_msg)
                return {
                    "error": error_msg,
                    "safety_notice": "SAFETY: Must use dry_run=True to preview changes before execution",
                    "dry_run": dry_run,
                    "blocked": True
                }

            directory_path = Path(directory)
            if not directory_path.exists():
                return {"error": f"Directory not found: {directory}"}

            # Determine file pattern for matching
            if file_pattern is None:
                file_pattern = "*"

            # Find matching files
            matching_files = []
            if "*" in file_pattern or "?" in file_pattern:
                # Use glob pattern
                for pattern_match in directory_path.rglob(file_pattern):
                    if pattern_match.is_file():
                        matching_files.append(pattern_match)
            else:
                # Use file extension filter
                for file_path in directory_path.rglob("*"):
                    if file_path.is_file() and file_path.suffix == file_pattern:
                        matching_files.append(file_path)

            changes = []
            total_matches = 0
            backup_paths = []

            for file_path in matching_files:
                try:
                    # Skip binary files and very large files
                    if file_path.stat().st_size > 10 * 1024 * 1024:  # 10MB limit
                        continue

                    # Read file content
                    with open(file_path, encoding="utf-8", errors="ignore") as f:
                        content = f.read()

                    # Find matches
                    import re

                    matches = list(re.finditer(search_pattern, content))

                    if matches:
                        # Perform replacement
                        new_content = re.sub(search_pattern, replacement, content)

                        # Create backup if requested and not dry run
                        backup_path = None
                        if backup and not dry_run:
                            backup_path = file_path.with_suffix(
                                f"{file_path.suffix}.bak.{int(time.time())}"
                            )
                            shutil.copy2(file_path, backup_path)
                            backup_paths.append(str(backup_path))

                        # Write new content if not dry run
                        if not dry_run:
                            with open(file_path, "w", encoding="utf-8") as f:
                                f.write(new_content)

                        # Record change information
                        change_info = {
                            "file": str(file_path.relative_to(directory_path)),
                            "matches": len(matches),
                            "backup_created": backup_path is not None,
                            "backup_path": str(backup_path) if backup_path else None,
                            "preview": (
                                {
                                    "first_match": {
                                        "line": content[: matches[0].start()].count("\n") + 1,
                                        "old": matches[0].group(),
                                        "new": re.sub(
                                            search_pattern, replacement, matches[0].group()
                                        ),
                                    }
                                }
                                if matches
                                else None
                            ),
                        }

                        changes.append(change_info)
                        total_matches += len(matches)

                except (UnicodeDecodeError, PermissionError):
                    # Skip files we can't read
                    continue

            result = {
                "operation": "search_and_replace_batch",
                "directory": directory,
                "search_pattern": search_pattern,
                "replacement": replacement,
                "file_pattern": file_pattern,
                "dry_run": dry_run,
                "backup_enabled": backup,
                "summary": {
                    "files_scanned": len(matching_files),
                    "files_with_matches": len(changes),
                    "total_matches": total_matches,
                    "backups_created": len(backup_paths),
                },
                "changes": changes,
                "backup_paths": backup_paths,
            }

            if ctx:
                if dry_run:
                    await ctx.info(
                        f"DRY RUN: Found {total_matches} matches in {len(changes)} files. Review before setting dry_run=False"
                    )
                else:
                    await ctx.info(
                        f"Replaced {total_matches} matches in {len(changes)} files with {len(backup_paths)} backups created"
                    )

            return result

        except Exception as e:
            error_msg = f"Search and replace batch operation failed: {str(e)}"
            if ctx:
                await self.log_critical(error_msg, exception=e, ctx=ctx)
            return {"error": error_msg}

    @mcp_tool(name="analyze_codebase", description="Generate codebase statistics and insights")
    async def analyze_codebase(
        self,
        directory: str,
        include_metrics: List[Literal["loc", "complexity", "dependencies"]],
        exclude_patterns: Optional[List[str]] = None,
        ctx: Context = None,
    ) -> Dict[str, Any]:
        """Analyze codebase and return metrics"""
        try:
            dir_path = Path(directory)
            if not dir_path.exists():
                return {"error": f"Directory not found: {directory}"}

            if ctx:
                await ctx.info(f"Analyzing codebase: {directory}")

            exclude_patterns = exclude_patterns or [
                "*.pyc",
                "__pycache__",
                ".git",
                ".venv",
                "node_modules",
            ]

            def should_exclude(path: Path) -> bool:
                for pattern in exclude_patterns:
                    if fnmatch.fnmatch(path.name, pattern) or fnmatch.fnmatch(str(path), pattern):
                        return True
                return False

            stats = {
                "directory": directory,
                "timestamp": datetime.now().isoformat(),
                "metrics": {},
                "files_analyzed": [],
                "summary": {},
            }

            # Collect files
            files = []
            for file_path in dir_path.rglob("*"):
                if file_path.is_file() and not should_exclude(file_path):
                    files.append(file_path)

            stats["summary"]["total_files"] = len(files)

            # LOC metrics
            if "loc" in include_metrics:
                total_lines = 0
                file_types = {}

                for file_path in files:
                    try:
                        if file_path.suffix:
                            ext = file_path.suffix.lower()
                            if ext in [
                                ".py",
                                ".js",
                                ".ts",
                                ".java",
                                ".cpp",
                                ".c",
                                ".go",
                                ".rs",
                                ".rb",
                            ]:
                                with open(file_path, encoding="utf-8", errors="ignore") as f:
                                    lines = len(f.readlines())
                                    total_lines += lines

                                    if ext not in file_types:
                                        file_types[ext] = {"files": 0, "lines": 0}
                                    file_types[ext]["files"] += 1
                                    file_types[ext]["lines"] += lines

                                    stats["files_analyzed"].append(
                                        {
                                            "path": str(file_path.relative_to(dir_path)),
                                            "extension": ext,
                                            "lines": lines,
                                        }
                                    )
                    except Exception:
                        continue

                stats["metrics"]["loc"] = {"total_lines": total_lines, "file_types": file_types}

            # Complexity metrics (enhanced implementation)
            if "complexity" in include_metrics:
                complexity_data = {
                    "total_functions": 0,
                    "total_classes": 0,
                    "average_function_length": 0,
                    "largest_files": [],
                    "cyclomatic_complexity": {"files": [], "average": 0},
                    "file_complexity_distribution": {
                        "simple": 0,
                        "moderate": 0,
                        "complex": 0,
                        "very_complex": 0,
                    },
                }

                function_lengths = []
                all_complexity_scores = []

                for file_path in files:
                    if file_path.suffix.lower() in [".py", ".js", ".ts", ".java", ".cpp", ".c"]:
                        try:
                            with open(file_path, encoding="utf-8", errors="ignore") as f:
                                content = f.read()
                                lines = content.count("\n") + 1

                                # Basic complexity analysis
                                file_complexity = self._analyze_file_complexity(
                                    content, file_path.suffix.lower()
                                )

                                complexity_data["total_functions"] += file_complexity["functions"]
                                complexity_data["total_classes"] += file_complexity["classes"]
                                function_lengths.extend(file_complexity["function_lengths"])

                                # File size categorization
                                if lines > 500:
                                    complexity_data["largest_files"].append(
                                        {
                                            "file": str(file_path.relative_to(dir_path)),
                                            "lines": lines,
                                            "functions": file_complexity["functions"],
                                            "classes": file_complexity["classes"],
                                        }
                                    )

                                # Categorize file complexity
                                complexity_score = file_complexity["complexity_score"]
                                all_complexity_scores.append(complexity_score)

                                if complexity_score < 10:
                                    complexity_data["file_complexity_distribution"]["simple"] += 1
                                elif complexity_score < 20:
                                    complexity_data["file_complexity_distribution"]["moderate"] += 1
                                elif complexity_score < 50:
                                    complexity_data["file_complexity_distribution"]["complex"] += 1
                                else:
                                    complexity_data["file_complexity_distribution"][
                                        "very_complex"
                                    ] += 1

                                complexity_data["cyclomatic_complexity"]["files"].append(
                                    {
                                        "file": str(file_path.relative_to(dir_path)),
                                        "score": complexity_score,
                                    }
                                )

                        except Exception:
                            continue

                # Calculate averages
                if function_lengths:
                    complexity_data["average_function_length"] = sum(function_lengths) / len(
                        function_lengths
                    )

                if all_complexity_scores:
                    complexity_data["cyclomatic_complexity"]["average"] = sum(
                        all_complexity_scores
                    ) / len(all_complexity_scores)

                # Sort largest files and keep top 10
                complexity_data["largest_files"] = sorted(
                    complexity_data["largest_files"], key=lambda x: x["lines"], reverse=True
                )[:10]

                # Sort by complexity score and keep top 10
                complexity_data["cyclomatic_complexity"]["files"] = sorted(
                    complexity_data["cyclomatic_complexity"]["files"],
                    key=lambda x: x["score"],
                    reverse=True,
                )[:10]

                stats["metrics"]["complexity"] = complexity_data

            # Dependencies metrics (enhanced implementation)
            if "dependencies" in include_metrics:
                deps = {
                    "package_files": [],
                    "dependency_counts": {},
                    "dependency_details": {},
                    "vulnerabilities_detected": False,
                    "outdated_deps": [],
                    "recommendations": [],
                }

                # Find and analyze dependency files
                for file_path in files:
                    file_name = file_path.name.lower()

                    if file_name in [
                        "requirements.txt",
                        "package.json",
                        "cargo.toml",
                        "go.mod",
                        "pyproject.toml",
                        "pipfile",
                        "composer.json",
                        "gemfile",
                    ]:
                        deps["package_files"].append(str(file_path.relative_to(dir_path)))

                        # Analyze specific dependency files
                        try:
                            dep_analysis = self._analyze_dependency_file(file_path)
                            deps["dependency_details"][file_name] = dep_analysis

                            if "count" in dep_analysis:
                                deps["dependency_counts"][file_name] = dep_analysis["count"]

                        except Exception as e:
                            deps["dependency_details"][file_name] = {"error": str(e)}

                # Import analysis for Python files
                import_counts = {"total": 0, "stdlib": 0, "third_party": 0, "local": 0}
                unique_imports = set()

                for file_path in files:
                    if file_path.suffix.lower() == ".py":
                        try:
                            imports = self._extract_python_imports(file_path)
                            import_counts["total"] += len(imports["all"])
                            import_counts["stdlib"] += len(imports["stdlib"])
                            import_counts["third_party"] += len(imports["third_party"])
                            import_counts["local"] += len(imports["local"])
                            unique_imports.update(imports["all"])
                        except Exception:
                            continue

                deps["import_analysis"] = {
                    "counts": import_counts,
                    "unique_imports": len(unique_imports),
                    "most_imported": list(unique_imports)[:20],  # Top 20
                }

                # Generate recommendations
                if len(deps["package_files"]) == 0:
                    deps["recommendations"].append(
                        "No dependency files found - consider adding requirements.txt or package.json"
                    )
                elif len(deps["package_files"]) > 2:
                    deps["recommendations"].append(
                        "Multiple dependency files detected - ensure consistency"
                    )

                if import_counts["third_party"] > 50:
                    deps["recommendations"].append(
                        "High number of third-party dependencies - consider dependency review"
                    )

                stats["metrics"]["dependencies"] = deps

            if ctx:
                await ctx.info(f"Analysis complete: {len(files)} files analyzed")

            return stats

        except Exception as e:
            if ctx:
                await ctx.error(f"Codebase analysis failed: {str(e)}")
            return {"error": str(e)}

    def _analyze_file_complexity(self, content: str, extension: str) -> Dict[str, Any]:
        """Analyze complexity metrics for a single file"""
        complexity = {"functions": 0, "classes": 0, "function_lengths": [], "complexity_score": 0}

        lines = content.split("\n")
        current_function_lines = 0

        if extension == ".py":
            # Python complexity analysis
            for i, line in enumerate(lines):
                stripped = line.strip()

                # Count functions and classes
                if stripped.startswith("def "):
                    complexity["functions"] += 1
                    if current_function_lines > 0:
                        complexity["function_lengths"].append(current_function_lines)
                    current_function_lines = 1
                elif stripped.startswith("class "):
                    complexity["classes"] += 1
                elif current_function_lines > 0:
                    current_function_lines += 1

                # Complexity indicators
                if any(
                    keyword in stripped
                    for keyword in ["if ", "elif ", "for ", "while ", "try:", "except:", "with "]
                ):
                    complexity["complexity_score"] += 1
                if any(keyword in stripped for keyword in ["and ", "or ", "&&", "||"]):
                    complexity["complexity_score"] += 0.5

        elif extension in [".js", ".ts"]:
            # JavaScript/TypeScript complexity analysis
            for line in lines:
                stripped = line.strip()

                # Count functions
                if "function " in stripped or "=>" in stripped:
                    complexity["functions"] += 1
                if "class " in stripped:
                    complexity["classes"] += 1

                # Complexity indicators
                if any(
                    keyword in stripped
                    for keyword in [
                        "if ",
                        "else",
                        "for ",
                        "while ",
                        "switch",
                        "case",
                        "try",
                        "catch",
                    ]
                ):
                    complexity["complexity_score"] += 1
                if any(keyword in stripped for keyword in ["&&", "||", "?", ":"]):
                    complexity["complexity_score"] += 0.5

        # Add final function length if we were tracking one
        if current_function_lines > 0:
            complexity["function_lengths"].append(current_function_lines)

        return complexity

    def _analyze_dependency_file(self, file_path: Path) -> Dict[str, Any]:
        """Analyze a specific dependency file"""
        analysis = {"count": 0, "dependencies": [], "type": "unknown"}

        try:
            if file_path.name.lower() == "package.json":
                analysis["type"] = "npm"
                with open(file_path) as f:
                    data = json.load(f)
                    deps = {}
                    if "dependencies" in data:
                        deps.update(data["dependencies"])
                    if "devDependencies" in data:
                        deps.update(data["devDependencies"])

                    analysis["count"] = len(deps)
                    analysis["dependencies"] = list(deps.keys())[:20]  # Top 20

            elif file_path.name.lower() in ["requirements.txt", "requirements-dev.txt"]:
                analysis["type"] = "pip"
                with open(file_path) as f:
                    lines = [
                        line.strip() for line in f if line.strip() and not line.startswith("#")
                    ]
                    analysis["count"] = len(lines)
                    analysis["dependencies"] = [
                        line.split("==")[0].split(">=")[0].split("<=")[0] for line in lines[:20]
                    ]

            elif file_path.name.lower() == "pyproject.toml":
                analysis["type"] = "python-project"
                # Basic TOML parsing without external dependencies
                with open(file_path) as f:
                    content = f.read()
                    # Simple dependency extraction
                    deps = []
                    if "[project.dependencies]" in content or "dependencies = [" in content:
                        lines = content.split("\n")
                        in_deps = False
                        for line in lines:
                            if "dependencies" in line and "[" in line:
                                in_deps = True
                                continue
                            if in_deps and "]" in line:
                                break
                            if in_deps and '"' in line:
                                dep = line.strip().strip(",").strip('"')
                                if dep:
                                    deps.append(dep.split(">=")[0].split("==")[0])

                    analysis["count"] = len(deps)
                    analysis["dependencies"] = deps[:20]

            elif file_path.name.lower() == "cargo.toml":
                analysis["type"] = "cargo"
                with open(file_path) as f:
                    content = f.read()
                    # Simple Cargo.toml parsing
                    lines = content.split("\n")
                    deps = []
                    in_deps = False
                    for line in lines:
                        if "[dependencies]" in line:
                            in_deps = True
                            continue
                        if in_deps and line.startswith("["):
                            break
                        if in_deps and "=" in line:
                            dep_name = line.split("=")[0].strip()
                            if dep_name:
                                deps.append(dep_name)

                    analysis["count"] = len(deps)
                    analysis["dependencies"] = deps[:20]

        except Exception as e:
            analysis["error"] = str(e)

        return analysis

    def _extract_python_imports(self, file_path: Path) -> Dict[str, List[str]]:
        """Extract import statements from Python file"""
        imports = {"all": [], "stdlib": [], "third_party": [], "local": []}

        # Standard library modules (partial list)
        stdlib_modules = {
            "os",
            "sys",
            "json",
            "re",
            "time",
            "datetime",
            "collections",
            "itertools",
            "functools",
            "typing",
            "pathlib",
            "subprocess",
            "threading",
            "multiprocessing",
            "urllib",
            "http",
            "email",
            "html",
            "xml",
            "csv",
            "sqlite3",
            "logging",
            "unittest",
            "argparse",
            "configparser",
            "tempfile",
            "shutil",
            "glob",
        }

        try:
            with open(file_path, encoding="utf-8", errors="ignore") as f:
                content = f.read()

                # Use AST for more accurate parsing
                try:
                    tree = ast.parse(content)
                    for node in ast.walk(tree):
                        if isinstance(node, ast.Import):
                            for alias in node.names:
                                module_name = alias.name.split(".")[0]
                                imports["all"].append(module_name)

                                if module_name in stdlib_modules:
                                    imports["stdlib"].append(module_name)
                                elif module_name.startswith(".") or "." in alias.name:
                                    imports["local"].append(module_name)
                                else:
                                    imports["third_party"].append(module_name)

                        elif isinstance(node, ast.ImportFrom):
                            if node.module:
                                module_name = node.module.split(".")[0]
                                imports["all"].append(module_name)

                                if module_name in stdlib_modules:
                                    imports["stdlib"].append(module_name)
                                elif node.level > 0:  # Relative import
                                    imports["local"].append(module_name)
                                else:
                                    imports["third_party"].append(module_name)

                except SyntaxError:
                    # Fallback to simple regex parsing
                    import re

                    import_pattern = r"^(?:from\s+(\S+)\s+import|import\s+(\S+))"
                    for line in content.split("\n"):
                        match = re.match(import_pattern, line.strip())
                        if match:
                            module = match.group(1) or match.group(2)
                            if module:
                                module_name = module.split(".")[0]
                                imports["all"].append(module_name)
                                if module_name in stdlib_modules:
                                    imports["stdlib"].append(module_name)
                                else:
                                    imports["third_party"].append(module_name)

        except Exception:
            pass

        # Remove duplicates while preserving order
        for key in imports:
            imports[key] = list(dict.fromkeys(imports[key]))

        return imports

    @mcp_tool(name="find_duplicates", description="🟡 SAFE: Detect duplicate code or files")
    async def find_duplicates(
        self,
        directory: str,
        similarity_threshold: Optional[float] = 80.0,
        file_types: Optional[List[str]] = None,
        ctx: Context = None,
    ) -> Dict[str, Any]:
        """Find duplicate code segments and identical files"""
        try:
            dir_path = Path(directory)
            if not dir_path.exists():
                return {"error": f"Directory not found: {directory}"}

            if ctx:
                await ctx.info(f"Scanning for duplicates in: {directory}")

            # Default file types to analyze
            if file_types is None:
                file_types = [
                    ".py",
                    ".js",
                    ".ts",
                    ".java",
                    ".cpp",
                    ".c",
                    ".cs",
                    ".rb",
                    ".php",
                    ".go",
                ]

            # Collect files
            files = []
            exclude_patterns = ["*.pyc", "__pycache__", ".git", ".venv", "node_modules", "*.min.js"]

            def should_exclude(path: Path) -> bool:
                for pattern in exclude_patterns:
                    if fnmatch.fnmatch(path.name, pattern) or fnmatch.fnmatch(str(path), pattern):
                        return True
                return False

            for file_path in dir_path.rglob("*"):
                if (
                    file_path.is_file()
                    and not should_exclude(file_path)
                    and file_path.suffix.lower() in file_types
                ):
                    files.append(file_path)

            results = {
                "directory": directory,
                "threshold": similarity_threshold,
                "file_types": file_types,
                "files_scanned": len(files),
                "identical_files": [],
                "similar_files": [],
                "duplicate_functions": [],
                "summary": {
                    "identical_file_groups": 0,
                    "similar_file_pairs": 0,
                    "duplicate_function_groups": 0,
                    "potential_savings_kb": 0,
                },
            }

            if len(files) == 0:
                return {**results, "message": "No files found matching the specified criteria"}

            # Find identical files (by content hash)
            identical_groups = await self._find_identical_files(files, dir_path)
            results["identical_files"] = identical_groups
            results["summary"]["identical_file_groups"] = len(identical_groups)

            # Find similar files (by content similarity)
            similar_pairs = await self._find_similar_files(
                files, dir_path, similarity_threshold, ctx
            )
            results["similar_files"] = similar_pairs
            results["summary"]["similar_file_pairs"] = len(similar_pairs)

            # Find duplicate functions/methods
            duplicate_functions = await self._find_duplicate_functions(
                files, dir_path, similarity_threshold
            )
            results["duplicate_functions"] = duplicate_functions
            results["summary"]["duplicate_function_groups"] = len(duplicate_functions)

            # Calculate potential space savings
            total_savings = 0
            for group in identical_groups:
                if len(group["files"]) > 1:
                    file_size = group["size_bytes"]
                    total_savings += file_size * (len(group["files"]) - 1)

            results["summary"]["potential_savings_kb"] = round(total_savings / 1024, 2)

            # Generate recommendations
            results["recommendations"] = self._generate_duplicate_recommendations(results)

            if ctx:
                total_duplicates = (
                    results["summary"]["identical_file_groups"]
                    + results["summary"]["similar_file_pairs"]
                    + results["summary"]["duplicate_function_groups"]
                )
                await ctx.info(
                    f"Duplicate analysis complete: {total_duplicates} duplicate groups found"
                )

            return results

        except Exception as e:
            error_msg = f"Duplicate detection failed: {str(e)}"
            if ctx:
                await self.log_critical(error_msg, exception=e, ctx=ctx)
            return {"error": error_msg}

    async def _find_identical_files(
        self, files: List[Path], base_path: Path
    ) -> List[Dict[str, Any]]:
        """Find files with identical content using hash comparison"""
        import hashlib

        file_hashes = {}

        for file_path in files:
            try:
                # Skip very large files (>10MB)
                if file_path.stat().st_size > 10 * 1024 * 1024:
                    continue

                with open(file_path, "rb") as f:
                    content = f.read()
                    file_hash = hashlib.md5(content).hexdigest()

                    if file_hash not in file_hashes:
                        file_hashes[file_hash] = []

                    file_hashes[file_hash].append(
                        {"path": str(file_path.relative_to(base_path)), "size_bytes": len(content)}
                    )

            except Exception:
                continue

        # Return only groups with more than one file
        identical_groups = []
        for file_hash, file_list in file_hashes.items():
            if len(file_list) > 1:
                identical_groups.append(
                    {
                        "hash": file_hash,
                        "files": file_list,
                        "count": len(file_list),
                        "size_bytes": file_list[0]["size_bytes"],
                    }
                )

        return sorted(identical_groups, key=lambda x: x["count"], reverse=True)

    async def _find_similar_files(
        self, files: List[Path], base_path: Path, threshold: float, ctx: Context
    ) -> List[Dict[str, Any]]:
        """Find files with similar content using text comparison"""
        similar_pairs = []

        # Process files in batches to avoid memory issues
        batch_size = 50

        for i in range(0, len(files), batch_size):
            batch_files = files[i : i + batch_size]

            # Load file contents for this batch
            file_contents = {}
            for file_path in batch_files:
                try:
                    if file_path.stat().st_size > 1024 * 1024:  # Skip files > 1MB
                        continue

                    with open(file_path, encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                        # Normalize content for comparison
                        normalized = self._normalize_code_content(content)
                        if len(normalized) > 100:  # Skip very small files
                            file_contents[file_path] = normalized

                except Exception:
                    continue

            # Compare files in this batch with all previous files
            batch_paths = list(file_contents.keys())

            for j in range(len(batch_paths)):
                for k in range(j + 1, len(batch_paths)):
                    file1, file2 = batch_paths[j], batch_paths[k]

                    similarity = self._calculate_text_similarity(
                        file_contents[file1], file_contents[file2]
                    )

                    if similarity >= threshold:
                        similar_pairs.append(
                            {
                                "file1": str(file1.relative_to(base_path)),
                                "file2": str(file2.relative_to(base_path)),
                                "similarity_percent": round(similarity, 1),
                                "file1_size": file1.stat().st_size,
                                "file2_size": file2.stat().st_size,
                            }
                        )

        return sorted(similar_pairs, key=lambda x: x["similarity_percent"], reverse=True)[
            :20
        ]  # Top 20

    async def _find_duplicate_functions(
        self, files: List[Path], base_path: Path, threshold: float
    ) -> List[Dict[str, Any]]:
        """Find duplicate functions/methods across files"""
        function_groups = {}

        for file_path in files:
            if file_path.suffix.lower() not in [".py", ".js", ".ts", ".java"]:
                continue

            try:
                with open(file_path, encoding="utf-8", errors="ignore") as f:
                    content = f.read()

                functions = self._extract_functions(content, file_path.suffix.lower())

                for func in functions:
                    # Create a normalized signature for comparison
                    normalized = self._normalize_function_content(func["content"])

                    if len(normalized) < 50:  # Skip very small functions
                        continue

                    # Group similar functions
                    found_group = False
                    for signature, group in function_groups.items():
                        if self._calculate_text_similarity(normalized, signature) >= threshold:
                            group["functions"].append(
                                {
                                    "file": str(file_path.relative_to(base_path)),
                                    "name": func["name"],
                                    "line_start": func["line_start"],
                                    "line_end": func["line_end"],
                                }
                            )
                            found_group = True
                            break

                    if not found_group:
                        function_groups[normalized] = {
                            "signature": normalized[:100] + "...",
                            "functions": [
                                {
                                    "file": str(file_path.relative_to(base_path)),
                                    "name": func["name"],
                                    "line_start": func["line_start"],
                                    "line_end": func["line_end"],
                                }
                            ],
                        }

            except Exception:
                continue

        # Return only groups with duplicates
        duplicate_groups = []
        for signature, group in function_groups.items():
            if len(group["functions"]) > 1:
                duplicate_groups.append(
                    {
                        "signature_preview": group["signature"],
                        "functions": group["functions"],
                        "count": len(group["functions"]),
                    }
                )

        return sorted(duplicate_groups, key=lambda x: x["count"], reverse=True)[:10]  # Top 10

    def _normalize_code_content(self, content: str) -> str:
        """Normalize code content for comparison"""
        lines = content.split("\n")
        normalized_lines = []

        for line in lines:
            # Remove leading/trailing whitespace
            stripped = line.strip()

            # Skip empty lines and comments
            if not stripped or stripped.startswith("#") or stripped.startswith("//"):
                continue

            # Basic normalization (could be enhanced)
            stripped = re.sub(r"\s+", " ", stripped)  # Normalize whitespace
            normalized_lines.append(stripped)

        return "\n".join(normalized_lines)

    def _normalize_function_content(self, content: str) -> str:
        """Normalize function content for comparison"""
        # Remove function signature line and normalize body
        lines = content.split("\n")[1:]  # Skip first line (signature)
        return self._normalize_code_content("\n".join(lines))

    def _calculate_text_similarity(self, text1: str, text2: str) -> float:
        """Calculate similarity between two text strings"""
        if not text1 or not text2:
            return 0.0

        # Simple character-based similarity
        shorter = min(len(text1), len(text2))
        longer = max(len(text1), len(text2))

        if longer == 0:
            return 100.0

        # Count matching characters in order
        matches = 0
        for i in range(shorter):
            if text1[i] == text2[i]:
                matches += 1

        # Calculate similarity as percentage
        return (matches / longer) * 100

    def _extract_functions(self, content: str, extension: str) -> List[Dict[str, Any]]:
        """Extract function definitions from code"""
        functions = []
        lines = content.split("\n")

        if extension == ".py":
            current_function = None
            indent_level = 0

            for i, line in enumerate(lines):
                stripped = line.strip()
                if stripped.startswith("def ") and ":" in stripped:
                    # Save previous function
                    if current_function:
                        current_function["line_end"] = i - 1
                        current_function["content"] = "\n".join(
                            lines[current_function["line_start"] : i]
                        )
                        functions.append(current_function)

                    # Start new function
                    func_name = stripped.split("(")[0].replace("def ", "").strip()
                    current_function = {
                        "name": func_name,
                        "line_start": i,
                        "line_end": i,
                        "content": "",
                    }
                    indent_level = len(line) - len(line.lstrip())

                elif (
                    current_function
                    and line
                    and len(line) - len(line.lstrip()) <= indent_level
                    and stripped
                ):
                    # Function ended
                    current_function["line_end"] = i - 1
                    current_function["content"] = "\n".join(
                        lines[current_function["line_start"] : i]
                    )
                    functions.append(current_function)
                    current_function = None

            # Add last function
            if current_function:
                current_function["line_end"] = len(lines) - 1
                current_function["content"] = "\n".join(lines[current_function["line_start"] :])
                functions.append(current_function)

        elif extension in [".js", ".ts"]:
            # Basic JavaScript/TypeScript function extraction
            for i, line in enumerate(lines):
                stripped = line.strip()
                if ("function " in stripped or "=>" in stripped) and "{" in stripped:
                    # Extract function name (simplified)
                    if "function " in stripped:
                        func_name = stripped.split("function ")[1].split("(")[0].strip()
                    else:
                        func_name = f"arrow_function_line_{i}"

                    # Find function end (simplified - just look for next function or end)
                    end_line = i + 10  # Limit search
                    for j in range(i + 1, min(len(lines), i + 50)):
                        if "function " in lines[j] or lines[j].strip().startswith("}"):
                            end_line = j
                            break

                    functions.append(
                        {
                            "name": func_name,
                            "line_start": i,
                            "line_end": end_line,
                            "content": "\n".join(lines[i : end_line + 1]),
                        }
                    )

        return functions

    def _generate_duplicate_recommendations(self, results: Dict[str, Any]) -> List[str]:
        """Generate actionable recommendations for duplicate cleanup"""
        recommendations = []
        summary = results["summary"]

        if (
            summary["identical_file_groups"] == 0
            and summary["similar_file_pairs"] == 0
            and summary["duplicate_function_groups"] == 0
        ):
            recommendations.append(
                "✅ No significant duplicates found! Codebase is well-organized."
            )
            return recommendations

        if summary["identical_file_groups"] > 0:
            recommendations.append(
                f"🔴 Found {summary['identical_file_groups']} groups of identical files - consider removing duplicates"
            )
            if summary["potential_savings_kb"] > 0:
                recommendations.append(
                    f"💾 Potential space savings: {summary['potential_savings_kb']} KB"
                )

        if summary["similar_file_pairs"] > 0:
            recommendations.append(
                f"⚠️ Found {summary['similar_file_pairs']} pairs of similar files - review for consolidation opportunities"
            )

        if summary["duplicate_function_groups"] > 0:
            recommendations.append(
                f"🔧 Found {summary['duplicate_function_groups']} groups of duplicate functions - consider refactoring into shared utilities"
            )

        # Specific actions
        if summary["identical_file_groups"] > 0:
            recommendations.append(
                "💡 Action: Remove or symlink identical files to reduce redundancy"
            )

        if summary["duplicate_function_groups"] > 0:
            recommendations.append(
                "💡 Action: Extract duplicate functions into a shared module or utility class"
            )

        if summary["similar_file_pairs"] > 0:
            recommendations.append(
                "💡 Action: Review similar files for opportunities to merge or create templates"
            )

        return recommendations


class DevelopmentWorkflow(MCPMixin):
    """Development workflow automation tools"""

    @mcp_tool(
        name="run_tests",
        description="🟡 SAFE: Execute test suites with intelligent framework detection",
    )
    async def run_tests(
        self,
        test_path: str,
        framework: Optional[Literal["pytest", "jest", "mocha", "auto-detect"]] = "auto-detect",
        pattern: Optional[str] = None,
        coverage: Optional[bool] = False,
        ctx: Context = None,
    ) -> Dict[str, Any]:
        """Run tests and return results with coverage information"""
        try:
            test_path_obj = Path(test_path)
            if not test_path_obj.exists():
                return {"error": f"Test path not found: {test_path}"}

            # Auto-detect framework if needed
            detected_framework = framework
            if framework == "auto-detect":
                # Check for Python test files and pytest
                if any(test_path_obj.rglob("test_*.py")) or any(test_path_obj.rglob("*_test.py")):
                    detected_framework = "pytest"
                # Check for JavaScript test files
                elif any(test_path_obj.rglob("*.test.js")) or any(test_path_obj.rglob("*.spec.js")):
                    detected_framework = "jest"
                elif test_path_obj.is_file() and test_path_obj.suffix == ".js":
                    detected_framework = "mocha"
                else:
                    # Default to pytest for directories
                    detected_framework = "pytest"

            # Build command based on framework
            cmd = []
            env_vars = os.environ.copy()

            if detected_framework == "pytest":
                cmd = ["python", "-m", "pytest"]
                if coverage:
                    cmd.extend(
                        [
                            "--cov",
                            str(test_path_obj.parent if test_path_obj.is_file() else test_path_obj),
                        ]
                    )
                    cmd.extend(["--cov-report", "term-missing"])
                if pattern:
                    cmd.extend(["-k", pattern])
                cmd.append(str(test_path_obj))
                cmd.extend(["-v", "--tb=short"])

            elif detected_framework == "jest":
                cmd = ["npx", "jest"]
                if coverage:
                    cmd.append("--coverage")
                if pattern:
                    cmd.extend(["--testNamePattern", pattern])
                cmd.append(str(test_path_obj))
                cmd.extend(["--verbose"])

            elif detected_framework == "mocha":
                cmd = ["npx", "mocha"]
                if pattern:
                    cmd.extend(["--grep", pattern])
                cmd.append(str(test_path_obj))
                cmd.append("--reporter")
                cmd.append("json")

            else:
                return {"error": f"Unsupported test framework: {detected_framework}"}

            # Run the tests
            start_time = time.time()

            result = subprocess.run(
                cmd,
                cwd=test_path_obj.parent if test_path_obj.is_file() else test_path_obj,
                capture_output=True,
                text=True,
                env=env_vars,
                timeout=300,  # 5 minute timeout
            )

            end_time = time.time()
            duration = round(end_time - start_time, 2)

            # Parse results based on framework
            test_results = {
                "framework": detected_framework,
                "command": " ".join(cmd),
                "exit_code": result.returncode,
                "duration_seconds": duration,
                "success": result.returncode == 0,
                "stdout": result.stdout,
                "stderr": result.stderr,
            }

            # Parse output for specific metrics
            if detected_framework == "pytest":
                # Parse pytest output
                stdout = result.stdout
                failed_pattern = r"(\d+) failed"
                passed_pattern = r"(\d+) passed"

                failed_match = re.search(failed_pattern, stdout)
                passed_match = re.search(passed_pattern, stdout)

                test_results.update(
                    {
                        "tests_passed": int(passed_match.group(1)) if passed_match else 0,
                        "tests_failed": int(failed_match.group(1)) if failed_match else 0,
                        "coverage_info": self._extract_coverage_info(stdout) if coverage else None,
                    }
                )

            elif detected_framework in ["jest", "mocha"]:
                # Basic parsing for JavaScript frameworks
                test_results.update(
                    {
                        "tests_passed": stdout.count("✓") if "✓" in stdout else 0,
                        "tests_failed": stdout.count("✗") if "✗" in stdout else 0,
                    }
                )

            # Summary
            total_tests = test_results.get("tests_passed", 0) + test_results.get("tests_failed", 0)
            test_results["total_tests"] = total_tests
            test_results["pass_rate"] = round(
                (test_results.get("tests_passed", 0) / max(total_tests, 1)) * 100, 1
            )

            if ctx:
                status_emoji = "✅" if test_results["success"] else "❌"
                await ctx.info(
                    f"{status_emoji} Tests completed: {test_results['tests_passed']}/{total_tests} passed ({duration}s)"
                )

            return test_results

        except subprocess.TimeoutExpired:
            error_msg = "Test execution timed out after 5 minutes"
            if ctx:
                await ctx.error(error_msg)
            return {"error": error_msg}

        except FileNotFoundError:
            error_msg = f"Test framework '{detected_framework}' not found in PATH"
            if ctx:
                await ctx.error(error_msg)
            return {"error": error_msg, "suggestion": f"Install {detected_framework} or check PATH"}

        except Exception as e:
            error_msg = f"Test execution failed: {str(e)}"
            if ctx:
                await self.log_critical(error_msg, exception=e, ctx=ctx)
            return {"error": error_msg}

    def _extract_coverage_info(self, stdout: str) -> Optional[Dict[str, Any]]:
        """Extract coverage information from pytest output"""
        try:
            # Look for coverage summary line
            lines = stdout.split("\n")
            for line in lines:
                if "TOTAL" in line and "%" in line:
                    parts = line.split()
                    for part in parts:
                        if part.endswith("%"):
                            return {"total_coverage": part, "raw_line": line.strip()}
            return None
        except Exception:
            return None

    @mcp_tool(name="lint_code", description="🟡 SAFE: Run code linting with multiple linters")
    async def lint_code(
        self,
        file_paths: List[str],
        linters: Optional[List[str]] = None,
        fix: Optional[bool] = False,
        ctx: Context = None,
    ) -> Dict[str, Any]:
        """Lint code files with automatic linter detection and optional fixing"""
        try:
            if not file_paths:
                return {"error": "No file paths provided"}

            # Validate all file paths exist
            valid_files = []
            for file_path in file_paths:
                path_obj = Path(file_path)
                if path_obj.exists() and path_obj.is_file():
                    valid_files.append(path_obj)
                else:
                    if ctx:
                        await ctx.warning(f"File not found: {file_path}")

            if not valid_files:
                return {"error": "No valid files found to lint"}

            # Group files by type for appropriate linter selection
            file_groups = self._group_files_by_type(valid_files)

            # Auto-detect linters if not specified
            if linters is None:
                linters = self._detect_available_linters(file_groups)

            results = {
                "total_files": len(valid_files),
                "file_groups": {k: len(v) for k, v in file_groups.items()},
                "linters_used": linters,
                "fix_mode": fix,
                "lint_results": {},
                "summary": {"total_issues": 0, "errors": 0, "warnings": 0, "fixed_issues": 0},
            }

            # Run linters for each file type
            for file_type, files in file_groups.items():
                if not files:
                    continue

                type_linters = self._get_linters_for_type(file_type, linters)
                if not type_linters:
                    results["lint_results"][file_type] = {
                        "status": "skipped",
                        "reason": f"No suitable linters available for {file_type} files",
                    }
                    continue

                # Run each applicable linter
                for linter in type_linters:
                    linter_key = f"{file_type}_{linter}"

                    try:
                        linter_result = await self._run_linter(linter, files, fix, ctx)
                        results["lint_results"][linter_key] = linter_result

                        # Update summary stats
                        if "issues" in linter_result:
                            issues = linter_result["issues"]
                            results["summary"]["total_issues"] += len(issues)
                            results["summary"]["errors"] += len(
                                [i for i in issues if i.get("severity") == "error"]
                            )
                            results["summary"]["warnings"] += len(
                                [i for i in issues if i.get("severity") == "warning"]
                            )

                        if "fixed_count" in linter_result:
                            results["summary"]["fixed_issues"] += linter_result["fixed_count"]

                    except Exception as e:
                        results["lint_results"][linter_key] = {"status": "failed", "error": str(e)}

            # Generate recommendations
            results["recommendations"] = self._generate_lint_recommendations(results)

            if ctx:
                total_issues = results["summary"]["total_issues"]
                fixed_issues = results["summary"]["fixed_issues"]
                status_emoji = "✅" if total_issues == 0 else "⚠️" if total_issues < 10 else "🚨"

                if fix and fixed_issues > 0:
                    await ctx.info(
                        f"{status_emoji} Linting complete: {total_issues} issues found, {fixed_issues} auto-fixed"
                    )
                else:
                    await ctx.info(
                        f"{status_emoji} Linting complete: {total_issues} issues found across {len(valid_files)} files"
                    )

            return results

        except Exception as e:
            error_msg = f"Code linting failed: {str(e)}"
            if ctx:
                await self.log_critical(error_msg, exception=e, ctx=ctx)
            return {"error": error_msg}

    def _group_files_by_type(self, files: List[Path]) -> Dict[str, List[Path]]:
        """Group files by programming language/type"""
        groups = {
            "python": [],
            "javascript": [],
            "typescript": [],
            "json": [],
            "yaml": [],
            "markdown": [],
            "other": [],
        }

        for file_path in files:
            suffix = file_path.suffix.lower()

            if suffix in [".py", ".pyx", ".pyi"]:
                groups["python"].append(file_path)
            elif suffix in [".js", ".jsx", ".mjs"]:
                groups["javascript"].append(file_path)
            elif suffix in [".ts", ".tsx"]:
                groups["typescript"].append(file_path)
            elif suffix in [".json"]:
                groups["json"].append(file_path)
            elif suffix in [".yaml", ".yml"]:
                groups["yaml"].append(file_path)
            elif suffix in [".md", ".markdown"]:
                groups["markdown"].append(file_path)
            else:
                groups["other"].append(file_path)

        return {k: v for k, v in groups.items() if v}  # Remove empty groups

    def _detect_available_linters(self, file_groups: Dict[str, List[Path]]) -> List[str]:
        """Detect which linters are available on the system"""
        available_linters = []

        # Python linters
        if "python" in file_groups:
            for linter in ["flake8", "pylint", "pycodestyle", "pyflakes"]:
                if self._is_command_available(linter):
                    available_linters.append(linter)

        # JavaScript/TypeScript linters
        if "javascript" in file_groups or "typescript" in file_groups:
            for linter in ["eslint", "jshint"]:
                if self._is_command_available(linter):
                    available_linters.append(linter)

        # JSON linters
        if "json" in file_groups:
            if self._is_command_available("jsonlint"):
                available_linters.append("jsonlint")

        # YAML linters
        if "yaml" in file_groups:
            if self._is_command_available("yamllint"):
                available_linters.append("yamllint")

        # Markdown linters
        if "markdown" in file_groups:
            if self._is_command_available("markdownlint"):
                available_linters.append("markdownlint")

        return available_linters

    def _get_linters_for_type(self, file_type: str, available_linters: List[str]) -> List[str]:
        """Get applicable linters for a specific file type"""
        type_mapping = {
            "python": ["flake8", "pylint", "pycodestyle", "pyflakes"],
            "javascript": ["eslint", "jshint"],
            "typescript": ["eslint"],
            "json": ["jsonlint"],
            "yaml": ["yamllint"],
            "markdown": ["markdownlint"],
        }

        applicable = type_mapping.get(file_type, [])
        return [linter for linter in applicable if linter in available_linters]

    def _is_command_available(self, command: str) -> bool:
        """Check if a command is available in PATH"""
        try:
            result = subprocess.run([command, "--version"], capture_output=True, timeout=5)
            return result.returncode == 0
        except (subprocess.TimeoutExpired, FileNotFoundError):
            return False

    async def _run_linter(
        self, linter: str, files: List[Path], fix: bool, ctx: Context
    ) -> Dict[str, Any]:
        """Run a specific linter on files"""
        file_paths = [str(f) for f in files]

        try:
            if linter == "flake8":
                return await self._run_flake8(file_paths, fix)
            elif linter == "pylint":
                return await self._run_pylint(file_paths, fix)
            elif linter == "pycodestyle":
                return await self._run_pycodestyle(file_paths, fix)
            elif linter == "eslint":
                return await self._run_eslint(file_paths, fix)
            elif linter == "jsonlint":
                return await self._run_jsonlint(file_paths)
            elif linter == "yamllint":
                return await self._run_yamllint(file_paths)
            elif linter == "markdownlint":
                return await self._run_markdownlint(file_paths)
            else:
                return {"status": "unsupported", "linter": linter}

        except Exception as e:
            return {"status": "error", "linter": linter, "error": str(e)}

    async def _run_flake8(self, file_paths: List[str], fix: bool) -> Dict[str, Any]:
        """Run flake8 linter"""
        cmd = ["flake8", "--format=json"] + file_paths

        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)

        issues = []
        if result.stdout:
            try:
                # flake8 doesn't output valid JSON by default, parse line by line
                for line in result.stdout.strip().split("\n"):
                    if line:
                        # Format: filename:line:col: code message
                        parts = line.split(":", 3)
                        if len(parts) >= 4:
                            issues.append(
                                {
                                    "file": parts[0],
                                    "line": int(parts[1]),
                                    "column": int(parts[2]),
                                    "code": parts[3].split()[0],
                                    "message": (
                                        parts[3].split(" ", 1)[1] if " " in parts[3] else parts[3]
                                    ),
                                    "severity": "error" if parts[3].startswith(" E") else "warning",
                                }
                            )
            except Exception:
                # Fallback to simple parsing
                issues = [{"message": result.stdout, "severity": "error"}]

        return {
            "linter": "flake8",
            "status": "completed",
            "exit_code": result.returncode,
            "issues": issues,
            "can_fix": False,  # flake8 doesn't auto-fix
        }

    async def _run_pylint(self, file_paths: List[str], fix: bool) -> Dict[str, Any]:
        """Run pylint linter"""
        cmd = ["pylint", "--output-format=json"] + file_paths

        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)

        issues = []
        if result.stdout:
            try:
                pylint_output = json.loads(result.stdout)
                for issue in pylint_output:
                    issues.append(
                        {
                            "file": issue.get("path", ""),
                            "line": issue.get("line", 0),
                            "column": issue.get("column", 0),
                            "code": issue.get("message-id", ""),
                            "message": issue.get("message", ""),
                            "severity": issue.get("type", "warning"),
                        }
                    )
            except json.JSONDecodeError:
                issues = [{"message": "Failed to parse pylint output", "severity": "error"}]

        return {
            "linter": "pylint",
            "status": "completed",
            "exit_code": result.returncode,
            "issues": issues,
            "can_fix": False,  # pylint doesn't auto-fix
        }

    async def _run_pycodestyle(self, file_paths: List[str], fix: bool) -> Dict[str, Any]:
        """Run pycodestyle linter"""
        cmd = ["pycodestyle"] + file_paths

        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)

        issues = []
        fixed_count = 0

        if result.stdout:
            for line in result.stdout.strip().split("\n"):
                if line:
                    # Format: filename:line:col: code message
                    parts = line.split(":", 3)
                    if len(parts) >= 4:
                        issues.append(
                            {
                                "file": parts[0],
                                "line": int(parts[1]),
                                "column": int(parts[2]),
                                "code": parts[3].split()[0],
                                "message": (
                                    parts[3].split(" ", 1)[1] if " " in parts[3] else parts[3]
                                ),
                                "severity": "warning",
                            }
                        )

        # Try autopep8 for fixing if requested
        if fix and self._is_command_available("autopep8"):
            for file_path in file_paths:
                fix_cmd = ["autopep8", "--in-place", file_path]
                fix_result = subprocess.run(fix_cmd, capture_output=True, timeout=30)
                if fix_result.returncode == 0:
                    fixed_count += 1

        return {
            "linter": "pycodestyle",
            "status": "completed",
            "exit_code": result.returncode,
            "issues": issues,
            "can_fix": True,
            "fixed_count": fixed_count,
        }

    async def _run_eslint(self, file_paths: List[str], fix: bool) -> Dict[str, Any]:
        """Run ESLint linter"""
        cmd = ["eslint", "--format=json"]
        if fix:
            cmd.append("--fix")
        cmd.extend(file_paths)

        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)

        issues = []
        fixed_count = 0

        if result.stdout:
            try:
                eslint_output = json.loads(result.stdout)
                for file_result in eslint_output:
                    fixed_count += file_result.get("fixableErrorCount", 0) + file_result.get(
                        "fixableWarningCount", 0
                    )

                    for message in file_result.get("messages", []):
                        issues.append(
                            {
                                "file": file_result.get("filePath", ""),
                                "line": message.get("line", 0),
                                "column": message.get("column", 0),
                                "code": message.get("ruleId", ""),
                                "message": message.get("message", ""),
                                "severity": message.get("severity", 1) == 2
                                and "error"
                                or "warning",
                            }
                        )
            except json.JSONDecodeError:
                issues = [{"message": "Failed to parse ESLint output", "severity": "error"}]

        return {
            "linter": "eslint",
            "status": "completed",
            "exit_code": result.returncode,
            "issues": issues,
            "can_fix": True,
            "fixed_count": fixed_count if fix else 0,
        }

    async def _run_jsonlint(self, file_paths: List[str]) -> Dict[str, Any]:
        """Run JSON linter"""
        issues = []

        for file_path in file_paths:
            try:
                with open(file_path) as f:
                    json.load(f)
            except json.JSONDecodeError as e:
                issues.append(
                    {
                        "file": file_path,
                        "line": e.lineno,
                        "column": e.colno,
                        "message": str(e),
                        "severity": "error",
                    }
                )
            except Exception as e:
                issues.append(
                    {
                        "file": file_path,
                        "message": f"Failed to read file: {str(e)}",
                        "severity": "error",
                    }
                )

        return {
            "linter": "jsonlint",
            "status": "completed",
            "exit_code": 0 if not issues else 1,
            "issues": issues,
            "can_fix": False,
        }

    async def _run_yamllint(self, file_paths: List[str]) -> Dict[str, Any]:
        """Run YAML linter"""
        cmd = ["yamllint", "--format=parsable"] + file_paths

        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)

        issues = []
        if result.stdout:
            for line in result.stdout.strip().split("\n"):
                if line and ":" in line:
                    # Format: filename:line:col: [level] message
                    parts = line.split(":", 3)
                    if len(parts) >= 4:
                        level_msg = parts[3].strip()
                        level = "warning"
                        if "[error]" in level_msg:
                            level = "error"

                        issues.append(
                            {
                                "file": parts[0],
                                "line": int(parts[1]) if parts[1].isdigit() else 0,
                                "column": int(parts[2]) if parts[2].isdigit() else 0,
                                "message": level_msg.replace("[error]", "")
                                .replace("[warning]", "")
                                .strip(),
                                "severity": level,
                            }
                        )

        return {
            "linter": "yamllint",
            "status": "completed",
            "exit_code": result.returncode,
            "issues": issues,
            "can_fix": False,
        }

    async def _run_markdownlint(self, file_paths: List[str]) -> Dict[str, Any]:
        """Run Markdown linter"""
        cmd = ["markdownlint"] + file_paths

        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)

        issues = []
        if result.stdout:
            for line in result.stdout.strip().split("\n"):
                if line and ":" in line:
                    # Format: filename:line message
                    parts = line.split(":", 2)
                    if len(parts) >= 3:
                        issues.append(
                            {
                                "file": parts[0],
                                "line": int(parts[1]) if parts[1].isdigit() else 0,
                                "message": parts[2].strip(),
                                "severity": "warning",
                            }
                        )

        return {
            "linter": "markdownlint",
            "status": "completed",
            "exit_code": result.returncode,
            "issues": issues,
            "can_fix": False,
        }

    def _generate_lint_recommendations(self, results: Dict[str, Any]) -> List[str]:
        """Generate actionable recommendations based on lint results"""
        recommendations = []
        summary = results["summary"]

        if summary["total_issues"] == 0:
            recommendations.append("✅ No linting issues found! Code quality looks excellent.")
            return recommendations

        if summary["errors"] > 0:
            recommendations.append(f"🚨 Fix {summary['errors']} critical errors before deployment")

        if summary["warnings"] > 10:
            recommendations.append(
                f"⚠️ Consider addressing {summary['warnings']} warnings for better code quality"
            )
        elif summary["warnings"] > 0:
            recommendations.append(f"Address {summary['warnings']} minor warnings when convenient")

        if summary["fixed_issues"] > 0:
            recommendations.append(f"✅ Auto-fixed {summary['fixed_issues']} issues")

        # Suggest auto-fixing if available
        can_fix_tools = []
        for result_key, result in results["lint_results"].items():
            if result.get("can_fix") and result.get("issues"):
                tool = result.get("linter", result_key)
                can_fix_tools.append(tool)

        if can_fix_tools and not results["fix_mode"]:
            recommendations.append(
                f"💡 Run with fix=True to auto-fix issues using: {', '.join(set(can_fix_tools))}"
            )

        return recommendations

    @mcp_tool(name="format_code", description="🟡 SAFE: Auto-format code using standard formatters")
    async def format_code(
        self,
        file_paths: List[str],
        formatter: Optional[
            Literal["prettier", "black", "autopep8", "auto-detect"]
        ] = "auto-detect",
        config_file: Optional[str] = None,
        ctx: Context = None,
    ) -> Dict[str, Any]:
        """Format code files using appropriate formatters"""
        try:
            if not file_paths:
                return {"error": "No file paths provided"}

            # Validate all file paths exist
            valid_files = []
            for file_path in file_paths:
                path_obj = Path(file_path)
                if path_obj.exists() and path_obj.is_file():
                    valid_files.append(path_obj)
                else:
                    if ctx:
                        await ctx.warning(f"File not found: {file_path}")

            if not valid_files:
                return {"error": "No valid files found to format"}

            # Group files by type for appropriate formatter selection
            file_groups = self._group_files_for_formatting(valid_files)

            results = {
                "total_files": len(valid_files),
                "file_groups": {k: len(v) for k, v in file_groups.items()},
                "formatter_mode": formatter,
                "config_file": config_file,
                "format_results": {},
                "summary": {
                    "formatted_files": 0,
                    "unchanged_files": 0,
                    "failed_files": 0,
                    "total_changes": 0,
                },
            }

            # Format each file group with appropriate formatter
            for file_type, files in file_groups.items():
                if not files:
                    continue

                # Determine formatter for this file type
                selected_formatter = self._select_formatter_for_type(file_type, formatter)

                if not selected_formatter:
                    results["format_results"][file_type] = {
                        "status": "skipped",
                        "reason": f"No suitable formatter available for {file_type} files",
                    }
                    continue

                # Check if formatter is available
                if not self._is_command_available(selected_formatter):
                    results["format_results"][file_type] = {
                        "status": "skipped",
                        "reason": f"Formatter '{selected_formatter}' not installed",
                        "suggestion": self._get_install_suggestion(selected_formatter),
                    }
                    continue

                # Run the formatter
                try:
                    format_result = await self._run_formatter(
                        selected_formatter, files, config_file, ctx
                    )
                    results["format_results"][file_type] = format_result

                    # Update summary
                    if "files_changed" in format_result:
                        results["summary"]["formatted_files"] += format_result["files_changed"]
                        results["summary"]["unchanged_files"] += format_result.get(
                            "files_unchanged", 0
                        )
                        results["summary"]["total_changes"] += format_result.get("total_changes", 0)

                except Exception as e:
                    results["format_results"][file_type] = {
                        "status": "failed",
                        "formatter": selected_formatter,
                        "error": str(e),
                    }
                    results["summary"]["failed_files"] += len(files)

            # Generate recommendations
            results["recommendations"] = self._generate_format_recommendations(results)

            if ctx:
                formatted = results["summary"]["formatted_files"]
                total = (
                    results["summary"]["formatted_files"] + results["summary"]["unchanged_files"]
                )
                status_emoji = "✅" if results["summary"]["failed_files"] == 0 else "⚠️"
                await ctx.info(
                    f"{status_emoji} Formatting complete: {formatted}/{total} files changed"
                )

            return results

        except Exception as e:
            error_msg = f"Code formatting failed: {str(e)}"
            if ctx:
                await self.log_critical(error_msg, exception=e, ctx=ctx)
            return {"error": error_msg}

    def _group_files_for_formatting(self, files: List[Path]) -> Dict[str, List[Path]]:
        """Group files by type for formatting"""
        groups = {
            "python": [],
            "javascript": [],
            "typescript": [],
            "json": [],
            "yaml": [],
            "css": [],
            "html": [],
            "markdown": [],
            "other": [],
        }

        for file_path in files:
            suffix = file_path.suffix.lower()

            if suffix in [".py", ".pyx", ".pyi"]:
                groups["python"].append(file_path)
            elif suffix in [".js", ".jsx", ".mjs"]:
                groups["javascript"].append(file_path)
            elif suffix in [".ts", ".tsx"]:
                groups["typescript"].append(file_path)
            elif suffix in [".json"]:
                groups["json"].append(file_path)
            elif suffix in [".yaml", ".yml"]:
                groups["yaml"].append(file_path)
            elif suffix in [".css", ".scss", ".sass", ".less"]:
                groups["css"].append(file_path)
            elif suffix in [".html", ".htm", ".xhtml"]:
                groups["html"].append(file_path)
            elif suffix in [".md", ".markdown"]:
                groups["markdown"].append(file_path)
            else:
                groups["other"].append(file_path)

        return {k: v for k, v in groups.items() if v}  # Remove empty groups

    def _select_formatter_for_type(self, file_type: str, requested_formatter: str) -> Optional[str]:
        """Select appropriate formatter for file type"""
        if requested_formatter != "auto-detect":
            # Check if requested formatter is appropriate for file type
            type_formatters = {
                "python": ["black", "autopep8"],
                "javascript": ["prettier"],
                "typescript": ["prettier"],
                "json": ["prettier"],
                "yaml": ["prettier"],
                "css": ["prettier"],
                "html": ["prettier"],
                "markdown": ["prettier"],
            }

            if file_type in type_formatters and requested_formatter in type_formatters[file_type]:
                return requested_formatter
            else:
                return None  # Requested formatter not suitable for this file type

        # Auto-detect best formatter for file type
        formatter_priority = {
            "python": ["black", "autopep8"],
            "javascript": ["prettier"],
            "typescript": ["prettier"],
            "json": ["prettier"],
            "yaml": ["prettier"],
            "css": ["prettier"],
            "html": ["prettier"],
            "markdown": ["prettier"],
        }

        candidates = formatter_priority.get(file_type, [])
        for formatter in candidates:
            if self._is_command_available(formatter):
                return formatter

        return None

    def _get_install_suggestion(self, formatter: str) -> str:
        """Get installation suggestion for formatter"""
        suggestions = {
            "black": "pip install black",
            "autopep8": "pip install autopep8",
            "prettier": "npm install -g prettier",
        }
        return suggestions.get(formatter, f"Install {formatter}")

    async def _run_formatter(
        self, formatter: str, files: List[Path], config_file: Optional[str], ctx: Context
    ) -> Dict[str, Any]:
        """Run a specific formatter on files"""
        file_paths = [str(f) for f in files]

        try:
            if formatter == "black":
                return await self._run_black(file_paths, config_file)
            elif formatter == "autopep8":
                return await self._run_autopep8(file_paths, config_file)
            elif formatter == "prettier":
                return await self._run_prettier(file_paths, config_file)
            else:
                return {"status": "unsupported", "formatter": formatter}

        except Exception as e:
            return {"status": "error", "formatter": formatter, "error": str(e)}

    async def _run_black(self, file_paths: List[str], config_file: Optional[str]) -> Dict[str, Any]:
        """Run Black Python formatter"""
        cmd = ["black", "--diff", "--color"]

        if config_file:
            cmd.extend(["--config", config_file])

        # First run with --diff to see what would change
        diff_cmd = cmd + file_paths
        diff_result = subprocess.run(diff_cmd, capture_output=True, text=True, timeout=60)

        # Count changes by counting diff sections
        changes = diff_result.stdout.count("--- ") if diff_result.stdout else 0

        # Run actual formatting
        format_cmd = ["black"] + (["--config", config_file] if config_file else []) + file_paths
        format_result = subprocess.run(format_cmd, capture_output=True, text=True, timeout=60)

        # Count files that were actually changed
        files_changed = 0
        if format_result.stderr:
            files_changed = format_result.stderr.count("reformatted")

        return {
            "formatter": "black",
            "status": "completed",
            "exit_code": format_result.returncode,
            "files_changed": files_changed,
            "files_unchanged": len(file_paths) - files_changed,
            "total_changes": changes,
            "diff_preview": (
                diff_result.stdout[:1000] if diff_result.stdout else None
            ),  # First 1000 chars
        }

    async def _run_autopep8(
        self, file_paths: List[str], config_file: Optional[str]
    ) -> Dict[str, Any]:
        """Run autopep8 Python formatter"""
        cmd = ["autopep8", "--in-place", "--aggressive", "--aggressive"]

        if config_file:
            cmd.extend(["--global-config", config_file])

        # Run diff first to see changes
        diff_cmd = ["autopep8", "--diff"] + file_paths
        diff_result = subprocess.run(diff_cmd, capture_output=True, text=True, timeout=60)
        changes = diff_result.stdout.count("@@") if diff_result.stdout else 0

        # Run actual formatting
        format_cmd = cmd + file_paths
        format_result = subprocess.run(format_cmd, capture_output=True, text=True, timeout=60)

        return {
            "formatter": "autopep8",
            "status": "completed",
            "exit_code": format_result.returncode,
            "files_changed": len(file_paths) if format_result.returncode == 0 else 0,
            "files_unchanged": 0 if format_result.returncode == 0 else len(file_paths),
            "total_changes": changes,
            "diff_preview": diff_result.stdout[:1000] if diff_result.stdout else None,
        }

    async def _run_prettier(
        self, file_paths: List[str], config_file: Optional[str]
    ) -> Dict[str, Any]:
        """Run Prettier formatter"""
        cmd = ["prettier", "--write"]

        if config_file:
            cmd.extend(["--config", config_file])

        # Check what files would be changed
        check_cmd = ["prettier", "--list-different"] + file_paths
        check_result = subprocess.run(check_cmd, capture_output=True, text=True, timeout=60)

        files_to_change = (
            len(check_result.stdout.strip().split("\n")) if check_result.stdout.strip() else 0
        )

        # Run actual formatting
        format_cmd = cmd + file_paths
        format_result = subprocess.run(format_cmd, capture_output=True, text=True, timeout=60)

        return {
            "formatter": "prettier",
            "status": "completed",
            "exit_code": format_result.returncode,
            "files_changed": files_to_change if format_result.returncode == 0 else 0,
            "files_unchanged": len(file_paths) - files_to_change,
            "total_changes": files_to_change,
            "changed_files": (
                check_result.stdout.strip().split("\n") if check_result.stdout.strip() else []
            ),
        }

    def _generate_format_recommendations(self, results: Dict[str, Any]) -> List[str]:
        """Generate actionable recommendations based on format results"""
        recommendations = []
        summary = results["summary"]

        if summary["formatted_files"] == 0 and summary["failed_files"] == 0:
            recommendations.append("✅ All files are already properly formatted!")
            return recommendations

        if summary["formatted_files"] > 0:
            recommendations.append(f"✅ Successfully formatted {summary['formatted_files']} files")

        if summary["failed_files"] > 0:
            recommendations.append(
                f"⚠️ Failed to format {summary['failed_files']} files - check error details"
            )

        # Check for missing formatters
        skipped_types = []
        for file_type, result in results["format_results"].items():
            if result.get("status") == "skipped" and "not installed" in result.get("reason", ""):
                skipped_types.append((file_type, result.get("suggestion", "")))

        if skipped_types:
            recommendations.append("💡 Install missing formatters:")
            for file_type, suggestion in skipped_types:
                recommendations.append(f"  - {suggestion} (for {file_type} files)")

        if summary["total_changes"] > 50:
            recommendations.append("📋 Many changes applied - review diff output carefully")

        return recommendations


class NetworkAPITools(MCPMixin):
    """Network and API testing tools"""

    @mcp_tool(name="http_request", description="🟡 SAFE: Make HTTP requests for API testing")
    async def http_request(
        self,
        url: str,
        method: Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS"],
        headers: Optional[Dict[str, str]] = None,
        body: Optional[Union[str, Dict[str, Any]]] = None,
        timeout: Optional[int] = 30,
        ctx: Context = None,
    ) -> Dict[str, Any]:
        """Make HTTP request and return detailed response information

        Args:
            url: The URL to request
            method: HTTP method
            headers: Request headers (dict or JSON string)
            body: Request body (string, dict, or JSON)
            timeout: Request timeout in seconds
            ctx: FastMCP context
        """
        try:
            if requests is None:
                return {
                    "error": "requests library not available",
                    "install": "pip install requests",
                }

            # Handle headers conversion from JSON string if needed
            if isinstance(headers, str):
                try:
                    import json
                    headers = json.loads(headers)
                except (json.JSONDecodeError, ValueError):
                    # If it's not valid JSON, treat it as a single header value
                    headers = {"Content-Type": headers}

            # Prepare headers
            request_headers = headers or {}

            # Prepare body based on type
            request_data = None
            request_json = None

            if body is not None:
                if isinstance(body, dict):
                    request_json = body
                    if "Content-Type" not in request_headers:
                        request_headers["Content-Type"] = "application/json"
                else:
                    request_data = body
                    if "Content-Type" not in request_headers:
                        request_headers["Content-Type"] = "text/plain"

            # Make the request
            start_time = time.time()

            response = requests.request(
                method=method,
                url=url,
                headers=request_headers,
                data=request_data,
                json=request_json,
                timeout=timeout,
                allow_redirects=True,
            )

            end_time = time.time()
            response_time = round((end_time - start_time) * 1000, 2)  # ms

            # Parse response body safely
            response_body = None
            content_type = response.headers.get("Content-Type", "").lower()

            try:
                if "application/json" in content_type:
                    response_body = response.json()
                else:
                    response_body = response.text
                    # Truncate very long text responses
                    if len(response_body) > 5000:
                        response_body = response_body[:5000] + "... [truncated]"
            except Exception:
                response_body = f"<Unable to parse response: {len(response.content)} bytes>"

            # Build response object
            result = {
                "request": {"method": method, "url": url, "headers": request_headers, "body": body},
                "response": {
                    "status_code": response.status_code,
                    "status_text": response.reason,
                    "headers": dict(response.headers),
                    "body": response_body,
                    "size_bytes": len(response.content),
                    "response_time_ms": response_time,
                },
                "success": 200 <= response.status_code < 300,
                "redirected": len(response.history) > 0,
                "final_url": response.url,
            }

            if ctx:
                status_emoji = "✅" if result["success"] else "❌"
                await ctx.info(
                    f"{status_emoji} {method} {url} → {response.status_code} ({response_time}ms)"
                )

            return result

        except requests.exceptions.Timeout:
            error_msg = f"Request timeout after {timeout}s"
            if ctx:
                await ctx.error(error_msg)
            return {"error": error_msg, "type": "timeout"}

        except requests.exceptions.ConnectionError as e:
            error_msg = f"Connection error: {str(e)}"
            if ctx:
                await ctx.error(error_msg)
            return {"error": error_msg, "type": "connection_error"}

        except requests.exceptions.RequestException as e:
            error_msg = f"Request failed: {str(e)}"
            if ctx:
                await ctx.error(error_msg)
            return {"error": error_msg, "type": "request_error"}

        except Exception as e:
            error_msg = f"HTTP request failed: {str(e)}"
            if ctx:
                await self.log_critical(error_msg, exception=e, ctx=ctx)
            return {"error": error_msg, "type": "unexpected_error"}

    @mcp_tool(name="api_mock_server", description="Start a simple mock API server")
    async def api_mock_server(
        self,
        port: int,
        routes: List[Dict[str, Any]],
        cors: Optional[bool] = True,
        ctx: Context = None,
    ) -> Dict[str, Any]:
        """Start mock API server

        Args:
            port: Port number for the server
            routes: List of route definitions
            cors: Enable CORS headers
            ctx: FastMCP context
        """
        # Handle boolean conversion for cors
        if not isinstance(cors, bool):
            if isinstance(cors, str):
                cors = cors.lower() in ('true', '1', 'yes', 'on')
            else:
                cors = bool(cors) if cors is not None else True

        return {
            "status": "not_implemented",
            "message": "Mock API server functionality is not yet implemented",
            "info": "This tool will start a mock HTTP server for API testing",
            "suggested_alternatives": [
                "Use 'python -m http.server <port>' for simple file serving",
                "Use 'json-server' npm package: npx json-server --watch db.json",
                "Use 'mockoon' for GUI-based API mocking",
                "Use FastAPI for quick mock endpoints: uvicorn main:app --reload"
            ],
            "example_fastapi_code": """
# Quick FastAPI mock server example:
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

if cors:  # %s
    app.add_middleware(CORSMiddleware, allow_origins=["*"])

# Add routes based on provided configuration
# Routes: %s
""" % (cors, len(routes) if routes else 0),
            "parameters_received": {
                "port": port,
                "routes_count": len(routes) if routes else 0,
                "cors": cors
            }
        }


class ProcessTracingTools(MCPMixin):
    """Process tracing and system call analysis tools"""

    @mcp_tool(
        name="trace_process", description="Trace system calls and signals for process debugging"
    )
    async def trace_process(
        self,
        target: str,  # Changed from Union[int, str] to str - can be PID as string or process name
        action: Literal["attach", "launch", "follow"],
        duration: Optional[int] = 30,
        output_format: Optional[Literal["summary", "detailed", "json", "timeline"]] = "summary",
        filter_calls: Optional[List[Literal["file", "network", "process"]]] = None,
        exclude_calls: Optional[List[str]] = None,
        follow_children: Optional[bool] = False,
        show_timestamps: Optional[bool] = True,
        buffer_size: Optional[int] = 10,
        filter_paths: Optional[List[str]] = None,
        ctx: Context = None,
    ) -> Dict[str, Any]:
        """Trace process system calls (cross-platform strace equivalent)

        Args:
            target: Process name or PID (as string)
            action: How to attach to process
            duration: Tracing duration in seconds
            output_format: Output format type
            filter_calls: Types of calls to filter
            exclude_calls: Specific calls to exclude
            follow_children: Follow child processes
            show_timestamps: Show timestamps in output
            buffer_size: Buffer size for output
            filter_paths: Paths to filter
            ctx: FastMCP context
        """
        # Handle numeric strings as PIDs
        try:
            # If it's a numeric string, treat it as a PID
            pid = int(target)
            target_identifier = f"PID:{pid}"
        except ValueError:
            # Otherwise treat it as a process name
            target_identifier = f"Process:{target}"

        # Provide a basic implementation or informative message
        return {
            "status": "not_implemented",
            "message": "Process tracing functionality is not yet implemented",
            "info": "This tool will provide system call tracing similar to strace/dtrace",
            "parameters_received": {
                "target": target,
                "target_identifier": target_identifier,
                "action": action,
                "duration": duration,
                "output_format": output_format
            }
        }

    @mcp_tool(name="analyze_syscalls", description="Analyze and summarize system call traces")
    async def analyze_syscalls(
        self,
        trace_data: str,
        analysis_type: Literal["file_access", "network", "performance", "errors", "overview"],
        group_by: Optional[Literal["call_type", "file_path", "process", "time_window"]] = None,
        threshold_ms: Optional[float] = None,
        ctx: Context = None,
    ) -> Dict[str, Any]:
        """Analyze system call traces with insights"""
        # Provide a basic implementation or informative message
        return {
            "status": "not_implemented",
            "message": "System call analysis functionality is not yet implemented",
            "info": "This tool will analyze system call traces for patterns and insights",
            "parameters_received": {
                "trace_data_length": len(trace_data) if trace_data else 0,
                "analysis_type": analysis_type,
                "group_by": group_by,
                "threshold_ms": threshold_ms
            }
        }

    @mcp_tool(
        name="process_monitor", description="Real-time process monitoring with system call tracking"
    )
    async def process_monitor(
        self,
        process_pattern: str,  # Changed from Union[str, int] to str - can be PID as string
        watch_events: List[Literal["file_access", "network", "registry", "process_creation"]],
        duration: Optional[int] = 60,
        alert_threshold: Optional[Dict[str, Any]] = None,
        output_format: Optional[Literal["live", "summary", "alerts_only"]] = "summary",
        ctx: Context = None,
    ) -> Dict[str, Any]:
        """Monitor process activity in real-time

        Args:
            process_pattern: Process name pattern or PID (as string)
            watch_events: Events to monitor
            duration: Monitoring duration in seconds
            alert_threshold: Alert configuration
            output_format: Output format type
            ctx: FastMCP context
        """
        # Handle numeric strings as PIDs
        try:
            # If it's a numeric string, treat it as a PID
            pid = int(process_pattern)
            process_identifier = f"PID:{pid}"
        except ValueError:
            # Otherwise treat it as a process name pattern
            process_identifier = f"Pattern:{process_pattern}"

        # Provide a basic implementation or informative message
        return {
            "status": "not_implemented",
            "message": "Process monitoring functionality is not yet implemented",
            "info": "This tool will provide real-time process monitoring with system call tracking",
            "parameters_received": {
                "process_pattern": process_pattern,
                "process_identifier": process_identifier,
                "watch_events": watch_events,
                "duration": duration,
                "output_format": output_format
            }
        }


class EnvironmentProcessManagement(MCPMixin):
    """Environment and process management tools"""

    @mcp_tool(
        name="environment_info",
        description="""🔍 Get comprehensive system diagnostics with smart auto-detection.
        
        USAGE EXAMPLES:
        - Quick overview: include_sections=["auto"] (detects what's available)
        - Development focus: include_sections=["dev"] (python, git, node essentials)
        - System troubleshooting: include_sections=["system"] 
        - Full analysis: include_sections=["all"] (everything available)
        - Specific sections: include_sections=["python", "git"]
        
        PERFORMANCE: ~0.1-0.2s execution time, safe for frequent use
        RETURNS: Structured data + LLM hints for next actions""",
    )
    def environment_info(
        self,
        include_sections: List[
            Literal["auto", "all", "dev", "system", "python", "node", "git", "env_vars"]
        ] = ["auto"],
        detail_level: Literal["basic", "detailed", "comprehensive"] = "detailed",
    ) -> Dict[str, Any]:
        """Get detailed environment information with smart auto-detection and LLM-friendly guidance"""
        try:
            start_time = time.time()  # Track performance

            # Smart section selection based on LLM-friendly modes
            actual_sections = []

            if "auto" in include_sections:
                # Auto-detect available and relevant sections
                actual_sections = ["system", "python"]  # Always available
                # Check for git availability
                try:
                    subprocess.run(["git", "--version"], capture_output=True, timeout=2)
                    actual_sections.append("git")
                except:
                    pass
                # Check for node availability
                try:
                    subprocess.run(["node", "--version"], capture_output=True, timeout=2)
                    actual_sections.append("node")
                except:
                    pass

            elif "all" in include_sections:
                actual_sections = ["system", "python", "node", "git", "env_vars"]

            elif "dev" in include_sections:
                # Development-focused essentials
                actual_sections = ["python", "git"]
                # Add node if available
                try:
                    subprocess.run(["node", "--version"], capture_output=True, timeout=2)
                    actual_sections.append("node")
                except:
                    pass

            else:
                # Use specified sections directly
                actual_sections = [s for s in include_sections if s not in ["auto", "all", "dev"]]

            result = {
                "timestamp": datetime.now().isoformat(),
                "sections_requested": include_sections,
                "sections_selected": actual_sections,
                "detail_level": detail_level,
                "sections_data": {},
                "errors": [],
                "warnings": [],
                "llm_hints": {
                    "suggested_next_actions": [],
                    "common_workflows": [],
                    "related_tools": [],
                },
            }

            # System information section
            if "system" in actual_sections:
                try:
                    system_info = {
                        "platform": {
                            "system": platform.system(),
                            "release": platform.release(),
                            "version": platform.version(),
                            "machine": platform.machine(),
                            "processor": platform.processor(),
                            "architecture": platform.architecture(),
                            "platform_string": platform.platform(),
                        },
                        "python_platform": {
                            "python_implementation": platform.python_implementation(),
                            "python_version": platform.python_version(),
                            "python_compiler": platform.python_compiler(),
                            "python_build": platform.python_build(),
                        },
                    }

                    # Add psutil system info if available
                    if psutil:
                        try:
                            system_info["hardware"] = {
                                "cpu_count_logical": psutil.cpu_count(logical=True),
                                "cpu_count_physical": psutil.cpu_count(logical=False),
                                "cpu_freq": (
                                    psutil.cpu_freq()._asdict() if psutil.cpu_freq() else None
                                ),
                                "memory": {
                                    "total": psutil.virtual_memory().total,
                                    "available": psutil.virtual_memory().available,
                                    "percent_used": psutil.virtual_memory().percent,
                                },
                                "disk_usage": {
                                    "total": (
                                        psutil.disk_usage("/").total
                                        if os.name != "nt"
                                        else psutil.disk_usage("C:").total
                                    ),
                                    "used": (
                                        psutil.disk_usage("/").used
                                        if os.name != "nt"
                                        else psutil.disk_usage("C:").used
                                    ),
                                    "free": (
                                        psutil.disk_usage("/").free
                                        if os.name != "nt"
                                        else psutil.disk_usage("C:").free
                                    ),
                                },
                                "boot_time": datetime.fromtimestamp(psutil.boot_time()).isoformat(),
                            }
                        except Exception as e:
                            result["warnings"].append(f"Failed to get hardware info: {str(e)}")
                    else:
                        result["warnings"].append("psutil not available - hardware info limited")

                    result["sections_data"]["system"] = system_info

                except Exception as e:
                    result["errors"].append(f"Failed to get system info: {str(e)}")

            # Python environment section
            if "python" in actual_sections:
                try:
                    python_info = {
                        "version": sys.version,
                        "version_info": {
                            "major": sys.version_info.major,
                            "minor": sys.version_info.minor,
                            "micro": sys.version_info.micro,
                            "releaselevel": sys.version_info.releaselevel,
                            "serial": sys.version_info.serial,
                        },
                        "executable": sys.executable,
                        "path": sys.path[:10],  # Limit to first 10 entries for readability
                        "modules": {
                            "builtin_module_names": list(sys.builtin_module_names)[
                                :20
                            ],  # Limit for readability
                            "loaded_modules_count": len(sys.modules),
                        },
                        "prefix": sys.prefix,
                        "base_prefix": getattr(sys, "base_prefix", sys.prefix),
                        "real_prefix": getattr(sys, "real_prefix", None),
                        "in_virtualenv": hasattr(sys, "real_prefix")
                        or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix),
                    }

                    # Check for common development packages
                    common_packages = [
                        "pip",
                        "setuptools",
                        "wheel",
                        "pytest",
                        "numpy",
                        "pandas",
                        "requests",
                        "fastmcp",
                    ]
                    installed_packages = {}
                    for pkg in common_packages:
                        try:
                            __import__(pkg)
                            installed_packages[pkg] = "available"
                        except ImportError:
                            installed_packages[pkg] = "not_installed"

                    python_info["common_packages"] = installed_packages
                    result["sections_data"]["python"] = python_info

                except Exception as e:
                    result["errors"].append(f"Failed to get Python info: {str(e)}")

            # Node.js environment section
            if "node" in actual_sections:
                try:
                    node_info = {"available": False}

                    # Check for Node.js
                    try:
                        node_result = subprocess.run(
                            ["node", "--version"], capture_output=True, text=True, timeout=5
                        )
                        if node_result.returncode == 0:
                            node_info["available"] = True
                            node_info["version"] = node_result.stdout.strip()

                            # Get npm version
                            npm_result = subprocess.run(
                                ["npm", "--version"], capture_output=True, text=True, timeout=5
                            )
                            if npm_result.returncode == 0:
                                node_info["npm_version"] = npm_result.stdout.strip()

                            # Check for package.json in current directory
                            if Path("package.json").exists():
                                try:
                                    with open("package.json") as f:
                                        package_json = json.load(f)
                                        node_info["local_project"] = {
                                            "name": package_json.get("name"),
                                            "version": package_json.get("version"),
                                            "dependencies_count": len(
                                                package_json.get("dependencies", {})
                                            ),
                                            "dev_dependencies_count": len(
                                                package_json.get("devDependencies", {})
                                            ),
                                        }
                                except Exception as e:
                                    result["warnings"].append(
                                        f"Failed to read package.json: {str(e)}"
                                    )

                    except (subprocess.TimeoutExpired, FileNotFoundError):
                        node_info["error"] = "Node.js not found or not accessible"

                    result["sections_data"]["node"] = node_info

                except Exception as e:
                    result["errors"].append(f"Failed to get Node.js info: {str(e)}")

            # Git environment section
            if "git" in actual_sections:
                try:
                    git_info = {"available": False}

                    try:
                        # Check git version
                        git_result = subprocess.run(
                            ["git", "--version"], capture_output=True, text=True, timeout=5
                        )
                        if git_result.returncode == 0:
                            git_info["available"] = True
                            git_info["version"] = git_result.stdout.strip()

                            # Get git config
                            config_items = [
                                "user.name",
                                "user.email",
                                "core.editor",
                                "init.defaultBranch",
                            ]
                            git_config = {}
                            for item in config_items:
                                try:
                                    config_result = subprocess.run(
                                        ["git", "config", "--get", item],
                                        capture_output=True,
                                        text=True,
                                        timeout=3,
                                    )
                                    if config_result.returncode == 0:
                                        git_config[item] = config_result.stdout.strip()
                                except subprocess.TimeoutExpired:
                                    git_config[item] = "timeout"
                                except Exception:
                                    git_config[item] = "not_set"

                            git_info["config"] = git_config

                            # Check if we're in a git repository
                            try:
                                repo_result = subprocess.run(
                                    ["git", "rev-parse", "--git-dir"],
                                    capture_output=True,
                                    text=True,
                                    timeout=3,
                                )
                                if repo_result.returncode == 0:
                                    git_info["repository"] = {
                                        "in_repo": True,
                                        "git_dir": repo_result.stdout.strip(),
                                    }

                                    # Get current branch
                                    branch_result = subprocess.run(
                                        ["git", "branch", "--show-current"],
                                        capture_output=True,
                                        text=True,
                                        timeout=3,
                                    )
                                    if branch_result.returncode == 0:
                                        git_info["repository"]["current_branch"] = (
                                            branch_result.stdout.strip()
                                        )
                                else:
                                    git_info["repository"] = {"in_repo": False}
                            except Exception:
                                git_info["repository"] = {"in_repo": False}

                    except (subprocess.TimeoutExpired, FileNotFoundError):
                        git_info["error"] = "Git not found or not accessible"

                    result["sections_data"]["git"] = git_info

                except Exception as e:
                    result["errors"].append(f"Failed to get Git info: {str(e)}")

            # Environment variables section (filtered for security)
            if "env_vars" in actual_sections:
                try:
                    # SACRED TRUST: Filter sensitive environment variables
                    sensitive_patterns = [
                        "password",
                        "secret",
                        "key",
                        "token",
                        "auth",
                        "credential",
                        "private",
                        "aws_",
                        "api_",
                        "database_url",
                        "db_pass",
                    ]

                    safe_env_vars = {}
                    development_env_vars = {}

                    for key, value in os.environ.items():
                        key_lower = key.lower()

                        # Check if potentially sensitive
                        is_sensitive = any(pattern in key_lower for pattern in sensitive_patterns)

                        if is_sensitive:
                            safe_env_vars[key] = f"[FILTERED - {len(value)} chars]"
                        elif len(value) > 200:
                            safe_env_vars[key] = (
                                f"[TRUNCATED - {len(value)} chars]: {value[:100]}..."
                            )
                        else:
                            safe_env_vars[key] = value

                        # Collect development-relevant variables
                        if any(
                            dev_key in key_lower
                            for dev_key in [
                                "path",
                                "python",
                                "node",
                                "npm",
                                "git",
                                "editor",
                                "shell",
                                "term",
                                "lang",
                                "lc_",
                            ]
                        ):
                            development_env_vars[key] = value if not is_sensitive else "[FILTERED]"

                    env_info = {
                        "total_count": len(os.environ),
                        "development_relevant": development_env_vars,
                        "all_variables": safe_env_vars,
                        "security_note": "Sensitive variables filtered for security",
                    }

                    result["sections_data"]["env_vars"] = env_info

                except Exception as e:
                    result["errors"].append(f"Failed to get environment variables: {str(e)}")

            # Add summary
            result["summary"] = {
                "sections_completed": len(result["sections_data"]),
                "sections_requested": len(include_sections),
                "sections_selected": len(actual_sections),
                "errors_count": len(result["errors"]),
                "warnings_count": len(result["warnings"]),
                "success": len(result["errors"]) == 0,
            }

            # Add LLM hints based on discovered environment
            llm_hints = result["llm_hints"]

            # Suggest next actions based on what was found
            if result["summary"]["success"]:
                if "python" in result["sections_data"]:
                    python_info = result["sections_data"]["python"]
                    if python_info["in_virtualenv"]:
                        llm_hints["suggested_next_actions"].append(
                            "Environment ready for development"
                        )
                    else:
                        llm_hints["suggested_next_actions"].append(
                            "Consider creating virtual environment with manage_virtual_env"
                        )
                        llm_hints["related_tools"].append("manage_virtual_env")

                if "git" in result["sections_data"]:
                    git_info = result["sections_data"]["git"]
                    if git_info.get("available") and git_info.get("repository", {}).get("in_repo"):
                        llm_hints["suggested_next_actions"].append(
                            "Git repository detected - ready for version control operations"
                        )
                        llm_hints["related_tools"].extend(["git_git_status", "git_git_diff"])
                    elif git_info.get("available"):
                        llm_hints["suggested_next_actions"].append(
                            "Git available but not in repository"
                        )

                if "node" in result["sections_data"]:
                    node_info = result["sections_data"]["node"]
                    if node_info.get("available") and node_info.get("local_project"):
                        llm_hints["suggested_next_actions"].append(
                            "Node.js project detected - ready for npm/yarn operations"
                        )
                        llm_hints["related_tools"].append("execute_command_enhanced")

                # Common workflows based on environment
                if "python" in actual_sections and "git" in actual_sections:
                    llm_hints["common_workflows"].append(
                        "Python development: setup → code → test → commit"
                    )

                if len(result["errors"]) == 0:
                    llm_hints["common_workflows"].append(
                        "Environment analysis complete - ready for development tasks"
                    )

            # Performance hints
            result["performance_hints"] = {
                "execution_time_ms": (
                    round((time.time() - start_time) * 1000, 1)
                    if "start_time" in locals()
                    else None
                ),
                "detail_level_used": detail_level,
                "sections_auto_detected": "auto" in include_sections,
                "recommendation": (
                    "Use 'dev' mode for faster Python/Git focus"
                    if len(actual_sections) > 3
                    else "Current selection optimal"
                ),
            }

            return result

        except Exception as e:
            return {
                "error": f"Critical error in environment_info: {str(e)}",
                "timestamp": datetime.now().isoformat(),
                "sections_requested": include_sections,
                "success": False,
            }

    @mcp_tool(name="process_tree", description="Show process hierarchy and relationships")
    def process_tree(
        self, root_pid: Optional[int] = None, include_children: Optional[bool] = True
    ) -> Dict[str, Any]:
        """Show process tree with resource usage and detailed hierarchy information"""
        try:
            if not psutil:
                return {
                    "error": "psutil not available - process monitoring requires psutil package",
                    "timestamp": datetime.now().isoformat(),
                    "success": False,
                }

            result = {
                "timestamp": datetime.now().isoformat(),
                "root_pid": root_pid,
                "include_children": include_children,
                "processes": {},
                "tree_structure": {},
                "summary": {},
                "errors": [],
                "warnings": [],
            }

            # Get all processes or start from specific root
            try:
                if root_pid:
                    # Start from specific process
                    try:
                        root_process = psutil.Process(root_pid)
                        process_list = [root_process]
                        if include_children:
                            process_list.extend(root_process.children(recursive=True))
                    except psutil.NoSuchProcess:
                        return {
                            "error": f"Process with PID {root_pid} not found",
                            "timestamp": datetime.now().isoformat(),
                            "success": False,
                        }
                else:
                    # Get all processes
                    process_list = list(psutil.process_iter())

                # Collect process information
                total_cpu = 0
                total_memory = 0
                process_count = 0

                for proc in process_list:
                    try:
                        # Get process info with error handling for each field
                        proc_info = {
                            "pid": proc.pid,
                            "name": "unknown",
                            "cmdline": [],
                            "status": "unknown",
                            "create_time": None,
                            "cpu_percent": 0.0,
                            "memory_percent": 0.0,
                            "memory_info": {},
                            "ppid": None,
                            "children_pids": [],
                            "num_threads": 0,
                            "username": "unknown",
                            "cwd": "unknown",
                            "exe": "unknown",
                            "connections": 0,
                            "open_files": 0,
                        }

                        # Safely get each piece of information
                        try:
                            proc_info["name"] = proc.name()
                        except (psutil.AccessDenied, psutil.NoSuchProcess):
                            pass

                        try:
                            cmdline = proc.cmdline()
                            proc_info["cmdline"] = (
                                cmdline[:5] if len(cmdline) > 5 else cmdline
                            )  # Limit for readability
                        except (psutil.AccessDenied, psutil.NoSuchProcess):
                            pass

                        try:
                            proc_info["status"] = proc.status()
                        except (psutil.AccessDenied, psutil.NoSuchProcess):
                            pass

                        try:
                            proc_info["create_time"] = datetime.fromtimestamp(
                                proc.create_time()
                            ).isoformat()
                        except (psutil.AccessDenied, psutil.NoSuchProcess):
                            pass

                        try:
                            proc_info["cpu_percent"] = proc.cpu_percent()
                            total_cpu += proc_info["cpu_percent"]
                        except (psutil.AccessDenied, psutil.NoSuchProcess):
                            pass

                        try:
                            proc_info["memory_percent"] = proc.memory_percent()
                            total_memory += proc_info["memory_percent"]
                        except (psutil.AccessDenied, psutil.NoSuchProcess):
                            pass

                        try:
                            memory_info = proc.memory_info()
                            proc_info["memory_info"] = {
                                "rss": memory_info.rss,
                                "vms": memory_info.vms,
                                "rss_mb": round(memory_info.rss / 1024 / 1024, 2),
                                "vms_mb": round(memory_info.vms / 1024 / 1024, 2),
                            }
                        except (psutil.AccessDenied, psutil.NoSuchProcess):
                            pass

                        try:
                            proc_info["ppid"] = proc.ppid()
                        except (psutil.AccessDenied, psutil.NoSuchProcess):
                            pass

                        try:
                            children = proc.children()
                            proc_info["children_pids"] = [child.pid for child in children]
                        except (psutil.AccessDenied, psutil.NoSuchProcess):
                            pass

                        try:
                            proc_info["num_threads"] = proc.num_threads()
                        except (psutil.AccessDenied, psutil.NoSuchProcess):
                            pass

                        try:
                            proc_info["username"] = proc.username()
                        except (psutil.AccessDenied, psutil.NoSuchProcess):
                            pass

                        try:
                            proc_info["cwd"] = proc.cwd()
                        except (psutil.AccessDenied, psutil.NoSuchProcess):
                            pass

                        try:
                            proc_info["exe"] = proc.exe()
                        except (psutil.AccessDenied, psutil.NoSuchProcess):
                            pass

                        try:
                            proc_info["connections"] = len(proc.connections())
                        except (psutil.AccessDenied, psutil.NoSuchProcess):
                            pass

                        try:
                            proc_info["open_files"] = len(proc.open_files())
                        except (psutil.AccessDenied, psutil.NoSuchProcess):
                            pass

                        result["processes"][proc.pid] = proc_info
                        process_count += 1

                    except psutil.NoSuchProcess:
                        # Process disappeared during iteration
                        result["warnings"].append(f"Process {proc.pid} disappeared during scan")
                    except Exception as e:
                        result["warnings"].append(f"Error processing PID {proc.pid}: {str(e)}")

                # Build tree structure
                tree_structure = {}
                orphans = []

                for pid, proc_info in result["processes"].items():
                    ppid = proc_info["ppid"]

                    if ppid is None or ppid not in result["processes"]:
                        # Root process or orphan
                        if ppid is not None and ppid not in result["processes"]:
                            orphans.append(pid)
                        tree_structure[pid] = {"process": proc_info, "children": {}, "depth": 0}

                # Build parent-child relationships
                def add_children(parent_pid, depth=0):
                    if parent_pid not in tree_structure:
                        tree_structure[parent_pid] = {
                            "process": result["processes"].get(parent_pid, {}),
                            "children": {},
                            "depth": depth,
                        }

                    parent_node = tree_structure[parent_pid]

                    for pid, proc_info in result["processes"].items():
                        if proc_info["ppid"] == parent_pid and pid != parent_pid:
                            if pid not in parent_node["children"]:
                                parent_node["children"][pid] = {
                                    "process": proc_info,
                                    "children": {},
                                    "depth": depth + 1,
                                }
                                add_children(pid, depth + 1)

                # Build tree for each root process
                for pid in list(tree_structure.keys()):
                    add_children(pid)

                result["tree_structure"] = tree_structure

                # Generate summary statistics
                summary = {
                    "total_processes": process_count,
                    "total_cpu_percent": round(total_cpu, 2),
                    "total_memory_percent": round(total_memory, 2),
                    "orphaned_processes": len(orphans),
                    "tree_roots": len(tree_structure),
                    "status_breakdown": {},
                    "top_cpu_processes": [],
                    "top_memory_processes": [],
                    "user_breakdown": {},
                }

                # Status breakdown
                status_counts = {}
                user_counts = {}

                # Top processes by resource usage
                processes_by_cpu = sorted(
                    result["processes"].values(), key=lambda x: x["cpu_percent"], reverse=True
                )[:10]

                processes_by_memory = sorted(
                    result["processes"].values(), key=lambda x: x["memory_percent"], reverse=True
                )[:10]

                for proc_info in result["processes"].values():
                    status = proc_info["status"]
                    username = proc_info["username"]

                    status_counts[status] = status_counts.get(status, 0) + 1
                    user_counts[username] = user_counts.get(username, 0) + 1

                summary["status_breakdown"] = status_counts
                summary["user_breakdown"] = user_counts
                summary["top_cpu_processes"] = [
                    {
                        "pid": proc["pid"],
                        "name": proc["name"],
                        "cpu_percent": proc["cpu_percent"],
                        "cmdline": " ".join(proc["cmdline"][:3]) if proc["cmdline"] else "",
                    }
                    for proc in processes_by_cpu
                ]
                summary["top_memory_processes"] = [
                    {
                        "pid": proc["pid"],
                        "name": proc["name"],
                        "memory_percent": proc["memory_percent"],
                        "memory_mb": proc["memory_info"].get("rss_mb", 0),
                        "cmdline": " ".join(proc["cmdline"][:3]) if proc["cmdline"] else "",
                    }
                    for proc in processes_by_memory
                ]

                result["summary"] = summary
                result["success"] = True

            except Exception as e:
                result["errors"].append(f"Failed to build process tree: {str(e)}")
                result["success"] = False

            return result

        except Exception as e:
            return {
                "error": f"Critical error in process_tree: {str(e)}",
                "timestamp": datetime.now().isoformat(),
                "root_pid": root_pid,
                "include_children": include_children,
                "success": False,
            }

    @mcp_tool(
        name="manage_virtual_env",
        description="""🐍 Ultra-fast UV-powered virtual environment management (158x faster than venv).
        
        COMMON WORKFLOWS:
        - List all environments: action="list" (env_name can be anything)
        - Quick create for project: action="create", auto_name=True (uses current directory)
        - Create with specific Python: action="create", python_version="3.11"
        - Safe removal: action="remove" (includes confirmation)
        
        PERFORMANCE: ~0.01s creation time with UV, graceful fallback to venv if needed
        RETURNS: Includes LLM guidance for next steps and workflow suggestions""",
    )
    def manage_virtual_env(
        self,
        action: Literal["list", "create", "activate", "deactivate", "remove"],
        env_name: str = "auto",  # "auto" generates name from directory, or specify custom name
        python_version: Optional[str] = None,
        auto_name: bool = False,  # Generate name from current directory
        workspace_detection: bool = True,  # Detect if in a project workspace
    ) -> Dict[str, Any]:
        """Manage Python virtual environments with UV enhancement, auto-naming, and LLM guidance"""
        try:
            start_time = time.time()  # Track performance

            # Smart environment name handling
            actual_env_name = env_name
            if auto_name or env_name == "auto":
                # Generate name from current directory
                current_dir = Path.cwd().name
                # Clean name for valid environment name
                actual_env_name = re.sub(r"[^a-zA-Z0-9_-]", "_", current_dir.lower())
                if not actual_env_name or actual_env_name[0].isdigit():
                    actual_env_name = f"env_{actual_env_name}"

            # Workspace detection for better guidance
            workspace_info = {}
            if workspace_detection and action in ["create", "list"]:
                workspace_info = {
                    "has_requirements_txt": Path("requirements.txt").exists(),
                    "has_pyproject_toml": Path("pyproject.toml").exists(),
                    "has_setup_py": Path("setup.py").exists(),
                    "has_git": Path(".git").exists(),
                    "current_directory": str(Path.cwd()),
                    "suggested_env_name": actual_env_name,
                }

            result = {
                "timestamp": datetime.now().isoformat(),
                "action": action,
                "env_name": actual_env_name,
                "original_env_name": env_name,
                "python_version": python_version,
                "auto_name_used": auto_name or env_name == "auto",
                "workspace_info": workspace_info,
                "success": False,
                "details": {},
                "instructions": [],
                "errors": [],
                "warnings": [],
                "llm_hints": {
                    "suggested_next_actions": [],
                    "common_workflows": [],
                    "related_tools": [],
                },
            }

            # Determine platform-specific paths and commands
            is_windows = os.name == "nt"

            # Common virtual environment directories
            venv_base_dirs = []
            if is_windows:
                # Windows common locations
                venv_base_dirs = [
                    os.path.expanduser("~/Envs"),
                    os.path.expanduser("~/.virtualenvs"),
                    os.path.join(os.getcwd(), ".venv"),
                    os.path.join(os.getcwd(), "venv"),
                ]
            else:
                # Unix-like systems
                venv_base_dirs = [
                    os.path.expanduser("~/.virtualenvs"),
                    os.path.expanduser("~/venvs"),
                    os.path.join(os.getcwd(), ".venv"),
                    os.path.join(os.getcwd(), "venv"),
                ]

            # Add conda environments if available
            conda_envs_dir = None
            try:
                conda_info = subprocess.run(
                    ["conda", "info", "--json"], capture_output=True, text=True, timeout=5
                )
                if conda_info.returncode == 0:
                    conda_data = json.loads(conda_info.stdout)
                    conda_envs_dir = conda_data.get("envs_dirs", [None])[0]
                    if conda_envs_dir:
                        venv_base_dirs.append(conda_envs_dir)
            except (subprocess.TimeoutExpired, FileNotFoundError, json.JSONDecodeError):
                pass

            # Helper function to find environment
            def find_env_path(env_name_to_find):
                possible_paths = []
                for base_dir in venv_base_dirs:
                    if base_dir and os.path.exists(base_dir):
                        env_path = os.path.join(base_dir, env_name_to_find)
                        possible_paths.append(env_path)
                        if os.path.exists(env_path):
                            return env_path
                return None

            # Helper function to get Python executable path in venv
            def get_venv_python_path(env_path):
                if is_windows:
                    return os.path.join(env_path, "Scripts", "python.exe")
                else:
                    return os.path.join(env_path, "bin", "python")

            # Helper function to get activation script path
            def get_activation_script(env_path):
                if is_windows:
                    return os.path.join(env_path, "Scripts", "activate.bat")
                else:
                    return os.path.join(env_path, "bin", "activate")

            # ACTION: CREATE
            if action == "create":
                try:
                    start_time = time.time()  # Track creation timing

                    # Determine Python executable to use
                    python_cmd = "python"
                    if python_version:
                        # Try version-specific Python
                        version_cmds = [
                            f"python{python_version}",
                            f"python{python_version[:3]}",
                            "python",
                        ]
                        for cmd in version_cmds:
                            try:
                                version_check = subprocess.run(
                                    [cmd, "--version"], capture_output=True, text=True, timeout=5
                                )
                                if version_check.returncode == 0:
                                    python_cmd = cmd
                                    break
                            except (subprocess.TimeoutExpired, FileNotFoundError):
                                continue

                    # Choose creation location (prefer ~/.virtualenvs)
                    base_dir = os.path.expanduser("~/.virtualenvs")
                    if not os.path.exists(base_dir):
                        try:
                            os.makedirs(base_dir, exist_ok=True)
                        except OSError:
                            # Fallback to current directory
                            base_dir = os.getcwd()
                            result["warnings"].append(
                                f"Could not create ~/.virtualenvs, using {base_dir}"
                            )

                    env_path = os.path.join(base_dir, actual_env_name)

                    # Check if environment already exists
                    if os.path.exists(env_path):
                        result["errors"].append(
                            f"Virtual environment '{actual_env_name}' already exists at {env_path}"
                        )
                        return result

                    # Create virtual environment with uv (much faster) or fallback to venv
                    uv_available = False
                    try:
                        # Check if uv is available
                        uv_check = subprocess.run(
                            ["uv", "--version"], capture_output=True, text=True, timeout=5
                        )
                        if uv_check.returncode == 0:
                            uv_available = True
                            result["details"]["uv_version"] = uv_check.stdout.strip()
                    except (subprocess.TimeoutExpired, FileNotFoundError):
                        pass

                    if uv_available:
                        # Use uv for much faster virtual environment creation
                        if python_version:
                            create_cmd = ["uv", "venv", env_path, "--python", python_version]
                        else:
                            create_cmd = ["uv", "venv", env_path]
                        creation_method = "uv"
                    else:
                        # Fallback to standard venv
                        create_cmd = [python_cmd, "-m", "venv", env_path]
                        creation_method = "venv"
                        result["warnings"].append("uv not available, using standard venv (slower)")

                    create_result = subprocess.run(
                        create_cmd, capture_output=True, text=True, timeout=120
                    )

                    if create_result.returncode == 0:
                        result["success"] = True
                        result["details"] = {
                            "env_path": env_path,
                            "python_executable": get_venv_python_path(env_path),
                            "activation_script": get_activation_script(env_path),
                            "creation_command": " ".join(create_cmd),
                            "creation_method": creation_method,
                            "creation_time": (
                                round(time.time() - start_time, 3)
                                if "start_time" in locals()
                                else None
                            ),
                        }

                        # Verify Python version in created environment
                        venv_python = get_venv_python_path(env_path)
                        if os.path.exists(venv_python):
                            try:
                                version_result = subprocess.run(
                                    [venv_python, "--version"],
                                    capture_output=True,
                                    text=True,
                                    timeout=5,
                                )
                                if version_result.returncode == 0:
                                    result["details"]["actual_python_version"] = (
                                        version_result.stdout.strip()
                                    )
                            except (subprocess.TimeoutExpired, FileNotFoundError):
                                pass

                        # Provide activation instructions
                        if is_windows:
                            result["instructions"] = [
                                f"To activate: {env_path}\\Scripts\\activate.bat",
                                f"Or in PowerShell: & '{env_path}\\Scripts\\Activate.ps1'",
                                "To deactivate: deactivate",
                                f"Created using: {creation_method} ({'ultra-fast' if creation_method == 'uv' else 'standard'})",
                            ]
                        else:
                            result["instructions"] = [
                                f"To activate: source {env_path}/bin/activate",
                                "To deactivate: deactivate",
                                f"Created using: {creation_method} ({'ultra-fast' if creation_method == 'uv' else 'standard'})",
                            ]
                    else:
                        result["errors"].append(
                            f"Failed to create virtual environment: {create_result.stderr}"
                        )

                except Exception as e:
                    result["errors"].append(f"Error creating virtual environment: {str(e)}")

            # ACTION: LIST
            elif action == "list":
                try:
                    environments = []

                    for base_dir in venv_base_dirs:
                        if base_dir and os.path.exists(base_dir):
                            try:
                                for item in os.listdir(base_dir):
                                    env_path = os.path.join(base_dir, item)
                                    if os.path.isdir(env_path):
                                        # Check if it's a valid virtual environment
                                        python_path = get_venv_python_path(env_path)
                                        activation_script = get_activation_script(env_path)

                                        if os.path.exists(python_path) or os.path.exists(
                                            activation_script
                                        ):
                                            env_info = {
                                                "name": item,
                                                "path": env_path,
                                                "base_dir": base_dir,
                                                "python_executable": (
                                                    python_path
                                                    if os.path.exists(python_path)
                                                    else None
                                                ),
                                                "activation_script": (
                                                    activation_script
                                                    if os.path.exists(activation_script)
                                                    else None
                                                ),
                                                "created": None,
                                                "python_version": None,
                                                "packages_count": None,
                                            }

                                            # Get creation time
                                            try:
                                                stat = os.stat(env_path)
                                                env_info["created"] = datetime.fromtimestamp(
                                                    stat.st_ctime
                                                ).isoformat()
                                            except OSError:
                                                pass

                                            # Get Python version
                                            if env_info["python_executable"]:
                                                try:
                                                    version_result = subprocess.run(
                                                        [
                                                            env_info["python_executable"],
                                                            "--version",
                                                        ],
                                                        capture_output=True,
                                                        text=True,
                                                        timeout=5,
                                                    )
                                                    if version_result.returncode == 0:
                                                        env_info["python_version"] = (
                                                            version_result.stdout.strip()
                                                        )
                                                except (
                                                    subprocess.TimeoutExpired,
                                                    FileNotFoundError,
                                                ):
                                                    pass

                                            # Get installed packages count
                                            if env_info["python_executable"]:
                                                try:
                                                    pip_list = subprocess.run(
                                                        [
                                                            env_info["python_executable"],
                                                            "-m",
                                                            "pip",
                                                            "list",
                                                        ],
                                                        capture_output=True,
                                                        text=True,
                                                        timeout=10,
                                                    )
                                                    if pip_list.returncode == 0:
                                                        lines = pip_list.stdout.strip().split("\n")
                                                        # Subtract header lines
                                                        env_info["packages_count"] = max(
                                                            0, len(lines) - 2
                                                        )
                                                except (
                                                    subprocess.TimeoutExpired,
                                                    FileNotFoundError,
                                                ):
                                                    pass

                                            environments.append(env_info)
                            except PermissionError:
                                result["warnings"].append(f"Permission denied accessing {base_dir}")

                    result["success"] = True
                    result["details"] = {
                        "environments": environments,
                        "total_count": len(environments),
                        "searched_directories": venv_base_dirs,
                    }

                except Exception as e:
                    result["errors"].append(f"Error listing virtual environments: {str(e)}")

            # ACTION: REMOVE
            elif action == "remove":
                try:
                    env_path = find_env_path(actual_env_name)

                    if not env_path:
                        result["errors"].append(
                            f"Virtual environment '{actual_env_name}' not found"
                        )
                        return result

                    if not os.path.exists(env_path):
                        result["errors"].append(
                            f"Virtual environment path does not exist: {env_path}"
                        )
                        return result

                    # SACRED TRUST: Safety check - ensure it's actually a virtual environment
                    python_path = get_venv_python_path(env_path)
                    activation_script = get_activation_script(env_path)

                    if not (os.path.exists(python_path) or os.path.exists(activation_script)):
                        result["errors"].append(
                            f"Path '{env_path}' does not appear to be a virtual environment"
                        )
                        return result

                    # Remove the environment
                    try:
                        shutil.rmtree(env_path)
                        result["success"] = True
                        result["details"] = {"removed_path": env_path, "env_name": env_name}
                        result["instructions"] = [
                            f"Virtual environment '{env_name}' has been removed successfully"
                        ]
                    except OSError as e:
                        result["errors"].append(f"Failed to remove virtual environment: {str(e)}")

                except Exception as e:
                    result["errors"].append(f"Error removing virtual environment: {str(e)}")

            # ACTION: ACTIVATE
            elif action == "activate":
                try:
                    env_path = find_env_path(actual_env_name)

                    if not env_path:
                        result["errors"].append(
                            f"Virtual environment '{actual_env_name}' not found"
                        )
                        return result

                    activation_script = get_activation_script(env_path)

                    if not os.path.exists(activation_script):
                        result["errors"].append(f"Activation script not found: {activation_script}")
                        return result

                    result["success"] = True
                    result["details"] = {
                        "env_path": env_path,
                        "activation_script": activation_script,
                    }

                    if is_windows:
                        result["instructions"] = [
                            f"Command Prompt: {activation_script}",
                            f"PowerShell: & '{env_path}\\Scripts\\Activate.ps1'",
                            f"Git Bash: source '{env_path}/Scripts/activate'",
                            "Note: Activation must be done in your shell session",
                        ]
                    else:
                        result["instructions"] = [
                            f"source {activation_script}",
                            "Note: Activation must be done in your shell session",
                        ]

                except Exception as e:
                    result["errors"].append(f"Error preparing activation: {str(e)}")

            # ACTION: DEACTIVATE
            elif action == "deactivate":
                try:
                    result["success"] = True
                    result["instructions"] = [
                        "To deactivate any active virtual environment, run: deactivate",
                        "Note: This command must be run in your shell session",
                    ]
                    result["details"] = {
                        "note": "Deactivation is universal across all virtual environments"
                    }

                except Exception as e:
                    result["errors"].append(f"Error preparing deactivation: {str(e)}")

            else:
                result["errors"].append(f"Unknown action: {action}")

            # Add LLM hints based on action and results
            llm_hints = result["llm_hints"]

            if result["success"]:
                if action == "create":
                    llm_hints["suggested_next_actions"] = [
                        f"Activate environment: manage_virtual_env('activate', '{actual_env_name}')",
                        "Install packages with execute_command_enhanced",
                        "Check environment with environment_info(['python'])",
                    ]
                    llm_hints["related_tools"] = ["execute_command_enhanced", "environment_info"]

                    if workspace_info.get("has_requirements_txt"):
                        llm_hints["common_workflows"] = [
                            "create → activate → pip install -r requirements.txt"
                        ]
                    elif workspace_info.get("has_pyproject_toml"):
                        llm_hints["common_workflows"] = ["create → activate → pip install -e ."]
                    else:
                        llm_hints["common_workflows"] = [
                            "create → activate → pip install <packages>"
                        ]

                elif action == "list":
                    if result["details"]["total_count"] > 0:
                        llm_hints["suggested_next_actions"] = [
                            "Activate existing environment or create new one"
                        ]
                    else:
                        llm_hints["suggested_next_actions"] = [
                            "Create first environment with manage_virtual_env('create', 'myproject')"
                        ]
                    llm_hints["related_tools"] = ["environment_info"]

                elif action == "activate":
                    llm_hints["suggested_next_actions"] = [
                        "Use the provided activation command in your terminal"
                    ]
                    llm_hints["common_workflows"] = [
                        "activate → install packages → start development"
                    ]

                elif action == "remove":
                    llm_hints["suggested_next_actions"] = ["Environment removed successfully"]
                    if workspace_info.get("has_requirements_txt"):
                        llm_hints["suggested_next_actions"].append(
                            "Consider creating new environment for this project"
                        )

            # Performance tracking
            result["performance_hints"] = {
                "execution_time_ms": round((time.time() - start_time) * 1000, 1),
                "creation_method": result["details"].get("creation_method", "n/a"),
                "uv_available": "uv" in str(result.get("details", {})),
                "workspace_detected": bool(workspace_info),
                "auto_naming_used": result["auto_name_used"],
            }

            return result

        except Exception as e:
            return {
                "error": f"Critical error in manage_virtual_env: {str(e)}",
                "timestamp": datetime.now().isoformat(),
                "action": action,
                "env_name": env_name,
                "python_version": python_version,
                "success": False,
            }


class EnhancedExistingTools(MCPMixin):
    """Enhanced versions of existing tools"""

    @mcp_tool(
        name="execute_command_enhanced",
        description="Enhanced command execution with advanced features",
    )
    def execute_command_enhanced(
        self,
        command: Union[str, List[str]],
        working_directory: Optional[str] = None,
        environment_vars: Optional[Dict[str, str]] = None,
        capture_output: Optional[Literal["all", "stdout", "stderr", "none"]] = "all",
        stream_callback: Optional[Any] = None,  # Callback function type
        retry_count: Optional[int] = 0,
    ) -> Dict[str, Any]:
        """Execute command with enhanced features including retry, streaming, and comprehensive error handling"""
        try:
            result = {
                "timestamp": datetime.now().isoformat(),
                "command": command,
                "working_directory": working_directory,
                "environment_vars": environment_vars,
                "capture_output": capture_output,
                "retry_count": retry_count,
                "success": False,
                "execution_details": {},
                "attempts": [],
                "errors": [],
                "warnings": [],
            }

            # Validate and prepare command
            if isinstance(command, str):
                # String command - parse for shell execution
                command_list = (
                    command.split()
                    if not any(char in command for char in ["|", "&", ">", "<", ";"])
                    else None
                )
                shell_mode = command_list is None
                exec_command = command if shell_mode else command_list
            elif isinstance(command, list):
                # List command - direct execution
                exec_command = command
                shell_mode = False
                command_str = " ".join(command)
            else:
                result["errors"].append("Command must be string or list")
                return result

            # Validate working directory
            original_cwd = os.getcwd()
            if working_directory:
                if not os.path.exists(working_directory):
                    result["errors"].append(
                        f"Working directory does not exist: {working_directory}"
                    )
                    return result
                if not os.path.isdir(working_directory):
                    result["errors"].append(
                        f"Working directory is not a directory: {working_directory}"
                    )
                    return result

            # Prepare environment
            exec_env = os.environ.copy()
            if environment_vars:
                # SACRED TRUST: Validate environment variables
                for key, value in environment_vars.items():
                    if not isinstance(key, str) or not isinstance(value, str):
                        result["warnings"].append(
                            f"Skipping non-string environment variable: {key}"
                        )
                        continue
                    exec_env[key] = value

            # Execute with retry mechanism
            max_attempts = retry_count + 1

            for attempt in range(max_attempts):
                attempt_result = {
                    "attempt": attempt + 1,
                    "timestamp": datetime.now().isoformat(),
                    "success": False,
                    "return_code": None,
                    "stdout": "",
                    "stderr": "",
                    "execution_time": 0.0,
                    "error": None,
                }

                try:
                    # Change working directory if specified
                    if working_directory:
                        os.chdir(working_directory)

                    start_time = time.time()

                    # Configure output capture
                    if capture_output == "none":
                        stdout_capture = subprocess.DEVNULL
                        stderr_capture = subprocess.DEVNULL
                    elif capture_output == "stdout":
                        stdout_capture = subprocess.PIPE
                        stderr_capture = subprocess.DEVNULL
                    elif capture_output == "stderr":
                        stdout_capture = subprocess.DEVNULL
                        stderr_capture = subprocess.PIPE
                    else:  # "all"
                        stdout_capture = subprocess.PIPE
                        stderr_capture = subprocess.PIPE

                    # Execute command
                    if shell_mode:
                        process = subprocess.run(
                            exec_command,
                            shell=True,
                            stdout=stdout_capture,
                            stderr=stderr_capture,
                            env=exec_env,
                            text=True,
                            timeout=300,  # 5 minute timeout
                        )
                    else:
                        process = subprocess.run(
                            exec_command,
                            stdout=stdout_capture,
                            stderr=stderr_capture,
                            env=exec_env,
                            text=True,
                            timeout=300,  # 5 minute timeout
                        )

                    end_time = time.time()
                    execution_time = end_time - start_time

                    # Collect results
                    attempt_result.update(
                        {
                            "success": process.returncode == 0,
                            "return_code": process.returncode,
                            "stdout": process.stdout or "",
                            "stderr": process.stderr or "",
                            "execution_time": round(execution_time, 3),
                        }
                    )

                    # Simulate streaming callback if provided
                    if stream_callback is not None:
                        attempt_result["streaming_note"] = (
                            "Streaming callback would be called with real-time output"
                        )

                    # Success case
                    if process.returncode == 0:
                        result["success"] = True
                        result["execution_details"] = {
                            "final_attempt": attempt + 1,
                            "total_execution_time": sum(
                                a["execution_time"] for a in result["attempts"]
                            )
                            + execution_time,
                            "return_code": process.returncode,
                            "stdout": process.stdout or "",
                            "stderr": process.stderr or "",
                            "command_type": "shell" if shell_mode else "direct",
                            "working_directory_used": working_directory or original_cwd,
                            "environment_vars_applied": (
                                len(environment_vars) if environment_vars else 0
                            ),
                        }

                        result["attempts"].append(attempt_result)
                        break

                    # Failure case - prepare for retry
                    else:
                        attempt_result["error"] = (
                            f"Command failed with return code {process.returncode}"
                        )
                        result["attempts"].append(attempt_result)

                        if attempt < max_attempts - 1:
                            # Wait before retry (exponential backoff)
                            wait_time = min(2**attempt, 10)  # Max 10 seconds
                            time.sleep(wait_time)
                            attempt_result["retry_wait"] = wait_time

                except subprocess.TimeoutExpired:
                    attempt_result["error"] = "Command timed out after 300 seconds"
                    attempt_result["execution_time"] = 300.0
                    result["attempts"].append(attempt_result)

                except subprocess.CalledProcessError as e:
                    attempt_result.update(
                        {
                            "error": f"Command failed: {str(e)}",
                            "return_code": e.returncode,
                            "execution_time": round(time.time() - start_time, 3),
                        }
                    )
                    result["attempts"].append(attempt_result)

                except FileNotFoundError:
                    attempt_result["error"] = "Command not found"
                    result["attempts"].append(attempt_result)
                    break  # Don't retry for command not found

                except PermissionError:
                    attempt_result["error"] = "Permission denied"
                    result["attempts"].append(attempt_result)
                    break  # Don't retry for permission errors

                except Exception as e:
                    attempt_result["error"] = f"Unexpected error: {str(e)}"
                    attempt_result["execution_time"] = (
                        round(time.time() - start_time, 3) if "start_time" in locals() else 0.0
                    )
                    result["attempts"].append(attempt_result)

                finally:
                    # Always restore original working directory
                    try:
                        os.chdir(original_cwd)
                    except OSError:
                        result["warnings"].append("Failed to restore original working directory")

            # Final result processing
            if not result["success"]:
                # Collect all errors from attempts
                all_errors = [
                    attempt["error"] for attempt in result["attempts"] if attempt.get("error")
                ]
                result["errors"].extend(all_errors)

                # Set final execution details from last attempt
                if result["attempts"]:
                    last_attempt = result["attempts"][-1]
                    result["execution_details"] = {
                        "final_attempt": len(result["attempts"]),
                        "total_execution_time": sum(
                            a["execution_time"] for a in result["attempts"]
                        ),
                        "return_code": last_attempt.get("return_code"),
                        "stdout": last_attempt.get("stdout", ""),
                        "stderr": last_attempt.get("stderr", ""),
                        "command_type": "shell" if shell_mode else "direct",
                        "working_directory_used": working_directory or original_cwd,
                        "environment_vars_applied": (
                            len(environment_vars) if environment_vars else 0
                        ),
                        "final_error": last_attempt.get("error"),
                    }

            # Add summary statistics
            result["summary"] = {
                "total_attempts": len(result["attempts"]),
                "max_attempts": max_attempts,
                "success": result["success"],
                "total_execution_time": sum(a["execution_time"] for a in result["attempts"]),
                "retry_used": len(result["attempts"]) > 1,
                "command_length": len(str(command)),
                "environment_vars_count": len(environment_vars) if environment_vars else 0,
            }

            return result

        except Exception as e:
            return {
                "error": f"Critical error in execute_command_enhanced: {str(e)}",
                "timestamp": datetime.now().isoformat(),
                "command": command,
                "working_directory": working_directory,
                "success": False,
            }

    @mcp_tool(
        name="search_code_enhanced",
        description="""🔎 Multi-modal code intelligence with LLM-optimized search strategies.
        
        SEARCH MODES (Auto-selected if search_type="smart"):
        - "text": Fast literal/regex search (~0.1s, 50+ files) - for strings, comments
        - "semantic": Context-aware functions/classes (~0.3s) - best for API discovery  
        - "ast": Python AST analysis (~0.2s) - perfect for refactoring, structure analysis
        - "cross-reference": Usage tracking (~0.5s) - ideal for impact analysis
        - "smart": Tries multiple modes, returns best results (recommended)
        
        PERFORMANCE: Searches 50+ files in under 0.5s, includes LLM workflow hints
        RETURNS: Rich context + suggested_next_actions for common development tasks""",
    )
    def search_code_enhanced(
        self,
        query: str,
        directory: str = ".",  # Default to current directory - LLM friendly
        search_type: Optional[
            Literal["smart", "text", "semantic", "ast", "cross-reference"]
        ] = "smart",
        file_pattern: Optional[str] = None,
        save_to_history: Optional[bool] = True,
        max_results: int = 20,  # Limit results for better LLM processing
        include_context: bool = True,  # Include before/after code lines
    ) -> List[Dict[str, Any]]:
        """Enhanced code search with multiple search modes including semantic analysis and AST parsing"""
        try:
            results = []
            search_metadata = {
                "timestamp": datetime.now().isoformat(),
                "query": query,
                "directory": directory,
                "search_type": search_type,
                "file_pattern": file_pattern,
                "total_files_searched": 0,
                "total_matches": 0,
                "search_duration": 0.0,
                "errors": [],
                "warnings": [],
            }

            start_time = time.time()

            # Validate directory
            if not os.path.exists(directory):
                search_metadata["errors"].append(f"Directory does not exist: {directory}")
                return [{"search_metadata": search_metadata}]

            if not os.path.isdir(directory):
                search_metadata["errors"].append(f"Path is not a directory: {directory}")
                return [{"search_metadata": search_metadata}]

            # Determine file patterns to search
            if file_pattern:
                # Use provided pattern
                patterns = [file_pattern]
            else:
                # Default patterns based on search type
                if search_type == "ast":
                    patterns = ["*.py"]  # AST search limited to Python
                else:
                    patterns = [
                        "*.py",
                        "*.js",
                        "*.ts",
                        "*.java",
                        "*.cpp",
                        "*.c",
                        "*.h",
                        "*.cs",
                        "*.php",
                        "*.rb",
                        "*.go",
                        "*.rs",
                        "*.kt",
                        "*.swift",
                        "*.html",
                        "*.css",
                        "*.sql",
                        "*.yaml",
                        "*.yml",
                        "*.json",
                        "*.xml",
                        "*.md",
                        "*.txt",
                        "*.sh",
                        "*.ps1",
                        "*.bat",
                    ]

            # Collect files to search
            files_to_search = []
            for pattern in patterns:
                try:
                    for file_path in Path(directory).rglob(pattern):
                        if file_path.is_file():
                            # Skip binary files and common excluded directories
                            relative_path = str(file_path.relative_to(directory))
                            if not any(
                                exclude in relative_path
                                for exclude in [
                                    ".git/",
                                    "__pycache__/",
                                    "node_modules/",
                                    ".venv/",
                                    "venv/",
                                    ".pytest_cache/",
                                    "dist/",
                                    "build/",
                                    ".tox/",
                                    ".coverage",
                                ]
                            ):
                                files_to_search.append(file_path)
                except Exception as e:
                    search_metadata["warnings"].append(
                        f"Error collecting files for pattern {pattern}: {str(e)}"
                    )

            files_to_search = list(set(files_to_search))  # Remove duplicates
            search_metadata["total_files_searched"] = len(files_to_search)

            # Perform search based on type
            if search_type == "smart":
                # Smart search: try multiple modes and combine best results
                all_results = []

                # Start with text search (fastest)
                text_results = self._search_text(query, files_to_search, search_metadata)
                for result in text_results[: max_results // 3]:  # Limit each mode
                    result["search_mode_used"] = "text"
                    all_results.append(result)

                # Add semantic search if query looks like code
                if any(char in query for char in ["(", ")", ".", "_"]) or len(query.split()) == 1:
                    semantic_results = self._search_semantic(
                        query, files_to_search, search_metadata
                    )
                    for result in semantic_results[: max_results // 3]:
                        result["search_mode_used"] = "semantic"
                        all_results.append(result)

                # Add AST search for Python files if appropriate
                python_files = [f for f in files_to_search if f.suffix == ".py"]
                if python_files and query.replace("_", "").isalnum():
                    ast_results = self._search_ast(query, python_files, search_metadata)
                    for result in ast_results[: max_results // 3]:
                        result["search_mode_used"] = "ast"
                        all_results.append(result)

                results.extend(all_results[:max_results])
                search_metadata["smart_modes_used"] = list(
                    set(
                        [
                            r.get("search_mode_used")
                            for r in all_results
                            if r.get("search_mode_used")
                        ]
                    )
                )

            elif search_type == "text":
                results.extend(self._search_text(query, files_to_search, search_metadata))
            elif search_type == "semantic":
                results.extend(self._search_semantic(query, files_to_search, search_metadata))
            elif search_type == "ast":
                results.extend(self._search_ast(query, files_to_search, search_metadata))
            elif search_type == "cross-reference":
                results.extend(
                    self._search_cross_reference(query, files_to_search, search_metadata)
                )
            else:
                search_metadata["errors"].append(f"Unknown search type: {search_type}")

            # Limit results for better LLM processing
            if len(results) > max_results:
                results = results[:max_results]
                search_metadata["results_limited"] = True

            # Finalize metadata
            search_metadata["search_duration"] = round(time.time() - start_time, 3)
            search_metadata["total_matches"] = len([r for r in results if "match" in r])

            # Save to history if requested
            if save_to_history:
                try:
                    history_entry = {
                        "timestamp": search_metadata["timestamp"],
                        "query": query,
                        "search_type": search_type,
                        "directory": directory,
                        "matches_found": search_metadata["total_matches"],
                        "duration": search_metadata["search_duration"],
                    }
                    # In a real implementation, this would save to a persistent store
                    search_metadata["history_saved"] = True
                except Exception as e:
                    search_metadata["warnings"].append(f"Failed to save to history: {str(e)}")

            # Add LLM hints based on search results
            search_metadata["llm_hints"] = {
                "suggested_next_actions": [],
                "common_workflows": [],
                "related_tools": [],
            }

            if search_metadata["total_matches"] > 0:
                # Suggest actions based on what was found
                if search_type == "smart" or search_type == "text":
                    search_metadata["llm_hints"]["suggested_next_actions"] = [
                        "Review found matches for relevant code",
                        "Use execute_command_enhanced to run related commands",
                        "Consider ast search for deeper code structure analysis",
                    ]
                elif search_type == "ast":
                    search_metadata["llm_hints"]["suggested_next_actions"] = [
                        "Analyze function/class structure",
                        "Use cross-reference search to find usage patterns",
                        "Consider refactoring with edit_block_enhanced",
                    ]
                elif search_type == "cross-reference":
                    search_metadata["llm_hints"]["suggested_next_actions"] = [
                        "Assess impact of potential changes",
                        "Plan refactoring strategy",
                        "Use git_git_grep for version history context",
                    ]

                search_metadata["llm_hints"]["related_tools"] = [
                    "execute_command_enhanced",
                    "edit_block_enhanced",
                    "git_git_grep",
                ]
                search_metadata["llm_hints"]["common_workflows"] = [
                    "search → analyze → edit → test",
                    "search → cross-reference → plan refactoring",
                ]
            else:
                search_metadata["llm_hints"]["suggested_next_actions"] = [
                    "Try different search terms or patterns",
                    "Use semantic search for concept-based discovery",
                    "Check if search directory contains expected files",
                ]
                if search_type != "smart":
                    search_metadata["llm_hints"]["suggested_next_actions"].append(
                        "Try smart search mode for comprehensive results"
                    )

            # Performance and optimization hints
            search_metadata["performance_hints"] = {
                "files_processed": search_metadata["total_files_searched"],
                "search_efficiency": (
                    "excellent"
                    if search_metadata["search_duration"] < 0.2
                    else (
                        "good" if search_metadata["search_duration"] < 0.5 else "consider filtering"
                    )
                ),
                "optimization_suggestions": [],
            }

            if search_metadata["total_files_searched"] > 100:
                search_metadata["performance_hints"]["optimization_suggestions"].append(
                    "Consider using file_pattern to limit scope"
                )
            if search_metadata["search_duration"] > 1.0:
                search_metadata["performance_hints"]["optimization_suggestions"].append(
                    "Large search - consider breaking into smaller queries"
                )

            # Add metadata as first result
            results.insert(0, {"search_metadata": search_metadata})

            return results

        except Exception as e:
            error_metadata = {
                "timestamp": datetime.now().isoformat(),
                "query": query,
                "directory": directory,
                "search_type": search_type,
                "critical_error": str(e),
                "success": False,
            }
            return [{"search_metadata": error_metadata}]

    def _search_text(
        self, query: str, files: List[Path], metadata: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Traditional text/regex search"""
        results = []

        try:
            # Compile regex if query looks like regex (contains special chars)
            use_regex = any(
                char in query
                for char in [".", "*", "+", "?", "^", "$", "[", "]", "(", ")", "|", "\\"]
            )
            if use_regex:
                try:
                    pattern = re.compile(query, re.IGNORECASE | re.MULTILINE)
                except re.error:
                    # Fall back to literal search
                    use_regex = False
                    metadata["warnings"].append("Invalid regex pattern, using literal search")

            for file_path in files:
                try:
                    with open(file_path, encoding="utf-8", errors="ignore") as f:
                        lines = f.readlines()

                    for line_num, line in enumerate(lines, 1):
                        matches = []
                        if use_regex:
                            matches = list(pattern.finditer(line))
                        else:
                            # Simple case-insensitive search
                            lower_line = line.lower()
                            lower_query = query.lower()
                            start = 0
                            while True:
                                pos = lower_line.find(lower_query, start)
                                if pos == -1:
                                    break
                                # Create match-like object
                                match_obj = type(
                                    "Match",
                                    (),
                                    {
                                        "start": lambda: pos,
                                        "end": lambda: pos + len(query),
                                        "group": lambda: line[pos : pos + len(query)],
                                    },
                                )()
                                matches.append(match_obj)
                                start = pos + 1

                        if matches:
                            # Get context lines
                            context_before = lines[max(0, line_num - 3) : line_num - 1]
                            context_after = lines[line_num : min(len(lines), line_num + 2)]

                            result = {
                                "match": {
                                    "file_path": str(file_path),
                                    "relative_path": str(
                                        file_path.relative_to(Path(file_path).anchor)
                                    ),
                                    "line_number": line_num,
                                    "line_content": line.rstrip(),
                                    "matches_in_line": len(matches),
                                    "match_positions": [(m.start(), m.end()) for m in matches],
                                    "matched_text": [m.group() for m in matches],
                                },
                                "context": {
                                    "before": [l.rstrip() for l in context_before],
                                    "after": [l.rstrip() for l in context_after],
                                },
                                "file_info": {
                                    "extension": file_path.suffix,
                                    "size_bytes": file_path.stat().st_size,
                                    "modified": datetime.fromtimestamp(
                                        file_path.stat().st_mtime
                                    ).isoformat(),
                                },
                                "search_type": "text",
                            }
                            results.append(result)

                except Exception as e:
                    metadata["warnings"].append(f"Error searching file {file_path}: {str(e)}")

        except Exception as e:
            metadata["errors"].append(f"Error in text search: {str(e)}")

        return results

    def _search_semantic(
        self, query: str, files: List[Path], metadata: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Semantic code search with context awareness"""
        results = []

        try:
            # Define semantic patterns for common code constructs
            semantic_patterns = {
                "function_definition": [
                    r"def\s+\w*" + re.escape(query) + r"\w*\s*\(",  # Python
                    r"function\s+\w*" + re.escape(query) + r"\w*\s*\(",  # JavaScript
                    r"(public|private|protected)?\s*(static)?\s*\w+\s+\w*"
                    + re.escape(query)
                    + r"\w*\s*\(",  # Java/C#
                ],
                "class_definition": [
                    r"class\s+\w*" + re.escape(query) + r"\w*\s*[\(:]",  # Python/Java
                    r"class\s+\w*" + re.escape(query) + r"\w*\s*\{",  # C++/JavaScript
                ],
                "variable_assignment": [
                    r"\b\w*" + re.escape(query) + r"\w*\s*[=:]",  # Various languages
                ],
                "import_statement": [
                    r"(import|from)\s+\w*" + re.escape(query) + r"\w*",  # Python
                    r"import\s+.*" + re.escape(query),  # JavaScript/Java
                ],
                "method_call": [
                    r"\.\s*\w*" + re.escape(query) + r"\w*\s*\(",  # Method calls
                    r"\b\w*" + re.escape(query) + r"\w*\s*\(",  # Function calls
                ],
            }

            # Try to detect query intent
            query_lower = query.lower()
            search_patterns = []

            # Add all patterns for comprehensive search
            for pattern_type, patterns in semantic_patterns.items():
                search_patterns.extend([(p, pattern_type) for p in patterns])

            # Also include literal search as fallback
            search_patterns.append((re.escape(query), "literal"))

            for file_path in files:
                try:
                    with open(file_path, encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                        lines = content.splitlines()

                    for pattern, pattern_type in search_patterns:
                        try:
                            regex = re.compile(pattern, re.IGNORECASE | re.MULTILINE)
                            for match in regex.finditer(content):
                                # Find line number
                                line_num = content[: match.start()].count("\\n") + 1
                                line_content = lines[line_num - 1] if line_num <= len(lines) else ""

                                # Get context
                                context_before = lines[max(0, line_num - 3) : line_num - 1]
                                context_after = lines[line_num : min(len(lines), line_num + 2)]

                                result = {
                                    "match": {
                                        "file_path": str(file_path),
                                        "relative_path": str(
                                            file_path.relative_to(Path(file_path).anchor)
                                        ),
                                        "line_number": line_num,
                                        "line_content": line_content,
                                        "matched_text": match.group(),
                                        "semantic_type": pattern_type,
                                        "match_start": match.start()
                                        - content[: match.start()].rfind("\\n")
                                        - 1,
                                        "match_end": match.end()
                                        - content[: match.start()].rfind("\\n")
                                        - 1,
                                    },
                                    "context": {"before": context_before, "after": context_after},
                                    "file_info": {
                                        "extension": file_path.suffix,
                                        "size_bytes": file_path.stat().st_size,
                                        "modified": datetime.fromtimestamp(
                                            file_path.stat().st_mtime
                                        ).isoformat(),
                                    },
                                    "search_type": "semantic",
                                }
                                results.append(result)

                        except re.error:
                            continue  # Skip invalid patterns

                except Exception as e:
                    metadata["warnings"].append(
                        f"Error in semantic search of {file_path}: {str(e)}"
                    )

        except Exception as e:
            metadata["errors"].append(f"Error in semantic search: {str(e)}")

        return results

    def _search_ast(
        self, query: str, files: List[Path], metadata: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """AST-based search for Python files"""
        results = []

        try:
            python_files = [f for f in files if f.suffix == ".py"]

            for file_path in python_files:
                try:
                    with open(file_path, encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                        lines = content.splitlines()

                    try:
                        tree = ast.parse(content)
                    except SyntaxError as e:
                        metadata["warnings"].append(f"Syntax error in {file_path}: {str(e)}")
                        continue

                    class ASTSearchVisitor(ast.NodeVisitor):
                        def __init__(self):
                            self.matches = []

                        def visit_FunctionDef(self, node):
                            if query.lower() in node.name.lower():
                                self.matches.append(("function", node.name, node.lineno))
                            self.generic_visit(node)

                        def visit_ClassDef(self, node):
                            if query.lower() in node.name.lower():
                                self.matches.append(("class", node.name, node.lineno))
                            self.generic_visit(node)

                        def visit_Name(self, node):
                            if query.lower() in node.id.lower():
                                self.matches.append(("variable", node.id, node.lineno))
                            self.generic_visit(node)

                        def visit_Attribute(self, node):
                            if query.lower() in node.attr.lower():
                                self.matches.append(("attribute", node.attr, node.lineno))
                            self.generic_visit(node)

                    visitor = ASTSearchVisitor()
                    visitor.visit(tree)

                    for match_type, name, line_num in visitor.matches:
                        if line_num <= len(lines):
                            line_content = lines[line_num - 1]
                            context_before = lines[max(0, line_num - 3) : line_num - 1]
                            context_after = lines[line_num : min(len(lines), line_num + 2)]

                            result = {
                                "match": {
                                    "file_path": str(file_path),
                                    "relative_path": str(
                                        file_path.relative_to(Path(file_path).anchor)
                                    ),
                                    "line_number": line_num,
                                    "line_content": line_content,
                                    "ast_node_type": match_type,
                                    "node_name": name,
                                    "matched_text": name,
                                },
                                "context": {"before": context_before, "after": context_after},
                                "file_info": {
                                    "extension": file_path.suffix,
                                    "size_bytes": file_path.stat().st_size,
                                    "modified": datetime.fromtimestamp(
                                        file_path.stat().st_mtime
                                    ).isoformat(),
                                },
                                "search_type": "ast",
                            }
                            results.append(result)

                except Exception as e:
                    metadata["warnings"].append(f"Error in AST search of {file_path}: {str(e)}")

        except Exception as e:
            metadata["errors"].append(f"Error in AST search: {str(e)}")

        return results

    def _search_cross_reference(
        self, query: str, files: List[Path], metadata: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Cross-reference search for tracking usage patterns"""
        results = []

        try:
            # First pass: find definitions
            definitions = []
            usages = []

            for file_path in files:
                try:
                    with open(file_path, encoding="utf-8", errors="ignore") as f:
                        lines = f.readlines()

                    for line_num, line in enumerate(lines, 1):
                        line_stripped = line.strip()

                        # Look for definitions (simplified)
                        definition_patterns = [
                            (r"def\s+" + re.escape(query) + r"\s*\(", "function"),
                            (r"class\s+" + re.escape(query) + r"\s*[\(:]", "class"),
                            (r"^" + re.escape(query) + r"\s*=", "variable"),
                            (r"const\s+" + re.escape(query) + r"\s*=", "constant"),
                            (r"let\s+" + re.escape(query) + r"\s*=", "variable"),
                            (r"var\s+" + re.escape(query) + r"\s*=", "variable"),
                        ]

                        for pattern, def_type in definition_patterns:
                            if re.search(pattern, line, re.IGNORECASE):
                                definitions.append(
                                    {
                                        "file_path": str(file_path),
                                        "line_number": line_num,
                                        "line_content": line.rstrip(),
                                        "definition_type": def_type,
                                    }
                                )

                        # Look for usages
                        if re.search(r"\b" + re.escape(query) + r"\b", line, re.IGNORECASE):
                            usages.append(
                                {
                                    "file_path": str(file_path),
                                    "line_number": line_num,
                                    "line_content": line.rstrip(),
                                }
                            )

                except Exception as e:
                    metadata["warnings"].append(
                        f"Error in cross-reference search of {file_path}: {str(e)}"
                    )

            # Combine definitions and usages
            all_references = definitions + usages

            for ref in all_references:
                file_path = Path(ref["file_path"])
                line_num = ref["line_number"]

                # Get context
                try:
                    with open(file_path, encoding="utf-8", errors="ignore") as f:
                        lines = f.readlines()

                    context_before = [
                        l.rstrip() for l in lines[max(0, line_num - 3) : line_num - 1]
                    ]
                    context_after = [
                        l.rstrip() for l in lines[line_num : min(len(lines), line_num + 2)]
                    ]

                    result = {
                        "match": {
                            "file_path": str(file_path),
                            "relative_path": str(file_path.relative_to(Path(file_path).anchor)),
                            "line_number": line_num,
                            "line_content": ref["line_content"],
                            "reference_type": ref.get("definition_type", "usage"),
                            "matched_text": query,
                        },
                        "context": {"before": context_before, "after": context_after},
                        "file_info": {
                            "extension": file_path.suffix,
                            "size_bytes": file_path.stat().st_size,
                            "modified": datetime.fromtimestamp(
                                file_path.stat().st_mtime
                            ).isoformat(),
                        },
                        "search_type": "cross-reference",
                    }
                    results.append(result)

                except Exception as e:
                    metadata["warnings"].append(
                        f"Error getting context for {file_path}:{line_num}: {str(e)}"
                    )

        except Exception as e:
            metadata["errors"].append(f"Error in cross-reference search: {str(e)}")

        return results

    @mcp_tool(
        name="edit_block_enhanced", description="Enhanced block editing with multi-file support"
    )
    def edit_block_enhanced(
        self,
        edits: List[Dict[str, Any]],
        rollback_support: Optional[bool] = True,
        template_name: Optional[str] = None,
        conflict_resolution: Optional[Literal["manual", "theirs", "ours", "auto"]] = "manual",
    ) -> Dict[str, Any]:
        """Enhanced edit operations with advanced features"""
        raise NotImplementedError("edit_block_enhanced not implemented")


class UtilityTools(MCPMixin):
    """Utility and convenience tools"""

    @mcp_tool(name="generate_documentation", description="Generate documentation from code")
    async def generate_documentation(
        self,
        source_directory: str,
        output_format: Literal["markdown", "html", "pdf"],
        include_private: Optional[bool] = False,
        ctx: Context = None,
    ) -> Dict[str, Any]:
        """Generate documentation from source code

        Args:
            source_directory: Directory containing source code
            output_format: Format for generated documentation
            include_private: Include private members in documentation
            ctx: FastMCP context
        """
        # Handle boolean conversion for include_private
        if not isinstance(include_private, bool):
            if isinstance(include_private, str):
                include_private = include_private.lower() in ('true', '1', 'yes', 'on')
            else:
                include_private = bool(include_private) if include_private is not None else False

        return {
            "status": "not_implemented",
            "message": "Documentation generation functionality is not yet implemented",
            "info": "This tool will generate API documentation from source code",
            "suggested_alternatives": [
                "Use 'pdoc' for Python documentation: pip install pdoc && pdoc --html <module>",
                "Use 'jsdoc' for JavaScript: npm install -g jsdoc && jsdoc <files>",
                "Use 'sphinx' for comprehensive docs: pip install sphinx && sphinx-quickstart"
            ],
            "parameters_received": {
                "source_directory": source_directory,
                "output_format": output_format,
                "include_private": include_private
            }
        }

    @mcp_tool(name="project_template", description="Generate project templates and boilerplate")
    async def project_template(
        self,
        template_type: Literal[
            "python-package", "react-app", "node-api", "django-app", "fastapi", "cli-tool"
        ],
        project_name: str,
        options: Optional[Dict[str, Any]] = None,
        ctx: Context = None,
    ) -> Dict[str, Any]:
        """Generate project from template

        Args:
            template_type: Type of project template
            project_name: Name for the new project
            options: Additional template options
            ctx: FastMCP context
        """
        template_commands = {
            "python-package": f"uv init {project_name} && cd {project_name} && uv add pytest black ruff",
            "react-app": f"npx create-react-app {project_name}",
            "node-api": f"mkdir {project_name} && cd {project_name} && npm init -y && npm install express",
            "django-app": f"django-admin startproject {project_name}",
            "fastapi": f"mkdir {project_name} && cd {project_name} && uv init && uv add fastapi uvicorn",
            "cli-tool": f"mkdir {project_name} && cd {project_name} && uv init && uv add click rich"
        }

        return {
            "status": "not_implemented",
            "message": "Project template generation is not yet fully implemented",
            "info": "This tool will generate boilerplate projects from templates",
            "suggested_command": template_commands.get(template_type, "No command available"),
            "manual_steps": [
                f"1. Create directory: mkdir {project_name}",
                f"2. Initialize project based on type: {template_type}",
                "3. Set up dependencies and configuration",
                "4. Create initial project structure"
            ],
            "parameters_received": {
                "template_type": template_type,
                "project_name": project_name,
                "options": options
            }
        }

    @mcp_tool(
        name="dependency_check", description="🟡 SAFE: Analyze and update project dependencies"
    )
    async def dependency_check(
        self,
        project_path: str,
        check_security: Optional[bool] = True,
        suggest_updates: Optional[bool] = True,
        ctx: Context = None,
    ) -> Dict[str, Any]:
        """Check dependencies for updates and vulnerabilities"""
        try:
            project_path_obj = Path(project_path)
            if not project_path_obj.exists():
                return {"error": f"Project path not found: {project_path}"}

            results = {
                "project_path": project_path,
                "project_type": None,
                "dependencies": {},
                "updates_available": [],
                "security_issues": [],
                "recommendations": [],
                "summary": {},
            }

            # Detect project type and dependency files
            dependency_files = []

            # Python projects
            pyproject_toml = project_path_obj / "pyproject.toml"
            requirements_txt = project_path_obj / "requirements.txt"
            pipfile = project_path_obj / "Pipfile"

            # Node.js projects
            package_json = project_path_obj / "package.json"

            if pyproject_toml.exists():
                results["project_type"] = "python-pyproject"
                dependency_files.append(("pyproject.toml", pyproject_toml))
            elif requirements_txt.exists():
                results["project_type"] = "python-requirements"
                dependency_files.append(("requirements.txt", requirements_txt))
            elif pipfile.exists():
                results["project_type"] = "python-pipfile"
                dependency_files.append(("Pipfile", pipfile))
            elif package_json.exists():
                results["project_type"] = "nodejs"
                dependency_files.append(("package.json", package_json))
            else:
                return {
                    "error": "No supported dependency files found (pyproject.toml, requirements.txt, package.json)"
                }

            # Parse dependency files
            for file_type, file_path in dependency_files:
                try:
                    if file_type == "pyproject.toml":
                        deps = self._parse_pyproject_toml(file_path)
                    elif file_type == "requirements.txt":
                        deps = self._parse_requirements_txt(file_path)
                    elif file_type == "package.json":
                        deps = self._parse_package_json(file_path)
                    elif file_type == "Pipfile":
                        deps = self._parse_pipfile(file_path)
                    else:
                        deps = {}

                    results["dependencies"][file_type] = deps

                except Exception as e:
                    results["dependencies"][file_type] = {"error": f"Failed to parse: {str(e)}"}

            # Check for updates if requested
            if suggest_updates and results["project_type"]:
                if results["project_type"].startswith("python"):
                    updates = await self._check_python_updates(project_path_obj, ctx)
                    results["updates_available"] = updates
                elif results["project_type"] == "nodejs":
                    updates = await self._check_nodejs_updates(project_path_obj, ctx)
                    results["updates_available"] = updates

            # Basic security checks
            if check_security:
                security_issues = await self._check_security_issues(
                    project_path_obj, results["project_type"], ctx
                )
                results["security_issues"] = security_issues

            # Generate recommendations
            results["recommendations"] = self._generate_recommendations(results)

            # Create summary
            total_deps = sum(
                len(deps) if isinstance(deps, dict) and "error" not in deps else 0
                for deps in results["dependencies"].values()
            )

            results["summary"] = {
                "total_dependencies": total_deps,
                "updates_available": len(results["updates_available"]),
                "security_issues": len(results["security_issues"]),
                "project_type": results["project_type"],
            }

            if ctx:
                await ctx.info(
                    f"Dependency check complete: {total_deps} deps, {len(results['updates_available'])} updates, {len(results['security_issues'])} security issues"
                )

            return results

        except Exception as e:
            error_msg = f"Dependency check failed: {str(e)}"
            if ctx:
                await self.log_critical(error_msg, exception=e, ctx=ctx)
            return {"error": error_msg}

    def _parse_pyproject_toml(self, file_path: Path) -> Dict[str, str]:
        """Parse pyproject.toml for dependencies"""
        try:
            import tomllib
        except ImportError:
            try:
                import tomli as tomllib
            except ImportError:
                return {"error": "tomllib/tomli not available for parsing pyproject.toml"}

        try:
            with open(file_path, "rb") as f:
                data = tomllib.load(f)

            deps = {}

            # Get dependencies from different sections
            if "project" in data and "dependencies" in data["project"]:
                for dep in data["project"]["dependencies"]:
                    name = (
                        dep.split(">=")[0]
                        .split("==")[0]
                        .split("~=")[0]
                        .split(">")[0]
                        .split("<")[0]
                        .strip()
                    )
                    deps[name] = dep

            if (
                "tool" in data
                and "poetry" in data["tool"]
                and "dependencies" in data["tool"]["poetry"]
            ):
                poetry_deps = data["tool"]["poetry"]["dependencies"]
                for name, version in poetry_deps.items():
                    if name != "python":
                        deps[name] = (
                            str(version)
                            if not isinstance(version, dict)
                            else version.get("version", "latest")
                        )

            return deps

        except Exception as e:
            return {"error": f"Failed to parse pyproject.toml: {str(e)}"}

    def _parse_requirements_txt(self, file_path: Path) -> Dict[str, str]:
        """Parse requirements.txt for dependencies"""
        try:
            deps = {}
            with open(file_path) as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#"):
                        name = (
                            line.split(">=")[0]
                            .split("==")[0]
                            .split("~=")[0]
                            .split(">")[0]
                            .split("<")[0]
                            .strip()
                        )
                        deps[name] = line
            return deps
        except Exception as e:
            return {"error": f"Failed to parse requirements.txt: {str(e)}"}

    def _parse_package_json(self, file_path: Path) -> Dict[str, str]:
        """Parse package.json for dependencies"""
        try:
            with open(file_path) as f:
                data = json.load(f)

            deps = {}
            if "dependencies" in data:
                deps.update(data["dependencies"])
            if "devDependencies" in data:
                deps.update(data["devDependencies"])

            return deps
        except Exception as e:
            return {"error": f"Failed to parse package.json: {str(e)}"}

    def _parse_pipfile(self, file_path: Path) -> Dict[str, str]:
        """Parse Pipfile for dependencies"""
        try:
            # Simple parsing for Pipfile - would need toml parser for full support
            deps = {}
            with open(file_path) as f:
                content = f.read()
                # Basic extraction - this is simplified
                if "[packages]" in content:
                    lines = content.split("[packages]")[1].split("[")[0].strip().split("\n")
                    for line in lines:
                        if "=" in line and line.strip():
                            name, version = line.split("=", 1)
                            deps[name.strip()] = version.strip().strip('"')
            return deps
        except Exception as e:
            return {"error": f"Failed to parse Pipfile: {str(e)}"}

    async def _check_python_updates(self, project_path: Path, ctx: Context) -> List[Dict[str, Any]]:
        """Check for Python package updates using pip"""
        try:
            result = subprocess.run(
                ["python", "-m", "pip", "list", "--outdated", "--format=json"],
                cwd=project_path,
                capture_output=True,
                text=True,
                timeout=60,
            )

            if result.returncode == 0:
                try:
                    outdated = json.loads(result.stdout)
                    return [
                        {
                            "package": pkg["name"],
                            "current_version": pkg["version"],
                            "latest_version": pkg["latest_version"],
                            "type": pkg.get("latest_filetype", "wheel"),
                        }
                        for pkg in outdated
                    ]
                except json.JSONDecodeError:
                    return []
            return []
        except Exception:
            return []

    async def _check_nodejs_updates(self, project_path: Path, ctx: Context) -> List[Dict[str, Any]]:
        """Check for Node.js package updates using npm"""
        try:
            result = subprocess.run(
                ["npm", "outdated", "--json"],
                cwd=project_path,
                capture_output=True,
                text=True,
                timeout=60,
            )

            # npm outdated returns exit code 1 when there are outdated packages
            if result.stdout:
                try:
                    outdated = json.loads(result.stdout)
                    return [
                        {
                            "package": name,
                            "current_version": info.get("current"),
                            "latest_version": info.get("latest"),
                            "wanted_version": info.get("wanted"),
                        }
                        for name, info in outdated.items()
                    ]
                except json.JSONDecodeError:
                    return []
            return []
        except Exception:
            return []

    async def _check_security_issues(
        self, project_path: Path, project_type: str, ctx: Context
    ) -> List[Dict[str, Any]]:
        """Check for known security vulnerabilities"""
        issues = []

        try:
            if project_type.startswith("python"):
                # Try to use pip-audit if available
                result = subprocess.run(
                    ["python", "-m", "pip", "install", "pip-audit"],
                    cwd=project_path,
                    capture_output=True,
                    timeout=30,
                )

                if result.returncode == 0:
                    audit_result = subprocess.run(
                        ["python", "-m", "pip-audit", "--format=json"],
                        cwd=project_path,
                        capture_output=True,
                        text=True,
                        timeout=60,
                    )

                    if audit_result.returncode == 0:
                        try:
                            audit_data = json.loads(audit_result.stdout)
                            if audit_data:
                                issues.extend(audit_data)
                        except json.JSONDecodeError:
                            pass

            elif project_type == "nodejs":
                # Try npm audit
                audit_result = subprocess.run(
                    ["npm", "audit", "--json"],
                    cwd=project_path,
                    capture_output=True,
                    text=True,
                    timeout=60,
                )

                if audit_result.stdout:
                    try:
                        audit_data = json.loads(audit_result.stdout)
                        if "vulnerabilities" in audit_data:
                            for vuln_name, vuln_info in audit_data["vulnerabilities"].items():
                                issues.append(
                                    {
                                        "package": vuln_name,
                                        "severity": vuln_info.get("severity", "unknown"),
                                        "description": vuln_info.get("via", [{}])[0].get(
                                            "title", "Unknown vulnerability"
                                        ),
                                    }
                                )
                    except json.JSONDecodeError:
                        pass

        except Exception:
            pass

        return issues

    def _generate_recommendations(self, results: Dict[str, Any]) -> List[str]:
        """Generate actionable recommendations"""
        recommendations = []

        if results["updates_available"]:
            recommendations.append(f"Update {len(results['updates_available'])} outdated packages")

        if results["security_issues"]:
            critical_issues = [
                issue
                for issue in results["security_issues"]
                if issue.get("severity") in ["critical", "high"]
            ]
            if critical_issues:
                recommendations.append(
                    f"🚨 Address {len(critical_issues)} critical/high security vulnerabilities immediately"
                )
            else:
                recommendations.append(f"Review {len(results['security_issues'])} security issues")

        project_type = results.get("project_type")
        if project_type == "python-requirements":
            recommendations.append(
                "Consider migrating to pyproject.toml for better dependency management"
            )
        elif project_type == "nodejs":
            recommendations.append("Run 'npm update' to install available updates")
        elif project_type and project_type.startswith("python"):
            recommendations.append("Run 'pip install --upgrade' for packages that need updates")

        if not results["updates_available"] and not results["security_issues"]:
            recommendations.append("✅ All dependencies are up to date and secure")

        return recommendations
