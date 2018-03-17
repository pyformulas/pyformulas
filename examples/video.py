import pyformulas as pf
import numpy as np

canvas = np.floor(np.random.random((480,640,3))*256).astype(np.uint8)

screen = pf.screen(canvas)

while screen.exists():
    canvas += 1
    screen.update(canvas=canvas)