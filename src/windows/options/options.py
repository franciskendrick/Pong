from utils import separate_sets_from_yaxis
from windows import window
from .title import Title
from .subtitle import Subtitle
from .scoretowin_btns import ScoreToWinButtons
from .startsafterpoint_btns import StartsAfterPointButtons
from .keybrsensitivity_btns import SensitivityButtons
from .miscellaneous_btns import MiscellaneousButtons
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
    original_optionssettings = {
        "score_to_win": "10",
        "who_starts_after_a_point": "losers_ball",
        "keyboard_sensitivity": "normal"
    }
    display_size_divider = 3

    # Initialize -------------------------------------------------- #
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
        self.miscellaneous_buttons = MiscellaneousButtons(
            self.display_size_divider, spriteset[3])

        # Score to win value
        self.score_limit = self.scoretowin_buttons.get_scoretowin_value()

    # Draw -------------------------------------------------------- #
    def draw(self, display):
        # Fill options' display with a transparent background
        self.display.fill((0, 0, 0, 0))

        # Draw options window on options' display
        self.title.draw(self.display)
        self.subtitle.draw(self.display)

        self.scoretowin_buttons.draw(self.display)
        self.startsafterpoint_buttons.draw(self.display)
        self.keyboardsensitivity_buttons.draw(self.display)
        self.miscellaneous_buttons.draw(self.display)

        # Blit options' display to original display
        resized_menu_display = pygame.transform.scale(
            self.display, display.get_size())
        display.blit(resized_menu_display, (0, 0))

    # Functions --------------------------------------------------- #
    def reset(self):
        options_buttons = {
            "score_to_win": self.scoretowin_buttons, 
            "who_starts_after_a_point": self.startsafterpoint_buttons,
            "keyboard_sensitivity": self.keyboardsensitivity_buttons}

        # Turn off all options settings' buttons' toggle status
        for options_btn in options_buttons.values():
            for button in options_btn.buttons.values():
                button[1] = False

        # Turn on the orignial values in options settings' buttons' toggle status
        for options_btn, original_value in zip(
                options_buttons.values(), self.original_optionssettings.values()):
            for (name, button) in options_btn.buttons.items():
                if name == original_value:
                    button[1] = True
                    break

    def reset_overdetection(self):
        options_buttons = [
            self.scoretowin_buttons,
            self.startsafterpoint_buttons,
            self.keyboardsensitivity_buttons,
            self.miscellaneous_buttons]
            
        for buttons in options_buttons:
            buttons.reset_overdetection()
