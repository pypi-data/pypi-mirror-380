"""Thread management utilities.

Provides ThreadManager for managing threads/callables and emitting lifecycle events.
"""

from __future__ import annotations

import inspect
import logging
import threading
from threading import Event
from typing import Any
from collections.abc import Callable

from mtb.core.observer import EventBus

log = logging.getLogger(__name__)


class ThreadManager:
    """Manage a collection of threads or callables with lifecycle events.

    Events (via the events EventBus):
      - "started": emitted when a thread starts; payload is a dict with keys
        ('name', 'thread').
      - "finished": emitted when a thread finishes normally; payload is a dict
        with similar structure.
      - "error": emitted when a thread raises an exception; payload is a dict
        with keys ('error', 'name', 'thread').

    You may add already-built threading.Thread objects via add_thread, or
    register callables with add_task (the manager will spawn threads for those).
    """

    def __init__(self) -> None:
        self._items: list[dict[str, Any]] = []
        self.events: EventBus = EventBus()

    def add_thread(self, t: threading.Thread, *, name: str | None = None) -> None:
        """Add an existing Thread to the manager.

        If the thread was created externally and has a cooperative stop_event
        attached, pass it in as an attribute before adding by setting
        `thread.stop_event` manually or use add_task instead.
        """
        t.name = name or t.name
        # allow externally-attached stop_event on the thread (optional)
        stop_event = getattr(t, "stop_event", None)
        self._items.append(
            {"thread": t, "name": t.name, "callable": None, "stop_event": stop_event}
        )

    def add_task(
        self,
        func: Callable[..., Any],
        *args: Any,
        name: str | None = None,
        daemon: bool = False,
        **kwargs: Any,
    ) -> threading.Thread:
        """Create a managed thread that runs func(*args, **kwargs).

        The returned Thread is stored in the manager and will be started by
        start_all.
        """
        stop_event = Event()

        def _target(*a: Any, **kw: Any) -> None:
            thread = threading.current_thread()
            try:
                accepts = _accepts_stop_event(func)
                self.events.emit(
                    "started",
                    {"name": name or thread.name, "thread": thread},
                )
                if accepts:
                    kw_with_stop = dict(kw)
                    kw_with_stop["stop_event"] = stop_event
                    func(*a, **kw_with_stop)
                else:
                    func(*a, **kw)
                self.events.emit(
                    "finished",
                    {"name": name or thread.name, "thread": thread},
                )
            except Exception as exc:  # pragma: no cover - let tests exercise
                log.exception("Exception in managed thread %s", thread.name)
                self.events.emit(
                    "error",
                    {"error": exc, "name": name or thread.name, "thread": thread},
                )

        t = threading.Thread(target=_target, args=args, kwargs=kwargs, name=name, daemon=daemon)
        self._items.append(
            {
                "thread": t,
                "name": name or t.name,
                "callable": func,
                "stop_event": stop_event,
            }
        )
        return t

    def start_all(self) -> None:
        """Start all managed threads that are not yet alive."""
        for item in self._items:
            t: threading.Thread = item["thread"]
            if not t.is_alive():
                t.start()

    def join_all(self, timeout: float | None = None) -> dict[str, bool]:
        """Join all threads, optionally with a per-thread timeout.

        Returns a mapping of thread name -> bool (True if the thread is no longer alive after join).
        """
        results: dict[str, bool] = {}
        for item in self._items:
            t: threading.Thread = item["thread"]
            t.join(timeout=timeout)
            results[item["name"]] = not t.is_alive()
        return results

    def active_count(self) -> int:
        """Return the number of threads that are currently alive."""
        return sum(1 for it in self._items if it["thread"].is_alive())

    def clear(self) -> None:
        """Clear managed items. Threads that are still running are left alone."""
        self._items.clear()

    def __enter__(self) -> ThreadManager:
        """Enter context: manager is returned so it can be used with 'with'."""
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        """Exit context: attempt to join managed threads."""
        # best-effort: wait for threads to finish on exit
        try:
            self.join_all()
        except Exception:
            log.exception("Error joining threads on context exit")

    def stop_all(self, *, join: bool = True, timeout: float | None = None) -> dict[str, bool]:
        """Set stop_event on all managed tasks that support cooperative stop.

        If join is True, attempt to join threads after setting stop events. The
        optional timeout is passed through to join_all.
        """
        # set stop events where present
        for it in self._items:
            se = it.get("stop_event")
            if isinstance(se, Event):
                se.set()

        if join:
            return self.join_all(timeout=timeout)
        return {it["name"]: not it["thread"].is_alive() for it in self._items}

    def stop(self, name: str, *, join: bool = True, timeout: float | None = None) -> bool:
        """Stop a single managed task by name if it exposes a stop_event.

        Returns True if thread no longer alive after optional join.
        """
        for it in self._items:
            if it["name"] == name:
                se = it.get("stop_event")
                if isinstance(se, Event):
                    se.set()
                if join:
                    it["thread"].join(timeout=timeout)
                    return not it["thread"].is_alive()
                return not it["thread"].is_alive()
        return False


def _accepts_stop_event(func: Callable[..., Any]) -> bool:
    """Return True if `func` accepts a 'stop_event' keyword argument.

    We accept var-keyword (**kwargs) as an indication the callable will
    tolerate receiving the stop_event kwarg.
    """
    try:
        sig = inspect.signature(func)
    except (ValueError, TypeError):
        return False
    for p in sig.parameters.values():
        if p.kind == p.VAR_KEYWORD:
            return True
        if p.name == "stop_event":
            return True
    return False
