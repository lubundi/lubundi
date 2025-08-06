from ursina import camera, mouse, Vec3, held_keys

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

    def update(self):
        if self.mode == 'FocusOnPlayer' and self.player:
            # Follow the player smoothly
            camera.position = self.player.position + Vec3(0, 5, -10)
            camera.look_at(self.player.position)

        elif self.mode == 'CameraIsMovable':
            if mouse.left:
                if not self.dragging:
                    self.dragging = True
                    self.drag_origin = mouse.position
                else:
                    dx = (mouse.position[0] - self.drag_origin[0]) * self.sensitivity * 100
                    dy = (mouse.position[1] - self.drag_origin[1]) * self.sensitivity * 100

                    camera.rotation_y -= dx
                    camera.rotation_x += dy
                    self.drag_origin = mouse.position
            else:
                self.dragging = False

        else:
            # Default fixed position
            camera.position = Vec3(0, 5, -10)
            camera.rotation = Vec3(20, 0, 0)

