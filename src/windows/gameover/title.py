from utils.image import clip_set_to_list_on_yaxis
import pygame
import json
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 
        "..", "..", "..", 
        "resources", "windows", "gameover"
        )
    )

# Json
with open(f"{resources_path}/gameover.json") as json_file:
    gameover_data = json.load(json_file)


class Title:
    def __init__(self):
        animation_set = pygame.image.load(
            f"{resources_path}/title_animation.png")
        self.idx = 0

        # Get title animation's frames
        self.frames = []
        for img in clip_set_to_list_on_yaxis(animation_set):
            # Resize image
            wd, ht = img.get_size()
            size = (wd * 3, ht * 3)
            img = pygame.transform.scale(img, size)

            # Append to frames
            self.frames.append(img)

    def init_rect(self, side):
        self.rect = gameover_data["title_positions"][side]

    def draw(self, display):
        # Reset
        if self.idx >= len(self.frames) * 10:
            self.idx = 0

        # Draw
        img = self.frames[self.idx // 10]
        display.blit(img, self.rect)

        # Update
        self.idx += 1
