from ursina import Ursina

class MainLoop:
    def __init__(self, update_func=None):
        """
        MainLoop initializes Ursina and handles automatic frame updates.
        :param update_func: a function to call every frame (like updating player, camera, etc.)
        """
        self.app = Ursina()
        self.update_func = update_func

        # Register the update callback if provided
        if self.update_func:
            from ursina import update
            update.append(self.update_func)

    def run(self):
        """Start the game loop"""
        self.app.run()
