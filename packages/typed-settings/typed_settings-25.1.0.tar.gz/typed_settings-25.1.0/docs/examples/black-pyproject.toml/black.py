from enum import Enum

import click

import typed_settings as ts


class PyVersion(Enum):
    """
    Python versions that we support.
    """

    py39 = "3.9"
    py310 = "3.10"
    py311 = "3.11"


@ts.settings
class Settings:
    """
    Black settings.

    We limit ourselves to three options.
    """

    line_length: int = 88
    skip_string_normalization: bool = False
    target_version: PyVersion = PyVersion.py311  # Better: Auto-detect


@click.command()
@ts.click_options(
    Settings,
    ts.default_loaders(
        appname="black",
        config_files=[ts.find("pyproject.toml")],
        config_file_section="tool.black",
        env_prefix=None,
    ),
)
def cli(settings: Settings) -> None:
    print(settings)


if __name__ == "__main__":
    cli()
