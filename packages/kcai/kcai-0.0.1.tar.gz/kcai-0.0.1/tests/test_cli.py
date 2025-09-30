import shlex
import subprocess

import pytest

from kcai.__main__ import execute, parse_args
from kcai._version_ import version

test_cases = [
    ("version", f"KCAI version : {version}"),  # no args
]
command_list = {"version": None}


@pytest.mark.parametrize(("command", "expected_output"), test_cases)
def test_main(capsys: pytest.CaptureFixture[str], command: str, expected_output: str) -> None:
    execute(shlex.split(command))
    output = capsys.readouterr().out.rstrip()
    assert output == expected_output


@pytest.mark.parametrize(("command", "expected_output"), test_cases)
def test_app(command: str, expected_output: str) -> None:
    full_command = ["kcai"] + shlex.split(command)
    result = subprocess.run(full_command, capture_output=True, text=True)
    output = result.stdout.rstrip()
    assert output == expected_output


@pytest.mark.parametrize(
    ("prompt", "command", "verbose", "quiet"),
    [
        # no params
        ("version", "version", False, False),
        # short params
        ("version -q", "version", False, True),
        ("version -v", "version", True, False),
        # long params TODO
    ],
)
def test_parse_args(prompt: str, command: str, quiet: str, verbose: str) -> None:
    args, _ = parse_args(shlex.split(prompt), command_list)

    # or split them up, either works
    assert args.command == command
    assert args.quiet == quiet
    assert args.verbose == verbose
