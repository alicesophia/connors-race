import pygame
from Player import Player
from Enemy import Enemy
from random import choice


class Game:

    def __init__(self, config):
        super().__init__()
        self.config = config

        pygame.time.set_timer(self.config.enemy_timer, 1800)

        # Criação dos sprites
        self.player_group = pygame.sprite.GroupSingle()
        self.player_group.add(Player(config))
        self.enemy_group = pygame.sprite.Group()

        # Criação do cenário
        self.background = pygame.transform.scale(self.config.game_scenario, (self.config.width, self.config.height * 0.7))
        self.ground = pygame.transform.scale(self.config.game_ground, (self.config.width, self.config.height * 0.3))

    def update(self):
        for event in self.config.events:
            if not self.config.game_over and self.config.state != 'pause':
                if event.type == self.config.enemy_timer:
                    self.enemy_group.add(Enemy(choice(["mine", "mine", "tower", "drone"]), self.config))

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.config.game_over:
                    self.config.game_over = False
                    self.config.start_time = int(pygame.time.get_ticks() / 1000)

        if not self.config.game_over:
            # Cenário
            self.config.screen.blit(self.background, (0, 0))
            self.config.screen.blit(self.ground, (0, self.config.height * 0.7))
            self.config.score = self.display_score()

            # Player
            self.player_group.draw(self.config.screen)
            self.player_group.update()

            # Inimigos
            self.enemy_group.draw(self.config.screen)
            self.enemy_group.update()

            # Colisões
            if self.player_collision():
                self.config.game_over = True
                self.config.death_sound.play()
            else:
                self.config.game_over = False
        else:
            # Tela do game over
            self.enemy_group.empty()
            self.config.screen.blit(self.background, (0, 0))
            self.config.screen.blit(self.ground, (0, self.config.height * 0.7))
            self.config.screen.fill((94, 129, 162, 255), None, pygame.BLEND_RGBA_MULT)

            # Mensagem do game over
            if self.config.score == 0:
                dialog = pygame.transform.scale(self.config.yellow_dialog, (self.config.width * 0.18, self.config.height * 0.1))
                dialog_rect = dialog.get_rect(center = (self.config.width * 0.5, self.config.height * 0.25))

                dialog_text = self.config.font.render("Como jogar?", True, (171, 52, 31))
                dialog_text_rect = dialog_text.get_rect(center = (self.config.width * 0.5, self.config.height * 0.25))

                space_button = pygame.transform.scale(self.config.space_button, (self.config.width * 0.09, self.config.height * 0.14))
                space_button_rect = space_button.get_rect(center = (self.config.width * 0.5, self.config.height * 0.37))
                space_text = self.config.font.render("Pular", True, (171, 52, 31))
                space_text_rect = space_text.get_rect(center = (self.config.width * 0.5, self.config.height * 0.45))

                esc_button = pygame.transform.scale(self.config.esc_button, (self.config.width * 0.08, self.config.height * 0.13))
                esc_button_rect = esc_button.get_rect(center = (self.config.width * 0.5, self.config.height * 0.63))
                esc_text = self.config.font.render("Pausar", True, (171, 52, 31))
                esc_text_rect = esc_text.get_rect(center = (self.config.width * 0.5, self.config.height * 0.73))

                self.config.screen.blit(dialog, dialog_rect)
                self.config.screen.blit(dialog_text, dialog_text_rect)
                self.config.screen.blit(esc_button, esc_button_rect)
                self.config.screen.blit(esc_text, esc_text_rect)
                self.config.screen.blit(space_button, space_button_rect)
                self.config.screen.blit(space_text, space_text_rect)
            else:
                dialog = pygame.transform.scale(self.config.yellow_dialog, (self.config.width * 0.45, self.config.height * 0.1))
                dialog_rect = dialog.get_rect(center = (self.config.width * 0.5, self.config.height * 0.5))

                score_message = self.config.font.render(f'Game over! Seu score foi: {self.config.score}', False, (171, 52, 31))
                score_message_rect = score_message.get_rect(center = (self.config.width * 0.5, self.config.height * 0.5))

                self.config.screen.blit(dialog, dialog_rect)
                self.config.screen.blit(score_message, score_message_rect)

    def display_score(self):
        current_score = int(pygame.time.get_ticks() / 1000) - self.config.start_time

        dialog = pygame.transform.scale(self.config.yellow_dialog, (self.config.width * 0.2, self.config.height * 0.1))
        dialog_rect = dialog.get_rect(center = (self.config.width * 0.87, self.config.height * 0.1))

        score_message = self.config.font.render(f'Score: {current_score}', False, (171, 52, 31))
        score_message_rect = score_message.get_rect(center = (self.config.width * 0.87, self.config.height * 0.1))

        self.config.screen.blit(dialog, dialog_rect)
        self.config.screen.blit(score_message, score_message_rect)
        return current_score

    def player_collision(self):
        return pygame.sprite.spritecollide(self.player_group.sprite, self.enemy_group, False)

    def __del__(self):
        self.config.score = 0
