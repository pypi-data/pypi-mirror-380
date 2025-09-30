from importlib.metadata import PackageNotFoundError, version

from .session import BrowsingEvent, HTMLSnapshot, SessionRecorder, SessionResult

__all__ = [
    "SessionRecorder",
    "BrowsingEvent",
    "SessionResult",
    "HTMLSnapshot",
    "__version__",
]

try:
    __version__ = version("webscrapehelper")
except PackageNotFoundError:  # pragma: no cover - local editable install fallback
    __version__ = "0.0.0"
