from utils.spriteset_clipping import clip_set_to_list_on_yaxis
import pygame
import json
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 
        "..", "..", "..", 
        "resources", "windows", "menu"
        )
    )

# Json
with open(f"{resources_path}/menu.json") as json_file:
    menu_data = json.load(json_file)


class Title:
    def __init__(self):
        animation_set = pygame.image.load(
            f"{resources_path}/title_animation.png")
        self.idx = 0

        # Frames
        self.frames = []
        for img in clip_set_to_list_on_yaxis(animation_set):
            # Resize image
            wd, ht = img.get_size()
            size = (wd * 3, ht * 3)
            img = pygame.transform.scale(img, size)

            # Initialize rectangle
            rect = pygame.Rect(
                menu_data["title_position"], img.get_size())

            # Append to frames
            frame = [
                img,  # original image
                rect  # image's rectangle
            ]
            self.frames.append(frame)

    def draw(self, display):
        # Reset
        if self.idx >= len(self.frames) * 10:
            self.idx = 0

        # Draw
        img, rect = self.frames[self.idx // 10]
        display.blit(img, rect)

        # Update
        self.idx += 1
