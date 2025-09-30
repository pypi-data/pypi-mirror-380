"""
Converters and structure hooks for various data types.
"""

import collections.abc
import dataclasses
import re
from collections.abc import Iterable, Mapping, Sequence
from datetime import date, datetime, timedelta
from enum import Enum
from pathlib import Path
from types import MappingProxyType
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Literal,
    Optional,
    Protocol,
    TypeVar,
    Union,
    get_args,
    get_origin,
)

from ._compat import PY_310, PY_311


if PY_310:
    from types import UnionType
else:
    from typing import Union as UnionType  # type: ignore

if PY_311:
    from enum import IntEnum, StrEnum
else:
    IntEnum = StrEnum = None  # type: ignore

from .types import ET, Secret, T


if TYPE_CHECKING:
    import cattrs
    import pydantic


#: A TypeVar for :class:`~pathlib.Path` types
TPath = TypeVar("TPath", bound=Path)
#: A TypeVar for :class:`~typed_settings.types.Secret` types
TSecret = TypeVar("TSecret", bound=Secret)


class Converter(Protocol):
    """
    **Protocol** that converters must implement.

    Only a :meth:`structure()` method similar to the one from :program:`cattrs` is
    required.

    .. versionadded:: 23.1.0
    """

    def structure(self, obj: Any, cl: type[T]) -> T:
        """
        Convert *obj* to an instance of *cl* and return it.

        Args:
            obj: The data to be converted.
            cl: The type to convert *obj* to.

        Return:
            An instance of *cl* for *obj*.
        """
        ...


class TSConverter:
    """
    A simple converter that can replace :program:`cattrs` if you want to use
    Typed Settings without dependencies.

    It supports the same types as the default :program:`cattrs` converter.
    """

    def __init__(
        self,
        resolve_paths: bool = True,
        strlist_sep: Union[str, Callable[[str], list], None] = ":",
    ) -> None:
        if strlist_sep is None:
            self.strlist_hook: Optional[Callable[[str], list]] = None
        elif isinstance(strlist_sep, str):
            self.strlist_hook = lambda v: v.split(strlist_sep)  # type: ignore
        else:
            self.strlist_hook = strlist_sep

        self.scalar_converters: dict[Any, Callable[[Any, type], Any]] = {
            Any: to_any,
            **(
                {
                    IntEnum: to_enum_by_value,
                    StrEnum: to_enum_by_value,
                }
                if PY_311
                else {}
            ),
            Enum: to_enum_by_name,
            bool: to_bool,
            int: to_type,
            float: to_type,
            str: to_type,
            datetime: to_datetime,
            date: to_date,  # Must come after "datetime" b/c of subclassing!
            timedelta: to_timedelta,
            Path: to_resolved_path if resolve_paths else to_path,
            re.Pattern: to_pattern,
        }
        try:
            import pydantic

            self.scalar_converters[pydantic.SecretBytes] = to_pydantic_secretbytes
            self.scalar_converters[pydantic.SecretStr] = to_pydantic_secretstr
        except ImportError:
            pass

        self.composite_hook_factories: list[HookFactory] = [
            ListHookFactory,
            TupleHookFactory,
            DictHookFactory,
            MappingProxyTypeHookFactory,
            SetHookFactory,
            FrozenSetHookFactory,
            LiteralHookFactory,
            UnionHookFactory,
            AttrsHookFactory,
            DataclassesHookFactory,
            PydanticHookFactory,
            SecretHookFactory,
        ]

    def structure(self, obj: Any, cl: type[T]) -> T:
        """
        Convert *obj* to an instance of *cl* and return it.

        Args:
            obj: The data to be converted.
            cl: The type to convert *obj* to.

        Return:
            An instance of *cl* for *obj*.
        """
        for ctype, convert in self.scalar_converters.items():
            if cl is ctype or (
                ctype is not Any and isinstance(cl, type) and issubclass(cl, ctype)
            ):
                return convert(obj, cl)

        origin = get_origin(cl)
        args = get_args(cl)
        for hook in self.composite_hook_factories:
            if hook.match(cl, origin, args):
                convert = hook.get_structure_hook(self, cl, origin, args)
                return convert(obj, cl)

        raise TypeError(f"Cannot create converter for generic type: {cl}")

    def maybe_apply_strlist_hook(self, value: T) -> Union[list, T]:
        """
        Apply the string list hook to *value* if one is defined and if *value* is a
        string.
        """
        if self.strlist_hook and isinstance(value, str):
            return self.strlist_hook(value)
        return value


