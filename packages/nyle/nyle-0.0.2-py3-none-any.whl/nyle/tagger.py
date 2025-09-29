from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable
    from types import FunctionType
    from types import ModuleType
    from typing import TypeVar

    from _typeshed import Incomplete

    T = TypeVar("T", type, FunctionType)


def add_metadata(
    *, field_name: str = "metadata", **metadata: object
) -> Callable[[T], T]:
    def inner(t: T) -> T:
        if not metadata:
            msg = f"You forgot to pass in metadata to '{t.__qualname__}'!"
            raise TypeError(msg)
        setattr(t, field_name, metadata)
        return t

    return inner


def find_with_metadata(
    obj: object | ModuleType, field_name: str = "metadata", /
) -> dict[Incomplete, Incomplete]:
    ret: dict[Incomplete, Incomplete] = {}
    for attribute_name in dir(obj):
        attribute = getattr(obj, attribute_name)
        metadata = getattr(attribute, field_name, None)
        if metadata is not None:
            ret[attribute] = metadata

    return ret
