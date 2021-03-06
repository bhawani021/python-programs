#!/usr/bin/env python
"""
Singleton example
"""


class MySingleton(object):
    __instance = None
    def __new__(self):
        if not self.__instance:
            self.__instance = super(MySingleton, self).__new__(self)
            self.y = 10

        return self.__instance


x = MySingleton()
print(x.y)  # 10
x.y = 20

z = MySingleton()
print(z.y)  # 20
