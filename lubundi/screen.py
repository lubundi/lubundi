from ursina import Entity, Text, color

class Screen(Entity):
    def __init__(self, text='', color_bg=color.black, **kwargs):
        super().__init__()
        self.bg = Entity(parent=self, model='quad', scale=(100, 100), color=color_bg)
        self.text = Text(text=text, origin=(0, 0), scale=2, color=color.white, parent=self)

    def show(self):
        self.enabled = True

    def hide(self):
        self.enabled = False
