import ttkbootstrap as tb
from pathlib import Path
from btotones_musica import cargar_vista, alternar_modo_compacto
from abrir_directorio import nombres_canciones_guardadas, cargar_directorio, canciones_guardadas

labels_resultados = []
ruta = ""
expandido = False # Variable de estado para el nombre completo

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
        # Usamos zip para recorrer ruta y nombre al mismo tiempo
        for ruta_completa, nombre_corto in zip(canciones_guardadas, nombres_canciones_guardadas):
            if entrada in nombre_corto.lower():
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
    if nombres_canciones_guardadas:
        for i, (ruta_completa, nombre) in enumerate(zip(canciones_guardadas, nombres_canciones_guardadas)):
            if i < 10:
                # En vista previa usualmente no está enfocado, usamos el corte
                nombre_mostrar = (nombre[:35] + '..') if len(nombre) > 37 else nombre
                opcion = tb.Label(panel, text=nombre_mostrar, bootstyle="warning", font=("Roboto", 13, "bold"), cursor="hand2")
                opcion.pack(side="top", fill="x", padx=5, pady=5)
                opcion.bind("<Button-1>", lambda e, r=ruta_completa: cargar_vista(panel_musica, r))
            else:
                break
    else:
        def recargar():
            if cargar_directorio():
                for widget in panel.winfo_children():
                    if not isinstance(widget, tb.Entry):
                        widget.destroy()
                vista_previa(panel, panel_musica)

        mostrar = tb.Label(panel, text="No hay ninguna cancion cargada en este momento", bootstyle="danger", font=("Roboto", 25, "bold", "underline"), justify="center")
        mostrar.pack(side="top", fill="x", padx=30, pady=(200,20))

        abrir = tb.Button(panel, text="Abrir directorio", style="primary.TButton", command=recargar)
        abrir.pack(side="top", pady=5, padx=5 , ipadx=15, ipady=15)