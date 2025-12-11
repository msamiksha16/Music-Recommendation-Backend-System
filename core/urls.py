from django.contrib import admin
from django.urls import path, include
from recommendations import views
from recommendations.views import recommend
from .views import home

urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),

    # Users API
    path("users/", include("users.urls")),

    # Recommendations API
    path("recommendations/", include("recommendations.urls")),

    # Spotify OAuth
    path("spotify/login/", views.spotify_login),
    path("spotify/callback/", views.spotify_callback),
    path("spotify/test/", views.spotify_test),
    path("spotify/recommend/", recommend),
    path("analytics/", include("analytics.urls")),

]
