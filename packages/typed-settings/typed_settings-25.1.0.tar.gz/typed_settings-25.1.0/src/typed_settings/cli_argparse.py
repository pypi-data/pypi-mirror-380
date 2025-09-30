"""
Utilities for generating an :mod:`argparse` based CLI.

.. versionadded:: 2.0.0
"""

import argparse
import itertools
import re
from collections.abc import Collection, Iterable, Mapping, Sequence
from datetime import date, datetime, timedelta
from enum import Enum
from functools import partial, wraps
from pathlib import Path
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Optional,
    Union,
    get_args,
    get_origin,
)

from ._compat import PY_311


if TYPE_CHECKING:
    from argparse import FileType

from . import _core, converters
from .cli_utils import (
    NO_DEFAULT,
    Default,
    DefaultFactorySentinel,
    StrDict,
    TypeArgsMaker,
    TypeHandlerFunc,
    get_default,
)
from .constants import ARGPARSE_METADATA_KEY as METADATA_KEY
from .converters import Converter
from .loaders import Loader
from .processors import Processor
from .types import (
    SECRET_REPR,
    ST,
    LoadedValue,
    LoaderMeta,
    MergedSettings,
    OptionInfo,
    Secret,
)


if PY_311:
    from enum import IntEnum, StrEnum
else:
    IntEnum = StrEnum = None  # type: ignore


__all__ = [
    "DEFAULT_TYPES",
    "ArgparseHandler",
    "BooleanOptionalAction",
    "DictItemAction",
    "ListAction",
    "cli",
    "handle_datetime",
    "handle_enum",
    "handle_enum_by_name",
    "handle_enum_by_value",
    "handle_path",
    "handle_pattern",
    "handle_secret",
    "make_parser",
    "namespace2settings",
]


WrapppedFunc = Callable[[ST], Any]
CliFn = Callable[[ST], Any]
DecoratedCliFn = Callable[[], Optional[int]]


def handle_datetime(typ: type, default: Default, is_optional: bool) -> StrDict:
    """
    Handle isoformatted datetimes.
    """
    kwargs: StrDict = {
        "type": partial(converters.to_datetime, cls=datetime),
        "metavar": "YYYY-MM-DD[Thh:mm:ss[+xx:yy]]",
    }
    if isinstance(default, datetime):
        kwargs["default"] = default.isoformat()
    elif is_optional:
        kwargs["default"] = None
    return kwargs


def handle_date(typ: type, default: Default, is_optional: bool) -> StrDict:
    """
    Handle isoformatted datetimes.
    """
    kwargs: StrDict = {
        "type": partial(converters.to_date, cls=date),
        "metavar": "YYYY-MM-DD",
    }
    if isinstance(default, date):
        kwargs["default"] = default.isoformat()
    elif is_optional:
        kwargs["default"] = None
    return kwargs


def handle_timedelta(typ: type, default: Default, is_optional: bool) -> StrDict:
    """
    Handle isoformatted datetimes.
    """
    kwargs: StrDict = {
        "type": partial(converters.to_timedelta, cls=timedelta),
        "metavar": "[-][Dd][HHh][MMm][SS[.ffffff]s]",
    }
    if isinstance(default, timedelta):
        kwargs["default"] = converters.timedelta_to_str(default)
    elif is_optional:
        kwargs["default"] = None
    return kwargs


def handle_enum_by_name(
    typ: type[Enum], default: Default, is_optional: bool
) -> StrDict:
    """
    Use *choices* as option type and use the enum value's name as default.
    """
    kwargs: StrDict = {"choices": [str(k) for k in typ.__members__]}
    if isinstance(default, typ):
        # Convert Enum instance to string
        kwargs["default"] = default.name
    elif is_optional:
        kwargs["default"] = None

    return kwargs


handle_enum = handle_enum_by_name


