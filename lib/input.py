from abc import ABCMeta, abstractmethod


class Input(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def listen(self):
        pass

    def generate_values(self):
        while True:
            yield self.listen()


def factory(name, chunk, rate):
    if name == "audio":
        from audio_input import AudioInput
        return AudioInput(chunk, rate)
    if name == "file":
        from file_input import FileInput
        return FileInput(chunk, rate)
    if name == "random":
        from random_input import RandomInput
        return RandomInput()
    else:
        raise ValueError
