from windows import window, Game, Menu, Options, Pause, GameOver
from entities import Paddle
from entities import Ball
import pygame
import time
import sys


# Functions ------------------------------------------------------- #
def game_reset():
    global paddles, ball

    for (side, paddle) in paddles.items():
        paddle.rect.x, paddle.rect.y = paddle_positions[side]
    ball.full_reset()
    game.scoreboard.full_reset()


# Redraw ---------------------------------------------------------- #
def redraw_game():
    # Draw background
    display.fill(window.white)
    window.draw_playablesurface(display)
    window.draw_centerline(display)
    
    # Draw game
    game.draw(display)

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
    window.draw_playablesurface(display)

    # Draw menu
    menu.draw(display)

    # Blit to window ---------------------------------------------- #
    resized_display = pygame.transform.scale(display, win_size)
    win.blit(resized_display, (0, 0))

    pygame.display.update()


def redraw_options():
    # Draw background
    display.fill(window.white)
    window.draw_playablesurface(display)

    # Draw options
    options.draw(display)
    
    # Blit to window ---------------------------------------------- #
    resized_display = pygame.transform.scale(display, win_size)
    win.blit(resized_display, (0, 0))

    pygame.display.update()


def redraw_pause():
    # Draw background
    display.fill(window.white)
    window.draw_playablesurface(display)
    window.draw_centerline(display)
    
    # Draw game
    game.scoreboard.draw(display)

    # Draw paddles
    for paddle in paddles.values():
        paddle.draw(display)

    # Draw ball
    ball.draw(display)

    # Draw pause
    pause.draw(display)

    # Blit to window ---------------------------------------------- #
    resized_display = pygame.transform.scale(display, win_size)
    win.blit(resized_display, (0, 0))

    pygame.display.update()


def redraw_gameover():
    # Draw background
    display.fill(window.white)
    window.draw_playablesurface(display)
    window.draw_centerline(display)

    # Draw game
    game.scoreboard.draw(display)

    # Draw paddles
    for paddle in paddles.values():
        paddle.draw(display)

    # Draw gameover
    gameover.draw(display)

    # Blit to window ---------------------------------------------- #
    resized_display = pygame.transform.scale(display, win_size)
    win.blit(resized_display, (0, 0))

    pygame.display.update()


# Loop ------------------------------------------------------------ #
def game_loop():
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

            # Keydown detection
            if event.type == pygame.KEYDOWN:
                # Pause
                if event.key == pygame.K_ESCAPE:
                    pause_loop()
        
        # Update paddles
        for (side, paddle) in paddles.items():
            paddle.movement(paddle_buttonkeys[side])

        # Update ball
        if not game.round_finished:
            # Update ball
            ball.update(paddles)

            # Check for round winner
            if ball.rect.centerx <= window.playable_rect.left:  # left player lost
                # Update time of round end variable
                game.time_of_round_end = time.perf_counter()

                # Update ball's position so it would be out of the screen
                ball.rect.right = window.playable_rect.left

                # Update winner's (right's) score
                game.scoreboard.scores["right"] += 1

                # Update round finished variable to true
                game.round_finished = True
            elif ball.rect.centerx >= window.playable_rect.right:  # right player lost
                # Update time of round end variable
                game.time_of_round_end = time.perf_counter()

                # Update ball's position so it would be out of the screen
                ball.rect.left = window.playable_rect.right

                # Update winner's (left's) score
                game.scoreboard.scores["left"] += 1

                # Update round finished variable to true
                game.round_finished = True
        else:
            # Reset ball 1.5 seconds after round winner has been declared
            dt = time.perf_counter() - game.time_of_round_end
            if dt * 1000 >= 1500:
                ball.round_reset()
                game.round_finished = False

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
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # left-click has been uped
                btn_pressed = menu.buttons.button_down_detection()
                if btn_pressed != None:  # a button has been pressed
                    if btn_pressed == "quit":  # the button pressed is the QUIT button
                        run = False
                    else:  # the button pressed is NOT the QUIT button
                        for function in btn_switchcase[btn_pressed]:
                            menu.buttons.reset_overdetection()
                            function()

            # Menu buttons' over detection
            if event.type == pygame.MOUSEMOTION:
                menu.buttons.button_over_detection()

        # Update display
        redraw_menu()
        clock.tick(window.framerate)
        
    pygame.quit()
    sys.exit()


def options_loop():
    # Loop
    run = True
    while run:
        # Event loop
        for event in pygame.event.get():
            # Quit detection
            if event.type == pygame.QUIT:
                run = False

            # Mouse buttons' down detection
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # left-click has been downed
                options.scoretowin_buttons.button_down_detection()
                options.startsafterpoint_buttons.button_down_detection()

            # Mouse buttons' over detection
            if event.type == pygame.MOUSEMOTION:
                options.scoretowin_buttons.button_over_detection()
                options.startsafterpoint_buttons.button_over_detection()
                options.keyboardsensitivity_buttons.button_over_detection()

        # Update display
        redraw_options() 
        clock.tick(window.framerate)

    pygame.quit()
    sys.exit()


def pause_loop():
    btn_switchcase = {
        "play": [game_loop],
        "menu": [game_reset, menu_loop]
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
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # left-click has been uped
                btn_pressed = pause.buttons.button_down_detection()
                if btn_pressed != None:
                    for function in btn_switchcase[btn_pressed]:
                        pause.buttons.reset_overdetection()
                        function()

            # Mouse buttons' over detection
            if event.type == pygame.MOUSEMOTION:
                pause.buttons.button_over_detection()

            # Keydown detection
            if event.type == pygame.KEYDOWN:
                # Pause
                if event.key == pygame.K_ESCAPE:
                    game_loop()

        # Update display
        redraw_pause()
        clock.tick(window.framerate)

    pygame.quit()
    sys.exit()


def gameover_loop():
    # !!!
    won_side = "left"
    gameover.title.init_rect(won_side)
    gameover.buttons.init_rect(
        won_side, GameOver.display_size_divider)

    # Initialize button switchcase
    btn_switchcase = {
        "play": [game_reset, game_loop],
        "options": [],  # !!!
        "menu": [game_reset, menu_loop]
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
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                btn_pressed = gameover.buttons.button_down_detection()
                if btn_pressed != None:  # a button has been pressed
                    for function in btn_switchcase[btn_pressed]:
                        gameover.buttons.reset_overdetection()
                        function()

            # Mouse buttons' over detection
            if event.type == pygame.MOUSEMOTION:
                gameover.buttons.button_over_detection()

        # Update display
        redraw_gameover()
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
    paddle_positions = {
        "left": [10, (window.rect.height // 2 - Paddle.height // 2)],
        "right": [
            (window.rect.width - 10 - Paddle.width), 
            (window.rect.height // 2 - Paddle.height // 2)
        ]
    }
    paddles = {
        "left": Paddle(*paddle_positions["left"]),
        "right": Paddle(*paddle_positions["right"])
    }

    # Initialize ball
    ball = Ball()

    # Initialize windows
    game = Game()
    menu = Menu()
    pause = Pause()
    gameover = GameOver()
    options = Options()

    # Execute
    options_loop()
