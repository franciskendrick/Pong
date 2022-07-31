import pygame
import json
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 
        "..", "..", "..",  "..",
        "resources", "windows", "before_game", "difficulty"
        )
    )

# Json
with open(f"{resources_path}/difficulty.json") as json_file:
    difficulty_data = json.load(json_file)


class Buttons:
    # Initialize -------------------------------------------------- #
    def __init__(self, display_size_divider):
        pass

    # Draw -------------------------------------------------------- #
    def draw(self, display):
        pass
    
    # Action detection -------------------------------------------- #
    def button_down_detection(self):
        pass

    def button_over_detection(self):
        pass

    # Functions --------------------------------------------------- #
    def reset_overdetection(self):
        pass
