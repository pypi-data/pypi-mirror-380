import argparse
import sys
from unittest.mock import patch

import pytest
from ordeq import node, run
from ordeq_args import CommandLineArg
from ordeq_common import StringBuffer


def test_it_loads():
    with patch.object(sys, "argv", ["sth", "--name", "Barend"]):
        arg = CommandLineArg("--name").load()
        assert arg == "Barend"


def test_it_loads_int():
    with patch.object(sys, "argv", ["sth", "--num", "4"]):
        arg = CommandLineArg("--num", type=int).load()
        assert arg == 4


def test_it_loads_only_known_arg():
    with patch.object(sys, "argv", ["sth", "--name", "Barend", "--num", "4"]):
        arg = CommandLineArg("--num", type=int).load()
        assert arg == 4


def test_it_loads_flag():
    with patch.object(sys, "argv", ["sth", "-n", "4"]):
        arg = CommandLineArg("-n", type=int).load()
        assert arg == 4


def test_it_loads_positional_arg():
    with patch.object(sys, "argv", ["sth", "4"]):
        arg = CommandLineArg("n", type=int).load()
        assert arg == 4


def test_it_works_boolean_arg_false():
    with patch.object(sys, "argv", ["sth", "4"]):
        arg = CommandLineArg("--yes", action="store_true").load()
        assert not arg


def test_it_works_boolean_arg_true():
    with patch.object(sys, "argv", ["sth", "--yes"]):
        arg = CommandLineArg("--yes", action="store_true").load()
        assert arg


@pytest.mark.parametrize(
    ("args", "expected"),
    [
        (["--arg1", "--arg2"], "and"),
        (["--arg1"], "not and"),
        (["--arg2"], "not and"),
        ([], "not and"),
    ],
)
def test_multi_arg(args: list[str], expected: str):
    with patch.object(sys, "argv", ["sth", *args]):
        CLI = [
            CommandLineArg("--arg1", action="store_true"),
            CommandLineArg("--arg2", action="store_true"),
        ]

        def func(v1: bool, v2: bool) -> str:
            return "and" if v1 and v2 else "not and"

        x = StringBuffer()
        n = node(func, inputs=CLI, outputs=x)
        run(n)
        assert x.load() == expected


def test_multi_arg_help(capsys):
    parser = argparse.ArgumentParser("Test CLI")
    with patch.object(sys, "argv", ["sth", "--help"]):
        CLI = [
            CommandLineArg("--arg1", action="store_true", parser=parser),
            CommandLineArg("--arg2", action="store_true", parser=parser),
        ]

        def func(v1: bool, v2: bool) -> str:
            return "and" if v1 and v2 else "not and"

        x = StringBuffer()
        n = node(func, inputs=CLI, outputs=x)
        with pytest.raises(SystemExit):
            run(n)

        captured = capsys.readouterr().out
        lines = captured.splitlines()
        assert lines[-4] == "options:"
        assert lines[-3] == "  -h, --help  show this help message and exit"
        assert lines[-2] == "  --arg1"
        assert lines[-1] == "  --arg2"
        assert parser.prog == "Test CLI"
