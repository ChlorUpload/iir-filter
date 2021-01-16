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

# IIR 임펄스 응답
def h(n: int):

    f_c = 600
    w_c = 2*pi*f_c / SAMPLE_RATE

    if n==0:
        return w_c / pi
    else:
        return sin(w_c * n) / pi / n

# LTI 시스템 패스
def lti(x, length, impulse_response):
    y = [0] * length
    for n in range(0, length):
        for k in range(-length, length):
            y[n] += x[k] * impulse_response(n - k)

    return y

x = np.linspace(-1000, 1000, num=2000)
impz = []
for i in range(-1000, 1000):
    impz.append(h(i))

plt.plot(x, impz)
plt.show()

# gen 생성
gen = sg.generate(SAMPLE_RATE)

# gen 에 필터 적용
gen = lti(gen, SAMPLE_RATE, h)

fig, axs = plt.subplots(2)
axs[0].plot(gen)
axs[1].plot(np.abs(np.fft.fft(gen)))
plt.show()

audio.push_chunk(convert_to_pcm(gen, SAMPLE_RATE))

audio.terminate()
