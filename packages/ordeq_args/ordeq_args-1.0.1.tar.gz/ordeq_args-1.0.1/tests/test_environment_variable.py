import os
from collections.abc import Generator
from typing import Any

import pytest
from ordeq import IOException
from ordeq_args import EnvironmentVariable


@pytest.fixture
def env() -> Generator[None, Any, None]:
    try:
        os.environ["KEY"] = "MyKey"
        yield
    finally:
        del os.environ["KEY"]


def test_it_loads(env):
    assert EnvironmentVariable("KEY").load() == "MyKey"


def test_it_loads_with_default(env):
    assert EnvironmentVariable("KEY", default="DEFAULT").load() == "MyKey"


def test_it_loads_the_default(env):
    assert (
        EnvironmentVariable("NON_EXISTENT_KEY", default="DEFAULT").load()
        == "DEFAULT"
    )


def test_it_raises_an_error_if_key_does_not_exist(env):
    with pytest.raises(IOException):
        EnvironmentVariable("NON_EXISTENT_KEY").load()


def test_it_saves(env):
    EnvironmentVariable("KEY").save("MySavedKey")
    assert os.environ["KEY"] == "MySavedKey"
