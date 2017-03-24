#!/usr/bin/env python
"""
Passing arguments to a decorator method
"""


def p_greet(arg):
    def p_greet_decorator(func):
        def inner(name):
            return '{} {}'.format(arg, func(name))
        return inner
    return p_greet_decorator


@p_greet('Hello')
def message(name):
    return name

m = message('Bhawani')

# Attribute of message is overridden  by wrapper function inner
print(message.__name__)   # inner


# Use of funtools.wraps to avoid overriding
from functools import wraps


def p_greet1(arg):
    def p_greet_decorator(func):
        @wraps(func)
        def inner(name):
            return '{} {}'.format(arg, func(name))
        return inner
    return p_greet_decorator


@p_greet1('Hello')
def message1(name):
    return name

m = message1('Shanker')
print(m)

print(message1.__name__)  # message1





