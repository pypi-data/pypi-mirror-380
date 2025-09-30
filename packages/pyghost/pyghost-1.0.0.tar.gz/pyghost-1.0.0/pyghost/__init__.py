"""
PyGhost - A Python wrapper for Ghost Admin API

A modular, easy-to-use Python library for interacting with Ghost CMS Admin API.
"""

from .client import GhostClient
from .posts import Posts
from .pages import Pages
from .tiers import Tiers
from .newsletters import Newsletters
from .offers import Offers
from .members import Members
from .users import Users
from .images import Images
from .themes import Themes
from .webhooks import Webhooks
from .exceptions import (
    GhostAPIError,
    AuthenticationError,
    ValidationError,
    NotFoundError,
    RateLimitError
)

__version__ = "1.0.0"
__author__ = "PyGhost Contributors"
__all__ = [
    "GhostClient",
    "Posts",
    "Pages",
    "Tiers",
    "Newsletters",
    "Offers",
    "Members",
    "Users",
    "Images",
    "Themes",
    "Webhooks",
    "GhostAPIError",
    "AuthenticationError",
    "ValidationError",
    "NotFoundError",
    "RateLimitError"
]
