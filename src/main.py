# Import window module
from windows import window

# Import main windows
from windows import Menu
from windows import GameMode
from windows import Game
from windows import Options
from windows import Pause
from windows import GameOver

# Import audio
from audio import Sound

# Import game entities
from entities import Paddle
from entities import Ball

# Import libraries
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


def redraw_gamemode():
    # Draw background
    display.fill(window.white)
    window.draw_playablesurface(display)

    # Draw gamemode
    gamemode.draw(display)

    # Blit to window ---------------------------------------------- #
    resized_display = pygame.transform.scale(display, win_size)
    win.blit(resized_display, (0, 0))

    pygame.display.update()


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
def menu_loop():
    # Loop
    run = True
    while run:
        # Event loop
        for event in pygame.event.get():
            # Quit detection
            if event.type == pygame.QUIT:
                # Update options settings' JSON
                options_settings = {
                    "score_to_win": options.scoretowin_buttons,
                    "who_starts_after_a_point": options.startsafterpoint_buttons,
                    "keyboard_sensitivity": options.keyboardsensitivity_buttons,
                    "miscellaneous": options.miscellaneous_buttons
                }
                window.update_optionssettings(options_settings)

                # Turn off the loop
                run = False

            # Menu buttons' down detection
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # left-click has been uped
                btn_pressed = menu.buttons.button_down_detection()
                if btn_pressed == "play":  # the button pressed is the PLAY button
                    sound.play_buttonclick()  # play sound
                    menu.buttons.reset_overdetection()  # reset menu's buttons' over detection
                    gamemode_loop()  # redirect to gamemode loop
                elif btn_pressed == "options":  # the button pressed is the OPTIONS button
                    sound.play_buttonclick()  # play sound
                    menu.buttons.reset_overdetection()  # reset menu's buttons' over detection
                    options_loop("menu")  # redirect to options loop
                elif btn_pressed == "quit":  # the button pressed is the QUIT button
                    sound.play_buttonclick()  # play sound
                    run = False

            # Menu buttons' over detection
            if event.type == pygame.MOUSEMOTION:
                menu.buttons.button_over_detection()

        # Update display
        redraw_menu()
        clock.tick(window.framerate)
        
    pygame.quit()
    sys.exit()


def gamemode_loop():
    # Initialize gamemode's buttons switchcase
    btn_switchcase = {
        "singleplayer": [],
        "multiplayer": [
            sound.play_buttonclick,  # play sound
            gamemode.buttons.reset_overdetection,  # reset gamemode's buttons' over detection
            game_reset,  # reset game variables
            game_loop  # redirect to game loop
        ],
    }
    
    # Loop
    run = True
    while run:
        # Event loop
        for event in pygame.event.get():
            # Quit detection
            if event.type == pygame.QUIT:
                # Update options settings' JSON
                options_settings = {
                    "score_to_win": options.scoretowin_buttons,
                    "who_starts_after_a_point": options.startsafterpoint_buttons,
                    "keyboard_sensitivity": options.keyboardsensitivity_buttons,
                    "miscellaneous": options.miscellaneous_buttons
                }
                window.update_optionssettings(options_settings)

                # Turn off the loop
                run = False

            # GameMode buttons' down detection
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # left-click has been uped
                btn_pressed = gamemode.buttons.button_down_detection()
                if btn_pressed != None:
                    for function in btn_switchcase[btn_pressed]:
                        function()

            # GameMode buttons' over detection
            if event.type == pygame.MOUSEMOTION:
                gamemode.buttons.button_over_detection()

        # Update display
        redraw_gamemode()
        clock.tick(window.framerate)

    pygame.quit()
    sys.exit()


