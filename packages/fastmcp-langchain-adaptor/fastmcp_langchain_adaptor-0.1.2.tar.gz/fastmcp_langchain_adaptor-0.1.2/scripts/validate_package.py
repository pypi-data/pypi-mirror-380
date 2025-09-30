#!/usr/bin/env python3
"""
Package validation script for fastmcp-langchain-adaptor.

This script runs comprehensive checks to ensure the package is ready for release.
"""

import shlex
import subprocess
import sys
from pathlib import Path


def run_command(cmd: str, description: str) -> bool:
    """Run a command and return True if successful."""
    print(f"\n🔍 {description}...")
    try:
        # Use shlex.split for safer command parsing that handles quotes and escaping
        cmd_parts = shlex.split(cmd)
        subprocess.run(
            cmd_parts, check=True, capture_output=True, text=True, shell=False
        )
        print(f"✅ {description} passed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"Command: {cmd}")
        print(f"Return code: {e.returncode}")
        print(f"Stdout: {e.stdout}")
        print(f"Stderr: {e.stderr}")
        return False


def check_file_exists(file_path: str) -> bool:
    """Check if a required file exists."""
    if Path(file_path).exists():
        print(f"✅ {file_path} exists")
        return True
    else:
        print(f"❌ {file_path} is missing")
        return False


def main():
    """Run all validation checks."""
    print("🚀 FastMCP LangChain Adaptor - Package Validation")
    print("=" * 60)

    checks = []

    # Check required files
    print("\n📄 Checking required files...")
    required_files = [
        "pyproject.toml",
        "README.md",
        "LICENSE",
        "CHANGELOG.md",
        "SECURITY.md",
        "CONTRIBUTING.md",
        "fastmcp_langchain_adaptor/__init__.py",
        "fastmcp_langchain_adaptor/tools.py",
        "tests/test_tools.py",
        "tests/conftest.py",
    ]

    for file_path in required_files:
        checks.append(check_file_exists(file_path))

    # Code quality checks
    print("\n🧹 Running code quality checks...")
    quality_checks = [
        ("uv run black --check .", "Code formatting (Black)"),
        ("uv run ruff check .", "Linting (Ruff)"),
        ("uv run mypy fastmcp_langchain_adaptor/", "Type checking (MyPy)"),
    ]

    for cmd, desc in quality_checks:
        checks.append(run_command(cmd, desc))

    # Security checks
    print("\n🔒 Running security checks...")
    security_checks = [
        ("uv run bandit -r fastmcp_langchain_adaptor/", "Security linting (Bandit)"),
        ("uv run safety check", "Dependency vulnerability check (Safety)"),
    ]

    for cmd, desc in security_checks:
        checks.append(run_command(cmd, desc))

    # Tests
    print("\n🧪 Running tests...")
    test_checks = [
        ("uv run pytest --tb=short", "Unit tests"),
        (
            "uv run pytest --cov=fastmcp_langchain_adaptor --cov-fail-under=80",
            "Test coverage (≥80%)",
        ),
    ]

    for cmd, desc in test_checks:
        checks.append(run_command(cmd, desc))

    # Package build
    print("\n📦 Building package...")
    build_checks = [
        ("uv build", "Package build"),
        ("uv run twine check dist/*", "Package validation"),
    ]

    for cmd, desc in build_checks:
        checks.append(run_command(cmd, desc))

    # Summary
    print("\n" + "=" * 60)
    passed = sum(checks)
    total = len(checks)

    if passed == total:
        print(f"🎉 All {total} checks passed! Package is ready for release.")
        print("\nNext steps:")
        print("1. Create a new tag: git tag v0.1.0")
        print("2. Push the tag: git push origin v0.1.0")
        print("3. GitHub Actions will automatically build and publish to PyPI")
        sys.exit(0)
    else:
        print(
            f"💥 {total - passed}/{total} checks failed. Please fix the issues above."
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
