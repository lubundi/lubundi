from ursina import Ursina, Func

class MainLoop:
    def __init__(self, update_func=None):
        """
        MainLoop initializes Ursina and handles automatic frame updates.
        :param update_func: a function to call every frame
        """
        self.app = Ursina()
        self.update_func = update_func

        # If an update function is provided, register it
        if self.update_func:
            # Ursina automatically calls 'update' functions; we can wrap it using Func
            from ursina import Entity
            class Updater(Entity):
                def update(self_inner):
                    self.update_func()
            Updater()

    def run(self):
        """Start the game loop"""
        self.app.run()
