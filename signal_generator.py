from math import pi, sin, lcm
import matplotlib.pyplot as plt
from audio import Audio
from convert_to_pcm import convert_to_pcm

class SignalGenerator:
    def __init__(self, sample_rate: int):

        # wave is tuple of amplitude, period_sample, phase_sample
        self._waves: list[tuple[float, float, float]] = []

        # generation starting position. This value is maintained to be in the range [0, sample_rate)
        self._position = 0

        # period number of samples
        self._period_sample = 1

        # number of samples in 1 second
        self._sample_rate = sample_rate

    @staticmethod
    def create(sample_rate: int):
        return SignalGenerator(sample_rate)

    def add_sinusoidal(self, amplitude: float, period_sample: float, phase_sample: float):

        ret = SignalGenerator(self._sample_rate)

        ret._waves = self._waves.copy()
        ret._waves.append((amplitude, period_sample, phase_sample))

        ret._period_sample = ret._period_sample * period_sample

        return ret

    def add_sinusoidal_by_ms(self, amplitude, period_ms: float, phase_ms: float):

        return self.add_sinusoidal(amplitude,
                                   self._sample_rate * period_ms / 1000,
                                   self._sample_rate * phase_ms / 1000)

    def generate(self, length: int) -> list[int]:

        ret = length * [0]

        for amplitude, period, phase in self._waves:
            for i in range(0, length):
                ret[i] += amplitude * \
                    sin(2 * pi * (i + phase + self._position) / period)

        self._position = (self._position + length) % self._period_sample

        return ret


if __name__ == "__main__":

    SAMPLE_RATE = 10000

    period1 = 1000 / 440
    period2 = 1000 / 554
    period3 = 1000 / 659
    period4 = 1000 / 880

    sg = SignalGenerator.create(SAMPLE_RATE) \
        .add_sinusoidal_by_ms(6000, period1, 0) \
        .add_sinusoidal_by_ms(10000, period2, 0) \
        .add_sinusoidal_by_ms(8000, period3, 0) \
        .add_sinusoidal_by_ms(5000, period4, 0)

    plt.plot(sg.generate(250))
    plt.ylabel('amplitude')
    plt.show()

    audio = Audio(2, 1, SAMPLE_RATE)

    # 3초 길이의 데이터 push
    for i in range(1, 3):
        audio.push_chunk(convert_to_pcm(sg.generate(SAMPLE_RATE), SAMPLE_RATE))

    audio.terminate()
