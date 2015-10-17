from node import Node

def main():
	node1 = Node(1)
	node2 = Node(2)
	node3 = Node(3)
	node4 = Node(6)
	node1.next = node2
	node2.next = node3
	node3.next = node4

	print_list(node1)

def print_list(node):
	while node:
		print node,
		node = node.next


if __name__ == '__main__':
	main()
