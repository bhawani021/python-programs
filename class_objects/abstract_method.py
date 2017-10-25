#!/usr/bin/env python
"""
Abstract class example
"""
from abc import ABCMeta, abstractmethod


class Animal(object):

	__metaclass__ = ABCMeta


	@abstractmethod
	def say_something(self):
		return 'I am an animal'


class Cat(Animal):

	def say_something(self):
		s = super(Cat, self).say_something()
		return '{} {}'.format(s, 'Maiuu')


if __name__ == '__main__':
	c = Cat()
	print(c.say_something())