def game_loop():
    # Update paddles' sensitivity
    sensitivity = options.keyboardsensitivity_buttons.get_sensitivity_value()
    for paddle in paddles.values():
        paddle.update_sensitivity(sensitivity)

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
                # Update options settings' JSON
                options_settings = {
                    "score_to_win": options.scoretowin_buttons,
                    "who_starts_after_a_point": options.startsafterpoint_buttons,
                    "keyboard_sensitivity": options.keyboardsensitivity_buttons,
                    "miscellaneous": options.miscellaneous_buttons
                }
                window.update_optionssettings(options_settings)

                # Turn off the loop
                run = False

            # Keydown detection
            if event.type == pygame.KEYDOWN:
                # Pause
                if event.key == pygame.K_ESCAPE:
                    sound.play_pause()  # play sound
                    pause_loop()  # redirect to pause loop
        
        # Update paddles
        for (side, paddle) in paddles.items():
            paddle.movement(paddle_buttonkeys[side])

        # Update ball
        if not game.round_finished:
            # Update ball
            ball.update(paddles, sound)

            # Check for round winner
            if ball.rect.centerx <= window.playable_rect.left:  # left player lost
                # Update time of round end variable
                game.time_of_round_end = time.perf_counter()

                # Play sound
                sound.play_missedshot()

                # Update ball's position so it would be out of the screen
                ball.rect.right = window.playable_rect.left

                # Update winner's (right's) score
                game.scoreboard.scores["right"] += 1

                # Update round finished variable to true
                game.round_finished = True
            elif ball.rect.centerx >= window.playable_rect.right:  # right player lost
                # Update time of round end variable
                game.time_of_round_end = time.perf_counter()

                # Play sound
                sound.play_missedshot()

                # Update ball's position so it would be out of the screen
                ball.rect.left = window.playable_rect.right

                # Update winner's (left's) score
                game.scoreboard.scores["left"] += 1

                # Update round finished variable to true
                game.round_finished = True
        
            # Check for game winner
            if game.scoreboard.scores["right"] >= options.score_limit:  # right player won
                # Initialize the winning side
                won_side = "right"

                # Initialize gameover's rectangles
                gameover.title.init_rect(won_side)
                gameover.buttons.init_rect(
                    won_side, GameOver.display_size_divider)

                # Play sound 
                sound.play_win()

                # Redirect to gameover loop
                gameover_loop()
            elif game.scoreboard.scores["left"] >= options.score_limit:  # left player won
                # Initialize the winning side
                won_side = "left"

                # Initialize gameover's rectangles
                gameover.title.init_rect(won_side)
                gameover.buttons.init_rect(
                    won_side, GameOver.display_size_divider)

                # Play sound 
                sound.play_win()

                # Redirect to gameover loop
                gameover_loop()
        else:
            # Reset ball 1.5 seconds after round winner has been declared
            dt = time.perf_counter() - game.time_of_round_end
            if dt * 1000 >= 1500:
                whos_ball = options.startsafterpoint_buttons.get_whosball_value()
                ball.round_reset(whos_ball)
                game.round_finished = False

        # Update display
        redraw_game()
        clock.tick(window.framerate)

    pygame.quit()
    sys.exit()


def options_loop(from_loop):
    # Initialize options' buttons switchcase
    backbtn_switchcase = {
        "menu": [
            sound.play_buttonclick,  # play sound
            options.reset_overdetection,  # reset options' buttons' over detection
            menu_loop  # redirect to menu loop
        ],
        "gameover": [
            sound.play_buttonclick,  # play sound
            options.reset_overdetection,  # reset options' buttons' over detection
            gameover_loop  # redirect to gameover loop
        ]
    }
    btn_switchcase = {
        "back": backbtn_switchcase[from_loop],
        "reset": [
            sound.play_buttonclick,  # play sound
            options.reset  # reset options settings
        ]
    }

    # Loop
    run = True
    while run:
        # Event loop
        for event in pygame.event.get():
            # Quit detection
            if event.type == pygame.QUIT:
                # Update options settings' JSON
                options_settings = {
                    "score_to_win": options.scoretowin_buttons,
                    "who_starts_after_a_point": options.startsafterpoint_buttons,
                    "keyboard_sensitivity": options.keyboardsensitivity_buttons,
                    "miscellaneous": options.miscellaneous_buttons
                }
                window.update_optionssettings(options_settings)

                # Turn off the loop
                run = False

            # Options buttons' down detection
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # left-click has been downed
                # Game settings buttons' down detection
                options.scoretowin_buttons.button_down_detection(options)
                options.startsafterpoint_buttons.button_down_detection()
                options.keyboardsensitivity_buttons.button_down_detection()

                # Miscellaneous buttons' down detection
                btn_pressed = options.miscellaneous_buttons.button_down_detection()
                if btn_pressed != None:  # a button has been pressed
                    if btn_pressed == "sound":
                        sound.play_buttonclick()  # play sound
                        options_buttons = options.miscellaneous_buttons.buttons
                        sound.update(options_buttons)
                    else:
                        for function in btn_switchcase[btn_pressed]:
                            function()

            # Options buttons' over detection
            if event.type == pygame.MOUSEMOTION:
                options.scoretowin_buttons.button_over_detection()
                options.startsafterpoint_buttons.button_over_detection()
                options.keyboardsensitivity_buttons.button_over_detection()
                options.miscellaneous_buttons.button_over_detection()

        # Update display
        redraw_options() 
        clock.tick(window.framerate)

    pygame.quit()
    sys.exit()


