from windows import window
from .title import Title
import pygame

pygame.init()


class Menu:
    def __init__(self):
        wd, ht = window.rect.size
        self.display = pygame.Surface(
            (wd // 2, ht // 2), pygame.SRCALPHA)

        self.title = Title()
    
    def draw(self, display):
        pass