def handle_enum_by_value(
    typ: type[Enum], default: Default, is_optional: bool
) -> StrDict:
    """
    Use *choices* as option type and use the enum value's name as default.
    """
    kwargs: StrDict = {"choices": [str(v) for v in typ.__members__.values()]}
    if isinstance(default, typ):
        # Convert Enum instance to string
        kwargs["default"] = default.value
    elif is_optional:
        kwargs["default"] = None

    return kwargs


def handle_path(typ: type[Path], default: Default, is_optional: bool) -> StrDict:
    """
    Handle :class:`pathlib.Path` and also use proper metavar.
    """
    kwargs: StrDict = {"type": typ, "metavar": "PATH"}
    if isinstance(default, (Path, str)):
        kwargs["default"] = str(default)
    elif is_optional:
        kwargs["default"] = None

    return kwargs


def handle_pattern(
    typ: type[re.Pattern], default: Default, is_optional: bool
) -> StrDict:
    """
    Use "re.compile()" as func param type so that the resulting value is a
    :class:`re.Pattern`.
    """
    kwargs: StrDict = {
        "type": re.compile,
        "metavar": "PATTERN",
    }
    if isinstance(default, typ):
        # Convert Enum instance to string
        kwargs["default"] = default.pattern

    elif is_optional:
        kwargs["default"] = None

    return kwargs


def handle_secret(typ: type[Secret], default: Default, is_optional: bool) -> StrDict:
    """
    Handle :class:`typed_settings.types.Secret` types.
    """
    metavar = "SECRET"
    if isinstance(typ, type):
        cli_type = Secret
        has_default = isinstance(default, typ)
    else:
        secret_type = get_args(typ)[0]
        cli_type = lambda v: Secret(secret_type(v))  # noqa: E731
        if secret_type is not str:
            metavar = f"SECRET_{secret_type.__name__.upper()}"
        has_default = isinstance(default, get_origin(typ))

    kwargs: StrDict = {
        "type": cli_type,
        "metavar": metavar,
    }
    if has_default:
        kwargs["default"] = default.get_secret_value()  # type: ignore[union-attr]
        kwargs["is_secret"] = True

    elif is_optional:
        kwargs["default"] = None

    return kwargs


#: Default handlers for argparse option types.
DEFAULT_TYPES: dict[type, TypeHandlerFunc] = {
    datetime: handle_datetime,
    date: handle_date,
    timedelta: handle_timedelta,
    **(
        {
            IntEnum: handle_enum_by_value,
            StrEnum: handle_enum_by_value,
        }
        if PY_311
        else {}
    ),
    Enum: handle_enum_by_name,
    Path: handle_path,
    re.Pattern: handle_pattern,
    Secret: handle_secret,
}


