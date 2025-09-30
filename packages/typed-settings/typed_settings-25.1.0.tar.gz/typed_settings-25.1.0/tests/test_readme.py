"""
Extract examples from the README and assert they work.
"""

import pathlib
import subprocess
from pathlib import Path
from typing import Optional

import pytest


HERE = pathlib.Path(__file__).parent


Example = dict[str, list[str]]


def readme() -> str:
    """
    Returns the contents of the `README.md`.
    """
    return HERE.parent.joinpath("README.md").read_text(encoding="utf-8")


def load_readme() -> list[tuple[str, list[str]]]:
    """
    Extracts the examples and returns a dict mapping example titles to a list
    of all lines in that section.
    """
    lines = readme().splitlines()
    in_examples = False
    example_title = None
    examples: dict[str, list[str]] = {}
    for line in lines:
        if line == "## Examples":
            in_examples = True
            continue

        if not in_examples:
            continue

        if line.startswith("## "):
            return list(examples.items())

        if line.startswith("### ") or line.startswith("#### "):
            _, _, example_title = line.partition(" ")
            examples[example_title] = []
            continue

        if example_title:
            examples[example_title].append(line)

    # If there's another section after the examples (which there is),
    # we should not be able to get here.
    raise AssertionError("We should not have gotten here")  # pragma: no cover


@pytest.fixture
def example(request: pytest.FixtureRequest, tmp_path: Path) -> Example:
    """
    Splits the example lines into code blocks.

    If a code block starts with "# filename", write the contents to that file
    in *tmp_path*.

    Else, assume that the block contains a console session.  Lines starting
    with "$" are commands, other lines are the expected output of the above
    command.
    """
    example_lines = request.param
    code_lines: Optional[list[str]] = None
    for line in example_lines:  # pragma: no cover
        if line.startswith("```") and len(line) > 3:
            code_lines = []
            continue

        if line == "```":
            assert code_lines is not None
            if code_lines[0].startswith("# "):
                first_line, *code_lines = code_lines
                _, _, fname = first_line.partition(" ")
                contents = "\n".join(code_lines) + "\n"
                tmp_path.joinpath(fname).write_text(contents)
            else:
                cmds: dict[str, list[str]] = {}
                current_cmd: str
                for line in code_lines:
                    if line.startswith("$"):
                        _, _, current_cmd = line.partition(" ")
                        cmds[current_cmd] = []
                    else:
                        cmds[current_cmd].append(line)
                return cmds
        elif code_lines is not None:
            code_lines.append(line)

    return {}


@pytest.mark.parametrize(
    "example",
    [pytest.param(e[1], id=e[0]) for e in load_readme()],
    indirect=True,
)
def test_readme(example: Example, tmp_path: Path) -> None:
    """
    All commands in the *console* block of an example produce the exact same
    results as shown in the example.
    """
    for cmd, expected in example.items():  # pragma: no-cover
        result = subprocess.run(  # noqa: S602
            cmd,
            shell=True,
            cwd=str(tmp_path),
            capture_output=True,
            text=True,
            check=False,
        )
        assert result.stderr == ""
        assert result.stdout.splitlines() == expected
        assert result.returncode == 0
