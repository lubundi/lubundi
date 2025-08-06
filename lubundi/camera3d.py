from ursina import camera, mouse, Vec3
from ursina.prefabs.editor_camera import EditorCamera  # Editor-style free camera

class Camera3D:
    def __init__(self, player=None, mode='Default', sensitivity=0.2):
        self.player = player
        self.mode = mode
        self.sensitivity = sensitivity
        self.dragging = False
        self.drag_origin = None

        # Camera starts at a reasonable position
        camera.position = Vec3(0, 5, -10)
        camera.rotation = Vec3(20, 0, 0)  # Slightly looking down

        self.editor_camera = None
        if self.mode == 'CameraIsMovable':
            self.activate_editor_camera()

    def activate_editor_camera(self):
        """Enable free movement camera like Lubundi editor"""
        if not self.editor_camera:
            self.editor_camera = EditorCamera()
            self.editor_camera.position = camera.position
            self.editor_camera.rotation = camera.rotation

    def update(self):
        if self.mode == 'FocusOnPlayer' and self.player:
            # Follow the player smoothly
            camera.position = self.player.position + Vec3(0, 5, -10)
            camera.look_at(self.player.position)

        elif self.mode == 'CameraIsMovable':
            # Make sure editor camera is active
            if not self.editor_camera:
                self.activate_editor_camera()
            # EditorCamera handles movement and mouse look automatically

        else:
            # Default fixed position
            camera.position = Vec3(0, 5, -10)
            camera.rotation = Vec3(20, 0, 0)
