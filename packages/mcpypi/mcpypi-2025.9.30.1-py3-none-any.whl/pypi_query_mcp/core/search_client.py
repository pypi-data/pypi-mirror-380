"""Advanced PyPI search client with filtering, sorting, and semantic search capabilities."""

import asyncio
import logging
import re
from datetime import datetime, timezone
from typing import Any

from packaging import version as pkg_version

from .exceptions import SearchError
from .pypi_client import PyPIClient
from .rate_limiter import get_rate_limited_client

logger = logging.getLogger(__name__)


class SearchFilter:
    """Search filter configuration."""

    def __init__(
        self,
        python_versions: list[str] | None = None,
        licenses: list[str] | None = None,
        categories: list[str] | None = None,
        min_downloads: int | None = None,
        max_age_days: int | None = None,
        maintenance_status: str | None = None,  # active, maintained, stale, abandoned
        has_wheels: bool | None = None,
        min_python_version: str | None = None,
        max_python_version: str | None = None,
    ):
        self.python_versions = python_versions or []
        self.licenses = licenses or []
        self.categories = categories or []
        self.min_downloads = min_downloads
        self.max_age_days = max_age_days
        self.maintenance_status = maintenance_status
        self.has_wheels = has_wheels
        self.min_python_version = min_python_version
        self.max_python_version = max_python_version


class SearchSort:
    """Search sorting configuration."""

    POPULARITY = "popularity"
    RECENCY = "recency"
    RELEVANCE = "relevance"
    QUALITY = "quality"
    NAME = "name"
    DOWNLOADS = "downloads"

    def __init__(self, field: str = RELEVANCE, reverse: bool = True):
        self.field = field
        self.reverse = reverse


