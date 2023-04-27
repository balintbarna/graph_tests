from dataclasses import dataclass, replace
#
from .graph_interfaces import HIERARCHY, Graph
from .graph_components import LocalEdge, LocalGraph


asd = LocalGraph({}, [])
xasd = (a for a in asd.get_edges())


@dataclass(frozen=True)
class HierarchyView:
    graph: Graph

    def get_parent(self, uri: str):
        query = (edge.get_from() for edge in self.graph.get_edges()
                if edge.get_relationship() == HIERARCHY and edge.get_to() == uri)
        try:
            result = next(query)
        except StopIteration:
            raise ValueError(f"The node {uri} does not have a parent.")
        try:
            _ = next(query)
        except StopIteration:
            return result
        raise ValueError(f"The node {uri} has multiple parents.")

    def set_parent(self, uri: str, new_parent_uri: str):
        without_parent = (edge for edge in self.graph.get_edges() if edge.get_to() != uri)
        with_new_parent = (*without_parent, LocalEdge(new_parent_uri, uri, HIERARCHY))
        return HierarchyView(self.graph.set_edges(with_new_parent))

    def get_children(self, uri: str):
        return (edge.get_to() for edge in self.graph.get_edges() if edge.get_from() == uri)
