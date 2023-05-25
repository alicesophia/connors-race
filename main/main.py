import pygame
from random import randint


# Função para exibir o score
def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = font.render(f"Score: {current_time}", False, (64, 64, 64))
    score_rect = score_surface.get_rect(center = (400, 50))
    screen.blit(score_surface, score_rect)
    return current_time


def move_enemy(enemy_list):
    if enemy_list:
        for enemy_rect in enemy_list:
            enemy_rect.x -= 5
            if enemy_rect.bottom == 300:
                screen.blit(snail_surface, enemy_rect)
            else:
                screen.blit(fly_surface, enemy_rect)

        enemy_list = [enemy for enemy in enemy_list if enemy.x > -50]
        return enemy_list
    else:
        return []


def player_collision(player, enemy):
    if enemy:
        for enemy_rect in enemy:
            if player.colliderect(enemy_rect):
                return True
    return False


# Inicialização do Pygame e variáveis
pygame.init()
screen = pygame.display.set_mode((800, 400), 0, 0, 0)
pygame.display.set_caption("Connor's Race")
clock = pygame.time.Clock()
game_over = True
running = True
paused = False
paused_time = 0
start_time = 0
score = 0

# Criação do cenário
sky_surface = pygame.image.load("../graphics/sky.png").convert_alpha()
ground_surface = pygame.image.load("../graphics/ground.png").convert_alpha()
font = pygame.font.Font("../font/pixeltype.ttf", 50)

# Criação dos inimigos
snail_surface = pygame.image.load("../graphics/snail/snail1.png").convert_alpha()
fly_surface = pygame.image.load("../graphics/fly/fly1.png").convert_alpha()
enemy_rect_list = []

# Criação do player
player_surface = pygame.image.load("../graphics/player/player_walk_1.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 300))
player_gravity = 0

# Criação do player no game over
player_stand = pygame.image.load("../graphics/player/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400, 200))

# Texto do nome do game
title_text = font.render("Connor's Race", False, (64, 64, 64))
title_text_rect = title_text.get_rect(center = (400, 50))

# Mensagem ao jogador
hint_text = font.render("Aperte espaço para começar", False, (64, 64, 64))
hint_text_rect = hint_text.get_rect(center = (400, 350))

# Timer dos inimigos
enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer, 1500)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if not game_over:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom == 300:
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    player_gravity = -20
            if event.type == enemy_timer:
                if randint(0, 2):
                    enemy_rect_list.append(snail_surface.get_rect(bottomright = (randint(900, 1100), 300)))
                else:
                    enemy_rect_list.append(fly_surface.get_rect(bottomright = (randint(900, 1100), 210)))

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_over:
                game_over = False
                start_time = int(pygame.time.get_ticks() / 1000)

    if not game_over:
        # Cenário
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        score = display_score()

        # Inimigos
        enemy_rect_list = move_enemy(enemy_rect_list)

        # Player
        player_gravity += 1
        player_rect.y += player_gravity

        if player_rect.bottom > 300:
            player_rect.bottom = 300

        screen.blit(player_surface, player_rect)

        # Colisões
        game_over = player_collision(player_rect, enemy_rect_list)
    else:
        # Tela do game over
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        screen.blit(title_text, title_text_rect)
        enemy_rect_list.clear()
        player_rect.midbottom = (80, 300)
        player_gravity = 0

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
