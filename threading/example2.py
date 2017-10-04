#!/usr/bin/env python
import time
import threading


def cal_square(numbers):
    print('Calculate square')
    for n in numbers:
        time.sleep(0.2)
        print('Square:', n*n)


def cal_cube(numbers):
    print('Calculate cube')
    for n in numbers:
        time.sleep(0.2)
        print('Cube', n*n*n)


numbers = [2, 3, 8, 9]
t = time.time()

t1 = threading.Thread(target=cal_square, args=(numbers,))
t2 = threading.Thread(target=cal_cube, args=(numbers,))

t1.start()
t2.start()

t1.join()
t2.join()

print('Done in: ', time.time() - t)

