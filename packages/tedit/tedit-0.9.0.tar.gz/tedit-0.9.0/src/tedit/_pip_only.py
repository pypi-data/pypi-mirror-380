import os, sys, pathlib
from importlib import metadata

def enforce_pip_only(package_name: str = "tedit") -> None:
    here = pathlib.Path(__file__).resolve()
    try:
        dist = metadata.distribution(package_name)
        dist_root = pathlib.Path(dist.locate_file(""))
        if not str(here).startswith(str(dist_root)):
            raise FileNotFoundError
    except Exception:
        sys.stderr.write(
            "License notice: TE may be used only when installed via pip from the official PyPI package.\n"
            f"Please run: pip install {package_name}\n"
        )
        sys.exit(1)
