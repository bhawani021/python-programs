"""
join() blocks indefinitely. It is also possible to pass a timeout argument
"""
import time
import logging
import threading


logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s',)


def daemon():
    logging.debug('Start')
    time.sleep(10)
    logging.debug('End')

d = threading.Thread(target=daemon, name='Daemon')
d.setDaemon(True)


def non_daemon():
    logging.debug('Start')
    logging.debug('End')

t = threading.Thread(target=non_daemon, name='Non Daemon')

t.start()
d.start()

d.join(5)
print('d.isAlive()', d.isAlive())
t.join()

# (Non Daemon) Start
# (Non Daemon) End
# (Daemon    ) Start
# d.isAlive() True
