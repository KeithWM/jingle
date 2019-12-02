import pygame

from output import Output


class PygameOutput(Output):
    ON_CHAR = u'\u2588'
    OFF_CHAR = '_'

    def __init__(self, chunk, rate, width=300, height=300):
        super().__init__(chunk, rate)
        pygame.init()
        self.fps = rate // chunk
        self.clock = pygame.time.Clock()
        self.colors = [(255, 255, 255), (128, 128, 128)]
        self.screen = pygame.display.set_mode((width, height))
        self.background = pygame.Surface((width, height))
        self.is_on = False

    def on(self):
        pygame.draw.rect(self.screen, self.colors[0], pygame.Rect(100, 100, 100, 100))

    def off(self):
        pygame.draw.rect(self.screen, self.colors[1], pygame.Rect(100, 100, 100, 100))

    def callback(self):
        pygame.display.flip()
        # self.clock.tick(self.fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # self.screen.fill((0, 0, 0))
