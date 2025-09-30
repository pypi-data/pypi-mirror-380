```{currentmodule} typed_settings
```

# Settings Classes

On this page, you'll learn everything about writing settings classes.

## Writing Settings Classes

Settings classes are normal [attrs], [dataclasses], or [Pydantic] classes with type hints:

[attrs]: https://www.attrs.org/en/stable/
[dataclasses]: https://docs.python.org/3/library/dataclasses.html
[pydantic]: https://pydantic-docs.helpmanual.io/

```python
>>> import attrs
>>> import dataclasses
>>> import pydantic
>>>
>>> @attrs.define
... class Settings1:
...     username: str
...     password: str
...
>>> # or
>>> @dataclasses.dataclass
... class Settings2:
...     username: str
...     password: str
...
>>> # or
>>> class Settings3(pydantic.BaseModel):
...     username: str
...     password: str
```

Typed Settings also provides some convenience aliases for `attrs` classes:

```python
>>> import typed_settings as ts
>>>
>>> @ts.settings
... class Settings:
...      username: str = ts.option(help="The username")
...      password: str = ts.secret(help="The password")
```

{func}`settings()` is just an alias for {func}`attrs.define`.
{func}`option()` and {func}`secret()` are wrappers for {func}`attrs.field()`.
They make it easier to add extra metadata for {doc}`CLI options <clis-argparse-or-click>`.
{func}`secret()` also adds basic protection against {ref}`leaking secrets <secrets>`.

```{hint}
Using {func}`settings()` may keep your code a bit cleaner,
but using {func}`attrs.define()` causes fewer problems with type checkers (see {ref}`sec-mypy`).

You *should* use {func}`attrs.define` (or even {func}`attrs.frozen`) if possible.

However, for the sake of brevity we will use {func}`settings()` in many examples.
```

## Nested Settings

Settings classes can be nested.
This allows you, for example, to create different settings classes for different components of your application and
combine them under a "main settings class":

```python
>>> import typed_settings as ts
>>>
>>> @ts.settings
... class ApiSettings:
...     root_path: str = "/"
...
>>> @ts.settings
... class TimeoutSettings:
...     db_read: int = 30
...     db_write: int = 60
...
>>> @ts.settings
... class Settings:
...     api_settings: ApiSettings = ApiSettings()
...     timeout_settings: TimeoutSettings = TimeoutSettings()
```

Nested classes also work inside collections:

```python
>>> import typed_settings as ts
>>>
>>> @ts.settings
... class ServerSettings:
...     host: str
...     port: int
...
>>> @ts.settings
... class Settings:
...     hosts: tuple[ServerSettings, ...] = ()
...     hosts_by_name: dict[str, ServerSettings] = {}
```

```{important}
Dictionary keys for nested settings must always be `str`.
```

Properties of nested classes:

- `-` and `_` in attributes names will be normalized to `_` when settings are loaded.
  That means that you can, e.g., either use `db-read` or `db_read` inside a TOML file.
- This normalization does *not* apply to keys of dictionaries.
  `hosts-by_name = { "host-a" = { ... }, "host_b" = { ... } }` will be normalized to `hosts_by_name = {"host-a": {...}, "host_b": {...}}`
  (`hosts_by_name` is being normalized but the host keys are not).
- Nested classes must be of the same kind, e.g., a nested attrs class within an attrs class.
  A dataclass inside an attrs class will not be recognised as nested settings.
- CLI options (see :doc:`guides/clis-argparse-or-click`) for a nested class will have the same prefix,
  namely, the attribute name in the parent class.
- CLI options are only generated for plain nested classes but not for nested classes inside a collection.

:::{admonition} Example for nested settings
:class: hint

In the following example,
`a-1`, `a-2`, and `b-1` will always be mapped to `a_1`, `a_2`, and `b_1`, respectively.
However, `k-1` is not normalized because it is a normal dictionary key.

```{code-block} python
:caption: settings.py

import rich
import typed_settings as ts


@ts.settings
class Sub:
    b_1: str = ""


@ts.settings
class Parent:
    a_1: str = ""
    a_2: str = ""
    sub_section: Sub = Sub()
    sub_list: list[Sub] = ts.option(factory=list)
    sub_dict: dict[str, Sub] = ts.option(factory=dict)


settings = ts.load(Parent, appname="myapp")
rich.print(settings)
```

```{code-block} toml
:caption: settings.toml

[myapp]
a-1 = "spam"
a_2 = "eggs"

[myapp.sub-section]
b-1 = "bacon"

[[myapp.sub-list]]
b-1 = "bacon"

[myapp.sub-dict.k-1]
b-1 = "bacon"
```

```{code-block} console
$ export MYAPP_SETTINGS="settings.toml"
$ python settings.py
Parent(
    a_1='spam',
    a_2='eggs',
    sub_section=Sub(b_1='bacon'),
    sub_list=[Sub(b_1='bacon')],
    sub_dict={'k-1': Sub(b_1='bacon')}
)
```
:::

