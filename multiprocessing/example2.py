#!/usr/bin/env python
"""
Multiprocessing
    Every process has its own address space (virtual memory).
    Thus program varaibles are not shared between processes.
    You need to use interprocess communication (IPC) techniques
    if you want to share data between two processes.
"""
import multiprocessing

square_result = []


def cal_square(numbers):
    global  square_result
    for n in numbers:
        print('Squares ', n*n)
        square_result.append(n * n)

    print('Within a process: result ', square_result)


if __name__ == '__main__':
    arr = [2, 3, 8, 9]
    p1 = multiprocessing.Process(target=cal_square, args=(arr,))
    p1.start()
    p1.join()

    print('result', square_result)

    """
    Output:
        Squares  4
        Squares  9
        Squares  64
        Squares  81
        Within a process: result  [4, 9, 64, 81]
        result []
    """

