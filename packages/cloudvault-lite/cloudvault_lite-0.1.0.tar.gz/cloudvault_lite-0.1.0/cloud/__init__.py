# cloud/__init__.py
"""
CloudVault distribution package entrypoint.

This package bundles the server-side SaaS helpers (wrappers, tokens, routes) that
integrate with ContextVault. The package name published to PyPI is 'cloudvault'
(see pyproject.toml).
"""

__all__ = ["wrappers", "app"]
__version__ = "0.1.0"
