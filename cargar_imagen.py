import ttkbootstrap as tb
from PIL import Image
from obtener_info import obtener_info

def cargar_imagen(ancho, alto):
    imagen = obtener_info
    try:
        Image.open(imagen[3])
        new_imagen = imagen.resize((ancho, alto))
        return new_imagen
    except Exception as e:
        print(f"No se pudo cargar la imagen: {e}")
        return
