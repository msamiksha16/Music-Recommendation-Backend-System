import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from django.conf import settings

def get_spotify_client():
    auth = SpotifyClientCredentials(...)
    return spotipy.Spotify(auth_manager=auth)


SPOTIFY_GENRES = [
    "acoustic", "afrobeat", "alt-rock", "alternative", "ambient", "anime",
    "black-metal", "bluegrass", "blues", "bossanova", "brazil",
    "breakbeat", "british", "cantopop", "chicago-house", "children",
    "chill", "classical", "club", "comedy", "country", "dance",
    "dancehall", "death-metal", "deep-house", "detroit-techno",
    "disco", "disney", "drum-and-bass", "dub", "dubstep",
    "edm", "electro", "electronic", "emo", "folk", "forro",
    "french", "funk", "garage", "german", "gospel", "goth",
    "grindcore", "groove", "grunge", "guitar", "happy", "hard-rock",
    "hardcore", "hardstyle", "heavy-metal", "hip-hop", "holidays",
    "honky-tonk", "house", "idm", "indian", "indie",
    "indie-pop", "industrial", "iranian", "j-dance", "j-idol",
    "j-pop", "j-rock", "jazz", "k-pop", "kids", "latin",
    "latino", "malay", "mandopop", "metal", "metal-misc",
    "metalcore", "minimal-techno", "movies", "mpb", "new-age",
    "new-release", "opera", "pagode", "party", "philippines-opm",
    "piano", "pop", "pop-film", "power-pop", "progressive-house",
    "psych-rock", "punk", "punk-rock", "r-n-b", "rainy-day",
    "reggae", "reggaeton", "road-trip", "rock", "rock-n-roll",
    "rockabilly", "romance", "sad", "salsa", "samba", "sertanejo",
    "show-tunes", "singer-songwriter", "ska", "sleep", "songwriter",
    "soul", "soundtracks", "spanish", "study", "summer",
    "swedish", "synth-pop", "tango", "techno", "trance",
    "trip-hop", "turkish", "work-out", "world"
]


def get_genres():
    return {"genres": SPOTIFY_GENRES}


def get_recommendations(genres):
    sp = get_spotify_client()
    results = sp.recommendations(seed_genres=genres, limit=5)
    
    songs = []
    for track in results["tracks"]:
        songs.append({
            "title": track["name"],
            "artist": track["artists"][0]["name"],
            "url": track["external_urls"]["spotify"],
        })
    return songs
