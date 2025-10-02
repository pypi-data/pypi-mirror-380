import logging
from collections.abc import Callable, Iterator
from dataclasses import Field, fields
from functools import lru_cache
from typing import Any, Iterable
from warnings import warn

log = logging.getLogger(__name__)


def compare(attr, a, b, strict: bool) -> bool:
    """Return :obj:`True` if ``a.attr`` == ``b.attr``.

    If strict is :obj:`False`, :obj:`None` is permissible as `a` or `b`; otherwise,

    .. deprecated:: 2.23.0

       Use :meth:`.Comparable.compare` or :func:`.compare` instead.
    """
    warn(
        "sdmx.util.compare(); use sdmx.compare instead",
        DeprecationWarning,
        stacklevel=2,
    )
    return getattr(a, attr) == getattr(b, attr) or (
        not strict and None in (getattr(a, attr), getattr(b, attr))
    )


def only(iterator: Iterator) -> Any:
    """Return the only element of `iterator`, or :obj:`None`."""
    try:
        result = next(iterator)
        flag = object()
        assert flag is next(iterator, flag)
    except (StopIteration, AssertionError):
        return None  # 0 or ≥2 matches
    else:
        return result


@lru_cache()
def parse_content_type(value: str) -> tuple[str, dict[str, Any]]:
    """Return content type and parameters from `value`.

    Modified from :mod:`requests.util`.
    """
    # FIXME handle a value like text/html,application/xhtml+xml,application/xml;q=0.9,
    #       image/avif,image/webp,*/*;q=0.8
    tokens = value.split(";")
    content_type, params_raw = tokens[0].strip(), tokens[1:]
    params = {}
    to_strip = "\"' "

    for param in params_raw:
        k, *v = param.strip().split("=")

        if not k and not v:
            continue

        params[k.strip(to_strip).lower()] = v[0].strip(to_strip) if len(v) else True

    return content_type, params


def ucfirst(value: str) -> str:
    """Return `value` with its first character transformed to upper-case."""
    return value[0].upper() + value[1:]


_FIELDS_CACHE: dict[str, list[Field]] = dict()


def direct_fields(cls) -> Iterable[Field]:
    """Return the data class fields defined on `cls` or its class.

    This is like the ``__fields__`` attribute, but excludes the fields defined on any
    parent class(es).
    """
    # Key for `_FIELDS_CACHE`: the fully qualified name
    cls_name = f"{cls.__module__}.{cls.__name__}"

    try:
        return _FIELDS_CACHE[cls_name]
    except KeyError:
        parent_fields = set(fields(cls.mro()[1]))
        result = list(filter(lambda f: f not in parent_fields, fields(cls)))
        return _FIELDS_CACHE.setdefault(cls_name, result)


def preserve_dunders(cls: type, *names: str) -> Callable[[type], type]:
    """Copy dunder `names` from `cls` to a decorated class."""

    def decorator(other_cls: type) -> type:
        for name in map(lambda s: f"__{s}__", names):
            candidates: Iterator[Callable] = filter(
                None, map(lambda k: getattr(k, name), cls.__mro__)
            )
            setattr(other_cls, name, next(candidates))
        return other_cls

    return decorator
