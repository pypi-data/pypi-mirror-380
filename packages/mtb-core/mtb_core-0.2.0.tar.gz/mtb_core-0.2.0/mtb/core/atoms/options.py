import json
from collections.abc import Callable
from typing import Any


class Options:
    """
    A class to encapsulate various options as attributes.

    This class provides arbitrary attribute access and manipulation,
    mimicking the behavior of a dictionary.

    Attributes
    ----------
        Any attribute can be added during initialization or runtime.

    Example:
        opts = Options(
            center=Vector(0, 0, 0),
            rotation=QtGui.QQuaternion(1, 0, 0, 0)
        )
        opts.distance = 10.0
    """

    def __init__(self, **kwargs):
        """Initialize the options by storing keyword arguments as attributes."""
        self.__dict__.update(kwargs)

    def __str__(self) -> str:
        """Return a string representation."""
        return str(self.__dict__)

    def __repr__(self) -> str:
        """Return the official string representation."""
        return f"Options({self.__dict__})"

    def to_json(self) -> str:
        """Serialize the object to a JSON-formatted string."""
        return json.dumps(self.__dict__)

    def from_json(self, json_str: str):
        """Initialize attributes from a JSON-formatted string."""
        self.__dict__.update(json.loads(json_str))

    def update(self, **kwargs):
        """Update multiple attributes at once."""
        self.__dict__.update(kwargs)

    def keys(self) -> list[str]:
        """Return a list of all attribute names."""
        return list(self.__dict__.keys())

    def values(self) -> list[Any]:
        """Return a list of all attribute values."""
        return list(self.__dict__.values())

    def items(self) -> list[tuple[str, Any]]:
        """Return a list of all (key, value) pairs."""
        return list(self.__dict__.items())

    def __len__(self) -> int:
        """Return the number of attributes."""
        return len(self.__dict__)

    def __contains__(self, key: str) -> bool:
        """Check if key exists."""
        return self.has_key(key)

    def has_key(self, key: str) -> bool:
        """Check if a certain key exists."""
        return key in self.__dict__

    def clear(self):
        """Remove all attributes, resetting the object to an empty state."""
        self.__dict__.clear()

    def filter(self, prefix: str) -> dict[str, Any]:
        """Return a dictionary of attributes that have keys starting with a given prefix."""
        return {k: v for k, v in self.__dict__.items() if k.startswith(prefix)}

    def equals(self, other) -> bool:
        """Check if this object is equal to another Options object."""
        return self.__dict__ == other.__dict__

    def merge(self, other):
        """Merge attributes from another Options object."""
        self.__dict__.update(other.__dict__)

    def transform(self, func: Callable[[Any], Any]):
        """Apply a function to all attribute values."""
        for key, value in self.__dict__.items():
            self.__dict__[key] = func(value)

    def __getattr__(self, key):
        """Get the value of the specified attribute."""
        return self.__dict__.get(key)

    def __setattr__(self, key, value):
        """Set the value of the specified attribute."""
        self.__dict__[key] = value