class ArgparseHandler:
    """
    Implementation of the :class:`~typed_settings.cli_utils.TypeHandler`
    protocol for Click.

    Args:
        extra_types: A dict mapping types to specialized handler functions.
            Use :data:`DEFAULT_TYPES` by default.
    """

    def __init__(
        self, extra_types: Optional[dict[type, TypeHandlerFunc]] = None
    ) -> None:
        self.extra_types = extra_types or DEFAULT_TYPES

    def get_scalar_handlers(self) -> dict[type, TypeHandlerFunc]:
        return self.extra_types

    def handle_scalar(
        self,
        type: Optional[type],
        default: Default,
        is_optional: bool,
    ) -> StrDict:
        kwargs: StrDict = {"type": type}
        if type is not None:
            if issubclass(type, str):
                kwargs["metavar"] = "TEXT"
            else:
                kwargs["metavar"] = str(type.__name__).upper()

        # if default is not None or is_optional:
        if default not in (None, NO_DEFAULT):
            kwargs["default"] = default
        elif is_optional:
            kwargs["default"] = None
        if type and issubclass(type, bool):
            kwargs["action"] = BooleanOptionalAction

        return kwargs

    def handle_literal(
        self, type: Optional[type], default: Default, is_optional: bool
    ) -> StrDict:
        """
        Use "choices" as option type and use the literal's values as choices.
        """
        values = get_args(type)
        if not all(isinstance(v, str) for v in values):
            raise ValueError(f"All Literal values must be strings: {values!r}")
        kwargs: StrDict = {"choices": [str(v) for v in values]}
        if default in values:
            kwargs["default"] = default
        elif is_optional:
            kwargs["default"] = None

        return kwargs

    def handle_tuple(
        self,
        type_args_maker: TypeArgsMaker,
        types: tuple[Any, ...],
        default: Optional[tuple],
        is_optional: bool,
    ) -> StrDict:
        metavar = tuple(
            "TEXT" if issubclass(t, str) else str(t.__name__).upper() for t in types
        )
        kwargs = {
            "metavar": metavar,
            "nargs": len(types),
            "default": default,
        }
        return kwargs

    def handle_collection(
        self,
        type_args_maker: TypeArgsMaker,
        types: tuple[Any, ...],
        default: Optional[Collection[Any]],
        is_optional: bool,
    ) -> StrDict:
        kwargs = type_args_maker.get_kwargs(types[0], NO_DEFAULT)
        kwargs["default"] = default or []  # Don't use None as default
        kwargs["action"] = ListAction
        return kwargs

    def handle_mapping(
        self,
        type_args_maker: TypeArgsMaker,
        types: tuple[Any, ...],
        default: Default,
        is_optional: bool,
    ) -> StrDict:
        kwargs = {
            "metavar": "KEY=VALUE",
            "action": DictItemAction,
        }
        if not isinstance(default, Mapping):
            default = {}
        kwargs["default"] = default
        kwargs["default_repr"] = ", ".join(f"{k}={v}" for k, v in default.items())

        return kwargs


def cli(
    settings_cls: type[ST],
    loaders: Union[str, Sequence[Loader]],
    *,
    processors: Sequence[Processor] = (),
    converter: Optional[Converter] = None,
    base_dir: Path = Path(),
    type_args_maker: Optional[TypeArgsMaker] = None,
    **parser_kwargs: Any,
) -> Callable[[CliFn[ST]], DecoratedCliFn]:
    r"""
    **Decorator:** Generate an argument parser for the options of the given
    settings class and pass an instance of that class to the decorated
    function.

    Args:
        settings_cls: The settings class to generate options for.

        loaders: Either a string with your app name or a list of
            :class:`.Loader`\ s.  If it's a string, use it with
            :func:`~typed_settings.default_loaders()` to get the default
            loaders.

        processors: A list of settings :class:`.Processor`'s.

        converter: An optional :class:`.Converter` used for converting option values to
            the required type.

            By default, :data:`typed_settings.default_converter()` is used.

        base_dir: Base directory for resolving relative paths in default option values.

        type_args_maker: The type args maker that is used to generate keyword
            arguments for :func:`click.option()`.  By default, use
            :class:`.TypeArgsMaker` with :class:`ArgparseHandler`.

        **parser_kwargs: Additional keyword arguments to pass to the
            :class:`argparse.ArgumentParser`.

    Return:
        A decorator for an argparse CLI function.

    Raise:
        InvalidSettingsError: If an instance of *cls* cannot be created for the given
            settings.

    Example:
        .. code-block:: python

           import typed_settings as ts

           @ts.settings
           class Settings: ...

           @ts.cli(Settings, "example")
           def cli(settings: Settings) -> None:
               print(settings)

    .. versionchanged:: 23.0.0
       Made *converter* and *type_args_maker* a keyword-only argument
    .. versionchanged:: 23.0.0
       Added the *processors* argument
    .. versionchanged:: 23.1.0
       Added the *base_dir* argument
    """
    if isinstance(loaders, str):
        loaders = _core.default_loaders(loaders)
    converter = converter or converters.default_converter()
    state = _core.SettingsState(settings_cls, loaders, processors, converter, base_dir)
    type_args_maker = type_args_maker or TypeArgsMaker(ArgparseHandler())

    decorator = _get_decorator(state, type_args_maker, **parser_kwargs)
    return decorator


