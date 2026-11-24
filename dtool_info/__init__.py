"""dtool_info package."""

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("dtool-info")
except PackageNotFoundError:
    # Package is not installed.
    __version__ = "unknown"
