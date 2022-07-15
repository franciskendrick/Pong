from windows import window
from .title import Title
import pygame

pygame.init()


class Pause:
    def __init__(self):
        wd, ht = window.rect.size
        self.display = pygame.Surface(
            (wd, ht), pygame.SRCALPHA)

        self.title = Title()

    def draw(self, display):
        # Fill pause's display with a transparent background
        self.display.fill((0, 0, 0, 0))

        # Draw pause window on pause's display
        self.title.draw(self.display)

        # Blit pause's display to original display
        display.blit(self.display, (0, 0))
