import pygame, math, random
# GameSprite inherits the PyGame Sprite class
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, image, tile_size):
        pygame.sprite.Sprite.__init__(self)
        self.tile_size = tile_size
        self.x = x * tile_size
        self.y = y * tile_size
        self.image = pygame.image.load(image)
        self.rect = pygame.Rect(self.x,self.y,32,32)
        

# OBJECT CLASSES
# Block is the class that will be raycasted as walls.
# Block inherits the user-defined class GameSprite
class Block(GameSprite):
    def __init__(self, sprite:GameSprite, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = sprite
        self.image = self.sprite.image
        self.rect = pygame.Rect(x,y,32,32)
        walls.append(self)

# Floor is the class that will be raycasted as floor.
# Floor inherits the user-defined class GameSprite
class Floor(GameSprite):
    def __init__(self, sprite:GameSprite, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = sprite
        self.image = self.sprite.image
        self.rect = pygame.Rect(x,y,32,32)
        grounds.append(self)


# Player inherits the user-defined class GameSprite
class Player(GameSprite):
    def __init__(self, sprite:GameSprite, speed):
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
grounds = []
walls = []