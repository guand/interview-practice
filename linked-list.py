from node import SingleList

def main():
	l = SingleList()
	l.append(1)
	l.append(3)
	l.append(9)
	l.remove(3)
	l.remove(55)
	l.show()

def print_list(node):
	while node:
		print node,
		node = node.next


if __name__ == '__main__':
	main()
