from ursina import Ursina, Entity, color, held_keys
from lubundi.player import Player
from lubundi.camera import Camera2D
from lubundi.screen import Screen

app = Ursina()

CAMERA_MODE = 'FocusOnPlayer'

# Sky background
sky = Entity(model='quad', texture='sky.png', scale=(40, 20), z=10)

# Platforms
platforms = []
for i in range(10):
    platform = Entity(model='quad', color=color.azure, scale=(3, 0.5), position=(i * 4, 0), collider='box')
    platforms.append(platform)

# Invisible death zone
death_zone = Entity(model='quad', collider='box', position=(0, -5), scale=(100, 1), visible=False)

# Player with texture
player = Player(texture='player.png')
player.y = 1
player.collider = 'box'

# Camera
cam = Camera2D(player=player, mode=CAMERA_MODE)

# Game over screen
game_over_screen = Screen(text="Game Over! Press R to Restart", color_bg=color.black)
game_over_screen.hide()

gravity = -0.03
velocity_y = 0
on_ground = False

def update():
    global velocity_y, on_ground

    cam.update()

    dx = 0
    if player.input('left arrow'):
        dx -= 0.1
    if player.input('right arrow'):
        dx += 0.1

    # Predict horizontal movement
    player.x += dx
    collision = False
    for p in platforms:
        if player.intersects(p).hit:
            collision = True
            break
    if collision:
        # Undo move, player stops at obstacle without snapping back
        player.x -= dx

    # Gravity and vertical movement
    velocity_y += gravity
    player.y += velocity_y
    on_ground = False

    for p in platforms:
        if player.intersects(p).hit:
            if velocity_y < 0:
                player.y = p.y + p.scale_y/2 + player.scale_y/2
                velocity_y = 0
                on_ground = True
            elif velocity_y > 0:
                player.y = p.y - p.scale_y/2 - player.scale_y/2
                velocity_y = 0

    # Jump
    if player.input('space') and on_ground:
        velocity_y = 0.45

    # Game Over check
    if player.y < -4:
        game_over_screen.show()

    # Restart game
    if game_over_screen.enabled and player.input('r'):
        player.position = (0, 1)
        velocity_y = 0
        game_over_screen.hide()


app.run()

