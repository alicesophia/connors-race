import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.index = 0
        self.walk = [
            pygame.image.load("../assets/graphics/player/player_walk_1.png").convert_alpha(),
            pygame.image.load("../assets/graphics/player/player_walk_2.png").convert_alpha()
        ]
        self.jump = pygame.image.load("../assets/graphics/player/player_jump.png")
        self.jump_sound = pygame.mixer.Sound("../assets/audio/jump.mp3")
        self.jump_sound.set_volume(0.2)
        self.image = self.walk[self.index]
        self.rect = self.image.get_rect(midbottom = (80, 300))
        self.gravity = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.jump_sound.play()
            self.gravity = -20

    def player_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def player_animation(self):
        if self.rect.bottom < 300:
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
