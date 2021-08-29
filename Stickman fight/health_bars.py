import pygame


class HealthBar:
    def __init__(self, ai_game, stickman):
        # Health Bar
        self.ai_game = ai_game
        self.stickman = stickman
        self.health_bar_image = pygame.Surface((100, 20))
        self.health_bar_rect = self.health_bar_image.get_rect()

        # Health Bar Border
        self.border_image = pygame.Surface((102, 22))
        self.border_rect = self.border_image.get_rect()

        # Health Bar background
        self.bg_image = pygame.Surface((100, 20))
        self.bg_rect = self.bg_image.get_rect()

    def blitme(self):
        if self.stickman.health >= 0:
            self.health_bar_rect.width = self.stickman.health
        elif self.stickman.health < 0:
            self.health_bar_rect.width = 0
        if self.stickman.facing_right:
            self.health_bar_rect.x, self.health_bar_rect.y = self.stickman.rect.x, self.stickman.rect.y - 30
            self.border_rect.x, self.border_rect.y = self.health_bar_rect.x, self.health_bar_rect.y
            self.bg_rect.x, self.bg_rect.y = self.health_bar_rect.x, self.health_bar_rect.y
        elif self.stickman.facing_left and not self.stickman.punching and not self.stickman.kicking:
            self.health_bar_rect.x, self.health_bar_rect.y = self.stickman.rect.x - 20, self.stickman.rect.y - 30
            self.border_rect.x, self.border_rect.y = self.health_bar_rect.x, self.health_bar_rect.y
            self.bg_rect.x, self.bg_rect.y = self.health_bar_rect.x, self.health_bar_rect.y

        pygame.draw.rect(self.ai_game.screen, (0, 0, 0), self.border_rect, 3)
        pygame.draw.rect(self.ai_game.screen, (255, 0, 0), self.bg_rect)
        pygame.draw.rect(self.ai_game.screen, (0, 255, 0), self.health_bar_rect)
