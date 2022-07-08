from windows import window
import pygame

pygame.init()


class Ball:
    # Ball size
    WIDTH = 10
    HEIGHT = 10

    # Initialize -------------------------------------------------- #
    def __init__(self):
        self.rect = pygame.Rect(
            (window.rect.w // 2 - self.WIDTH // 2) + 1, 
            (window.rect.h // 2 - self.HEIGHT // 2) + 1, 
            self.WIDTH, self.HEIGHT)

    # Draw -------------------------------------------------------- #
    def draw(self, display):
        pygame.draw.rect(display, window.white, self.rect)

    # Update ------------------------------------------------------ #
    def movement(self):
        pass

    # Functions --------------------------------------------------- #
    def collisions(self):
        pass