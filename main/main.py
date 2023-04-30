import pygame

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
running = True
font = pygame.font.Font("../font/pixeltype.ttf", 50)

sky_surface = pygame.image.load("../graphics/sky.png").convert_alpha()
ground_surface = pygame.image.load("../graphics/ground.png").convert_alpha()
text_surface = font.render("My game", False, "Black")

snail_surface = pygame.image.load("../graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (800, 300))

player_surface = pygame.image.load("../graphics/player/player_walk_1.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 300))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            if player_rect.collidepoint(event.pos):
                print("Mouse collision with player rect")
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     print(f"Mouse down {event.pos}")
        # if event.type == pygame.MOUSEBUTTONUP:
        #     print(f"Mouse up {event.pos}")
        # if event.type == pygame.MOUSEWHEEL:
        #     print(f"Mouse wheel {event}")

    snail_rect.x -= 4
    if snail_rect.right < 0:
        snail_rect.left = 800

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))

    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surface, player_rect)

    # if player_rect.colliderect(snail_rect):
    #     print("snail collision")

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(60)

pygame.quit()
