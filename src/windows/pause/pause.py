from windows import window
from .title import Title
from .buttons import Buttons
import pygame

pygame.init()


class Pause:
    def __init__(self):
        display_size_divider = 2
        wd, ht = window.rect.size
        self.display = pygame.Surface(
            (wd // display_size_divider, ht // display_size_divider), 
            pygame.SRCALPHA)

        self.title = Title()
        self.buttons = Buttons(display_size_divider)

    def draw(self, display):
        # Fill pause's display with a transparent background
        self.display.fill((0, 0, 0, 0))

        # Draw pause window on pause's display
        self.title.draw(self.display)
        self.buttons.draw(self.display)

        # Blit pause's display to original display
        resized_pause_display = pygame.transform.scale(
            self.display, display.get_size())
        display.blit(resized_pause_display, (0, 0))