(secrets)=

## Secrets

Secrets, even when stored in an encrypted vault, most of the time end up as plain strings in your app.
And plain strings tend to get printed.
This can be log messages, debug {func}`print()`s, tracebacks, you name it:

```python
>>> import typed_settings as ts
>>>
>>> @ts.settings
... class Settings:
...      username: str
...      password: str
...
>>> settings = Settings("spam", "eggs")
>>> print(f"Settings loaded: {settings}")
Settings loaded: Settings(username='spam', password='eggs')
```

Oops!

```{danger}
Never use environment variables to pass secrets to your application!

It's far easier for environment variables to leak outside than for config files.
You may, for example, accidentally leak your env via your CI/CD pipeline,
or you may be affected by a [security incident] for which you can't do anything.

The most secure thing is to use an encrypted vault to store your secrets.
If that is not possible, store them in a config file.

If you *have* to use environment variables, write the secret to a file and use the env var to point to that file,
e.g., {code}`MYAPP_API_TOKEN_FILE=/private/token` (instead of just {code}`MYAPP_API_TOKEN="3KX93ad..."`).
[GitLab CI/CD] supports this, for example.

[security incident]: https://thehackernews.com/2021/09/travis-ci-flaw-exposes-secrets-of.html
[gitlab ci/cd]: https://docs.gitlab.com/ee/ci/variables/#cicd-variable-types
```
```{seealso}
The article [Keeping Secrets Out of Logs](https://allan.reyes.sh/posts/keeping-secrets-out-of-logs/#run-time-part-deux) provides a good overview of how your code can leak secrets and
what you can do to prevent this.
```

The generic class {class}`~typed_settings.types.Secret` makes accidental secrets leakage nearly impossible,
because you have to call its {meth}`~typed_settings.types.Secret.get_secret_value()` method to retrieve the actual secret value.
Because of that, it is not a drop-in replacement for strings:

```python
>>> import typed_settings as ts
>>> from typed_settings.types import Secret
>>>
>>> @ts.settings
... class Settings:
...      username: str
...      password: Secret
...
>>> settings = Settings("spam", Secret("eggs"))
>>> print(f"Settings loaded: {settings}")
Settings loaded: Settings(username='spam', password=Secret('*******'))
>>> print(settings.password)
*******
>>> print(f"Le secret: {settings.password}")
Le secret: *******
>>> settings.password.get_secret_value()
'eggs'
```

If you need a drop-in replacement for strings,
you can use {class}`~typed_settings.types.SecretStr`:

```python
>>> import typed_settings as ts
>>> from typed_settings.types import SecretStr
>>>
>>> @ts.settings
... class Settings:
...      username: str
...      password: SecretStr = ts.secret()
...
>>> settings = Settings("spam", SecretStr("eggs"))
>>> print(f"Settings loaded: {settings}")
Settings loaded: Settings(username='spam', password='*******')
>>> print(f"{settings.username=}, {settings.password=}")
settings.username='spam', settings.password='*******'
```

Note that this only works for strings and that
it is not as safe as {class}`~typed_settings.types.Secret`:

```python
>>> print(settings.password)
eggs
>>> print(f"Le secret: {settings.password}")
Le secret: eggs
```

If you can't even use {class}`~typed_settings.types.SecretStr`,
you can still use {func}`secret()` which at leasts masks the secret in the setings class' `repr`:

```python
>>> import typed_settings as ts
>>>
>>> @ts.settings
... class Settings:
...      username: str
...      password: str = ts.secret()
...
>>> settings = Settings("spam", "eggs")
>>> print(f"Settings loaded: {settings}")
Settings loaded: Settings(username='spam', password='*******')
```

However, the secret would leak if you printed the field directly:

```python
>>> print(f"{settings.username=}, {settings.password=}")
settings.username='spam', settings.password='eggs'
```

```{important}
If possible, use {class}`~typed_settings.types.Secret()`,
because it is the most secure variant with regards to leaking secrets.

Only if this is not possible,
fall back to {class}`~typed_settings.types.SecretStr()` and {func}`~typed_settings.secret()`.

But no matter what you use,
you should explicitly test the (log) output of your code to make sure,
secrets are not contained at all or are masked at least.
```

## Field Aliases

attrs and Pydantic allow fields (attributes) to define an alias.
If an alias is defined for a field, Typed Settings will use this for loading settings:

```{code-block} python
:caption: settings.py
:emphasize-lines: 7

import typed_settings as ts


@ts.settings
class Settings:
    public: str = ""
    _private: str = ts.option(default="", alias="myalias")


settings = ts.load(Settings, appname="myapp")
print(settings)
```

```{code-block} toml
:caption: settings.toml
:emphasize-lines: 3

[myapp]
public = "spam"
myalias = "eggs"
```

```{code-block} console
$ export MYAPP_SETTINGS="settings.toml"
$ python settings.py
Settings(public='spam', _private='eggs')
```

## Dynamic Options

