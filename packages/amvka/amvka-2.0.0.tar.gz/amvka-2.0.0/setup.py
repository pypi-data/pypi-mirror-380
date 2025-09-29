"""Minimal legacy shim.

The project is defined in pyproject.toml (PEP 621). This file remains only for
old tooling that insists on importing setup.py. It intentionally provides no
metadata; setuptools will fall back to pyproject.toml.

Safe to delete once all environments use modern build frontends.
"""

from setuptools import setup  # type: ignore

if __name__ == "__main__":  # pragma: no cover
    setup()