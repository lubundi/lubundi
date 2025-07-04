from ursina import Entity

class CustomAction(Entity):
    def __init__(self, action_func, **kwargs):
        super().__init__()
        self.action_func = action_func

    def update(self):
        if self.action_func:
            self.action_func()
