from utils import clip_set_to_list_on_yaxis, palette_swap
from windows import window
import pygame
import json
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 
        "..", "..", "..",  "..",
        "resources", "windows", "before_game", "gamemode"
        )
    )

# Json
with open(f"{resources_path}/gamemode.json") as json_file:
    gamemode_data = json.load(json_file)


class Buttons:
    # Initialize -------------------------------------------------- #
    def __init__(self, display_size_divider):
        spriteset = pygame.image.load(
            f"{resources_path}/buttons.png")
        order = ["singleplayer", "multiplayer"]
        images = clip_set_to_list_on_yaxis(spriteset)
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
                gamemode_data["buttons_positions"][name],
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
        pass

    # Functions --------------------------------------------------- #
    def reset_overdetection(self):
        pass
