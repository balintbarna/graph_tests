from pytest import raises
from toml import loads as load_toml
#
from graphit import LocalGraph, HierarchyView


with open("simple_scene.toml", encoding='utf-8') as file:
    data = load_toml(file.read())


def test_get_parent():
    graph = LocalGraph.from_data(**data)
    hierarhcy = HierarchyView(graph)
    assert hierarhcy.get_parent('child1') == 'root'
    assert hierarhcy.get_parent('child2') == 'root'
    with raises(ValueError):
        _ = hierarhcy.get_parent('root')


def test_change_tree_structure():
    graph = LocalGraph.from_data(**data)
    hierarhcy = HierarchyView(graph)
    hierarhcy = hierarhcy.set_parent('child2', 'child1')
    assert hierarhcy.get_parent('child1') == 'root'
    assert hierarhcy.get_parent('child2') == 'child1'
    with raises(ValueError):
        _ = hierarhcy.get_parent('root')
