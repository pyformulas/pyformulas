"""
Creates audio waveforms (type uint8), then plays them with pf.audio.play()
"""

import numpy as np
import pyformulas as pf
from time import sleep

def playnote(frequency):
    bitrate = 3.6e5
    duration = 0.25
    num_samples = round(bitrate / 8 * duration)
    wavedata = np.round((65536/2-1)*np.sin(np.linspace(0, frequency * duration * 2 * np.pi, num_samples))).astype(np.int16)

    pf.audio.play(wavedata, bitrate=bitrate, bit_depth=16, block=False)
    sleep(duration)

c = 261
d = 294
e = 329
f = 349
g = 392
a = 440
b = 493
C = 523
R = 0

melody = [e, R, d, R, c, R, d, R, e, R, e, R, e, R, d, R, d, R, d, R, e, R, g, R, g, R, e, R, d, R, c, R, d, R, e, R, e, R, e, R, e, R, d, R, d, R, e, R, d, R, c, R, c]

for note in melody:
    playnote(note)