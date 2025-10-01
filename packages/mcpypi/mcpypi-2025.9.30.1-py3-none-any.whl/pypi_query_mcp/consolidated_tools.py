"""
🎯 Consolidated MCP Tools for mcpypi

This module provides consolidated, high-level tools that replace the granular micro-tools
with intelligent macro-tools. Each consolidated tool handles multiple related operations
through parameter-based routing.
"""

import asyncio
from typing import Any, Dict, List, Optional, Union, Literal
from enum import Enum

from .core.pypi_client import PyPIClient
from .core.exceptions import PyPIError, InvalidPackageNameError
from .security.validation import secure_validate_package_name, sanitize_for_logging


class PackageOperation(str, Enum):
    """Available package operations."""
    INFO = "info"
    VERSIONS = "versions"
    DEPENDENCIES = "dependencies"
    RESOLVE_DEPS = "resolve_dependencies"
    DOWNLOAD = "download"
    DOWNLOAD_STATS = "download_stats"
    DOWNLOAD_TRENDS = "download_trends"
    PYTHON_COMPATIBILITY = "python_compatibility"
    COMPATIBLE_VERSIONS = "compatible_versions"
    VALIDATE_NAME = "validate_name"
    PREVIEW_PAGE = "preview_page"
    ANALYTICS = "analytics"
    RANKINGS = "rankings"
    COMPETITION = "competition"
    RECOMMENDATIONS = "recommendations"
    HEALTH_SCORE = "health_score"
    COMPARE_HEALTH = "compare_health"
    REVIEWS = "reviews"
    MAINTAINER_CONTACTS = "maintainer_contacts"


class SearchType(str, Enum):
    """Available search types."""
    GENERAL = "general"
    CATEGORY = "category"
    ALTERNATIVES = "alternatives"
    TRENDING = "trending"
    TOP_DOWNLOADED = "top_downloaded"
    BY_MAINTAINER = "by_maintainer"


class SecurityAnalysisType(str, Enum):
    """Available security analysis types."""
    SCAN = "scan"
    BULK_SCAN = "bulk_scan"
    LICENSE = "license"
    BULK_LICENSE = "bulk_license"
    COMPREHENSIVE = "comprehensive"


