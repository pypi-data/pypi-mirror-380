from importlib import metadata

from langchain_cloudsway.smartsearch import SmartsearchTool

try:
    __version__ = metadata.version(__package__ or "langchain-cloudsway")
except metadata.PackageNotFoundError:
    __version__ = ""
del metadata

__all__ = [
    "SmartsearchTool",
    "__version__",
]