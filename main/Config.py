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

        self.clock = pygame.time.Clock()

        self.enemy_timer = pygame.USEREVENT + 1
        self.score = 0

        self.logo = pygame.image.load("../assets/graphics/main_menu/logo.png").convert_alpha()
        self.menu_background = pygame.image.load("../assets/graphics/main_menu/background.png").convert_alpha()
        self.game_scenario = pygame.image.load("../assets/graphics/scenario/game_background.png").convert_alpha()
        self.game_ground = pygame.image.load("../assets/graphics/scenario/game_ground.png").convert_alpha()

        self.play_button_pressed = pygame.image.load("../assets/graphics/main_menu/button_play_pressed.png").convert_alpha()
        self.options_button_pressed = pygame.image.load("../assets/graphics/main_menu/button_options_pressed.png").convert_alpha()
        self.quit_button_pressed = pygame.image.load("../assets/graphics/main_menu/button_quit_pressed.png").convert_alpha()
        self.yellow_button = pygame.image.load("../assets/graphics/main_menu/yellow_button.png").convert_alpha()
        self.yellow_button_pressed = pygame.image.load("../assets/graphics/main_menu/yellow_button_pressed.png").convert_alpha()
        self.yellow_dialog = pygame.image.load("../assets/graphics/main_menu/yellow_dialog.png").convert_alpha()
        self.space_button = pygame.image.load("../assets/graphics/main_menu/button_space.png").convert_alpha()
        self.esc_button = pygame.image.load("../assets/graphics/main_menu/button_esc.png").convert_alpha()

        self.player = ''
        self.sarah_walk = [
            pygame.image.load("../assets/graphics/player/sarah/sarah_walk_1.png").convert_alpha(),
            pygame.image.load("../assets/graphics/player/sarah/sarah_walk_2.png").convert_alpha(),
            pygame.image.load("../assets/graphics/player/sarah/sarah_walk_3.png").convert_alpha(),
            pygame.image.load("../assets/graphics/player/sarah/sarah_walk_4.png").convert_alpha()
        ]
        self.jonh_walk = [
            pygame.image.load("../assets/graphics/player/john/john_walk_1.png").convert_alpha(),
            pygame.image.load("../assets/graphics/player/john/john_walk_2.png").convert_alpha(),
            pygame.image.load("../assets/graphics/player/john/john_walk_3.png").convert_alpha(),
            pygame.image.load("../assets/graphics/player/john/john_walk_4.png").convert_alpha()
        ]

        self.font = pygame.font.Font("../assets/font/FFFFORWA.TTF", 24)

        self.click_sound = pygame.mixer.Sound("../assets/audio/click.ogg")
        self.click_sound.set_volume(1)
        self.jump_sound = pygame.mixer.Sound("../assets/audio/jump.mp3")
        self.jump_sound.set_volume(0.2)
        self.death_sound = pygame.mixer.Sound("../assets/audio/death.mp3")
        self.death_sound.set_volume(0.5)
        self.music = pygame.mixer.Sound("../assets/audio/music.wav")
        self.music.set_volume(0.1)
        self.music.play(-1)
