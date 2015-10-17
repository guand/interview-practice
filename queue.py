class Queue:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		print self.items == []

	def enqueue(self, item):
		self.items.insert(0, item)

	def dequeue(self):
		self.items.pop()

	def size(self):
		print len(self.items)

	def peek(self):
		print self.items[0]

	def print_list(self):
		for i in self.items:
			print i,