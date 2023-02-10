import math
import pygame, sys, os
from classes import *
from defaults import *
from equations import *
from mapgen import *
pygame.init()

def raycast():
    for wall in walls:
        rot_x = PLAYER.rect.centerx - wall.rect.left * math.sin(angle_rad)
        rot_y = PLAYER.rect.centery - wall.rect.top * math.cos(angle_rad)
        pygame.draw.line(screen, WHITE, PLAYER.rect.center, (rot_x * 1.5, rot_y * 1.5))


display = pygame.display
display.init()
display.set_caption("Tiled Map Test")
display.set_icon(WALLSPRITE.image)
screen = display.set_mode(size)
clock = pygame.time.Clock()
pygame.font.init()

ray = rx, ry = 0,0


# RAYCAST MAP


theta = 0
debug = False
text = pygame.font.Font(os.path.join(cwd, "fonts/NotoSans.ttf"), 15)

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
        if (theta < 0):
            theta += 360
    
    if (keys[pygame.K_r]):
        genMap(GROUND, WALLSPRITE)
    
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
        pygame.draw.line(screen, BLUE, PLAYER.rect.center,
                (PLAYER.rect.centerx - 100 * math.sin(angle_rad), PLAYER.rect.centery - 100 * math.cos(angle_rad)), 5)
        raycast()
        
    pygame.display.flip()
    clock.tick(60)
        
    
