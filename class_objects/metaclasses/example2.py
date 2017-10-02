#!/usr/bin/env python
"""
Creating classes dynamically
    - As classes are objects in Python, you can create them on the fly like any object
"""


def choose_class(name):
    if name == 'foo':
        class Foo(object):
            pass

        return Foo
    else:
        class Bar(object):
            pass

        return Bar

if __name__ == '__main__':
    my_class = choose_class('foo')
    print(my_class)  # <class '__main__.choose_class.<locals>.Foo'>
    print(my_class())  # <__main__.choose_class.<locals>.Foo object at 0x102915208>
