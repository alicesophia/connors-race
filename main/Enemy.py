import pygame
from random import randint


class Enemy(pygame.sprite.Sprite):

    def __init__(self, type):
        super().__init__()

        if type == "snail":
            self.enemy = [
                pygame.image.load("../assets/graphics/snail/snail1.png"),
                pygame.image.load("../assets/graphics/snail/snail2.png")
            ]
            self.pos_y = 300
        else:
            self.enemy = [
                pygame.image.load("../assets/graphics/fly/fly1.png"),
                pygame.image.load("../assets/graphics/fly/fly2.png")
            ]
            self.pos_y = 210

        self.index = 0
        self.image = self.enemy[self.index]
        self.rect = self.image.get_rect(midbottom = (randint(900, 1100), self.pos_y))

    def enemy_animation(self):
        self.rect.x -= 6
        self.index += 0.1
        if self.index >= len(self.enemy):
            self.index = 0
        self.image = self.enemy[int(self.index)]

    def enemy_kill(self):
        if self.rect.x <= -100:
            self.kill()

    def update(self):
        self.enemy_animation()
        self.enemy_kill()
