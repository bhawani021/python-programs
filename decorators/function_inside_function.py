#!/usr/bin/env python
"""
function inside another function
"""


def outer(name):
    def inner():
        return 'Hello ' + name

    return inner

call_outer = outer('Bhawani')
print(call_outer())