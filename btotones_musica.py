import ttkbootstrap as tb
from funciones import *
import vlc
from cargar_imagen import imagen
from obtener_info import obtener_info
from marquesina import marquesina
import os
from abrir_directorio import canciones_guardadas
from aleatorio import *
from obtener_playlists import agregar_cancion_a_playlist, crear_nueva_playlist

reproductor = Reproductor()
cancion_anterior = None
cancion_actual = None
barra_progreso = None
current_title_label = None
current_artist_label = None
current_image_canvas = None
estado_aleatorio = False
combo_playlist = None
estado_loop = False
ale_tg = None
lo_tg = None

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

def obtener_estado(panel):
    global cancion_actual, estado_loop
    # Verificamos el estado real del reproductor VLC
    estado_vlc = reproductor.player.get_state()

    if estado_vlc == vlc.State.Ended:
        if estado_loop:
            # Si el loop está activo, reiniciamos la misma canción
            if cancion_actual:
                reproductor.reproducir(cancion_actual)
        else:
            # Si no hay loop, usamos la lógica de "siguiente" (respeta aleatorio)
            ir_siguiente(panel)

    panel.after(1000, lambda: obtener_estado(panel))

def play(panel):
    global cancion_anterior
    def reproducir_cancion():
        if cancion_actual:
            reproductor.reproducir(cancion_actual)
        actualizar_barra(panel)
    cancion_anterior = cancion_actual
    play_bt = tb.Button(panel, text="Play ", style="success.TButton",command=reproducir_cancion)
    play_bt.grid(column=3, row=4, sticky="nsew", padx=10, pady=10, ipadx=5, ipady=5)
    return play_bt

def pause(panel):
    pause_bt = tb.Button(panel, text="Pause", style="secondary.TButton", command=reproductor.pausar)
    pause_bt.grid(column=2, row=4, sticky="nsew", padx=10, pady=10, ipadx=5, ipady=5)
    return pause_bt

def stop(panel):
    frenar_bt = tb.Button(panel, text="Stop", style="primary.TButton", command=reproductor.frenar)
    frenar_bt.grid(column=1, row=4, sticky="nsew", padx=10, pady=10, ipadx=5, ipady=5)
    return frenar_bt

def ir_siguiente(panel):
    global cancion_actual, cancion_anterior

    if not canciones_guardadas:
        return

    cancion_anterior = cancion_actual
    playlist = canciones_guardadas

    if not estado_aleatorio:
        try:
            indice = playlist.index(cancion_actual)
            sig_indice = (indice + 1) % len(playlist)
        except (ValueError, TypeError):
            sig_indice = 0
        nueva_ruta = playlist[sig_indice]
    else:
        nueva_ruta = reproducir_aleatorio(cancion_actual)

    cargar_vista(panel, nueva_ruta)
    reproductor.reproducir(nueva_ruta)
    actualizar_barra(panel)

def siguiente(panel):
    # El botón ahora simplemente llama a la función global ir_siguiente
    next_bt = tb.Button(panel, text="▶▶", style="info.TButton", command=lambda: ir_siguiente(panel))
    next_bt.grid(column=4, row=4, sticky="nsew", padx=10, pady=10, ipadx=5, ipady=5)
    return next_bt

def anterior(panel):
    def ir_anterior():
        global cancion_actual, cancion_anterior
        if not canciones_guardadas: return
        else: playlist = canciones_guardadas
        if estado_aleatorio == False:
            try:
                indice = playlist.index(cancion_actual)
                nueva_ruta = playlist[(indice - 1) % len(playlist)]
            except (ValueError, TypeError):
                nueva_ruta = playlist[0]
        elif estado_aleatorio:
            if cancion_anterior and cancion_anterior != cancion_actual:
                nueva_ruta = cancion_anterior
            else:
                try:
                    indice = playlist.index(cancion_actual)
                    nueva_ruta = playlist[(indice - 1) % len(playlist)]
                except (ValueError, TypeError):
                    nueva_ruta = playlist[0]
        if nueva_ruta:
            temporal = cancion_actual 
            
            cancion_actual = nueva_ruta
            cargar_vista(panel, nueva_ruta)
            reproductor.reproducir(nueva_ruta)
            actualizar_barra(panel)
            
            cancion_anterior = temporal
    prev_bt = tb.Button(panel, text="◀◀", style="info.TButton", command=ir_anterior)
    prev_bt.grid(column=0, row=4, sticky="nsew", padx=10, pady=10, ipadx=5, ipady=5)
    return prev_bt

