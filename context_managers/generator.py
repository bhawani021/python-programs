#!/usr/bin/env python
from contextlib import contextmanager


@contextmanager
def open_file(name):
    f = open(name, 'w')
    yield f
    f.close()


with open_file('aa.txt') as file:
    file.write('Yahoo!!!!!!!!!!!!!!!')