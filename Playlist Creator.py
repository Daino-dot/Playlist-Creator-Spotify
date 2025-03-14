import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set up your Spotify credentials
SPOTIPY_CLIENT_ID = 'TU_CLIENT_ID'
SPOTIPY_CLIENT_SECRET = 'TU_CLIENT_SECRET'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'  # You can use this to configure the application

scope = 'playlist-modify-public'

# Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=scope))

# Gets the ID of the current user
user_id = sp.current_user()['id']

# Create a new playlist
playlist_name = "TITLE"
playlist_description = "DESCRIPTION"
playlist = sp.user_playlist_create(user_id, playlist_name, public=True, description=playlist_description)
playlist_id = playlist['id']

# Songs
songs = [
    ("Bad Romance", "Lady Gaga"),         # Pop
    ("Bohemian Rhapsody", "Queen"),         # Rock
    ("Lose Yourself", "Eminem"),            # Hip-Hop
    ("Levels", "Avicii"),                   # EDM
    ("Take Me Home, Country Roads", "John Denver"),  # Country
    ("Take Five", "Dave Brubeck"),          # Jazz
    ("Moonlight Sonata", "Ludwig van Beethoven"),    # Classical
    ("No Woman, No Cry", "Bob Marley"),     # Reggae
    ("Enter Sandman", "Metallica"),         # Metal
    ("I Will Always Love You", "Whitney Houston"),   # R&B
    ("Take Me Out", "Franz Ferdinand"),     # Indie
    ("Superstition", "Stevie Wonder"),      # Funk
    ("The Thrill Is Gone", "B.B. King"),     # Blues
    ("Creep", "Radiohead"),                 # Alternative
    ("Ain't No Sunshine", "Bill Withers")    # Soul
]

track_ids = []

# Search for each song on Spotify and collect its ID
for titulo, artista in songs:
    consulta = f"track:{titulo} artist:{artista}"
    resultado = sp.search(q=consulta, type="track", limit=1)
    items = resultado.get("tracks", {}).get("items", [])
    if items:
        track_id = items[0]["id"]
        track_ids.append(track_id)
        print(f"Encontrado: {titulo} - {artista}")
    else:
        print(f"No encontrado: {titulo} - {artista}")

# Add tracks to the playlist (Spotify allows up to 100 per request)
if track_ids:
    sp.playlist_add_items(playlist_id, track_ids)
    print("¡Playlist creada exitosamente!")
