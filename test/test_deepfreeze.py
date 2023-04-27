from frozendict import frozendict
#
from graphit import deepfreeze


def test_on_imple_data():
    assert deepfreeze(None) is None
    assert deepfreeze(True) is True
    assert deepfreeze(2) is 2
    assert deepfreeze(2.) is 2.
    assert deepfreeze("asd") is "asd"
    assert deepfreeze(b"asd") is b"asd"


def test_on_dict():
    result = deepfreeze({'a': {'b': {}}})
    assert isinstance(result, frozendict)
    assert isinstance(result['a'], frozendict)
    assert isinstance(result['a']['b'], frozendict)


def test_on_list():
    result = deepfreeze([[[]], []])
    assert isinstance(result, tuple)
    assert isinstance(result[0], tuple)
    assert isinstance(result[0][0], tuple)
    assert isinstance(result[1], tuple)


def test_on_other_containers():
    assert isinstance(deepfreeze(set()), tuple)
    assert isinstance(deepfreeze(frozenset()), tuple)
    assert isinstance(deepfreeze(tuple()), tuple)