def make_parser(
    settings_cls: type[ST],
    loaders: Union[str, Sequence[Loader]],
    *,
    processors: Sequence[Processor] = (),
    converter: Optional[Converter] = None,
    base_dir: Path = Path(),
    type_args_maker: Optional[TypeArgsMaker] = None,
    **parser_kwargs: Any,
) -> tuple[argparse.ArgumentParser, MergedSettings]:
    r"""
    Return an argument parser for the options of the given settings class.

    Use :func:`namespace2settings()` to convert the parser's namespace to an
    instance of the settings class.

    Args:
        settings_cls: The settings class to generate options for.

        loaders: Either a string with your app name or a list of
            :class:`.Loader`\ s.  If it's a string, use it with
            :func:`~typed_settings.default_loaders()` to get the default
            loaders.

        processors: A list of settings :class:`.Processor`'s.

        converter: An optional :class:`.Converter` used for converting option values to
            the required type.

            By default, :data:`typed_settings.default_converter()` is used.

        base_dir: Base directory for resolving relative paths in default option values.

        type_args_maker: The type args maker that is used to generate keyword
            arguments for :func:`click.option()`.  By default, use
            :class:`.TypeArgsMaker` with :class:`ArgparseHandler`.

        **parser_kwargs: Additional keyword arguments to pass to the
            :class:`argparse.ArgumentParser`.

    Return:
        An argument parser configured with with an argument for each option of
        *settings_cls*.

    Raise:
        InvalidSettingsError: If an instance of *cls* cannot be created for the given
            settings.

    .. versionchanged:: 23.0.0
       Made *converter* and *type_args_maker* a keyword-only argument
    .. versionchanged:: 23.0.0
       Added the *processors* argument
    .. versionchanged:: 23.1.0
       Added the *base_dir* argument
    """
    if isinstance(loaders, str):
        loaders = _core.default_loaders(loaders)
    converter = converter or converters.default_converter()
    state = _core.SettingsState(settings_cls, loaders, processors, converter, base_dir)
    type_args_maker = type_args_maker or TypeArgsMaker(ArgparseHandler())

    return _mk_parser(state, type_args_maker, **parser_kwargs)


def namespace2settings(
    settings_cls: type[ST],
    namespace: argparse.Namespace,
    *,
    merged_settings: MergedSettings,
    converter: Optional[Converter] = None,
    base_dir: Path = Path(),
) -> ST:
    """
    Create a settings instance from an argparse namespace.

    To be used together with :func:`make_parser()`.

    Args:
        settings_cls: The settings class to instantiate.
        namespace: The namespace returned by the argument parser.
        merged_settings: The loaded and merged settings by settings name.
        converter: An optional :class:`.Converter` used for converting option values to
            the required type.  By default, :data:`typed_settings.default_converter()`
            is used.
        base_dir: Base directory for resolving relative paths in default option values.

    Raise:
        InvalidSettingsError: If an instance of *cls* cannot be created for the given
            settings.

    Return: An instance of *settings_cls*.

    .. versionchanged:: 23.1.0
       Added the *base_dir* argument
    """
    converter = converter or converters.default_converter()
    state = _core.SettingsState(settings_cls, [], [], converter, base_dir)
    return _ns2settings(namespace, state, merged_settings)


def _get_decorator(
    state: _core.SettingsState[ST],
    type_args_maker: TypeArgsMaker,
    **parser_kwargs: Any,
) -> Callable[[CliFn], DecoratedCliFn]:
    """
    Build the CLI decorator based on the user's config.
    """

    def decorator(func: CliFn) -> DecoratedCliFn:
        """
        Create an argument parsing wrapper for *func*.

        The wrapper

        - loads settings as default option values
        - creates an argument parser with an option for each setting
        - parses the command line options
        - passes the updated settings instance to the decorated function
        """

        @wraps(func)
        def cli_wrapper() -> Optional[int]:
            if "description" not in parser_kwargs and func.__doc__:
                parser_kwargs["description"] = func.__doc__.strip()
            parser, merged_settings = _mk_parser(
                state, type_args_maker, **parser_kwargs
            )

            args = parser.parse_args()
            settings = _ns2settings(args, state, merged_settings)
            return func(settings)

        return cli_wrapper

    return decorator


