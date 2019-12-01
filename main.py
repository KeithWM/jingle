import numpy as np
import matplotlib.pyplot as plt
import time

import input
import output
import controller


if __name__ == "__main__":
    CHUNK = 128
    RATE = 44100

    inp = input.factory('audio', CHUNK, RATE)
    outp = output.PrintOutput()
    ctrl = controller.Controller()

    n_keep = 4000
    i_keep = 0
    keep = np.zeros((n_keep, 5))

    for value in inp.generate_values():
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
