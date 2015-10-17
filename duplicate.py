def remove_duplicate(a):
	for i in set(a):
		if i != None:
			print i,
	print


def remove_duplicate_dic(a):
	a_dic = {}
	for i in a:
		a_dic[i] = i
	for key, value in a_dic.items():
		print value,
	

def main():
	a = "aabbc"
	remove_duplicate(a)
	remove_duplicate_dic(a)

if __name__ == "__main__":
	main()