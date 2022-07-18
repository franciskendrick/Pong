from windows import window
import pygame

pygame.init()


class GameOver:
    def __init__(self):
        wd, ht = window.rect.size
        self.display = pygame.Surface(
            (wd, ht), pygame.SRCALPHA)
        
    def draw(self, display):
        # Fill gameover's display with a transparent background
        self.display.fill((0, 0, 0, 0))

        # Blit gameover's display to original display
        resized_menu_display = pygame.transform.scale(
            self.display, display.get_size())
        display.blit(resized_menu_display, (0, 0))