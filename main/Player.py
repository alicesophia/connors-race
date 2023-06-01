import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, config):
        super().__init__()
        self.config = config
        self.index = 0
        self.walk = [
            pygame.image.load("../assets/graphics/player/player_walk_1.png").convert_alpha(),
            pygame.image.load("../assets/graphics/player/player_walk_2.png").convert_alpha()
        ]
        self.jump = pygame.image.load("../assets/graphics/player/player_jump.png")
        self.image = self.walk[self.index]
        self.rect = self.image.get_rect(midbottom = (self.config.width * 0.1, self.config.height * 0.7))
        self.gravity = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= self.config.height * 0.7:
            self.config.jump_sound.play()
            self.gravity = -(self.config.height * 0.030)

    def player_gravity(self):
        self.gravity += self.config.height * 0.0015
        self.rect.y += self.gravity
        if self.rect.bottom >= self.config.height * 0.7:
            self.rect.bottom = self.config.height * 0.7

    def player_animation(self):
        if self.rect.bottom < self.config.height * 0.7:
            self.image = self.jump
        else:
            self.index += 0.1
            if self.index >= len(self.walk):
                self.index = 0
            self.image = self.walk[int(self.index)]

    def update(self):
        self.player_input()
        self.player_gravity()
        self.player_animation()