def default_converter(*, resolve_paths: bool = True) -> Converter:
    """
    Get a default instances of a converter which will be used to convert/structured
    the loaded settings.

    Args:
        resolve_paths: Whether or not to resolve relative paths.

    Return:
        If :program:`cattrs` is installed, a :class:`cattrs.Converter`.  Else, a
        :class:`TSConverter`.  The converters are configured to handle the following
        types:

        - :class:`bool` (see :func:`to_bool()` for supported inputs)
        - :class:`int`
        - :class:`float`
        - :class:`str`
        - :class:`datetime.datetime` (see :func:`to_datetime()`)
        - :class:`datetime.date` (see :func:`to_date()`)
        - :class:`datetime.timedelta` (see :func:`to_timedelta()`)
        - :class:`enum.Enum` (see :func:`to_enum_by_name()`)
        - :class:`enum.IntEnum` (see :func:`to_enum_by_value()`)
        - :class:`enum.StrEnum` (see :func:`to_enum_by_value()`)
        - :class:`pathlib.Path` (see :func:`to_path()` and :func:`to_resolved_path()`)
        - :class:`re.Pattern` (via :func:`re.compile()`)
        - :class:`typing.Literal` (for CLI generation, all values must be `str`).
        - :class:`typed_settings.types.Secret`
        - :class:`typed_settings.types.SecretStr`
        - :class:`list`
        - :class:`tuple`
        - :class:`dict`
        - :class:`types.MappingProxyType`/:class:`collections.abc.Mapping` ("read-only"
          dicts)
        - :class:`set`
        - :class:`frozenset`
        - :data:`typing.Optional`
        - :data:`typing.Union` (depending on the converter, only to a certain degree,
          but this should not be relevant for settings with clearly defined types)
        - :mod:`attrs` classes (from instances and dicts)

        :class:`list`, :class:`tuple`, :class:`set`, and :class:`frozenset` set can also
        be converted from strings.  By default, strings are split by ``:``.  See
        :class:`TSConverter` or :func:`register_strlist_hook()` for details.

    This converter can also be used as a base for converters with custom
    structure hooks.

    .. versionchanged:: 23.1.0
       Return a :program:`cattrs` converter if it is installed or else a Typed Settings
       converter.
    .. versionchanged:: 24.3.0
       Added :func:`to_date()` and :func:`to_timedelta()`.
    """
    try:
        import cattrs  # noqa: F401
    except ImportError:
        return get_default_ts_converter(resolve_paths=resolve_paths)
    else:
        return get_default_cattrs_converter(resolve_paths=resolve_paths)


def get_default_ts_converter(resolve_paths: bool = True) -> "TSConverter":
    """
    Return a :class:`TSConverter` with default settings
    (see :func:`default_converter()` for argument and return value description).

    Args:
        resolve_paths: Whether or not to resolve relative paths.

    Return:
        A :class:`TSConverter` instance with default configuration.
    """
    return TSConverter(resolve_paths=resolve_paths)


def get_default_cattrs_converter(resolve_paths: bool = True) -> "cattrs.Converter":
    """
    Return a :class:`cattrs.Converter` with default settings
    (see :func:`default_converter()` for argument and return value description).

    Args:
        resolve_paths: Whether or not to resolve relative paths.

    Return:
        A :class:`cattrs.Converter` instance with default configuration.

    Raises:
        ModuleNotFoundError: if :program:`cattrs` is not installed.
    """
    try:
        import cattrs
    except ImportError as e:
        raise ModuleNotFoundError(
            "Module 'cattrs' not installed.  Please run "
            "'python -m pip install -U typed-settings[cattrs]'"
        ) from e

    converter = cattrs.Converter()
    register_mappingproxy_hook(converter)
    register_attrs_hook_factory(converter)
    register_dataclasses_hook_factory(converter)
    register_pydantic_hook_factory(converter)
    register_strlist_hook(converter, ":")
    register_secret_hook(converter)
    for t, h in get_default_structure_hooks(resolve_paths=resolve_paths):
        converter.register_structure_hook(t, h)  # type: ignore
    return converter


def get_default_structure_hooks(
    *,
    resolve_paths: bool = True,
) -> list[tuple[type, Callable[[Any, type], Any]]]:
    """
    Return a list of default structure hooks for cattrs.

    Args:
        resolve_paths: Whether or not to resolve relative paths.

    Return:
        A list of tuples that can be used as args for
        :meth:`cattrs.BaseConverter.register_structure_hook()`.
    """
    path_hook = to_resolved_path if resolve_paths else to_path
    hooks: list[tuple[type, Callable[[Any, type], Any]]] = [
        *(
            [
                (IntEnum, to_enum_by_value),
                (StrEnum, to_enum_by_value),
            ]
            if PY_311
            else []
        ),
        (Enum, to_enum_by_name),
        (bool, to_bool),
        (datetime, to_datetime),
        (date, to_date),
        (timedelta, to_timedelta),
        (Path, path_hook),
        (re.Pattern, to_pattern),
    ]
    try:
        import pydantic

        hooks.append((pydantic.SecretBytes, to_pydantic_secretbytes))
        hooks.append((pydantic.SecretStr, to_pydantic_secretstr))
    except ImportError:
        pass
    return hooks


def register_attrs_hook_factory(converter: "cattrs.Converter") -> None:
    """
    Register a hook factory that allows using instances of :program:`attrs` classes
    where :program:`cattrs` would normally expect a dictionary.

    These instances are then returned as-is and without further processing.

    Args:
        converter: The :class:`cattrs.Converter` to register the hook at.
    """

    def allow_attrs_instances(typ):  # type: ignore[no-untyped-def]
        def structure_attrs(val, _):  # type: ignore[no-untyped-def]
            if isinstance(val, typ):
                return val

            # Like structure_attrs_fromdict but using aliases instead of names. This is
            # used instead of the `use_alias` argument as that only works with functions
            # generated using `make_dict_structure_fn`, which is not used here.
            conv_obj = {}  # Start with a fresh dict, to ignore extra keys.
            for a in attrs.fields(typ):
                try:
                    _val = val[a.alias]
                except KeyError:
                    continue

                conv_obj[a.alias] = converter._structure_attribute(a, _val)

            return typ(**conv_obj)

        return structure_attrs

    import attrs

    converter.register_structure_hook_factory(attrs.has, allow_attrs_instances)


