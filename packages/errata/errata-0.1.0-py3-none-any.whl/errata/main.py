# main.py
import ast
import importlib
import inspect
import os
import pkgutil
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Set, Tuple

import typer
from rich.console import Console, Group
from rich.table import Table
from rich.tree import Tree


# --- Domain Objects ---
@dataclass
class UsageLocation:
    """Represents a location where an exception is used."""

    module_path: str
    line_numbers: List[int]


@dataclass
class ExceptionInfo:
    """Represents an exception with all its metadata."""

    name: str
    qualified_name: str
    exception_class: Any
    description: str
    usage_locations: List[UsageLocation]
    parent: Optional["ExceptionInfo"] = None
    children: List["ExceptionInfo"] = None

    def __post_init__(self):
        if self.children is None:
            self.children = []


@dataclass
class ExceptionHierarchy:
    """Represents the complete exception hierarchy for a module."""

    module_name: str
    exceptions: Dict[str, ExceptionInfo]
    roots: List[ExceptionInfo]

    def get_all_exceptions(self) -> List[ExceptionInfo]:
        """Get all exceptions in hierarchical order."""
        result = []
        visited = set()

        def traverse(exc: ExceptionInfo, depth: int = 0):
            if exc.qualified_name not in visited:
                visited.add(exc.qualified_name)
                result.append(exc)
                for child in sorted(exc.children, key=lambda x: x.qualified_name):
                    traverse(child, depth + 1)

        for root in sorted(self.roots, key=lambda x: x.qualified_name):
            traverse(root)

        return result


# --- Data Collection ---
def find_exceptions(module_name: str) -> List[Tuple[str, Any]]:
    """Recursively finds all exception classes in a given module."""
    try:
        module = importlib.import_module(module_name)
    except ImportError:
        return []

    seen: Set[int] = set()
    exceptions: List[Tuple[str, Any]] = []

    def _find(mod: Any):
        # Find exceptions in the current module
        for name, obj in inspect.getmembers(mod):
            if (
                inspect.isclass(obj)
                and issubclass(obj, Exception)
                and obj.__module__.startswith(module_name)
                and id(obj) not in seen
            ):
                full_name = f"{obj.__module__}.{name}"
                exceptions.append((full_name, obj))
                seen.add(id(obj))

        # Recurse into submodules
        if hasattr(mod, "__path__"):
            for _, sub_mod_name, _ in pkgutil.iter_modules(
                mod.__path__, mod.__name__ + "."
            ):
                if sub_mod_name.endswith(".__main__"):
                    continue
                try:
                    submodule = importlib.import_module(sub_mod_name)
                    _find(submodule)
                except Exception:
                    # Ignore import errors for optional dependencies, etc.
                    pass

    _find(module)
    return sorted(exceptions)


def collect_exception_usage(
    exception_class: Any, module_name: str
) -> List[UsageLocation]:
    """Collect where an exception is raised in the source code."""
    usage_locations = {}

    try:
        module = importlib.import_module(module_name)
    except ImportError:
        return []

    def _analyze_module(mod):
        try:
            source_file = inspect.getfile(mod)
        except (TypeError, OSError):
            return

        if not os.path.exists(source_file):
            return

        try:
            with open(source_file, "r", encoding="utf-8") as f:
                source = f.read()
        except (UnicodeDecodeError, IOError):
            return

        try:
            tree = ast.parse(source, filename=source_file)
        except SyntaxError:
            return

        class ExceptionVisitor(ast.NodeVisitor):
            def __init__(self):
                self.current_class = None

            def visit_ClassDef(self, node):
                old_class = self.current_class
                self.current_class = node.name
                self.generic_visit(node)
                self.current_class = old_class

            def visit_FunctionDef(self, node):
                self.generic_visit(node)

            def visit_AsyncFunctionDef(self, node):
                self.generic_visit(node)

            def visit_Raise(self, node):
                if node.exc:
                    exc_name = None
                    if isinstance(node.exc, ast.Name):
                        exc_name = node.exc.id
                    elif isinstance(node.exc, ast.Call) and isinstance(
                        node.exc.func, ast.Name
                    ):
                        exc_name = node.exc.func.id
                    elif isinstance(node.exc, ast.Call) and isinstance(
                        node.exc.func, ast.Attribute
                    ):
                        exc_name = node.exc.func.attr
                    elif isinstance(node.exc, ast.Attribute):
                        exc_name = node.exc.attr

                    if exc_name == exception_class.__name__:
                        module_path = mod.__name__
                        if self.current_class:
                            module_path = f"{module_path}.{self.current_class}"
                        if module_path not in usage_locations:
                            usage_locations[module_path] = []
                        usage_locations[module_path].append(node.lineno)

                self.generic_visit(node)

        visitor = ExceptionVisitor()
        visitor.visit(tree)

        # Recurse into submodules
        if hasattr(mod, "__path__"):
            for _, sub_mod_name, _ in pkgutil.iter_modules(
                mod.__path__, mod.__name__ + "."
            ):
                if sub_mod_name.endswith(".__main__"):
                    continue
                try:
                    submodule = importlib.import_module(sub_mod_name)
                    _analyze_module(submodule)
                except Exception:
                    pass

    _analyze_module(module)

    # Convert to UsageLocation objects
    return [
        UsageLocation(module_path, line_numbers)
        for module_path, line_numbers in usage_locations.items()
    ]


