import pyaudio
import audioop
import numpy as np
from matplotlib import pyplot as plt


chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 10

p = pyaudio.PyAudio()

s = p.open(format=FORMAT,
           channels=CHANNELS,
           rate=RATE,
           input=True,
           frames_per_buffer=chunk)

print("---recording---")

d = []

print((RATE / chunk) * RECORD_SECONDS)

n_samples = RATE // chunk * RECORD_SECONDS
mxs = np.empty(n_samples)

for i in range(0, n_samples):
    data = s.read(chunk)
    mx = audioop.max(data, 2)
    print(len(data), mx)

    mxs[i] = mx

plt.plot(range(n_samples), mxs)
