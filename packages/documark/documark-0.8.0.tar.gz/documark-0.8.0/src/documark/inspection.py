r"""
"""


#[

from __future__ import annotations

import functools as _ft

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from collections.abc import Callable

#]


def _list_some_names(
    namespace: type,
    test: Callable,
) -> tuple[str, ...]:
    r"""
    Find all undocumented methods of a class
    """
    return tuple(
        name for name in dir(namespace, )
        if not name.startswith("_") and test(getattr(namespace, name, ), )
    )


def _is_documented_callable(obj: Any, ) -> bool:
    return callable(obj) and getattr(obj, "_documark_reference", False, )


def _is_undocumented_callable(obj: Any, ) -> bool:
    return callable(obj) and not getattr(obj, "_documark_reference", False, )


list_documented_methods = _ft.partial(_list_some_names, test=_is_documented_callable, )
list_undocumented_methods = _ft.partial(_list_some_names, test=_is_undocumented_callable, )

