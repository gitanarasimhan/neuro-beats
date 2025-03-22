"""
Service for Spotify integration and music recommendations.
"""
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from ..config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

class SpotifyService:
    def __init__(self):
        client_credentials_manager = SpotifyClientCredentials(
            client_id=SPOTIFY_CLIENT_ID,
            client_secret=SPOTIFY_CLIENT_SECRET
        )
        self.sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    def get_recommendations(self, genre):
        """
        Get Spotify playlist recommendations based on genre.
        
        Args:
            genre (str): Music genre to search for
            
        Returns:
            str: URL of the recommended playlist, or None if not found
        """
        results = self.sp.search(q=f'genre:{genre}', type='playlist', limit=5)
        playlists = results['playlists']['items']
        
        if playlists:
            return playlists[0]['external_urls']['spotify']
        return None 