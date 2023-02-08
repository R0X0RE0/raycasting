import pygame, math
# GameSprite inherits the PyGame Sprite class
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, image, width=32, height=32, width_div=20, height_div=15):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.rect = pygame.Rect(x,y,32,32)
        self.rect.left = self.x * (width / width_div)
        self.rect.top = self.y * (height / height_div)