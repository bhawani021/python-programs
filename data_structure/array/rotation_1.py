#!/usr/bin/env python
"""
1. Array rotation using temp array
2. Array rotation using rotate one by one
"""


def rotation_1(arr, d):
	n = len(arr)
	
	# Store elements in a temp array
	temp = []
	for i in range(0, d):
		temp.append(arr[i])

	# Shift rest of array
	for i in range(n-d):
		arr[i] = arr[d+i]

	# Store back elements from temp array
	for i in range(d):
		arr[n-d+i] = temp[i]

	return arr


if __name__ == '__main__':
	arr = [10, 20, 30, 40, 50, 60, 70]
	res = rotation_1(arr, 2)
	print(res)








