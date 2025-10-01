from ordeq.framework import get_node
from ordeq_common import StringBuffer

from ordeq_viz.gather import (
    gather_ios_from_module,
    gather_nodes_and_ios_from_package,
    gather_nodes_from_registry,
)


def test_gather_ios_from_module():
    from example import catalog as mod  # ty: ignore[unresolved-import]

    datasets = gather_ios_from_module(mod)

    assert len(datasets) == 4
    assert isinstance(datasets["Hello"], StringBuffer)
    assert isinstance(datasets["World"], StringBuffer)
    assert datasets["TestInput"].__class__.__name__ == "MockInput"
    assert datasets["TestOutput"].__class__.__name__ == "MockOutput"


def test_gather_nodes_from_module():
    from example import nodes as mod  # ty: ignore[unresolved-import]

    nodes = gather_nodes_from_registry()

    assert len(nodes) >= 1
    assert get_node(mod.world) in nodes


def test_gather_nodes_and_ios_from_package(
    expected_example_nodes, expected_example_ios
) -> None:
    """Test gathering nodes and IOs from a package."""
    import example  # ty: ignore[unresolved-import]

    nodes, ios = gather_nodes_and_ios_from_package(example)
    assert expected_example_nodes == {n.func for n in nodes}
    assert expected_example_ios == ios
