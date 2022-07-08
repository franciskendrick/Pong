from windows import window
from paddle import Paddle
from ball import Ball
import pygame
import sys


# Redraw
def redraw_game():
    # Draw background
    display.fill(window.white)
    pygame.draw.rect(display, window.black, window.playable_rect)
    pygame.draw.line(display, window.white, *window.center_line, 10)
    
    # Draw paddles
    for paddle in paddles.values():
        paddle.draw(display)

    # Draw ball
    ball.draw(display)

    # Blit to screen ---------------------------------------------- #
    resized_display = pygame.transform.scale(display, win_size)
    win.blit(resized_display, (0, 0))

    pygame.display.update()


# Loop
def game_loop():
    paddle_buttonkeys = {
        "left": {
            "up": pygame.K_w,
            "down": pygame.K_s
        },
        "right": {
            "up": pygame.K_UP,
            "down": pygame.K_DOWN
        }
    }

    run = True
    while run:
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        # Update paddles
        for (side, paddle) in paddles.items():
            paddle.movement(paddle_buttonkeys[side])

        # Update ball
        ball.update()

        # Update display
        redraw_game()
        clock.tick(window.framerate)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    pygame.init()

    # Initialize window
    win_size = (
        int(window.rect.width * window.enlarge),
        int(window.rect.height * window.enlarge))
    win = pygame.display.set_mode(win_size, 32)
    display = pygame.Surface(window.rect.size)
    pygame.display.set_caption("Pong!")
    clock = pygame.time.Clock()

    # Initialize paddle
    paddles = {
        "left": Paddle(
            10, (window.rect.h // 2 - Paddle.HEIGHT // 2) + 1),
        "right": Paddle(
            window.rect.w - 10 - Paddle.WIDTH, 
            (window.rect.h // 2 - Paddle.HEIGHT // 2) + 1)
    }

    # Initialize ball
    ball = Ball()

    # Execute
    game_loop()
