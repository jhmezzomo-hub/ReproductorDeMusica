from mutagen.mp3 import MP3
from mutagen.id3 import ID3
import os

def obtener_info(ruta):
    nombre_arch = os.path.basename(ruta)

    metadata = {
        "titulo" : nombre_arch,
        "artista" : "Artista Desconocido",
        "caratula" : None
        }
    
    if ruta == "default":
        return metadata

    try: 
        audio = MP3(ruta, ID3=ID3)
        
        if "TIT2" in audio:
            metadata["titulo"] = audio["TIT2"].text[0]

        if "TPE1" in audio:
            metadata["artista"] = audio["TPE1"].text[0]

        for etiqueta in audio.keys():
            if etiqueta.startswith("APIC:"):
                metadata["caratula"] = audio[etiqueta].data
                break

    except Exception as e:
        print(f"Error al obtener información de {ruta}: {e}")

    return metadata
    