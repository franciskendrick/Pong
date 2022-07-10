from windows import window
import pygame

pygame.init()


class Ball:
    # Ball size
    WIDTH = 10
    HEIGHT = 10

    # Movement
    MAX_VEL = 5

    # Initialize -------------------------------------------------- #
    def __init__(self):
        self.rect = pygame.Rect(
            (window.rect.w // 2 - self.WIDTH // 2) + 1, 
            (window.rect.h // 2 - self.HEIGHT // 2) + 1, 
            self.WIDTH, self.HEIGHT)

        self.x_vel = self.MAX_VEL
        self.y_vel = 0

    # Draw -------------------------------------------------------- #
    def draw(self, display):
        pygame.draw.rect(display, window.white, self.rect)

    # Update ------------------------------------------------------ #
    def update(self, paddles):
        self.movement()
        self.edge_collisions()
        self.paddle_collisions(paddles)

    def movement(self):
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

    def edge_collisions(self):
        handle_rect = self.rect.copy()
        handle_rect.x += self.x_vel
        handle_rect.y += self.y_vel
        if handle_rect.bottom >= window.playable_rect.bottom:
            self.y_vel *= -1
        elif handle_rect.top <= window.playable_rect.top:
            self.y_vel *= -1

    def paddle_collisions(self, paddles):
        if self.x_vel < 0:  # ball is going LEFT
            if (self.rect.centery >= paddles["left"].rect.top) and ( 
                    self.rect.centery <= paddles["left"].rect.bottom) and (
                    self.rect.left <= paddles["left"].rect.right):
                
                # Update x velocity
                self.x_vel *= -1

                # Update y velocity
                difference_in_y = paddles["left"].rect.centery - self.rect.centery
                reduction_factor = (paddles["left"].rect.height / 2) / self.MAX_VEL
                new_y_vel = difference_in_y / reduction_factor
                self.y_vel = -1 * new_y_vel

        else:  # ball is going RIGHT
            if (self.rect.centery >= paddles["right"].rect.top) and (
                    self.rect.centery <= paddles["right"].rect.bottom) and (
                    self.rect.right >= paddles["right"].rect.left):
                
                # Update x velocity
                self.x_vel *= -1

                # Update y velocity
                difference_in_y = paddles["right"].rect.centery - self.rect.centery
                reduction_factor = (paddles["right"].rect.height / 2) / self.MAX_VEL
                new_y_vel = difference_in_y / reduction_factor
                self.y_vel = -1 * new_y_vel
