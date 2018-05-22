"""
Basic multithreading with pf.thread
"""

import pyformulas as pf
import time

def count_to(num):
    for i in range(1, num+1):
        print("%i..." % i)

        time.sleep(0.5)

thread = pf.thread(count_to, (10,))

time.sleep(2.5)
print("foo")
thread.join()
print('Done')