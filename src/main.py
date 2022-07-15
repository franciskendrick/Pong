from windows import window
from windows.game import Scoreboard
from windows.menu import Menu
from windows.pause import Pause
from entities import Paddle
from entities import Ball
import pygame
import time
import sys


# Redraw
def redraw_game():
    # Draw background
    display.fill(window.white)
    pygame.draw.rect(display, window.black, window.playable_rect)
    pygame.draw.rect(display, window.white, window.center_line)
    
    # Draw scoreboard
    scoreboard.draw(display)

    # Draw paddles
    for paddle in paddles.values():
        paddle.draw(display)

    # Draw ball
    ball.draw(display)

    # Blit to window ---------------------------------------------- #
    resized_display = pygame.transform.scale(display, win_size)
    win.blit(resized_display, (0, 0))

    pygame.display.update()


def redraw_menu():
    # Draw background
    display.fill(window.white)
    pygame.draw.rect(display, window.black, window.playable_rect)

    # Draw menu
    menu.draw(display)

    # Blit to window ---------------------------------------------- #
    resized_display = pygame.transform.scale(display, win_size)
    win.blit(resized_display, (0, 0))

    pygame.display.update()


def redraw_pause():
    # Blit to window ---------------------------------------------- #
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

    # Loop
    run = True
    while run:
        # Event loop
        for event in pygame.event.get():
            # Quit detection
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

                # Update winner's (right's) score
                scoreboard.scores["right"] += 1

                # Update round finished variable to true
                round_finished = True
            elif ball.rect.centerx >= window.playable_rect.right:  # right player lost
                # Update time of round end variable
                time_of_round_end = time.perf_counter()

                # Update ball's position so it would be out of the screen
                ball.rect.left = window.playable_rect.right

                # Update winner's (left's) score
                scoreboard.scores["left"] += 1

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


def menu_loop():
    btn_switchcase = {
        "play": [game_loop],
        "options": [],  # !!!
        "quit": []
    }

    # Loop
    run = True
    while run:
        # Event loop
        for event in pygame.event.get():
            # Quit detection
            if event.type == pygame.QUIT:
                run = False

            # Mouse buttons' down detection
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # left-click has been clicked
                btn_pressed = menu.buttons.button_down_detection()
                if btn_pressed != None:  # a button has been pressed
                    if btn_pressed == "quit":  # the button pressed is the QUIT button
                        run = False
                    else:  # the button pressed is NOT the QUIT button
                        for function in btn_switchcase[btn_pressed]:
                            function()


            # Menu Buttons' over detection
            if event.type == pygame.MOUSEMOTION:
                menu.buttons.button_over_detection()

        # Update display
        redraw_menu()
        clock.tick(window.framerate)
        
    pygame.quit()
    sys.exit()


def pause_loop():
    # Loop
    run = True
    while run:
        # Event loop
        for event in pygame.event.get():
            # Quit detection
            if event.type == pygame.QUIT:
                run = False

        # Update display
        redraw_pause()
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
            10, (window.rect.height // 2 - Paddle.height // 2)),
        "right": Paddle(
            window.rect.width - 10 - Paddle.width, 
            (window.rect.height // 2 - Paddle.height // 2))
    }

    # Initialize ball
    ball = Ball()

    # Initialize windows
    menu = Menu()
    pause = Pause()

    # Initialize scoreboard
    scoreboard = Scoreboard()

    # Initialize win-lose variables
    time_of_round_end = None
    round_finished = False

    # Execute
    menu_loop()
