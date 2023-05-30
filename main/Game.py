import pygame
from Player import Player
from Enemy import Enemy
from random import choice


class Game:

    def __init__(self, config):
        super().__init__()
        self.config = config
        self.score = 0
        self.start_time = 0
        pygame.time.set_timer(self.config.enemy_timer, 1500)

        # Criação dos sprites
        self.player_group = pygame.sprite.GroupSingle()
        self.player_group.add(Player(config))
        self.enemy_group = pygame.sprite.Group()

        # Criação do cenário
        self.sky_surface = pygame.image.load("../assets/graphics/sky.png").convert_alpha()
        self.ground_surface = pygame.image.load("../assets/graphics/ground.png").convert_alpha()

        # Tela do game over
        self.player_stand = pygame.image.load("../assets/graphics/player/player_stand.png").convert_alpha()
        self.player_stand = pygame.transform.rotozoom(self.player_stand, 0, 2)
        self.player_stand_rect = self.player_stand.get_rect(center = (400, 200))

        self.title_text = config.font.render("Connor's Race", False, (64, 64, 64))
        self.title_text_rect = self.title_text.get_rect(center = (400, 50))

        self.hint_text = config.font.render("Aperte espaço para começar".encode(), False, (64, 64, 64))
        self.hint_text_rect = self.hint_text.get_rect(center = (400, 350))



    def update(self):
        for event in self.config.events:
            if not self.config.game_over and self.config.state != 'pause':
                if event.type == self.config.enemy_timer:
                    print("TIMER")
                    self.enemy_group.add(Enemy(choice(["snail", "snail", "snail", "fly"])))

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.config.game_over:
                    self.config.game_over = False
                    self.start_time = int(pygame.time.get_ticks() / 1000)

        if not self.config.game_over:
            # print("JOGO RODANDO")
            # Cenário
            self.config.screen.blit(self.sky_surface, (0, 0))
            self.config.screen.blit(self.sky_surface, (700, 0))

            self.config.screen.blit(self.ground_surface, (0, 300))
            self.config.screen.blit(self.ground_surface, (700, 300))
            self.score = self.display_score()

            # Player
            self.player_group.draw(self.config.screen)
            self.player_group.update()

            # Inimigos
            self.enemy_group.draw(self.config.screen)
            self.enemy_group.update()

            # Colisões
            self.config.game_over = self.player_collision()
        else:
            # Tela do game over
            self.enemy_group.empty()
            self.config.screen.fill((94, 129, 162))
            self.config.screen.blit(self.player_stand, self.player_stand_rect)
            self.config.screen.blit(self.title_text, self.title_text_rect)

            # Mensagem do game over
            if self.score == 0:
                self.config.screen.blit(self.hint_text, self.hint_text_rect)
            else:
                score_message = self.config.font.render(f'Game over! Seu score foi: {self.score}', False, (64, 64, 64))
                score_message_rect = score_message.get_rect(center = (400, 350))
                self.config.screen.blit(score_message, score_message_rect)

    def display_score(self):
        current_time = int(pygame.time.get_ticks() / 1000) - self.start_time
        score_surface = self.config.font.render(f"Score: {current_time}", False, (64, 64, 64))
        score_rect = score_surface.get_rect(center = (400, 50))
        self.config.screen.blit(score_surface, score_rect)
        return current_time

    def player_collision(self):
        return pygame.sprite.spritecollide(self.player_group.sprite, self.enemy_group, False)
