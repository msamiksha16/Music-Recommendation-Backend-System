from django.urls import path
from .views import (
    RecommendationListView,
    UserRecommendationsView,
    UserRecommendationsRefresh,
    recommend
)

urlpatterns = [
    # Get recommendations (uses cache + celery)
    path("<int:user_id>/", UserRecommendationsView.as_view(), name="user-recommendations"),

    # Refresh recommendations (uses celery)
    path("<int:user_id>/refresh/", UserRecommendationsRefresh.as_view(), name="user-recommendations-refresh"),

    # Web UI recommendation test
    path("recommend/", recommend, name="recommend"),
]
