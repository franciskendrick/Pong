from windows import window
from .scoreboard import Scoreboard
import pygame

pygame.init()


class Game:
    def __init__(self):
        # Initialize display
        wd, ht = window.rect.size
        self.display = pygame.Surface(
            (wd, ht), pygame.SRCALPHA)

        # Initialize game objects
        self.scoreboard = Scoreboard()

        # Initialize win-lose variables
        self.time_of_round_end = None
        self.round_finished = False

    def draw(self, display):
        # Fill game's display with a transparent background
        self.display.fill((0, 0, 0, 0))

        # Draw game window on game's display
        self.scoreboard.draw(self.display)

        # Blit game's display to original display
        resized_game_display = pygame.transform.scale(
            self.display, display.get_size())
        display.blit(resized_game_display, (0, 0))
