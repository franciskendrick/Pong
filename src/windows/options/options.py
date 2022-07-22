from windows import window
from .title import Title
from .subtitle import Subtitle
from .buttons import ScoreToWinButtons, WhoStartsAfterAPointButtons, KeyboardSensitivityButtons
import pygame

pygame.init()


class Options:
    display_size_divider = 3

    def __init__(self):
        wd, ht = window.rect.size
        self.display = pygame.Surface(
            (wd // self.display_size_divider, 
            ht // self.display_size_divider), 
            pygame.SRCALPHA)

        self.title = Title()
        self.subtitle = Subtitle()
        self.scoretowin_buttons = ScoreToWinButtons(
            self.display_size_divider)

    def draw(self, display):
        # Fill options' display with a transparent background
        self.display.fill((0, 0, 0, 0))

        # Draw options window on options' display
        self.title.draw(self.display)
        self.subtitle.draw(self.display)
        self.scoretowin_buttons.draw(self.display)

        # Blit options' display to original display
        resized_menu_display = pygame.transform.scale(
            self.display, display.get_size())
        display.blit(resized_menu_display, (0, 0))
