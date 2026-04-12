import ttkbootstrap as tb
from PIL import Image
from obtener_info import obtener_info
from pathlib import Path

def cargar_imagen():
    imagen = obtener_info
    try:
        new_imagen = Image.open(imagen[3]).convert("RGBA")
        new_imagen = imagen.resize((300, 300))
        return new_imagen
    except Exception as e:
        print(f"No se pudo cargar la imagen: {e}")
        folder =  Path(__file__).parent
        pred = folder / "album_predeterminado.png"
        pred = Image.open(pred).convert("RGBA")
        album = pred.resize((300,300))
        return album
