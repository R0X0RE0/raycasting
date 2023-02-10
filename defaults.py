from classes import *
import os

cwd = os.getcwd()
size = width, height = 640,480

WIDTH_DIV = 20
HEIGHT_DIV = 15

# COLORS
BLACK = 12,15,28
SKYBLUE = 200,228,255
RED = 237,12,92
WHITE = 222,200,255
BLUE = 34,28,200

# TEXTURES
ROCKS = "assets/rocks.png"
BRICKS = "assets/bricks.png"
MARKER = "assets/player.png"

FOV = math.pi / 3
HALF_FOV = FOV / 2
CASTED_RAYS = 10
MAX_DEPTH = 10

DEF_IMG_SIZE = (96,96)

# OBJECTS

# SPRITE CLASS
WALLSPRITE = GameSprite(0,0,os.path.join(cwd, BRICKS))
PLAYERSPRITE = GameSprite(1,1,os.path.join(cwd,MARKER), width, height, WIDTH_DIV, HEIGHT_DIV)
GROUND = GameSprite(0,0,os.path.join(cwd, ROCKS))


PLAYER = Player(PLAYERSPRITE, 5)
