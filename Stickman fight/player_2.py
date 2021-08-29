import pygame

from stickman import StickMan


class Player2(StickMan):
    """Overall class for the 2nd player."""
    def __init__(self, game):
        """Initialize the variables."""
        super().__init__(game)
        self.rect.x = game.screen_rect.width - self.rect.width -18
        self.facing_left = True
        self.facing_right = False

    def check_key_downs(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.rect.x < self.settings.screen_width - self.rect.width - 30:
            self.facing_right = True
            self.facing_left = False
            if not self.jumping and not self.falling:
                self.standing = False
                self.walking = True
            self.walk(1)
        elif keys[pygame.K_LEFT] and self.rect.x > 0:
            self.facing_left = True
            self.facing_right = False
            if not self.jumping and not self.falling:
                self.standing = False
                self.walking = True
            self.walk(-1)
        elif keys[pygame.K_DOWN] and not self.jumping and not self.falling and not self.punching and not self.kicking:
            self.standing = False
            self.walking = False
            self.crouch()

    def check_key_ups(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                if not self.jumping and not self.falling:
                    self.standing = True
            elif event.key == pygame.K_LEFT:
                if not self.jumping and not self.falling:
                    self.standing = True
            elif event.key == pygame.K_DOWN:
                self.standing = True
                self.crouching = False

    def _check_collisions(self, game):
        """Handle collisions between sprites"""
        ground_hit_1 = pygame.sprite.spritecollide(self, game.platforms, False)
        if ground_hit_1:
            self.rect.bottom = ground_hit_1[0].rect.top + 3
            self.vel = 0
            self.falling = False
            self.standing = True
        player_col = pygame.sprite.collide_rect(self, game.stickman)
        if player_col and self.punching and self.animation.current_sprite == 3:
            print("COLLISION!!")
            game.stickman.health -= self.settings.punch_damage

        elif player_col and self.kicking and self.animation.current_sprite == 5:
            print("COLLISION!!")
            game.stickman.health -= self.settings.kick_damage
