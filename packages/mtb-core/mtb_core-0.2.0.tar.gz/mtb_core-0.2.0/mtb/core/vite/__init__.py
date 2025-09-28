"""Module to make working with Vite x Python easier."""

from contextlib import suppress

_FASTAPI_INSTALLED = False

with suppress(ImportError):
    from fastapi import FastAPI

    _FASTAPI_INSTALLED = True


if _FASTAPI_INSTALLED:
    from .fast_api import ViteManagerFastAPI as ViteManager
else:
    from .manager import ViteManager


__all__ = ["ViteManager"]
