# 🎯 mcpypi Clean Tool Interface (15 Tools)

## **✨ Primary Tools (3) - Handle 90% of Use Cases**

### 1. **`package_operations`** ⭐
Your master tool for all package-related operations.

**Usage:**
```python
package_operations("info", package_name="requests")
package_operations("dependencies", package_name="django", include_transitive=True)
package_operations("health_score", package_name="fastapi", include_github_metrics=True)
package_operations("compare_health", package_names=["django", "flask", "fastapi"])
```

**Operations:** info, versions, dependencies, resolve_dependencies, download, download_stats, download_trends, python_compatibility, compatible_versions, validate_name, preview_page, analytics, rankings, competition, recommendations, health_score, compare_health, reviews, maintainer_contacts

### 2. **`package_search`** 🔍
Universal search interface for discovering packages.

**Usage:**
```python
package_search("web framework", search_type="general")
package_search("requests", search_type="alternatives")
package_search("", search_type="trending", category="web")
package_search("gvanrossum", search_type="by_maintainer")
```

**Search Types:** general, category, alternatives, trending, top_downloaded, by_maintainer

### 3. **`security_analysis`** 🔒
Complete security and license compliance analysis.

**Usage:**
```python
security_analysis(["requests"], analysis_type="comprehensive")
security_analysis(["django", "flask"], analysis_type="bulk_scan")
security_analysis(["fastapi"], analysis_type="license")
```

**Analysis Types:** scan, bulk_scan, license, bulk_license, comprehensive

---

## **⚙️ Specialized Tools (12) - Advanced Operations**

### Publishing & Management (6)
- `upload_package_to_pypi` - Upload packages to PyPI
- `check_pypi_credentials` - Validate PyPI authentication
- `get_pypi_upload_history` - View upload history
- `delete_pypi_release` - Remove specific releases
- `manage_pypi_maintainers` - Add/remove maintainers
- `get_pypi_account_info` - Account information

### Metadata Management (3)
- `update_package_metadata` - Update package information
- `manage_package_urls` - Manage project URLs
- `set_package_visibility` - Control package visibility

### Advanced Operations (3)
- `manage_package_keywords` - SEO and discoverability
- `get_pypi_build_logs` - Build troubleshooting
- `manage_pypi_package_discussions` - Community management

---

## **🎯 Quick Reference**

**Most Common Operations:**
```python
# Get package info
package_operations("info", package_name="fastapi")

# Search for packages
package_search("machine learning", search_type="general")

# Check security
security_analysis(["django"], analysis_type="comprehensive")
```

**Publishing Workflow:**
```python
# 1. Check credentials
check_pypi_credentials("pypi")

# 2. Upload package
upload_package_to_pypi(package_path="./dist")

# 3. Manage maintainers
manage_pypi_maintainers("mypackage", "add", "username")
```

---

## **📊 Benefits of Clean Interface**

- **3 Primary Tools**: Clear starting point for new users
- **Intuitive Names**: No confusing suffixes or prefixes
- **Smart Routing**: Operations determined by parameters
- **Full Power**: All 48 original functions accessible through 15 tools
- **70% Reduction**: From 51 to 15 tools for optimal UX

The clean interface makes mcpypi feel professional, polished, and production-ready!