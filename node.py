class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

	def __str__(self):
		return str(self.data)


class SingleList:
	head = None
	tail = None

	def append(self, data):
		node = Node(data)
		if self.head is None:
			self.head = self.tail = node
		else:
			self.tail.next = node
		self.tail = node

	def show(self):
		current_node = self.head
		while current_node is not None:
			print current_node.data, "-> ",
			current_node = current_node.next
		print None

	def remove(self, data):
		current_node = self.head
		previous_node = None
		while current_node is not None:
			if current_node.data == data:
				if previous_node is not None:
					previous_node.next = current_node.next
				else:
					self.head = current_node

			previous_node = current_node
			current_node = current_node.next


	