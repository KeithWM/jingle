class PrintOutput:
    ON_CHAR = u'\u2588'
    OFF_CHAR = '_'

    def __init__(self):
        pass

    def on(self):
        print(self.ON_CHAR, end=' ')

    def off(self):
        print(self.OFF_CHAR, end=' ')


class OldPrintOutput:
    WIDTH = 100
    ON_CHAR = u'\u2588'
    OFF_CHAR = '_'

    def __init__(self):
        pass

    def on(self):
        print(self.ON_CHAR * self.WIDTH)

    def off(self):
        print(self.OFF_CHAR * self.WIDTH)


if __name__ == "__main__":
    import time

    outp = PrintOutput()
    print('hi')
    time.sleep(2)

    outp.on()
    time.sleep(1)

    outp.off()
    time.sleep(1)

    outp.on()
