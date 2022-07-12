from windows import window
from paddle import Paddle
from ball import Ball
import pygame
import time
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
    global time_of_round_end, round_finished

    # Paddle's button keys
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
        if not round_finished:
            # Update ball
            ball.update(paddles)

            # Check for round winner
            if ball.rect.centerx <= window.playable_rect.left:  # left player lost
                # Update time of round end variable
                time_of_round_end = time.perf_counter()

                # Update ball's position so it would be out of the screen
                ball.rect.right = window.playable_rect.left

                # Update round finished variable to true
                round_finished = True
            elif ball.rect.centerx >= window.playable_rect.right:  # right player lost
                # Update time of round end variable
                time_of_round_end = time.perf_counter()

                # Update ball's position so it would be out of the screen
                ball.rect.left = window.playable_rect.right

                # Update round finished variable to true
                round_finished = True
        else:
            # Reset ball 1.5 seconds after round winner has been declared
            dt = time.perf_counter() - time_of_round_end
            if dt * 1000 >= 1500:
                ball.reset()
                round_finished = False

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
            10, (window.rect.height // 2 - Paddle.height // 2) + 1),
        "right": Paddle(
            window.rect.width - 10 - Paddle.width, 
            (window.rect.height // 2 - Paddle.height // 2) + 1)
    }

    # Initialize ball
    ball = Ball()

    # Initialize win-lose variables
    time_of_round_end = None
    round_finished = False

    # Execute
    game_loop()
