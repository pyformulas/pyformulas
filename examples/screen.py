"""
Draws animated video frames to a window using pf.screen, along with an audio stream (pf.audio.play())
"""

import pyformulas as pf
import numpy as np
import time

def get_audio(duration):
    frequencies = [1, 150, 3, 200, 250]

    bitrate = 3.6e5
    duration = 10
    num_samples = round(bitrate / 8 * duration)

    waveforms = [np.cos(np.linspace(0, frequency * duration * 2 * np.pi, num_samples)) for frequency in frequencies]

    audio = np.multiply(*waveforms[:2]) + np.e**np.multiply(*waveforms[2:])

    audio /= audio[0]
    audio = np.floor(audio * 127.5 + 127.5).astype(np.uint8)

    return audio

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
