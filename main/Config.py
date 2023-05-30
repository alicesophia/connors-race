import pygame


class Config:

    def __init__(self):
        super().__init__()

        self.events = []
        self.state = 'menu'
        self.game_over = True

        self.screen = pygame.display.set_mode((1300, 400), 0, 0, 0)
        pygame.display.set_caption("Connor's Race")

        self.clock = pygame.time.Clock()

        self.font = pygame.font.Font("../assets/font/pixeltype.ttf", 50)

        self.enemy_timer = pygame.USEREVENT + 1

        self.jump_sound = pygame.mixer.Sound("../assets/audio/jump.mp3")
        self.jump_sound.set_volume(0.2)
        self.music = pygame.mixer.Sound("../assets/audio/music.wav")
        self.music.set_volume(0.1)
        self.music.play(-1)
