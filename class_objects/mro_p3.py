#!/usr/bin/env
"""
Python3

New stype classes
	- Base class is only searched once all its derived classes have been done.
	- They have __mro__ attribute
""" 

class C(object): i = 0


class C1(C): pass


class C2(C): i = 2


class C12(C1, C2): pass


class C21(C2, C1): pass


if __name__ == '__main__':
	print(C12.i) # 2
	print(C21.i) # 2
	print(C12.__mro__)
	# (<class '__main__.C12'>, <class '__main__.C1'>, <class '__main__.C2'>, <class '__main__.C'>, <class 'object'>)
	print(C21.__mro__)
	# (<class '__main__.C21'>, <class '__main__.C2'>, <class '__main__.C1'>, <class '__main__.C'>, <class 'object'>)
