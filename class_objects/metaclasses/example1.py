#!/usr/bin/env python
"""
classes and objects
    - classes are objects too in Python.
    - As soon as you use the keyword class, python executes it and creates an OBJECT.
    - Object (the class) is itself capable of creating object (the instance), and this is whu it's a class.
    - As class is a object, therefore
        - You can assign it to a varible
        - You can copy it
        - You can add attributes to it
        - You can pass it as a function parameter
"""


class ObjectCreator(object):
    pass


if __name__ == '__main__':
    my_object = ObjectCreator()
    print(my_object)  # <__main__.ObjectCreator object at 0x10283e898>

    print(ObjectCreator)  # <class '__main__.ObjectCreator'>

    # Check attribute
    print(hasattr(ObjectCreator, 'new_attribute'))  # False
    # Add attribute
    ObjectCreator.new_attribute = 'foo'
    # Check attribute
    print(hasattr(ObjectCreator, 'new_attribute'))  # True
    # Print attribute
    print(ObjectCreator.new_attribute)  # foo

    # Assign a class to a variable
    ObjectCreatorMirror = ObjectCreator
    # Check attribute
    print(hasattr(ObjectCreatorMirror, 'new_attribute'))  # True
    # Print attribute
    ObjectCreatorMirror.new_attribute1 = 'foo1'
    print(ObjectCreatorMirror.new_attribute1)  # foo1
    print(ObjectCreator.new_attribute1)  # foo1

    print(ObjectCreatorMirror()) # <__main__.ObjectCreator object at 0x10072ba90>

