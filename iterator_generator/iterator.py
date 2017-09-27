#!/usr/bin/env python
"""
- Any object containing __next__() method is called iterator
- We converts a iterable objects into iterator using iter() function
- Iterator is like a lazy factory, it will be ideal and when we ask for
  value it starts to buzz and produce a single value and returns back to
  ideal state
"""

a = [1, 2]
b = iter(a)
c = iter(a)

# Use of next()
print(next(b))  # 1
print(next(b))  # 2
# print(next(b))  # StopIteration

# Use of __next__()
print(c.__next__())  # 1
print(c.__next__())  # 2
# print(c.__next__())  # StopIteration

print(type(a))  # <class 'list'>
print(type(b))  # <class 'list_iterator'>
print(type(c))  # <class 'list_iterator>


# Fibonacci series using iterator
class fib(object):

    def __init__(self, limit):
        self.limit = limit
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.limit:
            raise StopIteration
        value = self.a
        self.a, self.b = self.b, self.a + self.b

        return value

    def next(self):
        return self.__next__()

f = fib(10)
for data in f:
    print(data)

