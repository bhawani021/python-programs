#!/usr/bin/env python
"""
Delete a node
"""


class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList(object):
	def __init__(self):
		self.head = None

	def printList(self):
		temp = self.head
		while temp:
			print(temp.data, end=' ')
			temp = temp.next
		print('')

	def delete(self, key):

		temp = self.head

		# If head node itself holds the key to be deleted.
		if temp:
			if temp.data == key:
				self.head = temp.next
				temp = None
				return

		while temp:
			if temp.data == key:
				break

			prev = temp
			temp = temp.next

		if temp is None:
			return

		prev.next = temp.next
		temp = None



if __name__ == '__main__':
	values = [10, 20, 30, 40, 50, 60, 70, 80]

	l = LinkedList()
	for i, v in enumerate(values):
		if i == 0:
			data = Node(v)
			l.head = data
		else:
			data.next = Node(v)
			data = data.next

	l.printList()

	# Delete a node
	l.delete(70)

	# Print after delete
	l.printList()
