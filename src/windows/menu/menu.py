from windows import window
from .title import Title
from .buttons import Buttons
import pygame

pygame.init()


class Menu:
    def __init__(self):
        wd, ht = window.rect.size
        self.display = pygame.Surface(
            (wd // 4, ht // 4), pygame.SRCALPHA)

        self.title = Title()
        self.buttons = Buttons()
    
    def draw(self, display):
        # Fill menu's display with a transparent background
        self.display.fill((0, 0, 0, 0))

        # Draw menu window on menu's display
        self.title.draw(self.display)
        self.buttons.draw(self.display)

        # Blit menu's display to original display
        resized_menu_display = pygame.transform.scale(
            self.display, display.get_size())
        display.blit(resized_menu_display, (0, 0))
