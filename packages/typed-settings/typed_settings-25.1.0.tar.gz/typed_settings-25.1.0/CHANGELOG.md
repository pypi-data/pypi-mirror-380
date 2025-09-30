# Changelog

Typed Settings follows [Calendar Versioning](https://calver.org):

- The **first number** of the version is the year.
- The **second number** is incremented with each release, starting at
  0 for each year.
- The **third number** is for emergencies when we need to start branches
  for older releases.

We try to be as backwards-compatible as possible, so you should not be
afraid to upgrade if you're only using our documented public APIs and
pay attention to `DeprecationWarning`s.

Whenever there's a need to break compatibility, it is announced in this
changelog.  The affected function raises a `DeprecationWarning` for at
least half a year (if possible) before it's finally really broken.

Except for emergencies, only the latest version is supported and will
receive bugfixes.

Support for older Python versions is dropped when they become
[end-of-life](https://devguide.python.org/versions/).

<!-- changelog follows -->

(v25-1-0)=
## [25.1.0](https://gitlab.com/sscherfke/typed-settings/-/compare/25.0.0...25.1.0) (2025-09-30)

- 💥 **BREAKING:** If a field of an `attrs` class or a Pydantic model
  defines an alias, use the alias instead of the original field name
  for loading settings.  Dataclasses don't support alias, so these are
  not affected.  See [!56].

- ✨ Assert support for Python 3.14.

- ✨ Add support for Path subclasses (with argparse)  ([!55]).

- ✨ Fix the support for [Secret][secret_251] and recommend using it instead
  of `SecretStr`.

- ✨ Add converter support for `re.Pattern`/`re.compile()`.

- ✨ Add converter support for `Literal` ([#68]).

  Caveat: When `Literal` is used for CLI generation, all values must be
  strings.

[!55]: https://gitlab.com/sscherfke/typed-settings/-/merge_requests/55
[#68]: https://gitlab.com/sscherfke/typed-settings/-/issues/68
[secret_251]: https://typed-settings.readthedocs.io/en/latest/guides/settings-classes.html#secrets


(v25-0-0)=
## [25.0.0](https://gitlab.com/sscherfke/typed-settings/-/compare/24.6.0...25.0.0) (2025-07-25)

- 💥 **BREAKING:** The `InvalidSettingsError` raised by the `convert()`,
  `load()`, and `load_settings()` functions is now an [ExceptionGroup]
  (but still also a subclass of `TsError`).  For Python versions below
  3.11, the 3rd party backport [exceptiongroup][exceptiongroup-pypi] is being used.
  This allows you to dig deeper if the converter fails for strange
  reasons (as in [#70]) ([#71]).

- ✨ Add support for `typing.Mapping` to converters ([!48]).

- ✨ Add support for `enum.IntEnum` and `enum.StrEnum` ([#59]).

  In contrast to `enum.Enum`, they are converted *by value* and not by
  *name*.

  See the [docs][docs-convert-enum] and [#59] for details and an
  example of how to change the behavior.

- 🐛 Improve handling of nested options in collections (lists and dicts)
  and improve [docs for nested settings][docs-nested-settings] ([#67]).

- 🐛 Improve error message when `os.chdir()` fails while resolving
  relative paths.  This error can occur if a config file is readable
  but its parent directory is not ([#71]).

[!48]: https://gitlab.com/sscherfke/typed-settings/-/merge_requests/48
[#59]: https://gitlab.com/sscherfke/typed-settings/-/issues/59
[#67]: https://gitlab.com/sscherfke/typed-settings/-/issues/67
[#70]: https://gitlab.com/sscherfke/typed-settings/-/issues/70
[#71]: https://gitlab.com/sscherfke/typed-settings/-/issues/71
[ExceptionGroup]: https://docs.python.org/3/library/exceptions.html#exception-groups
[exceptiongroup-pypi]: https://pypi.org/project/exceptiongroup/
[docs-convert-enum]: https://typed-settings.readthedocs.io/en/latest/guides/customize-converters.html
[docs-nested-settings]: https://typed-settings.readthedocs.io/en/latest/guides/settings-classes.html#nested-settings


(v24-6-0)=
## [24.6.0](https://gitlab.com/sscherfke/typed-settings/-/compare/24.5.0...24.6.0) (2024-11-07)

- 💥 **BREAKING:** Dropped support for Python 3.8.  Also switch from
  `Type[...]` to `type[...]` style annotations (for `list`, `tuple`,
  `dict`, ...).

- ✨ Officially support Python 3.13.

- 🐛 Fix regression "dictionary changed size during iteration" ([#60]).

- 🐛 Fix handling of list types with Pydantic models ([#61]).

- 🐛 Fix handling default factories in dataclasses ([#62]).

- 👷 Improve pipeline performance by a factor of ~3.5 through more and
  better usage of **uv** and improved caching.

[#60]: https://gitlab.com/sscherfke/typed-settings/-/issues/60
[#61]: https://gitlab.com/sscherfke/typed-settings/-/issues/61
[#62]: https://gitlab.com/sscherfke/typed-settings/-/issues/62


(v24-5-0)=
## [24.5.0](https://gitlab.com/sscherfke/typed-settings/-/compare/24.4.0...24.5.0) (2024-09-02)

- 🗑️ Support for **Python 3.8** will be dropped by the end of 2024.
  We will continue to provide fixes for critical bugs, though.

- ✨ Add *reload_settings_on_invoke* argument to `click_options()` to
  allow reloading settings on each invocation.  This can improve
  testability of Click CLIs ([#47]).

- 🐛 Fix compatibility with **cattrs** 24.1.  This is also the minium
  required version no ([!40]).

[!40]: https://gitlab.com/sscherfke/typed-settings/-/merge_requests/40
[#47]: https://gitlab.com/sscherfke/typed-settings/-/issues/47


(v24-4-0)=
## [24.4.0](https://gitlab.com/sscherfke/typed-settings/-/compare/24.3.0...24.4.0) (2024-07-02)

- ✨ Add `resolve_types()` function, which is an extended version of
  `attrs.resolve_types()` ([docs][docs-resolve_types], [#56]).

- ✨ Add support for processing of list items, regardless if they are
  strings or nested settings classes. ([#57])

- 📝 Further improve the [docs about postponed annotations / forward
  references][information about forward references] ([#56]).

- 📦 Speed-up CI/CD pipeline and **nox** runs.

- 📦 Use [Trusted Publishers] for uploading to PyPI.

[#56]: https://gitlab.com/sscherfke/typed-settings/-/issues/56
[docs-resolve_types]: https://typed-settings.readthedocs.io/en/latest/apiref.html#typed_settings.cls_utils.resolve_types
[trusted publishers]: https://docs.pypi.org/trusted-publishers/


(v24-3-0)=
## [24.3.0](https://gitlab.com/sscherfke/typed-settings/-/compare/24.2.0...24.3.0) (2024-05-09)

- ✨ Add converters for `date` and `timedelta`, e.g.:

  - date: `2025-05-04` (or `20250504` on Python ≥ 3.11) ([docs][docs-to_date])
  - timedelta (ISO): `P180DT03H04M05S`, `PT0.5S`, `-P180D`, `PT1H30M` ([docs][docs-to_timedelta])
  - timedelta (ISO simpliefied): `180d03h04m05s`, `0.5s`, `-180d`, `1h30m` ([docs][docs-to_timedelta])
  - timedelta (simple): `180d,03:04:05`, `0.5`, `-180d`, `01:30:00` ([docs][docs-to_timedelta])

  See: [#55]

- 🐛 [typed_settings.cls_attrs.combine()][docs-combine] now properly
  populates the `__annotations__` dict of the generated class.  Without
  that, forward references and postponed annotations ([PEP 563])
  wouldn't work properly ([#54]).

- 📝 Add [information about forward references] to the docs ([#54]).

- 📝 Update the [development guide] ([#53]).

[#53]: https://gitlab.com/sscherfke/typed-settings/-/issues/53
[#54]: https://gitlab.com/sscherfke/typed-settings/-/issues/54
[#55]: https://gitlab.com/sscherfke/typed-settings/-/issues/55
[PEP 563]: https://peps.python.org/pep-0563/
[development guide]: https://typed-settings.readthedocs.io/en/latest/development.html
[docs-combine]: https://typed-settings.readthedocs.io/en/latest/apiref.html#typed_settings.cls_attrs.combine
[docs-to_date]: https://typed-settings.readthedocs.io/en/latest/apiref.html#typed_settings.converters.to_date
[docs-to_timedelta]: https://typed-settings.readthedocs.io/en/latest/apiref.html#typed_settings.converters.to_timedelta
[information about forward references]: https://typed-settings.readthedocs.io/en/latest/guides/settings-classes.html#postponed-annotations-forward-references

(v24-2-0)=
## [24.2.0](https://gitlab.com/sscherfke/typed-settings/-/compare/24.1.0...24.2.0) (2024-03-12)

- ✨ Allow passing a custom Jinja Environment to `JinjaProcessor`.
  This lets the library use custom Jinja functions, filters, etc.
  ([!32])

- 🐛 Fix handling of built-in collection types in Pydantic classes
  [#50].

- 🐛 Fix handling of `NewType` types [#52].

[!32]: https://gitlab.com/sscherfke/typed-settings/-/merge_requests/32
[#50]: https://gitlab.com/sscherfke/typed-settings/-/issues/50
[#52]: https://gitlab.com/sscherfke/typed-settings/-/issues/52


(v24-1-0)=
## [24.1.0](https://gitlab.com/sscherfke/typed-settings/-/compare/24.0.0...24.1.0) (2024-02-24)

- ✨ Allow specifying an *env nested delimiter*.  This is the string
  used for concatenating the attribute names of nested classes when
  creating env. var. names.  It defaults to `"_"`.  ([!31])

[!31]: https://gitlab.com/sscherfke/typed-settings/-/merge_requests/31


(v24-0-1)=
## [24.0.1](https://gitlab.com/sscherfke/typed-settings/-/compare/24.0.0...24.0.1) (2024-02-15)

- 🐛 Fix a bug with Pydantic `SecretStr` in Click options [#49].

[#49]: https://gitlab.com/sscherfke/typed-settings/-/issues/49


(v24-0-0)=
## [24.0.0](https://gitlab.com/sscherfke/typed-settings/-/compare/23.1.1...24.0.0) (2024-01-17)

- ✨ For Pydantic classes, read the CLI option's help from the field's
  *desription* if the field's metadata does not contain a `help` key
  [#45].

- ✨ Settings can now be loaded from the top level of a TOML and Python
  file.  This is only exposed by the loaders themselves, but not the
  simple `load()` API, though [#36].

- ✨ Added support for Pydantic `SecretStr` and `SecretBytes` fields in
  settings [#46].

- 🐛 The env var prefix for app names containing a `-` is now derived
  like this: `a-b` => `A_B_` (previously it was `A-B_`) [!27].

[!27]: https://gitlab.com/sscherfke/typed-settings/-/merge_requests/27
[#36]: https://gitlab.com/sscherfke/typed-settings/-/issues/36
[#45]: https://gitlab.com/sscherfke/typed-settings/-/issues/45
[#46]: https://gitlab.com/sscherfke/typed-settings/-/issues/46


(v23-1-1)=
## [23.1.1](https://gitlab.com/sscherfke/typed-settings/-/compare/23.1.0...23.1.1) (2023-11-10)

- 🐛 Don't require `click` when `typed_settings.secret()` is used ([#44])

[#44]: https://gitlab.com/sscherfke/typed-settings/-/issues/44


(v23-1-0)=
## [23.1.0](https://gitlab.com/sscherfke/typed-settings/-/compare/23.0.1...23.1.0) (2023-10-30)

### Changed

- 💥 **BREAKING:** Dropped support for Python 3.7.

- 💥 **BREAKING:** Refactor internal handling of loaded option values.

  This will affect you if you have created a custom loader or processor,
  or if you rely on internal functionality.
  Otherwise, you should be fine.

  Every loader now stores some meta data with the settings it loaded.
  This meta data can, for example, be used to resolve relative paths in
  option values relative to the config file from which they were loaded.

  You can re-enable the old behavior by explicitly using the converter
  returned by `default_converter(resolve_paths=False)`.

  This also improves error messages for when one or more option values
  cannot be converted to the desired type.

  See [#20], [#30], [!16]

- 💥 **BREAKING:** Relative paths are now always resolved relative to
  the source they are loaded from.  This is either the parent directory
  of a config file or the current working directory ([#30]).

- 💥 **BREAKING:** The signature of `argparse_utils`’ `make_parser()`
  and `namespace2settings()` function changed.  They now return and take
  the *merged settings*.  The Signature of `cli()` remains unchanged.
  See [#41].

- 💥 **BREAKING:** The deprecated `typed_settings.attrs.hooks` module
  has been removed.


- 🗑 The modules `typed_settings.argparse_utils`,
  `typed_settings.ckick_utils`, and `typed_settings.attrs` are
  deprecated and are now aliases of the renamed
  `typed_settings.cli_argparse`, `typed_settings.cli_click`, and
  `typed_settings.cls_attrs`.  They will be removed in the next release.

- 🗑 The module `typed_settings.attrs` is deprecated and is now an alias
  for `typed_settings.cls_attrs`.  It will be removed in the next
  release.

- ✨ Added support **dataclasses** and **Pydantic** models as
  alternative to `attrs` (which is still the recommended backend).

- ✨ `attrs` is now an optional (but recommended) dependency.  You can
  install it with `python -m pip install -U typed-settings[attrs]`.

- ✨ Added a built-in `TSConverter` as an alternative for `cattrs`
  (which is still supported and recommended).

- ✨ `cattrs` is now an optional dependency.  You can install it with
  `python -m pip install -U typed-settings[cattrs]`.

- ✨ Typed Settings now has no mandatory dependencies on Python >= 3.11.
  On older versions, `tomli` is the only requirement.  There is also an
  official way to to [vendor] Typed Settings (i.e., to bundle it with
  your application).

- ✨ Added a dictionary loader.  This is useful for testing purposes.

- ✨ Added `start_dir` parameter to `find()`.

- ✨ Officially support Python 3.12.

- 📝 Split guides into smaller pages

- 📝 Converted docs from ReST to Markdown/[MyST] and use [Sybil] to test
  all examples.

- 📦 Switched from [safety] to [pip-audit].

[#20]: https://gitlab.com/sscherfke/typed-settings/-/issues/20
[#30]: https://gitlab.com/sscherfke/typed-settings/-/issues/30
[#41]: https://gitlab.com/sscherfke/typed-settings/-/issues/41
[myst]: https://myst-parser.readthedocs.io/en/latest/
[pip-audit]: https://pypi.org/project/pip-audit
[safety]: https://pypi.org/project/safety
[vendor]: https://gitlab.com/sscherfke/typed-settings-vendoring


(v23-0-1)=
## [23.0.1](https://gitlab.com/sscherfke/typed-settings/-/compare/23.0.0...23.0.1) (2023-05-23)

### Changed

- 🐛 Fixed typing issues with Pylance/Pyright and attrs decorators
  (see [#40])

[#40]: https://gitlab.com/sscherfke/typed-settings/-/issues/40


(v23-0-0)=
## [23.0.0](https://gitlab.com/sscherfke/typed-settings/-/compare/2.0.2...23.0.0) (2023-03-07)

### Deprecated

- 🗑 The next regular release (23.1.0) will drop support for Python 3.7.

- 🗑 The next regular release (23.1.0) will introduce breaking changes
  to the converter API and settings dict.
  See [!16] for details and for feedback.

  Your code will break when:

  - You extend the default converter or pass in your own
  - You have written custom loaders

### Changed

- 📦 Switch to [CalVer] with scheme `YY.MINOR.MICRO` (same as pip, attrs
  and cattrs).

- 📦 Switch to [ruff](https://github.com/charliermarsh/ruff) as linter.

- ♻️ Make `dict_utils` part of the public API.

- ♻️ Make optional imports in `typed_settings` more IDE friendly (see [!14]).

- 📝 Added a copy button to the examples in the docs.
  Prompt characters and out for doctest examples or bash are not
  copied, only the actual code / command.

- 📝 Start migration to Markdown docs with [MyST-Parser].

- 📝 Start using [Sybil] for doctests and examples.

- 📝 Fixed spelling and grammatical mistakes.

### Added

- ✨ Added settings (post) processors.  They allow modifying loaded
  settings before they are passed to your app.  This allows, e.g., using
  settings templates/interpolation or loading secrets from external
  resources via helper scripts. (See [#2], [#19])

- ✨ Added a 1Password loader.

- ✨ Added an `op://` resource handler for the new URL processor (see
  [#19]).

- ✨ Optionally show env var name in the help string for Click options (see [#33]).

[!14]: https://gitlab.com/sscherfke/typed-settings/-/merge_requests/14
[!16]: https://gitlab.com/sscherfke/typed-settings/-/merge_requests/16
[#2]: https://gitlab.com/sscherfke/typed-settings/-/issues/2
[#19]: https://gitlab.com/sscherfke/typed-settings/-/issues/19
[#33]: https://gitlab.com/sscherfke/typed-settings/-/issues/33
[calver]: https://calver.org
[myst-parser]: https://myst-parser.readthedocs.io
[sybil]: https://sybil.readthedocs.io


(v2-0-2)=
## [2.0.2](https://gitlab.com/sscherfke/typed-settings/-/compare/2.0.1...2.0.2) (2023-01-18)

### Fixed

- 🐛 Fixed [#29]: Do not modify attrs metadata when creating CLI
  options. The metadata dict is now copied before popping items from it.

[#29]: https://gitlab.com/sscherfke/typed-settings/-/issues/29


(v2-0-1)=
## [2.0.1](https://gitlab.com/sscherfke/typed-settings/-/compare/2.0.0...2.0.1) (2023-01-14)

### Fixed

- 🐛 Fixed [#26]: Typing error with Pyright/VSCode.
- 📝 Improve documentation for custom Click flags (see [#28]).

[#26]: https://gitlab.com/sscherfke/typed-settings/-/issues/26
[#28]: https://gitlab.com/sscherfke/typed-settings/-/issues/28


(v2-0-0)=
## [2.0.0](https://gitlab.com/sscherfke/typed-settings/-/compare/1.1.1...2.0.0) (2022-11-30)

### Changed

- 💥 **BREAKING:** The `click_utils.TypeHandler` is now called
  `cli_utils.TypeArgsMaker` and has a completely different interface.
  If you do not explicitly use this class, nothing will change for you.
- 💥 **BREAKING:** Remove bundled attrs validators.  They are now in
  `attrs.validators` (see [#17]).

### Added

- ✨ Click options: Support optional types (See [#22]).
- ✨ Click options: Support dicts (e.g., `--env VAR1=val1 --env
  VAR=val2`).
- ✨ Add support for Argparse based CLIs via `typed_settings.cli()` (See
  [#14]).
- ✨ Added wrappers for secrets (`SecretStr` and `Secret`) that mask their
  values when they are printed/logged.
- ✨ Added mypy plugin for our attrs extensions.
- 📝 The guides for core functionality now contain a section about
  writing settings classes and handling secrets.

[#14]: https://gitlab.com/sscherfke/typed-settings/-/issues/14
[#17]: https://gitlab.com/sscherfke/typed-settings/-/issues/17
[#22]: https://gitlab.com/sscherfke/typed-settings/-/issues/22


(v1-1-1)=
## [1.1.1](https://gitlab.com/sscherfke/typed-settings/-/compare/1.1.0...1.1.1) (2022-10-08)

### Added

- ✨ Added support for [cattrs 22.2] which renamed the main converter
  classes. The older version 22.1 remains supported, too.

[cattrs 22.2]: https://cattrs.readthedocs.io/en/latest/history.html#id1


(v1-1-0)=
## [1.1.0](https://gitlab.com/sscherfke/typed-settings/-/compare/1.0.1...1.1.0) (2022-07-09)

This release mainly focuses on improving the integration with [Click],
especially if you want to use command groups or write extensible
applications like [Pytest].

### Changed

- 💥 **BREAKING:** Settings values that are dictionaries are no longer
  merged when they are provided by different settings sources. They
  override each other now as other scalar and container types do.

- ♻️ Replace `toml` with `tomli` for Python \<= 3.10.

- ♻️ Use `tomllib` on Python 3.11 and do not depend on `tomli`.

- ♻️ Require cattrs >= 22.1.0.

- ✅ Increase test coverage to 100% (and enforce it).

- 📝 Impove and extend the docs' examples section.

- 📝 Extend the guides and split them into multiple pages.

### Added

- ✨ Support Python 3.11

- ✨ Improve Click option generation:

  - Add support for `dict` options to `click_options()` (e.g., `--env
    PWD_FILE=/pwd --env DEBUG=1`) (See [#5]).
  - Allow overriding param decls and parameters for Click options (See
    [#15]).
  - You can configure the argument name of your settings in the CLI
    function. This allows you to use different settings in nested click
    commands (See [#15]).
  - Add support for Click option groups (See [!6]).
  - Add `combine()` function to merge multiple settings (e.g., from
    plug-ins) with a base class.

[!6]: https://gitlab.com/sscherfke/typed-settings/-/merge_requests/6
[#5]: https://gitlab.com/sscherfke/typed-settings/-/issues/5
[#15]: https://gitlab.com/sscherfke/typed-settings/-/issues/15
[Click]: https://click.palletsprojects.com
[Pytest]: https://pytest.org


(v1-0-1)=
## [1.0.1](https://gitlab.com/sscherfke/typed-settings/-/compare/1.0.0...1.0.1) (2022-04-04)

### Deprecated

- 🗑 Deprecate the bundled `attrs` validators.  They are now part of
  `attrs.validators`.

### Changed

- ✅ Adjust tests for Click 8.1

### Fixed

- 🐛 Fixed [#16]: Support new (c)attrs namespaces.  `attrs` 21.3 and
  `cattrs` 1.10 are now required.

- 🐛 Bug fix

[#16]: https://gitlab.com/sscherfke/typed-settings/-/issues/16


(v1-0-0)=
## [1.0.0](https://gitlab.com/sscherfke/typed-settings/-/compare/0.11.1...1.0.0) (2022-03-04)

- 🎉 First stable release!

### Changed

- 💥 **BREAKING:** Change `Loader` and `FileFormat` protocols to use
  `__call__()`. This allows "normal" functions to be used as loaders,
  too.

- 💥 **BREAKING:** Pass the settings class to loaders (in addition to
  the list of `OptionInfo`s).

- 💥 **BREAKING:** Enums are only converted from member name, not by
  value.

- ♻️ The `attrs` auto-convert hook now uses a Cattrs converter instead of
  custom conversion logic.

- ✅ Increase test coverage to 100% again.

- ✅ Migrate to pytest7.

- 📝 Write "Guides" section of the docs.

- 📝 Update "Getting Started" section of the docs.

- 📝 Update "Why" section of the docs.

- 📝 Try MyST (Markdown) but switch back to ReST (only for now, MyST
  looks very promising).

### Added

- ✨ Add `evolve()` function for recursively updading settings.

- ✨ Add `InstanceLoader` which loads settings from an existing instance
  of the settings class.

- ✨ `click_options()` accepts just an appname and then works similar to
  `load()`. The old behavior (which is comparable to `load_settings()`
  still exists.

- ✨ The `strlisthook` with `:` as separator is now activated by
  default. It helps loading lists from environment variables.

### Fixed

- 🐛 Fixed [#10]: Fix handling tuples and sets in `strlist` hook.

- 🐛 Fixed [#11]: Properly convert loaded values to click default
  values.

[#10]: https://gitlab.com/sscherfke/typed-settings/-/issues/10
[#11]: https://gitlab.com/sscherfke/typed-settings/-/issues/11


(v0-11-1)=
## [0.11.1](https://gitlab.com/sscherfke/typed-settings/-/compare/0.11.0...0.11.1) (2021-10-03)

### Fixed

- 🐛 Allow using instances of nested attrs/settings classes as default
  values for options again. Fixes a regression introduced by switching
  to cattrs.


(v0-11-0)=
## [0.11.0](https://gitlab.com/sscherfke/typed-settings/-/compare/0.10.0...0.11.0) (2021-10-02)

### Deprecated

- 🗑 The attrs specific converters and hooks are deprecated and will be
  removed in a future release.

### Changed

- 💥 **BREAKING:** Use [cattrs] instead of [attrs auto-convert hooks].
  This makes converters more robust and easier to extend.

- 💥 **BREAKING:** The signature of `load_settings()` has changed.
  `load()` is now the pre-configured convenience loader while
  `load_settings()` allows full customization of all settings loaders
  and value converters.

### Added

- ✨ Loaders can now be extended by users.  Typed settings bundles
  a file loader and an environment loader. New loaders must implement
  the [Loader] protocol.

- ✨ The file loader can be extended to support additional file formats.
  File loaders must implement the [FileFormat] protocol.

- ✨ Add experimental support for Python config files.

- ✨ Environment variables can now contain list values.  Theses lists
  can eitehr be JSON or simple *\{separator}* spearted lists (the
  separator can be configured, e.g., `:` or `,`).

[FileFormat]: https://typed-settings.readthedocs.io/en/latest/apiref.html#typed_settings.loaders.FileFormat
[Loader]: https://typed-settings.readthedocs.io/en/latest/apiref.html#typed_settings.loaders.Loader
[attrs auto-convert hooks]: https://www.attrs.org/en/stable/extending.html#automatic-field-transformation-and-modification
[cattrs]: https://cattrs.readthedocs.io/en/latest/index.html

(v0-10-0)=
## [0.10.0](https://gitlab.com/sscherfke/typed-settings/-/compare/0.9.2...0.10.0) (2021-06-23)

### Deprecated

- 🗑 The signature of `load_settings()` will change in a backwars
  incompatible way in the next release.

### Changed

- 💥 **BREAKING:** Settings classes are now mutable by default. This
  makes especially testing and monkeypatching a lot easier. Since
  settings classes are normal **attrs** classes, you can make your
  settings immutable again by passing `frozen=True` to the class
  decorator.

- 🐍 Add support for **Python 3.10**.

- 🏗  Add support for **click 8**.

### Added

- ✨ `load()` is now the new main function for loading settings. It has
  the same signature as `load_settings()` (See: [#8]).

- ✨ `find()` searches for a given config file from the current working
  dir upwards.

- ✨ The `to_bool()` converter converts bools from addional values.
  Please use `load()`  instead (See: [#8]).

[#8]: https://gitlab.com/sscherfke/typed-settings/-/issues/8


(v0-9-2)=
## [0.9.2](https://gitlab.com/sscherfke/typed-settings/-/compare/0.9.1...0.9.2) (2021-02-10)

### Fixed

- 🐛 Fixed [#3]: Only replace `-` with `_` for sections and option
  names, but not for dict keys.

- 🐛 Remove debug printa.

[#3]: https://gitlab.com/sscherfke/typed-settings/-/issues/3


(v0-9-1)=
## [0.9.1](https://gitlab.com/sscherfke/typed-settings/-/compare/0.9...0.9.1) (2020-12-01)

### Fixed

- 🐛 Fixed [#6]: Properly handle attrs default factories in options.

[#6]: https://gitlab.com/sscherfke/typed-settings/-/issues/6


(v0-9)=
## [0.9](https://gitlab.com/sscherfke/typed-settings/-/compare/0.8...0.9) (2020-11-29)

### Changed

- 💥 **BREAKING:** A `ValueError` is now raised when a config file
  contains invalid options.

- 💥 **BREAKING:** Click options without a default (or loaded value) are
  now marked as `required=True`.

- 📝 Improve *Why Typed Settings* docs.

- 📝 Improve docs for attrs converters/validators/hooks.

- ✅ Increase test coverage to 100%.

### Added

- ✨ Click options support more types (datetimes, lists, tuples, ...)

  - List like types use `multiple=True`
  - Tuple uses `nargs=X`

  Click types can also be exteded by users now.

- ✨ Options can specify a help string for Click options via the
  `click_help` parameter.

- ✨ Improve handling of container types (like `set`) in the attrs
  auto-converter.

### Fixed

- 🐛 Click help strings no longer show values of secret options.


(v0-8)=
## [0.8](https://gitlab.com/sscherfke/typed-settings/-/compare/0.7...0.8) (2020-11-05)

### Added

- ✨ Depend on attrs 20.3 and implement auto-converters for attribute
  values.

- ✨ Properly convert env. vars. with "bool strings" to real booleans.

- 📝 Use [Furo] as documentation theme

- 📝 Update docs:

  - Improve landing page
  - Add Getting Started section to docs
  - Add examples to example guide
  - Add doctests and test examples

[Furo]: https://github.com/pradyunsg/furo

### Fixed

- 🐛 Replace "-" in env. var. names with "\_"


(v0-7)=
## [0.7](https://gitlab.com/sscherfke/typed-settings/-/compare/0.6...0.7) (2020-10-13)

### Added

- 📝 Added API reference to docs.

### Fixed

- 🐛 Fixed loaded settings not being used as option defaults with click.


(v0-6)=
## [0.6](https://gitlab.com/sscherfke/typed-settings/-/compare/0.5...0.6) (2020-10-11)

### Added

- ✨ Add `pass_settings` decorator that pass settings to nested Click
  commands.
- 📝 Initialize documentaion at <https://typed-settings.readthedocs.io>
- 📝 Improve README and automatically test examples


(v0-5)=
## [0.5](https://gitlab.com/sscherfke/typed-settings/-/compare/0.4...0.5) (2020-09-30)

### Added

- ✨ Click options for basic data types (`bool`, `int`, `str`, `Enum`)
  can be generated now.

### Fixed

- 🐛 Fix bug that prevented nested settings classes from automatically
  being instantiated when no settings for them were loaded.


(v0-4)=
## [0.4](https://gitlab.com/sscherfke/typed-settings/-/compare/0.3...0.4) (2020-09-25)

### Changed

- 💥 **BREAKING:** Flip *appname* and *settings_cls* args of
  `load_settings()`.

- ♻️ Refactor internals to improve extensibility.

### Added

- ✨ Added convenience wrappers for attrs:

  - `settings` is an alias for `attr.frozen`
  - `option` is an alias for `attr.field`
  - `secret` is an alias for `attr.field` and masks the options's value
    with `***` when the settings classes is printed.

- ✨ Added `update_settings()` method which is useful for overriding
  settings in tests.

- ✨ Mandatory config files can be prefixed with `!`
  (e.g., `!./credentials.toml`). An error is raised if a mandatory
  config file does not exist.

- 👷 Add pre-commit hooks


(v0-3)=
## [0.3](https://gitlab.com/sscherfke/typed-settings/-/compare/0.2...0.3) (2020-09-17)

### Changed

- 📦 Improved packaging
- ♻️ Refactorings

### Added

- 👷 Added code linting and improve CI


(v0-2)=
## [0.2](https://gitlab.com/sscherfke/typed-settings/-/compare/0.1...0.2) (2020-09-02)

### Changed

- ✨ Make sure env vars can be read

### Added

- ✅ Added tests for `load_settings()`


(v0-1)=
## [0.1](https://gitlab.com/sscherfke/typed-settings/-/tree/0.1) (2020-08-28)

- 🎉 Initial PoC


(legend)=
## Legend

```{hlist}
---
columns: 2
---
- 💥 Breaking change
- ✨ New feature
- 🗑 Deprecation
- 🐛 Bug fix
- ✅ Tests added or improved
- 📝 Docs added or improved
- ♻️ Refactorings
- 📦 Packaging
- 👷 CI/CD
- 🎉 Something to celebrate
```
