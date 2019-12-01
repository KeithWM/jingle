import numpy as np
import matplotlib.pyplot as plt
import time

import input
import output


if __name__ == "__main__":
    CHUNK = 1024
    RATE = 44100
    KEEP_SECONDS = 10

    inp = input.factory('audio', CHUNK, RATE)

    n_keep = KEEP_SECONDS * RATE // CHUNK
    keep = np.zeros(n_keep)
    i_keep = 0

    now = time.time() % 10

    outp = output.PrintOutput()

    for value in inp.generate_values():
        keep[i_keep] = value
        i_keep = (i_keep + 1) % n_keep

        now, prev = time.time(), now
        print((now - prev) * RATE / CHUNK, value)
        if i_keep == 0:
            break

    plt.plot(np.arange(n_keep) * CHUNK / RATE, keep)
    plt.show()
