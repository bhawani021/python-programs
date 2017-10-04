#!/usr/bin/env python
"""
Multiprocessing Pool
"""
import time
import multiprocessing


def f(n):
    sum = 0
    for x in range(1000):
        sum += x*x

    return sum


if __name__ == '__main__':
    t = time.time()
    p = multiprocessing.Pool()
    result = p.map(f, range(1, 100000))
    p.close()
    p.join()

    print('Pool took: ', time.time() - t)

    t1 = time.time()
    result = []
    for x in range(100000):
        result.append(f(x))

    print('Serial processing took: ', time.time() - t1)
    """
    output
        Pool took:  8.6281099319458
        Serial processing took:  17.258402109146118
    """