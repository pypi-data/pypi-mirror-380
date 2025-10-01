"""
Custom exceptions for YouTube Short Search library.
"""


class YouTubeSearchError(Exception):
    """Base exception for YouTube search related errors."""
    pass


class InvalidSearchQueryError(YouTubeSearchError):
    """Raised when the search query is invalid or empty."""
    pass


class APIKeyError(YouTubeSearchError):
    """Raised when there's an issue with the YouTube API key."""
    pass


class NetworkError(YouTubeSearchError):
    """Raised when there's a network connectivity issue."""
    pass


class NoResultsFoundError(YouTubeSearchError):
    """Raised when no YouTube shorts are found for the given query."""
    pass
