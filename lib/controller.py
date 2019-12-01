class RollingAverage:
    def __init__(self, default, a=.1, b=.01):
        self.a = a
        self.b = b
        self.value = default
        self.value_prev = default
        self.trend = 0
        self.trend_prev = 0

    def update(self, value_new):
        value_new = self.a * value_new + (1 - self.a) * (self.value_prev + self.trend_prev)
        trend_new = self.b * (value_new - self.value_prev) + (1 - self.b) * self.trend_prev
        self.value, self.value_prev = value_new, self.value
        self.trend, self.trend_prev = trend_new, self.trend


class Controller:
    def __init__(self):
        self.rolling_avg = RollingAverage(1024)
        self.pattern = [True, False]
        self.i_pattern = 0
        self.mode = 'playing'

    def decide(self, value):
        self.rolling_avg.update(value)
        decision = self.pattern[self.i_pattern]
        self.i_pattern = (self.i_pattern + 1) % len(self.pattern)
        return decision


if __name__ == "__main__":
    import input
    import numpy as np
    import matplotlib.pyplot as plt
    CHUNK = 1024
    RATE = 44100

    inp = input.factory('audio', CHUNK, RATE)
    gen = inp.generate_values()
    ctrl = Controller()

    n_exp = 2**10
    keep = np.zeros((n_exp, 2))

    for i in range(n_exp):
        val = next(gen)
        ctrl.decide(val)
        keep[i, 0] = val
        keep[i, 1] = ctrl.rolling_avg.value

    plt.plot(keep)

