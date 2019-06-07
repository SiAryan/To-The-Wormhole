import pygame

class Player(pygame.sprite.Sprite):
    color = (0, 0, 0)
    width = 20
    height = 20

    def __init__(self, color, width, height):
       pygame.sprite.Sprite.__init__(self)

       self.image = pygame.Surface([width, height])
       self.image.fill(color)

       self.rect = self.image.get_rect()
