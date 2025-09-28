"""Simple observer pattern implementation."""

import asyncio
import weakref
from collections.abc import Callable
from typing import Any

from .log import mklog

log = mklog(__name__)


class Observable:
    """Base class for objects that can notify observers of changes."""

    def __init__(self, *args, **kwargs):
        """Initialize this observable object."""
        self._observers: set[weakref.ReferenceType[Observer]] = set()

    def cleanup(self):
        """Remove any garbage collected observers."""
        self._observers = {ref for ref in self._observers if ref() is not None}

    def subscribe(self, observer: "Observer") -> None:
        """Add an observer to be informed of changes."""
        if observer is None:
            log.warning("Attempted to subscribe None observer")
            return

        # Find existing reference or create new one
        observer_ref = None
        for ref in self._observers:
            if ref() is observer:
                observer_ref = ref
                break

        if observer_ref is None:
            observer_ref = weakref.ref(observer)
            self._observers.add(observer_ref)
            log.debug(f"Subscribed observer: {observer}")

    def unsubscribe(self, observer: "Observer") -> None:
        """Remove an observer from being informed of changes."""
        if observer is None:
            return

        # Find and remove the reference
        to_remove = None
        for ref in self._observers:
            if ref() is observer:
                to_remove = ref
                break

        if to_remove:
            self._observers.remove(to_remove)
            try:
                observer.close()
            except Exception as e:
                log.warning(f"Error closing observer {observer}: {e}")
            log.debug(f"Unsubscribed observer: {observer}")

    def notify(self, *args, **kwargs) -> None:
        """Notify subscribed observers of a change synchronously."""
        self.cleanup()
        current_observers = [ref() for ref in self._observers if ref() is not None]

        for observer in current_observers:
            if observer is None:  # Additional safety check
                continue
            try:
                if asyncio.iscoroutinefunction(observer.update):
                    log.error(
                        f"Observer {observer} has async update method. "
                        f"Use notify_async() instead of notify()"
                    )
                    continue
                observer.update(self, *args, **kwargs)
            except Exception as e:
                log.error(f"Error notifying observer {observer}: {e}")

    async def notify_async(self, *args, **kwargs) -> None:
        """Notify subscribed observers of a change asynchronously."""
        self.cleanup()
        current_observers = [ref() for ref in self._observers if ref() is not None]

        async_tasks = []

        for observer in current_observers:
            if observer is None:  # Additional safety check
                continue
            try:
                if asyncio.iscoroutinefunction(observer.update):
                    task = asyncio.create_task(observer.update(self, *args, **kwargs))
                    async_tasks.append(task)
                else:
                    observer.update(self, *args, **kwargs)
            except Exception as e:
                log.error(f"Error preparing notification for observer {observer}: {e}")

        if async_tasks:
            try:
                await asyncio.gather(*async_tasks, return_exceptions=True)
            except Exception as e:
                log.error(f"Error in async observer notifications: {e}")

    @property
    def observer_count(self) -> int:
        """Get the number of active observers."""
        self.cleanup()
        return len(self._observers)


class Observer:
    """Base class for objects that observe changes in Observable objects."""

    def close(self) -> None:
        """Observer is unsubscribed. Override if cleanup is needed."""
        pass

    def update(self, observable: Observable, *args, **kwargs) -> None:
        """Observed object changes.

        Override this method to handle notifications. Can be async if needed.
        """
        raise NotImplementedError("Observer subclasses must implement update()")


class Property(Observable):
    """Observable property that notifies when its value changes."""

    def __init__(self, initial_value: Any = None):
        """Initialize property with optional initial value."""
        super().__init__()
        self._value = initial_value

    def __format__(self, format_spec: str) -> str:
        """Format this property's value as a string."""
        return format(self._value, format_spec)

    def __repr__(self) -> str:
        """Represent this property as a string."""
        return f"Property({repr(self._value)})"

    def __str__(self) -> str:
        """Convert this property's value to a string."""
        return str(self._value)

    def __eq__(self, other: Any) -> bool:
        """Compare property value with another value."""
        if isinstance(other, Property):
            return self._value == other._value
        return self._value == other

    def __hash__(self) -> int:
        """Hash based on value (if hashable)."""
        try:
            return hash(self._value)
        except TypeError:
            return id(self)

    def get(self) -> Any:
        """Get the current value of this property."""
        return self._value

    def set(self, value: Any) -> None:
        """Set the property value and notify observers if changed."""
        if value != self._value:
            old_value = self._value
            self._value = value
            log.debug(f"Property changed: {old_value} -> {value}")
            self.notify(old_value, value)

    @property
    def value(self) -> Any:
        """Property-style access to the value."""
        return self._value

    @value.setter
    def value(self, new_value: Any) -> None:
        """Property-style setter for the value."""
        self.set(new_value)


