#!/usr/bin/env
"""
Python2

Classic classes
	- They do depth first search from left to right and stop on first match.
	- They don't have __mro__ attribute
""" 

class C(): i = 0


class C1(C): pass


class C2(C): i = 2


class C12(C1, C2): pass


class C21(C2, C1): pass


if __name__ == '__main__':
	print(C12.i) # 0
	print(C21.i) # 2
