import numpy as np
import matplotlib.pyplot as plt
import time

import input
import output
import controller


if __name__ == "__main__":
    CHUNK = 1024
    RATE = 44100

    inp = input.factory('audio', CHUNK, RATE)
    outp = output.PrintOutput()
    ctrl = controller.Controller()

    for value in inp.generate_values():
        decision = ctrl.decide(value)
        if decision:
            outp.on()
        else:
            outp.off()
