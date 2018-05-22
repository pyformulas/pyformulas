class object:
    pass

def screen(canvas=None, title='Display'):
    """
    Creates a high framerate window for displaying numpy.ndarray image data. To update the window contents, *self.update()* must be called.
    """

    from ._formulas.screen import screen
    globals()['screen'] = screen

    return screen(canvas, title)

audio = object()
def _play(wavedata, bitrate=None, duration=None, num_channels=1, bit_depth=2, block=False):
    """
    Plays a stream of mono 8-bit audio. (Stereo streams not supported yet)

    If *block* is False, then plays the audio in a separate thread.
    """

    from ._formulas.audio.play import play
    globals()['audio'].play = play

    return play(wavedata, bitrate, duration, num_channels, bit_depth, block)
audio.play = _play


def download(url, out_path=None, get_headers=False, get_body=None):
    """
    Retrieves *url* and returns the response as bytes.

    If a location is set in *out_path*, then saves the response to that location.
    """

    from ._formulas.download import download
    globals()['download'] = download

    return download(url, out_path, get_headers, get_body)

def thread(function, args=(), kwargs={}, callback=None):
    """
    Starts *function* in a new thread.

    If *callback* is set, then passes *function*'s return value to *callback*.
    """

    from ._formulas.thread import thread
    globals()['thread'] = thread

    return thread(function, args, kwargs)

def settimeout(function, delay, repeat=False, args=(), kwargs={}):
    """
    Calls *function* after *delay*. If *repeat* is True, then calls *function* repeatedly every *delay* seconds.
    """

    from ._formulas.settimeout import settimeout
    globals()['settimeout'] = settimeout

    return settimeout(function, delay, repeat, args, kwargs)

net = object()
from ._formulas.net.Stream import Stream as _Stream # Import directly since it's used as a class
net.Stream = _Stream

def discrete_search(root_obj, expansion_fn, goal_fn, heuristic_fn=None):
    """
    Searches for a goal object, starting from an initial object. Uses A* algorithm.

    :param root_obj: Initial object
    :param expansion_fn: Takes an object and returns (child_objects, step_costs). step_costs is a list of the costs of transitioning to each child.
    :param goal_fn: Returns whether an object is a goal object
    :param heuristic_fn: Returns an estimation of the remaining path length between an object and the nearest goal object.
    """

    from ._formulas.discrete_search import discrete_search
    globals()['discrete_search'] = discrete_search

    return discrete_search(root_obj, expansion_fn, goal_fn, heuristic_fn)