#!/usr/bin/env python
"""
Share data between processes using Array and Value
"""
import multiprocessing


def cal_square(numbers, result, v):
    v.value = 10.5
    for id, val in enumerate(numbers):
        result[id] = val*val

    print('Within process:', result[:])


if __name__ == '__main__':
    numbers = [2, 3, 5]
    result = multiprocessing.Array('i', 3)
    v = multiprocessing.Value('d', 0.0)
    p = multiprocessing.Process(target=cal_square, args=(numbers, result, v))

    p.start()
    p.join()

    print('Outside process:', result[:])
    print(v.value)
