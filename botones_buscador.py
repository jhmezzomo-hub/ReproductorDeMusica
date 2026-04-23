import ttkbootstrap as tb
from pathlib import Path
from btotones_musica import cargar_vista, alternar_modo_compacto
from abrir_directorio import nombres_canciones_guardadas, cargar_directorio, canciones_guardadas
from obtener_playlists import playlist, nombre_playlist, abrir_playlist

labels_resultados = []
ruta = ""
expandido = False 

def buscar_similitudes(buscador, panel_resultados, panel_musica):
    for label in panel_resultados.winfo_children():
        if not isinstance(label, tb.Entry):
            label.destroy()
    labels_resultados.clear()

    entrada = buscador.get().lower()
    if entrada == "":
        vista_previa(panel_resultados, panel_musica)
        return

    try:
        import btotones_musica
        # Obtenemos la playlist seleccionada y sus canciones desde el JSON
        seleccionada = btotones_musica.combo_playlist.get() if btotones_musica.combo_playlist else "original"
        canciones_permitidas = playlist.get(seleccionada, [])

        # Usamos zip para recorrer ruta y nombre al mismo tiempo
        for ruta_completa, nombre_corto in zip(canciones_guardadas, nombres_canciones_guardadas):
            # FILTRO: El nombre debe estar en la entrada del buscador Y en la playlist del JSON
            if entrada in nombre_corto.lower() and nombre_corto in canciones_permitidas:
                # Si está expandido mostramos todo, si no, cortamos
                if expandido:
                    nombre_mostrar = nombre_corto
                else:
                    nombre_mostrar = (nombre_corto[:35] + '..') if len(nombre_corto) > 37 else nombre_corto
                
                opcion = tb.Label(panel_resultados, text=nombre_mostrar, bootstyle="warning", font=("Roboto", 13, "bold"), cursor="hand2")
                opcion.pack(side="top", fill="x", padx=5, pady=5)

                # El primer argumento de la lambda debe ser el evento del clic
                opcion.bind("<Button-1>", lambda e, r=ruta_completa: cargar_vista(panel_musica, r))

                labels_resultados.append(opcion)
    except Exception as error:
        print(error)

def manejar_foco(event, buscador, panel, panel_musica, estado):
    global expandido
    expandido = estado
    alternar_modo_compacto(estado) # True achica el reproductor, False lo agranda
    buscar_similitudes(buscador, panel, panel_musica)

def barra_busqueda(panel, panel_musica):
    buscador = tb.Entry(panel, bootstyle="info", textvariable="text")
    buscador.pack(side="top", fill="x", padx=5, pady=5)

    buscador.bind("<KeyRelease>", lambda e: buscar_similitudes(buscador, panel, panel_musica))
    
    # Eventos de foco para expandir/contraer
    buscador.bind("<FocusIn>", lambda e: manejar_foco(e, buscador, panel, panel_musica, True))
    # Usamos after para dar tiempo a que el clic en la canción se procese antes de contraer
    buscador.bind("<FocusOut>", lambda e: panel.after(200, lambda: manejar_foco(None, buscador, panel, panel_musica, False)))
    
    return buscador

def vista_previa(panel, panel_musica):
    # Limpiamos el panel para que no se dupliquen las canciones al cambiar de playlist
    for widget in panel.winfo_children():
        if not isinstance(widget, tb.Entry):
            widget.destroy()

    if nombres_canciones_guardadas:
        import btotones_musica
        seleccionada = btotones_musica.combo_playlist.get() if btotones_musica.combo_playlist else "original"
        canciones_permitidas = playlist.get(seleccionada, [])
        
        contador = 0
        for i, (ruta_completa, nombre) in enumerate(zip(canciones_guardadas, nombres_canciones_guardadas)):
            # En vista previa usamos el nombre recortado
            if nombre in canciones_permitidas:
                if contador >= 10: break

                nombre_mostrar = (nombre[:35] + '..') if len(nombre) > 37 else nombre
                opcion = tb.Label(panel, text=nombre_mostrar, bootstyle="warning", font=("Roboto", 13, "bold"), cursor="hand2")
                opcion.pack(side="top", fill="x", padx=5, pady=5)
                
                # Vinculamos el clic para que la canción se cargue y reproduzca
                opcion.bind("<Button-1>", lambda e, r=ruta_completa: cargar_vista(panel_musica, r))
                contador += 1
    else:
        def recargar():
            from abrir_directorio import cargar_playlist_original
            if cargar_directorio():
                cargar_playlist_original()
                abrir_playlist()
                
                import btotones_musica
                if btotones_musica.combo_playlist:
                    btotones_musica.combo_playlist['values'] = nombre_playlist
                vista_previa(panel, panel_musica)

        mostrar = tb.Label(panel, text="No hay ninguna cancion cargada en este momento", bootstyle="danger", font=("Roboto", 25, "bold", "underline"), justify="center")
        mostrar.pack(side="top", fill="x", padx=30, pady=(200,20))

        abrir = tb.Button(panel, text="Abrir directorio", style="primary.TButton", command=recargar)
        abrir.pack(side="top", pady=5, padx=5 , ipadx=15, ipady=15)

def opcion_playlist(panel, buscador_panel):
    import btotones_musica
    global lista_desplegable

    if not canciones_guardadas:
        panel.after(1000, lambda: opcion_playlist(panel, buscador_panel))
        return None

    if btotones_musica.combo_playlist is not None:
        return btotones_musica.combo_playlist

    lista_desplegable = tb.Combobox(panel, values=nombre_playlist, bootstyle="dark", state="readonly")
    lista_desplegable.grid(column=0, row=5, columnspan=2, sticky="nsew", padx=10, pady=10)
    
    if nombre_playlist:
        lista_desplegable.current(0)

    btotones_musica.combo_playlist = lista_desplegable
    lista_desplegable.bind("<<ComboboxSelected>>", lambda e: vista_previa(buscador_panel, panel))
    return lista_desplegable