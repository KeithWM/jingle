import pygame

from output import Output


class PygameOutput(Output):
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
        for _ in pygame.event.get():
            pass


if __name__ == "__main__":
    import numpy as np
    import time
    import matplotlib.pyplot as plt

    n_keep = 1000
    keep = np.zeros(n_keep)

    outp = PygameOutput(2**10, 44800)

    now = time.time()
    for i in range(n_keep):
        if np.random.rand() > 0.5:
            outp.on()
        else:
            outp.off()

        now, prev = time.time(), now
        keep[i] = now - prev

    plt.plot(keep)

