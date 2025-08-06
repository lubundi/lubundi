from ursina import Ursina, window, Entity

class MainLoop:
    def __init__(self, update_func=None):
        # Initialize Ursina app
        self.app = Ursina()
        
        # Force the window title to "Lubundi"
        window.title = "Lubundi"

        # Attach update function if provided
        self.update_func = update_func
        if self.update_func:
            # Dummy entity whose update method calls the function every frame
            self.updater = Entity()
            self.updater.update = self.update_func

    def run(self):
        self.app.run()
