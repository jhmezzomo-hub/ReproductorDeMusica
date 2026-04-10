import json
import cloudinary
import cloudinary.uploader
from obtener_info import obtener_genero

cloudinary.config(
        cloud_name = "JHMezzo",
        api_key = "344916362891248",
        api_secret = "frai2iQ4fJMvIXiSNU4rXqBgYOg"
    )

def cargar_canciones(nombre, autor, ruta, genero=None):
    try:
        info = {
            "nombre" : nombre,
            "autor" : autor,
            "genero" : genero,
            "url" : cloudinary.uploader.upload(ruta, resource_type = "video")
        }
        with open("Infos.json", "w+") as f:
            json.dump(info, f, indent=4)
    except Exception as e:
        print(e)
        pass