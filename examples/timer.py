import pyformulas as pf
import time

timer = pf.settimeout(lambda: print(time.time()%1), 0.25, repeat=True)

time.sleep(2.5)

timer.stop()