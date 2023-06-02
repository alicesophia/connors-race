import pygame
from random import randint


class Enemy(pygame.sprite.Sprite):

    def __init__(self, name, config):
        super().__init__()
        self.config = config

        if name == "tower":
            self.enemy = [
                pygame.transform.scale(self.config.enemy_tower[0], (self.config.width * 0.05, self.config.height * 0.1)),
                pygame.transform.scale(self.config.enemy_tower[1], (self.config.width * 0.05, self.config.height * 0.1)),
                pygame.transform.scale(self.config.enemy_tower[2], (self.config.width * 0.05, self.config.height * 0.1)),
                pygame.transform.scale(self.config.enemy_tower[3], (self.config.width * 0.05, self.config.height * 0.1))
            ]
            self.pos_y = self.config.height * 0.7
        elif name == "mine":
            self.enemy = [
                pygame.transform.scale(self.config.enemy_mine[0], (self.config.width * 0.05, self.config.height * 0.08)),
                pygame.transform.scale(self.config.enemy_mine[1], (self.config.width * 0.05, self.config.height * 0.08)),
                pygame.transform.scale(self.config.enemy_mine[2], (self.config.width * 0.05, self.config.height * 0.08)),
                pygame.transform.scale(self.config.enemy_mine[3], (self.config.width * 0.05, self.config.height * 0.08))
            ]
            self.pos_y = self.config.height * 0.7
        else:
            self.enemy = [
                pygame.transform.scale(self.config.enemy_drone[0], (self.config.width * 0.048, self.config.height * 0.08)),
                pygame.transform.scale(self.config.enemy_drone[1], (self.config.width * 0.048, self.config.height * 0.08)),
                pygame.transform.scale(self.config.enemy_drone[2], (self.config.width * 0.048, self.config.height * 0.08)),
                pygame.transform.scale(self.config.enemy_drone[3], (self.config.width * 0.048, self.config.height * 0.08))
            ]
            self.pos_y = self.config.height * 0.53

        self.index = 0
        self.image = self.enemy[self.index]
        self.rect = self.image.get_rect(midbottom = (randint(self.config.width * 1.125, self.config.width * 1.375), self.pos_y))

    def enemy_animation(self):
        self.rect.x -= (self.config.width * 0.005) + (self.config.score * 0.05)
        self.index += 0.07
        if self.index >= len(self.enemy):
            self.index = 0
        self.image = self.enemy[int(self.index)]

    def enemy_kill(self):
        if self.rect.x <= -(self.config.height * 0.1):
            self.kill()

    def update(self):
        self.enemy_animation()
        self.enemy_kill()
