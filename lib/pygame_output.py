import pygame as pg

from output import Output


WHITE = (255, 255, 255)
GREY = (128, 128, 128)


class Tile(pg.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pg.Surface((100, 100))
        self.color = WHITE
        self.image.fill(self.color)
        self.ref = self.image.get_rect(topleft=position)

    def change_color(self, color):
        self.color = color
        self.image.fill(self.color)


class PygameOutput(Output):
    def __init__(self, chunk, rate, width=300, height=300):
        super().__init__(chunk, rate)
        pg.init()
        self.fps = rate // chunk
        self.clock = pg.time.Clock()
        self.colors = [WHITE, GREY]
        self.screen = pg.display.set_mode((width, height))
        self.background = pg.Surface((width, height))
        self.tile = Tile((100, 100))
        self.is_on = False

    def on(self):
        self.screen.fill(WHITE)
        # self.tile.change_color(WHITE)

    def off(self):
        self.screen.fill(GREY)
        # self.tile.change_color(GREY)

    def callback(self):
        pg.display.flip()
        # self.clock.tick(self.fps)
        for event in pg.event.get():
            pass


if __name__ == "__main__":
    import numpy as np
    import time
    import matplotlib.pyplot as plt

    n_keep = 1000
    keep = np.zeros(n_keep)

    chunk = 2 ** 10
    rate = 44800
    outp = PygameOutput(chunk, rate)

    now = time.time()
    for i in range(n_keep):
        if np.random.rand() > 0.5:
            outp.on()
        else:
            outp.off()

        now, prev = time.time(), now
        keep[i] = now - prev

    plt.plot(keep * rate / chunk)

