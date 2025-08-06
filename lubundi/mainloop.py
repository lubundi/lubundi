from ursina import Ursina, window, Func

class MainLoop:
    def __init__(self, update_func=None):
        self.app = Ursina()
        window.title = "Lubundi"  # Set Lubundi title
        self.update_func = update_func

        # Attach the update function via Ursina's global update
        if self.update_func:
            # Ursina calls update functions automatically every frame if they're global
            # We'll create a small Entity just to call our function every frame
            from ursina import Entity
            self.updater = Entity()
            self.updater.update = self.update_func

    def run(self):
        self.app.run()
