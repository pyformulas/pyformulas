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