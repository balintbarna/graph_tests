from typing import Mapping, NamedTuple, Sequence
#
from .deepfreeze import deepfreeze
from .graph_interfaces import Relationship, Edge


class LocalEdge(NamedTuple):
    from_node: str
    to_node: str
    relationship: Relationship

    def get_from(self):
        return self.from_node

    def get_to(self):
        return self.to_node

    def get_relationship(self):
        return self.relationship

    @classmethod
    def from_data(cls, **data):
        return cls(data['from'], data['to'], data['rel'])


RESERVED_KEYS = (
    'edges',
)


class LocalGraph(NamedTuple):
    nodes: Mapping[str, dict]
    edges: Sequence[Edge]

    def get_nodes(self):
        return self.nodes

    def get_edges(self):
        return self.edges

    def set_nodes(self, nodes: Mapping[str, dict]):
        return LocalGraph(nodes, self.edges)

    def set_edges(self, edges: Sequence[Edge]):
        return LocalGraph(self.nodes, edges)

    @classmethod
    def from_data(cls, **data):
        nodes = deepfreeze({k: v for k, v in data.items() if k not in RESERVED_KEYS})
        edges = tuple(LocalEdge.from_data(**edge) for edge in data['edges'])
        return cls(nodes, edges)
