import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = ""
client_secret = ""

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,
                                                           client_secret=client_secret))

def obtener_info(nombre):
    resultado = sp.search(q=nombre, type="track", limit=1)
    if resultado["tracks"]["items"]:
        cancion_encontrada = resultado["tracks"]["items"][0]

        titulo = cancion_encontrada["name"]
        artista = cancion_encontrada["artists"][0]["name"]
        album = cancion_encontrada["album"]["name"]

        caratula_url = cancion_encontrada["album"]["images"][0]["url"]

        return titulo, artista, album, caratula_url
    else:
        print("Cancion no encntrada")
