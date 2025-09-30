#!/usr/bin/env python3
"""
Test script for archive operations functionality
Tests create_archive, extract_archive, list_archive, and compress_file
"""

import asyncio
import shutil
import tempfile
from pathlib import Path

from enhanced_mcp.archive_compression import ArchiveCompression


async def test_archive_operations():
    """Test the archive operations with various formats"""

    # Initialize the archive operations class
    archive_ops = ArchiveCompression()

    # Create a temporary directory for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        print(f"Testing in temporary directory: {temp_path}")

        # Create some test files
        test_files_dir = temp_path / "test_files"
        test_files_dir.mkdir()

        # Create test content
        (test_files_dir / "test1.txt").write_text("This is test file 1\nWith multiple lines\n")
        (test_files_dir / "test2.py").write_text("# Python test file\nprint('Hello, World!')\n")

        subdir = test_files_dir / "subdir"
        subdir.mkdir()
        (subdir / "nested.txt").write_text("This is a nested file\n")

        # Test different archive formats
        formats_to_test = ["tar", "tar.gz", "tgz", "tar.bz2", "tar.xz", "zip"]

        for archive_format in formats_to_test:
            print(f"\n=== Testing {archive_format} format ===")

            # 1. Create archive
            archive_path = temp_path / f"test_archive.{archive_format}"
            print(f"Creating archive: {archive_path}")

            result = await archive_ops.create_archive(
                source_paths=[str(test_files_dir)],
                output_path=str(archive_path),
                format=archive_format,
                exclude_patterns=["*.tmp", "__pycache__"],
                compression_level=6,
            )

            if "error" in result:
                print(f"❌ Error creating archive: {result['error']}")
                continue

            print("✅ Archive created successfully:")
            print(f"   Files: {result['files_count']}")
            print(f"   Original size: {result['total_size_bytes']} bytes")
            print(f"   Compressed size: {result['compressed_size_bytes']} bytes")
            print(f"   Compression ratio: {result['compression_ratio_percent']}%")

            # 2. List archive contents
            print("\nListing archive contents:")
            list_result = await archive_ops.list_archive(
                archive_path=str(archive_path), detailed=True
            )

            if "error" in list_result:
                print(f"❌ Error listing archive: {list_result['error']}")
                continue

            print(f"✅ Archive contains {list_result['total_files']} items:")
            for item in list_result["contents"][:5]:  # Show first 5 items
                print(f"   {item['type']}: {item['name']} ({item['size']} bytes)")

            # 3. Extract archive
            extract_dir = temp_path / f"extracted_{archive_format.replace('.', '_')}"
            print(f"\nExtracting archive to: {extract_dir}")

            extract_result = await archive_ops.extract_archive(
                archive_path=str(archive_path),
                destination=str(extract_dir),
                overwrite=True,
                preserve_permissions=True,
            )

            if "error" in extract_result:
                print(f"❌ Error extracting archive: {extract_result['error']}")
                continue

            print(f"✅ Extracted {extract_result['files_extracted']} files")

            # Verify extracted files exist
            extracted_test1 = extract_dir / "test_files" / "test1.txt"
            if extracted_test1.exists():
                content = extracted_test1.read_text()
                print(f"   Verified content: {content.strip()}")
            else:
                print("❌ Extracted file not found")

        # Test individual file compression
        print("\n=== Testing individual file compression ===")
        test_file = test_files_dir / "test1.txt"
        algorithms = ["gzip", "bzip2", "xz"]

        for algorithm in algorithms:
            print(f"\nTesting {algorithm} compression:")

            compress_result = await archive_ops.compress_file(
                file_path=str(test_file),
                algorithm=algorithm,
                compression_level=6,
                keep_original=True,
            )

            if "error" in compress_result:
                print(f"❌ Error compressing file: {compress_result['error']}")
                continue

            print(f"✅ Compressed with {algorithm}:")
            print(f"   Original: {compress_result['original_size_bytes']} bytes")
            print(f"   Compressed: {compress_result['compressed_size_bytes']} bytes")
            print(f"   Ratio: {compress_result['compression_ratio_percent']}%")

            # Verify compressed file exists
            compressed_file = Path(compress_result["compressed_file"])
            if compressed_file.exists():
                print(f"   File created: {compressed_file.name}")
            else:
                print("❌ Compressed file not found")

        print("\n🎉 All archive operation tests completed!")


if __name__ == "__main__":
    asyncio.run(test_archive_operations())
