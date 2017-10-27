#/usr/bin/env python
"""
Search, insert and delete in an unsorted array
"""

def find_element(arr, key):
	total = len(arr)
	for i in range(total):
		if key == arr[i]:
			return i

	return -1


def insert_element(arr, position, value):
	n = len(arr)
	for i in range(n -1 , position - 1, -1):
		arr[i] = arr[i-1]

	arr[position] = value

	return n - 1


def delete_element(arr, position):
	n = len(arr)
	for i in range(position, n-1):
		arr[i] = arr[i+1]
		# print(i)

	return arr




if __name__ == '__main__':
	arr = [10, 30, 20, 50, 40]
	key = 40
	index = find_element(arr, key)
	if index != -1:
		print('Element found at position: {}'.format(index+1))

	arr = [10, 30, 20, 50, 40, 0]
	res = insert_element(arr, 5, 15)
	print(res)

	arr = [10, 30, 20, 50, 40]
	print('Before delete: {}'.format(arr))
	
	n = delete_element(arr, 2)
	print('After deletion')
	for i in range(len(arr) - 1):
		print(arr[i], end=' ')
	print('')
	
	