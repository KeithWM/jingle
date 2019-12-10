import input
import output
import controller


if __name__ == "__main__":
    CHUNK = 2**10
    RATE = 48000

    outp = output.factory('optocoupler', CHUNK, RATE)
    outp.callback()

    ctrl = controller.Controller()

    inp = input.factory('random', CHUNK, RATE)
    value_gen = inp.generate_values()
    while True:
        value = next(value_gen)
        outp.callback()

        decision = ctrl.decide(value)
        if decision:
            outp.on()
        else:
            outp.off()