def build_exception_hierarchy(
    module_name: str, collect_usage: bool = False
) -> ExceptionHierarchy:
    """Build the complete exception hierarchy for a module."""

    # Step 1: Find all exceptions
    raw_exceptions = find_exceptions(module_name)

    # Step 2: Create ExceptionInfo objects
    exceptions = {}
    for qualified_name, exception_class in raw_exceptions:
        name = qualified_name.split(".")[-1]

        # Get description
        doc = exception_class.__doc__ or "No description."
        description = doc.strip().split("\n")[0]
        if len(description) > 60:
            description = description[:57] + "..."

        # Collect usage if requested
        usage_locations = []
        if collect_usage:
            usage_locations = collect_exception_usage(exception_class, module_name)

        exc_info = ExceptionInfo(
            name=name,
            qualified_name=qualified_name,
            exception_class=exception_class,
            description=description,
            usage_locations=usage_locations,
        )
        exceptions[qualified_name] = exc_info

    # Step 3: Build parent-child relationships
    roots = []
    for qualified_name, exc_info in exceptions.items():
        exception_class = exc_info.exception_class

        # Find parent in our exceptions
        mro = exception_class.__mro__[1:]  # Skip the class itself
        parent_exc = None

        for parent_class in mro:
            for other_name, other_info in exceptions.items():
                if other_info.exception_class is parent_class:
                    parent_exc = other_info
                    break
            if parent_exc:
                break

        if parent_exc:
            exc_info.parent = parent_exc
            parent_exc.children.append(exc_info)
        else:
            roots.append(exc_info)

    return ExceptionHierarchy(
        module_name=module_name, exceptions=exceptions, roots=roots
    )


def create_usage_tree(usage_locations: List[UsageLocation]) -> Tree | str:
    """Create a Rich Tree representation of exception usage locations."""
    if not usage_locations:
        return ""

    tree = Tree("Raised at")

    # Sort by module path and add them
    for location in sorted(usage_locations, key=lambda x: x.module_path):
        lines_str = ", ".join(f"L{line}" for line in sorted(location.line_numbers))
        tree.add(f"{location.module_path} ({lines_str})")

    return tree


# --- Table Rendering ---
@dataclass
class TreeNode:
    """Represents a node in the rendered tree with position info."""

    exception: ExceptionInfo
    depth: int
    is_last: bool
    tree_prefix: str
    continuation_lines: List[str]  # Lines needed to maintain tree structure


