# cloud/contextvault_shim.py
"""
Shim: make the installed PyPI `contextvault` package accessible under
`cloud.contextvault`.

This lets code that imports `cloud.contextvault` work seamlessly,
while the real implementation is provided by the PyPI package.
"""

from importlib import import_module, util

if util.find_spec("contextvault") is not None:
    contextvault = import_module("contextvault")
