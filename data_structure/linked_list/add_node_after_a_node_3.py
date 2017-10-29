#!/usr/bin/env python
"""
Add node after a node
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
		print(' ')

	def insert_after_a_node(self, prev_node, new_data):
		new_node = Node(new_data)
		new_node.next = prev_node.next
		prev_node.next = new_node


if __name__ == '__main__':
	l = LinkedList()


	values = [10, 20, 40, 50, 50, 70]
	for i, v in enumerate(values):
		if i == 0:
			l.head = Node(v)
			data = l.head
		else:
			data.next = Node(v)
			data = data.next
		
	l.printList()

	# Insert a new node after second node
	second_node = l.head.next
	l.insert_after_a_node(second_node, 30)
	# Print after inserting a new node
	l.printList()





	
