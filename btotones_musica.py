import ttkbootstrap as tb
from funciones import *
from cargar_imagen import imagen
from obtener_info import obtener_info

def play(panel):
    play_bt = tb.Button(panel, text="Play ", style="success.TButton",command=reproducir)
    play_bt.grid(column=2, row=3, sticky="nsew", padx=10, pady=10, ipadx=5, ipady=5)
    return play_bt

def pause(panel):
    pause_bt = tb.Button(panel, text="Pause", style="secondary.TButton", command=pausar)
    pause_bt.grid(column=1, row=3, sticky="nsew", padx=10, pady=10, ipadx=5, ipady=5)
    return pause_bt

def stop(panel):
    frenar_bt = tb.Button(panel, text="Stop", style="primary.TButton", command=frenar)
    frenar_bt.grid(column=0, row=3, sticky="nsew", padx=10, pady=10, ipadx=5, ipady=5)
    return frenar_bt

def cargar_vista(panel,nombre="default"):
    if nombre == "default":
        titulo = "Ninguna canción seleccionada"
        artista = "No encontrado"
        nombre = "album_predeterminado.png"
    else:
        print(f"Cargando vista para: {nombre}")
        info = obtener_info(nombre)
        titulo = info[0]
        artista = info[1]
    
    title = tb.Label(panel, text=titulo, bootstyle="light", font=("Roboto", 16, "bold"))
    title. grid(column=0, row=1, columnspan=3, pady=5, padx=5)

    artist = tb.Label(panel, text=artista, bootstyle="info", font=("Roboto", 12))
    artist.grid(column=0, row=2, columnspan=2, pady=5, padx=5)

    img = imagen(panel, nombre)

    return title, artist, img