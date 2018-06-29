import sys

def print_colorful_text(string, st, fg, bg):
	color_format = ';'.join([st, fg, bg])
	print("\x1b[{}m {} \x1b[0m".format(color_format, string))


def main(argv):
	argc = len(sys.argv)
	if argc == 5:
		print_colorful_text(argv[1], argv[2], argv[3], argv[4])
	else:
		print("Invalid number argument: Requires 4")

main(sys.argv)
