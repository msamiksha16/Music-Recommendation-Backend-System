from django.urls import path
from .views import AnalyticsSummary, AnalyticsTrends, UserAnalytics, ActivityView


urlpatterns = [
    path("activity/", ActivityView.as_view()),

    path("summary/", AnalyticsSummary.as_view()),
    path("trends/", AnalyticsTrends.as_view()),
    path("user/<int:user_id>/", UserAnalytics.as_view()),
]
