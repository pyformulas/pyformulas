from threading import Thread

class thread(Thread):
    def __init__(self, function, args=(), kwargs={}, callback=None):
        from threading import Thread
        Thread.__init__(self)

        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.callback = callback
        self.result = None

        self.start()

    def run(self):
        self.result = self.function(*self.args, **self.kwargs)

        if not isinstance(self.result, tuple):
            self.result = (self.result,)

        if self.callback is not None:
            self.callback(*self.result)