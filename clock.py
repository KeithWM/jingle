import time

import output
import controller
import morse


def get_time():
    return time.strftime('%H%M')


if __name__ == "__main__":
    CHUNK = 2**10
    RATE = 48000

    outp = output.factory('optocoupler', CHUNK, RATE)
    outp.callback()

    m = morse.Morse(outp, 4)

    ctrl = controller.Controller()

    try:
        while True:
            curr_time = get_time()
            while curr_time == get_time():
                outp.callback()
                print(curr_time)
                m.show(curr_time)
    finally:
        outp.close()
