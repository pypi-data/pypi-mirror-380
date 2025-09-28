"""Codegen for TypeScript."""

import contextlib
import inspect
import json
from typing import Union, get_args, get_origin

from pydantic import BaseModel

PY_TO_TS_TYPE = {
    int: "number",
    float: "number",
    str: "string",
    bool: "boolean",
    dict: "Record<string, any>",
    list: "any[]",
    type(None): "null",
}


def python_type_to_ts(py_type) -> str:
    """Convert a Python type to a TypeScript type string.

    Args:
        py_type: The Python type to convert.

    Returns
    -------
        A string representing the equivalent TypeScript type.
        Defaults to "any" if no mapping is found.

    Raises
    ------
        TypeError: If the input is not a valid Python type.
    """
    origin = get_origin(py_type)
    args = get_args(py_type)

    if origin is Union:
        ts_parts = [python_type_to_ts(arg) for arg in args]
        return " | ".join(sorted(set(ts_parts)))

    elif origin is list:
        item_type = python_type_to_ts(args[0]) if args else "any"
        return f"{item_type}[]"

    elif isinstance(py_type, type) and issubclass(py_type, BaseModel):
        return py_type.__name__

    return PY_TO_TS_TYPE.get(py_type, "any")


def python_value_to_ts(value):
    """Convert a Python value to its equivalent TypeScript representation.

    Args:
        value: The Python value to convert.

    Returns
    -------
        str: The TypeScript representation of the value.  Returns "undefined" for unhandled types.

    Raises
    ------
        TypeError, if the input is not a basic Python type
        from str, bool, int, float, None, list, dict.

    Examples
    --------
        >>> python_value_to_ts("hello")
        '"hello"'
        >>> python_value_to_ts(True)
        'true'
        >>> python_value_to_ts(123)
        '123'
        >>> python_value_to_ts(None)
        'null'
        >>> python_value_to_ts([1, "hello", True])
        '[1, "hello", true]'
        >>> python_value_to_ts({"a": 1, "b": "hello"})
        '{a: 1, b: "hello"}'
    """
    if isinstance(value, str):
        return json.dumps(value)
    elif isinstance(value, bool):
        return "true" if value else "false"
    elif isinstance(value, int | float):
        return str(value)
    elif value is None:
        return "null"
    elif isinstance(value, list):
        return "[" + ", ".join(python_value_to_ts(v) for v in value) + "]"
    elif isinstance(value, dict):
        return "{" + ", ".join(f"{k}: {python_value_to_ts(v)}" for k, v in value.items()) + "}"
    return "undefined"


def pydantic_to_ts(model: type[BaseModel], utility: bool = False) -> str:
    """Convert a Pydantic model to a TypeScript interface string.

    Args:
        model: The Pydantic model class to convert.

    Returns
    -------
        A string representing the TypeScript interface for the model.
    """
    doc = inspect.getdoc(model)
    lines = []

    if doc and doc != BaseModel.__doc__:
        lines.append(f"/** {doc} */")

    lines.append(f"export interface {model.__name__} {{")

    defaults = {}

    for field_name, model_field in model.model_fields.items():
        ts_type = python_type_to_ts(model_field.annotation)
        optional = not model_field.is_required()
        description = model_field.description or model_field.alias or ""

        if description:
            lines.append(f"  /** {description} */")
        lines.append(f"  {field_name}{'?' if optional else ''}: {ts_type};")

        if model_field.default is not None or model_field.default_factory is not None:
            # TODO: avoid using this (properly report errors)
            with contextlib.suppress(Exception):
                default_value = model_field.get_default()
                defaults[field_name] = default_value

    lines.append("")
    if utility:
        name = model.__name__
        # Emit default constant
        lines.append(f"export const default_{name.lower()}: {name} = {{")
        for key, val in defaults.items():
            lines.append(f"  {key}: {python_value_to_ts(val)},")
        lines.append("};\n")

        # Emit create function
        lines.append(f"export function create_{name}(data: Partial<{name}> = {{}}): {name} {{")
        lines.append(f"  return {{ ...default_{name}, ...data }};")
        lines.append("}")

    lines.append("}")
    return "\n".join(lines)
