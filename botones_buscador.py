import ttkbootstrap as tb
from pathlib import Path
from btotones_musica import cargar_vista
from abrir_directorio import nombres_canciones_guardadas, cargar_directorio, canciones_guardadas

labels_resultados = []
ruta = ""

def buscar_similitudes(buscador, panel_resultados, panel_musica):
    for label in labels_resultados:
        label.destroy()
    labels_resultados.clear()

    entrada = buscador.get().lower()
    if entrada == "":
        return

    try:
        # Usamos zip para recorrer ruta y nombre al mismo tiempo
        for ruta_completa, nombre_corto in zip(canciones_guardadas, nombres_canciones_guardadas):
            if entrada in nombre_corto.lower():
                opcion = tb.Label(panel_resultados, text=nombre_corto, bootstyle="warning", font=("Roboto", 13, "bold"), cursor="hand2")
                opcion.pack(side="top", fill="x", padx=5, pady=5)

                # El primer argumento de la lambda debe ser el evento del clic
                opcion.bind("<Button-1>", lambda e, r=ruta_completa: cargar_vista(panel_musica, r))

                labels_resultados.append(opcion)
    except Exception as error:
        print(error)

def barra_busqueda(panel, panel_musica):
    buscador = tb.Entry(panel, bootstyle="info", textvariable="text")
    buscador.pack(side="top", fill="x", padx=5, pady=5)

    buscador.bind("<KeyRelease>", lambda e: buscar_similitudes(buscador, panel, panel_musica))
    return buscador

def vista_previa(panel, panel_musica):
    if nombres_canciones_guardadas:
        for i, (ruta_completa, nombre) in enumerate(zip(canciones_guardadas, nombres_canciones_guardadas)):
            if i < 10:
                opcion = tb.Label(panel, text=nombre, bootstyle="warning", font=("Roboto", 13, "bold"), cursor="hand2")
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