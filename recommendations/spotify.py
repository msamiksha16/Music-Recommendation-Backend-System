import requests
import base64
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")


def get_spotify_access_token():
    auth_string = f"{CLIENT_ID}:{CLIENT_SECRET}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {"grant_type": "client_credentials"}

    response = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)

    return response.json().get("access_token")


def get_spotify_recommendations(genres):
    token = get_spotify_access_token()

    headers = {
        "Authorization": f"Bearer {token}"
    }

    url = "https://api.spotify.com/v1/recommendations"

    params = {
        "seed_genres": ",".join(genres),
        "limit": 5
    }

    response = requests.get(url, headers=headers, params=params)

    data = response.json()

    tracks = []

    for item in data.get("tracks", []):
        tracks.append({
            "title": item["name"],
            "artist": item["artists"][0]["name"],
            "url": item["external_urls"]["spotify"]
        })

    return tracks
