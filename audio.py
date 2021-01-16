import pyaudio
import wave
import sys


class Audio:
    def __init__(self, bytes_for_sample: int, channels: int, sample_rate: int):

        self._pyaudio = pyaudio.PyAudio()
        self._stream = self._pyaudio.open(
            format=self._pyaudio.get_format_from_width(bytes_for_sample),
            channels=channels,
            rate=sample_rate,
            output=True)

    def push_chunk(self, data):

        self._stream.write(data)

    def terminate(self):

        self._stream.stop_stream()
        self._stream.close()
        self._pyaudio.terminate()


if __name__ == "__main__":

    CHUNK = 1024
    wf = wave.open('./test.wav', 'rb')

    data = wf.readframes(CHUNK)
    bytes_for_sample = wf.getsampwidth()
    channels = wf.getnchannels()
    sample_rate = wf.getframerate()

    audio = Audio(bytes_for_sample, channels, sample_rate)

    # play stream
    while len(data) > 0:
        audio.push_chunk(data)
        data = wf.readframes(CHUNK)

    audio.terminate()
