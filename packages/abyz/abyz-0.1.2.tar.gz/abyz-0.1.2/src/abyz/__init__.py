from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("abyz")
except PackageNotFoundError:
    # fallback for editable installs, local runs, etc.
    __version__ = "0.0.0"

