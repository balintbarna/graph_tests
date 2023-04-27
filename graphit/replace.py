from dataclasses import replace
# for NamedTuple use x._replace(**kw)
from frozendict import frozendict


def set_values(data, **new_values):
    return frozendict(**data, **new_values)


def delete_keys(data, *keys):
    return frozendict({k: v for k, v in data.items() if k not in keys})


def delete_values(data, *values):
    return frozendict({k: v for k, v in data.items() if k not in values})
