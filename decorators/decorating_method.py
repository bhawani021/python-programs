#!/usr/bin/env python
"""
Decorating a class method
"""


# Example 1
def deco_greet(func):
    def inner(self):
        return 'Hello {}'.format(func(self))

    return inner


class Person(object):

    def __init__(self, name):
        self.name = name

    @deco_greet
    def greet(self):
        return self.name

p = Person('Bhawani')
print(p.greet())  # Hello Bhawani


# Example 2
def deco_greet1(func):
    def inner(*args, **kwargs):
        return 'Hello {}'.format(func(*args, **kwargs))

    return inner


class Person1(object):

    def __init__(self, name):
        self.name = name

    @deco_greet1
    def greet(self):
        return self.name

p = Person1('Shanker')
print(p.greet())

