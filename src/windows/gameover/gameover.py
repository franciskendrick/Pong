from windows import window
from .title import Title
from .buttons import Buttons
import pygame

pygame.init()


class GameOver:
    display_size_divider = 4

    def __init__(self):
        wd, ht = window.rect.size
        self.display = pygame.Surface(
            (wd // self.display_size_divider, 
            ht // self.display_size_divider), 
            pygame.SRCALPHA)
        
        self.title = Title()
        self.buttons = Buttons()

    def draw(self, display):
        # Fill gameover's display with a transparent background
        self.display.fill((0, 0, 0, 0))

        # Draw gameover window on gameover's display
        self.title.draw(self.display)
        self.buttons.draw(self.display)

        # Blit gameover's display to original display
        resized_gameover_display = pygame.transform.scale(
            self.display, display.get_size())
        display.blit(resized_gameover_display, (0, 0))
