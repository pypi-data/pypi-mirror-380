"""Small demo for the EventBus in mtb.core.observer.

Run this module directly to see the EventBus in action.
"""

import asyncio
import gc

from mtb.core.observer import EventBus

from common import log, warn


async def async_handler(payload):
    """Asynchronous handler that simulates work."""
    await asyncio.sleep(0.05)
    log("async_handler received:", payload)


def sync_handler(payload):
    """Log the payload (synchronous handler)."""
    log("sync_handler received:", payload)


def raising_handler(payload):
    """Raise an error to demonstrate error handling in subscribers."""
    raise RuntimeError("handler boom")


class Handler:
    """Example object with a bound method handler (demonstrates weak refs)."""

    def __init__(self, name: str):
        self.name = name

    def method(self, payload):
        """Bound method to be used as a handler."""
        log(f"{self.name}.method received:", payload)


async def main():
    """Comprehensive EventBus demo covering common use cases."""
    bus = EventBus()

    # connect several handlers
    bus.connect("greet", sync_handler)
    bus.connect("greet", async_handler)
    bus.connect("greet", raising_handler)

    warn(f"current handlers: {len(bus)}")

    # basic emit (schedules async handlers)
    warn("Emit (sync) - async handler will be scheduled; raising handler will be logged")
    bus.emit("greet", "hello")
    # give scheduled tasks a chance to run
    await asyncio.sleep(0.2)

    # await all coroutine handlers
    warn("Awaiting emit_async - both coroutine handlers will be awaited")
    await bus.emit_async("greet", "world")

    # demonstrate connect_once
    warn("connect_once demo")
    bus.connect_once("once", lambda p: log("one-shot got:", p))
    bus.emit("once", "first")
    bus.emit("once", "second")
    await asyncio.sleep(0.05)

    # disconnect a handler
    warn("disconnect demo: removing sync_handler")
    bus.disconnect("greet", sync_handler)
    await bus.emit_async("greet", "after disconnect")

    # demonstrate weakref removal of bound methods
    h = Handler("H1")
    bus.connect("greet", h.method)
    warn(f"Added bound method handler; handlers: {len(bus)}")

    # drop the instance and force GC — handler should be pruned
    del h
    gc.collect()
    warn(f"After GC, handlers: {len(bus)}")

    # bulk handlers performance test
    warn("bulk handlers performance test: registering many handlers")
    import time

    bulk_count = 100
    called = 0

    def bulk_sync(p):
        nonlocal called
        called += 1

    async def bulk_async(p):
        await asyncio.sleep(0.001)

    # register many sync handlers and a few async ones
    for _ in range(bulk_count):
        bus.connect("bulk", bulk_sync)
    for _ in range(5):
        bus.connect("bulk", bulk_async)

    t0 = time.perf_counter()
    await bus.emit_async("bulk", {"n": bulk_count})
    t1 = time.perf_counter()
    warn(f"bulk emit_async completed in {t1 - t0:.3f}s, sync-called {called}")

    # demonstrate async connect_once workaround: create an async wrapper
    async_called = 0

    async def once_async(payload):
        nonlocal async_called
        async_called += 1

    async def _once_wrapper(p):
        try:
            await once_async(p)
        finally:
            bus.disconnect("once_async", _once_wrapper)

    bus.connect("once_async", _once_wrapper)
    await bus.emit_async("once_async", "a")
    await bus.emit_async("once_async", "b")
    warn(f"async connect_once workaround called: {async_called}")

    # final emit to show remaining handlers called
    bus.emit("greet", "final")
    await asyncio.sleep(0.2)


if __name__ == '__main__':
    asyncio.run(main())
