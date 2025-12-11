import json
import redis
from django.conf import settings

r = redis.Redis(
    host=getattr(settings, "REDIS_HOST", "localhost"),
    port=getattr(settings, "REDIS_PORT", 6379),
    db=0,
    decode_responses=True
)

def set_cached_recs(user_id, recs, ttl=3600):
    key = f"user:{user_id}:recs"
    r.setex(key, ttl, json.dumps(recs))

def get_cached_recs(user_id):
    key = f"user:{user_id}:recs"
    raw = r.get(key)
    if raw:
        return json.loads(raw)
    return None
