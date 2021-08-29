import pygame


class Animations:
    """Overall class that contains stickman's movement sprites."""
    def __init__(self):
        # self.stick_info = StickMan()
        self.current_sprite = 0
        # Idle
        self.idle_ani = []
        self.idle_ani.append(pygame.image.load('assets/animations/idle animation/idle animation00.png').convert())
        self.idle_ani.append(pygame.image.load('assets/animations/idle animation/idle animation01.png').convert())
        self.idle_ani.append(pygame.image.load('assets/animations/idle animation/idle animation02.png').convert())
        self.idle_ani.append(pygame.image.load('assets/animations/idle animation/idle animation03.png').convert())
        self.idle_ani.append(pygame.image.load('assets/animations/idle animation/idle animation04.png').convert())
        self.idle_ani.append(pygame.image.load('assets/animations/idle animation/idle animation05.png').convert())
        self.idle_ani.append(pygame.image.load('assets/animations/idle animation/idle animation06.png').convert())
        self.idle_ani.append(pygame.image.load('assets/animations/idle animation/idle animation07.png').convert())
        self.idle_ani.append(pygame.image.load('assets/animations/idle animation/idle animation08.png').convert())
        self.idle_ani.append(pygame.image.load('assets/animations/idle animation/idle animation09.png').convert())
        self.idle_ani.append(pygame.image.load('assets/animations/idle animation/idle animation10.png').convert())
        self.idle_ani.append(pygame.image.load('assets/animations/idle animation/idle animation11.png').convert())
        self.idle_ani.append(pygame.image.load('assets/animations/idle animation/idle animation12.png').convert())
        self.idle_ani.append(pygame.image.load('assets/animations/idle animation/idle animation13.png').convert())
        self.idle_ani.append(pygame.image.load('assets/animations/idle animation/idle animation14.png').convert())
        self.idle_ani.append(pygame.image.load('assets/animations/idle animation/idle animation15.png').convert())
        self.idle_ani.append(pygame.image.load('assets/animations/idle animation/idle animation16.png').convert())
        self.idle_ani.append(pygame.image.load('assets/animations/idle animation/idle animation17.png').convert())
        self.idle_rect = self.idle_ani[0].get_rect()

        # Walking
        self.walking_ani = []
        self.walking_ani.append(pygame.image.load('assets/animations/walking/walking0.png').convert())
        self.walking_ani.append(pygame.image.load('assets/animations/walking/walking1.png').convert())
        self.walking_ani.append(pygame.image.load('assets/animations/walking/walking2.png').convert())
        self.walking_ani.append(pygame.image.load('assets/animations/walking/walking3.png').convert())
        self.walking_ani.append(pygame.image.load('assets/animations/walking/walking4.png').convert())

        # Jumping
        self.jumping_ani = pygame.image.load('assets/animations/jump/jumping0.png')

        # Crouching
        self.crouch_ani = pygame.image.load('assets/animations/crouching0.png')
        self.crouch_rect = self.crouch_ani.get_rect()

        # Punching
        self.punch_ani = []
        self.punch_ani.append(pygame.image.load('assets/animations/punch/punch0.png').convert())
        self.punch_ani.append(pygame.image.load('assets/animations/punch/punch1.png').convert())
        self.punch_ani.append(pygame.image.load('assets/animations/punch/punch2.png').convert())
        self.punch_ani.append(pygame.image.load('assets/animations/punch/punch3.png').convert())
        self.punch_rect = self.punch_ani[-1].get_rect()

        # Kick
        self.kick_ani = []
        self.kick_ani.append(pygame.image.load('assets/animations/kick/kick0.png').convert())
        self.kick_ani.append(pygame.image.load('assets/animations/kick/kick01.png').convert())
        self.kick_ani.append(pygame.image.load('assets/animations/kick/kick02.png').convert())
        self.kick_ani.append(pygame.image.load('assets/animations/kick/kick03.png').convert())
        self.kick_ani.append(pygame.image.load('assets/animations/kick/kick04.png').convert())
        self.kick_ani.append(pygame.image.load('assets/animations/kick/kick05.png').convert())
        self.kick_ani.append(pygame.image.load('assets/animations/kick/kick06.png').convert())
        self.kick_ani.append(pygame.image.load('assets/animations/kick/kick07.png').convert())
        self.kick_ani.append(pygame.image.load('assets/animations/kick/kick08.png').convert())
        self.kick_ani.append(pygame.image.load('assets/animations/kick/kick09.png').convert())
        self.kick_ani.append(pygame.image.load('assets/animations/kick/kick10.png').convert())
        self.kick_rect = self.kick_ani[4].get_rect()

        # Energy Ball
        self.energy_ball_ani = []
        self.energy_ball_ani.append(pygame.image.load('assets/animations/energy ball/energy ball00.png').convert())
        self.energy_ball_ani.append(pygame.image.load('assets/animations/energy ball/energy ball01.png').convert())
        self.energy_ball_ani.append(pygame.image.load('assets/animations/energy ball/energy ball02.png').convert())
        self.energy_ball_ani.append(pygame.image.load('assets/animations/energy ball/energy ball03.png').convert())
        self.energy_ball_ani.append(pygame.image.load('assets/animations/energy ball/energy ball04.png').convert())
        self.energy_ball_ani.append(pygame.image.load('assets/animations/energy ball/energy ball05.png').convert())
        self.energy_ball_ani.append(pygame.image.load('assets/animations/energy ball/energy ball06.png').convert())
        self.energy_ball_ani.append(pygame.image.load('assets/animations/energy ball/energy ball07.png').convert())
        self.energy_ball_ani.append(pygame.image.load('assets/animations/energy ball/energy ball08.png').convert())
        self.energy_ball_ani.append(pygame.image.load('assets/animations/energy ball/energy ball09.png').convert())
        self.energy_ball_ani.append(pygame.image.load('assets/animations/energy ball/energy ball10.png').convert())
        self.energy_ball_ani.append(pygame.image.load('assets/animations/energy ball/energy ball11.png').convert())
        self.energy_ball_ani.append(pygame.image.load('assets/animations/energy ball/energy ball12.png').convert())
        self.energy_ball_ani.append(pygame.image.load('assets/animations/energy ball/energy ball13.png').convert())
        self.energy_ball_ani.append(pygame.image.load('assets/animations/energy ball/energy ball14.png').convert())
        self.energy_ball_ani.append(pygame.image.load('assets/animations/energy ball/energy ball15.png').convert())
        self.energy_ball_ani.append(pygame.image.load('assets/animations/energy ball/energy ball16.png').convert())
        self.energy_ball_ani.append(pygame.image.load('assets/animations/energy ball/energy ball17.png').convert())
        self.energy_ball_ani.append(pygame.image.load('assets/animations/energy ball/energy ball18.png').convert())
        self.energy_ball_ani.append(pygame.image.load('assets/animations/energy ball/energy ball19.png').convert())
        self.energy_ball_ani.append(pygame.image.load('assets/animations/energy ball/energy ball20.png').convert())
        self.energy_ball_ani.append(pygame.image.load('assets/animations/energy ball/energy ball21.png').convert())
        self.energy_ball_ani.append(pygame.image.load('assets/animations/energy ball/energy ball22.png').convert())
        self.energy_ball_ani.append(pygame.image.load('assets/animations/energy ball/energy ball23.png').convert())
        self.energy_ball_ani.append(pygame.image.load('assets/animations/energy ball/energy ball24.png').convert())
        self.energy_ball_ani.append(pygame.image.load('assets/animations/energy ball/energy ball25.png').convert())
        self.energy_ball_rect = self.energy_ball_ani[18].get_rect()

        self.ball_buildup = []
        self.ball_buildup.append(pygame.image.load('assets/animations/energyball_buildup/energyball_buildup0.png')
                                 .convert())
        self.ball_buildup.append(pygame.image.load('assets/animations/energyball_buildup/energyball_buildup1.png')
                                 .convert())
        self.ball_buildup.append(pygame.image.load('assets/animations/energyball_buildup/energyball_buildup2.png')
                                 .convert())
        self.ball_buildup.append(pygame.image.load('assets/animations/energyball_buildup/energyball_buildup3.png')
                                 .convert())
        self.ball_buildup.append(pygame.image.load('assets/animations/energyball_buildup/energyball_buildup4.png')
                                 .convert())
        self.ball_buildup.append(pygame.image.load('assets/animations/energyball_buildup/energyball_buildup5.png')
                                 .convert())
        self.ball_buildup.append(pygame.image.load('assets/animations/energyball_buildup/energyball_buildup6.png')
                                 .convert())
        self.ball_buildup.append(pygame.image.load('assets/animations/energyball_buildup/energyball_buildup7.png')
                                 .convert())
        self.ball_buildup.append(pygame.image.load('assets/animations/energyball_buildup/energyball_buildup8.png')
                                 .convert())
