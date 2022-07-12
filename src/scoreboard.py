from number_font import NumberFont
from windows import window
import pygame

pygame.init()


class Scoreboard(NumberFont):
    # Positions
    positions = {
        "left": (
            window.center_line.left - (5 * 4) - 20,
            window.playable_rect.y + 8
        ),
        "right": (
            window.center_line.right + 20,
            window.playable_rect.y + 8)
    }

    def __init__(self):
        super().__init__()

        self.scores = {
            "left": 0,
            "right": 0
        }

    def draw(self, display):
        # Left's score
        self.render_font(
            display, 
            str(self.scores["left"]),
            self.positions["left"],
            enlarge=4)

        # Right's score
        self.render_font(
            display, 
            str(self.scores["right"]),
            self.positions["right"],
            enlarge=4)
