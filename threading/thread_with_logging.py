"""
Thread name in logging message
"""
import time
import logging
import threading

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)s) %(message)s',
)


def worker():
    logging.debug('Start')
    time.sleep(3)
    logging.debug('End')


def service():
    logging.debug('Start')
    time.sleep(3)
    logging.debug('End')

w = threading.Thread(target=worker)
s = threading.Thread(target=service, name='MyServce')

w.start()
s.start()
