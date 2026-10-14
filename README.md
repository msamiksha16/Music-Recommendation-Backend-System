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

## React.js Frontend

The project includes a React.js frontend built with Vite in the `frontend/` directory. It provides a responsive music discovery interface connected to the Django REST API.

Frontend features include:

* Create and update a listener profile with favorite genres, artists, and moods.
* Browse and search personalized recommendation tracks.
* Connect to Spotify through the backend OAuth flow.
* Record play, like, and skip activity and view listening stats.

To run the frontend locally, first start the Django backend and its required services. Then open a terminal in `frontend/` and run:

```sh
npm install
npm run dev
```

Open the local URL printed by Vite, usually `http://localhost:5173`. The Vite development server proxies API requests to Django at `http://127.0.0.1:8000`. Spotify-powered recommendations and login require Spotify API credentials in the backend environment. See [frontend/README.md](frontend/README.md) for full setup details.

## 🛠 Tech Stack

| 🔧 Component | 🚀 Technology |
|-------------|--------------|
| Frontend | React.js, JavaScript, Vite |
| Backend | Python, Django, DRF |
| Database | PostgreSQL |
| Caching | Redis |
| Async Processing | Celery |
| External API | Spotify Web API |
| Auth | Spotify OAuth |
| Deployment | Docker, Docker Compose |

