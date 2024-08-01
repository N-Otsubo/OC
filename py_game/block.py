import pygame
from constans import *


class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface(BLOCK_SIZE)
        self.image.fill(BLOCK_COLOR)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
