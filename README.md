# Music-Recommendation-Backend-System

This backend service powers a Music Discovery App that gives personalized recommendations from the Spotify API, stores user preferences, caches results using Redis, and performs async tasks using Celery.

🚀 Features Implemented
✔ User Management

* Create/update profile

* Save genres, moods, favorite artists

*GET user profile

✔ Recommendations Engine

* Fetch Spotify recommendations

* Cache results in Redis

* Celery background task refresh

* Store logs in PostgreSQL

✔ User Activity Tracking

* Users can “play”, “like”, “skip” tracks

* Logged in PostgreSQL

* Used for analytics

✔ Analytics APIs

* Total users

* Most liked songs

* Trending artists

* User-specific engagement summary

✔ Spotify OAuth Integration

* Login using Spotify

* Use authorized token for recommendations

✔ Database

* Full PostgreSQL schema

* User, Recommendation, Activity

✔ Dockerized Stack

* Django backend

* PostgreSQL

* Redis

* Celery worker

## 🛠 Tech Stack

| 🔧 Component | 🚀 Technology |
|-------------|--------------|
| Backend | Python, Django, DRF |
| Database | PostgreSQL |
| Caching | Redis |
| Async Processing | Celery |
| External API | Spotify Web API |
| Auth | Spotify OAuth |
| Deployment | Docker, Docker Compose |

