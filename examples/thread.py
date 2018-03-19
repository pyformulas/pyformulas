import pyformulas as pf
import time

def count_to(num):
    for i in range(1, num+1):
        print("%i..." % i)

        time.sleep(1)

pf.thread(count_to, (10,))

time.sleep(5)
print("foo")