async def package_operations_impl(
    operation: PackageOperation,
    package_name: Optional[str] = None,
    package_names: Optional[List[str]] = None,
    version: Optional[str] = None,
    include_dependencies: bool = True,
    include_transitive: bool = False,
    include_github_metrics: bool = False,
    target_python_version: Optional[str] = None,
    **kwargs: Any
) -> Dict[str, Any]:
    """
    🎯 Consolidated Package Operations Tool

    Handles all package-related operations through a single, intelligent interface.
    Replaces 28 individual micro-tools with parameter-based operation routing.

    Args:
        operation: The package operation to perform
        package_name: Single package name (for single-package operations)
        package_names: Multiple package names (for bulk operations)
        version: Specific package version (optional)
        include_dependencies: Include dependency information
        include_transitive: Include transitive dependencies
        include_github_metrics: Include GitHub repository metrics
        target_python_version: Target Python version for compatibility
        **kwargs: Additional operation-specific parameters

    Returns:
        Operation results with metadata about the performed operation

    Examples:
        # Get package info
        await package_operations("info", "requests")

        # Get dependencies with transitive
        await package_operations("dependencies", "django", include_transitive=True)

        # Health score with GitHub metrics
        await package_operations("health_score", "fastapi", include_github_metrics=True)

        # Compare health scores
        await package_operations("compare_health", package_names=["django", "flask"])
    """

    try:
        # Input validation
        if operation in [PackageOperation.COMPARE_HEALTH] and not package_names:
            raise InvalidPackageNameError("package_names required for bulk operations")

        if operation not in [PackageOperation.COMPARE_HEALTH] and not package_name:
            raise InvalidPackageNameError("package_name required for single-package operations")

        # Validate package names
        names_to_validate = []
        if package_name:
            names_to_validate.append(package_name)
        if package_names:
            names_to_validate.extend(package_names)

        for name in names_to_validate:
            validation = secure_validate_package_name(name)
            if not validation["valid"]:
                raise InvalidPackageNameError(f"Invalid package name: {validation['reason']}")

        # Get appropriate client
        client = PyPIClient()

        # Route to appropriate operation
        match operation:
            case PackageOperation.INFO:
                from .tools.package_query import query_package_info
                result = await query_package_info(package_name)

            case PackageOperation.VERSIONS:
                from .tools.package_query import query_package_versions
                result = await query_package_versions(package_name)

            case PackageOperation.DEPENDENCIES:
                from .tools.package_query import query_package_dependencies
                result = await query_package_dependencies(
                    package_name,
                    version=version,
                    include_transitive=include_transitive,
                    python_version=target_python_version,
                    **kwargs
                )

            case PackageOperation.RESOLVE_DEPS:
                from .tools.dependency_resolver import resolve_package_dependencies
                result = await resolve_package_dependencies(
                    package_name,
                    python_version=target_python_version,
                    include_dependencies=include_dependencies,
                    **kwargs
                )

            case PackageOperation.DOWNLOAD:
                from .tools.package_downloader import download_package_with_dependencies
                result = await download_package_with_dependencies(
                    package_name,
                    python_version=target_python_version,
                    include_dependencies=include_dependencies,
                    **kwargs
                )

            case PackageOperation.DOWNLOAD_STATS:
                from .tools.download_stats import get_package_download_stats
                result = await get_package_download_stats(package_name, **kwargs)

            case PackageOperation.DOWNLOAD_TRENDS:
                from .tools.download_stats import get_package_download_trends
                result = await get_package_download_trends(package_name, **kwargs)

            case PackageOperation.PYTHON_COMPATIBILITY:
                from .tools.compatibility_check import check_python_compatibility
                if not target_python_version:
                    raise InvalidPackageNameError("target_python_version required for compatibility check")
                result = await check_python_compatibility(
                    package_name,
                    target_python_version,
                    **kwargs
                )

            case PackageOperation.COMPATIBLE_VERSIONS:
                from .tools.compatibility_check import get_compatible_python_versions
                result = await get_compatible_python_versions(package_name, **kwargs)

            case PackageOperation.VALIDATE_NAME:
                from .tools.workflow import validate_package_name
                result = await validate_package_name(package_name)

            case PackageOperation.PREVIEW_PAGE:
                from .tools.publishing import preview_package_page
                result = await preview_package_page(
                    package_name,
                    version=version,
                    **kwargs
                )

            case PackageOperation.ANALYTICS:
                from .tools.analytics import get_package_analytics
                result = await get_package_analytics(
                    package_name,
                    include_historical=include_github_metrics,
                    **kwargs
                )

            case PackageOperation.RANKINGS:
                from .tools.analytics import get_package_rankings
                result = await get_package_rankings(package_name, **kwargs)

            case PackageOperation.COMPETITION:
                from .tools.analytics import analyze_competition
                result = await analyze_competition(package_name, **kwargs)

            case PackageOperation.RECOMMENDATIONS:
                from .tools.discovery import get_package_recommendations
                result = await get_package_recommendations(package_name, **kwargs)

            case PackageOperation.HEALTH_SCORE:
                from .tools.health_tools import assess_package_health_score
                result = await assess_package_health_score(
                    package_name,
                    version=version,
                    include_github_metrics=include_github_metrics
                )

            case PackageOperation.COMPARE_HEALTH:
                from .tools.health_tools import compare_packages_health_scores
                result = await compare_packages_health_scores(
                    package_names,
                    include_github_metrics=include_github_metrics
                )

            case PackageOperation.REVIEWS:
                from .tools.community import get_package_reviews
                result = await get_package_reviews(package_name, **kwargs)

            case PackageOperation.MAINTAINER_CONTACTS:
                from .tools.community import get_maintainer_contacts
                result = await get_maintainer_contacts(package_name, **kwargs)

            case _:
                raise InvalidPackageNameError(f"Unknown operation: {operation}")

        # Add operation metadata
        result["operation_metadata"] = {
            "operation": operation.value,
            "package_name": package_name,
            "package_names": package_names,
            "consolidated_tool": True,
            "tool_version": "2.0",
            "replaced_tools_count": _get_replaced_tools_count(operation)
        }

        return result

    except Exception as e:
        sanitized_error = sanitize_for_logging(str(e))
        raise PyPIError(f"Package operation '{operation}' failed: {sanitized_error}") from e


