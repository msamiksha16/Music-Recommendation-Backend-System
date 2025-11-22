# Music-Recommendation-Backend-System

This backend service powers a Music Discovery App that gives personalized recommendations from the Spotify API, stores user preferences, caches results using Redis, and performs async tasks using Celery.

✨ Features

* User Profile Management: Create and update user profiles with name, email, favorite genres, artists, and moods.

* Spotify-Powered Recommendations: Fetch personalized song recommendations using Spotify Web API.

* Caching with Redis: Cache user recommendations to reduce duplicate API calls and speed up responses.

* Asynchronous Processing with Celery: Refresh recommendations in the background without blocking the API.

* Recommendation Logging: Store generated recommendations in PostgreSQL for analytics and history.

* User Activity Tracking: Log actions like play, like, skip to measure engagement.

* Analytics & Insights:

    * Total users

    * Trending genres

    * Trending artists

    * Most liked tracks

    * User-specific engagement summary

* Spotify OAuth Integration: Authenticate users via Spotify to personalize recommendations.

* PostgreSQL Database: Robust schema for users, recommendations, and user activity.

* Docker Support: Containerized services (Django, PostgreSQL, Redis, Celery Worker) for easy deployment.

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

