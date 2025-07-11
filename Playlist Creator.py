import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# === CONFIGURATION ===
SPOTIPY_CLIENT_ID = 'spotify_client_ID'
SPOTIPY_CLIENT_SECRET = 'spotify_client_secret'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'

scope = 'playlist-modify-public'

# === AUTHENTICATION ===
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope=scope
))

# === FUNCTIONS ===

def crear_playlist(nombre, descripcion=""):
    user_id = sp.current_user()['id']
    playlist = sp.user_playlist_create(user_id, nombre, public=True, description=descripcion)
    print(f"🎵 created playlist: {nombre}")
    return playlist['id']

def buscar_y_confirmar_cancion(nombre_cancion):
    resultado = sp.search(q=nombre_cancion, type="track", limit=5)
    canciones = resultado.get("tracks", {}).get("items", [])
    
    if not canciones:
        print(f"❌ No match found for '{nombre_cancion}'")
        return None

    print(f"\n🎧 Results for '{nombre_cancion}':")
    for idx, item in enumerate(canciones):
        nombre = item['name']
        artista = item['artists'][0]['name']
        print(f"{idx + 1}. {nombre} - {artista}")
    
    seleccion = input("Select the correct song number (0 to cancel): ")
    if not seleccion.isdigit():
        print("⚠️ Invalid entry.")
        return None

    seleccion = int(seleccion)
    if seleccion < 1 or seleccion > len(canciones):
        print("🚫 Selection cancelled.")
        return None

    return canciones[seleccion - 1]['id']

def agregar_canciones_a_playlist(playlist_id, canciones):
    if canciones:
        sp.playlist_add_items(playlist_id, canciones)
        print("✅ Songs added to the playlist.")
    else:
        print("🚫 There are no songs to add.")

# === MAIN FLOW ===

def main():
    nombre_playlist = input("🎼 Playlist name: ")
    descripcion_playlist = input("📝 Description (optional): ")
    playlist_id = crear_playlist(nombre_playlist, descripcion_playlist)

    canciones_para_agregar = []

    print("\n🔍 Type song names to search. Type 'end' to finish.\n")

    while True:
        entrada = input("Song name: ")
        if entrada.strip().lower() == 'end':
            break
        track_id = buscar_y_confirmar_cancion(entrada)
        if track_id:
            canciones_para_agregar.append(track_id)

    agregar_canciones_a_playlist(playlist_id, canciones_para_agregar)

if __name__ == "__main__":
    main()
