import sys

def convert_base(num, base=2):
	data = []
	digits = "0123456789ABCDEF"
	while num:
		data.append(digits[num % base])
		num //= base
	return "".join(data[::-1])


def main(args):
	if len(args) == 2:
		casted_arg  = int(args[1])
		print(f"""{convert_base(casted_arg)}
	{convert_base(casted_arg, base=16)}
	{convert_base(casted_arg, base=8)}""")

if __name__ == "__main__":
	main(sys.argv)
