"""
Git Integration Module

Provides advanced git operations, code search, and repository analysis.
"""

from .base import *


class GitIntegration(MCPMixin):
    """Git integration tools"""

    @mcp_tool(name="git_status", description="Get comprehensive git repository status")
    async def git_status(
        self, repository_path: str, include_untracked: Optional[bool] = True, ctx: Context = None
    ) -> Dict[str, Any]:
        """Get git repository status with modified, staged, and untracked files"""
        try:
            result = subprocess.run(
                ["git", "status", "--porcelain"],
                cwd=repository_path,
                capture_output=True,
                text=True,
            )

            if result.returncode != 0:
                return {"error": f"Git command failed: {result.stderr}"}

            status = {"modified": [], "staged": [], "untracked": [], "deleted": []}

            for line in result.stdout.strip().split("\n"):
                if not line:
                    continue

                status_code = line[:2]
                filename = line[3:]

                if status_code[0] in ["M", "A", "D", "R", "C"]:
                    status["staged"].append(filename)
                if status_code[1] in ["M", "D"]:
                    status["modified"].append(filename)
                elif status_code[1] == "?":
                    status["untracked"].append(filename)

            if ctx:
                await ctx.info(f"Git status retrieved for {repository_path}")

            return status

        except Exception as e:
            if ctx:
                await ctx.error(f"git status failed: {str(e)}")
            return {"error": str(e)}

    @mcp_tool(name="git_diff", description="Show git diffs with intelligent formatting")
    async def git_diff(
        self,
        repository_path: str,
        staged: Optional[bool] = False,
        file_path: Optional[str] = None,
        commit_range: Optional[str] = None,
        ctx: Context = None,
    ) -> str:
        """Show git diffs with syntax highlighting and statistics"""
        try:
            cmd = ["git", "diff"]

            if staged:
                cmd.append("--cached")
            if commit_range:
                cmd.append(commit_range)
            if file_path:
                cmd.append("--")
                cmd.append(file_path)

            result = subprocess.run(cmd, cwd=repository_path, capture_output=True, text=True)

            if result.returncode != 0:
                return f"Git diff failed: {result.stderr}"

            if ctx:
                await ctx.info(f"Git diff generated for {repository_path}")

            return result.stdout

        except Exception as e:
            if ctx:
                await ctx.error(f"git diff failed: {str(e)}")
            return f"Error: {str(e)}"

    @mcp_tool(
        name="git_grep",
        description="🔍 Advanced git grep with annotations, context, and intelligent filtering",
    )
    async def git_grep(
        self,
        repository_path: str,
        pattern: str,
        search_type: Optional[
            Literal["basic", "regex", "fixed-string", "extended-regex"]
        ] = "basic",
        file_patterns: Optional[List[str]] = None,
        exclude_patterns: Optional[List[str]] = None,
        context_lines: Optional[int] = 0,
        show_line_numbers: Optional[bool] = True,
        case_sensitive: Optional[bool] = True,
        whole_words: Optional[bool] = False,
        invert_match: Optional[bool] = False,
        max_results: Optional[int] = 1000,
        git_ref: Optional[str] = None,
        include_untracked: Optional[bool] = False,
        annotations: Optional[bool] = True,
        ctx: Context = None,
    ) -> Dict[str, Any]:
        """Advanced git grep with comprehensive search capabilities and intelligent annotations.

        🔍 SEARCH MODES:
        - basic: Simple text search (default)
        - regex: Perl-compatible regular expressions
        - fixed-string: Literal string search (fastest)
        - extended-regex: Extended regex with more features

        📝 ANNOTATIONS:
        - File metadata (size, last modified, git status)
        - Match context with syntax highlighting hints
        - Pattern analysis and suggestions
        - Performance statistics and optimization hints

        Args:
            repository_path: Path to git repository
            pattern: Search pattern (text, regex, or fixed string)
            search_type: Type of search to perform
            file_patterns: Glob patterns for files to include (e.g., ['*.py', '*.js'])
            exclude_patterns: Glob patterns for files to exclude (e.g., ['*.pyc', '__pycache__'])
            context_lines: Number of context lines before/after matches
            show_line_numbers: Include line numbers in results
            case_sensitive: Perform case-sensitive search
            whole_words: Match whole words only
            invert_match: Show lines that DON'T match the pattern
            max_results: Maximum number of matches to return
            git_ref: Search in specific git ref (branch/commit/tag)
            include_untracked: Include untracked files in search
            annotations: Include intelligent annotations and metadata

        Returns:
            Comprehensive search results with annotations and metadata
        """
        try:
            repo_path = Path(repository_path)
            if not repo_path.exists():
                return {"error": f"Repository path not found: {repository_path}"}

            if not (repo_path / ".git").exists():
                return {"error": f"Not a git repository: {repository_path}"}

            if ctx:
                await ctx.info(f"Starting git grep search for pattern: '{pattern}'")

            cmd = ["git", "grep"]

            if search_type == "regex":
                cmd.append("--perl-regexp")
            elif search_type == "fixed-string":
                cmd.append("--fixed-strings")
            elif search_type == "extended-regex":
                cmd.append("--extended-regexp")

            if not case_sensitive:
                cmd.append("--ignore-case")

            if whole_words:
                cmd.append("--word-regexp")

            if invert_match:
                cmd.append("--invert-match")

            if show_line_numbers:
                cmd.append("--line-number")

            if context_lines > 0:
                cmd.extend([f"--context={context_lines}"])

            cmd.append(pattern)

            if git_ref:
                cmd.append(git_ref)

            if file_patterns:
                cmd.append("--")
                for file_pattern in file_patterns:
                    cmd.append(file_pattern)

            search_start = time.time()

            if ctx:
                await ctx.info(f"Executing: {' '.join(cmd)}")

            result = subprocess.run(
                cmd,
                cwd=repository_path,
                capture_output=True,
                text=True,
                timeout=30,  # 30 second timeout
            )

            search_duration = time.time() - search_start

            if result.returncode > 1:
                return {"error": f"Git grep failed: {result.stderr}"}

            matches = []
            files_searched = set()
            total_matches = 0

            if result.stdout:
                lines = result.stdout.strip().split("\n")

                for line in lines[:max_results]:  # Limit results
                    if ":" in line:
                        parts = line.split(":", 2)
                        if len(parts) >= 3:
                            filename = parts[0]
                            line_number = parts[1]
                            content = parts[2]

                            try:
                                line_num = int(line_number)
                            except ValueError:
                                continue  # Skip malformed lines

                            files_searched.add(filename)
                            total_matches += 1

                            match_info = {
                                "file": filename,
                                "line_number": line_num,
                                "content": content,
                                "match_type": "exact",
                            }

                            if annotations:
                                match_info["annotations"] = await self._annotate_git_grep_match(
                                    repo_path,
                                    filename,
                                    line_num,
                                    content,
                                    pattern,
                                    search_type,
                                    ctx,
                                )

                            matches.append(match_info)

                    elif "-" in line and context_lines > 0:
                        parts = line.split("-", 2)
                        if len(parts) >= 3:
                            filename = parts[0]
                            line_number = parts[1]
                            content = parts[2]

                            try:
                                line_num = int(line_number)
                            except ValueError:
                                continue

                            files_searched.add(filename)

                            match_info = {
                                "file": filename,
                                "line_number": line_num,
                                "content": content,
                                "match_type": "context",
                            }

                            matches.append(match_info)

            untracked_matches = []
            if include_untracked and result.returncode == 1:  # No matches in tracked files
                untracked_matches = await self._search_untracked_files(
                    repo_path,
                    pattern,
                    search_type,
                    file_patterns,
                    exclude_patterns,
                    context_lines,
                    show_line_numbers,
                    case_sensitive,
                    whole_words,
                    invert_match,
                    max_results,
                    annotations,
                    ctx,
                )

            search_result = {
                "repository_path": str(repo_path),
                "pattern": pattern,
                "search_type": search_type,
                "total_matches": total_matches,
                "files_with_matches": len(files_searched),
                "files_searched": list(files_searched),
                "matches": matches,
                "untracked_matches": untracked_matches,
                "performance": {
                    "search_duration_seconds": round(search_duration, 3),
                    "matches_per_second": (
                        round(total_matches / search_duration, 2) if search_duration > 0 else 0
                    ),
                    "git_grep_exit_code": result.returncode,
                },
                "search_parameters": {
                    "context_lines": context_lines,
                    "case_sensitive": case_sensitive,
                    "whole_words": whole_words,
                    "invert_match": invert_match,
                    "max_results": max_results,
                    "git_ref": git_ref,
                    "include_untracked": include_untracked,
                    "file_patterns": file_patterns,
                    "exclude_patterns": exclude_patterns,
                },
            }

            if annotations:
                search_result["annotations"] = await self._generate_search_annotations(
                    search_result, pattern, search_type, repo_path, ctx
                )

            if ctx:
                await ctx.info(
                    f"Git grep completed: {total_matches} matches in {len(files_searched)} files "
                    f"in {search_duration:.2f}s"
                )

            return search_result

        except subprocess.TimeoutExpired:
            error_msg = "Git grep search timed out (>30s)"
            if ctx:
                await ctx.error(error_msg)
            return {"error": error_msg}

        except Exception as e:
            error_msg = f"Git grep failed: {str(e)}"
            if ctx:
                await ctx.error(f"CRITICAL: {error_msg} | Exception: {type(e).__name__}")
            return {"error": error_msg}

    async def _annotate_git_grep_match(
        self,
        repo_path: Path,
        filename: str,
        line_number: int,
        content: str,
        pattern: str,
        search_type: str,
        ctx: Context,
    ) -> Dict[str, Any]:
        """Generate intelligent annotations for a git grep match"""
        try:
            file_path = repo_path / filename
            annotations = {
                "file_info": {},
                "match_analysis": {},
                "context_hints": {},
                "suggestions": [],
            }

            if file_path.exists():
                stat_info = file_path.stat()
                annotations["file_info"] = {
                    "size_bytes": stat_info.st_size,
                    "modified_timestamp": stat_info.st_mtime,
                    "modified_iso": datetime.fromtimestamp(stat_info.st_mtime).isoformat(),
                    "extension": file_path.suffix,
                    "is_binary": self._is_likely_binary(file_path),
                    "estimated_lines": await self._estimate_file_lines(file_path),
                }

                try:
                    git_status = subprocess.run(
                        ["git", "status", "--porcelain", filename],
                        cwd=repo_path,
                        capture_output=True,
                        text=True,
                        timeout=5,
                    )
                    if git_status.returncode == 0:
                        status_line = git_status.stdout.strip()
                        if status_line:
                            annotations["file_info"]["git_status"] = status_line[:2]
                        else:
                            annotations["file_info"]["git_status"] = "clean"
                except Exception:
                    annotations["file_info"]["git_status"] = "unknown"

            annotations["match_analysis"] = {
                "line_length": len(content),
                "leading_whitespace": len(content) - len(content.lstrip()),
                "pattern_occurrences": (
                    content.count(pattern) if search_type == "fixed-string" else 1
                ),
                "context_type": self._detect_code_context(content, file_path.suffix),
            }

            if file_path.suffix in [".py", ".js", ".ts", ".java", ".cpp", ".c"]:
                annotations["context_hints"]["language"] = self._detect_language(file_path.suffix)
                annotations["context_hints"]["likely_element"] = self._analyze_code_element(content)

            suggestions = []

            if search_type == "basic" and any(char in pattern for char in r".*+?[]{}()|\^$"):
                suggestions.append(
                    {
                        "type": "optimization",
                        "message": "Pattern contains regex characters. Consider using --perl-regexp for regex search.",
                        "command_hint": f"git grep --perl-regexp '{pattern}'",
                    }
                )

            if file_path.suffix and not any(
                f"*.{file_path.suffix[1:]}" in str(pattern) for pattern in []
            ):
                suggestions.append(
                    {
                        "type": "scope",
                        "message": f"Consider limiting search to {file_path.suffix} files for better performance.",
                        "command_hint": f"git grep '{pattern}' -- '*.{file_path.suffix[1:]}'",
                    }
                )

            annotations["suggestions"] = suggestions

            return annotations

        except Exception as e:
            return {"error": f"Failed to generate annotations: {str(e)}"}

    async def _search_untracked_files(
        self,
        repo_path: Path,
        pattern: str,
        search_type: str,
        file_patterns: Optional[List[str]],
        exclude_patterns: Optional[List[str]],
        context_lines: int,
        show_line_numbers: bool,
        case_sensitive: bool,
        whole_words: bool,
        invert_match: bool,
        max_results: int,
        annotations: bool,
        ctx: Context,
    ) -> List[Dict[str, Any]]:
        """Search untracked files using traditional grep"""
        try:
            untracked_result = subprocess.run(
                ["git", "ls-files", "--others", "--exclude-standard"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                timeout=10,
            )

            if untracked_result.returncode != 0:
                return []

            untracked_files = [f for f in untracked_result.stdout.strip().split("\n") if f]

            if not untracked_files:
                return []

            cmd = ["grep"]

            if search_type == "regex":
                cmd.append("--perl-regexp")
            elif search_type == "fixed-string":
                cmd.append("--fixed-strings")
            elif search_type == "extended-regex":
                cmd.append("--extended-regexp")

            if not case_sensitive:
                cmd.append("--ignore-case")

            if whole_words:
                cmd.append("--word-regexp")

            if invert_match:
                cmd.append("--invert-match")

            if show_line_numbers:
                cmd.append("--line-number")

            if context_lines > 0:
                cmd.extend([f"--context={context_lines}"])

            cmd.extend(["--with-filename", pattern])
            cmd.extend(untracked_files)

            grep_result = subprocess.run(
                cmd, cwd=repo_path, capture_output=True, text=True, timeout=15
            )

            matches = []
            if grep_result.stdout:
                lines = grep_result.stdout.strip().split("\n")

                for line in lines[:max_results]:
                    if ":" in line:
                        parts = line.split(":", 2)
                        if len(parts) >= 3:
                            filename = parts[0]
                            line_number = parts[1]
                            content = parts[2]

                            try:
                                line_num = int(line_number)
                            except ValueError:
                                continue

                            match_info = {
                                "file": filename,
                                "line_number": line_num,
                                "content": content,
                                "match_type": "untracked",
                                "file_status": "untracked",
                            }

                            if annotations:
                                match_info["annotations"] = await self._annotate_git_grep_match(
                                    repo_path,
                                    filename,
                                    line_num,
                                    content,
                                    pattern,
                                    search_type,
                                    ctx,
                                )

                            matches.append(match_info)

            return matches

        except Exception as e:
            if ctx:
                await ctx.warning(f"Failed to search untracked files: {str(e)}")
            return []

    async def _generate_search_annotations(
        self,
        search_result: Dict[str, Any],
        pattern: str,
        search_type: str,
        repo_path: Path,
        ctx: Context,
    ) -> Dict[str, Any]:
        """Generate comprehensive search annotations and insights"""
        try:
            annotations = {
                "search_insights": {},
                "performance_analysis": {},
                "pattern_analysis": {},
                "optimization_suggestions": [],
            }

            total_matches = search_result["total_matches"]
            files_with_matches = search_result["files_with_matches"]
            search_duration = search_result["performance"]["search_duration_seconds"]

            annotations["search_insights"] = {
                "match_density": round(total_matches / max(files_with_matches, 1), 2),
                "search_efficiency": (
                    "high"
                    if search_duration < 1.0
                    else "medium"
                    if search_duration < 5.0
                    else "low"
                ),
                "coverage_assessment": await self._assess_search_coverage(
                    repo_path, search_result, ctx
                ),
            }

            annotations["performance_analysis"] = {
                "is_fast_search": search_duration < 1.0,
                "bottlenecks": [],
                "optimization_potential": (
                    "high"
                    if search_duration > 5.0
                    else "medium"
                    if search_duration > 2.0
                    else "low"
                ),
            }

            if search_duration > 2.0:
                annotations["performance_analysis"]["bottlenecks"].append(
                    "Large repository or complex pattern"
                )

            annotations["pattern_analysis"] = {
                "pattern_type": self._analyze_pattern_type(pattern, search_type),
                "complexity": self._assess_pattern_complexity(pattern, search_type),
                "suggested_improvements": [],
            }

            suggestions = []

            if search_duration > 5.0:
                suggestions.append(
                    {
                        "type": "performance",
                        "priority": "high",
                        "suggestion": "Consider adding file type filters to reduce search scope",
                        "example": f"git grep '{pattern}' -- '*.py' '*.js'",
                    }
                )

            if total_matches > 500:
                suggestions.append(
                    {
                        "type": "refinement",
                        "priority": "medium",
                        "suggestion": "Large number of matches. Consider refining the pattern for more specific results",
                        "example": f"git grep '{pattern}' | head -20",
                    }
                )

            if search_type == "basic" and len(pattern) < 3:
                suggestions.append(
                    {
                        "type": "accuracy",
                        "priority": "medium",
                        "suggestion": "Short patterns may produce many false positives. Consider using word boundaries",
                        "example": f"git grep --word-regexp '{pattern}'",
                    }
                )

            annotations["optimization_suggestions"] = suggestions

            return annotations

        except Exception as e:
            return {"error": f"Failed to generate search annotations: {str(e)}"}

    async def _assess_search_coverage(
        self, repo_path: Path, search_result: Dict[str, Any], ctx: Context
    ) -> str:
        """Assess how comprehensive the search coverage was"""
        try:
            ls_files_result = subprocess.run(
                ["git", "ls-files"], cwd=repo_path, capture_output=True, text=True, timeout=10
            )

            if ls_files_result.returncode != 0:
                return "unknown"

            total_files = len([f for f in ls_files_result.stdout.strip().split("\n") if f])
            files_searched = len(search_result["files_searched"])

            if files_searched == 0:
                return "no_matches"
            elif files_searched / total_files > 0.5:
                return "comprehensive"
            elif files_searched / total_files > 0.1:
                return "moderate"
            else:
                return "limited"

        except Exception:
            return "unknown"

    def _is_likely_binary(self, file_path: Path) -> bool:
        """Check if file is likely binary"""
        try:
            with open(file_path, "rb") as f:
                chunk = f.read(8192)
                return b"\0" in chunk
        except Exception:
            return False

    async def _estimate_file_lines(self, file_path: Path) -> int:
        """Estimate number of lines in file"""
        try:
            with open(file_path, "rb") as f:
                return sum(1 for _ in f)
        except Exception:
            return 0

    def _detect_code_context(self, content: str, file_extension: str) -> str:
        """Detect what type of code context this match represents"""
        content_lower = content.strip().lower()

        if file_extension in [".py"]:
            if content_lower.startswith("def "):
                return "function_definition"
            elif content_lower.startswith("class "):
                return "class_definition"
            elif content_lower.startswith("import ") or content_lower.startswith("from "):
                return "import_statement"
            elif "#" in content:
                return "comment"
        elif file_extension in [".js", ".ts"]:
            if "function" in content_lower:
                return "function_definition"
            elif "class" in content_lower:
                return "class_definition"
            elif "//" in content or "/*" in content:
                return "comment"
        elif file_extension in [".md"]:
            if content.strip().startswith("#"):
                return "markdown_heading"

        return "code_line"

    def _detect_language(self, file_extension: str) -> str:
        """Detect programming language from file extension"""
        lang_map = {
            ".py": "Python",
            ".js": "JavaScript",
            ".ts": "TypeScript",
            ".java": "Java",
            ".cpp": "C++",
            ".c": "C",
            ".go": "Go",
            ".rs": "Rust",
            ".rb": "Ruby",
            ".php": "PHP",
            ".sh": "Shell",
            ".md": "Markdown",
            ".yml": "YAML",
            ".yaml": "YAML",
            ".json": "JSON",
            ".xml": "XML",
            ".html": "HTML",
            ".css": "CSS",
        }
        return lang_map.get(file_extension, "Unknown")

    def _analyze_code_element(self, content: str) -> str:
        """Analyze what code element this line likely represents"""
        stripped = content.strip()

        if not stripped:
            return "empty_line"
        elif stripped.startswith("#") or stripped.startswith("//"):
            return "comment"
        elif any(keyword in stripped for keyword in ["def ", "function ", "class ", "interface "]):
            return "definition"
        elif any(keyword in stripped for keyword in ["import ", "from ", "#include", "require("]):
            return "import"
        elif "=" in stripped and not any(op in stripped for op in ["==", "!=", "<=", ">="]):
            return "assignment"
        elif any(keyword in stripped for keyword in ["if ", "else", "elif", "while ", "for "]):
            return "control_flow"
        elif stripped.endswith(":") or stripped.endswith("{"):
            return "block_start"
        else:
            return "statement"

    def _analyze_pattern_type(self, pattern: str, search_type: str) -> str:
        """Analyze the type of search pattern"""
        if search_type == "fixed-string":
            return "literal_string"
        elif search_type in ["regex", "extended-regex"]:
            if any(char in pattern for char in r".*+?[]{}()|\^$"):
                return "complex_regex"
            else:
                return "simple_regex"
        else:  # basic
            if any(char in pattern for char in r".*+?[]{}()|\^$"):
                return "basic_with_special_chars"
            else:
                return "simple_text"

    def _assess_pattern_complexity(self, pattern: str, search_type: str) -> str:
        """Assess the complexity of the search pattern"""
        if search_type == "fixed-string":
            return "low"

        complexity_indicators = [
            r"\w",
            r"\d",
            r"\s",  # Character classes
            r".*",
            r".+",
            r".?",  # Quantifiers
            r"[",
            r"]",  # Character sets
            r"(",
            r")",  # Groups
            r"|",  # Alternation
            r"^",
            r"$",  # Anchors
            r"\\",  # Escapes
        ]

        complexity_score = sum(1 for indicator in complexity_indicators if indicator in pattern)

        if complexity_score == 0:
            return "low"
        elif complexity_score <= 3:
            return "medium"
        else:
            return "high"

    @mcp_tool(
        name="git_commit_prepare",
        description="🟡 SAFE: Intelligent commit preparation with AI-suggested messages",
    )
    async def git_commit_prepare(
        self,
        repository_path: str,
        files: List[str],
        suggest_message: Optional[bool] = True,
        ctx: Context = None,
    ) -> Dict[str, Any]:
        """Prepare git commit with AI-suggested message based on file changes"""
        try:
            # Verify git repository
            result = subprocess.run(
                ["git", "rev-parse", "--git-dir"],
                cwd=repository_path,
                capture_output=True,
                text=True,
            )

            if result.returncode != 0:
                return {"error": f"Not a git repository: {repository_path}"}

            # Stage specified files
            stage_results = []
            for file_path in files:
                result = subprocess.run(
                    ["git", "add", file_path],
                    cwd=repository_path,
                    capture_output=True,
                    text=True,
                )

                if result.returncode == 0:
                    stage_results.append({"file": file_path, "staged": True})
                else:
                    stage_results.append(
                        {"file": file_path, "staged": False, "error": result.stderr.strip()}
                    )

            # Get staged changes for commit message suggestion
            suggested_message = ""
            if suggest_message:
                diff_result = subprocess.run(
                    ["git", "diff", "--cached", "--stat"],
                    cwd=repository_path,
                    capture_output=True,
                    text=True,
                )

                if diff_result.returncode == 0:
                    stats = diff_result.stdout.strip()

                    # Analyze file types and changes
                    lines = stats.split("\n")
                    modified_files = []
                    for line in lines[:-1]:  # Last line is summary
                        if "|" in line:
                            file_name = line.split("|")[0].strip()
                            modified_files.append(file_name)

                    # Generate suggested commit message
                    if len(modified_files) == 1:
                        file_ext = Path(modified_files[0]).suffix
                        if file_ext in [".py", ".js", ".ts"]:
                            suggested_message = f"Update {Path(modified_files[0]).name}"
                        elif file_ext in [".md", ".txt", ".rst"]:
                            suggested_message = (
                                f"Update documentation in {Path(modified_files[0]).name}"
                            )
                        elif file_ext in [".json", ".yaml", ".yml", ".toml"]:
                            suggested_message = (
                                f"Update configuration in {Path(modified_files[0]).name}"
                            )
                        else:
                            suggested_message = f"Update {Path(modified_files[0]).name}"
                    elif len(modified_files) <= 5:
                        suggested_message = f"Update {len(modified_files)} files"
                    else:
                        suggested_message = f"Update multiple files ({len(modified_files)} changed)"

            # Get current status
            status_result = subprocess.run(
                ["git", "status", "--porcelain"],
                cwd=repository_path,
                capture_output=True,
                text=True,
            )

            response = {
                "repository": repository_path,
                "staged_files": stage_results,
                "suggested_message": suggested_message,
                "ready_to_commit": all(r["staged"] for r in stage_results),
                "status": status_result.stdout.strip()
                if status_result.returncode == 0
                else "Status unavailable",
            }

            if ctx:
                staged_count = sum(1 for r in stage_results if r["staged"])
                await ctx.info(f"Prepared commit: {staged_count}/{len(files)} files staged")

            return response

        except Exception as e:
            error_msg = f"Git commit preparation failed: {str(e)}"
            if ctx:
                await ctx.error(error_msg)
            return {"error": error_msg}
