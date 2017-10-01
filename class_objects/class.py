#!/usr/bin/env python
import datetime


class User(object):

    location = 'Bangalore'

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    @classmethod
    def get_location(cls):
        return cls.location

    @staticmethod
    def get_currnet_time():
        return datetime.datetime.now()

if __name__ == '__main__':

    u = User('Bhawani')
    print(u.get_name())

    print(User.get_currnet_time())
    print(User.get_location())
