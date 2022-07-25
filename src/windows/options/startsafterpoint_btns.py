from utils.image import clip_set_to_list_on_yaxis, palette_swap
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


class StartsAfterPointButtons:
    # Initialize -------------------------------------------------- #
    def __init__(self, display_size_divider, spriteset):
        order = ["winners_ball", "losers_ball"]
        images = clip_set_to_list_on_yaxis(spriteset)
        enlarge = display_size_divider * window.enlarge

        # Palette
        palettes = {
            "hover": {
                (0, 0, 0): (64, 64, 64),
                (255, 255, 255): (128, 128, 128)},
            "on": {
                (0, 0, 0): (128, 128, 128)}
        }

        # Buttons
        self.buttons = {}
        for name, img in zip(order, images):
            # Initialize toggle status
            options_settings = window.options_settings["who_starts_after_a_point"]
            toggle_status = True if options_settings == name else False

            # Initialize palette swapped images
            palette_swapped_images = {}
            for (type, palette) in palettes.items():
                palette_swapped_images[type] = palette_swap(
                    img.convert(), palette)
            else:
                palette_swapped_images["off"] = img

            # Initialize rectangle & hitbox
            rect = pygame.Rect(
                options_data["buttons_positions"]["who_starts_after_a_point"][name],
                img.get_rect().size)
            hitbox = pygame.Rect(
                rect.x * enlarge, rect.y * enlarge,
                rect.width * enlarge, rect.height * enlarge)

            # Append
            button = [
                False,  # if mouse is over
                toggle_status,  # toggle status
                palette_swapped_images,  # palette swapped images
                rect,  # image's rectangle
                hitbox  # hitbox
            ]
            self.buttons[name] = button

    # Draw -------------------------------------------------------- #
    def draw(self, display):
        for button in self.buttons.values():
            mouse_is_over, toggle_status, palette_swapped_images, rect, _ = button

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
        for (name, button) in self.buttons.items():
            *_, hitbox = button

            mouse_pos = pygame.mouse.get_pos()
            if hitbox.collidepoint(mouse_pos):
                # Update all buttons' toggle status to false
                for button in self.buttons.values():
                    button[1] = False
                
                # Update clicked button's toggle status to true
                self.buttons[name][1] = True

    def button_over_detection(self):
        for button in self.buttons.values():
            *_, hitbox = button

            mouse_pos = pygame.mouse.get_pos()
            button[0] = True if hitbox.collidepoint(mouse_pos) else False

    # Functions --------------------------------------------------- #
    def reset_overdetection(self):
        for button in self.buttons.values():
            button[0] = False
