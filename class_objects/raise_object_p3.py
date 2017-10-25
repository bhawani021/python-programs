#!/usr/bin/env python
"""
Python3
	- New class objects can't be raised unless derived from Exception
"""


class New(object):
	pass


raise New()
# Traceback (most recent call last):
#   File "class_objects/raise_object_p3.py", line 12, in <module>
#     raise New()
# TypeError: exceptions must derive from BaseException


class New1(Exception):
	pass

raise New1()
# Traceback (most recent call last):
#   File "class_objects/raise_object_p3.py", line 22, in <module>
#     raise New1()
# __main__.New1