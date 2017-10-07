#!/usr/bin/env python
"""
Multiple Inheritance
"""


class Father():
    def gardending(self):
        print('I enjoy gardending')


class Mother():
    def cooking(self):
        print('I love cooking')


class Child(Father, Mother):
    def sports(self):
        print('I enjoy sports')


c = Child()
c.gardending()
c.cooking()
c.sports()