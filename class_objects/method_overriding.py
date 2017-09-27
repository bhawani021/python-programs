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
        return self.counter + 1


if __name__ == '__main__':

    c = Child()
    value = c.get_value() # Ouput: 6
    print(value)