The benefit of class based settings is that you can use properties to create "dynamic" or "aggregated" settings.

Imagine, you want to configure the URL for a REST API but the only part that usually changes with every deployment is the hostname.

For these cases, you can make each part of the URL configurable and create a property that returns the full URL:

```python
>>> from pathlib import Path
>>> import typed_settings as ts
>>>
>>> @ts.settings
... class ServiceConfig:
...     scheme: str = "https"
...     host: str = "example.com"
...     port: int = 443
...     path: Path() = Path("api")
...
...     @property
...     def url(self) -> str:
...         return f"{self.scheme}://{self.host}:{self.port}/{self.path}"
...
>>> print(ServiceConfig().url)
https://example.com:443/api
```

Another use case is loading data from files, e.g., secrets like SSH keys:

```python
>>> from functools import cache
>>> from pathlib import Path
>>> import typed_settings as ts
>>>
>>> @ts.settings(frozen=True)
... class SSH:
...     key_file: Path
...
...     @property
...     @cache
...     def key(self) -> str:
...         return self.key_file.read_text()
...
>>> key_file = tmp_path.joinpath("id_1337")
>>> key_file.write_text("le key")
6
>>> print(SSH(key_file=key_file).key)
le key
```

(sec-mypy)=

## Mypy

Unfortunately, [mypy] still gets confused when you alias {func}`attrs.define` (or even import it from any module other than {mod}`attr` or {mod}`attrs`).

Accessing your settings class' attributes does work without any problems,
but when you manually instantiate your class, mypy will issue a `call-arg` error.

The [suggested workaround] is to create a simple mypy plugin,
so Typed Settings ships with a simple mypy plugin in {mod}`typed_settings.mypy`.

You can activate the plugin via your {file}`pyproject.toml` or {file}`mypy.ini`:

[mypy]: http://mypy-lang.org/
[suggested workaround]: https://www.attrs.org/en/stable/extending.html?highlight=mypy#wrapping-the-decorator

```{code-block} toml
:caption: pyproject.toml

 [tool.mypy]
 plugins = ["typed_settings.mypy"]
```

```{code-block} ini
:caption: mypy.ini

 [mypy]
 plugins=typed_settings.mypy
```


## Postponed Annotations / Forward References

```{hint}
Type annotations that are encoded as string literals (e.g. `x: "int"`) are called [forward references].

Forward references can be resolved to actual types at runtime using functions like {func}`typing.get_type_hints()` or {func}`attrs.resolve_types()`.

[forward references]: https://peps.python.org/pep-0484/#forward-references
```

Typed Settings tries to resolve forward references when loading settings or
when combining settings from attrs classes to new classes.

This may not always work reliably, for example

- if classes are defined inside nested scopes (i.e., inside functions or other classes):

  ```python
  >>> import attrs
  >>>
  >>> def get_cls():
  ...     @attrs.frozen
  ...     class Nested:
  ...         x: "int"
  ...
  ...     @attrs.frozen
  ...     class Settings:
  ...         opt: "Nested"
  ...
  ...     return Settings
  >>>
  >>> attrs.resolve_types(get_cls())
  Traceback (most recent call last):
    ...
  NameError: name 'Nested' is not defined
  ```

- if classes reference other classes in a collection:

  ```python
  >>> import attrs
  >>>
  >>> @attrs.frozen
  ... class Nested:
  ...     x: "int"
  ...
  >>> @attrs.frozen
  ... class Settings:
  ...     opt: "list[Nested]"
  ...
  >>>
  >>> # This works
  >>> # ("globalns" and "localns" are only required for this doctest example):
  >>> Settings = attrs.resolve_types(Settings, globalns=globals(), localns=locals())
  >>> attrs.fields(Settings).opt.type
  list[__test__.Nested]
  >>> # But "resolve_types" is not recursive, so "Nested" is still unresolved:
  >>> attrs.fields(Nested).x.type
  'int'
  ```

In these cases, you can decorate your classes with {func}`typed_settings.resolve_types()`,
which is an improved version of {func}`attrs.resolve_types()`.
You can pass globals and locals when using it as a class decorator and
it also supports dataclasses:

```python
>>> import attrs
>>> import typed_settings as ts
>>>
>>> def get_cls():
...
...     @ts.resolve_types
...     @attrs.frozen
...     class Nested:
...         x: "int"
...
...     @ts.resolve_types(globalns=globals(), localns=locals())
...     @attrs.frozen
...     class Settings:
...         opt: "list[Nested]"
...
...     return Settings, Nested
>>>
>>> Settings2, Nested2 = get_cls()
>>> attrs.fields(Settings2).opt.type
list[__test__.get_cls.<locals>.Nested]
>>> attrs.fields(Nested2).x.type
<class 'int'>
```


```{hint}
Pydantic models are not resolved ({func}`~typed_settings.resolve_types()` is a no-op),
because they [just work](https://docs.pydantic.dev/latest/concepts/postponed_annotations/) out-of-the box.
```