class TableRenderer:
    """Renders exception hierarchy as a table with proper tree structure."""

    def __init__(self, hierarchy: ExceptionHierarchy, show_usage: bool = False):
        self.hierarchy = hierarchy
        self.show_usage = show_usage

    def _count_usage_lines(self, exc: ExceptionInfo) -> int:
        """Count how many lines the usage tree for an exception will take."""
        if not exc.usage_locations:
            return 1  # "No usage found" takes 1 line

        # Count: 1 for the root "📍 Raised at" + number of locations
        return 1 + len(exc.usage_locations)

    def _build_hierarchy_tree(self) -> Tree:
        """Build a Rich Tree for the exception hierarchy with vertical padding."""
        hierarchy_tree = Tree("Exception Hierarchy")

        def add_to_tree(parent_node, exc: ExceptionInfo, has_children: bool = False):
            # Add this exception to the parent node
            if self.show_usage:
                usage_lines = self._count_usage_lines(exc)
                # Create a multi-line label for the exception with padding
                lines = [exc.name]
                # Add padding lines with proper tree continuation
                for _ in range(usage_lines - 1):
                    if has_children:
                        lines.append("│   ")
                    else:
                        lines.append("    ")

                # Join with newlines to create a multi-line node
                child_node = parent_node.add("\n".join(lines))
            else:
                child_node = parent_node.add(exc.name)

            # Add children recursively
            if exc.children:
                children = sorted(exc.children, key=lambda x: x.qualified_name)
                for child in children:
                    add_to_tree(child_node, child, has_children=len(child.children) > 0)

        # Add root exceptions
        roots = sorted(self.hierarchy.roots, key=lambda x: x.qualified_name)
        for root in roots:
            add_to_tree(hierarchy_tree, root, has_children=False)

        return hierarchy_tree

    def _build_description_content(self) -> str:
        """Build description content that aligns with the tree structure."""
        descriptions = []

        def collect_descriptions(exc: ExceptionInfo, depth: int = 0):
            descriptions.append(exc.description)

            # Add children descriptions
            if exc.children:
                children = sorted(exc.children, key=lambda x: x.qualified_name)
                for child in children:
                    collect_descriptions(child, depth + 1)

        # Collect descriptions in the same order as the tree
        roots = sorted(self.hierarchy.roots, key=lambda x: x.qualified_name)
        for root in roots:
            collect_descriptions(root)

        return "\n".join(descriptions)

    def _build_usage_group(self) -> Group:
        """Build usage Group that aligns with the tree structure."""
        usage_items = []

        def collect_usage(exc: ExceptionInfo, depth: int = 0):
            usage_tree = create_usage_tree(exc.usage_locations)
            usage_items.append(usage_tree)

            # Add children usage
            if exc.children:
                children = sorted(exc.children, key=lambda x: x.qualified_name)
                for child in children:
                    collect_usage(child, depth + 1)

        # Collect usage in the same order as the tree
        roots = sorted(self.hierarchy.roots, key=lambda x: x.qualified_name)
        for root in roots:
            collect_usage(root)

        return Group(*usage_items)

    def render_table(self) -> Table:
        """Render the complete table."""
        table = Table(title=f"Exceptions in {self.hierarchy.module_name!r}")
        table.add_column("Exception Hierarchy", style="cyan", vertical="top")
        table.add_column("Description", style="magenta", vertical="top")

        if self.show_usage:
            table.add_column("Usage Locations", style="green", vertical="top")

        # Build the tree and aligned content
        hierarchy_tree = self._build_hierarchy_tree()
        description_content = self._build_description_content()

        if self.show_usage:
            usage_group = self._build_usage_group()
            table.add_row(hierarchy_tree, description_content, usage_group)
        else:
            table.add_row(hierarchy_tree, description_content)

        return table


# --- Typer CLI application ---
app = typer.Typer()
console = Console()


@app.command()
def find(
    library_name: str = typer.Argument(
        ...,
        help="The name of the Python library to inspect, e.g., 'openai' or 'requests'",
    ),
    show_usage: bool = typer.Option(
        False,
        "--show-usage",
        "-u",
        help="Show a tree of call/raise locations for each exception",
    ),
):
    """
    Discovers and lists all custom exceptions in a Python library.
    """
    with console.status(f"[bold green]Inspecting {library_name}..."):
        hierarchy = build_exception_hierarchy(library_name, collect_usage=show_usage)

    if not hierarchy.exceptions:
        console.print(
            f"[bold red]No custom exceptions found in '{library_name}'.[/bold red]"
        )
        raise typer.Exit()

    # Render table
    renderer = TableRenderer(hierarchy, show_usage=show_usage)
    table = renderer.render_table()
    console.print(table)


if __name__ == "__main__":
    app()
