import pygame

pygame.init()


class Window:
    # Window
    rect = pygame.Rect(0, 0, 640, 360)
    enlarge = 2
    # enlarge = max(
    #     pygame.display.Info().current_w / rect.width,
    #     pygame.display.Info().current_h / rect.height)

    # Court
    playable_rect = pygame.Rect(
        0, 10, rect.width, rect.height-20)
    center_line = pygame.Rect(
        rect.centerx - 10 // 2, 0,
        10, rect.height)

    # Colors
    black = (0, 0, 0)
    white = (255, 255, 255)

    framerate = 60

    def draw_playablesurface(self, display):
        pygame.draw.rect(display, self.black, self.playable_rect)

    def draw_centerline(self, display):
        pygame.draw.rect(display, self.white, self.center_line)


window = Window()