def pause_loop():
    # Initialize pause's buttons switchcase
    btn_switchcase = {
        "play": [
            sound.play_buttonclick,  # play sound
            pause.buttons.reset_overdetection,  # reset pause's buttons' over detection
            game_loop  # redirect to game loop
        ],
        "menu": [
            sound.play_buttonclick,  # play sound
            pause.buttons.reset_overdetection,  # reset pause's buttons' over detection
            game_reset,  # reset game variables
            menu_loop   # redirect to menu loop
        ]
    }

    # Loop
    run = True
    while run:
        # Event loop
        for event in pygame.event.get():
            # Quit detection
            if event.type == pygame.QUIT:
                # Update options settings' JSON
                options_settings = {
                    "score_to_win": options.scoretowin_buttons,
                    "who_starts_after_a_point": options.startsafterpoint_buttons,
                    "keyboard_sensitivity": options.keyboardsensitivity_buttons,
                    "miscellaneous": options.miscellaneous_buttons
                }
                window.update_optionssettings(options_settings)

                # Turn off the loop
                run = False

            # Pause buttons' down detection
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # left-click has been uped
                btn_pressed = pause.buttons.button_down_detection()
                if btn_pressed != None:
                    for function in btn_switchcase[btn_pressed]:
                        function()

            # Pause buttons' over detection
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
    # Initialize gameover's buttons switchcase
    btn_switchcase = {
        "play": [
            sound.play_buttonclick,  # play sound
            gameover.buttons.reset_rect,  # reset gameover's buttons' rectangles
            gameover.buttons.reset_overdetection,  # reset gameover's buttons' over detection
            game_reset,  # reset game variables
            game_loop  # redirect to game loop
        ],
        "menu": [ 
            sound.play_buttonclick,  # play sound
            gameover.buttons.reset_rect,  # reset gameover's buttons' rectangles
            gameover.buttons.reset_overdetection,  # reset gameover's buttons' over detection
            game_reset,  # reset game variables
            menu_loop  # redirect to menu loop
        ]
    }

    # Loop
    run = True
    while run:
        # Event loop
        for event in pygame.event.get():
            # Quit detection
            if event.type == pygame.QUIT:
                # Update options settings' JSON
                options_settings = {
                    "score_to_win": options.scoretowin_buttons,
                    "who_starts_after_a_point": options.startsafterpoint_buttons,
                    "keyboard_sensitivity": options.keyboardsensitivity_buttons,
                    "miscellaneous": options.miscellaneous_buttons
                }
                window.update_optionssettings(options_settings)

                # Turn off the loop
                run = False

            # GameOver buttons' down detection
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                btn_pressed = gameover.buttons.button_down_detection()
                if btn_pressed != None:  # a button has been pressed
                    if btn_pressed == "options":
                        gameover.buttons.reset_overdetection()  # reset gameover's buttons' over detection
                        options_loop("gameover")  # redirect to options' loop
                    else:
                        for function in btn_switchcase[btn_pressed]:
                            function()

            # GameOver buttons' over detection
            if event.type == pygame.MOUSEMOTION:
                gameover.buttons.button_over_detection()

        # Update display
        redraw_gameover()
        clock.tick(window.framerate)
    
    pygame.quit()
    sys.exit()


# Execute --------------------------------------------------------- #
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

    # Initialize windows
    menu = Menu()
    gamemode = GameMode()
    game = Game()
    options = Options()
    pause = Pause()
    gameover = GameOver()

    # Initialize audio
    options_buttons = options.miscellaneous_buttons.buttons
    sound = Sound(options_buttons)

    # Initialize paddle
    sensitivity = options.keyboardsensitivity_buttons.get_sensitivity_value()
    paddle_positions = {
        "left": [10, (window.rect.height // 2 - Paddle.height // 2)],
        "right": [
            (window.rect.width - 10 - Paddle.width), 
            (window.rect.height // 2 - Paddle.height // 2)
        ]
    }
    paddles = {
        "left": Paddle(sensitivity, paddle_positions["left"]),
        "right": Paddle(sensitivity, paddle_positions["right"])
    }

    # Initialize ball
    ball = Ball()

    # Execute
    menu_loop()
