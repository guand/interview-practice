class Stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		print self.items == []

	def push(self, item):
		self.items.insert(0, item)

	def pop(self):
		self.items.pop(0)

	def size(self):
		print len(self.items)

	def peek(self):
		print self.items[0]

	def print_list(self):
		for i in self.items:
			print i,