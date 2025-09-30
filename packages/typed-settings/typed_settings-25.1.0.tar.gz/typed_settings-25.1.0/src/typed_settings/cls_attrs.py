"""
Helpers for and additions to :mod:`attrs`.
"""

import sys
from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Optional,
    overload,
)

import attr  # The old namespaces is needed in "combine()"
import attrs

from . import constants, types


if TYPE_CHECKING:
    from attr import (  # type: ignore[attr-defined]
        _T,
        _ConverterType,
        _OnSetAttrArgType,
        _ReprArgType,
        _ValidatorArgType,
    )


__all__ = [
    "SECRET",
    "evolve",
    "option",
    "secret",
    "settings",
]


SECRET = types.SecretRepr()


settings = attrs.define
"""An alias to :func:`attrs.define()`"""


@overload
def option(
    *,
    default: None = ...,
    validator: None = ...,
    repr: "_ReprArgType" = ...,
    hash: Optional[bool] = ...,
    init: bool = ...,
    metadata: Optional[dict[Any, Any]] = ...,
    converter: None = ...,
    factory: None = ...,
    kw_only: bool = ...,
    eq: Optional[bool] = ...,
    order: Optional[bool] = ...,
    on_setattr: Optional["_OnSetAttrArgType"] = ...,
    alias: Optional[str] = ...,
    help: Optional[str] = ...,
    click: Optional[dict[str, Any]] = ...,
    argparse: Optional[dict[str, Any]] = ...,
) -> Any: ...


# This form catches an explicit None or no default and infers the type from the
# other arguments.
@overload
def option(
    *,
    default: None = ...,
    validator: "Optional[_ValidatorArgType[_T]]" = ...,
    repr: "_ReprArgType" = ...,
    hash: Optional[bool] = ...,
    init: bool = ...,
    metadata: Optional[dict[Any, Any]] = ...,
    converter: Optional["_ConverterType"] = ...,
    factory: "Optional[Callable[[], _T]]" = ...,
    kw_only: bool = ...,
    eq: Optional[bool] = ...,
    order: Optional[bool] = ...,
    on_setattr: "Optional[_OnSetAttrArgType]" = ...,
    alias: Optional[str] = ...,
    help: Optional[str] = ...,
    click: Optional[dict[str, Any]] = ...,
    argparse: Optional[dict[str, Any]] = ...,
) -> "_T": ...


# This form catches an explicit default argument.
@overload
def option(
    *,
    default: "_T",
    validator: "Optional[_ValidatorArgType[_T]]" = ...,
    repr: "_ReprArgType" = ...,
    hash: Optional[bool] = ...,
    init: bool = ...,
    metadata: Optional[dict[Any, Any]] = ...,
    converter: "Optional[_ConverterType]" = ...,
    factory: "Optional[Callable[[], _T]]" = ...,
    kw_only: bool = ...,
    eq: Optional[bool] = ...,
    order: Optional[bool] = ...,
    on_setattr: "Optional[_OnSetAttrArgType]" = ...,
    alias: Optional[str] = ...,
    help: Optional[str] = ...,
    click: Optional[dict[str, Any]] = ...,
    argparse: Optional[dict[str, Any]] = ...,
) -> "_T": ...


# This form covers type=non-Type: e.g. forward references (str), Any
@overload
def option(
    *,
    default: Optional["_T"] = ...,
    validator: "Optional[_ValidatorArgType[_T]]" = ...,
    repr: "_ReprArgType" = ...,
    hash: Optional[bool] = ...,
    init: bool = ...,
    metadata: Optional[dict[Any, Any]] = ...,
    converter: "Optional[_ConverterType]" = ...,
    factory: "Optional[Callable[[], _T]]" = ...,
    kw_only: bool = ...,
    eq: Optional[bool] = ...,
    order: Optional[bool] = ...,
    on_setattr: "Optional[_OnSetAttrArgType]" = ...,
    alias: Optional[str] = ...,
    help: Optional[str] = ...,
    click: Optional[dict[str, Any]] = ...,
    argparse: Optional[dict[str, Any]] = ...,
) -> Any: ...


def option(  # type: ignore[no-untyped-def]
    *,
    default=attrs.NOTHING,
    validator=None,
    repr=True,
    hash=None,
    init=True,
    metadata=None,
    converter=None,
    factory=None,
    kw_only=False,
    eq=None,
    order=None,
    on_setattr=None,
    alias=None,
    help=None,
    click=None,
    argparse=None,
):
    """
    An alias to :func:`attrs.field()`.
    """
    metadata = _get_metadata(metadata, help, click, argparse)

    return attrs.field(
        default=default,
        validator=validator,
        repr=repr,
        hash=hash,
        init=init,
        metadata=metadata,
        converter=converter,
        factory=factory,
        kw_only=kw_only,
        eq=eq,
        order=order,
        on_setattr=on_setattr,
        alias=alias,
    )


