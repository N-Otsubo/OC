import pygame
from pygame.locals import *
from constans import *


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface(BALL_SIZE)
        self.image.fill(BALL_COLOR)
        self.rect = self.image.get_rect()
        self.rect.center = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
        self.speed = [BALL_SPEED, BALL_SPEED]

    def update(self):
        self.rect.move_ip(self.speed)
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0:
            self.speed[1] = -self.speed[1]

    def increase_speed(self):
        self.speed[0] += 0.5
        self.speed[1] += 0.5
