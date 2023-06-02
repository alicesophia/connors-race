import pygame
from random import randint


class Enemy(pygame.sprite.Sprite):

    def __init__(self, type, config):
        super().__init__()
        self.config = config

        if type == "snail":
            self.enemy = [
                pygame.image.load("../assets/graphics/snail/snail1.png"),
                pygame.image.load("../assets/graphics/snail/snail2.png")
            ]
            self.pos_y = self.config.height * 0.7
        else:
            self.enemy = [
                pygame.image.load("../assets/graphics/fly/fly1.png"),
                pygame.image.load("../assets/graphics/fly/fly2.png")
            ]
            self.pos_y = self.config.height * 0.54

        self.index = 0
        self.image = self.enemy[self.index]
        self.rect = self.image.get_rect(midbottom = (randint(self.config.width * 1.125, self.config.width * 1.375), self.pos_y))

    def enemy_animation(self):
        self.rect.x -= (self.config.width * 0.005) + (self.config.score * 0.05)
        self.index += 0.1
        if self.index >= len(self.enemy):
            self.index = 0
        self.image = self.enemy[int(self.index)]

    def enemy_kill(self):
        if self.rect.x <= -(self.config.height * 0.1):
            self.kill()

    def update(self):
        self.enemy_animation()
        self.enemy_kill()
