#!/usr/bin/env python
"""
Given a number x, find two elements in array which are equal to x
"""


def sum_two_numbers(arr, num):
	left = 0
	right = len(arr) - 1

	while left < right:
		if  arr[left] + arr[right] == num:
			return arr[left], arr[right]
		elif arr[left] + arr[right] > num:
			right -= 1
		else:
			left += 1

	return -1
	


def sort_arr(arr):
	size = len(arr)
	for i in range(size):
		for j in range(size-i-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]

if __name__ == '__main__':
	arr = [0, 8, 9, 3, 19, -5, 4, 2]
	sort_arr(arr)

	print('Array after sorting: {}'.format(arr))
	
	res = sum_two_numbers(arr, 17)
	print(res)
