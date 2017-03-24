#!/usr/bin/env python
"""
Decorators example
"""


# Example 1
def d_greet(func):
    def inner(name):
        return 'Hello ' + func(name)

    return inner


@d_greet
def message(name):
    return name

call_message = message('Bhawani')
print(call_message)


# Example 2
def decorator1(func):
    def inner(name):
        return 'Hello {}. '.format(func(name))

    return inner


def decorator2(func):
    def inner(name):
        return func(name) + 'How are you? '

    return inner


def decorator3(func):
    def inner(name):
        return func(name) + 'And how was your weekend?'

    return inner


@decorator3
@decorator2
@decorator1
def check_decorator(name):
    return name

call_check_decorator = check_decorator('Shanker')
print(call_check_decorator)




