"""FastMCP server for PyPI package queries - Clean interface with consolidated tools.

This server provides the streamlined interface through consolidated macro-tools.
"""

import logging
import os
from datetime import datetime, timezone
from typing import Any

import click
from fastmcp import FastMCP

from .consolidated_tools import (
    package_operations_impl,
    package_search_impl,
    security_analysis_impl,
    PackageOperation,
    SearchType,
    SecurityAnalysisType,
)

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Create FastMCP application
mcp = FastMCP("PyPI Query MCP Server")


# ============================================================================
# PRIMARY CONSOLIDATED TOOLS (3) - Clean Interface
# ============================================================================

@mcp.tool()
async def package_operations(
    operation: str,
    package_name: str = None,
    package_names: list[str] = None,
    version: str = None,
    include_dependencies: bool = True,
    include_transitive: bool = False,
    include_github_metrics: bool = False,
    target_python_version: str = None,
) -> dict[str, Any]:
    """
    🎯 **PACKAGE OPERATIONS** - Master tool for all package operations!

    **Available Operations:**
    • **info** - Get comprehensive package information
    • **versions** - List all available package versions
    • **dependencies** - Analyze package dependencies (with transitive support)
    • **resolve_dependencies** - Full dependency resolution with conflict detection
    • **download** - Download package with all dependencies
    • **download_stats** - Get download statistics and trends
    • **download_trends** - Detailed download trend analysis over time
    • **python_compatibility** - Check Python version compatibility
    • **compatible_versions** - Get all compatible Python versions
    • **validate_name** - Validate package name against PyPI rules
    • **preview_page** - Preview how package will look on PyPI
    • **analytics** - Comprehensive package analytics and metrics
    • **rankings** - Package ranking and popularity analysis
    • **competition** - Competitive landscape analysis
    • **recommendations** - Get package recommendations based on usage
    • **health_score** - Comprehensive package health assessment
    • **compare_health** - Compare health scores across multiple packages
    • **reviews** - Community reviews and sentiment analysis
    • **maintainer_contacts** - Find maintainer contact information

    **Examples:**
    ```python
    # Get package info
    package_operations("info", package_name="requests")

    # Deep dependency analysis with transitive deps
    package_operations("dependencies", package_name="django",
                      include_transitive=True, target_python_version="3.11")

    # Health score with GitHub metrics
    package_operations("health_score", package_name="fastapi",
                      include_github_metrics=True)

    # Compare multiple packages
    package_operations("compare_health",
                      package_names=["django", "flask", "fastapi"])
    ```
    """
    operation_enum = PackageOperation(operation)
    return await package_operations_impl(
        operation=operation_enum,
        package_name=package_name,
        package_names=package_names,
        version=version,
        include_dependencies=include_dependencies,
        include_transitive=include_transitive,
        include_github_metrics=include_github_metrics,
        target_python_version=target_python_version,
    )


@mcp.tool()
async def package_search(
    query: str,
    search_type: str = "general",
    limit: int = 20,
    category: str = None,
    maintainer_name: str = None,
) -> dict[str, Any]:
    """
    🔍 **PACKAGE SEARCH** - Universal search interface for PyPI packages!

    **Available Search Types:**
    • **general** - General PyPI package search with advanced filters
    • **category** - Search within specific categories (web, data-science, testing, etc.)
    • **alternatives** - Find alternative packages to a given package
    • **trending** - Get currently trending packages (hot right now!)
    • **top_downloaded** - Most downloaded packages (popularity ranking)
    • **by_maintainer** - Find all packages by a specific maintainer/author

    **Examples:**
    ```python
    # General search with filters
    package_search("machine learning", search_type="general", limit=10)

    # Category-specific search
    package_search("testing", search_type="category")

    # Find alternatives to existing packages
    package_search("requests", search_type="alternatives")

    # What's trending in Python?
    package_search("", search_type="trending", category="web")

    # Packages by maintainer
    package_search("gvanrossum", search_type="by_maintainer")
    ```
    """
    search_type_enum = SearchType(search_type)
    return await package_search_impl(
        query=query,
        search_type=search_type_enum,
        limit=limit,
        category=category,
        maintainer_name=maintainer_name,
    )


