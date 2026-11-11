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

import importlib.util
import re
import sys
from collections.abc import Callable
from pathlib import Path

ROOT = Path(__file__).resolve().parent

TARGETS: dict[str, str] = {}


def list_targets() -> None:
    if not TARGETS:
        print("run.py: no targets configured yet. Add entries to TARGETS in run.py.")
        return
    print("Available targets:")
    for name, location in sorted(TARGETS.items()):
        print(f"  {name:<12} {location}")


def load_callable(location: str) -> Callable[[list[str]], int | None]:
    path_str, _, func_name = location.partition(":")
    if not path_str or not func_name:
        raise ValueError(f"target location must look like 'path.py:function', got '{location}'")

    path = (ROOT / path_str).resolve()
    if not path.is_file():
        raise FileNotFoundError(f"target file not found: {path_str}")

    # Derive a unique, valid module name from the relative path.
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


def dispatch(name: str, args: list[str]) -> int:
    location = TARGETS.get(name)
    if location is None:
        print(f"run.py: unknown target '{name}'", file=sys.stderr)
        list_targets()
        return 2
    func = load_callable(location)
    result = func(args)
    return result if isinstance(result, int) else 0


def main(argv: list[str]) -> int:
    if not argv:
        list_targets()
        return 0
    return dispatch(argv[0], argv[1:])


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
