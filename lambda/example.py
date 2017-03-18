"""
lambda syntax
    lambda argument_list: expression
"""
from functools import reduce


# Add two numbers
add = lambda x, y: x + y

# Square a number
sqr = lambda x: x**2


# Increment of a number
def do_increment(num):
    """
    Increase a number
    :param num: int
    :return: int
    """

    return lambda x: x + num

# Use with filter
nums = range(1, 15)
new_filtered_nums = filter(lambda x: x % 2 == 0, nums)

# use with map
nums = range(1, 10)
new_mapped_nums = map(lambda x: x + 1, nums)

# Use with reduce
nums = range(1, 10)
new_reduced_nums = reduce(lambda x, y: x + y, nums)

# Find length of each words in a string using lambda and list comprehension
st = 'My name is Bhawani Shanker'
words_length = [(lambda x: len(x))(x) for x in st.split()]

# Find length of each words in a string using lambda and map
st = 'World is so beautiful'
wl = map(lambda x: len(x), st.split())


if __name__ == '__main__':
    # Sum of two numbers
    result = add(10, 20)
    print(result)

    # Square a number
    result = sqr(10)
    print(result)

    # Increase a number
    increase = do_increment(5)
    result = increase(10)
    print(result)

    # Use with filter
    print(list(new_filtered_nums))

    # Use with map
    print(list(new_mapped_nums))

    # Use of reduce
    print(new_reduced_nums)

    # Find words length using lambda and list comprehension
    print(list(words_length))

    # Find words length using lambda and map
    print(list(wl))








