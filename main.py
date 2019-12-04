import numpy as np
import matplotlib.pyplot as plt
import time

import input
import output
import controller


if __name__ == "__main__":
    CHUNK = 2**10
    RATE = 48000

    outp = output.factory('pygame', CHUNK, RATE)
    outp.callback()

    ctrl = controller.Controller()

    n_keep = 1000
    i_keep = 0
    keep = np.zeros((n_keep, 7))

    inp = input.factory('audio', CHUNK, RATE)
    value_gen = inp.generate_values()
    # for value in value_gen:
    try:
        while True:
            prev = time.time()
            value = next(value_gen)
            delta_time = time.time() - prev

            keep[i_keep, 2] = delta_time * RATE / CHUNK
            print(f'{i_keep}, A: {delta_time}')

            prev = time.time()
            outp.callback()
            delta_time = time.time() - prev

            print(f'{i_keep}, B: {delta_time}')
            keep[i_keep, 3] = delta_time * RATE / CHUNK

            decision = ctrl.decide(value)
            if decision:
                outp.on()
            else:
                outp.off()
            keep[i_keep, 0] = value
            keep[i_keep, 1] = ctrl.rolling_avg.value * ctrl.THRESHOLD
            keep[i_keep, 4] = decision
            keep[i_keep, 5] = ctrl.mode == 'listening'
            keep[i_keep, 6] = -int(ctrl.mode == 'playing')
            i_keep = i_keep + 1
            if i_keep == len(keep):
                break
    finally:
        fig, (ax, bin_ax) = plt.subplots(2, 1, sharex=True)
        # bin_ax = ax.twinx()
        ax.plot(keep[:, :2])
        bin_ax.plot(keep[:, 2:])
        plt.show()
