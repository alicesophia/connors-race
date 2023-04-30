import pygame

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
running = True

sky_surface = pygame.image.load("../graphics/sky.png").convert_alpha()
ground_surface = pygame.image.load("../graphics/ground.png").convert_alpha()

font = pygame.font.Font("../font/pixeltype.ttf", 50)
score_surface = font.render("My game", False, (64, 64, 64))
score_rect = score_surface.get_rect(center = (400, 50))

snail_surface = pygame.image.load("../graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (800, 300))

player_surface = pygame.image.load("../graphics/player/player_walk_1.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 300))
player_gravity = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos):
                player_gravity = -20
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_gravity = -20

    snail_rect.x -= 4
    if snail_rect.right < 0:
        snail_rect.left = 800

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))

    pygame.draw.rect(screen, "#c0e8ec", score_rect)
    screen.blit(score_surface, score_rect)

    screen.blit(snail_surface, snail_rect)

    player_gravity += 1
    player_rect.y += player_gravity
    screen.blit(player_surface, player_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
