import importlib
import pkgutil
from types import ModuleType

from ordeq.framework._registry import NODE_REGISTRY  # noqa: PLC2701
from ordeq.framework.io import IO, Input, Output
from ordeq.framework.nodes import Node


def gather_ios_from_module(
    module: ModuleType,
) -> dict[str, IO | Input | Output]:
    """Find all `IO` objects defined in the provided module

    Args:
        module: the Python module object

    Returns:
        a dict of `IO` objects with their variable name as key
    """
    return {
        k: v
        for k, v in vars(module).items()
        if isinstance(v, (IO, Input, Output))
    }


def gather_nodes_from_registry() -> set[Node]:
    """Find all `Node` objects defined in the provided module

    Returns:
        a set of `Node` objects
    """
    return set(NODE_REGISTRY._data.values())  # noqa: SLF001


def gather_nodes_and_ios_from_package(
    package: ModuleType,
) -> tuple[set[Node], dict[str, IO | Input | Output]]:
    """Gather all nodes and IOs from the provided package.

    Args:
        package: the Python package object

    Returns:
        a tuple of a set of `Node` objects and a dict of `IO` objects
    """
    module_names = [
        name for _, name, _ in pkgutil.iter_modules(package.__path__)
    ]
    modules = [
        importlib.import_module(f".{name}", package=package.__name__)
        for name in module_names
    ]
    ios = {}
    for m in modules:
        ios.update(gather_ios_from_module(m))

    # Gather nodes from the registry
    nodes = gather_nodes_from_registry()
    return nodes, ios
