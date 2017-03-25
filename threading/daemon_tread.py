"""
A program has implicitly waited to exit nutl all threads have completed to work

Daemon thread: Runs without blocking main program
"""
import time
import logging
import threading

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)s) %(message)s')


def daemon():
    logging.debug('Start')
    time.sleep(3)
    logging.debug('End')


def non_daemon():
    logging.debug('Start')
    logging.debug('End')


d = threading.Thread(target=daemon, name='Daemon')
d.setDaemon(True)

t = threading.Thread(target=non_daemon, name='Non-Daemon')

d.start()
t.start()

# Output
# (Daemon) Start
# (Non-Daemon) Start
# (Non-Daemon) End


