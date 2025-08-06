from ursina import Ursina, Entity
from panda3d.core import WindowProperties
from ursina import window, application

class MainLoop:
    def __init__(self, update_func=None):
        # Initialize Ursina app
        self.app = Ursina()

        # Force the window title via Panda3D after window is created
        if application.base.win:  # ensure Panda3D window exists
            wp = WindowProperties()
            wp.setTitle("Lubundi")
            application.base.win.requestProperties(wp)

        # Attach update function if provided
        self.update_func = update_func
        if self.update_func:
            self.updater = Entity()
            self.updater.update = self.update_func

    def run(self):
        self.app.run()