def aleatorio(panel):
    global ale_tg, estado_ale
    estado_ale = tb.IntVar(value=estado_aleatorio)
    def inversion():
        global cancion_actual, estado_aleatorio, estado_loop, estado_lo

        estado_aleatorio = bool(estado_ale.get())

        if estado_aleatorio:
            estado_loop = False
            if "estado_lo" in globals():
                estado_lo.set(0)
            reproducir_aleatorio(cancion_actual)
    
    color_inicial = "warning-round-toggle" 

    aleatory = tb.Checkbutton(panel, text="⥬", variable=estado_ale, bootstyle=color_inicial, command=inversion)
    aleatory.grid(column=2, row=5, sticky="nswe", padx=10, pady=10, ipadx=5, ipady=5)
    ale_tg = aleatory
    return aleatory

def loop(panel):
    global lo_tg, estado_lo
    estado_lo = tb.IntVar(value=estado_loop)
    def invertir():
        global cancion_actual, estado_aleatorio, estado_loop, estado_ale

        estado_loop = bool(estado_lo.get())

        if estado_loop:
            estado_aleatorio = False
            if "estado_ale" in globals() and estado_ale is not None:
                estado_ale.set(0) # Apaga el botón visual de aleatorio

    loop_tg = tb.Checkbutton(panel, text="↺", variable=estado_lo, bootstyle="light-round-toggle", command=invertir)
    loop_tg.grid(column=3, row=5, sticky="nswe", padx=10, pady=10, ipadx=5, ipady=5)
    lo_tg = loop_tg
    return loop_tg

def agregar_cancion(panel):
    # Función interna para capturar los valores REALES al momento de hacer clic
    def comando_agregar():
        global cancion_actual, combo_playlist
        if cancion_actual and combo_playlist:
            destino = combo_playlist.get()
            agregar_cancion_a_playlist(cancion_actual, destino)
        else:
            print("Error: No hay canción cargada o no se seleccionó playlist.")

    if not combo_playlist:
        panel.after(1000, lambda: agregar_cancion(panel))
        return None
    agregar = tb.Button(panel, text="Agregar", style="success.TButton", command=comando_agregar)
    agregar.grid(column=0, row=6, sticky="nsew", padx=10, pady=10, ipadx=5, ipady=5)
    return agregar

def cargar_vista(panel, nombre="default"):
    global barra_progreso, cancion_actual, current_title_label, current_artist_label, current_image_canvas

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

    if titulo.lower().endswith(".mp3"):
        titulo = os.path.splitext(titulo)[0] 

    current_title_label = tb.Label(panel, text=titulo, bootstyle="light", font=("Roboto", 16, "bold"))
    marquesina(current_title_label, titulo)
    current_title_label.grid(column=0, row=2, columnspan=5, pady=(20,5), padx=5)

    current_artist_label = tb.Label(panel, text=artista, bootstyle="info", font=("Roboto", 12))
    current_artist_label.grid(column=0, row=3, columnspan=5, pady=5, padx=5)

    if not barra_progreso: # Crear la barra de progreso solo si no existe
        barra_progreso = tb.Progressbar(panel, bootstyle="success-striped", maximum=100, value=0)
        barra_progreso.grid(column=0, row=1, columnspan=5, sticky="ew", padx=10, pady=20)
    else:
        # Reiniciar el valor de la barra de progreso para la nueva canción
        barra_progreso['value'] = 0

    current_image_canvas = imagen(panel, nombre)

    return current_title_label, current_artist_label, current_image_canvas, nombre