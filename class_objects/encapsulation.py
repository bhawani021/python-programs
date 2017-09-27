#!/usr/bin/env python
"""
Encapsulation:
    We can restrict access to class methods and variables.
    This can prevent the data from being modified by accident
    and called encapsulation.

Encapsulation prevents from accessing accidentally, but not intentionally.
"""


class Person(object):

    def __init__(self):
        self.__dob()

    def __dob(self):
        print('21/07/1984')

    def name(self):
        print('bhawani')

if __name__ == '__main__':
    p = Person()
    print(dir(Person))
    p.name()
    # 21/07/1984
    # bhawani
