from threading import Lock
from typing import Any, ClassVar

from mtb.core import mklog

log = mklog("mtb.core")


class Singleton(type):
    """Thread-safe Singleton metaclass.

    This metaclass ensures only one instance of a class using it is created.
    The implementation uses double-checked locking to avoid acquiring the
    class-level lock on every access.
    """

    _instances: ClassVar[dict[type, Any]] = {}
    _lock: ClassVar[Lock] = Lock()

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        """Return the singleton instance for `cls`, creating it if necessary.

        Uses a double-checked locking pattern to avoid locking on reads once
        an instance has already been created.
        """
        instance = cls._instances.get(cls)
        if instance is None:
            # Instance not present — acquire lock and check again
            with cls._lock:
                instance = cls._instances.get(cls)
                if instance is None:
                    instance = super().__call__(*args, **kwargs)
                    cls._instances[cls] = instance
                    log.debug("Created singleton instance for %s", cls.__name__)
                else:
                    log.debug("Singleton instance created concurrently for %s", cls.__name__)
        else:
            log.debug("Reusing singleton instance for %s", cls.__name__)
        return instance

    @classmethod
    def clear_instance(cls, target: type) -> None:
        """Remove the stored singleton instance for `target` (used in tests)."""
        cls._instances.pop(target, None)

    @classmethod
    def clear_all(cls) -> None:
        """Clear all cached singleton instances. Use with care."""
        cls._instances.clear()
