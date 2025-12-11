from django.db import models
from users.models import UserProfile
from django.db import models

class Recommendation(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="recommendations")
    tracks = models.JSONField(default=list)
    source = models.CharField(max_length=50, default="spotify")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Recommendations for {self.user.name}"
