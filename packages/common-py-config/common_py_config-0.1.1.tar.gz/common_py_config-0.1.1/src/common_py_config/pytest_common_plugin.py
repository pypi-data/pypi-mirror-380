# common_py_config/pytest_common_plugin.py
import sys
from pathlib import Path

def pytest_addoption(parser):
    """
    Example: you could add extra CLI flags here if needed.
    Coverage flags from pytest.ini are preferred.
    """
    parser.addoption(
        "--extra-flag",
        action="store_true",
        help="Example extra flag injected by common plugin",
    )

def pytest_configure(config):
    """
    Example: automatically add <project>/src to sys.path
    so tests can import the local source code.
    """
    root = Path(config.rootdir)
    src_path = root / "src"
    if src_path.exists():
        sys.path.insert(0, str(src_path.resolve()))
        print(f"[common plugin] inserted src -> {src_path.resolve()}", flush=True)
    else:
        print(f"[common plugin] src not found at {src_path}", flush=True)
