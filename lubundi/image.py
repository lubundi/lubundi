from ursina import Entity

class Image(Entity):
    def __init__(self, texture, **kwargs):
        super().__init__()
        self.model = 'quad'
        self.texture = texture
