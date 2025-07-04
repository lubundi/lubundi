from ursina import Entity, color

class Player(Entity):
    def __init__(self, texture=None, **kwargs):
        super().__init__()
        self.texture = texture
        self.color = color.gray if texture is None else color.white
        self.model = 'quad'
        self.scale = (1, 1)
        if texture:
            self.texture = texture
        else:
            self.texture = None

    def update(self):
        # Simple movement example
        if self.input('left arrow'):
            self.x -= 0.1
        if self.input('right arrow'):
            self.x += 0.1
        if self.input('up arrow'):
            self.y += 0.1
        if self.input('down arrow'):
            self.y -= 0.1

    def input(self, key):
        from ursina import held_keys
        return held_keys.get(key, False)
