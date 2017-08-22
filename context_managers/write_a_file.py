#!/usr/bin/env python

# Example 1: Write a file using context Manager

"""
Context manager allow you to allocate and release resources precisely when you what to.

Use case: Closing file automatically.
"""


with open('text.txt', 'w') as f:
    f.write('Hello there.')


#
class File(object):
    """Context manager as a Class
    """

    def __init__(self, file, method):
        self.f = open(file, method)

    def __enter__(self):
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()


with File('a.txt', 'w') as f:
    f.write('Hi there!!!!')


class File1(object):
    """Context manager- Handling exception
    """

    def __init__(self, file, method):
        self.f = open(file, method)

    def __enter__(self):
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exception has been handled!!!')
        self.f.close()
        # If anything else than True is returned by __exit__ then an exception is raised by the with statement.
        return True

with File1('a1.txt', 'w') as f:
    f.undefined_function()
