"""
Core functionality for loading settings.
"""

import logging
import os
from collections.abc import Generator, Iterable, Sequence
from contextlib import contextmanager
from pathlib import Path
from types import MappingProxyType
from typing import (
    Any,
    Generic,
    Optional,
    Union,
)

from . import cls_utils, dict_utils
from .converters import Converter, default_converter
from .exceptions import ConfigFileLoadError, InvalidSettingsError, InvalidValueError
from .loaders import EnvLoader, FileLoader, Loader, TomlFormat, _DefaultsLoader
from .processors import Processor
from .types import (
    AUTO,
    ST,
    LoadedSettings,
    LoaderMeta,
    MergedSettings,
    OptionDict,
    OptionInfo,
    OptionList,
    SettingsDict,
    _Auto,
)


__all__ = [
    "LOGGER",
    "SettingsState",
    "convert",
    "default_loaders",
    "load",
    "load_settings",
]


LOGGER = logging.getLogger("typed-settings")


class SettingsState(Generic[ST]):
    """
    A representation of Typed Settings' internal state and configuration.
    """

    def __init__(
        self,
        settings_cls: type[ST],
        loaders: Sequence[Loader],
        processors: Sequence[Processor],
        converter: Converter,
        base_dir: Path,
    ) -> None:
        self._cls = settings_cls
        self._options = tuple(cls_utils.deep_options(settings_cls))
        self._options_by_name = MappingProxyType({o.path: o for o in self._options})
        self._loaders = loaders
        self._processors = processors
        self._converter = converter
        self._base_dir = base_dir

    @property
    def settings_class(self) -> type[ST]:
        """
        The user's settings class.
        """
        return self._cls

    @property
    def options(self) -> OptionList:
        """
        All options the settings class (and nested sub classes) define.
        """
        return self._options

    @property
    def options_by_path(self) -> OptionDict:
        """
        All options the settings class (and nested sub classes) define, mapped by
        their dotted path (e.g., `nested_cls.option_name`).
        """
        return self._options_by_name

    @property
    def loaders(self) -> list[Loader]:
        """
        A copy of the list of all configured settings loaders.
        """
        return list(self._loaders)

    @property
    def processors(self) -> list[Processor]:
        """
        A copy of the list of all configured post processors.
        """
        return list(self._processors)

    @property
    def converter(self) -> Converter:
        """
        The configured converter.
        """
        return self._converter

    @property
    def cwd(self) -> Path:
        """
        The current working directory.
        """
        return self._base_dir


def default_loaders(
    appname: str,
    config_files: Iterable[Union[str, Path]] = (),
    *,
    config_file_section: Union[None, str, _Auto] = AUTO,
    config_files_var: Union[None, str, _Auto] = AUTO,
    env_prefix: Union[None, str, _Auto] = AUTO,
    env_nested_delimiter: str = "_",
) -> list[Loader]:
    """
    Return a list of default settings loaders that are used by :func:`load()`.

    These loaders are:

    #. A :class:`.FileLoader` loader configured with the :class:`.TomlFormat`
    #. An :class:`.EnvLoader`

    The :class:`.FileLoader` will load files from *config_files* and from the
    environment variable *config_files_var*.

    Args:
        appname: Your application's name -- used to derive defaults for the
          remaining args.

        config_files: Load settings from these files.  The last one has the
          highest precedence.

        config_file_section: Name of your app's section in the config file.
          By default, use *appname* (in lower case and with "_" replaced by
          "-".

        config_files_var: Load list of settings files from this environment
          variable.  By default, use :code:`{APPNAME}_SETTINGS`.  Multiple
          paths have to be separated by ":".  The last file has the highest
          precedence.  All files listed in this var have higher precedence than
          files from *config_files*.

          Set to ``None`` to disable this feature.

        env_prefix: Load settings from environment variables with this prefix.
          By default, use *APPNAME_*.

          Set to ``None`` to disable loading env vars.

        env_nested_delimiter: Delimiter for concatenating attribute names of nested
            classes in env. var. names.

    Return:
        A list of :class:`.Loader` instances.
    """
    loaders: list[Loader] = []

    section = (
        appname.lower().replace("_", "-")
        if isinstance(config_file_section, _Auto)
        else config_file_section
    )
    var_name = (
        f"{appname.upper()}_SETTINGS".replace("-", "_")
        if isinstance(config_files_var, _Auto)
        else config_files_var
    )
    loaders.append(
        FileLoader(
            files=config_files,
            env_var=var_name,
            formats={"*.toml": TomlFormat(section)},
        )
    )

    if env_prefix is None:
        LOGGER.debug("Loading settings from env vars is disabled.")
    else:
        prefix = (
            f"{appname.upper()}_".replace("-", "_")
            if isinstance(env_prefix, _Auto)
            else env_prefix
        )
        loaders.append(EnvLoader(prefix=prefix, nested_delimiter=env_nested_delimiter))

    return loaders


