import time
from threading import Thread


def sleepnprint():
    i = 0
    while True:
        time.sleep(1)
        print(i)
        i += 1


t1 = Thread(target=sleepnprint)
t2 = Thread(target=sleepnprint)

t1.start()
t2.start()
t1.join()
t2.join()
