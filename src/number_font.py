from windows import window
import pygame
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..", "resources"
    )
)


class NumberFont:
    def __init__(self):
        pass

    def render_font(self, display, text, pos, color=window.white):
        pass
