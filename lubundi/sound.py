from ursina import Audio

class SoundPlayer:
    def __init__(self, file_path, loop=False, autoplay=False):
        self.audio = Audio(file_path, loop=loop, autoplay=autoplay)

    def play(self):
        self.audio.play()

    def stop(self):
        self.audio.stop()

    def pause(self):
        self.audio.pause()

    def resume(self):
        self.audio.resume()
