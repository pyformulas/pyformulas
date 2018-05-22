import pyaudio

class play:
    def __init__(self, wavedata, bitrate=None, duration=None, num_channels=1, bit_depth=16, block=False):
        import pyformulas as pf

        self.wavedata = wavedata if (isinstance(wavedata, bytes) or isinstance(wavedata, bytearray)) else bytes(wavedata)
        self.bitrate = bitrate
        self.duration = duration
        self.num_channels = num_channels

        formats = {8:pyaudio.paInt8, 16:pyaudio.paInt16, 24:pyaudio.paInt24, 32:pyaudio.paInt32}
        self.format = formats[bit_depth]

        assert (len(wavedata) % (bit_depth/8*num_channels)) == 0

        if block:
            self._play()
        else:
            pf.thread(self._play)

    def _play(self):
        pa = pyaudio.PyAudio()

        if self.bitrate is None and self.duration is None:
            raise ValueError("Must set either bitrate or duration")

        if self.duration is not None:
            bits = len(self.wavedata) * 8
            self.bitrate = bits / self.duration

        sample_rate = round(self.bitrate / 8)

        stream = pa.open(
            format=self.format,
            channels=self.num_channels,
            rate=sample_rate,
            output=True
        )

        stream.write(self.wavedata)
        stream.stop_stream()
        stream.close()
        pa.terminate()