from ordeq.framework import get_node

from ordeq_viz.gather import gather_nodes_and_ios_from_package
from ordeq_viz.to_mermaid import pipeline_to_mermaid


def test_mermaid():
    from example import nodes as mod  # ty: ignore[unresolved-import]

    diagram = pipeline_to_mermaid(
        nodes={get_node(mod.world)}, datasets={"x": mod.x, "y": mod.y}
    )

    assert diagram.startswith("graph TB")
    assert "world:::function" in diagram
    assert "[(x)]:::dataset0" in diagram
    assert "[(y)]:::dataset0" in diagram


def test_mermaid_wrapped():
    import example  # ty: ignore[unresolved-import]

    nodes, ios = gather_nodes_and_ios_from_package(example)
    diagram = pipeline_to_mermaid(nodes=nodes, datasets=ios)

    assert "-.->|name|" in diagram
    assert "-.->|writer|" in diagram

    diagram = pipeline_to_mermaid(
        nodes=nodes, datasets=ios, connect_wrapped_datasets=False
    )

    assert "-.->|name|" not in diagram
    assert "-.->|writer|" not in diagram
