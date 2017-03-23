#!/usr/local/env python
"""
An object is a container if it can be asked whether it contains a certain element.
    1. list
    2. set
    3. tuple
    4. dict
    5. string

We can perform membership tests on a container
"""

# Use list
data = [1, 2, 3, 4]
print(2 in data, 10 in data)

# Use set
data = {1, 2, 3, 4}
print(2 in data, 10 in data)

# Use tuple
data = (1, 2, 3, 4)
print(2 in data, 10 in data)

# Use dict, it checks key
data = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
print(2 in data, 10 in data)

# Use string
st = 'World'
print('W' in st, 'x' in st)