def _mk_parser(
    state: _core.SettingsState[ST],
    type_args_maker: TypeArgsMaker,
    **parser_kwargs: Any,
) -> tuple[argparse.ArgumentParser, MergedSettings]:
    """
    Create an :class:`argparse.ArgumentParser` for all options.
    """
    merged_settings = _core._load_settings(state)
    grouped_options = [
        (g_cls, list(g_opts))
        for g_cls, g_opts in itertools.groupby(
            state.options, key=lambda o: o.parent_cls
        )
    ]
    parser = argparse.ArgumentParser(**parser_kwargs)
    for g_cls, g_opts in grouped_options:
        group = parser.add_argument_group(g_cls.__name__, f"{g_cls.__name__} options")
        for oinfo in g_opts:
            default = get_default(oinfo, merged_settings, state.converter)
            flags, cfg = _mk_argument(oinfo, default, type_args_maker)
            group.add_argument(*flags, **cfg)
    return (parser, merged_settings)


def _mk_argument(
    oinfo: OptionInfo,
    default: Default,
    type_args_maker: TypeArgsMaker,
) -> tuple[tuple[str, ...], dict[str, Any]]:
    user_config = dict(oinfo.metadata.get(METADATA_KEY, {}))

    # The option type specifies the default option kwargs
    kwargs = type_args_maker.get_kwargs(oinfo.cls, default)

    param_decls: tuple[str, ...]
    user_param_decls: Union[str, Sequence[str]]
    user_param_decls = user_config.pop("param_decls", ())
    if not user_param_decls:
        option_name = oinfo.path.replace(".", "-").replace("_", "-")
        param_decls = (f"--{option_name}",)
    elif isinstance(user_param_decls, str):
        param_decls = (user_param_decls,)
    else:
        param_decls = tuple(user_param_decls)

    # Get "help" from the user_config *now*, because we may need to update it
    # below.  Also replace "None" with "".
    kwargs["help"] = user_config.pop("help", None) or ""
    is_secret = any([oinfo.is_secret, kwargs.pop("is_secret", False)])
    if "default" in kwargs and kwargs["default"] is not NO_DEFAULT:
        default_repr = kwargs.pop("default_repr", kwargs["default"])
        if kwargs["default"] is None:
            help_extra = ""
        elif is_secret:
            help_extra = f" [default: ({SECRET_REPR})]"
        elif isinstance(callable(kwargs["default"]), DefaultFactorySentinel):
            help_extra = "[default: (dynamic)]"
        else:
            help_extra = f" [default: {default_repr}]"
        if kwargs["default"] not in (None, (), [], {}):
            kwargs["default"] = DefaultFactorySentinel()
    else:
        kwargs["required"] = True
        help_extra = " [required]"
    kwargs["help"] = f"{kwargs['help']}{help_extra}"

    # The user has the last word, though.
    kwargs.update(user_config)

    return (param_decls, kwargs)


def _ns2settings(
    namespace: argparse.Namespace,
    state: _core.SettingsState[ST],
    merged_settings: MergedSettings,
) -> ST:
    """
    Convert the :class:`argparse.Namespace` to an instance of the settings
    class and return it.
    """
    meta = LoaderMeta("Command line args")
    for option_info in state.options:
        path = option_info.path
        attr = path.replace(".", "_")
        if hasattr(namespace, attr):  # pragma: no cover
            # "path" *should* always be in "cli_options", b/c we *currently*
            # generate CLI options for all options.  But let's stay safe here
            # in case the behavior changes in the future.
            value = getattr(namespace, attr)
            if not isinstance(value, DefaultFactorySentinel):
                merged_settings[path] = LoadedValue(value, meta)
    settings = _core.convert(merged_settings, state)
    return settings


