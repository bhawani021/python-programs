#!/usr/bin/env python
"""
Multithreading example: Running two tasks sequentially
"""
import time


def cal_square(numbers):
    print('Calculate square')
    for n in numbers:
        time.sleep(0.2)
        print('squares:', n*n)


def cal_cube(numbers):
    print('Calculate Cube')
    for n in numbers:
        time.sleep(0.2)
        print('Cube', n*n*n)


if __name__ == '__main__':

    numbers = [2, 3, 8, 9]

    t = time.time()
    cal_square(numbers)
    cal_cube(numbers)
    print('Time Taken: {}'.format(time.time()-t))
