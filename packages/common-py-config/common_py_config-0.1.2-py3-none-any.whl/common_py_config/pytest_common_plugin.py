# common_py_config/pytest_common_plugin.py
import sys
from pathlib import Path

import pytest
from _pytest.config import Parser, PytestPluginManager, Config, _PluggyPlugin


@pytest.hookimpl
def pytest_addhooks(pluginmanager: PytestPluginManager) -> None:
    print("PYTEST_ADDHOOKS CONFTEST_PLUGIN")

@pytest.hookimpl
def pytest_plugin_registered(
    plugin: _PluggyPlugin,
    plugin_name: str,
    manager: PytestPluginManager,
) -> None:
    print(f"pytest_plugin_registered CONFTEST_PLUGIN {plugin_name}")

@pytest.hookimpl
def pytest_addoption(parser: Parser, pluginmanager: PytestPluginManager):
    """
    Example: you could add extra CLI flags here if needed.
    Coverage flags from pytest.ini are preferred.
    """
    print(f"pytest_addoption CONFTEST_PLUGIN")

    parser.addoption(
        "--extra-flag",
        action="store_true",
        help="Example extra flag injected by common plugin",
    )

@pytest.hookimpl
def pytest_configure(config: Config):
    """
    Example: automatically add <project>/src to sys.path
    so tests can import the local source code.
    """
    print("pytest_configure CONFTEST_PLUGIN")
    root = Path(config.rootdir)
    src_path = root / "src"
    if src_path.exists():
        sys.path.insert(0, str(src_path.resolve()))
        print(f"[common plugin] inserted src -> {src_path.resolve()}", flush=True)
    else:
        print(f"[common plugin] src not found at {src_path}", flush=True)
    print(config.args)
    print(config.option)

# def pytest_cmdline_parse

import configparser
from pathlib import Path

@pytest.hookimpl
def pytest_cmdline_parse(
    pluginmanager: PytestPluginManager, args: list[str]
) -> Config | None:
    print("pytest_cmdline_parse CONFTEST_PLUGIN")
    return None


@pytest.hookimpl(tryfirst=True)
def pytest_load_initial_conftests(early_config: Config, parser: Parser, args: list[str]) -> None:
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

@pytest.hookimpl
def load():
    print("LOADED")
