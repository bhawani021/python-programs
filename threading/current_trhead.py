#!/usr/bin/env python
"""
Current thread
"""
import time
import threading


def worker():
    print(threading.current_thread().getName(), 'Start')
    time.sleep(3)
    print(threading.current_thread().getName(), 'End')


def service():
    print(threading.current_thread().getName(), 'Start')
    time.sleep(3)
    print(threading.current_thread().getName(), 'End')


thread1 = threading.Thread(name='a_worker', target=worker)
thread2 = threading.Thread(target=service)

thread1.start()
thread2.start()
