from classes import *
import os

cwd = os.getcwd()
size = width, height = 640,480

# COLORS
BLACK = 12,15,28
SKYBLUE = 200,228,255
RED = 247,12,52
WHITE = 244,233,255
BLUE = 34,28,200

# TEXTURES
ROCKS = "assets/rocks.png"
BRICKS = "assets/bricks.png"
MARKER = "assets/player.png"

TILE_SIZE = 32
MAP_SIZE = 12
FOV = math.pi / 4
HALF_FOV = FOV / 2
CASTED_RAYS = 120
MAX_DEPTH = 16
ROT_VALUE = 5
NONZERO = 0.1

DEF_IMG_SIZE = (96,96)

# OBJECTS

# SPRITE CLASS
WALLSPRITE = GameSprite(0,0,os.path.join(cwd, BRICKS), TILE_SIZE)
PLAYERSPRITE = GameSprite(1,1,os.path.join(cwd,MARKER), TILE_SIZE)
GROUND = GameSprite(0,0,os.path.join(cwd, ROCKS), TILE_SIZE)


PLAYER = Player(PLAYERSPRITE, 5)
