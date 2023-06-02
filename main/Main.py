import pygame
import Config
import Game


def menu():
    background = pygame.transform.scale(config.menu_background, (config.width, config.height))
    config.screen.blit(background, (0, 0))
    config.screen.blit(logo_img, logo_rect)
    config.screen.blit(play_button_pressed, play_button_pressed_rect)
    config.screen.blit(options_button_pressed, options_button_pressed_rect)
    config.screen.blit(quit_button_pressed, quit_button_pressed_rect)


def selection():
    background = pygame.transform.scale(config.menu_background, (config.width, config.height))
    config.screen.blit(background, (0, 0))
    dialog_text = config.font.render("Com quem você vai jogar?", True, (171, 52, 31))
    dialog_text_rect = dialog_text.get_rect(center = (config.width * 0.5, config.height * 0.25))
    choose_sarah = config.font.render("Sarah Connor", True, (171, 52, 31))
    sarah_rect = choose_sarah.get_rect(center = (config.width * 0.35, config.height * 0.80))
    choose_john = config.font.render("John Connor", True, (171, 52, 31))
    john_rect = choose_john.get_rect(center = (config.width * 0.65, config.height * 0.80))
    config.screen.blit(dialog, dialog_rect)
    config.screen.blit(dialog_text, dialog_text_rect)
    config.screen.blit(choose_sarah_button, choose_sarah_rect)
    config.screen.blit(choose_john_button, choose_john_rect)
    config.screen.blit(choose_john, john_rect)
    config.screen.blit(choose_sarah, sarah_rect)


def pause():
    pause_message = config.font.render("Jogo pausado", True, (171, 52, 31))
    pause_message_rect = pause_message.get_rect(center = (config.width * 0.5, config.height * 0.4))
    config.screen.blit(dialog_pause, dialog_pause_rect)
    config.screen.blit(pause_message, pause_message_rect)
    config.screen.blit(quit_pause_button, quit_pause_button_rect)


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

quit_pause_button = pygame.transform.scale(config.quit_button_pressed, (config.width * 0.175, config.height * 0.13))
quit_pause_button_rect = quit_pause_button.get_rect(center = (config.width * 0.5, config.height * 0.6))

choose_sarah_button = pygame.transform.scale(config.yellow_button, (config.width * 0.2, config.height * 0.10))
choose_sarah_rect = choose_sarah_button.get_rect(center = (config.width * 0.35, config.height * 0.80))

choose_john_button = pygame.transform.scale(config.yellow_button, (config.width * 0.2, config.height * 0.10))
choose_john_rect = choose_john_button.get_rect(center = (config.width * 0.65, config.height * 0.80))

dialog = pygame.transform.scale(config.yellow_dialog, (config.width * 0.35, config.height * 0.10))
dialog_rect = dialog.get_rect(center = (config.width * 0.5, config.height * 0.25))

dialog_pause = pygame.transform.scale(config.yellow_dialog, (config.width * 0.2, config.height * 0.10))
dialog_pause_rect = dialog_pause.get_rect(center = (config.width * 0.5, config.height * 0.4))

while running:
    config.events = pygame.event.get()

    for event in config.events:
        if event.type == pygame.QUIT:
            running = False

        if config.state == 'menu':
            if event.type == pygame.MOUSEMOTION:
                if (play_button_pressed_rect.collidepoint(event.pos) or
                   options_button_pressed_rect.collidepoint(event.pos) or
                   quit_button_pressed_rect.collidepoint(event.pos)):
                    pygame.mouse.set_cursor(cursor_hand)
                else:
                    pygame.mouse.set_cursor(cursor_arrow)

            if event.type == pygame.MOUSEBUTTONUP:
                if play_button_pressed_rect.collidepoint(event.pos) and event.button == 1:
                    config.click_sound.play()
                    config.clock.tick(5)
                    config.state = 'selection'

                if options_button_pressed_rect.collidepoint(event.pos) and event.button ==1:
                    config.click_sound.play()

                if quit_button_pressed_rect.collidepoint(event.pos) and event.button == 1:
                    running = False

        if config.state == 'selection':
            if event.type == pygame.MOUSEMOTION:
                if choose_sarah_rect.collidepoint(event.pos) or choose_john_rect.collidepoint(event.pos):
                    pygame.mouse.set_cursor(cursor_hand)
                else:
                    pygame.mouse.set_cursor(cursor_arrow)

            if event.type == pygame.MOUSEBUTTONUP:
                if (choose_sarah_rect.collidepoint(event.pos) or
                   choose_john_rect.collidepoint(event.pos) and
                   event.button == 1):
                    config.click_sound.play()
                    config.clock.tick(5)
                    game = Game.Game(config)
                    pygame.mouse.set_cursor(cursor_arrow)
                    config.state = 'play'

        if config.state == 'pause':
            if event.type == pygame.MOUSEMOTION:
                if quit_pause_button_rect.collidepoint(event.pos):
                    pygame.mouse.set_cursor(cursor_hand)
                else:
                    pygame.mouse.set_cursor(cursor_arrow)

            if event.type == pygame.MOUSEBUTTONUP:
                if quit_pause_button_rect.collidepoint(event.pos) and event.button == 1:
                    config.click_sound.play()
                    config.clock.tick(5)
                    config.state = 'menu'
                    config.game_over = True
                    del game

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if not config.game_over:
                    if config.state == 'play' and config.score != 0:
                        config.state = 'pause'
                        pygame.time.set_timer(config.enemy_timer, 0)
                    elif config.state == 'pause':
                        config.state = 'play'
                        pygame.time.set_timer(config.enemy_timer, 1800)

    match config.state:
        case 'selection': selection()
        case 'play': game.update()
        case 'pause': pause()
        case 'menu': menu()

    pygame.display.update()
    config.clock.tick(60)

pygame.quit()
