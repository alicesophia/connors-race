import pygame
from main import Config, Game


def menu():
    print("MENU")


def selection():
    print("SELECTION")


def pause():
    print("PAUSE")


pygame.init()
running = True
config = Config.Config()
cursor = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND)
pygame.mouse.set_cursor(cursor)

while running:
    config.events = pygame.event.get()
    for event in config.events:
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and config.state != 'menu':
                if config.state == 'play':
                    config.state = 'pause'
                    pygame.time.set_timer(config.enemy_timer, 0)
                else:
                    config.state = 'play'
                    pygame.time.set_timer(config.enemy_timer, 1500)

            if event.key == pygame.K_w:
                config.state = 'selection'

            if event.key == pygame.K_RETURN:
                game = Game.Game(config)
                config.state = 'play'

    match config.state:
        case 'selection': selection()
        case 'play':
            print("PLAY")
            game.update()
        case 'pause': pause()
        case 'menu': menu()

    pygame.display.update()
    config.clock.tick(60)

pygame.quit()
