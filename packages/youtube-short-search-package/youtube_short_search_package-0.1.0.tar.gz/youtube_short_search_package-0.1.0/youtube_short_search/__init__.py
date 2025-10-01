"""
YouTube Short Search Library

A Python library for searching YouTube shorts and retrieving metadata including title, views, and URL.
"""

__version__ = "0.1.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

from .searcher import YouTubeShortSearcher
from .exceptions import (
    YouTubeSearchError, 
    InvalidSearchQueryError, 
    APIKeyError, 
    NetworkError, 
    NoResultsFoundError
)

__all__ = [
    "YouTubeShortSearcher", 
    "YouTubeSearchError", 
    "InvalidSearchQueryError", 
    "APIKeyError", 
    "NetworkError", 
    "NoResultsFoundError"
]
