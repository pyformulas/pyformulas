from threading import Thread

class thread(Thread):
    def __init__(self, function, args=(), kwargs={}):
        from threading import Thread
        Thread.__init__(self)

        self.function = function
        self.args = args
        self.kwargs = kwargs

        self.start()

    def run(self):
        result = self.function(*self.args, **self.kwargs)