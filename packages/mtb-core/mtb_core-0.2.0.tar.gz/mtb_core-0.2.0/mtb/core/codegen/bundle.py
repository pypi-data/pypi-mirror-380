import argparse
import ast
from importlib import import_module
from pathlib import Path

# from ..log import mklog
from mtb.core import mklog

log = mklog("mtb.core.codegen", use_rich=True)


def resolve_module_to_path(module: str, base_dir: Path) -> Path | None:
    """Resolve a module name like 'my_private_lib.foo' to a file path."""
    parts = module.split(".")
    maybe = None
    log.info(f"Trying to resolve {module} from {base_dir}")
    # for root in [base_dir, *base_dir.glob("**/")]:
    #     maybe = root.joinpath(*parts).with_suffix(".py")
    #     if maybe.exists():
    # return maybe.resolve()
    if not maybe:
        log.info(f"Couldn't resolve {module} from {base_dir}, trying to import")
        try:
            mod = import_module(module)
            if mod.__file__:
                maybe = Path(mod.__file__).resolve()
        except Exception as e:
            log.error(f"Fallback either couldn't import {module}: {e}")

    return maybe


def extract_definitions(path: Path, wanted_symbols: set[str]) -> list[ast.AST]:
    """
    Parse the file and return AST nodes for the requested symbols.
    """
    tree = ast.parse(path.read_text())
    result = []

    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)) and node.name in wanted_symbols:
            result.append(node)

    return result


def remove_tracked_imports(tree: ast.Module, tracked_imports: dict[str, set[str]]):
    """
    Mutates the tree to remove tracked import lines.
    """
    new_body = []
    for stmt in tree.body:
        if isinstance(stmt, ast.ImportFrom) and stmt.module in tracked_imports:
            continue
        if isinstance(stmt, ast.Import):
            if any(alias.name in tracked_imports for alias in stmt.names):
                continue
        new_body.append(stmt)
    tree.body = new_body


def embed_definitions(tree: ast.Module, definitions: list[ast.AST]):
    """
    Prepend extracted definitions at the top of the module.
    """
    tree.body = definitions + tree.body


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+", help="Source files to inspect")
    parser.add_argument("--track", nargs="+", required=True, help="Module names to track")
    parser.add_argument("-o", "--output", required=True, help="Output directory")
    return parser.parse_args()


class ImportTracker(ast.NodeVisitor):
    def __init__(self, tracked_modules: set[str]):
        self.tracked_modules = tracked_modules
        self.found_imports = {}  # module -> set(symbols)

    def visit_ImportFrom(self, node: ast.ImportFrom):
        if node.module and any(node.module.startswith(t) for t in self.tracked_modules):
            self.found_imports.setdefault(node.module, set()).update(
                alias.name for alias in node.names
            )

    def visit_Import(self, node: ast.Import):
        for alias in node.names:
            if any(alias.name.startswith(t) for t in self.tracked_modules):
                self.found_imports.setdefault(alias.name, set())


def analyze_file(filepath: Path, tracked_modules: set[str]) -> dict[str, set[str]]:
    tree = ast.parse(filepath.read_text())
    tracker = ImportTracker(tracked_modules)
    tracker.visit(tree)
    return tracker.found_imports


def main():
    args = parse_args()
    tracked_modules = set(args.track)
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    for file in args.files:
        file_path = Path(file)
        imports = analyze_file(file_path, tracked_modules)
        log.info(f"Processing: {file_path}")
        used_defs = []

        for module, symbols in imports.items():
            mod_path = resolve_module_to_path(module, file_path.parent)
            if not mod_path:
                print(f"  ⚠ Could not resolve {module}")
                continue

            defs = extract_definitions(mod_path, symbols)
            used_defs.extend(defs)

        # Load and rewrite file
        tree = ast.parse(file_path.read_text())
        remove_tracked_imports(tree, imports)
        embed_definitions(tree, used_defs)

        # Output
        output_file = output_dir / file_path.name
        output_file.write_text(ast.unparse(tree))

        print(f"  ✅ Output written to: {output_file}")


if __name__ == "__main__":
    main()
