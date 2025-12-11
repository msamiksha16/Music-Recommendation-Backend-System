from rest_framework import generics
from .models import Recommendation     
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import UserProfile
from .serializers import RecommendationSerializer


class RecommendationListView(generics.ListAPIView):
    serializer_class = RecommendationSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        return Recommendation.objects.filter(user_id=user_id)
      



        
from django.shortcuts import redirect, HttpResponse
from spotipy.oauth2 import SpotifyOAuth
from django.conf import settings
import spotipy

REDIRECT_URI = "http://127.0.0.1:8000/spotify/callback"

def spotify_login(request):
    sp_oauth = SpotifyOAuth(
        client_id=settings.SPOTIFY_CLIENT_ID,
        client_secret=settings.SPOTIFY_CLIENT_SECRET,
        redirect_uri=settings.SPOTIFY_REDIRECT_URI,
        scope="user-read-email user-read-private"
    )

    auth_url = sp_oauth.get_authorize_url()
    return HttpResponseRedirect(auth_url)


import spotipy
from spotipy.oauth2 import SpotifyOAuth
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect


def spotify_callback(request):
    sp_oauth = SpotifyOAuth(
        client_id=settings.SPOTIFY_CLIENT_ID,
        client_secret=settings.SPOTIFY_CLIENT_SECRET,
        redirect_uri=settings.SPOTIFY_REDIRECT_URI,
        scope="user-read-email user-read-private"
    )

    # Read ?code=... from URL
    code = request.GET.get("code")

    # Get access token
    token_info = sp_oauth.get_access_token(code, as_dict=True)

    # SAVE token in session
    request.session["token_info"] = token_info
    request.session.modified = True

    return HttpResponseRedirect("/spotify/test/")


from .engine import generate_recommendations
def spotify_test(request):
    token_info = request.session.get("token_info")

    if not token_info:
        return HttpResponse("User not logged in.")

    access_token = token_info["access_token"]

    sp = spotipy.Spotify(auth=access_token)

    from .engine import generate_recommendations
    recs = generate_recommendations(sp, "pop", "happy")

    html = "<h2>Recommendations:</h2>"
    for r in recs:
        html += f"{r['name']} - {r['artist']}<br>"

    return HttpResponse(html)


from django.shortcuts import render, redirect
import spotipy

from .engine import generate_recommendations


def recommend(request):
    if "token_info" not in request.session:
        return redirect("/spotify/login/")

    genre = request.GET.get("genre", "pop")
    mood = request.GET.get("mood", None)

    token_info = request.session["token_info"]

    sp = spotipy.Spotify(auth=token_info["access_token"])

    recs = generate_recommendations(sp, genre, mood)

    return render(request, "results.html", {"recs": recs})

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from users.models import UserProfile
from .cache import get_cached_recs
from .tasks import refresh_recommendations

class UserRecommendationsView(APIView):

    def get(self, request, user_id):
        # verify user
        try:
            user = UserProfile.objects.get(id=user_id)
        except:
            return Response({"error": "User not found"}, status=404)

        # try cache first
        cached = get_cached_recs(user_id)
        if cached:
            return Response({"recommendations": cached}, status=200)

        # trigger background refresh
        refresh_recommendations.delay(user_id)
        return Response({"message": "Building recommendations..."}, status=202)


class UserRecommendationsRefresh(APIView):
    def post(self, request, user_id):
        refresh_recommendations.delay(user_id)
        return Response({"message": "Refresh started"}, status=202)
