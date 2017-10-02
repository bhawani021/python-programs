#!/usr/bin/env python
"""
Use of type function
"""

MyShinyClass = type('MyShinyClass', (), {})


"""
class Foo(object):
    bar = True
"""
Foo = type('Foo', (), {'bar': True})

"""
class FooChild(Foo):
    pass
"""


def echo_bar(self):
    print(self.bar)

FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar})

if __name__ == '__main__':
    print(MyShinyClass)  # <class '__main__.MyShinyClass'>
    print(MyShinyClass()) # <__main__.MyShinyClass object at 0x10063e898>

    print(Foo)  # <class '__main__.Foo'>
    print(Foo())  # <__main__.Foo object at 0x102133860>
    f = Foo()
    print(f.bar)  # True

    print(FooChild)  # <class '__main__.FooChild'>
    print(FooChild.bar)  # True

    print(hasattr(FooChild, 'echo_bar'))  # True
    f1 = FooChild()
    print(f1.echo_bar())
