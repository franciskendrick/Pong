import pygame

pygame.init()


class Window:
    def __init__(self):
        # Window
        self.rect = pygame.Rect(0, 0, 640, 360)
        self.enlarge = 2
        self.enlarge = max(
            pygame.display.Info().current_w / self.rect.width,
            pygame.display.Info().current_h / self.rect.height)

        # Court
        self.playable_rect = pygame.Rect(
            0, 10, self.rect.w, self.rect.h-20)
        self.center_line = [
            (self.rect.w // 2, 0),
            (self.rect.w // 2, self.rect.h)]

        # Colors
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)

        # Framerate
        self.framerate = 60


window = Window()
