import pygame
import json
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 
        "..", "..", "..", 
        "resources", "windows", "pause"
        )
    )

# Json
with open(f"{resources_path}/pause.json") as json_file:
    pause_data = json.load(json_file)


class Buttons:
    # Initialize -------------------------------------------------- #
    def __init__(self, display_size_divider):
        pass

    # Draw -------------------------------------------------------- #
    def draw(self, display):
        pass

    # Functions --------------------------------------------------- #
    def button_down_detection(self):
        pass

    def button_over_detection(self):
        pass
