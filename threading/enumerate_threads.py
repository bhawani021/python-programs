#!/usr/bin/env python
"""
Enumerating threads
"""
import time
import logging
import threading
import random
logging.basicConfig(level=logging.DEBUG, format='[%(threadName)s] %(message)s')


def worker():
    t = threading.currentThread()
    pause = random.randint(1, 5)
    logging.debug('Sleeping {}'.format(pause))
    time.sleep(pause)
    logging.debug('Ending')
    return

for i in range(5):
    t = threading.Thread(target=worker)
    t.setDaemon(True)
    t.start()

main_thread = threading.currentThread()
for t in threading.enumerate():
    if t is main_thread:
        continue
    logging.debug('Joining {}'.format(t.getName()))
    t.join()