@overload
def secret(
    *,
    default: None = ...,
    validator: None = ...,
    repr: types.SecretRepr = ...,
    hash: Optional[bool] = ...,
    init: bool = ...,
    metadata: Optional[dict[Any, Any]] = ...,
    converter: None = ...,
    factory: None = ...,
    kw_only: bool = ...,
    eq: Optional[bool] = ...,
    order: Optional[bool] = ...,
    on_setattr: "Optional[_OnSetAttrArgType]" = ...,
    alias: Optional[str] = ...,
    help: Optional[str] = ...,
    click: Optional[dict[str, Any]] = ...,
    argparse: Optional[dict[str, Any]] = ...,
) -> Any: ...


# This form catches an explicit None or no default and infers the type from the
# other arguments.
@overload
def secret(
    *,
    default: None = ...,
    validator: "Optional[_ValidatorArgType[_T]]" = ...,
    repr: types.SecretRepr = ...,
    hash: Optional[bool] = ...,
    init: bool = ...,
    metadata: Optional[dict[Any, Any]] = ...,
    converter: "Optional[_ConverterType]" = ...,
    factory: "Optional[Callable[[], _T]]" = ...,
    kw_only: bool = ...,
    eq: Optional[bool] = ...,
    order: Optional[bool] = ...,
    on_setattr: "Optional[_OnSetAttrArgType]" = ...,
    alias: Optional[str] = ...,
    help: Optional[str] = ...,
    click: Optional[dict[str, Any]] = ...,
    argparse: Optional[dict[str, Any]] = ...,
) -> "_T": ...


# This form catches an explicit default argument.
@overload
def secret(
    *,
    default: "_T",
    validator: "Optional[_ValidatorArgType[_T]]" = ...,
    repr: types.SecretRepr = ...,
    hash: Optional[bool] = ...,
    init: bool = ...,
    metadata: Optional[dict[Any, Any]] = ...,
    converter: "Optional[_ConverterType]" = ...,
    factory: "Optional[Callable[[], _T]]" = ...,
    kw_only: bool = ...,
    eq: Optional[bool] = ...,
    order: Optional[bool] = ...,
    on_setattr: "Optional[_OnSetAttrArgType]" = ...,
    alias: Optional[str] = ...,
    help: Optional[str] = ...,
    click: Optional[dict[str, Any]] = ...,
    argparse: Optional[dict[str, Any]] = ...,
) -> "_T": ...


# This form covers type=non-Type: e.g. forward references (str), Any
@overload
def secret(
    *,
    default: "Optional[_T]" = ...,
    validator: "Optional[_ValidatorArgType[_T]]" = ...,
    repr: types.SecretRepr = ...,
    hash: Optional[bool] = ...,
    init: bool = ...,
    metadata: Optional[dict[Any, Any]] = ...,
    converter: "Optional[_ConverterType]" = ...,
    factory: "Optional[Callable[[], _T]]" = ...,
    kw_only: bool = ...,
    eq: Optional[bool] = ...,
    order: Optional[bool] = ...,
    on_setattr: "Optional[_OnSetAttrArgType]" = ...,
    alias: Optional[str] = ...,
    help: Optional[str] = ...,
    click: Optional[dict[str, Any]] = ...,
    argparse: Optional[dict[str, Any]] = ...,
) -> Any: ...


def secret(  # type: ignore[no-untyped-def]
    *,
    default=attrs.NOTHING,
    validator=None,
    repr=SECRET,
    hash=None,
    init=True,
    metadata=None,
    converter=None,
    factory=None,
    kw_only=False,
    eq=None,
    order=None,
    on_setattr=None,
    alias=None,
    help=None,
    click=None,
    argparse=None,
):
    """
    An alias to :func:`option()` but with a default repr that hides screts.

    When printing a settings instances, secret settings will represented with
    `***` istead of their actual value.

    See Also:
        All arguments are describted here:

        - :func:`option()`
        - :func:`attrs.field()`

    Example:
        >>> from typed_settings import settings, secret
        >>>
        >>> @settings
        ... class Settings:
        ...     password: str = secret()
        ...
        >>> Settings(password="1234")
        Settings(password='*******')

    """
    metadata = _get_metadata(metadata, help, click, argparse)

    return attrs.field(
        default=default,
        validator=validator,
        repr=repr,
        hash=hash,
        init=init,
        metadata=metadata,
        converter=converter,
        factory=factory,
        kw_only=kw_only,
        eq=eq,
        order=order,
        on_setattr=on_setattr,
        alias=alias,
    )


def _get_metadata(
    metadata: Optional[dict[str, Any]],
    help: Optional[str],
    click: Optional[dict[str, Any]],
    argparse: Optional[dict[str, Any]],
) -> dict[str, Any]:
    click_config = {"help": help}
    if click:
        click_config.update(click)
    argparse_config = {"help": help}
    if argparse:
        argparse_config.update(argparse)
    if metadata is None:
        metadata = {}
    ts_meta = metadata.setdefault(constants.METADATA_KEY, {})
    ts_meta["help"] = help
    ts_meta[constants.CLICK_METADATA_KEY] = click_config
    ts_meta[constants.ARGPARSE_METADATA_KEY] = argparse_config
    return metadata


