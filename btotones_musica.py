import ttkbootstrap as tb
from funciones import *
from cargar_imagen import imagen
from obtener_info import obtener_info
from marquesina import marquesina
import os

reproductor = Reproductor()
cancion_actual = None
barra_progreso = None
current_title_label = None
current_artist_label = None
current_image_canvas = None

def alternar_modo_compacto(compacto):
    """Oculta o muestra la imagen para que el panel se achique."""
    if current_image_canvas:
        if compacto:
            current_image_canvas.grid_remove()
        else:
            current_image_canvas.grid()

def actualizar_barra(panel):
    if barra_progreso:
        posicion = reproductor.obtener_posicion()
        if posicion >= 0:
            barra_progreso['value'] = posicion * 100
        panel.after(1000, lambda: actualizar_barra(panel))

def play(panel):
    def reproducir_cancion():
        if cancion_actual:
            reproductor.reproducir(cancion_actual)
        actualizar_barra(panel)
    play_bt = tb.Button(panel, text="Play ", style="success.TButton",command=reproducir_cancion)
    play_bt.grid(column=2, row=4, sticky="nsew", padx=10, pady=10, ipadx=5, ipady=5)
    return play_bt

def pause(panel):
    pause_bt = tb.Button(panel, text="Pause", style="secondary.TButton", command=reproductor.pausar)
    pause_bt.grid(column=1, row=4, sticky="nsew", padx=10, pady=10, ipadx=5, ipady=5)
    return pause_bt

def stop(panel):
    frenar_bt = tb.Button(panel, text="Stop", style="primary.TButton", command=reproductor.frenar)
    frenar_bt.grid(column=0, row=4, sticky="nsew", padx=10, pady=10, ipadx=5, ipady=5)
    return frenar_bt

def cargar_vista(panel, nombre="default"):
    global barra_progreso, cancion_actual, current_title_label, current_artist_label, current_image_canvas

    # Destruir los widgets anteriores si existen
    if current_title_label:
        current_title_label.destroy()
    if current_artist_label:
        current_artist_label.destroy()
    if current_image_canvas:
        current_image_canvas.destroy()
    cancion_actual = nombre if nombre != "default" else None
    print(f"Cargando vista para: {nombre}")
    info = obtener_info(nombre)
    titulo = info["titulo"]
    artista = info["artista"]

    if titulo.endswith(".mp3"):
        titulo = os.path.splitext(titulo)[0] 
    current_title_label = tb.Label(panel, text=titulo, bootstyle="light", font=("Roboto", 16, "bold"))
    marquesina(current_title_label, titulo)
    current_title_label.grid(column=0, row=2, columnspan=3, pady=(20,5), padx=5)

    current_artist_label = tb.Label(panel, text=artista, bootstyle="info", font=("Roboto", 12))
    current_artist_label.grid(column=0, row=3, columnspan=3, pady=5, padx=5)

    if not barra_progreso: # Crear la barra de progreso solo si no existe
        barra_progreso = tb.Progressbar(panel, bootstyle="success-striped", maximum=100, value=0)
        barra_progreso.grid(column=0, row=1, columnspan=3, sticky="ew", padx=10, pady=20)
    else:
        # Reiniciar el valor de la barra de progreso para la nueva canción
        barra_progreso['value'] = 0

    current_image_canvas = imagen(panel, nombre)

    return current_title_label, current_artist_label, current_image_canvas, nombre