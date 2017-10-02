#!/usr/bin/env python
"""
Metaclasses
    - Creates classes
    - Python classes are objects, metaclasses are what create these objects.
    - They are classes'classes
    - function type is a metaclass
    - class factory
"""

age = 35
name = 'bob'


def foo():
    pass


class Bar(object):
    pass


if __name__ == '__main__':
    print(age.__class__)  # <class 'int'>
    print(name.__class__)  # <class 'str'>
    print(foo.__class__)  # <class 'function'>
    print(Bar.__class__)  # <class 'type'>
    print(Bar().__class__)  # <class '__main__.Bar'>

    print(age.__class__.__class__)  # <class 'type'>
    print(name.__class__.__class__)  # <class 'type'>
    print(foo.__class__.__class__)  # <class 'type'>
    print(Bar().__class__.__class__)  # <class 'type'>