from ursina import Ursina, window

class MainLoop:
    def __init__(self, update_func=None):
        # Initialize Ursina app
        self.app = Ursina()

        # Change window title to "Lubundi"
        window.title = "Lubundi"

        # Store optional update callback
        self.update_func = update_func
        if self.update_func:
            from ursina import update
            update.append(self.update_func)

    def run(self):
        # Start game loop
        self.app.run()
