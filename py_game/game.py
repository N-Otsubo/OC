import pygame
from pygame.locals import *
from paddle import Paddle
from ball import Ball
from block import Block
from constans import *


class BreakoutGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("ブロック崩し")

        self.clock = pygame.time.Clock()
        self.running = True
        self.game_active = False

        self.font = pygame.font.Font(None, 74)

        self.blocks = pygame.sprite.Group()
        self.paddle = Paddle()
        self.ball = Ball()

    def initialize(self):
        self.blocks.empty()
        for row in range(5):
            for col in range(8):
                block = Block(col * 100, row * 40)
                self.blocks.add(block)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.game_active = True
                    self.initialize()
                elif event.key == pygame.K_r:
                    self.remove_all_blocks()

    def draw(self):
        self.screen.fill(SCREEN_COLOR)
        if not self.game_active:
            self.game_start()
        else:
            self.blocks.draw(self.screen)
            self.screen.blit(self.paddle.image, self.paddle.rect)
            self.screen.blit(self.ball.image, self.ball.rect)

    # アップデート関数
    def update(self):
        if self.game_active:
            self.paddle.update(self.screen)
            self.ball.update()

            if self.ball.rect.top > SCREEN_HEIGHT:
                self.running = self.game_over()

            if pygame.sprite.collide_rect(self.ball, self.paddle):
                self.ball.speed[1] = -self.ball.speed[1]

            collided_blocks = pygame.sprite.spritecollide(self.ball, self.blocks, True)
            if collided_blocks:
                self.ball.speed[1] = -self.ball.speed[1]

            self.game_clear()

    # ゲームスタート待機
    def game_start(self):
        text = self.font.render("Press enter to start", True, (0, 0, 0))
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()

    # ゲームクリアー時の処理
    def game_clear(self):
        if len(self.blocks) == 0:
            text = self.font.render("Clear!", True, (0, 0, 0))
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            self.screen.blit(text, text_rect)
            pygame.display.flip()
            pygame.time.wait(2000)
            self.running = False

    # ゲームオーバー時の処理
    def game_over(self):
        text = self.font.render("Game Over", True, (255, 0, 0))
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(2000)
        self.running = False

    # 全てのブロックを削除する関数
    def remove_all_blocks(self):
        self.blocks.empty()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()


if __name__ == "__main__":
    game = BreakoutGame()
    game.run()
