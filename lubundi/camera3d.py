from ursina import Entity, mouse, Vec3

class Camera3D(Entity):
    def __init__(self, player=None, mode='Default', sensitivity=0.1, **kwargs):
        super().__init__()
        self.player = player
        self.mode = mode
        self.sensitivity = sensitivity  # Mouse drag sensitivity
        self.dragging = False
        self.drag_origin = None
        self.position = Vec3(0, 0, 0)
        self.rotation = Vec3(0, 0, 0)  # pitch, yaw, roll

    def update(self):
        if self.mode == 'FocusOnPlayer' and self.player:
            # Follow player position exactly
            self.position = Vec3(self.player.x, self.player.y, self.player.z)

        elif self.mode == 'CameraIsMovable':
            if mouse.left:
                if not self.dragging:
                    self.dragging = True
                    self.drag_origin = mouse.position
                else:
                    dx = (mouse.position[0] - self.drag_origin[0]) * self.sensitivity * 100
                    dy = (mouse.position[1] - self.drag_origin[1]) * self.sensitivity * 100

                    # Rotate camera based on mouse movement
                    self.rotation.y -= dx
                    self.rotation.x += dy
                    self.drag_origin = mouse.position
            else:
                self.dragging = False

        else:
            # Default: fixed camera at origin
            self.position = Vec3(0, 0, 0)
            self.rotation = Vec3(0, 0, 0)
