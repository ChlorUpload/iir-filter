from signal_generator import SignalGenerator
import matplotlib.pyplot as plt
from audio import Audio
from convert_to_pcm import convert_to_pcm
import numpy as np
from math import pi, sin
from time import sleep

SAMPLE_RATE = 2000

period1 = 1000 / 440
period2 = 1000 / 554
period3 = 1000 / 659
period4 = 1000 / 880

sg = SignalGenerator.create(SAMPLE_RATE) \
    .add_sinusoidal_by_ms(6000, period1, 0) \
    .add_sinusoidal_by_ms(6000, period2, 0) \
    .add_sinusoidal_by_ms(6000, period3, 0) \
    .add_sinusoidal_by_ms(6000, period4, 0)

audio = Audio(2, 1, SAMPLE_RATE)

# gen 생성
gen = sg.generate(SAMPLE_RATE)

fig, axs = plt.subplots(2)
axs[0].plot(gen)
axs[1].plot(np.abs(np.fft.fft(gen)))
plt.show()

audio.push_chunk(convert_to_pcm(gen, SAMPLE_RATE))

audio.terminate()
