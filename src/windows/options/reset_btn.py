from utils.image import palette_swap
from windows import window
import pygame
import json
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 
        "..", "..", "..", 
        "resources", "windows", "options"
        )
    )

# Json
with open(f"{resources_path}/options.json") as json_file:
    options_data = json.load(json_file)


class ResetButton:
    # Initialize -------------------------------------------------- #
    def __init__(self, display_size_divider, sprite):
        enlarge = display_size_divider * window.enlarge

        # Palette
        palettes = {
            "hover": {
                (0, 0, 0): (64, 64, 64),
                (255, 255, 255): (128, 128, 128)},
            "on": {
                (0, 0, 0): (128, 128, 128)}
        }

        # Button
        # Initialize palette swapped images
        palette_swapped_images = {}
        for (type, palette) in palettes.items():
            palette_swapped_images[type] = palette_swap(
                sprite.convert(), palette)
        else:
            palette_swapped_images["off"] = sprite

        # Initialize rectangle & hitbox
        rect = pygame.Rect(
            options_data["buttons_positions"]["reset"],
            sprite.get_rect().size)
        hitbox = pygame.Rect(
            rect.x * enlarge, rect.y * enlarge,
            rect.width * enlarge, rect.height * enlarge)

        # Append to button
        self.button = [
            False,  # if mouse is over
            False,  # toggle status
            palette_swapped_images,  # palette swapped images
            rect,  # image's rectangle
            hitbox  # hitbox
        ]

    # Draw -------------------------------------------------------- #
    def draw(self, display):
        mouse_is_over, toggle_status, palette_swapped_images, rect, _ = self.button

        # Get palette swapped image
        if mouse_is_over:
            img = palette_swapped_images["hover"]
        elif toggle_status:
            img = palette_swapped_images["on"]
        else:
            img = palette_swapped_images["off"]

        # Draw to display
        display.blit(img, rect)

    # Action detection -------------------------------------------- #
    def button_down_detection(self):
        pass

    def button_over_detection(self):
        pass

    # Functions --------------------------------------------------- #
    def reset_overdetection(self):
        pass
