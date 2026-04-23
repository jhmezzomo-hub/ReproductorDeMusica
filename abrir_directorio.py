import os
import re
from tkinter import filedialog
from pathlib import Path
import json

canciones_guardadas = []
nombres_canciones_guardadas = []

def cargar_directorio():
    carpeta = filedialog.askdirectory(title="Seleccionar carpeta de música")

    if carpeta:
        canciones_guardadas.clear()
        nombres_canciones_guardadas.clear()
        for ruta_actual, subcarpetas, archivos in os.walk(carpeta):
            for archivo in archivos:
                if archivo.lower().endswith(".mp3"):
                    ruta_completa = os.path.join(ruta_actual, archivo)
                    canciones_guardadas.append(ruta_completa)
                    nombre = os.path.splitext(archivo)[0]
                    
                    # Limpieza: Quitar números al inicio, contenido entre () o [] y espacios extra
                    nombre = re.sub(r'^\d+[\s.\-_]*', '', nombre)
                    nombre = re.sub(r'\[.*?\]|\(.*?\)', '', nombre).strip()
                    
                    nombres_canciones_guardadas.append(nombre)
        return True
    return False

def cargar_playlist_original():
    global nombres_canciones_guardadas
    folder = Path(__file__).parent
    ruta_json = folder / "playlist.json"

    if not canciones_guardadas:
        return
    
    canciones = nombres_canciones_guardadas

    playlist1 = {"original": canciones}

    try:
        if ruta_json.exists():
            with open(ruta_json, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
        else:
            datos = {}

        datos.update(playlist1)

        with open(ruta_json, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
    except (FileNotFoundError, json.JSONDecodeError):
        with open(ruta_json, "w", encoding="utf-8") as archivo:
            json.dump(playlist1, archivo, indent=4, ensure_ascii=False)