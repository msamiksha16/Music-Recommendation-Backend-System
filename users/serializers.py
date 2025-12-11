from rest_framework import serializers
from .models import UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            "id",
            "name",
            "email",
            "favorite_genres",
            "favorite_artists",
            "moods",
            "created_at",
            "updated_at",
            "active",
        ]

    def validate_favorite_genres(self, value):
        # optional: normalize input: lower-case
        return [v.strip().lower() for v in value if v]

    def validate_favorite_artists(self, value):
        return [v.strip() for v in value if v]

