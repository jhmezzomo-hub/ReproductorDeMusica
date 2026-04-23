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

    def set_volumen(self, volumen):
        self.player.audio_set_volume(int(volumen))

    def cancion_sig_o_loop(self, cancion_actual, estado_loop, cancion_siguiente=None):
        if not cancion_actual:
            return
        estado_vlc = self.player.get_state()
        if estado_vlc == vlc.State.Ended and estado_loop:
            self.reproducir(cancion_actual)
        elif estado_vlc == vlc.State.Ended:
            self.reproducir(cancion_siguiente)