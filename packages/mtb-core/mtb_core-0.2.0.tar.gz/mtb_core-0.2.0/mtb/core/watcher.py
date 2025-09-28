"""Robust file-system watcher utilities.

This module provides a Watcher class that wraps watchdog to provide:
 - typed, documented API
 - debounce/coalescing of rapid duplicate events
 - glob / extension filtering
 - multiple callbacks
 - context-manager lifecycle
"""

from __future__ import annotations

import fnmatch
import logging
from collections.abc import Callable, Iterable
from pathlib import Path
from threading import Timer
from typing import Any

from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer

log = logging.getLogger(__name__)


class _DebouncedHandler(FileSystemEventHandler):
    """Internal handler which debounces rapid events and dispatches to callbacks."""

    def __init__(
        self,
        callbacks: list[Callable[[FileSystemEvent], None]],
        patterns: Iterable[str] | None = None,
        debounce: float = 0.1,
    ) -> None:
        # keep a reference to the callback list so add/remove on the manager
        # are immediately visible to the handler
        self._callbacks = callbacks
        self._patterns = list(patterns) if patterns else []
        self._debounce = float(debounce)
        self._timers: dict[str, Timer] = {}

    def _match(self, src_path: str) -> bool:
        """Check if the src_path matches any of the patterns.

        If a pattern looks like a basename glob (does not contain a path
        separator) we match against the basename, otherwise we match the
        full path. This allows patterns such as ('*.txt',) to work with
        absolute paths returned by watchdog.
        """
        if not self._patterns:
            return True
        p = Path(src_path)
        for pat in self._patterns:
            if ("/" in pat) or ("\\" in pat):
                if fnmatch.fnmatch(src_path, pat):
                    return True
            else:
                if fnmatch.fnmatch(p.name, pat):
                    return True
        return False

    def _dispatch(self, event: FileSystemEvent) -> None:
        """Dispatch the event to all registered callbacks."""
        for cb in list(self._callbacks):
            try:
                cb(event)
            except Exception:
                log.exception("Watcher callback raised an exception")

    def on_any_event(self, event: FileSystemEvent) -> None:
        """Handle any event by dispatching it to the registered callbacks."""
        # ignore directory events
        log.debug(
            "Raw watcher event: %s %s",
            getattr(event, "event_type", None),
            getattr(event, "src_path", None),
        )
        if getattr(event, "is_directory", False):
            return
        src = str(event.src_path)
        if not self._match(src):
            return

        # debounce: replace any existing timer for this path
        timer = self._timers.get(src)
        if timer is not None:
            timer.cancel()

        def _run() -> None:
            self._timers.pop(src, None)
            log.debug("Dispatching event for %s", src)
            self._dispatch(event)

        t = Timer(self._debounce, _run)
        self._timers[src] = t
        t.daemon = True
        t.start()


class Watcher:
    """High-level file watcher.

    Parameters
    ----------
    path: str | Path
        Directory to watch.
    patterns: Iterable[str] | None
        Optional glob patterns to filter files (e.g., ('*.py', '*.txt')). If
        None, all non-directory events are passed through.
    debounce: float
        Seconds to coalesce rapid events for the same path.
    observer_cls: type
        Observer implementation to use (defaults to watchdog.observers.Observer).
    recursive: bool
        Whether to watch directories recursively.
    """

    def __init__(
        self,
        path: str | Path,
        *,
        patterns: Iterable[str] | None = None,
        debounce: float = 0.1,
        observer_factory: Callable[[], Any] = Observer,
        recursive: bool = False,
    ) -> None:
        self.path = Path(path)
        self._callbacks: list[Callable[[FileSystemEvent], None]] = []
        self._handler = _DebouncedHandler(self._callbacks, patterns=patterns, debounce=debounce)
        self._observer = observer_factory()
        self._recursive = bool(recursive)
        self._scheduled = False

    def add_callback(self, callback: Callable[[FileSystemEvent], None]) -> None:
        """Register a callback to be invoked with the FileSystemEvent."""
        self._callbacks.append(callback)

    def remove_callback(self, callback: Callable[[FileSystemEvent], None]) -> None:
        """Remove a previously-registered callback (if present)."""
        try:
            self._callbacks.remove(callback)
        except ValueError:
            log.debug("Callback not found when removing from watcher")

    def start(self) -> None:
        """Start observing the path. Safe to call multiple times."""
        if not self._scheduled:
            self._observer.schedule(self._handler, str(self.path), recursive=self._recursive)
            self._scheduled = True
        self._observer.start()
        log.debug("Watcher started for %s", self.path)

    def stop(self) -> None:
        """Stop the observer. This is non-blocking; call join() to wait."""
        try:
            self._observer.stop()
        except Exception:
            log.exception("Error stopping watcher")

    def join(self, timeout: float | None = None) -> None:
        """Block until the observer thread has stopped or timeout expires."""
        try:
            self._observer.join(timeout=timeout)
        except Exception:
            log.exception("Error joining watcher")

    def close(self) -> None:
        """Stop and join, and cancel any pending debounce timers."""
        self.stop()
        # cancel in-flight timers
        for t in list(self._handler._timers.values()):
            try:
                t.cancel()
            except Exception:
                log.debug("Failed to cancel timer")
        self.join()

    @property
    def is_alive(self) -> bool:
        """Return True if the underlying observer thread is alive."""
        return self._observer.is_alive()

    def __enter__(self) -> Watcher:
        """Enter context and start watching."""
        self.start()
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        """Exit context and stop watching (best-effort)."""
        self.close()
