#!/usr/bin/env python
"""
Fibanacci series using loop
"""


def fib(n):
	a, b = 0, 1
	for i in range(n):
		a, b = b, a + b
		print(a, end=' ')


if __name__ == '__main__':
	fib(10)
    