def register_dataclasses_hook_factory(converter: "cattrs.Converter") -> None:
    """
    Register a hook factory that allows using instances of :mod:`dataclasses` classes
    where :program:`cattrs` would normally expect a dictionary.

    These instances are then returned as-is and without further processing.

    Args:
        converter: The :class:`cattrs.Converter` to register the hook at.
    """

    def allow_dataclasses_instances(typ):  # type: ignore[no-untyped-def]
        def structure_dataclasses(val, _):  # type: ignore[no-untyped-def]
            if isinstance(val, typ):
                return val
            return converter.structure_attrs_fromdict(val, typ)

        return structure_dataclasses

    converter.register_structure_hook_factory(
        dataclasses.is_dataclass, allow_dataclasses_instances
    )


def register_pydantic_hook_factory(converter: "cattrs.Converter") -> None:
    """
    Register a hook factory that allows using instances of :mod:`dataclasses` classes
    where :program:`cattrs` would normally expect a dictionary.

    These instances are then returned as-is and without further processing.

    Args:
        converter: The :class:`cattrs.Converter` to register the hook at.
    """
    try:
        import pydantic
    except ImportError:  # pragma: no cover
        return

    def check(typ: type) -> bool:
        return issubclass(typ, pydantic.BaseModel)

    def to_pydantic(typ):  # type: ignore[no-untyped-def]
        def structure_dataclasses(val, _):  # type: ignore[no-untyped-def]
            if isinstance(val, typ):
                return val
            return typ(**val)

        return structure_dataclasses

    converter.register_structure_hook_factory(check, to_pydantic)


def register_mappingproxy_hook(converter: "cattrs.Converter") -> None:
    """
    Register a hook factory for converting data to :class:`types.MappingProxyType`
    instances.

    Args:
        converter: The :class:`cattrs.Converter` to register the hook at.
    """

    def check(cls: type) -> bool:
        return (
            cls is MappingProxyType
            or cls is collections.abc.Mapping
            or get_origin(cls) is MappingProxyType
            or get_origin(cls) is collections.abc.Mapping
        )

    def convert(val: Mapping, cls: type[T]) -> T:
        args = get_args(cls)
        t = dict[args[0], args[1]] if args else dict  # type: ignore
        return MappingProxyType(converter.structure(val, t))  # type: ignore

    converter.register_structure_hook_func(check, convert)


def register_strlist_hook(
    converter: "cattrs.Converter",
    sep: Optional[str] = None,
    fn: Optional[Callable[[str], list]] = None,
) -> None:
    """
    Register a hook factory with *converter* that allows structuring lists,
    (frozen) sets and tuples from strings (which may, e.g., come from
    environment variables).

    Args:
        converter: The :class:`cattrs.Converter` to register the hook at.
        sep: A separator used for splitting strings (see :meth:`str.split()`).
            Cannot be used together with *fn*.
        fn: A function that takes a string and returns a list, e.g.,
            :func:`json.loads()`.  Cannot be used together with *sep*.

    Example:
        >>> from typing import List
        >>>
        >>> converter = default_converter()
        >>> register_strlist_hook(converter, sep=":")
        >>> converter.structure("1:2:3", List[int])
        [1, 2, 3]
        >>>
        >>> import json
        >>>
        >>> converter = default_converter()
        >>> register_strlist_hook(converter, fn=json.loads)
        >>> converter.structure("[1,2,3]", List[int])
        [1, 2, 3]

    """
    if (sep is None and fn is None) or (sep is not None and fn is not None):
        raise ValueError('You may either pass "sep" *or* "fn"')
    if sep is not None:
        fn = lambda v: v.split(sep)  # noqa

    from cattrs._compat import is_tuple
    from cattrs.cols import is_frozenset, is_sequence, is_set, list_structure_factory

    collection_types = [
        # Order is important, tuple must be last!
        (is_sequence, list_structure_factory),
        (is_set, lambda _, converter: converter._structure_set),
        (is_frozenset, lambda _, converter: converter._structure_frozenset),
        (is_tuple, lambda _, converter: converter._structure_tuple),
    ]

    for check, structure_func_factory in collection_types:
        hook_factory = _generate_hook_factory(structure_func_factory, fn)
        converter.register_structure_hook_factory(check, hook_factory)


