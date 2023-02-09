import math
import pygame, sys, os
from classes import *
from defaults import *
from equations import *
pygame.init()

def raycast():
    for wall in walls:
        rot_pos = rot_x, rot_y = PLAYER.rect.centerx - math.dist(PLAYER.rect.center, wall.rect.center) * math.sin(angle_rad), PLAYER.rect.centery - math.dist(PLAYER.rect.center, wall.rect.center) * math.cos(angle_rad)
        pygame.draw.line(screen, WHITE, PLAYER.rect.center, (rot_x * 1.5, rot_y * 1.5))


display = pygame.display
display.init()
display.set_caption("Tiled Map Test")
display.set_icon(WALLSPRITE.image)
screen = display.set_mode(size)

clock = pygame.time.Clock()
pygame.font.init()
x = y= 0
ray = rx, ry = 0,0

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
        print(theta)
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
        raycast()
        
    pygame.display.flip()
    clock.tick(60)
        
    