def load(
    cls: type[ST],
    appname: str,
    config_files: Iterable[Union[str, Path]] = (),
    *,
    config_file_section: Union[None, str, _Auto] = AUTO,
    config_files_var: Union[None, str, _Auto] = AUTO,
    env_prefix: Union[None, str, _Auto] = AUTO,
    env_nested_delimiter: str = "_",
    base_dir: Path = Path(),
) -> ST:
    """
    Load settings for *appname* and return an instance of *cls*.

    This function is a shortcut for :func:`load_settings()` with
    :func:`default_loaders()`.

    Settings are loaded from *config_files* and from the files specified
    via the *config_files_var* environment variable.  Settings can also be
    overridden via environment variables named like the corresponding setting
    and prefixed with *env_prefix*.

    Settings precedence (from lowest to highest priority):

    - Default value from *cls*
    - First file from *config_files*
    - ...
    - Last file from *config_files*
    - First file from *config_files_var*
    - ...
    - Last file from *config_files_var*
    - Environment variable :code:`{env_prefix}_{SETTING}`

    Config files (both, explicitly specified, and loaded from an environment
    variable) are optional by default.  You can prepend an ``!`` to their path
    to mark them as mandatory (e.g., `!/etc/credentials.toml`).  An error is
    raised if a mandatory file does not exist.

    Args:
        cls: Attrs class with default settings.

        appname: Your application's name.  Used to derive defaults for the
          remaining args.

        config_files: Load settings from these files.

        config_file_section: Name of your app's section in the config file.
          By default, use *appname* (in lower case and with "_" replaced by
          "-".

        config_files_var: Load list of settings files from this environment
          variable.  By default, use :code:`{APPNAME}_SETTINGS`.  Multiple
          paths have to be separated by ":".  The last file has the highest
          precedence.  All files listed in this var have higher precedence than
          files from *config_files*.

          Set to ``None`` to disable this feature.

        env_prefix: Load settings from environment variables with this prefix.
          By default, use *APPNAME_*.

          Set to ``None`` to disable loading env vars.

        env_nested_delimiter: Delimiter for concatenating attribute names of nested
            classes in env. var. names.

        base_dir: Base directory for resolving relative paths in default option values.

    Return:
        An instance of *cls* populated with settings from settings files and
        environment variables.

    Raise:
        UnknownFormatError: When no :class:`~typed_settings.loaders.FileFormat`
            is configured for a loaded file.
        ConfigFileNotFoundError: If *path* does not exist.
        ConfigFileLoadError: If *path* cannot be read/loaded/decoded.
        InvalidOptionsError: If invalid settings have been found.
        InvalidValueError: If a value cannot be converted to the correct type.
        InvalidSettingsError: With :exc:`.InvalidValueError` exceptions if an instance
            of *cls* cannot be created from the loaded settings.

    .. versionchanged:: 23.1.0
       Added the *base_dir* argument

    .. versionchanged:: 25.0.0
       Raise :exc:`.InvalidSettingsError` is now an :exc:`ExceptionGroup`.
    """
    loaders = default_loaders(
        appname=appname,
        config_files=config_files,
        config_file_section=config_file_section,
        config_files_var=config_files_var,
        env_prefix=env_prefix,
        env_nested_delimiter=env_nested_delimiter,
    )
    converter = default_converter()
    state = SettingsState(cls, loaders, [], converter, base_dir)
    settings = _load_settings(state)
    return convert(settings, state)


def load_settings(
    cls: type[ST],
    loaders: Sequence[Loader],
    *,
    processors: Sequence[Processor] = (),
    converter: Optional[Converter] = None,
    base_dir: Path = Path(),
) -> ST:
    """
    Load settings defined by the class *cls* and return an instance of it.

    Args:
        cls: Attrs class with options (and default values).
        loaders: A list of settings :class:`.Loader`'s.
        processors: A list of settings :class:`.Processor`'s.
        converter: An optional :class:`.Converter` used for converting option values to
            the required type.

            By default, :func:`.default_converter()` is used.
        base_dir: Base directory for resolving relative paths in default option values.

    Return:
        An instance of *cls* populated with settings from the defined loaders.

    Raise:
        TsError: Depending on the configured loaders, any subclass of this
            exception.

    .. versionchanged:: 23.0.0
       Made *converter* a keyword-only argument
    .. versionchanged:: 23.0.0
       Added the *processors* argument
    .. versionchanged:: 23.1.0
       Added the *base_dir* argument
    """
    if converter is None:
        converter = default_converter()
    state = SettingsState(cls, loaders, processors, converter, base_dir=base_dir)
    settings = _load_settings(state)
    return convert(settings, state)


