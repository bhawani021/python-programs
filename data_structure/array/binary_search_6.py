#!/usr/bin/env python
"""
Binary search
"""


def binary_search(arr, min_pos, max_pos, key):
	if max_pos < min_pos:
		return -1

	mid = (min_pos + max_pos) // 2

	print(mid, key, arr)
	if key == arr[mid]:
		return mid

	if key > arr[mid]:
		return binary_search(arr, mid+1, max_pos, key)

	return binary_search(arr, min_pos, mid-1, key) 


	


if __name__ == '__main__':

	arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
	min_pos = 0
	max_pos = len(arr) - 1
	key = 100

	position = binary_search(arr, min_pos, max_pos, key)
	print(position)
