import pygame
import sys
from stickman import StickMan
from player_2 import Player2
from settings import Settings
from ground import Ground


class StickManFight:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        # Screen variables
        self.screen_height, self.screen_width = 540, 960
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("StickMan Fight")
        self.background = pygame.image.load('assets/bg.jpg')

        # Instances
        self.stickman = StickMan(self)
        self.player2 = Player2(self)
        self.settings = Settings()

        # Sprites
        self.sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.sprites.add(self.stickman)
        self.sprites.add(self.player2)
        self.ground = Ground(0, self.screen_height-40, self.screen_width, 40)
        self.platforms.add(self.ground)
        self.sprites.add(self.ground)

        self.clock = pygame.time.Clock()

    def run_game(self):
        """The main loop of the game."""
        while True:
            self.clock.tick(self.settings.fps)
            self.check_events()
            self.stickman.update(self)
            self.player2.update(self)
            print(self.stickman.energy_balls)

            self.update_screen()

    def check_events(self):
        """Keep track of pressed keys."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and not self.stickman.falling and not self.stickman.jumping:
                    self.stickman.jump()
                elif event.key == pygame.K_UP and not self.player2.falling and not self.player2.jumping:
                    self.player2.jump()
                elif event.key == pygame.K_e and not self.stickman.punching:
                    self.stickman.punch()
                elif event.key == pygame.K_KP1 and not self.player2.punching:
                    self.player2.punch()
                elif event.key == pygame.K_q and not self.stickman.kicking:
                    self.stickman.kick()
                elif event.key == pygame.K_KP2 and not self.player2.kicking:
                    self.player2.kick()
                elif event.key == pygame.K_r and not self.stickman.doing_energy_ball and not self.stickman.jumping and not self.stickman.falling:
                    self.stickman.energy_ball()
            self.stickman.check_key_ups(event)
            self.player2.check_key_ups(event)

    def update_screen(self):
        self.screen.blit(self.background, (0, 0))
        self.sprites.draw(self.screen)
        if self.stickman.energy_balls:
            self.stickman.current_energy_ball.blitme()
        # self.stickman.energy_balls.draw(self.screen)
        self.stickman.update_health()
        self.player2.update_health()
        # pygame.draw.rect(self.screen, (255, 0, 0), self.player2.rect, 1)
        pygame.draw.rect(self.screen, (255, 0, 0), self.stickman.rect, 1)

        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = StickManFight()
    ai.run_game()
