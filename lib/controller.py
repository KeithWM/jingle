import numpy as np


class RollingAverage:
    def __init__(self, default, a=.01, b=0.):
        self.a = a
        self.b = b
        self.value = default
        self.tf_value_prev = self._transform(default)
        self.trend = 0
        self.trend_prev = 0

    def update(self, value_new):
        tf_value_new = self._transform(value_new)
        tf_value_new = self.a * tf_value_new + (1 - self.a) * (self.tf_value_prev + self.trend_prev)
        trend_new = self.b * (tf_value_new - self.tf_value_prev) + (1 - self.b) * self.trend_prev
        self.value, self.tf_value_prev = self._inv_transform(tf_value_new), self._transform(self.value)
        self.trend, self.trend_prev = trend_new, self.trend

    @staticmethod
    def _transform(x):
        return np.log(abs(x))

    @staticmethod
    def _inv_transform(x):
        return np.exp(x)


class Controller:
    THRESHOLD = 10

    def __init__(self):
        self.rolling_avg = RollingAverage(300)
        self.pattern = [True, ]
        self.listening_pattern = [True, ]
        self.new_pattern = []
        self.i_pattern = 0
        self.mode = 'playing'

    def decide(self, value):
        self.rolling_avg.update(value)
        self._decide_mode(value)
        decision = self.pattern[self.i_pattern]
        self.i_pattern = (self.i_pattern + 1) % len(self.pattern)
        return decision

    def _decide_mode(self, value):
        if self.mode == 'playing' and self._loud_enough(value):
            print('\nStarted listening')
            self.mode = 'listening'
            self.pattern = self.listening_pattern
            self.new_pattern = [True]
            self.i_pattern = 0
        if self.mode == 'listening':
            self.new_pattern.append(self._loud_enough(value))
            if self.new_pattern[-1] and not all(self.new_pattern):
                print(f'\nFinished listening')
                self.mode = 'just_playing'
                self.pattern = self.new_pattern
        if self.mode == 'just_playing' and self.i_pattern in (0, 10):
            self.mode = 'playing'

    def _loud_enough(self, value):
        return value > self.THRESHOLD * self.rolling_avg.value


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

