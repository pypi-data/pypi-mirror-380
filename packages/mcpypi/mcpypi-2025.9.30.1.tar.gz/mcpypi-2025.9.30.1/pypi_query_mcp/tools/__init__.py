"""MCP tools for PyPI package queries.

This package contains the FastMCP tool implementations that provide
the user-facing interface for PyPI package operations.
"""

from .analytics import (
    analyze_competition,
    get_package_analytics,
    get_package_rankings,
    get_security_alerts,
)
from .community import (
    get_maintainer_contacts,
    get_package_reviews,
)
from .compatibility_check import (
    check_python_compatibility,
    get_compatible_python_versions,
    suggest_python_version_for_packages,
)
from .dependency_resolver import resolve_package_dependencies
from .discovery import (
    get_package_recommendations,
    get_trending_today,
    monitor_new_releases,
    search_by_maintainer,
)
from .download_stats import (
    get_package_download_stats,
    get_package_download_trends,
    get_top_packages_by_downloads,
)
from .health_tools import (
    assess_package_health_score,
    compare_packages_health_scores,
)
from .license_tools import (
    analyze_package_license,
    check_bulk_license_compliance,
)
from .metadata import (
    manage_package_keywords,
    manage_package_urls,
    set_package_visibility,
    update_package_metadata,
)
from .package_downloader import download_package_with_dependencies
from .package_query import (
    query_package_dependencies,
    query_package_info,
    query_package_versions,
)
from .publishing import (
    check_credentials,
    delete_release,
    get_account_info,
    get_upload_history,
    manage_maintainers,
    upload_package,
)
from .requirements_tools import (
    analyze_requirements_file_tool,
    compare_multiple_requirements_files,
)
from .search import (
    find_alternatives,
    get_trending_packages,
    search_by_category,
    search_packages,
)
# Security tools removed - using consolidated tools instead
from .workflow import (
    check_upload_requirements,
    get_build_logs,
    preview_package_page,
    validate_package_name,
)

__all__ = [
    # Core package tools
    "query_package_info",
    "query_package_versions",
    "query_package_dependencies",
    "check_python_compatibility",
    "get_compatible_python_versions",
    "suggest_python_version_for_packages",
    "resolve_package_dependencies",
    "download_package_with_dependencies",
    "get_package_download_stats",
    "get_package_download_trends",
    "get_top_packages_by_downloads",
    # Search tools
    "search_packages",
    "search_by_category",
    "find_alternatives",
    "get_trending_packages",
    # Publishing tools
    "upload_package",
    "check_credentials",
    "get_upload_history",
    "delete_release",
    "manage_maintainers",
    "get_account_info",
    # Metadata tools
    "update_package_metadata",
    "manage_package_urls",
    "set_package_visibility",
    "manage_package_keywords",
    # Analytics tools
    "get_package_analytics",
    "get_security_alerts",
    "get_package_rankings",
    "analyze_competition",
    # Discovery tools
    "monitor_new_releases",
    "get_trending_today",
    "search_by_maintainer",
    "get_package_recommendations",
    # Workflow tools
    "validate_package_name",
    "preview_package_page",
    "check_upload_requirements",
    "get_build_logs",
    # Community tools
    "get_package_reviews",
    "manage_package_discussions",
    "get_maintainer_contacts",
    # Security tools
    "scan_package_security",
    "bulk_scan_package_security",
    # License tools
    "analyze_package_license",
    "check_bulk_license_compliance",
    # Health tools
    "assess_package_health_score",
    "compare_packages_health_scores",
    # Requirements tools
    "analyze_requirements_file_tool",
    "compare_multiple_requirements_files",
]
