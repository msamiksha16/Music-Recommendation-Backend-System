from celery import shared_task
from users.models import UserProfile
from .models import Recommendation
from .cache import set_cached_recs
from .spotify_utils import get_spotify_client_app
from .engine import generate_recommendations

@shared_task
def refresh_recommendations(user_id):
    user = UserProfile.objects.get(id=user_id)

    sp = get_spotify_client_app()

    genre = user.favorite_genres[0] if user.favorite_genres else "pop"
    mood = user.moods[0] if user.moods else None

    recs = generate_recommendations(sp, genre, mood)

    # cache it
    set_cached_recs(user_id, recs)

    # log in DB
    Recommendation.objects.create(
        user=user,
        tracks=recs,
        source="engine"
    )

    return True
