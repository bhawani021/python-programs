#!/usr/local/bin python
"""
Objects which can be used with a for loop called iterable
    1. list
    2. set
    3. tuple
    4. dict
    5. string
"""

# Use list
print('Use list in a for loop')
for data in [1, 2, 3, 4]:
    print(data, end=' ')

# Use set
print('\nUse set in a for loop')
for data in {1, 2, 3, 4}:
    print(data, end=' ')

# Use tuple
print('\nUse tuple in for loop')
for data in (1, 2, 3, 4):
    print(data, end=' ')

# Use dict
print('\nUse dictionary in for loop')
for data in {1: 'one', 2: 'two', 3: 'three', 4: 'four'}:
    print(data, end=' ')

# Use string
print('\nUse string in for loop')
for data in 'World':
    print(data, end=' ')

# Some function consumes iterable
print('\nfunction consuming iterable')

# Covert a list into string
print(''.join(['a', 'b', 'c', 'd']))

# Convert a string into list
print(list('python'))

# Convert a dictionary into list
print(list({1: 'one', 2: 'two', 3: 'three', 4: 'four'}))



