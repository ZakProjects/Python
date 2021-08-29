import pygame
from settings import Settings


class EnergyBall(pygame.sprite.Sprite):
    def __init__(self, stickman, game):
        super().__init__()
        self.settings = Settings()
        self.stickman = stickman
        self.image = self.stickman.animation.ball_buildup[0]
        self.rect = self.image.get_rect()
        self.going_right = False
        self.going_left = False
        if self.stickman.facing_right:
            self.rect.x = self.stickman.rect.x + self.stickman.rect.w
            self.going_right = True
        elif self.stickman.facing_left:
            self.rect.x = self.stickman.rect.x - 20
            self.going_left = True
        self.rect.y = self.stickman.rect.y + 20
        self.screen = game.screen
        self.screen_rect = game.screen_rect

    def draw_ball(self):
        if self.stickman.doing_energy_ball:
            if 17 >= self.stickman.animation.current_sprite > 8:
                self.image = self.stickman.animation.ball_buildup[self.stickman.animation.current_sprite % 9]
            elif self.stickman.animation.current_sprite > 18:
                self.image = self.stickman.animation.ball_buildup[-1]
            self.image.set_colorkey((255, 255, 255))

    def update_me(self):
        self.draw_ball()
        if not self.stickman.doing_energy_ball:
            if self.going_right:
                self.rect.x += 20
            elif self.going_left:
                self.rect.x -= 20
        if self.rect.left > self.screen_rect.w or self.rect.right < 0:
            self.kill()

    def blitme(self):
        self.screen.blit(self.image, self.rect)
