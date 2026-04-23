import json
from pathlib import Path

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
