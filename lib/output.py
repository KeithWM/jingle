from abc import ABCMeta, abstractmethod


class Output(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, chunk, rate):
        self.chunk = chunk
        self.rate = rate

    @abstractmethod
    def on(self):
        pass

    @abstractmethod
    def off(self):
        pass

    def callback(self):
        pass

    def close(self):
        pass


def factory(name, chunk, rate):
    if name == "print":
        return PrintOutput(chunk, rate)
    if name == "pygame":
        from pygame_output import PygameOutput
        return PygameOutput(chunk, rate)
    if name == "optocoupler":
        from optocoupler_output import OptocouplerOutput
        return OptocouplerOutput(chunk, rate)
    else:
        raise ValueError


class PrintOutput(Output):
    ON_CHAR = u'\u2588'
    OFF_CHAR = '_'

    def __init__(self, chunk, rate):
        super().__init__(chunk, rate)

    def on(self):
        print(self.ON_CHAR, end=' ')

    def off(self):
        print(self.OFF_CHAR, end=' ')

    def callback(self):
        pass


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
