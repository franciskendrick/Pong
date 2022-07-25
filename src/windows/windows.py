import pygame
import json
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 
        "..", "..", 
        "resources", "windows"
        )
    )


class Window:
    # Window
    rect = pygame.Rect(0, 0, 640, 360)
    enlarge = 2
    # enlarge = max(
    #     pygame.display.Info().current_w / rect.width,
    #     pygame.display.Info().current_h / rect.height)

    # Court
    playable_rect = pygame.Rect(
        0, 10, rect.width, rect.height-20)
    center_line = pygame.Rect(
        rect.centerx - 10 // 2, 0,
        10, rect.height)

    # Colors
    black = (0, 0, 0)
    white = (255, 255, 255)

    # Framerate
    framerate = 60

    # Initialize -------------------------------------------------- #
    def __init__(self):
        # Options Stauts
        with open(f"{resources_path}/options_settings.json") as json_file:
            self.options_settings = json.load(json_file)

    # Draw -------------------------------------------------------- #
    def draw_playablesurface(self, display):
        pygame.draw.rect(display, self.black, self.playable_rect)

    def draw_centerline(self, display):
        pygame.draw.rect(display, self.white, self.center_line)


window = Window()