class PyPISearchClient:
    """Advanced PyPI search client with comprehensive filtering and analysis."""

    def __init__(self, timeout: float = 30.0):
        self.timeout = timeout
        self.pypi_client = None

        # Common license mappings
        self.license_aliases = {
            "mit": ["MIT", "MIT License"],
            "apache": ["Apache", "Apache 2.0", "Apache-2.0", "Apache Software License"],
            "bsd": ["BSD", "BSD License", "BSD-3-Clause", "BSD-2-Clause"],
            "gpl": ["GPL", "GNU General Public License", "GPL-3.0", "GPL-2.0"],
            "lgpl": ["LGPL", "GNU Lesser General Public License"],
            "mpl": ["MPL", "Mozilla Public License"],
            "unlicense": ["Unlicense", "Public Domain"],
        }

        # Category keywords for classification
        self.category_keywords = {
            "web": ["web", "flask", "django", "fastapi", "http", "rest", "api", "server", "wsgi", "asgi"],
            "data-science": ["data", "science", "machine", "learning", "ml", "ai", "pandas", "numpy", "scipy"],
            "database": ["database", "db", "sql", "nosql", "orm", "sqlite", "postgres", "mysql", "mongodb"],
            "testing": ["test", "testing", "pytest", "unittest", "mock", "coverage", "tox"],
            "cli": ["cli", "command", "terminal", "console", "argparse", "click"],
            "security": ["security", "crypto", "encryption", "ssl", "tls", "auth", "password"],
            "networking": ["network", "socket", "tcp", "udp", "http", "requests", "urllib"],
            "dev-tools": ["development", "tools", "build", "package", "deploy", "lint", "format"],
            "cloud": ["cloud", "aws", "azure", "gcp", "docker", "kubernetes", "serverless"],
            "gui": ["gui", "ui", "interface", "tkinter", "qt", "wx", "kivy"],
        }

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass

    async def search_packages(
        self,
        query: str,
        limit: int = 20,
        filters: SearchFilter | None = None,
        sort: SearchSort | None = None,
        semantic_search: bool = False,
    ) -> dict[str, Any]:
        """
        Search PyPI packages with advanced filtering and sorting.
        
        Args:
            query: Search query string
            limit: Maximum number of results to return
            filters: Optional search filters
            sort: Optional sort configuration
            semantic_search: Whether to use semantic search on descriptions
            
        Returns:
            Dictionary containing search results and metadata
        """
        if not query or not query.strip():
            raise SearchError("Search query cannot be empty")

        filters = filters or SearchFilter()
        sort = sort or SearchSort()

        logger.info(f"Searching PyPI for: '{query}' (limit: {limit}, semantic: {semantic_search})")

        try:
            # Use PyPI's search API as the primary source
            try:
                pypi_results = await self._search_pypi_api(query, limit * 3)  # Get more for filtering
                logger.info(f"Got {len(pypi_results)} raw results from PyPI API")
            except Exception as e:
                logger.error(f"PyPI API search failed: {e}")
                pypi_results = []

            # Enhance results with additional metadata
            try:
                enhanced_results = await self._enhance_search_results(pypi_results)
                logger.info(f"Enhanced to {len(enhanced_results)} results")
            except Exception as e:
                logger.error(f"Enhancement failed: {e}")
                enhanced_results = pypi_results

            # Apply filters
            try:
                filtered_results = self._apply_filters(enhanced_results, filters)
                logger.info(f"Filtered to {len(filtered_results)} results")
            except Exception as e:
                logger.error(f"Filtering failed: {e}")
                filtered_results = enhanced_results

            # Apply semantic search if requested
            if semantic_search:
                try:
                    filtered_results = self._apply_semantic_search(filtered_results, query)
                except Exception as e:
                    logger.error(f"Semantic search failed: {e}")

            # Sort results
            try:
                sorted_results = self._sort_results(filtered_results, sort)
            except Exception as e:
                logger.error(f"Sorting failed: {e}")
                sorted_results = filtered_results

            # Limit results
            final_results = sorted_results[:limit]

            return {
                "query": query,
                "total_found": len(pypi_results),
                "filtered_count": len(filtered_results),
                "returned_count": len(final_results),
                "packages": final_results,
                "filters_applied": self._serialize_filters(filters),
                "sort_applied": {"field": sort.field, "reverse": sort.reverse},
                "semantic_search": semantic_search,
                "timestamp": datetime.now(timezone.utc).isoformat(),
            }

        except Exception as e:
            logger.error(f"Search failed for query '{query}': {e}")
            raise SearchError(f"Search failed: {e}") from e

    async def _search_pypi_api(self, query: str, limit: int) -> list[dict[str, Any]]:
        """Search using available PyPI methods - no native search API exists."""
        logger.info(f"PyPI has no native search API, using curated search for: '{query}'")

        # PyPI doesn't have a search API, so we'll use our curated approach
        # combined with direct package lookups for exact matches
        results = []

        # First: try direct package lookup (exact match)
        try:
            direct_result = await self._try_direct_package_lookup(query)
            if direct_result:
                results.extend(direct_result)
        except Exception as e:
            logger.debug(f"Direct lookup failed: {e}")

        # Second: search curated packages
        try:
            curated_results = await self._search_curated_packages(query, limit)
            # Add curated results that aren't already in the list
            existing_names = {r["name"].lower() for r in results}
            for result in curated_results:
                if result["name"].lower() not in existing_names:
                    results.append(result)
        except Exception as e:
            logger.error(f"Curated search failed: {e}")

        return results[:limit]

    async def _try_direct_package_lookup(self, query: str) -> list[dict[str, Any]]:
        """Try to get package info directly using PyPI JSON API."""
        candidates = [
            query.strip(),
            query.strip().lower(),
            query.strip().replace(" ", "-"),
            query.strip().replace(" ", "_"),
            query.strip().replace("_", "-"),
            query.strip().replace("-", "_"),
        ]

        results = []
        for candidate in candidates:
            try:
                async with PyPIClient() as client:
                    package_data = await client.get_package_info(candidate)

                    results.append({
                        "name": package_data["info"]["name"],
                        "summary": package_data["info"]["summary"] or "",
                        "version": package_data["info"]["version"],
                        "source": "direct_api",
                        "description": package_data["info"]["description"] or "",
                        "author": package_data["info"]["author"] or "",
                        "license": package_data["info"]["license"] or "",
                        "home_page": package_data["info"]["home_page"] or "",
                        "requires_python": package_data["info"]["requires_python"] or "",
                        "classifiers": package_data["info"]["classifiers"] or [],
                        "keywords": package_data["info"]["keywords"] or "",
                    })
                    break  # Found exact match, stop looking

            except Exception:
                continue  # Try next candidate

        return results

    async def _search_curated_packages(self, query: str, limit: int) -> list[dict[str, Any]]:
        """Search our curated package database."""
        from ..data.popular_packages import ALL_POPULAR_PACKAGES

        curated_matches = []
        query_lower = query.lower()

        logger.info(f"Searching {len(ALL_POPULAR_PACKAGES)} curated packages for '{query}'")

        # First: exact name matches
        for pkg in ALL_POPULAR_PACKAGES:
            if query_lower == pkg.name.lower():
                curated_matches.append({
                    "name": pkg.name,
                    "summary": pkg.description,
                    "version": "latest",
                    "source": "curated_exact",
                    "category": pkg.category,
                    "estimated_downloads": pkg.estimated_monthly_downloads,
                    "github_stars": pkg.github_stars,
                    "primary_use_case": pkg.primary_use_case,
                })

        # Second: name contains query (if not too many exact matches)
        if len(curated_matches) < limit:
            for pkg in ALL_POPULAR_PACKAGES:
                if (query_lower in pkg.name.lower() and
                    pkg.name not in [m["name"] for m in curated_matches]):
                    curated_matches.append({
                        "name": pkg.name,
                        "summary": pkg.description,
                        "version": "latest",
                        "source": "curated_name",
                        "category": pkg.category,
                        "estimated_downloads": pkg.estimated_monthly_downloads,
                        "github_stars": pkg.github_stars,
                        "primary_use_case": pkg.primary_use_case,
                    })

        # Third: description or use case matches (if still need more results)
        if len(curated_matches) < limit:
            for pkg in ALL_POPULAR_PACKAGES:
                if ((query_lower in pkg.description.lower() or
                     query_lower in pkg.primary_use_case.lower()) and
                    pkg.name not in [m["name"] for m in curated_matches]):
                    curated_matches.append({
                        "name": pkg.name,
                        "summary": pkg.description,
                        "version": "latest",
                        "source": "curated_desc",
                        "category": pkg.category,
                        "estimated_downloads": pkg.estimated_monthly_downloads,
                        "github_stars": pkg.github_stars,
                        "primary_use_case": pkg.primary_use_case,
                    })

        # Sort by popularity (downloads)
        curated_matches.sort(key=lambda x: x.get("estimated_downloads", 0), reverse=True)

        logger.info(f"Found {len(curated_matches)} curated matches")
        return curated_matches[:limit]

    async def _fallback_search(self, query: str, limit: int) -> list[dict[str, Any]]:
        """Fallback search using PyPI JSON API and our curated data."""
        try:
            from ..data.popular_packages import (
                ALL_POPULAR_PACKAGES,
            )

            # Search in our curated packages first
            curated_matches = []
            query_lower = query.lower()

            logger.info(f"Searching in {len(ALL_POPULAR_PACKAGES)} curated packages for '{query}'")

            # First: exact name matches
            for package_info in ALL_POPULAR_PACKAGES:
                if query_lower == package_info.name.lower():
                    curated_matches.append({
                        "name": package_info.name,
                        "summary": package_info.description,
                        "version": "latest",
                        "source": "curated_exact",
                        "category": package_info.category,
                        "estimated_downloads": package_info.estimated_monthly_downloads,
                        "github_stars": package_info.github_stars,
                    })

            # Second: name contains query
            for package_info in ALL_POPULAR_PACKAGES:
                if (query_lower in package_info.name.lower() and
                    package_info.name not in [m["name"] for m in curated_matches]):
                    curated_matches.append({
                        "name": package_info.name,
                        "summary": package_info.description,
                        "version": "latest",
                        "source": "curated_name",
                        "category": package_info.category,
                        "estimated_downloads": package_info.estimated_monthly_downloads,
                        "github_stars": package_info.github_stars,
                    })

            # Third: description or use case matches
            for package_info in ALL_POPULAR_PACKAGES:
                if ((query_lower in package_info.description.lower() or
                     query_lower in package_info.primary_use_case.lower()) and
                    package_info.name not in [m["name"] for m in curated_matches]):
                    curated_matches.append({
                        "name": package_info.name,
                        "summary": package_info.description,
                        "version": "latest",
                        "source": "curated_desc",
                        "category": package_info.category,
                        "estimated_downloads": package_info.estimated_monthly_downloads,
                        "github_stars": package_info.github_stars,
                    })

            logger.info(f"Found {len(curated_matches)} curated matches")

            # If we have some matches, return them (sorted by popularity)
            if curated_matches:
                curated_matches.sort(key=lambda x: x.get("estimated_downloads", 0), reverse=True)
                return curated_matches[:limit]

            # Last resort: try direct package lookup
            logger.info("No curated matches, trying direct package lookup")
            try:
                async with PyPIClient() as client:
                    package_data = await client.get_package_info(query)
                    return [{
                        "name": package_data["info"]["name"],
                        "summary": package_data["info"]["summary"] or "",
                        "version": package_data["info"]["version"],
                        "source": "direct_fallback",
                        "description": package_data["info"]["description"] or "",
                        "author": package_data["info"]["author"] or "",
                    }]
            except Exception as e:
                logger.info(f"Direct lookup failed: {e}")

        except Exception as e:
            logger.error(f"Fallback search failed: {e}")

        return []

    async def _search_xmlrpc(self, query: str, limit: int) -> list[dict[str, Any]]:
        """Search using enhanced curated search with fuzzy matching."""
        # Since PyPI XML-RPC search is deprecated, use our enhanced curated search
        try:
            from ..data.popular_packages import (
                ALL_POPULAR_PACKAGES,
            )

            query_lower = query.lower()
            results = []

            # First pass: exact name matches
            for pkg in ALL_POPULAR_PACKAGES:
                if query_lower == pkg.name.lower():
                    results.append({
                        "name": pkg.name,
                        "summary": pkg.description,
                        "version": "latest",
                        "source": "curated_exact",
                        "category": pkg.category,
                        "estimated_downloads": pkg.estimated_monthly_downloads,
                        "github_stars": pkg.github_stars,
                    })

            # Second pass: name contains query
            for pkg in ALL_POPULAR_PACKAGES:
                if query_lower in pkg.name.lower() and pkg.name not in [r["name"] for r in results]:
                    results.append({
                        "name": pkg.name,
                        "summary": pkg.description,
                        "version": "latest",
                        "source": "curated_name",
                        "category": pkg.category,
                        "estimated_downloads": pkg.estimated_monthly_downloads,
                        "github_stars": pkg.github_stars,
                    })

            # Third pass: description contains query
            for pkg in ALL_POPULAR_PACKAGES:
                if (query_lower in pkg.description.lower() or
                    query_lower in pkg.primary_use_case.lower()) and pkg.name not in [r["name"] for r in results]:
                    results.append({
                        "name": pkg.name,
                        "summary": pkg.description,
                        "version": "latest",
                        "source": "curated_desc",
                        "category": pkg.category,
                        "estimated_downloads": pkg.estimated_monthly_downloads,
                        "github_stars": pkg.github_stars,
                    })

            # Sort by popularity (downloads)
            results.sort(key=lambda x: x.get("estimated_downloads", 0), reverse=True)

            return results[:limit]

        except Exception as e:
            logger.debug(f"Enhanced curated search error: {e}")

        return []

    async def _search_simple_api(self, query: str, limit: int) -> list[dict[str, Any]]:
        """Search using direct PyPI JSON API for specific packages."""
        try:
            # Try direct package lookup if query looks like a package name
            query_clean = query.strip().lower().replace(" ", "-")

            # Try variations of the query as package names
            candidates = [
                query_clean,
                query_clean.replace("-", "_"),
                query_clean.replace("_", "-"),
                query.strip(),  # Original query
            ]

            results = []

            for candidate in candidates:
                if len(results) >= limit:
                    break

                try:
                    async with PyPIClient() as client:
                        package_data = await client.get_package_info(candidate)

                        results.append({
                            "name": package_data["info"]["name"],
                            "summary": package_data["info"]["summary"] or "",
                            "version": package_data["info"]["version"],
                            "source": "direct_api",
                            "description": package_data["info"]["description"] or "",
                            "author": package_data["info"]["author"] or "",
                            "license": package_data["info"]["license"] or "",
                        })

                except Exception:
                    # Package doesn't exist, continue to next candidate
                    continue

            return results

        except Exception as e:
            logger.debug(f"Simple API search error: {e}")

        return []

    async def _parse_search_html(self, html: str, limit: int) -> list[dict[str, Any]]:
        """Parse PyPI search results from HTML (simplified parser)."""
        # This is a simplified parser - in production, you'd use BeautifulSoup
        # For now, return empty and rely on fallback
        return []

    async def _enhance_search_results(self, results: list[dict[str, Any]]) -> list[dict[str, Any]]:
        """Enhance search results with additional metadata from PyPI API."""
        enhanced = []

        # Skip enhancement if results already have good metadata from curated source
        if results and results[0].get("source", "").startswith("curated"):
            logger.info("Using curated results without enhancement")
            return results

        # For direct API results, they're already enhanced
        if results and results[0].get("source") == "direct_api":
            logger.info("Using direct API results without additional enhancement")
            return results

        # Process in small batches to avoid overwhelming the API
        batch_size = 3
        for i in range(0, min(len(results), 10), batch_size):  # Limit to first 10 results
            batch = results[i:i + batch_size]
            batch_tasks = [
                self._enhance_single_result(result)
                for result in batch
            ]

            enhanced_batch = await asyncio.gather(*batch_tasks, return_exceptions=True)

            for result in enhanced_batch:
                if isinstance(result, Exception):
                    logger.warning(f"Failed to enhance result: {result}")
                    continue
                if result:
                    enhanced.append(result)

        return enhanced

    async def _enhance_single_result(self, result: dict[str, Any]) -> dict[str, Any] | None:
        """Enhance a single search result with PyPI metadata."""
        try:
            async with PyPIClient() as client:
                package_data = await client.get_package_info(result["name"])
                info = package_data["info"]

                # Extract useful metadata
                enhanced = {
                    "name": info["name"],
                    "summary": info["summary"] or result.get("summary", ""),
                    "description": info["description"] or "",
                    "version": info["version"],
                    "author": info["author"] or "",
                    "license": info["license"] or "",
                    "home_page": info["home_page"] or "",
                    "project_urls": info.get("project_urls", {}),
                    "requires_python": info.get("requires_python", ""),
                    "classifiers": info.get("classifiers", []),
                    "keywords": info.get("keywords", ""),
                    "last_modified": package_data.get("last_modified", ""),
                    "download_url": info.get("download_url", ""),

                    # Derived fields
                    "categories": self._extract_categories(info),
                    "license_type": self._normalize_license(info.get("license", "")),
                    "python_versions": self._extract_python_versions(info.get("classifiers", [])),
                    "has_wheels": self._check_wheels(package_data),
                    "quality_score": self._calculate_quality_score(info, package_data),
                    "maintenance_status": self._assess_maintenance_status(package_data),
                }

                # Add original search metadata
                enhanced.update({
                    "search_source": result.get("source", "pypi"),
                    "estimated_downloads": result.get("estimated_downloads"),
                })

                return enhanced

        except Exception as e:
            logger.warning(f"Failed to enhance package {result['name']}: {e}")
            return result

    def _extract_categories(self, info: dict[str, Any]) -> list[str]:
        """Extract categories from package metadata."""
        categories = set()

        # Check classifiers
        for classifier in info.get("classifiers", []):
            if "Topic ::" in classifier:
                topic = classifier.split("Topic ::")[-1].strip()
                categories.add(topic.lower())

        # Check keywords and description
        text = f"{info.get('keywords', '')} {info.get('summary', '')} {info.get('description', '')[:500]}".lower()

        for category, keywords in self.category_keywords.items():
            if any(keyword in text for keyword in keywords):
                categories.add(category)

        return list(categories)

    def _normalize_license(self, license_text: str) -> str:
        """Normalize license text to standard types."""
        if not license_text:
            return "unknown"

        license_lower = license_text.lower()

        for license_type, aliases in self.license_aliases.items():
            if any(alias.lower() in license_lower for alias in aliases):
                return license_type

        return "other"

    def _extract_python_versions(self, classifiers: list[str]) -> list[str]:
        """Extract supported Python versions from classifiers."""
        versions = []

        for classifier in classifiers:
            if "Programming Language :: Python ::" in classifier:
                version_part = classifier.split("::")[-1].strip()
                if re.match(r"^\d+\.\d+", version_part):
                    versions.append(version_part)

        return sorted(versions, key=lambda v: pkg_version.parse(v) if v != "Implementation" else pkg_version.parse("0"))

    def _check_wheels(self, package_data: dict[str, Any]) -> bool:
        """Check if package has wheel distributions."""
        releases = package_data.get("releases", {})
        latest_version = package_data["info"]["version"]

        if latest_version in releases:
            for release in releases[latest_version]:
                if release.get("packagetype") == "bdist_wheel":
                    return True

        return False

    def _calculate_quality_score(self, info: dict[str, Any], package_data: dict[str, Any]) -> float:
        """Calculate a quality score for the package (0-100)."""
        score = 0.0

        # Documentation (25 points)
        if info.get("description") and len(info["description"]) > 100:
            score += 15
        if info.get("home_page"):
            score += 5
        if info.get("project_urls"):
            score += 5

        # Metadata completeness (25 points)
        if info.get("author"):
            score += 5
        if info.get("license"):
            score += 5
        if info.get("keywords"):
            score += 5
        if info.get("classifiers"):
            score += 10

        # Technical quality (25 points)
        if self._check_wheels(package_data):
            score += 10
        if info.get("requires_python"):
            score += 5
        if len(info.get("classifiers", [])) >= 5:
            score += 10

        # Maintenance (25 points) - simplified scoring
        if package_data.get("last_modified"):
            score += 25  # Assume recent if we have the data

        return min(score, 100.0)

    def _assess_maintenance_status(self, package_data: dict[str, Any]) -> str:
        """Assess maintenance status of the package."""
        # Simplified assessment - in production, would analyze release patterns
        version = package_data["info"]["version"]

        try:
            parsed_version = pkg_version.parse(version)
            if parsed_version.is_prerelease:
                return "development"
            elif parsed_version.major >= 1:
                return "maintained"
            else:
                return "early"
        except:
            return "unknown"

    def _apply_filters(self, results: list[dict[str, Any]], filters: SearchFilter) -> list[dict[str, Any]]:
        """Apply search filters to results."""
        filtered = []

        for result in results:
            if self._passes_filters(result, filters):
                filtered.append(result)

        return filtered

    def _passes_filters(self, result: dict[str, Any], filters: SearchFilter) -> bool:
        """Check if a result passes all filters."""

        # Python version filter
        if filters.python_versions:
            package_versions = result.get("python_versions", [])
            if not any(v in package_versions for v in filters.python_versions):
                return False

        # License filter
        if filters.licenses:
            license_type = result.get("license_type", "unknown")
            if license_type not in filters.licenses:
                return False

        # Category filter
        if filters.categories:
            package_categories = result.get("categories", [])
            if not any(cat in package_categories for cat in filters.categories):
                return False

        # Downloads filter
        if filters.min_downloads:
            downloads = result.get("estimated_downloads", 0)
            if downloads < filters.min_downloads:
                return False

        # Maintenance status filter
        if filters.maintenance_status:
            status = result.get("maintenance_status", "unknown")
            if status != filters.maintenance_status:
                return False

        # Wheels filter
        if filters.has_wheels is not None:
            has_wheels = result.get("has_wheels", False)
            if has_wheels != filters.has_wheels:
                return False

        return True

    def _apply_semantic_search(self, results: list[dict[str, Any]], query: str) -> list[dict[str, Any]]:
        """Apply semantic search scoring based on description similarity."""
        query_words = set(query.lower().split())

        for result in results:
            description = f"{result.get('summary', '')} {result.get('description', '')[:500]}"
            desc_words = set(description.lower().split())

            # Simple similarity scoring
            intersection = len(query_words & desc_words)
            union = len(query_words | desc_words)
            similarity = intersection / union if union > 0 else 0

            result["semantic_score"] = similarity

        return results

    def _sort_results(self, results: list[dict[str, Any]], sort: SearchSort) -> list[dict[str, Any]]:
        """Sort search results by specified criteria."""

        def sort_key(result):
            if sort.field == SearchSort.POPULARITY:
                return result.get("estimated_downloads", 0)
            elif sort.field == SearchSort.QUALITY:
                return result.get("quality_score", 0)
            elif sort.field == SearchSort.NAME:
                return result.get("name", "").lower()
            elif sort.field == SearchSort.DOWNLOADS:
                return result.get("estimated_downloads", 0)
            elif sort.field == SearchSort.RELEVANCE:
                return result.get("semantic_score", 0)
            elif sort.field == SearchSort.RECENCY:
                # Would need to parse last_modified for true recency
                return result.get("version", "0")
            else:
                return 0

        return sorted(results, key=sort_key, reverse=sort.reverse)

    def _serialize_filters(self, filters: SearchFilter) -> dict[str, Any]:
        """Serialize filters for response metadata."""
        return {
            "python_versions": filters.python_versions,
            "licenses": filters.licenses,
            "categories": filters.categories,
            "min_downloads": filters.min_downloads,
            "max_age_days": filters.max_age_days,
            "maintenance_status": filters.maintenance_status,
            "has_wheels": filters.has_wheels,
            "min_python_version": filters.min_python_version,
            "max_python_version": filters.max_python_version,
        }


