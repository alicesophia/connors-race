import pygame
from player import Player
from enemy import Enemy
from random import choice


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = font.render(f"Score: {current_time}", False, (64, 64, 64))
    score_rect = score_surface.get_rect(center = (400, 50))
    screen.blit(score_surface, score_rect)
    return current_time


def player_collision():
    return pygame.sprite.spritecollide(player_group.sprite, enemy_group, False)


# Inicialização do Pygame e variáveis
pygame.init()
screen = pygame.display.set_mode((800, 400), 0, 0, 0)
pygame.display.set_caption("Connor's Race")
clock = pygame.time.Clock()
game_over = True
running = True
start_time = 0
score = 0
music = pygame.mixer.Sound("../assets/audio/music.wav")
music.set_volume(0.1)
music.play(-1)

# Criação do cenário
sky_surface = pygame.image.load("../assets/graphics/sky.png").convert_alpha()
ground_surface = pygame.image.load("../assets/graphics/ground.png").convert_alpha()
font = pygame.font.Font("../assets/font/pixeltype.ttf", 50)

# Criação dos sprites
player_group = pygame.sprite.GroupSingle()
player_group.add(Player())

enemy_group = pygame.sprite.Group()

# Tela do game over
player_stand = pygame.image.load("../assets/graphics/player/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400, 200))

title_text = font.render("Connor's Race", False, (64, 64, 64))
title_text_rect = title_text.get_rect(center = (400, 50))

hint_text = font.render("Aperte espaço para começar".encode(), False, (64, 64, 64))
hint_text_rect = hint_text.get_rect(center = (400, 350))

# Timer do spawn dos inimigos
enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer, 1500)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not game_over:
            if event.type == enemy_timer:
                enemy_group.add(Enemy(choice(["snail", "snail", "snail", "fly"])))

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_over:
                game_over = False
                start_time = int(pygame.time.get_ticks() / 1000)

    if not game_over:
        # Cenário
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        score = display_score()

        # Player
        player_group.draw(screen)
        player_group.update()

        # Inimigos
        enemy_group.draw(screen)
        enemy_group.update()

        # Colisões
        game_over = player_collision()
    else:
        # Tela do game over
        enemy_group.empty()
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        screen.blit(title_text, title_text_rect)

        # Mensagem do game over
        if score == 0:
            screen.blit(hint_text, hint_text_rect)
        else:
            score_message = font.render(f'Game over! Seu score foi: {score}', False, (64, 64, 64))
            score_message_rect = score_message.get_rect(center = (400, 350))
            screen.blit(score_message, score_message_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
