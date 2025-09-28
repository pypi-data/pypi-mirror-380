#!/usr/bin/env python3
"""Example demonstrating `mtb.core.config.Config` usage.

Shows JSON/TOML save/load, strict vs non-strict attribute access, and serializer
selection.
"""
from pathlib import Path

from mtb.core.config import Config, JSONSerializer, TOMLSerializer, _HAS_TOMLI_W

# Use local files in the examples directory to avoid writing to ~/.config
json_path = Path("./example_config.json")
toml_path = Path("./example_config.toml")

# Create a non-strict config and set values
cfg = Config(name="example_app", strict=False)
cfg.username = "alice"
cfg.retries = 3
cfg.database = {"host": "localhost", "port": 5432}

print("Initial config:", cfg.to_dict())

# Save as JSON
p_json = cfg.save(json_path)
print("Saved JSON to:", p_json)

# Load into a fresh instance
cfg2 = Config(name="example_app")
cfg2.load(json_path)
print("Loaded config:", cfg2.to_dict())

# Try strict mode
cfg_strict = Config(name="example_app", strict=True)
try:
    print(cfg_strict.nonexistent)
except AttributeError as exc:
    print("Strict mode raised as expected:", exc)

# Save TOML only if tomli-w is available for writing
if _HAS_TOMLI_W:
    cfg.set_serializer(TOMLSerializer())
    p_toml = cfg.save(toml_path)
    print("Saved TOML to:", p_toml)
else:
    print("Skipping TOML save: tomli-w not available")
