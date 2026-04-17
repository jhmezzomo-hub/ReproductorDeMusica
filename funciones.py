import vlc

class Reproductor:
    def __init__(self):
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()

    def reproducir(self, ruta):
        media = self.instance.media_new(ruta)
        self.player.set_media(media)
        self.player.play()

    def pausar(self):
        self.player.pause()
        if self.player.is_playing():
            print("Reproduciendo")
        else:
            print("Pausado")

    def frenar(self):
        self.player.stop()
        print("Detenido")

    def obtener_posicion(self):
        return self.player.get_position()