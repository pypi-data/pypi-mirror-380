from ._pip_only import enforce_pip_only
from . import __version__

def main():
    enforce_pip_only("tedit")
    from .app import run
    run()

if __name__ == "__main__":
    main()
