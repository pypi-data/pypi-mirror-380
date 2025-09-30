from ._pip_only import enforce_pip_only
from importlib import import_module
import sys

def main():
    enforce_pip_only("tedit")
    mod = import_module("tedit.app")
    entry = getattr(mod, "run", None) or getattr(mod, "main", None)
    if entry is None:
        sys.stderr.write(
            "tedit.app must define a 'run()' or 'main()' function as the entry point.\n"
        )
        sys.exit(1)
    return entry()

if __name__ == "__main__":
    main()