class FunctionObserver(Observer):
    """Observer that calls a function when notified."""

    def __init__(self, func: Callable[...,Any]):
        """Initialize with a function to call on updates."""
        self.func = func

    def update(self, observable: Observable, *args, **kwargs) -> None:
        """Call the stored function with the notification."""
        try:
            self.func(observable, *args, **kwargs)
        except Exception as e:
            log.error(f"Error in function observer: {e}")

    def __repr__(self) -> str:
        return f"FunctionObserver({self.func.__name__})"


class EventBus:
    """A simple named-event bus built on top of weak-referenced handlers.

    Usage:
        bus = EventBus()
        bus.connect('my_event', handler)
        bus.emit('my_event', payload)

    Handlers may be regular functions or coroutines; coroutine handlers are
    scheduled when using emit(), or awaited when using emit_async().
    """

    class _Handler:
        def __init__(self, callback: Callable[..., Any]):
            # try weakref.WeakMethod for bound methods
            try:
                self._ref = weakref.WeakMethod(callback)
            except Exception:
                try:
                    self._ref = weakref.ref(callback)
                except TypeError:
                    # fall back to a strong reference for non-weakrefable callables
                    self._ref = lambda: callback  # type: ignore

        def is_alive(self) -> bool:
            return self._ref() is not None

        def get(self) -> Callable[..., Any] | None:
            return self._ref()

        def matches(self, callback: Callable[..., Any]) -> bool:
            current = self.get()
            return current is callback

    def __init__(self):
        self._handlers: dict[str, list[EventBus._Handler]] = {}

    def _get_handlers_list(self, event: str) -> list["EventBus._Handler"]:
        return self._handlers.setdefault(event, [])

    def connect(self, event: str, callback: Callable[..., Any]) -> None:
        """Register a handler for a named event.

        Duplicate registrations of the same callable for the same event are
        ignored.
        """
        handlers = self._get_handlers_list(event)
        if any(h.matches(callback) for h in handlers if h.is_alive()):
            return
        handlers.append(EventBus._Handler(callback))

    def disconnect(self, event: str, callback: Callable[..., Any]) -> None:
        """Unregister a previously registered handler for an event."""
        handlers = self._handlers.get(event)
        if not handlers:
            return
        self._handlers[event] = [h for h in handlers if not h.matches(callback)]

    def _prune(self) -> None:
        for event, handlers in list(self._handlers.items()):
            alive = [h for h in handlers if h.is_alive()]
            if alive:
                self._handlers[event] = alive
            else:
                self._handlers.pop(event, None)

    def emit(self, event: str, *args: Any, **kwargs: Any) -> None:
        """Emit an event synchronously.

        Coroutine handlers will be scheduled as tasks. Use emit_async to await
        coroutine handlers instead.
        """
        self._prune()
        handlers = list(self._handlers.get(event, []))
        for handler in handlers:
            cb = handler.get()
            if cb is None:
                continue
            try:
                if asyncio.iscoroutinefunction(cb):
                    # schedule coroutine handlers
                    asyncio.create_task(cb(*args, **kwargs))
                else:
                    cb(*args, **kwargs)
            except Exception as exc:  # pragma: no cover - defensive
                log.error("Error in EventBus handler for event %s: %s", event, exc)

    async def emit_async(self, event: str, *args: Any, **kwargs: Any) -> None:
        """Emit an event and await coroutine handlers."""
        self._prune()
        handlers = list(self._handlers.get(event, []))
        tasks = []
        for handler in handlers:
            cb = handler.get()
            if cb is None:
                continue
            try:
                if asyncio.iscoroutinefunction(cb):
                    tasks.append(asyncio.create_task(cb(*args, **kwargs)))
                else:
                    # sync handlers are executed inline
                    cb(*args, **kwargs)
            except Exception as exc:  # pragma: no cover - defensive
                log.error("Error preparing EventBus handler for event %s: %s", event, exc)

        if tasks:
            # gather and log exceptions rather than failing
            results = await asyncio.gather(*tasks, return_exceptions=True)
            for r in results:
                if isinstance(r, Exception):
                    log.error("Error in async EventBus handler for event %s: %s", event, r)

    def connect_once(self, event: str, callback: Callable[..., Any]) -> None:
        """Register a handler that disconnects after the first invocation."""

        def _wrapper(*a: Any, **kw: Any):
            try:
                callback(*a, **kw)
            finally:
                self.disconnect(event, _wrapper)

        self.connect(event, _wrapper)

    def __len__(self) -> int:
        self._prune()
        return sum(len(v) for v in self._handlers.values())
