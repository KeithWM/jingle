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
    inp = input.factory('audio', CHUNK, RATE)
    ctrl = controller.Controller()

    n_keep = 1000
    i_keep = 0
    keep = np.zeros((n_keep, 5))

    prev = time.time()

    value_gen = inp.generate_values()
    # for value in value_gen:
    while True:
        print(i_keep, time.time() - prev)
        value = next(value_gen)
        prev = time.time()
        outp.callback()
        decision = ctrl.decide(value)
        if decision:
            outp.on()
        else:
            outp.off()
        keep[i_keep, 0] = value
        keep[i_keep, 1] = ctrl.rolling_avg.value * ctrl.THRESHOLD
        keep[i_keep, 2] = decision
        keep[i_keep, 3] = ctrl.mode == 'listening'
        keep[i_keep, 4] = -int(ctrl.mode == 'playing')
        i_keep = i_keep + 1
        if i_keep == len(keep):
            break

    fig, (ax, bin_ax) = plt.subplots(2, 1, sharex=True)
    # bin_ax = ax.twinx()
    ax.plot(keep[:, :2])
    bin_ax.plot(keep[:, 2:])
    plt.show()
