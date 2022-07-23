from utils.image import separate_sets_from_yaxis
from utils.image import clip_set_to_list_on_xaxis, palette_swap
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

# Button spritesets
full_spriteset = pygame.image.load(f"{resources_path}/buttons.png")
scoretowin_spriteset, _, _, _, _ = separate_sets_from_yaxis(
    full_spriteset, (255, 0, 0))


class ScoreToWinButtons:
    # Initialize -------------------------------------------------- #
    def __init__(self, display_size_divider):
        order = ["3", "5", "10", "15", "20"]
        images = clip_set_to_list_on_xaxis(scoretowin_spriteset)
        enlarge = display_size_divider * window.enlarge

        # Palette
        hover_palette = {
            (0, 0, 0): (64, 64, 64),
            (255, 255, 255): (128, 128, 128)}

        # Buttons
        self.buttons = {}
        for name, img in zip(order, images):
            # Initialize button
            hover_img = palette_swap(img.convert(), hover_palette)
            rect = pygame.Rect(
                options_data["buttons_positions"]["score_to_win"][name],
                img.get_rect().size)
            hitbox = pygame.Rect(
                rect.x * enlarge, rect.y * enlarge,
                rect.width * enlarge, rect.height * enlarge)

            # Append to buttons
            button = [
                False,  # if mouse is over
                img,  # original image
                hover_img,  # hover image
                rect,  # image's rectangle
                hitbox  # hitbox
            ]
            self.buttons[name] = button

    # Draw -------------------------------------------------------- #
    def draw(self, display):
        for button in self.buttons.values():
            mouse_is_over, orig_img, hover_img, rect, _ = button
            img = hover_img if mouse_is_over else orig_img

            display.blit(img, rect)

    # Action detection -------------------------------------------- #
    def button_down_detection(self):
        pass

    def button_over_detection(self):
        for button in self.buttons.values():
            *_, hitbox = button

            mouse_pos = pygame.mouse.get_pos()
            button[0] = True if hitbox.collidepoint(mouse_pos) else False

    # Functions --------------------------------------------------- #
    def reset_overdetection(self):
        for button in self.buttons.values():
            button[0] = False


class WhoStartsAfterAPointButtons:
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


class KeyboardSensitivityButtons:
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
