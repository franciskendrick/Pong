from windows import window
from paddle import Paddle
import pygame
import sys


# Redraw
def redraw_game():
    # Background
    display.fill(window.white)
    pygame.draw.rect(display, window.black, window.playable_rect)
    pygame.draw.line(display, window.white, *window.center_line, 10)
    
    # Paddle
    for paddle in paddles.values():
        paddle.draw(display)

    # Blit to Screen ---------------------------------------------- #
    resized_display = pygame.transform.scale(display, win_size)
    win.blit(resized_display, (0, 0))

    pygame.display.update()


# Loop
def game_loop():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        redraw_game()
        clock.tick(window.framerate)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    pygame.init()

    # Initialize Window
    win_size = (
        int(window.rect.width * window.enlarge),
        int(window.rect.height * window.enlarge))
    win = pygame.display.set_mode(win_size, 32)
    display = pygame.Surface(window.rect.size)
    pygame.display.set_caption("Pong!")
    clock = pygame.time.Clock()

    # Initialize Paddle
    paddles = {
        "left_paddle": Paddle(
            10, window.rect.h // 2 - Paddle.HEIGHT // 2),
        "right_paddle": Paddle(
            window.rect.w - 10 - Paddle.WIDTH, 
            window.rect.h // 2 - Paddle.HEIGHT // 2)
    }

    # Execute
    game_loop()
