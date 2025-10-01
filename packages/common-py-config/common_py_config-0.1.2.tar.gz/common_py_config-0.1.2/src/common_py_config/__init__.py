import configparser
from pathlib import Path

import pytest
from _pytest.config import Parser, Config


def pytest_load_initial_conftests(args: list[str]) -> None:
    """
    Inject defaults from common pytest.ini, unless overridden locally.
    """
    print("pytest_load_initial_conftests CONFTEST_PLUGIN")
    cfg_path = Path(__file__).parent.parent.parent / "pytest.ini"

    assert cfg_path.exists(), f"common pytest.ini not found at {cfg_path}"
    # if not cfg_path.exists():
    #     return

    parser = configparser.ConfigParser()
    parser.read(cfg_path)

    if parser.has_section("pytest") and parser.has_option("pytest", "addopts"):
        common_addopts = parser.get("pytest", "addopts").split()

        # If user already passed --cov or other opts, don’t duplicate
        if not any(opt.startswith("--cov") for opt in args):
            args[:] = common_addopts + args

    print("ARGUEMNTS", args)