"""
Tests for YouTube Short Searcher functionality.
"""

import pytest
from unittest.mock import Mock, patch
from youtube_short_search import (
    YouTubeShortSearcher,
    YouTubeSearchError,
    InvalidSearchQueryError,
    APIKeyError,
    NetworkError,
    NoResultsFoundError
)


class TestYouTubeShortSearcher:
    """Test cases for YouTubeShortSearcher class."""
    
    def test_init_with_api_key(self):
        """Test initialization with API key."""
        searcher = YouTubeShortSearcher(api_key="test_key")
        assert searcher.api_key == "test_key"
        assert searcher.base_url == "https://www.googleapis.com/youtube/v3"
    
    def test_init_without_api_key(self):
        """Test initialization without API key."""
        searcher = YouTubeShortSearcher()
        assert searcher.api_key is None
    
    def test_empty_search_query(self):
        """Test that empty search query raises InvalidSearchQueryError."""
        searcher = YouTubeShortSearcher()
        
        with pytest.raises(InvalidSearchQueryError):
            searcher.search_shorts("")
        
        with pytest.raises(InvalidSearchQueryError):
            searcher.search_shorts("   ")
    
    @patch('youtube_short_search.searcher.requests.get')
    def test_api_search_success(self, mock_get):
        """Test successful API search."""
        # Mock API responses
        search_response = Mock()
        search_response.status_code = 200
        search_response.json.return_value = {
            'items': [
                {
                    'id': {'videoId': 'test_video_1'},
                    'snippet': {
                        'title': 'Test Video 1',
                        'channelTitle': 'Test Channel',
                        'publishedAt': '2023-01-01T00:00:00Z',
                        'description': 'Test description'
                    }
                }
            ]
        }
        
        stats_response = Mock()
        stats_response.status_code = 200
        stats_response.json.return_value = {
            'items': [
                {
                    'id': 'test_video_1',
                    'statistics': {
                        'viewCount': '1000000',
                        'likeCount': '50000',
                        'commentCount': '1000'
                    }
                }
            ]
        }
        
        mock_get.side_effect = [search_response, stats_response]
        
        searcher = YouTubeShortSearcher(api_key="test_key")
        results = searcher.search_shorts("test query")
        
        assert len(results) == 1
        assert results[0]['title'] == 'Test Video 1'
        assert results[0]['views'] == '1.0M views'
        assert results[0]['url'] == 'https://www.youtube.com/watch?v=test_video_1'
    
    @patch('youtube_short_search.searcher.requests.get')
    def test_api_search_invalid_key(self, mock_get):
        """Test API search with invalid key."""
        mock_response = Mock()
        mock_response.status_code = 401
        mock_get.return_value = mock_response
        
        searcher = YouTubeShortSearcher(api_key="invalid_key")
        
        with pytest.raises(APIKeyError):
            searcher.search_shorts("test query")
    
    @patch('youtube_short_search.searcher.requests.get')
    def test_api_search_no_results(self, mock_get):
        """Test API search with no results."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'items': []}
        mock_get.return_value = mock_response
        
        searcher = YouTubeShortSearcher(api_key="test_key")
        
        with pytest.raises(NoResultsFoundError):
            searcher.search_shorts("no results query")
    
    def test_format_view_count(self):
        """Test view count formatting."""
        searcher = YouTubeShortSearcher()
        
        assert searcher._format_view_count(500) == "500 views"
        assert searcher._format_view_count(1500) == "1.5K views"
        assert searcher._format_view_count(1000000) == "1.0M views"
        assert searcher._format_view_count(2500000) == "2.5M views"
    
    def test_invalid_video_url(self):
        """Test get_video_details with invalid URL."""
        searcher = YouTubeShortSearcher(api_key="test_key")
        
        with pytest.raises(InvalidSearchQueryError):
            searcher.get_video_details("invalid_url")
    
    def test_video_url_extraction(self):
        """Test video ID extraction from various URL formats."""
        searcher = YouTubeShortSearcher(api_key="test_key")
        
        urls = [
            "https://www.youtube.com/watch?v=test_id_123",
            "https://youtu.be/test_id_123",
            "https://www.youtube.com/embed/test_id_123",
        ]
        
        for url in urls:
            # We're testing the regex pattern indirectly
            try:
                searcher.get_video_details(url)
            except YouTubeSearchError:
                # Expected since we don't have a valid API response
                pass
            except InvalidSearchQueryError:
                pytest.fail(f"URL {url} should be valid")
    
    @patch('youtube_short_search.searcher.requests.get')
    def test_network_error(self, mock_get):
        """Test network error handling."""
        mock_get.side_effect = Exception("Network error")
        
        searcher = YouTubeShortSearcher(api_key="test_key")
        
        with pytest.raises(YouTubeSearchError):
            searcher.search_shorts("test query")
    
    def test_scraping_without_api_key(self):
        """Test that scraping method is called without API key."""
        searcher = YouTubeShortSearcher()
        
        # This test would require mocking the web scraping, but for now
        # we just ensure the method exists and can be called
        try:
            searcher.search_shorts("test")
        except (NetworkError, NoResultsFoundError, YouTubeSearchError):
            # These are expected since we're not mocking the web request
            pass


class TestExceptions:
    """Test custom exception classes."""
    
    def test_youtube_search_error(self):
        """Test YouTubeSearchError exception."""
        with pytest.raises(YouTubeSearchError):
            raise YouTubeSearchError("Test error")
    
    def test_invalid_search_query_error(self):
        """Test InvalidSearchQueryError exception."""
        with pytest.raises(InvalidSearchQueryError):
            raise InvalidSearchQueryError("Invalid query")
    
    def test_api_key_error(self):
        """Test APIKeyError exception."""
        with pytest.raises(APIKeyError):
            raise APIKeyError("API key error")
    
    def test_network_error(self):
        """Test NetworkError exception."""
        with pytest.raises(NetworkError):
            raise NetworkError("Network error")
    
    def test_no_results_found_error(self):
        """Test NoResultsFoundError exception."""
        with pytest.raises(NoResultsFoundError):
            raise NoResultsFoundError("No results")
