from utils import clip_set_to_list_on_yaxis
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


class Subtitle:
    def __init__(self):
        spriteset = pygame.image.load(
            f"{resources_path}/subtitles.png")
        order = [
            "score_to_win", 
            "who_starts_after_a_point", 
            "keyboard_sensitivity"]

        self.subtitle = {
            name: [img, rect] 
                for (name, img, rect) in zip(
                    order, 
                    clip_set_to_list_on_yaxis(spriteset), 
                    options_data["subtitle_positions"].values())
            }

    def draw(self, display):
        for img, rect in self.subtitle.values():
            display.blit(img, rect)
