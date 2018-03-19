class play:
    def __init__(self, wavedata, bitrate=None, duration=None, block=False):
        import pyformulas as pf

        self.wavedata = wavedata
        self.bitrate = bitrate
        self.duration = duration

        if block:
            self._play()
        else:
            pf.thread(self._play)

    def _play(self):
        from pyaudio import PyAudio
        self.wavedata = bytes(self.wavedata)
        pa = PyAudio()

        if self.bitrate is None and self.duration is None:
            raise ValueError("Must set either bitrate or duration")

        if self.duration is not None:
            bits = len(self.wavedata) * 8
            self.bitrate = bits / self.duration

        sample_rate = round(self.bitrate / 8)

        stream = pa.open(
            format=pa.get_format_from_width(1),
            channels=1,
            rate=sample_rate,
            output=True
        )

        stream.write(self.wavedata)
        stream.stop_stream()
        stream.close()
        pa.terminate()