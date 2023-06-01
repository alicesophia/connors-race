import pygame


class Config:

    def __init__(self):
        super().__init__()

        self.events = []
        self.state = 'menu'
        self.game_over = True

        self.screen = pygame.display.set_mode((1280, 720), 0, 0, 0, 0)
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        pygame.display.set_caption("Connor's Race")

        self.menu_background = pygame.image.load("../assets/graphics/main_menu/background.png").convert_alpha()
        self.logo = pygame.image.load("../assets/graphics/main_menu/logo.png").convert_alpha()
        self.play_button_pressed = pygame.image.load("../assets/graphics/main_menu/button_play_pressed.png").convert_alpha()
        self.options_button_pressed = pygame.image.load("../assets/graphics/main_menu/button_options_pressed.png").convert_alpha()
        self.quit_button_pressed = pygame.image.load("../assets/graphics/main_menu/button_quit_pressed.png").convert_alpha()

        self.game_scenario = pygame.image.load("../assets/graphics/scenario/game_background_1.png").convert_alpha()
        self.game_ground = pygame.image.load("../assets/graphics/ground.png").convert_alpha()

        self.clock = pygame.time.Clock()

        self.font = pygame.font.Font("../assets/font/pixeltype.ttf", 50)

        self.enemy_timer = pygame.USEREVENT + 1
        self.score = 0

        self.jump_sound = pygame.mixer.Sound("../assets/audio/jump.mp3")
        self.jump_sound.set_volume(0.2)
        self.music = pygame.mixer.Sound("../assets/audio/music.wav")
        self.music.set_volume(0.1)
        self.music.play(-1)
