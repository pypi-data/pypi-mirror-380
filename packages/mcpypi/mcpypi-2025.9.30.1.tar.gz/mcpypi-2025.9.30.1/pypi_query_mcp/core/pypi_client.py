"""PyPI API client for package information retrieval."""

import asyncio
import logging
import re
from typing import Any
from urllib.parse import quote

import httpx

from .exceptions import (
    InvalidPackageNameError,
    NetworkError,
    PackageNotFoundError,
    PyPIServerError,
    RateLimitError,
)
from .rate_limiter import get_rate_limited_client

logger = logging.getLogger(__name__)


class PyPIClient:
    """Async client for PyPI JSON API."""

    def __init__(
        self,
        base_url: str = "https://pypi.org/pypi",
        timeout: float = 30.0,
        max_retries: int = 3,
        retry_delay: float = 1.0,
    ):
        """Initialize PyPI client.

        Args:
            base_url: Base URL for PyPI API
            timeout: Request timeout in seconds
            max_retries: Maximum number of retry attempts
            retry_delay: Delay between retries in seconds
        """
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.max_retries = max_retries
        self.retry_delay = retry_delay

        # Simple in-memory cache
        self._cache: dict[str, dict[str, Any]] = {}
        self._cache_ttl = 300  # 5 minutes

        # Use rate-limited HTTP client for PyPI API
        self._client = get_rate_limited_client("pypi")

    async def __aenter__(self):
        """Async context manager entry."""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.close()

    async def close(self):
        """Close the HTTP client."""
        await self._client.close()

    def _validate_package_name(self, package_name: str) -> str:
        """Validate and normalize package name.

        Args:
            package_name: Package name to validate

        Returns:
            Normalized package name

        Raises:
            InvalidPackageNameError: If package name is invalid
        """
        if not package_name or not package_name.strip():
            raise InvalidPackageNameError(package_name)

        # Normalize package name (convert to lowercase, replace _ with -)
        normalized = re.sub(r"[-_.]+", "-", package_name.lower())

        # Basic validation - package names should contain only alphanumeric, hyphens, dots, underscores
        if not re.match(r"^[a-zA-Z0-9]([a-zA-Z0-9._-]*[a-zA-Z0-9])?$", package_name):
            raise InvalidPackageNameError(package_name)

        return normalized

    def _get_cache_key(self, package_name: str, endpoint: str = "info") -> str:
        """Generate cache key for package data."""
        return f"{endpoint}:{package_name}"

    def _is_cache_valid(self, cache_entry: dict[str, Any]) -> bool:
        """Check if cache entry is still valid."""
        import time

        return time.time() - cache_entry.get("timestamp", 0) < self._cache_ttl

    async def _make_request(self, url: str) -> dict[str, Any]:
        """Make HTTP request with retry logic.

        Args:
            url: URL to request

        Returns:
            JSON response data

        Raises:
            NetworkError: For network-related errors
            PackageNotFoundError: When package is not found
            RateLimitError: When rate limit is exceeded
            PyPIServerError: For server errors
        """
        last_exception = None

        for attempt in range(self.max_retries + 1):
            try:
                logger.debug(f"Making request to {url} (attempt {attempt + 1})")

                response = await self._client.get(url)

                # Handle different HTTP status codes
                if response.status_code == 200:
                    return response.json()
                elif response.status_code == 404:
                    # Extract package name from URL for better error message
                    package_name = url.split("/")[-2] if "/" in url else "unknown"
                    raise PackageNotFoundError(package_name)
                elif response.status_code == 429:
                    retry_after = response.headers.get("Retry-After")
                    retry_after_int = int(retry_after) if retry_after else None
                    raise RateLimitError(retry_after_int)
                elif response.status_code >= 500:
                    raise PyPIServerError(response.status_code)
                else:
                    raise PyPIServerError(
                        response.status_code,
                        f"Unexpected status code: {response.status_code}",
                    )

            except httpx.TimeoutException as e:
                last_exception = NetworkError(f"Request timeout: {e}", e)
            except httpx.NetworkError as e:
                last_exception = NetworkError(f"Network error: {e}", e)
            except (PackageNotFoundError, RateLimitError, PyPIServerError):
                # Don't retry these errors
                raise
            except Exception as e:
                last_exception = NetworkError(f"Unexpected error: {e}", e)

            # Wait before retry (except on last attempt)
            if attempt < self.max_retries:
                await asyncio.sleep(
                    self.retry_delay * (2**attempt)
                )  # Exponential backoff

        # If we get here, all retries failed
        raise last_exception

    async def get_package_info(
        self, package_name: str, version: str | None = None, use_cache: bool = True
    ) -> dict[str, Any]:
        """Get comprehensive package information from PyPI.

        Args:
            package_name: Name of the package to query
            version: Specific version to query (optional, defaults to latest)
            use_cache: Whether to use cached data if available

        Returns:
            Dictionary containing package information

        Raises:
            InvalidPackageNameError: If package name is invalid
            PackageNotFoundError: If package is not found or version doesn't exist
            NetworkError: For network-related errors
        """
        normalized_name = self._validate_package_name(package_name)

        # Create cache key that includes version info
        cache_suffix = f"v{version}" if version else "latest"
        cache_key = self._get_cache_key(normalized_name, f"info_{cache_suffix}")

        # Check cache first
        if use_cache and cache_key in self._cache:
            cache_entry = self._cache[cache_key]
            if self._is_cache_valid(cache_entry):
                logger.debug(
                    f"Using cached data for package: {normalized_name} version: {version or 'latest'}"
                )
                return cache_entry["data"]

        # Build URL - include version if specified
        if version:
            url = f"{self.base_url}/{quote(normalized_name)}/{quote(version)}/json"
            logger.info(
                f"Fetching package info for: {normalized_name} version {version}"
            )
        else:
            url = f"{self.base_url}/{quote(normalized_name)}/json"
            logger.info(f"Fetching package info for: {normalized_name} (latest)")

        try:
            data = await self._make_request(url)

            # Cache the result
            import time

            self._cache[cache_key] = {"data": data, "timestamp": time.time()}

            return data

        except PackageNotFoundError as e:
            if version:
                # More specific error message for version not found
                logger.error(
                    f"Version {version} not found for package {normalized_name}"
                )
                raise PackageNotFoundError(
                    f"Version {version} not found for package {normalized_name}"
                )
            else:
                logger.error(f"Failed to fetch package info for {normalized_name}: {e}")
                raise
        except Exception as e:
            logger.error(
                f"Failed to fetch package info for {normalized_name} version {version or 'latest'}: {e}"
            )
            raise

    async def get_package_versions(
        self, package_name: str, use_cache: bool = True
    ) -> list[str]:
        """Get list of available versions for a package.

        Args:
            package_name: Name of the package to query
            use_cache: Whether to use cached data if available

        Returns:
            List of version strings
        """
        package_info = await self.get_package_info(
            package_name, version=None, use_cache=use_cache
        )
        releases = package_info.get("releases", {})
        return list(releases.keys())

    async def get_latest_version(
        self, package_name: str, use_cache: bool = True
    ) -> str:
        """Get the latest version of a package.

        Args:
            package_name: Name of the package to query
            use_cache: Whether to use cached data if available

        Returns:
            Latest version string
        """
        package_info = await self.get_package_info(
            package_name, version=None, use_cache=use_cache
        )
        return package_info.get("info", {}).get("version", "")

    def clear_cache(self):
        """Clear the internal cache."""
        self._cache.clear()
        logger.debug("Cache cleared")
