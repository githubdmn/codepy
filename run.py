"""Central dispatcher for the codepy lab.

Usage:
    python run.py                 # list configured targets
    python run.py <target> [args] # run a configured target

Each entry in TARGETS maps a name to a "path/to/file.py:function" string. The
file is loaded directly by path, so folders whose names start with digits
(e.g. 02-scripts) work. The function is called with the remaining
command-line arguments and should return an int exit code (or None for
success).
"""

import importlib
import importlib.util
import re
import sys
from collections.abc import Callable
from pathlib import Path

ROOT = Path(__file__).resolve().parent

TARGETS: dict[str, str] = {
    "fastapi": "fastapi_fundamentals.main:app",
}

# What `python run.py` (and `make run`) runs when no target is given.
DEFAULT = "fastapi"

# How to serve ASGI apps. Edit here if you change port/host.
SERVE_HOST = "127.0.0.1"
SERVE_PORT = 8000


def list_targets() -> None:
    if not TARGETS:
        print("run.py: no targets configured yet. Add entries to TARGETS in run.py.")
        return
    print("Available targets:")
    for name, location in sorted(TARGETS.items()):
        marker = " *" if name == DEFAULT else ""
        print(f"  {name:<12} {location}{marker}")
    print(f"\n* = default (run by `python run.py` / `make run`)")


def _load_by_path(path_str: str, func_name: str) -> Callable[[list[str]], int | None]:
    path = (ROOT / path_str).resolve()
    if not path.is_file():
        raise FileNotFoundError(f"target file not found: {path_str}")
    module_name = "codepy_target_" + re.sub(r"\W", "_", path.relative_to(ROOT).as_posix())
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load module from {path_str}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    func = getattr(module, func_name, None)
    if not callable(func):
        raise AttributeError(f"'{func_name}' not found or not callable in {path_str}")
    return func


def _load_by_module(module_path: str, attr: str):
    module = importlib.import_module(module_path)
    obj = getattr(module, attr, None)
    if obj is None:
        raise AttributeError(f"'{attr}' not found in module {module_path}")
    return obj


def dispatch(name: str, args: list[str]) -> int:
    location = TARGETS.get(name)
    if location is None:
        print(f"run.py: unknown target '{name}'", file=sys.stderr)
        list_targets()
        return 2

    target, _, attr = location.partition(":")
    if not target or not attr:
        raise ValueError(
            f"target location must be 'path.py:function' or 'module:app', got '{location}'"
        )

    # Heuristic: ".py" in the path portion -> file-based script.
    # Otherwise -> importable module (ASGI app / callable).
    if target.endswith(".py"):
        func = _load_by_path(target, attr)
        result = func(args)
        return result if isinstance(result, int) else 0

    # Module path -> ASGI app object; serve it with uvicorn.
    import uvicorn  # local import: only needed when actually serving

    obj = _load_by_module(target, attr)
    if not callable(obj):
        raise TypeError(
            f"'{target}:{attr}' is not callable and doesn't look like an ASGI app"
        )
    uvicorn.run(obj, host=SERVE_HOST, port=SERVE_PORT, reload=False)
    return 0


def main(argv: list[str]) -> int:
    if not argv:
        return dispatch(DEFAULT, [])
    if argv[0] in ("-h", "--help", "list"):
        list_targets()
        return 0
    return dispatch(argv[0], argv[1:])


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