def register_secret_hook(converter: "cattrs.Converter") -> None:
    """
    Register a hook factory for converting data to :class:`typed_settings.types.Secret`
    instances.

    Args:
        converter: The :class:`cattrs.Converter` to register the hook at.
    """

    def check(cls: type) -> bool:
        origin = get_origin(cls)
        return (isinstance(cls, type) and issubclass(cls, Secret)) or (
            origin is not None and issubclass(origin, Secret)
        )

    def convert(val: Union[T, Any], cls: type[TSecret]) -> TSecret:
        origin = get_origin(cls)
        if isinstance(val, cls if origin is None else origin):
            val = val.get_secret_value()  # type: ignore[union-attr]
        args = get_args(cls)
        if args:
            val = converter.structure(val, args[0])
        return cls(val)

    converter.register_structure_hook_func(check, convert)


def _generate_hook_factory(structure_func_factory, fn):  # type: ignore[no-untyped-def]
    def gen_func(typ, converter):  # type: ignore[no-untyped-def]
        base_hook = structure_func_factory(typ, converter)

        def str2collection(val, _, base_hook=base_hook):  # type: ignore[no-untyped-def]
            if isinstance(val, str):
                val = fn(val)
            return base_hook(val, typ)

        return str2collection

    return gen_func


def to_any(value: Any, _cls: type) -> Any:
    """
    Return *value* as-is.
    """
    return value


def to_bool(value: Any, _cls: type = bool) -> bool:
    """
    Convert "boolean" strings (e.g., from env. vars.) to real booleans.

    Values mapping to :code:`True`:

    - :code:`True`
    - :code:`"true"` / :code:`"t"` (case insensitive)
    - :code:`"yes"` / :code:`"y"` (case insensitive)
    - :code:`"on"` (case insensitive)
    - :code:`"1"`
    - :code:`1`

    Values mapping to :code:`False`:

    - :code:`False`
    - :code:`"false"` / :code:`"f"` (case insensitive)
    - :code:`"no"` / :code:`"n"` (case insensitive)
    - :code:`"off"` (case insensitive)
    - :code:`"0"`
    - :code:`0`

    Args:
        value: The value to parse.
        _cls: (ignored)

    Return:
        A :class:`bool` for the input *value*.

    Raise:
        ValueError: If *value* is any other value than stated above.
    """
    if isinstance(value, str):
        value = value.lower()
    truthy = {True, "true", "t", "yes", "y", "on", "1"}
    falsy = {False, "false", "f", "no", "n", "off", "0"}
    try:
        if value in truthy:
            return True
        if value in falsy:
            return False
    except TypeError:
        # Raised when "val" is not hashable (e.g., lists)
        pass
    raise ValueError(f"Cannot convert value to bool: {value}")


def to_date(value: Union[datetime, str], cls: type[date] = date) -> date:
    """
    Convert an ISO formatted string to :class:`datetime.date`.  Leave the input
    untouched if it is already a date.

    See: :meth:`datetime.date.fromisoformat()`

    Args:
        value: The input data
        cls: The target type.  Must be :class:`datetime.date` or a subclass.

    Return:
        The converted date instance

    Raise:
        TypeError: If *value* is neither a string nor a date
        ValueError: If *value* cannot be parsed as date.

    .. versionadded:: 24.3.0
    """
    if not isinstance(value, (date, str)):
        raise TypeError(
            f"Invalid type {type(value).__name__!r}; expected 'date' or 'str'."
        )
    if isinstance(value, str):
        return cls.fromisoformat(value)
    return value


def to_datetime(
    value: Union[datetime, str], cls: type[datetime] = datetime
) -> datetime:
    """
    Convert an ISO formatted string to :class:`datetime.datetime`.  Leave the input
    untouched if it is already a datetime.

    See: :meth:`datetime.datetime.fromisoformat()`

    The ``Z`` suffix is supported on Python versions prior to 3.11, too.

    Args:
        value: The input data
        cls: The target type.  Must be :class:`datetime.datetime` or a subclass.

    Return:
        The converted datetime instance

    Raise:
        TypeError: If *value* is neither a string nor a datetime
        ValueError: If *value* cannot be parsed as datetime.
    """
    if not isinstance(value, (datetime, str)):
        raise TypeError(
            f"Invalid type {type(value).__name__!r}; expected 'datetime' or 'str'."
        )
    if isinstance(value, str):
        if not PY_311 and value[-1] == "Z":
            value = value.replace("Z", "+00:00")
        return cls.fromisoformat(value)
    return value


_SIGN = "(?P<sign>[+-])?"
_DAYS = "(?P<days>[0-9]+)"
_HOURS = "(?P<hours>[0-9]+)"
_MINUTES = "(?P<minutes>[0-9]+)"
_SECONDS = r"(?P<seconds>[0-9]+)(\.(?P<micros>[0-9]{1,6}))?"
# [±][{D}d[,]][[{HH}:]{MM}:]{SS}[.{ffffff}]
RE_TIMEDELTA_SIMPLE = re.compile(
    f"^{_SIGN}({_DAYS}D,?)?(({_HOURS}:)?{_MINUTES}:)?{_SECONDS}$", flags=re.IGNORECASE
)
# [±][{D}d][{HH}h][{MM}m][{SS}[.{ffffff}]s]
RE_TIMEDELTA_SIMPLE_ISO = re.compile(
    f"^{_SIGN}({_DAYS}D)?({_HOURS}H)?({_MINUTES}M)?({_SECONDS}S)?$", flags=re.IGNORECASE
)
# [±]P[{D}D][T[{HH}H][{MM}M][{SS}[.{ffffff}]S]]
RE_TIMEDELTA_ISO = re.compile(
    f"^{_SIGN}"
    r"P(?!\b)"  # "P", but not on a word boundary (e.g., at the end of the string)
    f"({_DAYS}D)?"
    f"("
    r"T(?!\b)"  # "T", but not on a word boundary (e.g., at the end of the string)
    f"({_HOURS}H)?"
    f"({_MINUTES}M)?"
    f"({_SECONDS}S)?"
    r")?$",
    flags=re.IGNORECASE,
)


