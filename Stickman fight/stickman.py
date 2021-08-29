import pygame
from animations import Animations
from settings import Settings
from health_bars import HealthBar
from energy_ball import EnergyBall


class StickMan(pygame.sprite.Sprite):
    """Overall class to handle the behaviour and assets of
    a stickman character
    """

    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        # Instances
        self.animation = Animations()
        self.settings = Settings()
        self.health_bar = HealthBar(game, self)
        self.game = game

        # Bools
        self.standing = True
        self.facing_right = True
        self.facing_left = False
        self.walking = False
        self.jumping = False
        self.falling = True
        self.crouching = False
        self.punching = False
        self.is_hit = False
        self.kicking = False
        self.doing_energy_ball = False

        # Character
        self.image = self.animation.idle_ani[self.animation.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.y = 100
        self.health = 100
        self.energy = 100

        self.vel = 0

        # Health
        self.health = 100

        self.energy_balls = pygame.sprite.Group()

    def walk(self, direction):
        """A function to handle the stickman's walking behaviour."""
        if not self.doing_energy_ball:
            self.rect.x += self.settings.walk_speed * direction
        # Handle animation
        if not self.jumping and not self.falling and not self.punching and not self.kicking and not\
                self.doing_energy_ball:
            self.animate(self.animation.walking_ani)

    def idle(self):
        if self.standing and not self.punching and not self.kicking and not self.doing_energy_ball:
            self.animate(self.animation.idle_ani)

    def jump(self):
        """Handle the jump behaviour."""
        self.standing = False
        self.punching = False
        self.jumping = True
        self.falling = False
        self.current_y = float(self.rect.y)
        self.vel = -50

    def _handle_jumping(self):
        if self.falling:
            # Draw animation
            if self.facing_right:
                self.image = self.animation.jumping_ani
            elif self.facing_left:
                self.image = pygame.transform.flip(self.animation.jumping_ani, True, False)
            self.image.set_colorkey((255, 255, 255))

            self.vel = 1.1
            self.rect.y += self.settings.gravity * self.vel
        elif self.jumping:
            if self.rect.y > self.current_y - self.settings.jump_limit:
                # Draw animation
                if self.facing_right:
                    self.image = self.animation.jumping_ani
                elif self.facing_left:
                    self.image = pygame.transform.flip(self.animation.jumping_ani, True, False)
                self.image.set_colorkey((255, 255, 255))

                self.vel -= 1
                self.rect.y += self.vel

            else:
                self.falling = True
                self.jumping = False

    def check_key_downs(self):
        # Key Downs
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and self.rect.x < self.settings.screen_width - self.rect.width - 30:
            self.facing_right = True
            self.facing_left = False
            if not self.jumping and not self.falling:
                self.standing = False
                self.walking = True
            self.walk(1)
        elif keys[pygame.K_a] and self.rect.x > 0:
            self.facing_left = True
            self.facing_right = False
            if not self.jumping and not self.falling:
                self.standing = False
                self.walking = True
            self.walk(-1)
        elif keys[pygame.K_s] and not self.jumping and not self.falling and not self.punching and not self.kicking\
                and not self.doing_energy_ball:
            self.standing = False
            self.walking = False
            self.crouch()

    def check_key_ups(self, event):
        # Key UPS
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                if not self.jumping and not self.falling:
                    self.standing = True
                    self.walking = False
            elif event.key == pygame.K_a:
                if not self.jumping and not self.falling:
                    self.standing = True
                    self.walking = False
            elif event.key == pygame.K_s:
                self.standing = True
                self.crouching = False

    def crouch(self):
        self.rect.y = 384  # 360
        self.crouching = True
        if self.facing_right:
            self.image = self.animation.crouch_ani
        elif self.facing_left:
            self.image = pygame.transform.flip(self.animation.crouch_ani, True, False)
        self.image.set_colorkey((255, 255, 255))

    def punch(self):
        if self.health >= 0 and not self.crouching and not self.kicking and not self.doing_energy_ball:
            self.animation.current_sprite = 0
            self.standing = False
            self.punching = True

    def kick(self):
        if self.health >= 0 and not self.crouching and not self.punching and not self.doing_energy_ball:
            self.animation.current_sprite = 0
            self.standing = False
            self.kicking = True

    def animate_kick(self):
        self.animation.current_sprite += 1
        if self.animation.current_sprite == len(self.animation.kick_ani):
            self.animation.current_sprite = 0
            self.kicking = False
            self.standing = True
            if self.facing_left:
                self.rect.x += self.animation.kick_rect.width - self.animation.idle_rect.w - 50
        if self.facing_right:
            self.image = self.animation.kick_ani[self.animation.current_sprite]
        elif self.facing_left:
            self.image = pygame.transform.flip(self.animation.kick_ani[self.animation.current_sprite],
                                               True, False)
            if self.animation.current_sprite == 5:
                self.rect.x -= self.animation.kick_rect.width - self.animation.idle_rect.w - 50
        self.image.set_colorkey((255, 255, 255))

    def animate_punch(self):
        self.animation.current_sprite += 1
        if self.animation.current_sprite == len(self.animation.punch_ani):
            self.animation.current_sprite = 0
            self.punching = False
            self.standing = True
            if self.facing_left:
                self.rect.x += self.animation.punch_rect.width - self.animation.idle_rect.w
        if self.facing_right:
            self.image = self.animation.punch_ani[self.animation.current_sprite]
        elif self.facing_left:
            self.image = pygame.transform.flip(self.animation.punch_ani[self.animation.current_sprite],
                                               True, False)
            if self.animation.current_sprite == 3:
                self.rect.x -= self.animation.punch_rect.width - self.animation.idle_rect.w
        self.image.set_colorkey((255, 255, 255))

    def energy_ball(self):
        if self.health >= 0 and not self.kicking and not self.punching and not self.crouching and not self.energy_balls:
            self.animation.current_sprite = 0
            self.doing_energy_ball = True
            self.standing = False

    def animate_energy_ball(self):
        self.animation.current_sprite += 1
        if self.animation.current_sprite == len(self.animation.energy_ball_ani):
            self.doing_energy_ball = False
            self.animation.current_sprite = 0
            self.standing = True
        if self.facing_right:
            self.image = self.animation.energy_ball_ani[self.animation.current_sprite]
        elif self.facing_left:
            self.image = pygame.transform.flip(self.animation.energy_ball_ani[self.animation.current_sprite],
                                               True, False)
            #if self.animation.current_sprite in range(5, 22):
            #    self.rect.width = self.animation.energy_ball_rect.width - 70
            #    self.rect.x -= 2.5
        if self.animation.current_sprite == 8:
            self.current_energy_ball = EnergyBall(self, self.game)
            self.energy_balls.add(self.current_energy_ball)
        self.image.set_colorkey((255, 255, 255))

    def animate(self, ani_list):
        self.animation.current_sprite += 1
        if self.animation.current_sprite >= len(ani_list):
            self.animation.current_sprite = 0
            self.punching = False
        if self.facing_right:
            self.image = ani_list[self.animation.current_sprite]
        elif self.facing_left:
            self.image = pygame.transform.flip(ani_list[self.animation.current_sprite],
                                               True, False)
        self.image.set_colorkey((255, 255, 255))

    def _check_collisions(self, game):
        """Handle collisions between sprites"""
        ground_hit_1 = pygame.sprite.spritecollide(self, game.platforms, False)
        if ground_hit_1:
            self.rect.bottom = ground_hit_1[0].rect.top + 3
            self.vel = 0
            self.falling = False
            self.standing = True
        player_col = pygame.sprite.collide_mask(self, game.player2)
        if player_col and self.punching and self.animation.current_sprite == 3:
            print("COLLISION!!")
            game.player2.health -= self.settings.punch_damage
        elif player_col and self.kicking and self.animation.current_sprite == 5:
            print("COLLISION!!")
            game.player2.health -= self.settings.kick_damage
        energy_coll = pygame.sprite.spritecollide(game.player2, self.energy_balls, True)
        if energy_coll:
            game.player2.health -= self.settings.energy_ball_damage

    def update_health(self):
        self.health_bar.blitme()

    def update(self, game):
        # self.rect.height = self.image.get_rect().height
        self.rect.width = self.image.get_rect().width
        self.mask = pygame.mask.from_surface(self.image)
        self._handle_jumping()
        self._check_collisions(game)
        self.check_key_downs()
        if self.punching:
            self.animate_punch()
        if self.kicking:
            self.animate_kick()
        if self.doing_energy_ball:
            self.animate_energy_ball()
        if self.energy_balls:
            self.current_energy_ball.update_me()
        if self.health <= 0:
            self.kill()
        self.idle()
