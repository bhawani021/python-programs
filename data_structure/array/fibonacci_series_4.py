#!/usr/bin/env python
"""
Fibanacci series using generator
"""


def fib(n):
	a, b = 0, 1
	while a < n:
		yield a
		a, b = b, a + b


if __name__ == '__main__':
	f = fib(10)
	print(list(f))