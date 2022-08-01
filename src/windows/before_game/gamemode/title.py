from utils import clip_set_to_list_on_yaxis
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


class Title:
    orig_mult = 10

    def __init__(self):
        animation_set = pygame.image.load(
            f"{resources_path}/title_animation.png")
        self.idx = 0

        # Get title animation's frames
        self.frames = []
        for img in clip_set_to_list_on_yaxis(animation_set):
            # Resize image
            wd, ht = img.get_size()
            size = (wd * 2, ht * 2)
            img = pygame.transform.scale(img, size)

            # Append to frames
            self.frames.append(img)

        # Initialize rectangle
        self.rect = pygame.Rect(
            gamemode_data["title_position"], img.get_size())

    def draw(self, display):
        # Get Multiplier
        dt = round(window.delta_time)
        dt_multiplier = round(self.orig_mult / dt) if dt > 0 else 0
        multiplier = dt_multiplier if dt_multiplier > 0 else self.orig_mult

        # Reset
        if self.idx >= len(self.frames) * multiplier:
            self.idx = 0

        # Draw
        img = self.frames[self.idx // multiplier]
        display.blit(img, self.rect)

        # Update
        self.idx += 1