def to_timedelta(
    value: Union[timedelta, int, float, str], cls: type[timedelta]
) -> timedelta:
    """
    Convert *value* to a :class:`datetime.timedelta`.

    Accepts strings, integers and floats, and timedelta instances.

    Timedelta instances are returned unchanged.

    Integers and floats are interpreted as seconds.

    Supported string formats (all are case-insensitive):

    - :samp:`[±]P[{D}D][T[{HH}H][{MM}M][{SS}[.{ffffff}]S]]` (`ISO durations`_), e.g.:

      - ``P1DT03H04M05S``
      - ``-P180D``
      - ``PT4H30M``
      - ``P1DT30S``

    - :samp:`[±][{D}d][{HH}h][{MM}m][{SS}[.{ffffff}]s]` (simplified ISO variant), e.g.:

      - ``1d3h4m5s``
      - ``-180d``
      - ``4h30m``
      - ``1d30s``

    - :samp:`[±][{D}d[,]][[{HH}:]{MM}:]{SS}[.{ffffff}]`, e.g.:

      - ``1d,03:04:05``
      - ``-180D``
      - ``4:30:00``
      - ``1d30``

    .. _iso durations: https://en.wikipedia.org/wiki/ISO_8601#Durations

    Args:
        value: The input data
        cls: The target type.  Must be :class:`datetime.timedelta` or a subclass.

    Return:
        The converted timedelta instance

    Raise:
        TypeError: If *value* is neither a string, float, or int nor a timedelta.
        ValueError: If *value* cannot be parsed as timedelta.

    .. versionadded:: 24.3.0
    """
    if not isinstance(value, (timedelta, str, float, int)):
        raise TypeError(
            f"Invalid type {type(value).__name__!r}; expected 'timedelta', 'float', "
            f"'int', or 'str'."
        )

    if isinstance(value, timedelta):
        return value

    if isinstance(value, (int, float)):
        return cls(seconds=value)

    for regex in (RE_TIMEDELTA_ISO, RE_TIMEDELTA_SIMPLE_ISO, RE_TIMEDELTA_SIMPLE):
        match = regex.match(value)
        if match:
            break
    else:
        raise ValueError(f"Cannot parse value as timedelta: {value}")

    parts = match.groupdict(default="0")
    days = int(parts["days"])
    hours = int(parts["hours"])
    minutes = int(parts["minutes"])
    seconds = int(parts["seconds"])
    # Append "0" to "micros" to get a 6-digit number (.7 -> 7 -> 700_000)
    micros = int(f"{parts['micros']:<06}")

    td = cls(
        days=days, hours=hours, minutes=minutes, seconds=seconds, microseconds=micros
    )
    if parts["sign"] == "-":
        return -td
    return td


