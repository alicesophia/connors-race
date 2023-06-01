import pygame
from main import Config, Game


def menu():
    background = pygame.transform.scale(config.menu_background, (config.width, config.height))
    config.screen.blit(background, (0, 0))
    config.screen.blit(logo_img, logo_rect)
    config.screen.blit(play_button_pressed, play_button_pressed_rect)
    config.screen.blit(options_button_pressed, options_button_pressed_rect)
    config.screen.blit(quit_button_pressed, quit_button_pressed_rect)
    print("MENU")


def selection():
    config.screen.fill((94, 129, 162))
    score_message = config.font.render(f'PRESSIONE ENTER', False, (64, 64, 64))
    score_message_rect = score_message.get_rect(center = (400, 350))
    config.screen.blit(score_message, score_message_rect)
    print("SELECTION")


def pause():
    print("PAUSE")


pygame.init()
running = True
config = Config.Config()
cursor_arrow = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW)
cursor_hand = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND)

logo_img = pygame.transform.scale(config.logo, (config.width * 0.45, config.height * 0.8))
logo_rect = logo_img.get_rect(center = (config.width * 0.5, config.height * 0.25))

play_button_pressed = pygame.transform.scale(config.play_button_pressed, (config.width * 0.2, config.height * 0.15))
play_button_pressed_rect = play_button_pressed.get_rect(center = (config.width * 0.5, config.height * 0.55))

options_button_pressed = pygame.transform.scale(config.options_button_pressed, (config.width * 0.165, config.height * 0.125))
options_button_pressed_rect = options_button_pressed.get_rect(center = (config.width * 0.5, config.height * 0.7))

quit_button_pressed = pygame.transform.scale(config.quit_button_pressed, (config.width * 0.175, config.height * 0.13))
quit_button_pressed_rect = quit_button_pressed.get_rect(center = (config.width * 0.5, config.height * 0.85))

while running:
    config.events = pygame.event.get()
    for event in config.events:
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEMOTION:
            if play_button_pressed_rect.collidepoint(event.pos) or \
               options_button_pressed_rect.collidepoint(event.pos) or \
               quit_button_pressed_rect.collidepoint(event.pos):
                pygame.mouse.set_cursor(cursor_hand)
            else:
                pygame.mouse.set_cursor(cursor_arrow)

        if event.type == pygame.MOUSEBUTTONUP:
            if play_button_pressed_rect.collidepoint(event.pos) and event.button == 1:
                config.clock.tick(5)
                config.state = 'selection'
            if quit_button_pressed_rect.collidepoint(event.pos) and event.button == 1:
                running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and config.state != 'menu':
                if config.state == 'play':
                    config.state = 'pause'
                    pygame.time.set_timer(config.enemy_timer, 0)
                else:
                    config.state = 'play'
                    pygame.time.set_timer(config.enemy_timer, 2000)

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
