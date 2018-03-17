class screen:
    import numpy as np
    import cv2

    def __init__(self, canvas=None, title='Display'):
        self.title = title

        if canvas is None:
            self.canvas = self.np.zeros((480,640), dtype=self.np.uint8)
        else:
            self.canvas = canvas

        self.cv2.imshow(self.title, self.canvas)

        self._closed = False

        #cv2.destroyAllWindows() #TODO

    def update(self, canvas=None):
        if self.cv2.getWindowProperty(self.title, 0) < 0:
            #cv2.destroyAllWindows()
            self._closed = True
            return

        if canvas is not None:
            self.canvas = canvas

        self.cv2.imshow(self.title, self.canvas)

        # keycode = cv2.waitKey(1) & 0xFF
        self.cv2.waitKey(1)

    def exists(self):
        return not self._closed

class audio:
    class play:
        def __init__(self, wavedata, bitrate=None, duration=None, block=False):
            self.wavedata = wavedata
            self.bitrate = bitrate
            self.duration = duration

            if block:
                self._play()
            else:
                self._play_thread(self).start()

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

        from threading import Thread
        class _play_thread(Thread):
            def __init__(self, parent):
                from threading import Thread
                Thread.__init__(self)

                self.parent = parent

            def run(self):
                self.parent._play()

            #def stop(self):
            #    """ Graceful shutdown """
            #    self._stop.set()
            #    self.stream.close()
            #    self.p.terminate()