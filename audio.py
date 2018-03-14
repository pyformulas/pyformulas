class play:
    def __init__(self, wavedata, bitrate=2.56e5, duration=None):#TODO: restrict bitrate based on pyaudio limits
        self.wavedata = wavedata
        self.bitrate = bitrate
        self.duration = duration

        #if block:TODO
        self._play()

    def _play(self):
        import pyaudio

        pa = pyaudio.PyAudio()

        # if hasattr(wavedata, 'shape'):TODO

        wavedata = bytes(self.wavedata)

        bitrate = round(self.bitrate)
        if self.duration is not None:
            bits = len(wavedata) * 8
            bitrate = round(bits / self.duration)

        sample_rate = round(bitrate/8)

        stream = pa.open(format=pa.get_format_from_width(1),
                         channels=1,
                         rate=sample_rate,
                         output=True)

        stream.write(wavedata)
        stream.stop_stream()
        stream.close()
        pa.terminate()