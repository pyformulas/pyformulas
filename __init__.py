class Class:
    pass

def screen(canvas=None, title='Display'):
    from _formulas.screen import screen
    globals()['screen'] = screen

    return screen(canvas, title)

audio = Class()
def _play(wavedata, bitrate=None, duration=None, block=False):
    from _formulas.audio.play import play
    globals()['audio'].play = play

    return play(wavedata, bitrate, duration, block)
audio.play = _play


def download(url, out_path=None, get_headers=False, get_body=None):
    from _formulas.download import download
    globals()['download'] = download

    return download(url, out_path, get_headers, get_body)