from django.db import models
from django.core.validators import EmailValidator
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone

class UserProfile(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    # store list of genres/artists/moods as Postgres text arrays
    favorite_genres = ArrayField(models.CharField(max_length=100), default=list, blank=True)
    favorite_artists = ArrayField(models.CharField(max_length=200), default=list, blank=True)
    moods = ArrayField(models.CharField(max_length=50), default=list, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # optional flags
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} <{self.email}>"

