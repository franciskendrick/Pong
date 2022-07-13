from windows import window
import pygame

pygame.init()


class Menu:
    def __init__(self):
        wd, ht = window.rect.size
        self.display = pygame.Surface(
            (wd // 2, ht // 2), pygame.SRCALPHA)
    
    def draw(self, display):
        pass

