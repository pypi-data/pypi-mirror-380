from importlib.metadata import version, PackageNotFoundError
from . import agent

try:
    __version__ = version("skeptofox")
except PackageNotFoundError:
    # Fallback for when the package is not installed
    __version__ = "0.1.0"