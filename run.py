"""Central dispatcher for the codepy lab.

Usage:
    python run.py                 # list configured targets
    python run.py <target> [args] # run a configured target

Each entry in TARGETS maps a name to a "module:function" string. The function
is called with the remaining command-line arguments and should return an int
exit code (or None for success).
"""

import importlib
import sys

TARGETS: dict[str, str] = {}


def list_targets() -> None:
    if not TARGETS:
        print("run.py: no targets configured yet. Add entries to TARGETS in run.py.")
        return
    print("Available targets:")
    for name, location in sorted(TARGETS.items()):
        print(f"  {name:<12} {location}")


def dispatch(name: str, args: list[str]) -> int:
    location = TARGETS.get(name)
    if location is None:
        print(f"run.py: unknown target '{name}'", file=sys.stderr)
        list_targets()
        return 2
    module_name, _, func_name = location.partition(":")
    module = importlib.import_module(module_name)
    func = getattr(module, func_name)
    result = func(args)
    return result if isinstance(result, int) else 0


def main(argv: list[str]) -> int:
    if not argv:
        list_targets()
        return 0
    return dispatch(argv[0], argv[1:])


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
