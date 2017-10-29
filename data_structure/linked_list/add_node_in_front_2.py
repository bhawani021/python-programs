#!usr/bin/env python
"""
Add node in front
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
			print(temp.data, end= ' ')
			temp = temp.next
		print(' ')

	def push(self, data):
		new_node = Node(data)
		new_node.next = self.head

		self.head = new_node


if __name__ == '__main__':

	first = Node(20)
	second = Node(30)
	third = Node(50)

	second.next = third
	first.next = second

	l = LinkedList()
	l.head = first
	l.printList()

	# Add new node
	l.push(10)

	# Print linked list
	l.printList()

	# Time coplexity: O(1)