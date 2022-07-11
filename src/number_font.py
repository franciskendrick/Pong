from utils import clip_font_to_dict
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
        # Get font spriteset
        font_set = pygame.image.load(
            f"{resources_path}/number_font.png")
        font_set.convert()

        # Order of characters in font spriteset
        self.order = [
            "0", "1", "2", "3", "4",
            "5", "6", "7", "8", "9"
        ]

        # Get characters dictionary
        self.characters = clip_font_to_dict(
            font_set, self.order)

        # Spacing
        self.character_spacing = 1

    def render_font(self, display, text, pos, enlarge=1):
        display_handle = pygame.Surface(
            display.get_size(), pygame.SRCALPHA)
        x, y = pos
        x_offset = 0

        # Loop over every character in text
        for char in text:
            # Get character image
            character = self.characters[char]

            # Resize character image
            wd, ht = character.get_size()
            resized_character = pygame.transform.scale(
                character, (wd * enlarge, ht * enlarge))

            # Blit to Handle Display
            display_handle.blit(
                resized_character, (x + x_offset, y))

            # Add to offset the width of resized character and spacing
            x_offset += resized_character.get_width() + self.character_spacing
        
        # Blit to screen
        display.blit(display_handle, (0, 0))
