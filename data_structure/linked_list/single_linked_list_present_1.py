#!/usr/bin/env python
"""
Presentation of linked list
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
		while(temp):
			print(temp.data, end=' ')
			temp = temp.next
		print(' ')


if __name__ == '__main__':
	first = Node(1)  # First node
	second = Node(2)  # Second node
	third = Node(3)  # Third node

	l = LinkedList()
	l.head = first

	l.head.next = second

	second.next = third

	l.printList()

