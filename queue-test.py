from queue import Queue

def main():
	q = Queue()
	q.isEmpty()
	q.enqueue(9)
	q.enqueue(2)
	q.enqueue(3)
	q.isEmpty()
	q.size()
	q.peek()
	q.print_list()


if __name__ == '__main__':
	main()