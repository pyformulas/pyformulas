class settimeout:
    def __init__(self, callback, delay, repeat=False, args=(), kwargs={}):
        import pyformulas
        self._thread = pyformulas.thread

        self.callback = callback
        self.delay = delay
        self.repeat = repeat
        self.args = args
        self.kwargs = kwargs

        self.running = True
        self._thread(self._timer)

    def _timer(self):
        import time

        start_time = time.time()
        while True:
            delta_time = (time.time() - start_time) % self.delay
            time.sleep(self.delay - delta_time)

            self._thread(self.callback, self.args, self.kwargs)

            if not (self.running and self.repeat):
                break

    def stop(self):
        self.running = False

    def start(self):
        if self.running:
            return

        self.running = True
        self._thread(self._timer)