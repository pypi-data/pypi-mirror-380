"""Polars compatible wrappers for :mod:`ta.others`."""
from __future__ import annotations

from ta import others as _pandas_module

from ._wrapping import build_wrapped_namespace


globals().update(build_wrapped_namespace(_pandas_module))

__all__ = [name for name in globals() if not name.startswith("_")]
