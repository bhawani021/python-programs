#!/usrbin/env python
"""
Add note at end of a linked list
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

	def add_node_at_end(self, data):
		new_node = Node(data)

		last = self.head
		while last.next:
			last = last.next

		last.next = new_node


if __name__ == '__main__':

	l = LinkedList()

	values = [10, 20, 30, 40, 50]
	for i, v in enumerate(values):
		if i == 0:
			data = Node(v)
			l.head = data
		else:
			data.next = Node(v)
			data = data.next

	# Print list before inserting a value
	l.printList()

	# Insert a new node at end
	l.add_node_at_end(60)

	# Print list after inserting node at end
	l.printList()

	# Time complexity: O(n)
