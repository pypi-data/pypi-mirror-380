"""
Core functions for loading and working with settings.
"""

from typing import Any

from ._core import SettingsState, convert, default_loaders, load, load_settings
from ._file_utils import find
from .cli_argparse import cli
from .cls_utils import resolve_types
from .converters import default_converter, register_strlist_hook
from .loaders import EnvLoader, FileLoader, TomlFormat
from .types import Secret, SecretStr


_attrs_imports = {"combine", "evolve", "option", "secret", "settings"}
_click_imports = {"click_options", "pass_settings"}

try:
    from .cls_attrs import combine, evolve, option, secret, settings
except ImportError:
    pass

try:
    from .cli_click import click_options, pass_settings
except ImportError:
    pass


def __getattr__(name: str) -> Any:
    """
    Raise a helpful :exc:`ModuleNotFound` error when getting something that requires an
    optional dependency that is not installed.
    """
    # This method is only invoked if either
    # - attrs/click is not installed or
    # - an attribute that actually doesn't exist
    # is requested.
    if name in _attrs_imports:
        raise ModuleNotFoundError(
            "Module 'attrs' not installed.  Please run "
            "'python -m pip install -U typed-settings[attrs]'"
        )

    if name in _click_imports:
        raise ModuleNotFoundError(
            "Module 'click' not installed.  Please run "
            "'python -m pip install -U typed-settings[click]'"
        )

    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


__all__ = [
    # Loaders
    "EnvLoader",
    "FileLoader",
    # Types
    "Secret",
    "SecretStr",
    # Core
    "SettingsState",
    "TomlFormat",
    # Argparse utils
    "cli",
    # Optional: click
    "click_options",
    # Optional: attrs
    "combine",
    "convert",
    # Cattrs converters/helpers
    "default_converter",
    "default_loaders",
    "evolve",
    # File utils
    "find",
    "load",
    "load_settings",
    "option",
    "pass_settings",
    "register_strlist_hook",
    # Class utils
    "resolve_types",
    "secret",
    "settings",
]


def __dir__() -> list[str]:
    return __all__
