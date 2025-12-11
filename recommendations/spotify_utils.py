import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from django.conf import settings


def get_spotify_client_app():
    """
    App-only authentication for background tasks.
    """
    auth = SpotifyClientCredentials(
        client_id=settings.SPOTIFY_CLIENT_ID,
        client_secret=settings.SPOTIFY_CLIENT_SECRET,
    )
    return spotipy.Spotify(auth_manager=auth)


def get_spotify_client_user(access_token):
    """
    User-authenticated client (if needed later).
    """
    return spotipy.Spotify(auth=access_token)
