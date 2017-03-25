"""
Daemon thread with join
 Wait until a daemon thread has completed its work, we can use join() method
"""
import time
import logging
import threading

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')


def daemon():
    logging.debug('Start')
    time.sleep(3)
    logging.debug('End')


d = threading.Thread(name='Daemon', target=daemon)
d.setDaemon(True)


def non_daemon():
    logging.debug('Start')
    logging.debug('End')

t = threading.Thread(name='NonDaemon', target=non_daemon)

d.start()
d.join()
t.start()
t.join()

# Daemon Start
# Daemon End
# NonDaemon Start
# NonDaemon End