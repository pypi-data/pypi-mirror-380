import contextlib
import sys
from enum import Enum
from functools import lru_cache as cached
from pathlib import Path

from .log import mklog

log = mklog("mtb.core.context")


class Context(Enum):
    """Small utility class to identify the context of the current execution."""

    STANDALONE = 1
    NUKE = 2
    BLENDER = 3
    HOUDINI = 4
    UNKNOWN = 400


@cached(maxsize=1)
def get_context() -> tuple[Context, Path]:
    """Get the context of the current execution."""
    exe_path = Path(sys.executable)

    with contextlib.suppress(ImportError):
        import nuke

        dir(nuke)
        log.debug(f"Running in nuke context: {exe_path}")
        return (Context.NUKE, exe_path)
    with contextlib.suppress(ImportError):
        import hou

        dir(hou)
        log.debug(f"Running in houdini context: {exe_path}")
        return (Context.HOUDINI, exe_path)

    with contextlib.suppress(ImportError):
        import bpy

        exe_path = Path(bpy.app.binary_path_python)
        log.debug(f"Running in blender context: {exe_path}")
        return (Context.BLENDER, exe_path)

    if "python" in exe_path.stem.lower():
        log.debug(f"Running in standalone mode: {exe_path}")
        return (Context.STANDALONE, exe_path)

    return (Context.UNKNOWN, exe_path)
