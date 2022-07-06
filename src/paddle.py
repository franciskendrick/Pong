from windows import window
import pygame

pygame.init()


class Paddle:
    WIDTH = 5
    HEIGHT = 50

    def __init__(self, x, y):
        self.rect = pygame.Rect(
            x, y, self.WIDTH, self.HEIGHT)

    def draw(self, display):
        pygame.draw.rect(display, window.white, self.rect)

    def update(self):
        pass
