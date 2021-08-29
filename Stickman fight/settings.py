import pygame


class Settings:
    """A class that contains all of the settings for the game."""
    def __init__(self):
        self.fps = 20

        # Stickman Settings
        self.walk_speed = 7
        self.screen_height, self.screen_width = 540, 960
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.gravity = 20
        self.jump_limit = 200
        self.punch_time = 1000
        self.punch_damage = 10
        self.kick_damage = 15
        self.energy_ball_damage = 35