async def package_search_impl(
    query: str,
    search_type: SearchType = SearchType.GENERAL,
    limit: int = 20,
    category: Optional[str] = None,
    maintainer_name: Optional[str] = None,
    **kwargs: Any
) -> Dict[str, Any]:
    """
    🔍 Consolidated Package Search Tool

    Handles all search and discovery operations through a single interface.
    Replaces 6 individual search tools with type-based routing.

    Args:
        query: Search query string
        search_type: Type of search to perform
        limit: Maximum number of results
        category: Category filter (for category searches)
        maintainer_name: Maintainer name (for maintainer searches)
        **kwargs: Additional search-specific parameters

    Returns:
        Search results with metadata about the performed search

    Examples:
        # General search
        await package_search("web framework")

        # Category search
        await package_search("testing", search_type="category")

        # Find alternatives
        await package_search("requests", search_type="alternatives")

        # Trending packages
        await package_search("", search_type="trending")
    """

    try:
        # Route to appropriate search operation
        match search_type:
            case SearchType.GENERAL:
                from .tools.search import search_packages
                result = await search_packages(query, limit=limit, **kwargs)

            case SearchType.CATEGORY:
                from .tools.search import search_by_category
                search_category = category or query
                result = await search_by_category(
                    search_category,
                    limit=limit,
                    **kwargs
                )

            case SearchType.ALTERNATIVES:
                from .tools.search import find_alternatives
                result = await find_alternatives(query, limit=limit, **kwargs)

            case SearchType.TRENDING:
                from .tools.search import get_trending_packages
                result = await get_trending_packages(
                    category=category,
                    limit=limit,
                    **kwargs
                )

            case SearchType.TOP_DOWNLOADED:
                from .tools.download_stats import get_top_packages_by_downloads
                result = await get_top_packages_by_downloads(limit=limit, **kwargs)

            case SearchType.BY_MAINTAINER:
                from .tools.discovery import search_by_maintainer
                search_maintainer = maintainer_name or query
                result = await search_by_maintainer(
                    search_maintainer,
                    **kwargs
                )

            case _:
                raise InvalidPackageNameError(f"Unknown search type: {search_type}")

        # Add search metadata
        result["search_metadata"] = {
            "query": query,
            "search_type": search_type.value,
            "limit": limit,
            "consolidated_tool": True,
            "tool_version": "2.0",
            "replaced_tools_count": 6
        }

        return result

    except Exception as e:
        sanitized_error = sanitize_for_logging(str(e))
        raise PyPIError(f"Package search '{search_type}' failed: {sanitized_error}") from e