def _load_settings(state: SettingsState) -> MergedSettings:
    """
    Loads settings for *options* and returns them as dict.

    This function makes it easier to extend settings since it returns a dict
    that can easily be updated.
    """
    loaders = [_DefaultsLoader(state.cwd), *state.loaders]
    loaded_settings: list[LoadedSettings] = []
    for loader in loaders:
        result = loader(state.settings_class, state.options)
        if isinstance(result, LoadedSettings):
            loaded_settings.append(result)
        else:
            loaded_settings.extend(result)

    merged_settings = dict_utils.merge_settings(state.options, loaded_settings)

    # Get a "dict view" to merged settings and update the merged_settings afterwards
    # without changing the LoaderMeta for each setting
    settings_dict = dict_utils.flat2nested(merged_settings)
    for processor in state.processors:
        settings_dict = processor(settings_dict, state.settings_class, state.options)
    merged_settings = dict_utils.update_settings(merged_settings, settings_dict)

    return merged_settings


def convert(
    merged_settings: MergedSettings,
    state: SettingsState[ST],
) -> ST:
    """
    Create an instance of *cls* from the settings in *merged_settings*.

    Args:
        merged_settings: The loaded and merged settings by settings name.
        state: The state and configuration for this run.

    Return:
        An instance of *cls*.

    Raise:
        InvalidSettingsError: With :exc:`.InvalidValueError` exceptions if an instance
            of *cls* cannot be created from the loaded settings.

    .. versionchanged:: 25.0.0
       Raise :exc:`.InvalidSettingsError` is now an :exc:`ExceptionGroup`.
    """
    settings_dict: SettingsDict = {}
    errors: list[Exception] = []
    loaded_settings_paths: set[str] = set()
    oi_by_path = state.options_by_path
    for path, (value, meta) in merged_settings.items():
        oinfo = oi_by_path[path]
        try:
            converted_value = convert_value(oinfo, value, meta, state.converter)
        except Exception as e:
            msg = (
                f"Could not convert value {value!r} for option "
                f"{path!r} from loader {meta.name}: {e!r}"
            )
            errors.append(InvalidValueError(msg).with_traceback(e.__traceback__))
            continue
        dict_utils.set_path(settings_dict, path, converted_value)
        loaded_settings_paths.add(path)

    for option_info in state.options:
        if option_info.path in loaded_settings_paths:
            continue
        if option_info.has_default:
            continue
        msg = f"No value set for required option {option_info.path!r}"
        errors.append(InvalidValueError(msg))

    try:
        settings = state.converter.structure(settings_dict, state.settings_class)
    except Exception as e:
        msg = f"Could not convert loaded settings: {e!r}"
        errors.append(InvalidValueError(msg).with_traceback(e.__traceback__))

    if errors:
        msg = (
            f"{len(errors)} errors occured while converting the loaded option values "
            f"to an instance of {state.settings_class.__name__!r}"
        )
        raise InvalidSettingsError(msg, errors)

    return settings


def convert_value(
    oinfo: OptionInfo, value: Any, meta: LoaderMeta, converter: Converter
) -> Any:
    """
    Convert the value for an option to the designated type.

    Args:
        oinfo: Metadata for the option.
        value: The value to be converted.
        meta: Metadata for the loader that loaded *value*.
        converter: The converter to use.

    Return:
        The converted value.

    Raise:
        Exception: If the value cannot be converted.
    """
    if oinfo.cls:
        with _set_context(meta):
            if oinfo.converter:
                converted_value = oinfo.converter(value)
            else:
                converted_value = converter.structure(value, oinfo.cls)
    else:
        converted_value = value
    return converted_value


@contextmanager
def _set_context(meta: LoaderMeta) -> Generator[None, None, None]:
    """
    Set the context for converting option values from a given loader.

    Currently only chagnes the cwd to :attr:`.LoaderMeta.cwd`.

    Args:
        meta: A loaders meta data

    Return:
        A context manager (that yields ``None``)
    """
    old_cwd = os.getcwd()
    try:
        os.chdir(meta.base_dir)
    except OSError as e:
        # This is a rare case where a config file can be read but were we are not
        # allowed to chdir into its parent directory.
        # See: https://gitlab.com/sscherfke/typed-settings/-/issues/71
        raise ConfigFileLoadError(
            f"Cannot chdir into '{meta.base_dir}': {e.strerror}"
        ) from e
    try:
        yield
    finally:
        os.chdir(old_cwd)
