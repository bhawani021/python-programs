#!/usr/bin/env python
"""
Prime number
"""


def prime(max):
	prime_nums = []
	for number in range(2, max):
		for val in range(2, number):
			if number % val == 0:
				break;
		else:
			prime_nums.append(number)

	return prime_nums


if __name__ == '__main__':
	res = prime(20)
	print(res)

