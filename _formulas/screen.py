import numpy as np
import cv2

class screen:
    def __init__(self, canvas=None, title='Display'):
        self.title = title

        if canvas is None:
            self.canvas = np.zeros((480,640), dtype=np.uint8)
        else:
            self.canvas = canvas

        cv2.imshow(self.title, self.canvas)

        self._closed = False

    def update(self, canvas=None):
        if cv2.getWindowProperty(self.title, 0) < 0:
            return self.close()

        if canvas is not None:
            self.canvas = canvas

        cv2.imshow(self.title, self.canvas)

        # keycode = cv2.waitKey(1) & 0xFF
        cv2.waitKey(1)

    def exists(self):
        return not self._closed

    def close(self):
        try:
            cv2.destroyWindow(self.title)
        except:
            pass

        self._closed = True