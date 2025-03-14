# Playlist Creator: Spotify

This guide will help you obtain your **Client ID**, **Client Secret**, and set up the **Redirect URI** for your Spotify API project. Use this information to authenticate your app and create or modify playlists.

## 1. Create or Log in to Your Spotify Account

- **If you don't have an account:**  
  Sign up at [Spotify](https://www.spotify.com).

- **If you already have an account:**  
  Simply log in with your credentials.

## 2. Access the Spotify Developer Dashboard

- Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
- Log in using your Spotify account.

## 3. Create a New Application

- Click on **"Create an App"**.
- Fill in the required fields:
  - **Name:** For example, "Moto Playlist Creator".
  - **Description:** A brief description of your project.
- Accept the terms and conditions.

## 4. Get Your Client ID and Client Secret

- Once your application is created, you will see the **Client ID** on the application details page.
- To view your **Client Secret**, click on the option to reveal or copy the secret.
- **Important:** Store both values securely.

## 5. Configure the Redirect URI

- In your application details page, click on **"Edit Settings"** or **"Configurations"**.
- In the **Redirect URIs** section, add the URL where you want users to be redirected after authentication. For example:
http://localhost:8888/callback
- Save the changes.

## 6. Using Your Credentials in the Project

With your credentials ready, integrate them into your application. For example, using the [Spotipy](https://spotipy.readthedocs.io/) library in Python:

```python
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Replace these with your credentials
SPOTIPY_CLIENT_ID = 'YOUR_CLIENT_ID'
SPOTIPY_CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'

scope = 'playlist-modify-public'

# Authenticate and create a Spotipy instance
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                             client_secret=SPOTIPY_CLIENT_SECRET,
                                             redirect_uri=SPOTIPY_REDIRECT_URI,
                                             scope=scope))
