"""Utilities for wrapping the pandas based *ta* library with Polars friendly APIs."""
from __future__ import annotations

import inspect
from functools import wraps
from typing import Any, Callable, Dict, Iterable

import pandas as pd
import polars as pl

from ta.utils import IndicatorMixin


def _convert_input(value: Any) -> Any:
    """Convert Polars inputs to pandas equivalents recursively."""
    if isinstance(value, pl.Series):
        return value.to_pandas()
    if isinstance(value, pl.DataFrame):
        return value.to_pandas()
    if isinstance(value, (list, tuple)):
        converted = [_convert_input(item) for item in value]
        return type(value)(converted)  # preserve tuple/list type
    if isinstance(value, dict):
        return {key: _convert_input(val) for key, val in value.items()}
    return value


def _convert_output(value: Any) -> Any:
    """Convert pandas outputs to Polars equivalents recursively."""
    if isinstance(value, pd.Series):
        name = value.name if value.name is not None else ""
        return pl.Series(name, value.to_numpy())
    if isinstance(value, pd.DataFrame):
        return pl.DataFrame(value)
    if isinstance(value, (list, tuple)):
        converted = [_convert_output(item) for item in value]
        return type(value)(converted)
    if isinstance(value, dict):
        return {key: _convert_output(val) for key, val in value.items()}
    return value


def _wrap_callable(func: Callable[..., Any]) -> Callable[..., Any]:
    """Wrap a callable so that it accepts Polars inputs and returns Polars outputs."""

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        converted_args = tuple(_convert_input(arg) for arg in args)
        converted_kwargs = {key: _convert_input(val) for key, val in kwargs.items()}
        result = func(*converted_args, **converted_kwargs)
        return _convert_output(result)

    return wrapper


def wrap_class(cls: type) -> type:
    """Create a Polars friendly wrapper class for a pandas based indicator class."""

    if not inspect.isclass(cls):
        raise TypeError("wrap_class expects a class instance")

    class WrappedIndicator:
        """Polars aware proxy for ``{}``.""".format(cls.__name__)

        def __init__(self, *args: Any, **kwargs: Any) -> None:
            converted_args = tuple(_convert_input(arg) for arg in args)
            converted_kwargs = {key: _convert_input(val) for key, val in kwargs.items()}
            self._indicator = cls(*converted_args, **converted_kwargs)

        def __getattr__(self, name: str) -> Any:
            attribute = getattr(self._indicator, name)
            if callable(attribute):
                return _wrap_callable(attribute)
            return attribute

        def __dir__(self) -> Iterable[str]:
            base_dir = set(super().__dir__())
            base_dir.update(dir(self._indicator))
            return sorted(base_dir)

    WrappedIndicator.__name__ = cls.__name__
    WrappedIndicator.__qualname__ = cls.__qualname__
    WrappedIndicator.__module__ = cls.__module__
    WrappedIndicator.__doc__ = cls.__doc__
    return WrappedIndicator


def build_wrapped_namespace(module: Any) -> Dict[str, Any]:
    """Return a dict with wrapped objects from a TA module."""
    wrapped: Dict[str, Any] = {}
    for name, obj in inspect.getmembers(module):
        if name.startswith("_"):
            continue
        if inspect.isclass(obj) and issubclass(obj, IndicatorMixin):
            wrapped[name] = wrap_class(obj)
        elif inspect.isfunction(obj):
            wrapped[name] = _wrap_callable(obj)
        else:
            wrapped[name] = obj
    return wrapped
