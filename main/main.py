import pygame


def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score_surface = font.render(f"Score: {round(current_time / 1000)}", False, (64, 64, 64))
    score_rect = score_surface.get_rect(center = (400, 50))
    screen.blit(score_surface, score_rect)


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
game_over = False
running = True
start_time = 0

sky_surface = pygame.image.load("../graphics/sky.png").convert_alpha()
ground_surface = pygame.image.load("../graphics/ground.png").convert_alpha()
font = pygame.font.Font("../font/pixeltype.ttf", 50)

snail_surface = pygame.image.load("../graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (800, 300))

player_surface = pygame.image.load("../graphics/player/player_walk_1.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 300))
player_gravity = 0

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
                start_time = pygame.time.get_ticks()

    if not game_over:

        snail_rect.x -= 5
        if snail_rect.right < 0:
            snail_rect.left = 800

        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))

        display_score()

        screen.blit(snail_surface, snail_rect)

        player_gravity += 1
        player_rect.y += player_gravity

        if player_rect.bottom > 300:
            player_rect.bottom = 300

        screen.blit(player_surface, player_rect)

        if snail_rect.colliderect(player_rect):
            game_over = True
    else:
        screen.fill("Yellow")

    pygame.display.update()
    clock.tick(60)

pygame.quit()
