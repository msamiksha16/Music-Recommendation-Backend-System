# Soundscape frontend

React and Vite interface for the Music Recommendation Django backend.

## Run locally

1. Start the Django API at `http://127.0.0.1:8000` and make sure its database, Redis, and Celery worker are running.
2. From this directory, install dependencies and start Vite:

   ```sh
   npm install
   npm run dev
   ```

3. Open the local URL printed by Vite (usually `http://localhost:5173`).

Vite proxies `/users`, `/recommendations`, `/analytics`, and `/spotify` to Django. To use a different backend URL, set `VITE_API_URL` in a `.env` file in this directory and update the proxy target in `vite.config.js` if you need proxied local requests.

Spotify connection requires valid `SPOTIFY_CLIENT_ID` and `SPOTIFY_CLIENT_SECRET` values in the backend environment, plus the callback URL `http://127.0.0.1:8000/spotify/callback` configured in the Spotify developer application.

The frontend stores the selected profile in this browser's local storage. Recommendations are built asynchronously by the backend; the page shows the backend's pending response while the Celery task runs.
