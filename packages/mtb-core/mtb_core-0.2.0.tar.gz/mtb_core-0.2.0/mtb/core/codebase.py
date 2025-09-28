import ast
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Symbol:
    name: str
    type: str  # This could be further defined based on your needs (e.g., function, variable, etc.)
    line_number: int


def get_symbols(code_file: Path) -> list[Symbol]:
    """Return a list of Symbol objects extracted from the given Python code file."""
    # Read the content of the file
    with code_file.open("r") as f:
        tree = ast.parse(f.read())

    symbols = []

    # Walk through the abstract syntax tree and collect symbol information
    for node in ast.walk(tree):
        if isinstance(
            node, (ast.FunctionDef, ast.AsyncFunctionDef)
        ):  # If it's a function definition
            symbol_type = "function"
            name = node.name
            line_number = node.lineno
            symbols.append(Symbol(name, symbol_type, line_number))
        elif isinstance(node, ast.Assign):  # If it's a variable assignment
            for target in node.targets:
                if isinstance(
                    target, ast.Name
                ):  # Only consider simple name assignments (not tuples or attributes)
                    symbol_type = "variable"
                    name = target.id
                    line_number = node.lineno
                    symbols.append(Symbol(name, symbol_type, line_number))
        # Add more conditions as needed to handle other types of symbols

    return symbols