async def security_analysis_impl(
    package_names: List[str],
    analysis_type: SecurityAnalysisType = SecurityAnalysisType.COMPREHENSIVE,
    include_dependencies: bool = True,
    severity_filter: Optional[str] = None,
    **kwargs: Any
) -> Dict[str, Any]:
    """
    🔒 Consolidated Security Analysis Tool

    Handles all security analysis operations through a single interface.
    Replaces 4 individual security tools with type-based routing.

    Args:
        package_names: List of package names to analyze
        analysis_type: Type of security analysis to perform
        include_dependencies: Include dependency analysis
        severity_filter: Filter by severity level
        **kwargs: Additional analysis-specific parameters

    Returns:
        Security analysis results with metadata

    Examples:
        # Single package comprehensive analysis
        await security_analysis(["requests"], analysis_type="comprehensive")

        # Bulk vulnerability scan
        await security_analysis(["django", "flask"], analysis_type="bulk_scan")

        # License analysis
        await security_analysis(["fastapi"], analysis_type="license")
    """

    try:
        # Validate package names
        for name in package_names:
            validation = secure_validate_package_name(name)
            if not validation["valid"]:
                raise InvalidPackageNameError(f"Invalid package name: {validation['reason']}")

        # Route to appropriate security operation
        match analysis_type:
            case SecurityAnalysisType.SCAN:
                from .tools.security_tools import scan_package_security
                if len(package_names) != 1:
                    raise InvalidPackageNameError("Single package scan requires exactly one package name")
                result = await scan_package_security(
                    package_names[0],
                    include_dependencies=include_dependencies,
                    severity_filter=severity_filter,
                    **kwargs
                )

            case SecurityAnalysisType.BULK_SCAN:
                from .tools.security_tools import bulk_scan_package_security
                result = await bulk_scan_package_security(
                    package_names,
                    include_dependencies=include_dependencies,
                    severity_threshold=severity_filter,
                    **kwargs
                )

            case SecurityAnalysisType.LICENSE:
                from .tools.license_tools import analyze_package_license
                if len(package_names) != 1:
                    raise InvalidPackageNameError("License analysis requires exactly one package name")
                result = await analyze_package_license(
                    package_names[0],
                    include_dependencies=include_dependencies,
                    **kwargs
                )

            case SecurityAnalysisType.BULK_LICENSE:
                from .tools.license_tools import check_bulk_license_compliance
                result = await check_bulk_license_compliance(
                    package_names,
                    **kwargs
                )

            case SecurityAnalysisType.COMPREHENSIVE:
                # Run both security scan and license analysis
                tasks = []
                for package_name in package_names:
                    # Security scan
                    tasks.append(
                        security_analysis(
                            [package_name],
                            SecurityAnalysisType.SCAN,
                            include_dependencies=include_dependencies,
                            severity_filter=severity_filter
                        )
                    )
                    # License analysis
                    tasks.append(
                        security_analysis(
                            [package_name],
                            SecurityAnalysisType.LICENSE,
                            include_dependencies=include_dependencies
                        )
                    )

                results = await asyncio.gather(*tasks, return_exceptions=True)

                # Combine results
                result = {
                    "comprehensive_analysis": True,
                    "packages_analyzed": package_names,
                    "security_scans": [],
                    "license_analyses": []
                }

                for i, res in enumerate(results):
                    if isinstance(res, Exception):
                        continue
                    if i % 2 == 0:  # Security scan
                        result["security_scans"].append(res)
                    else:  # License analysis
                        result["license_analyses"].append(res)

            case _:
                raise InvalidPackageNameError(f"Unknown analysis type: {analysis_type}")

        # Add analysis metadata
        result["analysis_metadata"] = {
            "package_names": package_names,
            "analysis_type": analysis_type.value,
            "include_dependencies": include_dependencies,
            "consolidated_tool": True,
            "tool_version": "2.0",
            "replaced_tools_count": 4
        }

        return result

    except Exception as e:
        sanitized_error = sanitize_for_logging(str(e))
        raise PyPIError(f"Security analysis '{analysis_type}' failed: {sanitized_error}") from e


def _get_replaced_tools_count(operation: PackageOperation) -> int:
    """Get the number of individual tools replaced by this operation."""
    # Most operations replace 1 tool, some replace multiple
    if operation in [PackageOperation.COMPARE_HEALTH]:
        return 2  # Replaces both individual and comparison tools
    return 1


# Export consolidated tools for FastMCP registration
CONSOLIDATED_TOOLS = {
    "package_operations": package_operations_impl,
    "package_search": package_search_impl,
    "security_analysis": security_analysis_impl
}