def evolve(inst: attrs.AttrsInstance, **changes: Any) -> attrs.AttrsInstance:
    """
    Create a new instance, based on *inst* with *changes* applied.

    If the old value of an attribute is an ``attrs`` class and the new value
    is a dict, the old value is updated recursively.

    .. warning::

       This function is very similar to :func:`attrs.evolve()`, but the
       ``attrs`` version is not updating values recursively.  Instead, it will
       just replace ``attrs`` instances with a dict.

    Args:
        inst: Instance of a class with ``attrs`` attributes.
        changes: Keyword changes in the new copy.

    Return:
        A copy of *inst* with *changes* incorporated.

    Raise:
        TypeError: If *attr_name* couldn't be found in the class ``__init__``.
        attrs.exceptions.NotAnAttrsClassError: If *cls* is not an ``attrs``
            class.

    ..  versionadded:: 1.0.0
    """
    cls = inst.__class__
    attribs = attrs.fields(cls)  # type: ignore[misc]
    for a in attribs:
        if not a.init:
            continue
        attr_name = a.name  # To deal with private attributes.
        init_name = a.alias
        old_value = getattr(inst, attr_name)
        if init_name not in changes:
            # Add original value to changes
            changes[init_name] = old_value
        elif attrs.has(old_value) and isinstance(changes[init_name], Mapping):
            # Evolve nested attrs classes
            changes[init_name] = evolve(old_value, **changes[init_name])  # type: ignore[arg-type]

    return cls(**changes)


def combine(
    name: str,
    base_cls: type[attrs.AttrsInstance],
    nested: dict[str, attrs.AttrsInstance],
) -> type[attrs.AttrsInstance]:
    """
    Create a new class called *name* based on *base_class* with additional
    attributes for *nested* classes.

    The same effect can be achieved by manually composing settings classes.
    A use case for this method is to combine settings classes from dynamically
    loaded plugins with the base settings of the main program.

    Args:
        name: The name for the new class.
        base_cls: The base class from which to copy all attributes.
        nested: A mapping of attribute names to (settings) class instances
            for which to generated additional attributes.  The attribute's
            type is the instance's type and its default value is the instance
            itself.  Keys in this dict must not overlap with the attributes
            of *base_cls*.

    Return:
        The created class *name*.

    Raise:
        ValueError: If *nested* contains a key for which *base_cls* already
            defines an attribute.

    Example:
        >>> import typed_settings as ts
        >>>
        >>> @ts.settings
        ... class Nested1:
        ...     a: str = ""
        >>>
        >>> @ts.settings
        ... class Nested2:
        ...     a: str = ""
        >>>
        >>> # Static composition
        >>> @ts.settings
        ... class Composed1:
        ...     a: str = ""
        ...     n1: Nested1 = Nested1()
        ...     n2: Nested2 = Nested2()
        ...
        >>> Composed1()
        Composed1(a='', n1=Nested1(a=''), n2=Nested2(a=''))
        >>>
        >>> # Dynamic composition
        >>> @ts.settings
        ... class BaseSettings:
        ...     a: str = ""
        >>>
        >>> Composed2 = ts.combine(
        ...     "Composed2",
        ...     BaseSettings,
        ...     {"n1": Nested1(), "n2": Nested2()},
        ... )
        >>> Composed2()
        Composed2(a='', n1=Nested1(a=''), n2=Nested2(a=''))

    .. versionadded:: 1.1.0
    """
    attribs = {
        a.name: attr.attrib(
            default=a.default,
            validator=a.validator,
            repr=a.repr,
            hash=a.hash,
            init=a.init,
            metadata=a.metadata,
            type=a.type,
            converter=a.converter,
            kw_only=a.kw_only,
            eq=a.eq,
            order=a.order,
            on_setattr=a.on_setattr,
            alias=a.alias,
        )
        for a in attr.fields(base_cls)  # type: ignore[misc]
    }
    annotations = dict(base_cls.__annotations__)
    for aname, default in nested.items():
        if aname in attribs:
            raise ValueError(f"Duplicate attribute for nested class: {aname}")
        attribs[aname] = attr.attrib(default=default, type=default.__class__)
        annotations[aname] = default.__class__

    try:
        globalns = sys.modules[base_cls.__module__].__dict__
    except KeyError:  # pragma: no cover
        globalns = None

    cls = attr.make_class(name, attribs)
    cls.__annotations__ = annotations
    cls.__doc__ = base_cls.__doc__
    # Store globals in class so that they can later be used,
    # see ".cls_utils.Attrs.iter_fields()".
    cls.__globals__ = globalns  # type: ignore[attr-defined]
    return cls