class BooleanOptionalAction(argparse.Action):
    """
    An argparse action for handling boolean flags.
    """

    def __init__(
        self,
        option_strings: Sequence[str],
        dest: str,
        default: Default = None,
        type: Union[Callable[[str], Any], "FileType", None] = None,
        choices: Optional[Iterable[Any]] = None,
        required: bool = False,
        help: Optional[str] = None,
        metavar: Union[str, tuple[str, ...], None] = None,
    ) -> None:
        _option_strings = []
        for option_string in option_strings:
            _option_strings.append(option_string)

            if not option_string.startswith("--"):
                raise ValueError(
                    f"Only boolean flags starting with '--' are supported: "
                    f"{option_string}"
                )
            option_string = "--no-" + option_string[2:]
            _option_strings.append(option_string)

        super().__init__(
            option_strings=_option_strings,
            dest=dest,
            nargs=0,
            default=default,
            type=type,
            choices=choices,
            required=required,
            help=help,
            metavar=metavar,
        )

    def __call__(
        self,
        parser: argparse.ArgumentParser,
        namespace: argparse.Namespace,
        values: Union[str, Sequence[Any], None],
        option_string: Optional[str] = None,
    ) -> None:
        if option_string and option_string in self.option_strings:  # pragma: no cover
            setattr(namespace, self.dest, not option_string.startswith("--no-"))

    def format_usage(self) -> str:
        return " | ".join(self.option_strings)


class ListAction(argparse.Action):
    """
    An argparse action for handling lists.
    """

    def __init__(
        self,
        option_strings: Sequence[str],
        dest: str,
        nargs: Union[int, str, None] = None,
        default: Default = None,
        type: Union[Callable[[str], Any], "FileType", None] = None,
        choices: Optional[Iterable[Any]] = None,
        required: bool = False,
        help: Optional[str] = None,
        metavar: Union[str, tuple[str, ...], None] = None,
    ) -> None:
        if nargs == 0:  # pragma: no cover
            raise ValueError(f"nargs for append actions must be != 0: {nargs}")
        super().__init__(
            option_strings=option_strings,
            dest=dest,
            nargs=nargs,
            default=default,
            type=type,
            choices=choices,
            required=required,
            help=help,
            metavar=metavar,
        )

    def __call__(
        self,
        parser: argparse.ArgumentParser,
        namespace: argparse.Namespace,
        values: Union[str, Sequence[Any], None],
        option_string: Optional[str] = None,
    ) -> None:
        if values is None:
            return  # pragma: no cover

        items = getattr(namespace, self.dest, [])
        # Do not append to the defaults but create a new list!
        if items is self.default:
            items = []
        items.append(values)
        setattr(namespace, self.dest, items)


class DictItemAction(argparse.Action):
    """
    An argparse action for handling dicts.
    """

    def __init__(
        self,
        option_strings: Sequence[str],
        dest: str,
        default: Default = None,
        type: Union[Callable[[str], Any], "FileType", None] = None,
        choices: Optional[Iterable[Any]] = None,
        required: bool = False,
        help: Optional[str] = None,
        metavar: Union[str, tuple[str, ...], None] = None,
    ) -> None:
        super().__init__(
            option_strings=option_strings,
            dest=dest,
            nargs=1,
            default=default,
            type=type,
            choices=choices,
            required=required,
            help=help,
            metavar=metavar,
        )

    def __call__(
        self,
        parser: argparse.ArgumentParser,
        namespace: argparse.Namespace,
        values: Union[str, Sequence[Any], None],
        option_string: Optional[str] = None,
    ) -> None:
        if values is None:
            return  # pragma: no cover

        if isinstance(values, str):
            values = [values]  # pragma: no cover

        items = getattr(namespace, self.dest, {})
        # Do not append to the defaults but create a new list!
        if items is self.default:
            items = {}

        for value in values:
            k, _, v = value.partition("=")
            items[k] = v

        setattr(namespace, self.dest, items)
