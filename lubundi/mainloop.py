import platform
import sys
from ursina import Ursina, Entity, application

from panda3d.core import WindowProperties

class MainLoop:
    def __init__(self, update_func=None):
        # Initialize Ursina app
        self.app = Ursina()

        # Build dynamic title
        os_info = platform.system() + " " + platform.release()
        python_info = f"Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
        title = f"Lubundi on {os_info} and {python_info}"

        # Force the window title via Panda3D
        if application.base.win:
            wp = WindowProperties()
            wp.setTitle(title)
            application.base.win.requestProperties(wp)

        # Attach update function if provided
        self.update_func = update_func
        if self.update_func:
            self.updater = Entity()
            self.updater.update = self.update_func

    def run(self):
        self.app.run()
