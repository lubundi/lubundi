from ursina import Entity, mouse

class Camera2D(Entity):
    def __init__(self, player=None, mode='Default', **kwargs):
        super().__init__()
        self.player = player
        self.mode = mode
        self.dragging = False
        self.drag_origin = None
        self.position = (0, 0)

    def update(self):
        if self.mode == 'FocusOnPlayer' and self.player:
            # Follow player position exactly, no clamping
            self.position = (self.player.x, self.player.y)

        elif self.mode == 'CameraIsMovable':
            if mouse.left:
                if not self.dragging:
                    self.dragging = True
                    self.drag_origin = mouse.position
                else:
                    dx = mouse.position[0] - self.drag_origin[0]
                    dy = mouse.position[1] - self.drag_origin[1]
                    self.position = (self.position[0] - dx, self.position[1] - dy)
                    self.drag_origin = mouse.position
            else:
                self.dragging = False

        else:
            # Default: fixed camera at origin
            self.position = (0, 0)
