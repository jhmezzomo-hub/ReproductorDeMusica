# SpotiMezzo 🎵

**SpotiMezzo** es un reproductor de música moderno desarrollado en Python utilizando `tkinter` y `ttkbootstrap` para una interfaz visual atractiva con el tema *Vapor*. Utiliza el motor de VLC para una reproducción de audio fluida y robusta.

## ✨ Características

- **Gestión de Playlists:** Crea tus propias listas de reproducción y agrega canciones desde tus directorios locales. Las listas se guardan automáticamente en un archivo JSON.
- **Buscador Inteligente:** Filtra canciones por nombre dentro de la playlist seleccionada.
- **Controles Completos:** Reproducir, pausar, detener, siguiente, anterior, modo aleatorio (shuffle) y repetición (loop).
- **Control de Volumen:** Ajuste preciso mediante un Spinbox integrado.
- **Interfaz Dinámica:** La marquesina muestra el nombre de la canción y se ajusta automáticamente.
- **Metadatos:** Visualización de carátulas de álbumes y nombres de artistas usando `mutagen`.

## 📋 Requisitos Previos

Antes de ejecutar el proyecto, asegúrate de tener instalado:

1. **Python 3.x**
2. **VLC Media Player:** Es indispensable tener instalado el reproductor VLC en tu sistema operativo, ya que el programa utiliza sus librerías para procesar el audio.

## 🚀 Instalación

1. Clona este repositorio o descarga los archivos.
2. Instala las dependencias necesarias mediante `pip`:

```bash
pip install ttkbootstrap python-vlc mutagen Pillow
```

## 🎮 Uso

Para iniciar el reproductor, simplemente ejecuta el archivo principal:

```bash
python main.py
```

1. Haz clic en **Abrir Directorio** para seleccionar la carpeta donde tienes tus archivos MP3.
2. Selecciona una canción de la lista de la izquierda para comenzar la reproducción.
3. Usa el botón **Crear** para generar una nueva playlist y el botón **Agregar** para incluir la canción actual en la lista seleccionada en el buscador.

## 📁 Estructura del Proyecto

- `main.py`: Punto de entrada de la aplicación.
- `btotones_musica.py`: Lógica de la interfaz del reproductor y controles.
- `obtener_playlists.py`: Manejo y persistencia de las listas de reproducción en JSON.
- `funciones.py`: Clase envolvente para las funciones del motor VLC.
- `abrir_directorio.py`: Manejo del sistema de archivos y limpieza de nombres.
- `botones_buscador.py`: Lógica del buscador y filtrado de temas.
- `playlist.json`: Archivo donde se guardan tus configuraciones y listas.

---
Desarrollado con ❤️ en Python.