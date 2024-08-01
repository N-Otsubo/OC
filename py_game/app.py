import pygame
from pygame.locals import *

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("ブロック崩し")


class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, 20))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 20
        self.speed = 10

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= self.speed
        if keys[K_RIGHT]:
            self.rect.x += self.speed
        self.rect.clamp_ip(screen.get_rect())


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((15, 15))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
        self.speed = [3, 3]

    def update(self):
        self.rect.move_ip(self.speed)
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0:
            self.speed[1] = -self.speed[1]
        if self.rect.top > SCREEN_HEIGHT:
            game_over()

    def increase_speed(self):
        self.speed[0] += 0.5
        self.speed[1] += 0.5


# ゲームオーバー時の処理
def game_over():
    font = pygame.font.Font(None, 74)
    text = font.render("Game Over", True, (255, 0, 0))
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    exit()


class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((100, 40))
        self.image.fill((100, 100, 100))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        # ボールが画面下に行った場合はゲームオーバー


blocks = pygame.sprite.Group()
for row in range(5):
    for col in range(8):
        block = Block(col * 100, row * 40)
        blocks.add(block)

paddle = Paddle()
ball = Ball()

clock = pygame.time.Clock()
running = True


# 全てのブロックを削除する関数
def remove_all_blocks():
    blocks.empty()


while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                remove_all_blocks()

    paddle.update()
    ball.update()

    if pygame.sprite.collide_rect(ball, paddle):
        ball.speed[1] = -ball.speed[1]

    collided_blocks = pygame.sprite.spritecollide(ball, blocks, True)
    if collided_blocks:
        ball.speed[1] = -ball.speed[1]
        ball.increase_speed()

    blocks.draw(screen)
    screen.blit(paddle.image, paddle.rect)
    screen.blit(ball.image, ball.rect)

    if len(blocks) == 0:
        font = pygame.font.Font(None, 74)
        text = font.render("Clear!", True, (0, 0, 0))
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
