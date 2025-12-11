from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count

from analytics.models import UserActivity
from users.models import UserProfile


# --------- SUMMARY FOR ALL USERS -------------
class AnalyticsSummary(APIView):
    def get(self, request):
        total_users = UserProfile.objects.count()
        total_activity = UserActivity.objects.count()

        most_liked = (
            UserActivity.objects
            .filter(action="like")
            .values("track_name", "artist")
            .annotate(count=Count("id"))
            .order_by("-count")
        )

        return Response({
            "total_users": total_users,
            "total_activity_events": total_activity,
            "most_liked_tracks": list(most_liked[:5]),
        })


# --------- TRENDING ARTISTS & GENRES ----------
class AnalyticsTrends(APIView):
    def get(self, request):

        trending_artists = (
            UserActivity.objects
            .values("artist")
            .annotate(count=Count("id"))
            .order_by("-count")
        )

        trending_genres = (
            UserProfile.objects
            .values("favorite_genres")
            .annotate(count=Count("id"))
            .order_by("-count")
        )

        return Response({
            "trending_artists": trending_artists[:5],
            "trending_genres": trending_genres[:5],
        })


# --------- USER-SPECIFIC ANALYTICS ----------
class UserAnalytics(APIView):
    def get(self, request, user_id):

        try:
            user = UserProfile.objects.get(id=user_id)
        except:
            return Response({"error": "User not found"}, status=404)

        activities = UserActivity.objects.filter(user_id=user_id)

        return Response({
            "user": user.name,
            "total_events": activities.count(),
            "likes": activities.filter(action="like").count(),
            "plays": activities.filter(action="play").count(),
            "skips": activities.filter(action="skip").count(),
        })


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserActivity
from analytics.serializers import UserActivitySerializer
from rest_framework.parsers import JSONParser

class ActivityView(APIView):
    parser_classes = [JSONParser]   # <-- ADD THIS LINE
    def post(self, request):
        serializer = UserActivitySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)
