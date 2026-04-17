import ttkbootstrap as tb
from PIL import Image, ImageTk
from obtener_info import obtener_info
from pathlib import Path
import io

def cargar_imagen(nombre):
    try:
        info = obtener_info(nombre)
        caratula_data = info["caratula"]

        if caratula_data:
            new_imagen = Image.open(io.BytesIO(caratula_data))
            new_imagen = new_imagen.resize((300, 300))
            return new_imagen
        else:
            folder =  Path(__file__).parent
            pred = folder / "album_predeterminado.png"
            pred = Image.open(pred)
            album = pred.resize((300,300))
            return album
    except Exception as e:
        print(f"No se pudo cargar la imagen: {e}")
        folder =  Path(__file__).parent
        pred = folder / "album_predeterminado.png"
        pred = Image.open(pred)
        album = pred.resize((300,300))
        return album

def imagen(panel, img_path):
    portada = cargar_imagen(img_path)
    portada = ImageTk.PhotoImage(portada)
    img = tb.Canvas(panel, relief="raised", background="#FFFFFF", width=300, height=300, bd=10)
    img.create_image(0, 0, anchor="nw", image=portada)
    img.grid(column=0, row=0, columnspan=3)
    img.reference = portada
    return img