@mcp.tool()
async def security_analysis(
    package_names: list[str],
    analysis_type: str = "comprehensive",
    include_dependencies: bool = True,
    severity_filter: str = None,
) -> dict[str, Any]:
    """
    🔒 **SECURITY ANALYSIS** - Complete security intelligence!

    **Available Analysis Types:**
    • **scan** - Individual package vulnerability scan (CVE database check)
    • **bulk_scan** - Bulk vulnerability scanning across multiple packages
    • **license** - License compatibility analysis and risk assessment
    • **bulk_license** - Bulk license compliance checking
    • **comprehensive** - Full security + license analysis (RECOMMENDED)

    **Key Features:**
    • CVE database integration (GHSA, OSV, NVD)
    • Dependency vulnerability scanning
    • License compatibility analysis
    • SPDX license normalization
    • Risk scoring and prioritization
    • Actionable remediation recommendations

    **Examples:**
    ```python
    # Comprehensive security analysis (recommended)
    security_analysis(["requests"], analysis_type="comprehensive")

    # Bulk vulnerability scan for your project
    security_analysis(["django", "flask", "sqlalchemy"],
                     analysis_type="bulk_scan", severity_filter="high")

    # License compliance check
    security_analysis(["fastapi", "pydantic"],
                     analysis_type="bulk_license")

    # Deep scan with dependencies
    security_analysis(["tensorflow"], analysis_type="scan",
                     include_dependencies=True)
    ```
    """
    analysis_type_enum = SecurityAnalysisType(analysis_type)
    return await security_analysis_impl(
        package_names=package_names,
        analysis_type=analysis_type_enum,
        include_dependencies=include_dependencies,
        severity_filter=severity_filter,
    )


# ============================================================================
# ZEN TOOL
# ============================================================================

@mcp.tool()
async def zen_of_python() -> dict[str, Any]:
    """Display the Zen of Python with current user attribution."""
    try:
        current_user = os.getenv("USER") or os.getenv("USERNAME") or "pythoneer"
        zen_text = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

        return {
            "zen": zen_text,
            "attributed_to": current_user,
            "message": f"🧘‍♂️ The Zen of Python, as appreciated by {current_user}",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "fun_fact": "The 'this' module contains the famous Zen of Python easter egg!"
        }
    except Exception as e:
        return {
            "error": str(e),
            "error_type": type(e).__name__,
            "message": "Failed to achieve enlightenment 😅"
        }


# ============================================================================
# SERVER STARTUP
# ============================================================================

@click.command()
@click.option(
    "--log-level",
    default="INFO",
    type=click.Choice(["DEBUG", "INFO", "WARNING", "ERROR"]),
    help="Logging level",
)
def main(log_level: str) -> None:
    """Start the PyPI Query MCP Server."""
    # Set logging level
    logging.getLogger().setLevel(getattr(logging, log_level))

    # Show package version in startup banner
    try:
        from importlib.metadata import version
        package_version = version("mcpypi")
    except:
        package_version = "1.0.0"

    print(f"🎬 MCPyPI v{package_version} - PyPI Query MCP Server")
    logger.info("Starting PyPI Query MCP Server with ultra-clean interface")
    logger.info(f"Package version: {package_version}")
    logger.info(f"Log level set to: {log_level}")
    logger.info("✨ 3 consolidated tools provide 95% of functionality")
    logger.info("🎯 1 zen tool for Python enlightenment")
    logger.info("📉 92% tool reduction: 51 → 4 tools for optimal UX")

    # Run the FastMCP server (uses STDIO transport by default)
    mcp.run()


if __name__ == "__main__":
    main()