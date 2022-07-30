from windows import window
import pygame

pygame.init()


class Ball:
    # Ball size
    width = 10
    height = 10

    # Ball position
    original_x = (window.rect.w // 2 - width // 2)
    original_y = (window.rect.h // 2 - height // 2)

    # Movement
    max_vel = 5

    # Initialize -------------------------------------------------- #
    def __init__(self):
        # Rectangle
        self.rect = pygame.Rect(
            self.original_x, self.original_y, 
            self.width, self.height)

        # Velocities
        self.x_vel = self.max_vel
        self.y_vel = 0

    # Draw -------------------------------------------------------- #
    def draw(self, display):
        pygame.draw.rect(display, window.white, self.rect)

    # Update ------------------------------------------------------ #
    def update(self, paddles, sound):
        self.movement()
        self.edge_collisions(sound)
        self.paddle_collisions(paddles, sound)

    def movement(self):
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

    def edge_collisions(self, sound):
        handle_rect = self.rect.copy()
        handle_rect.x += self.x_vel
        handle_rect.y += self.y_vel
        if handle_rect.bottom >= window.playable_rect.bottom:
            # Update y velocity
            self.y_vel *= -1

            # Play sound
            sound.play_ballcollision()
        elif handle_rect.top <= window.playable_rect.top:
            # Update y velocity
            self.y_vel *= -1

            # Play sound
            sound.play_ballcollision()

    def paddle_collisions(self, paddles, sound):
        if self.x_vel < 0:  # ball is going LEFT
            if (self.rect.centery >= paddles["left"].rect.top) and ( 
                    self.rect.centery <= paddles["left"].rect.bottom) and (
                    self.rect.left <= paddles["left"].rect.right):
                
                # Update x velocity
                self.x_vel *= -1

                # Update y velocity
                difference_in_y = paddles["left"].rect.centery - self.rect.centery
                reduction_factor = (paddles["left"].rect.height / 2) / self.max_vel
                new_y_vel = difference_in_y / reduction_factor
                self.y_vel = -1 * new_y_vel

                # Play sound
                sound.play_ballcollision()

        else:  # ball is going RIGHT
            if (self.rect.centery >= paddles["right"].rect.top) and (
                    self.rect.centery <= paddles["right"].rect.bottom) and (
                    self.rect.right >= paddles["right"].rect.left):
                
                # Update x velocity
                self.x_vel *= -1

                # Update y velocity
                difference_in_y = paddles["right"].rect.centery - self.rect.centery
                reduction_factor = (paddles["right"].rect.height / 2) / self.max_vel
                new_y_vel = difference_in_y / reduction_factor
                self.y_vel = -1 * new_y_vel

                # Play sound
                sound.play_ballcollision()

    # Functions --------------------------------------------------- #
    def round_reset(self, whos_ball):
        # Rectangle
        self.rect.x = self.original_x
        self.rect.y = self.original_y

        # Velocities
        if whos_ball == "winners_ball":
            self.x_vel *= -1
        self.y_vel = 0

    def full_reset(self):
        # Rectangle
        self.rect.x = self.original_x
        self.rect.y = self.original_y

        # Velocities
        self.x_vel = self.max_vel
        self.y_vel = 0
