from windows import window
import pygame

pygame.init()


class Paddle:
    # Paddle size
    WIDTH = 5
    HEIGHT = 50

    # Movement
    VEL = 4

    # Initialize -------------------------------------------------- #
    def __init__(self, x, y):
        self.rect = pygame.Rect(
            x, y, self.WIDTH, self.HEIGHT)

    # Draw -------------------------------------------------------- #
    def draw(self, display):
        pygame.draw.rect(display, window.white, self.rect)

    # Update ------------------------------------------------------ #
    def movement(self, buttons):
        keys = pygame.key.get_pressed()

        # Up movement
        if keys[buttons["up"]]:
            # Get a hitbox handle
            handle_hitbox = self.rect.copy()
            handle_hitbox.y -= self.VEL
            # Check for playable rectangle and hitbox collision
            if window.playable_rect.top < handle_hitbox.top:
                self.rect.y -= self.VEL

        # Down movement
        if keys[buttons["down"]]: 
            # Get a hitbox handle
            handle_hitbox = self.rect.copy()
            handle_hitbox.y += self.VEL
            # Check for playable rectangle and hitbox collision
            if window.playable_rect.bottom > handle_hitbox.bottom:
                self.rect.y += self.VEL
