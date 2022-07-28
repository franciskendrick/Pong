from windows import window
import pygame

pygame.init()


class GameMode:
    display_size_divider = 4

    def __init__(self):
        wd, ht = window.rect.size
        self.display = pygame.Surface(
            (wd // self.display_size_divider, 
            ht // self.display_size_divider), 
            pygame.SRCALPHA)

    def draw(self, display):
        # Fill gamemode's display with a transparent background
        self.display.fill((0, 0, 0, 0))

        # Draw gamemode window on gamemode's display

        # Blit gamemode's display to original display
        resized_gamemode_display = pygame.transform.scale(
            self.display, display.get_size())
        display.blit(resized_gamemode_display, (0, 0))