def timedelta_to_str(td: timedelta) -> str:
    """
    Serialize a timedelta to a string that can be parsed by :func:`to_timedelta()`.
    """
    if td == abs(td):
        is_negative = False
    else:
        is_negative = True
        td = -td
    days = td.days
    hours, seconds = divmod(td.seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    micros = f".{td.microseconds:>06}".rstrip("0") if td.microseconds else ""
    result = (
        f"{f'{days}d' if days else ''}"
        f"{f'{hours}h' if hours else ''}"
        f"{f'{minutes}m' if minutes else ''}"
        f"{f'{seconds}{micros}s' if seconds or micros else ''}"
    )
    if result and is_negative:
        result = f"-{result}"
    return result


def to_enum_by_name(value: Any, cls: type[ET]) -> ET:
    """
    Return an instance of the enum *cls* for *value*.

    If the to be converted value is not already an enum, the converter will
    create one by name (``MyEnum[val]``).

    Args:
        value: The input data
        cls: The enum type

    Return:
        An instance of *cls*

    Raise:
        KeyError: If *value* is not a valid member of *cls*
    """
    if isinstance(value, cls):
        return value

    return cls[value]


#: Alias for :func:`to_enum_by_name()`.
to_enum = to_enum_by_name


def to_enum_by_value(value: Any, cls: type[ET]) -> ET:
    """
    Return an instance of the enum *cls* for *value*.

    If the to be converted value is not already an enum, the converter will
    create one by value (``MyEnum(val)``).

    Args:
        value: The input data
        cls: The enum type

    Return:
        An instance of *cls*

    Raise:
        KeyError: If *value* is not a valid member of *cls*
    """
    if isinstance(value, cls):
        return value

    if PY_311 and issubclass(cls, IntEnum):
        value = int(value)
    return cls(value)


def to_path(value: Union[Path, str], cls: type[TPath]) -> TPath:
    """
    Convert *value* to a path type.

    Args:
        value: The input data
        cls: The :class:`~pathlib.Path` type.

    Return:
        An instance of :class:`~pathlib.Path`

    Raise:
        TypeError: If *value* cannot be converted to a path.
    """
    return cls(value)


def to_resolved_path(value: Union[Path, str], cls: type[TPath]) -> TPath:
    """
    Convert *value* to a path type and resolve it.

    Args:
        value: The input data
        cls: The :class:`~pathlib.Path` type.

    Return:
        A resolved instance of :class:`~pathlib.Path`

    Raise:
        TypeError: If *value* cannot be converted to a path.
    """
    return cls(value).resolve()


def to_pattern(value: Union[re.Pattern, str], cls: type[re.Pattern]) -> re.Pattern:
    """
    Compile *value* to :class:`re.Pattern`.

    Args:
        value: The input data.
        cls: The :class:`re.Pattern` type.

    Return:
        The result of :func:`re.compile()`.

    Raise:
        TypeError: If *value* is not a string or already a pattern.
        re.PatternError: If *value* ist not a valid regular expression.
    """
    if isinstance(value, re.Pattern):
        return value
    return re.compile(value)


def to_type(value: Any, cls: type[T]) -> T:
    """
    Convert *value* to *cls*.

    Args:
        value: The input data
        cls: A class that takes a single argument, e.g., :class:`int`, :class:`float`,
            or :class:`str`.

    Return:
        An instance of *cls*.

    Raise:
        ValueError: if *value* cannot be converted to *cls*.
    """
    return cls(value)  # type: ignore[call-arg]


def to_pydantic_secretbytes(
    value: Any, _cls: "type[pydantic.SecretBytes]"
) -> "pydantic.SecretBytes":
    """
    Convert *value* to :class:`pydantic.SecretStr`.

    Args:
        value: The input data
        _cls: (ignored)

    Return:
        An instance of *cls*.
    """
    import pydantic

    if isinstance(value, pydantic.SecretBytes):
        return value

    return pydantic.SecretBytes(value)


def to_pydantic_secretstr(
    value: Any, _cls: "type[pydantic.SecretStr]"
) -> "pydantic.SecretStr":
    """
    Convert *value* to :class:`pydantic.SecretStr`.

    Args:
        value: The input data
        cls: A pydantic SecretStr class or any subclass
        _cls: (ignored)

    Return:
        An instance of *cls*.
    """
    import pydantic

    if isinstance(value, pydantic.SecretStr):
        return value

    return pydantic.SecretStr(value)


class HookFactory(Protocol):
    """
    **Protocol** for :class:`TSConverter` hook factories.

    Hook factories have a :meth:`match` functions that decides whether they can handle
    given type/class.  In addition, they can generate a structure hook for that type.
    """

    @staticmethod
    def match(cls: type, origin: Optional[Any], args: tuple[Any, ...]) -> bool:
        """
        Check whether this class can handle the given type *cls*.

        Args:
            cls: The type/class to check.
            origin: The type's origin as returned by :func:`typing.get_origin()`.
            args: The type's args as retuned by :func:`typing.get_args()`.

        Return:
            ``True`` if this class can convert the given type, or else ``False``.
        """
        ...

    @staticmethod
    def get_structure_hook(
        converter: TSConverter, cls: type, origin: Optional[Any], args: tuple[Any, ...]
    ) -> Callable[[Any, type[T]], T]:
        """
        Return a structure hook for the given type/class.

        Args:
            converter: The :class:`TSConverter` that the returned hook will be
                registered at.  The structure hook can use the converter to recursively
                convert sub elements of composite types.
            cls: The type/class to convert to.
            origin: The type's origin as returned by :func:`typing.get_origin()`.
            args: The type's args as retuned by :func:`typing.get_args()`.

        Return:
            A structure hook, which is a function
            :samp:`hook({value}: Any, {cls}: Type[T]) -> T`.
        """
        ...


class AttrsHookFactory:
    """
    A :class:`HookFactory` that returns :program:`attrs` classes from dicts.  Instances
    are of the given class are accepted as well and returned as-is (without further
    processing of their attributes).
    """

    @staticmethod
    def match(cls: type, origin: Optional[Any], args: tuple[Any, ...]) -> bool:
        try:
            import attrs
        except ImportError:
            return False

        return attrs.has(cls)

    @staticmethod
    def get_structure_hook(
        converter: Converter, cls: type, origin: Optional[Any], args: tuple[Any, ...]
    ) -> Callable[[Union[dict, T], type[T]], T]:
        import attrs

        def convert(value: Union[dict, T], cls: type[T]) -> T:
            if isinstance(value, cls):
                return value

            if not isinstance(value, dict):
                raise TypeError(
                    f'Invalid type "{type(value).__name__}"; expected '
                    f'"{cls.__name__}" or "dict".'
                )

            fields = {field.alias: field for field in attrs.fields(cls)}  # type: ignore[arg-type]
            values = {
                n: converter.structure(v, fields[n].type)  # type: ignore[arg-type]
                for n, v in value.items()
            }
            return cls(**values)

        return convert


class DataclassesHookFactory:
    """
    A :class:`HookFactory` that returns :mod:`dataclasses` from dicts.  Instances
    are of the given class are accepted as well and returned as-is (without further
    processing of their attributes).
    """

    @staticmethod
    def match(cls: type, origin: Optional[Any], args: tuple[Any, ...]) -> bool:
        return dataclasses.is_dataclass(cls)

    @staticmethod
    def get_structure_hook(
        converter: Converter, cls: type, origin: Optional[Any], args: tuple[Any, ...]
    ) -> Callable[[Union[dict, T], type[T]], T]:
        def convert(value: Union[dict, T], cls: type[T]) -> T:
            if isinstance(value, cls):
                return value

            if not isinstance(value, dict):
                raise TypeError(
                    f'Invalid type "{type(value).__name__}"; expected '
                    f'"{cls.__name__}" or "dict".'
                )

            fields = {f.name: f for f in dataclasses.fields(cls)}  # type: ignore[arg-type]
            values = {
                n: converter.structure(v, fields[n].type)  # type: ignore[arg-type]
                for n, v in value.items()
            }
            return cls(**values)

        return convert


class PydanticHookFactory:
    """
    A :class:`HookFactory` that returns :mod:`dataclasses` from dicts.  Instances
    are of the given class are accepted as well and returned as-is (without further
    processing of their attributes).
    """

    @staticmethod
    def match(cls: type, origin: Optional[Any], args: tuple[Any, ...]) -> bool:
        try:
            import pydantic
        except ImportError:
            return False
        return issubclass(cls, pydantic.BaseModel)

    @staticmethod
    def get_structure_hook(
        converter: Converter, cls: type, origin: Optional[Any], args: tuple[Any, ...]
    ) -> Callable[[Union[dict, T], type[T]], T]:
        def convert(value: Union[dict, T], cls: type[T]) -> T:
            if isinstance(value, cls):
                return value

            if not isinstance(value, dict):
                raise TypeError(
                    f'Invalid type "{type(value).__name__}"; expected '
                    f'"{cls.__name__}" or "dict".'
                )

            return cls(**value)

        return convert


class ListHookFactory:
    """
    A :class:`HookFactory` for :class:`list` and :class:`typing.List`.
    """

    @staticmethod
    def match(cls: type, origin: Optional[Any], args: tuple[Any, ...]) -> bool:
        return cls is list or origin is list

    @staticmethod
    def get_structure_hook(
        converter: TSConverter, cls: type, origin: Optional[Any], args: tuple[Any, ...]
    ) -> Callable[[Iterable, type[T]], T]:
        if not args:
            args = (Any,)
        item_type = args[0]

        def convert(value: Iterable, cls: type[T]) -> T:
            value = converter.maybe_apply_strlist_hook(value)
            values = [converter.structure(v, item_type) for v in value]
            return list(values)  # type: ignore[return-value]

        return convert


class TupleHookFactory:
    """
    A :class:`HookFactory` for :class:`tuple` and :class:`typing.Tuple`.
    """

    @staticmethod
    def match(cls: type, origin: Optional[Any], args: tuple[Any, ...]) -> bool:
        return cls is tuple or origin is tuple

    @staticmethod
    def get_structure_hook(
        converter: TSConverter, cls: type, origin: Optional[Any], args: tuple[Any, ...]
    ) -> Union[Callable[[Iterable, type[T]], T], Callable[[Sequence, type[T]], T]]:
        if not args:
            args = (Any, ...)

        convert: Union[
            Callable[[Iterable, type[T]], T],  # For list-like tuples
            Callable[[Sequence, type[T]], T],  # For struct-like tuples
        ]
        if len(args) == 2 and args[1] == ...:
            item_type = args[0]

            def convert(value: Iterable, cls: type[T]) -> T:
                value = converter.maybe_apply_strlist_hook(value)
                values = [converter.structure(v, item_type) for v in value]
                return tuple(values)  # type: ignore[return-value]

        else:

            def convert(value: Sequence, cls: type[T]) -> T:
                value = converter.maybe_apply_strlist_hook(value)
                if len(value) != len(args):
                    raise TypeError(
                        f"Value must have {len(args)} items but has: {len(value)}"
                    )
                values = [converter.structure(v, t) for v, t in zip(value, args)]
                return tuple(values)  # type: ignore[return-value]

        return convert


class DictHookFactory:
    """
    A :class:`HookFactory` for :class:`dict` and :class:`typing.Dict`.
    """

    @staticmethod
    def match(cls: type, origin: Optional[Any], args: tuple[Any, ...]) -> bool:
        return cls is dict or origin is dict

    @staticmethod
    def get_structure_hook(
        converter: TSConverter, cls: type, origin: Optional[Any], args: tuple[Any, ...]
    ) -> Callable[[Mapping, type[T]], T]:
        if not args:
            args = (Any, Any)
        key_type, val_type = args

        def convert(value: Mapping, cls: type[T]) -> T:
            values = {
                converter.structure(k, key_type): converter.structure(v, val_type)
                for k, v in value.items()
            }
            return values  # type: ignore[return-value]

        return convert


class MappingProxyTypeHookFactory:
    """
    A :class:`HookFactory` for :class:`types.MappingProxyType` (a read-only dict proxy).
    """

    @staticmethod
    def match(cls: type, origin: Optional[Any], args: tuple[Any, ...]) -> bool:
        mapping_types = (MappingProxyType, Mapping, collections.abc.Mapping)

        for type_ in (cls, origin):
            for mapping_type in mapping_types:
                if type_ is mapping_type:
                    return True
        return False

    @staticmethod
    def get_structure_hook(
        converter: TSConverter, cls: type, origin: Optional[Any], args: tuple[Any, ...]
    ) -> Callable[[Any, type[T]], T]:
        if not args:
            args = (Any, Any)
        key_type, val_type = args

        def convert(value: Mapping, cls: type[T]) -> T:
            values = {
                converter.structure(k, key_type): converter.structure(v, val_type)
                for k, v in value.items()
            }
            return MappingProxyType(values)  # type: ignore[return-value]

        return convert


class SetHookFactory:
    """
    A :class:`HookFactory` for :class:`set` and :class:`typing.Set`.
    """

    @staticmethod
    def match(cls: type, origin: Optional[Any], args: tuple[Any, ...]) -> bool:
        return cls is set or origin is set

    @staticmethod
    def get_structure_hook(
        converter: TSConverter, cls: type, origin: Optional[Any], args: tuple[Any, ...]
    ) -> Callable[[Any, type[T]], T]:
        if not args:
            args = (Any,)
        item_type = args[0]

        def convert(value: Iterable, cls: type[T]) -> T:
            value = converter.maybe_apply_strlist_hook(value)
            values = [converter.structure(v, item_type) for v in value]
            return set(values)  # type: ignore[return-value]

        return convert


class FrozenSetHookFactory:
    """
    A :class:`HookFactory` for :class:`frozenset` and :class:`typing.FrozenSet`.
    """

    @staticmethod
    def match(cls: type, origin: Optional[Any], args: tuple[Any, ...]) -> bool:
        return cls is frozenset or origin is frozenset

    @staticmethod
    def get_structure_hook(
        converter: TSConverter, cls: type, origin: Optional[Any], args: tuple[Any, ...]
    ) -> Callable[[Any, type[T]], T]:
        if not args:
            args = (Any,)
        item_type = args[0]

        def convert(value: Iterable, cls: type[T]) -> T:
            value = converter.maybe_apply_strlist_hook(value)
            values = [converter.structure(v, item_type) for v in value]
            return frozenset(values)  # type: ignore[return-value]

        return convert


class SecretHookFactory:
    """
    A :class:`HookFactory` for :class:`typed_settings.types.Secret`.

    If the input is already a secret, it will be returned as-is.
    """

    @staticmethod
    def match(cls: type, origin: Optional[Any], args: tuple[Any, ...]) -> bool:
        return (isinstance(cls, type) and issubclass(cls, Secret)) or (
            isinstance(origin, type) and issubclass(origin, Secret)
        )

    @staticmethod
    def get_structure_hook(
        converter: TSConverter, cls: type, origin: Optional[Any], args: tuple[Any, ...]
    ) -> Callable[[Any, type[T]], T]:
        def convert(value: Any, cls: type[T]) -> T:
            if isinstance(value, Secret):
                value = value.get_secret_value()
            if args:
                value = converter.structure(value, args[0])
            return cls(value)  # type: ignore[call-arg]

        return convert


class LiteralHookFactory:
    """
    A :class:`HookFactory` for :data:`typing.Literal`.

    Only accepts valid literals and otherwise raises a :exc:`ValueError`.
    """

    @staticmethod
    def match(cls: type, origin: Optional[Any], args: tuple[Any, ...]) -> bool:
        return origin is Literal

    @staticmethod
    def get_structure_hook(
        converter: TSConverter, cls: type, origin: Optional[Any], args: tuple[Any, ...]
    ) -> Callable[[Any, type[T]], T]:
        def convert(value: Any, cls: type[T]) -> T:
            if value not in args:
                raise ValueError(f"Value is not in literals {args!r}: {value}")
            return value

        return convert


class UnionHookFactory:
    """
    A :class:`HookFactory` for :data:`typing.Optional` and :data:`typing.Union`.

    If the input data already has one of the uniton types, it will be returned without
    further processing.  Otherwise, converters for all union types will be tried until
    one works (i.e., raises no exception).
    """

    @staticmethod
    def match(cls: type, origin: Optional[Any], args: tuple[Any, ...]) -> bool:
        return origin in (Union, UnionType)

    @staticmethod
    def get_structure_hook(
        converter: TSConverter, cls: type, origin: Optional[Any], args: tuple[Any, ...]
    ) -> Callable[[Any, type[T]], T]:
        def convert(value: Any, cls: type[T]) -> T:
            if type(value) in args:
                # Preserve val as-is if it already has a matching type.
                # Otherwise float(3.2) would be converted to int
                # if the converters are [int, float].
                return value
            for arg in args:
                try:
                    return converter.structure(value, arg)
                except Exception:  # noqa: S110
                    pass
            raise ValueError(f"Failed to convert value to any Union type: {value}")

        return convert
