import math
import pygame, sys, os
import equations as eq
import parents
pygame.init()

cwd = os.getcwd()


size = width, height = 640,480

WIDTH_DIV = 20
HEIGHT_DIV = 15

# OBJECT CLASSES
# Block is the class that will be raycasted as walls.
# Block inherits the user-defined class GameSprite
class Block(parents.GameSprite):
    def __init__(self, sprite:parents.GameSprite, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = sprite
        self.image = self.sprite.image
        self.rect = pygame.Rect(x,y,32,32)
        walls.append(self)

# Floor is the class that will be raycasted as floor.
# Floor inherits the user-defined class GameSprite
class Floor(parents.GameSprite):
    def __init__(self, sprite:parents.GameSprite, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = sprite
        self.image = self.sprite.image
        self.rect = pygame.Rect(x,y,32,32)
        grounds.append(self)


# Player inherits the user-defined class GameSprite
class Player(parents.GameSprite):
    def __init__(self, sprite:parents.GameSprite, speed):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = sprite
        self.originSpeed = speed
        self.speed = speed
        self.image = self.sprite.image
        self.rect = self.sprite.rect
        self.angle = 0
        self.dx = 0
        self.dy = 0

    def move(self, speed):
        angle_rad = self.angle * math.pi / 180
        self.dx = speed * math.sin(angle_rad)
        self.dy = speed * math.cos(angle_rad)
        self.rect.x -= self.dx
        self.rect.y -= self.dy
            
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if (self.rect.y < wall.rect.y) and self.dy < 0:
                    self.rect.bottom = wall.rect.top
                if (self.rect.y > wall.rect.y) and self.dy > 0:
                    self.rect.top = wall.rect.bottom
                if (self.rect.x < wall.rect.x) and self.dx < 0 and self.speed > 0:
                    self.rect.right = wall.rect.left
                if (self.rect.x > wall.rect.x) and self.dx > 0 and self.speed > 0:
                    self.rect.left = wall.rect.right
                
    
    def rotate(self, image, angle):
        self.angle = angle
        image_clean = pygame.image.load(image).copy()
        self.image = pygame.transform.rotate(image_clean, angle)
        old_center = self.rect.center
        self.rect = image_clean.get_rect(center = old_center)


        
    

# COLORS
BLACK = 12,15,28
SKYBLUE = 200,228,255
RED = 255,0,0
WHITE = 255,255,255

# TEXTURES
DIRT = "assets/ground.png"
WALL1 = "assets/boundary.png"
WALL2 = "assets/wall.png"
ROCKS = "assets/rocks.png"
BRICKS = "assets/bricks.png"
MARKER = "assets/player.png"


DEF_IMG_SIZE = (96,96)

# OBJECTS

# SPRITE CLASS
WALLSPRITE = parents.GameSprite(0,0,os.path.join(cwd, BRICKS))
PLAYERSPRITE = parents.GameSprite(1,1,os.path.join(cwd,MARKER), width, height, WIDTH_DIV, HEIGHT_DIV)
GROUND = parents.GameSprite(0,0,os.path.join(cwd, ROCKS))


PLAYER = Player(PLAYERSPRITE, 5)


# RAYCAST MAP
map1 = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,1,1,1,1,1,1,1,1,1,0,0,1,1,1,0,0,1],
    [1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,0,0,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]
grounds = []
walls = []

display = pygame.display
display.init()
display.set_caption("Tiled Map Test")
display.set_icon(WALLSPRITE.image)
screen = display.set_mode(size)

clock = pygame.time.Clock()
pygame.font.init()
x = y= 0
for i in range(len(map1)):
        for j in range(len(map1[i])):
            if map1[i][j] == 0:
                Floor(GROUND, x, y)
            elif map1[i][j] == 1:
                Block(WALLSPRITE, x, y)
            x += 32
        y += 32
        x = 0

theta = 0
ROT_VALUE = 5
debug = False
text = pygame.font.Font(os.path.join(cwd, "assets/NotoSans.ttf"), 15)

while True:
    angle_rad = theta * math.pi / 180
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    mods = pygame.key.get_mods()
    #fill(COLOR)
    screen.fill(SKYBLUE)
    
    if (keys[pygame.K_ESCAPE]):
        sys.exit()

    #blit(TEXTURE, OBJECT)
    
    for ground in grounds:
        screen.blit(ground.image, ground.rect)
    for wall in walls:
        screen.blit(wall.image, wall.rect)
    
    # Move Player
    # Forwards
    if (keys[pygame.K_w]):
        PLAYER.move(PLAYER.speed)
    
    # Backwards
    if (keys[pygame.K_s]):
        PLAYER.move(-PLAYER.speed)

    # Rotate Player
    # Left
    if (keys[pygame.K_a]):
        PLAYER.rotate(os.path.join(cwd, MARKER), theta)
        theta += ROT_VALUE
        if (theta > 360):
            theta -= 360

    # Right
    if (keys[pygame.K_d]):
        PLAYER.rotate(os.path.join(cwd, MARKER), theta)
        theta -= ROT_VALUE
        if (theta < -360):
            theta += 360
    
    # Debug Shortcut : Shift D
    if (mods and pygame.KMOD_SHIFT and keys[pygame.K_d]):
        pygame.time.delay(250)
        if debug is True:
            debug = False
        elif debug is False:
            debug = True
    
    screen.blit(PLAYER.image, PLAYER.rect)
    if debug is True:
        screen.blit(text.render("Debug Mode is ON", False, WHITE, BLACK), (0,0))
        pygame.draw.rect(screen, RED, PLAYER.rect, 1)
        pygame.draw.line(screen, WHITE, PLAYER.rect.center, 
        (PLAYER.rect.centerx - 20 * math.sin(angle_rad), PLAYER.rect.centery - 20 * math.cos(angle_rad)))

    
    pygame.display.flip()
    clock.tick(60)
        
    