import pygame

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
running = True
font = pygame.font.Font("../font/pixeltype.ttf", 50)

sky_surface = pygame.image.load("../graphics/sky.png")
ground_surface = pygame.image.load("../graphics/ground.png")
text_surface = font.render("My game", False, "Black")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
