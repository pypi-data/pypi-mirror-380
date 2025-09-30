"""
Archive and Compression Operations Module

Provides archive creation, extraction, and compression capabilities.
"""

import os
import tarfile
import zipfile
from pathlib import Path
from typing import Any, Dict, List, Literal, Optional

from fastmcp import Context
from fastmcp.contrib.mcp_mixin import MCPMixin, mcp_tool


class ArchiveCompression(MCPMixin):
    """Archive and compression tools

    - list_archive_contents: List archive contents (read-only)
    - create_archive: Create compressed archives
    - extract_archive: Extract archives (can overwrite files)
    """

    def __init__(self):
        super().__init__()

    @mcp_tool(name="create_archive", description="Create compressed archives in various formats")
    async def create_archive(
        self,
        source_paths: List[str],
        output_path: str,
        format: Literal["tar", "tar.gz", "tgz", "tar.bz2", "tar.xz", "zip"],
        exclude_patterns: Optional[List[str]] = None,
        compression_level: Optional[int] = 6,
        follow_symlinks: Optional[bool] = False,
        ctx: Context = None,
    ) -> Dict[str, Any]:
        """Create compressed archive with comprehensive format support

        Args:
            source_paths: List of files/directories to archive
            output_path: Output archive file path
            format: Archive format (tar, tar.gz, tgz, tar.bz2, tar.xz, zip)
            exclude_patterns: Patterns to exclude (glob-style)
            compression_level: Compression level (1-9, default 6)
            follow_symlinks: Whether to follow symbolic links
        """
        import tarfile
        import zipfile
        from fnmatch import fnmatch

        try:
            output_path = Path(output_path)
            exclude_patterns = exclude_patterns or []

            format_map = {"tgz": "tar.gz", "tbz": "tar.bz2", "tbz2": "tar.bz2", "txz": "tar.xz"}
            archive_format = format_map.get(format, format)

            def should_exclude(path_str: str) -> bool:
                """Check if path should be excluded based on patterns"""
                path_obj = Path(path_str)
                for pattern in exclude_patterns:
                    if fnmatch(path_obj.name, pattern) or fnmatch(str(path_obj), pattern):
                        return True
                return False

            files_added = []
            total_size = 0
            compressed_size = 0

            if ctx:
                await ctx.info(f"Creating {archive_format} archive: {output_path}")

            if archive_format.startswith("tar"):
                if archive_format == "tar":
                    mode = "w"
                elif archive_format == "tar.gz":
                    mode = "w:gz"
                elif archive_format == "tar.bz2":
                    mode = "w:bz2"
                elif archive_format == "tar.xz":
                    mode = "w:xz"
                else:
                    raise ValueError(f"Unsupported tar format: {archive_format}")

                with tarfile.open(output_path, mode) as tar:
                    for source_path in source_paths:
                        source = Path(source_path)
                        if not source.exists():
                            if ctx:
                                await ctx.warning(f"Source not found: {source_path}")
                            continue

                        if source.is_file():
                            if not should_exclude(str(source)):
                                try:
                                    tar.add(
                                        source, arcname=source.name, follow_symlinks=follow_symlinks
                                    )
                                except TypeError:
                                    tar.add(source, arcname=source.name)
                                files_added.append(str(source))
                                total_size += source.stat().st_size
                        else:
                            for root, dirs, files in os.walk(source, followlinks=follow_symlinks):
                                dirs[:] = [
                                    d for d in dirs if not should_exclude(os.path.join(root, d))
                                ]

                                for file in files:
                                    file_path = Path(root) / file
                                    if not should_exclude(str(file_path)):
                                        arcname = file_path.relative_to(source.parent)
                                        try:
                                            tar.add(
                                                file_path,
                                                arcname=arcname,
                                                follow_symlinks=follow_symlinks,
                                            )
                                        except TypeError:
                                            tar.add(file_path, arcname=arcname)
                                        files_added.append(str(file_path))
                                        total_size += file_path.stat().st_size

                        if ctx:
                            await ctx.report_progress(
                                len(files_added) / max(len(source_paths) * 10, 1),
                                f"Added {len(files_added)} files...",
                            )

            elif archive_format == "zip":
                with zipfile.ZipFile(
                    output_path,
                    "w",
                    compression=zipfile.ZIP_DEFLATED,
                    compresslevel=compression_level,
                ) as zip_file:
                    for source_path in source_paths:
                        source = Path(source_path)
                        if not source.exists():
                            if ctx:
                                await ctx.warning(f"Source not found: {source_path}")
                            continue

                        if source.is_file():
                            if not should_exclude(str(source)):
                                zip_file.write(source, arcname=source.name)
                                files_added.append(str(source))
                                total_size += source.stat().st_size
                        else:
                            for root, dirs, files in os.walk(source, followlinks=follow_symlinks):
                                dirs[:] = [
                                    d for d in dirs if not should_exclude(os.path.join(root, d))
                                ]

                                for file in files:
                                    file_path = Path(root) / file
                                    if not should_exclude(str(file_path)):
                                        arcname = file_path.relative_to(source.parent)
                                        zip_file.write(file_path, arcname=arcname)
                                        files_added.append(str(file_path))
                                        total_size += file_path.stat().st_size

                        if ctx:
                            await ctx.report_progress(
                                len(files_added) / max(len(source_paths) * 10, 1),
                                f"Added {len(files_added)} files...",
                            )
            else:
                raise ValueError(f"Unsupported archive format: {archive_format}")

            if output_path.exists():
                compressed_size = output_path.stat().st_size

            compression_ratio = (1 - compressed_size / total_size) * 100 if total_size > 0 else 0

            result = {
                "archive_path": str(output_path),
                "format": archive_format,
                "files_count": len(files_added),
                "total_size_bytes": total_size,
                "compressed_size_bytes": compressed_size,
                "compression_ratio_percent": round(compression_ratio, 2),
                "files_added": files_added[:50],  # Limit to first 50 for display
            }

            if ctx:
                await ctx.info(
                    f"Archive created successfully: {len(files_added)} files, "
                    f"{compression_ratio:.1f}% compression"
                )

            return result

        except Exception as e:
            error_msg = f"Failed to create archive: {str(e)}"
            if ctx:
                await ctx.error(error_msg)
            return {"error": error_msg}

    @mcp_tool(
        name="extract_archive", description="Extract compressed archives with format auto-detection"
    )
    async def extract_archive(
        self,
        archive_path: str,
        destination: str,
        overwrite: Optional[bool] = False,
        preserve_permissions: Optional[bool] = True,
        extract_filter: Optional[List[str]] = None,
        ctx: Context = None,
    ) -> Dict[str, Any]:
        """Extract archive contents with comprehensive format support

        Args:
            archive_path: Path to archive file
            destination: Destination directory for extraction
            overwrite: Whether to overwrite existing files
            preserve_permissions: Whether to preserve file permissions
            extract_filter: List of patterns to extract (glob-style)
        """
        import tarfile
        import zipfile
        from fnmatch import fnmatch

        try:
            archive = Path(archive_path)
            dest = Path(destination)

            if not archive.exists():
                return {"error": f"Archive not found: {archive_path}"}

            dest.mkdir(parents=True, exist_ok=True)

            archive_format = self._detect_archive_format(archive)
            if not archive_format:
                return {"error": f"Unable to detect archive format: {archive_path}"}

            if ctx:
                await ctx.info(f"Extracting {archive_format} archive: {archive_path}")

            extracted_files = []

            def should_extract(member_name: str) -> bool:
                """Check if member should be extracted based on filter"""
                if not extract_filter:
                    return True
                return any(fnmatch(member_name, pattern) for pattern in extract_filter)

            def safe_extract_path(member_path: str, dest_path: Path) -> Path:
                """Ensure extraction path is safe (prevents directory traversal)"""
                full_path = dest_path / member_path
                resolved_path = full_path.resolve()
                dest_resolved = dest_path.resolve()

                try:
                    resolved_path.relative_to(dest_resolved)
                    return resolved_path
                except ValueError:
                    raise ValueError(
                        f"SECURITY_VIOLATION: Path traversal attack detected: {member_path}"
                    ) from None

            if archive_format.startswith("tar"):
                with tarfile.open(archive, "r:*") as tar:
                    members = tar.getmembers()
                    total_members = len(members)

                    for i, member in enumerate(members):
                        if should_extract(member.name):
                            try:
                                safe_path = safe_extract_path(member.name, dest)

                                if safe_path.exists() and not overwrite:
                                    if ctx:
                                        await ctx.warning(f"Skipping existing file: {member.name}")
                                    continue

                                tar.extract(member, dest, filter="data")
                                extracted_files.append(member.name)

                                if preserve_permissions and hasattr(member, "mode"):
                                    try:
                                        safe_path.chmod(member.mode)
                                    except (OSError, PermissionError):
                                        pass  # Silently fail on permission errors

                            except ValueError as e:
                                # Check if this is a security violation (path traversal attack)
                                if "SECURITY_VIOLATION" in str(e):
                                    # 🚨 EMERGENCY: Security violation detected
                                    emergency_msg = (
                                        f"Security violation during archive extraction: {str(e)}"
                                    )
                                    if ctx:
                                        # Check if emergency method exists (future-proofing)
                                        if hasattr(ctx, "emergency"):
                                            await ctx.emergency(emergency_msg)
                                        else:
                                            # Fallback to error with EMERGENCY prefix
                                            await ctx.error(f"EMERGENCY: {emergency_msg}")
                                    else:
                                        print(f"🚨 EMERGENCY: {emergency_msg}")
                                else:
                                    # Regular path issues (non-security)
                                    if ctx:
                                        await ctx.warning(f"Skipping unsafe path: {e}")
                                continue

                        if ctx and i % 10 == 0:  # Update progress every 10 files
                            await ctx.report_progress(
                                i / total_members, f"Extracted {len(extracted_files)} files..."
                            )

            elif archive_format == "zip":
                with zipfile.ZipFile(archive, "r") as zip_file:
                    members = zip_file.namelist()
                    total_members = len(members)

                    for i, member_name in enumerate(members):
                        if should_extract(member_name):
                            try:
                                safe_path = safe_extract_path(member_name, dest)

                                if safe_path.exists() and not overwrite:
                                    if ctx:
                                        await ctx.warning(f"Skipping existing file: {member_name}")
                                    continue

                                zip_file.extract(member_name, dest)
                                extracted_files.append(member_name)

                            except ValueError as e:
                                if ctx:
                                    await ctx.warning(f"Skipping unsafe path: {e}")
                                continue

                        if ctx and i % 10 == 0:
                            await ctx.report_progress(
                                i / total_members, f"Extracted {len(extracted_files)} files..."
                            )
            else:
                return {"error": f"Unsupported archive format for extraction: {archive_format}"}

            result = {
                "archive_path": str(archive),
                "destination": str(dest),
                "format": archive_format,
                "files_extracted": len(extracted_files),
                "extracted_files": extracted_files[:50],  # Limit for display
            }

            if ctx:
                await ctx.info(f"Extraction completed: {len(extracted_files)} files")

            return result

        except Exception as e:
            error_msg = f"Failed to extract archive: {str(e)}"
            if ctx:
                await ctx.error(error_msg)
            return {"error": error_msg}

    @mcp_tool(name="list_archive_contents", description="🟢 SAFE: List contents of archive without extracting")
    async def list_archive_contents(
        self, archive_path: str, detailed: Optional[bool] = False, ctx: Context = None
    ) -> Dict[str, Any]:
        """List archive contents with optional detailed information - SAFE read-only operation"""
        return await self.list_archive(archive_path, detailed, ctx)

    @mcp_tool(name="list_archive", description="List contents of archive without extracting")
    async def list_archive(
        self, archive_path: str, detailed: Optional[bool] = False, ctx: Context = None
    ) -> Dict[str, Any]:
        """List archive contents with optional detailed information"""
        import tarfile
        import zipfile

        try:
            archive = Path(archive_path)
            if not archive.exists():
                return {"error": f"Archive not found: {archive_path}"}

            archive_format = self._detect_archive_format(archive)
            if not archive_format:
                return {"error": f"Unable to detect archive format: {archive_path}"}

            if ctx:
                await ctx.info(f"Listing {archive_format} archive: {archive_path}")

            contents = []
            total_size = 0

            if archive_format.startswith("tar"):
                with tarfile.open(archive, "r:*") as tar:
                    for member in tar.getmembers():
                        item = {
                            "name": member.name,
                            "type": (
                                "file"
                                if member.isfile()
                                else "directory"
                                if member.isdir()
                                else "other"
                            ),
                            "size": member.size,
                        }

                        if detailed:
                            item.update(
                                {
                                    "mode": oct(member.mode) if member.mode else None,
                                    "uid": member.uid,
                                    "gid": member.gid,
                                    "mtime": (
                                        datetime.fromtimestamp(member.mtime).isoformat()
                                        if member.mtime
                                        else None
                                    ),
                                    "is_symlink": member.issym() or member.islnk(),
                                    "linkname": member.linkname if member.linkname else None,
                                }
                            )

                        contents.append(item)
                        total_size += member.size or 0

            elif archive_format == "zip":
                with zipfile.ZipFile(archive, "r") as zip_file:
                    for info in zip_file.infolist():
                        item = {
                            "name": info.filename,
                            "type": "directory" if info.is_dir() else "file",
                            "size": info.file_size,
                        }

                        if detailed:
                            item.update(
                                {
                                    "compressed_size": info.compress_size,
                                    "compression_type": info.compress_type,
                                    "date_time": (
                                        f"{info.date_time[0]:04d}-{info.date_time[1]:02d}-{info.date_time[2]:02d} "
                                        f"{info.date_time[3]:02d}:{info.date_time[4]:02d}:{info.date_time[5]:02d}"
                                    ),
                                    "crc": info.CRC,
                                    "external_attr": info.external_attr,
                                }
                            )

                        contents.append(item)
                        total_size += info.file_size

            result = {
                "archive_path": str(archive),
                "format": archive_format,
                "total_files": len(contents),
                "total_size_bytes": total_size,
                "contents": contents,
            }

            if ctx:
                await ctx.info(f"Listed {len(contents)} items in archive")

            return result

        except Exception as e:
            error_msg = f"Failed to list archive: {str(e)}"
            if ctx:
                await ctx.error(error_msg)
            return {"error": error_msg}

    @mcp_tool(name="compress_file", description="Compress individual files with various algorithms")
    async def compress_file(
        self,
        file_path: str,
        output_path: Optional[str] = None,
        algorithm: Literal["gzip", "bzip2", "xz", "lzma"] = "gzip",
        compression_level: Optional[int] = 6,
        keep_original: Optional[bool] = True,
        ctx: Context = None,
    ) -> Dict[str, Any]:
        """Compress individual files using various compression algorithms"""
        import bz2
        import gzip
        import lzma

        try:
            source = Path(file_path)
            if not source.exists():
                return {"error": f"File not found: {file_path}"}

            if not source.is_file():
                return {"error": f"Path is not a file: {file_path}"}

            if output_path:
                output = Path(output_path)
            else:
                extensions = {"gzip": ".gz", "bzip2": ".bz2", "xz": ".xz", "lzma": ".lzma"}
                output = source.with_suffix(source.suffix + extensions[algorithm])

            if ctx:
                await ctx.info(f"Compressing {source} with {algorithm}")

            original_size = source.stat().st_size

            if algorithm == "gzip":
                with (
                    source.open("rb") as src,
                    gzip.open(output, "wb", compresslevel=compression_level) as dst,
                ):
                    shutil.copyfileobj(src, dst)
            elif algorithm == "bzip2":
                with (
                    source.open("rb") as src,
                    bz2.open(output, "wb", compresslevel=compression_level) as dst,
                ):
                    shutil.copyfileobj(src, dst)
            elif algorithm in ("xz", "lzma"):
                preset = compression_level if compression_level <= 9 else 6
                with source.open("rb") as src, lzma.open(output, "wb", preset=preset) as dst:
                    shutil.copyfileobj(src, dst)

            compressed_size = output.stat().st_size
            compression_ratio = (
                (1 - compressed_size / original_size) * 100 if original_size > 0 else 0
            )

            if not keep_original:
                source.unlink()

            result = {
                "original_file": str(source),
                "compressed_file": str(output),
                "algorithm": algorithm,
                "original_size_bytes": original_size,
                "compressed_size_bytes": compressed_size,
                "compression_ratio_percent": round(compression_ratio, 2),
                "original_kept": keep_original,
            }

            if ctx:
                await ctx.info(f"Compression completed: {compression_ratio:.1f}% reduction")

            return result

        except Exception as e:
            error_msg = f"Failed to compress file: {str(e)}"
            if ctx:
                await ctx.error(error_msg)
            return {"error": error_msg}

    def _detect_archive_format(self, archive_path: Path) -> Optional[str]:
        """Detect archive format based on file extension and magic bytes"""
        import tarfile
        import zipfile

        suffix = archive_path.suffix.lower()
        suffixes = archive_path.suffixes

        if suffix == ".zip":
            return "zip"
        elif suffix in (".tar", ".tgz", ".tbz", ".tbz2", ".txz"):
            if suffix == ".tgz" or ".tar.gz" in " ".join(suffixes):
                return "tar.gz"
            elif suffix in (".tbz", ".tbz2") or ".tar.bz2" in " ".join(suffixes):
                return "tar.bz2"
            elif suffix == ".txz" or ".tar.xz" in " ".join(suffixes):
                return "tar.xz"
            else:
                return "tar"
        elif ".tar." in str(archive_path):
            if ".tar.gz" in str(archive_path):
                return "tar.gz"
            elif ".tar.bz2" in str(archive_path):
                return "tar.bz2"
            elif ".tar.xz" in str(archive_path):
                return "tar.xz"

        try:
            if tarfile.is_tarfile(archive_path):
                with tarfile.open(archive_path, "r:*") as tar:
                    if hasattr(tar, "mode"):
                        if "gz" in tar.mode:
                            return "tar.gz"
                        elif "bz2" in tar.mode:
                            return "tar.bz2"
                        elif "xz" in tar.mode:
                            return "tar.xz"
                return "tar"
            elif zipfile.is_zipfile(archive_path):
                return "zip"
        except Exception:
            pass

        return None
