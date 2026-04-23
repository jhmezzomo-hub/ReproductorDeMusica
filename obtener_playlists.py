import json
from pathlib import Path
from abrir_directorio import limpiar_nombre 

playlist = {}
nombre_playlist = []
folder = Path(__file__).parent
ruta_json = folder / "playlist.json"

def abrir_playlist():
    global playlist, nombre_playlist
    try:
        with open(ruta_json, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            playlist.clear()
            playlist.update(datos)
            nombre_playlist.clear()
            for key in datos.keys():
                nombre_playlist.append(key)
    except (FileNotFoundError, json.JSONDecodeError):
        playlist.clear()
        nombre_playlist.clear()

def guardar_playlist_en_json():
    """Función auxiliar para guardar el diccionario de playlist actual en el archivo JSON."""
    global playlist
    try:
        with open(ruta_json, "w", encoding="utf-8") as archivo:
            json.dump(playlist, archivo, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error al guardar la playlist en JSON: {e}")

def crear_nueva_playlist(nueva_playlist):
    global playlist, nombre_playlist
    if not nueva_playlist or not isinstance(nueva_playlist, str):
        print("El nombre de la playlist no es válido.")
        return False

    if nueva_playlist in playlist:
        print(f"La playlist '{nueva_playlist}' ya existe.")
        return False

    playlist[nueva_playlist] = []
    nombre_playlist.append(nueva_playlist)
    guardar_playlist_en_json()
    print(f"Playlist '{nueva_playlist}' creada exitosamente.")
    abrir_playlist()
    return True

def agregar_cancion_a_playlist(ruta_cancion, nombre_playlist_destino):
    global playlist

    if not nombre_playlist_destino or nombre_playlist_destino not in playlist:
        print(f"La playlist '{nombre_playlist_destino}' no existe.")
        return False

    if not ruta_cancion or not Path(ruta_cancion).is_file():
        print(f"La ruta de la canción '{ruta_cancion}' no es válida o el archivo no existe.")
        return False

    cleaned_song_name = limpiar_nombre(ruta_cancion)

    if cleaned_song_name in playlist[nombre_playlist_destino]:
        print(f"La canción '{cleaned_song_name}' ya está en la playlist '{nombre_playlist_destino}'.")
        return False

    playlist[nombre_playlist_destino].append(cleaned_song_name)
    guardar_playlist_en_json()
    print(f"Canción '{cleaned_song_name}' agregada a la playlist '{nombre_playlist_destino}'.")
    return True
