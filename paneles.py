import ttkbootstrap as tb

def panel_busqueda(root):
    panel = tb.Labelframe(root, text="Buscador", padding=15, bootstyle="secondary")
    panel.pack(side="left", fill="both", expand=True, padx=10, pady=10)
    return panel

def panel_musica(root):
    panel = tb.Labelframe(root, text="Reproductor", padding=15, bootstyle="info")
    panel.pack(side="right", fill="y", padx=10, pady=10)
    return panel

def panel_playlist(root):
    panel = tb.Labelframe(root, text="Playlist", padding=15, bootstyle="primary")
    panel.pack(side="left", fill="x", padx=10, pady=10)
    return panel