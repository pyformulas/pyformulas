"""
Draws animated image frames to a window with pf.screen, along with an audio stream (pf.audio.play())
"""

import pyformulas as pf
import numpy as np
import time

def get_audio(duration):
    bitrate = 3.6e5
    num_samples = round(bitrate / 8 * duration)

    bass = np.sin(np.linspace(0, 90 * duration * 2 * np.pi, num_samples))
    mids = np.sin(np.linspace(0, 100 * duration * 2 * np.pi, num_samples))
    highs = np.sin(np.linspace(0, 105 * duration * 2 * np.pi, num_samples))

    song = (bass + mids + highs)
    song /= np.max(song)

    wavedata = np.rint(song * 127.5 + 127.5).astype(np.uint8)

    return wavedata

wavedata = get_audio(10)

canvas = np.floor(np.random.normal(scale=50, size=(480,640,3)) % 256).astype(np.uint8)

screen = pf.screen(canvas)
pf.audio.play(wavedata, duration=10)

start = time.time()
while screen.exists():
    canvas -= 1
    screen.update()

    if time.time() - start > 10:
        screen.close()