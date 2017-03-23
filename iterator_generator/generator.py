#!/usr/bin/env python
"""
A generator is a special kind of iterator, i.e. a generator is also an iterator.
It produces values lazily
"""


def fib(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

f = fib(10)
for data in f:
    print(data)

# Generator expression
nums = range(1, 10)
squares = (x**2 for x in nums)
print(type(squares))  # <class 'generator'>
print(list(squares))  # [1, 4, 9, 16, 25, 36, 49, 64, 81]






