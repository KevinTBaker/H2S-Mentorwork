import sys

def main(argv):
	for i in range(len(argv)):
		if i > 0:
			print("Arg Number {}: ".format(i), argv[i].rstrip('[]'))
	lst = argv[1:]
	lst.sort(key=len, reverse=True)
	for item in lst:
		print(item)
main(sys.argv)
