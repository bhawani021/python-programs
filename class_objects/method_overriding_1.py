#!/usr/bin/env python
"""
Method overriding
"""


class Parent(object):

    def __init__(self):
        self.counter = 5

    def get_value(self):
        return self.counter


class Child(Parent):

    def get_value(self):
        c = super(Child, self).get_value()
        return c + 10


if __name__ == '__main__':
    c = Child()
    print(c.get_value())
