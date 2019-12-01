import pyaudio
import audioop

from input import Input


class AudioInput(Input):
    FORMAT = pyaudio.paInt16
    CHANNELS = 1

    def __init__(self, chunk, rate):
        super().__init__()
        self.chunk = chunk
        self.rate = rate
        self.p = pyaudio.PyAudio()

        self.s = self.p.open(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.rate,
            input=True,
            frames_per_buffer=self.chunk)

    def listen(self):
        data = self.s.read(self.chunk)
        return audioop.max(data, 2)
