import pygame
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 
        "..", "..", 
        "resources", "audio"
        )
    )


class Sound:
    # Initialize -------------------------------------------------- #
    def __init__(self, options_buttons):
        # Button click audio
        self.buttonclick_sound = pygame.mixer.Sound(
            f"{resources_path}/ES_Switch Click 5 - SFX Producer.mp3")

        self.buttonclick_sound.set_volume(0.35)

        # Window redirect audios
        self.pause_sound = pygame.mixer.Sound(
            f"{resources_path}/envatoelements_pause.mp3")
        self.win_sound = pygame.mixer.Sound(
            f"{resources_path}/mixkit_win.mp3")

        self.win_sound.set_volume(0.25)

        # Game audios
        self.ballcollision_sound = pygame.mixer.Sound(
            f"{resources_path}/mixkit_ballcollision.mp3")
        self.missedshot_sound = pygame.mixer.Sound(
            f"{resources_path}/mixkit_missedshot.mp3")

        self.ballcollision_sound.set_volume(0.5)
        self.missedshot_sound.set_volume(0.5)

        # Is playing variable
        self.playing = not options_buttons["sound"][1]

    # Play -------------------------------------------------------- #
    def play_buttonclick(self):
        if self.playing:
            self.buttonclick_sound.play()
    
    def play_pause(self):
        if self.playing:
            self.pause_sound.play()
    
    def play_win(self):
        if self.playing:
            self.win_sound.play()
    
    def play_ballcollision(self):
        if self.playing:
            self.ballcollision_sound.play()

    def play_missedshot(self):
        if self.playing:
            self.missedshot_sound.play()

    # Update ------------------------------------------------------ #
    def update(self, options_buttons):
        self.playing = options_buttons["sound"][1]
