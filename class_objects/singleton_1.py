#!/usr/bin/env python
"""
Singleton example
"""


def singleton(myClass):
    instance = {}

    def get_instance(*args, **kwargs):
        if myClass not in instance:
            instance[myClass] = myClass(*args, **kwargs)
            return instance[myClass]
    return get_instance


@singleton
class TestClass(object):
    pass

x = TestClass()