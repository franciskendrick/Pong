from utils.image import separate_sets_from_yaxis, clip_set_to_list_on_xaxis
from windows import window
from .title import Title
from .subtitle import Subtitle
from .scoretowin_btns import ScoreToWinButtons
from .startsafterpoint_btns import StartsAfterPointButtons
from .keybrsensitivity_btns import SensitivityButtons
from .back_btn import BackButton
from .reset_btn import ResetButton
from .sound_btn import SoundButton
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


class Options:
    display_size_divider = 3

    def __init__(self):
        wd, ht = window.rect.size
        self.display = pygame.Surface(
            (wd // self.display_size_divider, 
            ht // self.display_size_divider), 
            pygame.SRCALPHA)

        # Initialize titles
        self.title = Title()
        self.subtitle = Subtitle()

        # Get full button spritesets
        full_spriteset = pygame.image.load(
            f"{resources_path}/buttons.png")
        spriteset = separate_sets_from_yaxis(
            full_spriteset, (255, 0, 0))

        # Initialize game settings buttons
        self.scoretowin_buttons = ScoreToWinButtons(
            self.display_size_divider, spriteset[0])
        self.startsafterpoint_buttons = StartsAfterPointButtons(
            self.display_size_divider, spriteset[1])
        self.keyboardsensitivity_buttons = SensitivityButtons(
            self.display_size_divider, spriteset[2])

        # Get miscellaneous button spriteset
        back_img, reset_img, sound_img = clip_set_to_list_on_xaxis(
            spriteset[3])

        # Initialize miscellaneous buttons
        self.back_button = BackButton(
            self.display_size_divider, back_img)
        self.reset_button = ResetButton(
            self.display_size_divider, reset_img)
        self.sound_button = SoundButton(
            self.display_size_divider, sound_img)

    def draw(self, display):
        # Fill options' display with a transparent background
        self.display.fill((0, 0, 0, 0))

        # Draw options window on options' display
        self.title.draw(self.display)
        self.subtitle.draw(self.display)
        self.scoretowin_buttons.draw(self.display)
        self.startsafterpoint_buttons.draw(self.display)
        self.keyboardsensitivity_buttons.draw(self.display)

        # Blit options' display to original display
        resized_menu_display = pygame.transform.scale(
            self.display, display.get_size())
        display.blit(resized_menu_display, (0, 0))
