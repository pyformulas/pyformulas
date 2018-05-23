class plot:
    def __init__(self, x, y, color='blue', block=False, title=None, xlim=None, ylim=None, xlabel=None, ylabel=None):
        from matplotlib import pyplot as plt
        plt.plot(x, y, color=color)
        plt.grid(True)

        if title is not None:
            plt.title(title)
        if xlim is not None:
            plt.xlim(xlim)
        if ylim is not None:
            plt.ylim(ylim)
        if xlabel is not None:
            plt.xlabel(xlabel)
        if ylabel is not None:
            plt.ylabel(ylabel)

        from io import BytesIO
        imgfile = BytesIO()
        plt.savefig(imgfile)

        from PIL import Image
        img = Image.open(imgfile)

        import numpy as np
        canvas = np.asarray(img, dtype=np.uint8)
        b, g, r = canvas[:,:,0], canvas[:,:,1], canvas[:,:,2]
        self.canvas = np.stack((r,g,b), axis=2)

        self._closed = False
        if block:
            self._run_screen()
        else:
            import pyformulas as pf
            pf.thread(self._run_screen)

    def _run_screen(self):
        import pyformulas as pf
        screen = pf.screen(self.canvas, 'Plot')

        while screen.exists() and not self._closed:
            screen.update()

    def close(self):
        self._closed = True