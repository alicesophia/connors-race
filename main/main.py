import pygame


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = font.render(f"Score: {current_time}", False, (64, 64, 64))
    score_rect = score_surface.get_rect(center = (400, 50))
    screen.blit(score_surface, score_rect)
    return current_time


pygame.init()
screen = pygame.display.set_mode((800, 400), 0, 0, 0)
pygame.display.set_caption("Connor's Race")
clock = pygame.time.Clock()
game_over = True
running = True
start_time = 0
score = 0

sky_surface = pygame.image.load("../graphics/sky.png").convert_alpha()
ground_surface = pygame.image.load("../graphics/ground.png").convert_alpha()
font = pygame.font.Font("../font/pixeltype.ttf", 50)

snail_surface = pygame.image.load("../graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (800, 300))

player_surface = pygame.image.load("../graphics/player/player_walk_1.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 300))
player_gravity = 0

player_stand = pygame.image.load("../graphics/player/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400, 200))

title_text = font.render("Connor's Race", False, (64, 64, 64))
title_text_rect = title_text.get_rect(center = (400, 50))

hint_text = font.render("Aperte espaço para começar", False, (64, 64, 64))
hint_text_rect = hint_text.get_rect(center = (400, 350))

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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_over:
                game_over = False
                snail_rect.left = 800
                start_time = int(pygame.time.get_ticks() / 1000)

    if not game_over:
        snail_rect.x -= 5
        if snail_rect.right < 0:
            snail_rect.left = 800

        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))

        score = display_score()

        screen.blit(snail_surface, snail_rect)

        player_gravity += 1
        player_rect.y += player_gravity

        if player_rect.bottom > 300:
            player_rect.bottom = 300

        screen.blit(player_surface, player_rect)

        if snail_rect.colliderect(player_rect):
            game_over = True
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        screen.blit(title_text, title_text_rect)

        if score == 0:
            screen.blit(hint_text, hint_text_rect)
        else:
            score_message = font.render(f'Game over! Seu score foi: {score}', False, (64, 64, 64))
            score_message_rect = score_message.get_rect(center = (400, 350))
            screen.blit(score_message, score_message_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
