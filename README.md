# Music-Recommendation-Backend-System

This backend service powers a Music Discovery App that gives personalized recommendations from the Spotify API, stores user preferences, caches results using Redis, and performs async tasks using Celery.

🚀 Features Implemented
✔ User Management

Create & update user profiles

Store preferences:

🎵 Favorite genres

🎤 Favorite artists

😊 Moods

Retrieve user profile (GET /users/{id}/)

🎵 2. Recommendations Engine

Fetch recommendations from Spotify Web API

Cache results using Redis

Background refresh using Celery Worker

Store recommendation logs in PostgreSQL

🎧 3. User Activity Tracking

Users can log actions:

❤️ like

▶️ play

⏭️ skip

Activities stored in PostgreSQL

Used for analytics and engagement insights

📊 4. Analytics Endpoints

Total users

Total activity events

Most liked tracks

Trending genres / artists

User-specific engagement summary

🔐 5. Spotify OAuth Integration

Login with Spotify account

Secure access token storage in session

Use Spotify token for personalized recommendation fetching

🗄️ 6. Database Layer (PostgreSQL)

Tables implemented:

UserProfile

Recommendation

UserActivity

🐳 7. Dockerized Infrastructure

(Optional but implemented if needed)

Django API Server

PostgreSQL DB

Redis Cache

Celery Worker

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

