from windows import window
import pygame

pygame.init()


class Ball:
    # Ball size
    WIDTH = 10
    HEIGHT = 10

    # Movement
    MAX_VEL = 5

    # Initialize -------------------------------------------------- #
    def __init__(self):
        self.rect = pygame.Rect(
            (window.rect.w // 2 - self.WIDTH // 2) + 1, 
            (window.rect.h // 2 - self.HEIGHT // 2) + 1, 
            self.WIDTH, self.HEIGHT)

        self.x_vel = self.MAX_VEL
        self.y_vel = 0

    # Draw -------------------------------------------------------- #
    def draw(self, display):
        pygame.draw.rect(display, window.white, self.rect)

    # Update ------------------------------------------------------ #
    def update(self):
        self.movement()

    def movement(self):
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

    def collisions(self):
        pass