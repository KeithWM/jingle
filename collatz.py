import time

import output
import controller


if __name__ == "__main__":
    CHUNK = 2**10
    RATE = 48000

    outp = output.factory('pygame', CHUNK, RATE)
    outp.callback()

    ctrl = controller.Controller()

    i = 1
    try:
        while True:
            outp.callback()
            print(i)
            if i == 1:
                outp.on()
                time.sleep(1)
                outp.off()
                time.sleep(1)
                i = int(time.time())
            else:
                time.sleep(.1)
                if i % 2 == 0:
                    outp.on()
                    i = i // 2
                else:
                    outp.off()
                    i = 3*i + 1
    finally:
        outp.close()
