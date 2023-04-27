from graphit import Edge, LocalEdge, Graph, LocalGraph


def test_local_edge():
    assert issubclass(LocalEdge, Edge)


def test_local_graph():
    assert issubclass(LocalGraph, Graph)
