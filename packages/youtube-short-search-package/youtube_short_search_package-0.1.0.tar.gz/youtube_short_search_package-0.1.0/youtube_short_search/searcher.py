"""
YouTube Short Searcher - Main class for searching YouTube shorts.

This module provides the main functionality for searching YouTube shorts
and retrieving metadata including title, views, and URL.
"""

import requests
import re
from typing import List, Dict, Optional
from urllib.parse import quote_plus
from .exceptions import (
    YouTubeSearchError,
    InvalidSearchQueryError,
    APIKeyError,
    NetworkError,
    NoResultsFoundError
)


class YouTubeShortSearcher:
    """
    A class for searching YouTube shorts and retrieving their metadata.
    
    This class provides methods to search for YouTube shorts based on a query string
    and retrieve information such as title, views, and URL.
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the YouTube Short Searcher.
        
        Args:
            api_key (str, optional): YouTube Data API v3 key. If not provided,
                                   will attempt to use web scraping method.
        """
        self.api_key = api_key
        self.base_url = "https://www.googleapis.com/youtube/v3"
        self.search_endpoint = f"{self.base_url}/search"
        
    def search_shorts(self, query: str, max_results: int = 10) -> List[Dict[str, str]]:
        """
        Search for YouTube shorts based on the given query.
        
        Args:
            query (str): The search query string
            max_results (int): Maximum number of results to return (default: 10)
            
        Returns:
            List[Dict[str, str]]: A list of dictionaries containing:
                - title: Video title
                - views: View count (formatted string)
                - url: YouTube video URL
                - duration: Video duration
                - channel: Channel name
                
        Raises:
            InvalidSearchQueryError: If the query is empty or invalid
            APIKeyError: If API key is invalid or missing
            NetworkError: If there's a network connectivity issue
            NoResultsFoundError: If no shorts are found
        """
        if not query or not query.strip():
            raise InvalidSearchQueryError("Search query cannot be empty")
            
        if self.api_key:
            return self._search_with_api(query, max_results)
        else:
            return self._search_with_scraping(query, max_results)
    
    def _search_with_api(self, query: str, max_results: int) -> List[Dict[str, str]]:
        """
        Search using YouTube Data API v3.
        
        Args:
            query (str): Search query
            max_results (int): Maximum results to return
            
        Returns:
            List[Dict[str, str]]: List of video information dictionaries
        """
        try:
            # Search for videos
            search_params = {
                'part': 'snippet',
                'q': query,
                'type': 'video',
                'videoDuration': 'short',  # Filter for shorts (< 4 minutes)
                'maxResults': max_results,
                'key': self.api_key,
                'order': 'relevance'
            }
            
            response = requests.get(self.search_endpoint, params=search_params, timeout=10)
            
            if response.status_code == 401:
                raise APIKeyError("Invalid or missing YouTube API key")
            elif response.status_code != 200:
                raise YouTubeSearchError(f"API request failed with status {response.status_code}")
                
            data = response.json()
            
            if 'items' not in data or not data['items']:
                raise NoResultsFoundError(f"No shorts found for query: {query}")
            
            # Get video statistics
            video_ids = [item['id']['videoId'] for item in data['items']]
            stats = self._get_video_statistics(video_ids)
            
            results = []
            for item in data['items']:
                video_id = item['id']['videoId']
                snippet = item['snippet']
                
                video_info = {
                    'title': snippet['title'],
                    'views': stats.get(video_id, {}).get('viewCount', 'N/A'),
                    'url': f"https://www.youtube.com/watch?v={video_id}",
                    'channel': snippet['channelTitle'],
                    'published': snippet['publishedAt'],
                    'description': snippet['description'][:200] + '...' if len(snippet['description']) > 200 else snippet['description']
                }
                results.append(video_info)
                
            return results
            
        except (APIKeyError, NoResultsFoundError, YouTubeSearchError):
            # Re-raise our custom exceptions without wrapping them
            raise
        except requests.exceptions.RequestException as e:
            raise NetworkError(f"Network error occurred: {str(e)}")
        except Exception as e:
            raise YouTubeSearchError(f"An error occurred during API search: {str(e)}")
    
    def _get_video_statistics(self, video_ids: List[str]) -> Dict[str, Dict[str, str]]:
        """
        Get video statistics for multiple videos.
        
        Args:
            video_ids (List[str]): List of video IDs
            
        Returns:
            Dict[str, Dict[str, str]]: Video statistics indexed by video ID
        """
        try:
            stats_params = {
                'part': 'statistics',
                'id': ','.join(video_ids),
                'key': self.api_key
            }
            
            stats_response = requests.get(
                f"{self.base_url}/videos", 
                params=stats_params, 
                timeout=10
            )
            
            if stats_response.status_code == 200:
                stats_data = stats_response.json()
                stats_dict = {}
                
                for item in stats_data.get('items', []):
                    video_id = item['id']
                    statistics = item.get('statistics', {})
                    
                    # Format view count
                    view_count = statistics.get('viewCount', '0')
                    formatted_views = self._format_view_count(int(view_count))
                    
                    stats_dict[video_id] = {
                        'viewCount': formatted_views,
                        'likeCount': statistics.get('likeCount', 'N/A'),
                        'commentCount': statistics.get('commentCount', 'N/A')
                    }
                
                return stats_dict
            
            return {}
            
        except Exception:
            return {}
    
    def _search_with_scraping(self, query: str, max_results: int) -> List[Dict[str, str]]:
        """
        Search using web scraping method (fallback when no API key).
        
        Args:
            query (str): Search query
            max_results (int): Maximum results to return
            
        Returns:
            List[Dict[str, str]]: List of video information dictionaries
        """
        try:
            # Encode the query for URL
            encoded_query = quote_plus(f"{query} shorts")
            search_url = f"https://www.youtube.com/results?search_query={encoded_query}"
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            
            response = requests.get(search_url, headers=headers, timeout=10)
            response.raise_for_status()
            
            # Extract video data using regex patterns
            # This is a simplified approach - in production, you might want to use a more robust parser
            video_pattern = r'"videoId":"([^"]+)".*?"title":{"runs":\[{"text":"([^"]+)"}.*?"viewCountText":{"simpleText":"([^"]+)"}'
            
            matches = re.findall(video_pattern, response.text)
            
            if not matches:
                raise NoResultsFoundError(f"No shorts found for query: {query}")
            
            results = []
            for i, (video_id, title, views) in enumerate(matches[:max_results]):
                video_info = {
                    'title': title,
                    'views': views,
                    'url': f"https://www.youtube.com/watch?v={video_id}",
                    'channel': 'N/A',  # Channel info is harder to extract via scraping
                    'published': 'N/A',
                    'description': 'N/A'
                }
                results.append(video_info)
            
            return results
            
        except requests.exceptions.RequestException as e:
            raise NetworkError(f"Network error occurred: {str(e)}")
        except Exception as e:
            raise YouTubeSearchError(f"An error occurred during web scraping: {str(e)}")
    
    def _format_view_count(self, view_count: int) -> str:
        """
        Format view count for display.
        
        Args:
            view_count (int): Raw view count
            
        Returns:
            str: Formatted view count (e.g., "1.2M views", "543K views")
        """
        if view_count >= 1_000_000:
            return f"{view_count / 1_000_000:.1f}M views"
        elif view_count >= 1_000:
            return f"{view_count / 1_000:.1f}K views"
        else:
            return f"{view_count} views"
    
    def get_video_details(self, video_url: str) -> Dict[str, str]:
        """
        Get detailed information about a specific YouTube video.
        
        Args:
            video_url (str): YouTube video URL
            
        Returns:
            Dict[str, str]: Video details including title, views, channel, etc.
            
        Raises:
            InvalidSearchQueryError: If the URL is invalid
            YouTubeSearchError: If unable to retrieve video details
        """
        # Extract video ID from URL
        video_id_pattern = r'(?:v=|\/embed\/|\/watch\?v=|\/v\/|youtu\.be\/)([^&\n?#]+)'
        match = re.search(video_id_pattern, video_url)
        
        if not match:
            raise InvalidSearchQueryError("Invalid YouTube URL provided")
        
        video_id = match.group(1)
        
        if self.api_key:
            return self._get_video_details_api(video_id)
        else:
            raise YouTubeSearchError("API key required for video details retrieval")
    
    def _get_video_details_api(self, video_id: str) -> Dict[str, str]:
        """
        Get video details using YouTube API.
        
        Args:
            video_id (str): YouTube video ID
            
        Returns:
            Dict[str, str]: Video details
        """
        try:
            params = {
                'part': 'snippet,statistics',
                'id': video_id,
                'key': self.api_key
            }
            
            response = requests.get(f"{self.base_url}/videos", params=params, timeout=10)
            
            if response.status_code == 401:
                raise APIKeyError("Invalid or missing YouTube API key")
            elif response.status_code != 200:
                raise YouTubeSearchError(f"API request failed with status {response.status_code}")
            
            data = response.json()
            
            if 'items' not in data or not data['items']:
                raise NoResultsFoundError("Video not found")
            
            item = data['items'][0]
            snippet = item['snippet']
            statistics = item.get('statistics', {})
            
            view_count = int(statistics.get('viewCount', 0))
            formatted_views = self._format_view_count(view_count)
            
            return {
                'title': snippet['title'],
                'views': formatted_views,
                'url': f"https://www.youtube.com/watch?v={video_id}",
                'channel': snippet['channelTitle'],
                'published': snippet['publishedAt'],
                'description': snippet['description'],
                'likes': statistics.get('likeCount', 'N/A'),
                'comments': statistics.get('commentCount', 'N/A')
            }
            
        except requests.exceptions.RequestException as e:
            raise NetworkError(f"Network error occurred: {str(e)}")
        except Exception as e:
            raise YouTubeSearchError(f"An error occurred while retrieving video details: {str(e)}")
