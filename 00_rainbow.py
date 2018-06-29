def print_colorful_text(string, style, foreground, background):
	"""
	prints string with colorful text and backgound
	"""
	format = ';'.join([str(style), str(foreground), str(background)])
	s = '\x1b[%sm%s\x1b[0m' % (format, string)
	print(s, end = "")

print_colorful_text("R ", 1, 31, 40)
print_colorful_text("A ", 1, 32, 40)
print_colorful_text("I ", 1, 33, 40)
print_colorful_text("N ", 1, 34, 40)
print_colorful_text("B ", 1, 35, 40)
print_colorful_text("O ", 1, 36, 40)
print_colorful_text("W", 1, 37, 40)
print('\n')
BOLD = 1
DIM = 2
UNDERLINED = 4
BLINK = 5
REVERSE = 7
FG_BLACK = 30
FG_RED = 31
FG_GREEN = 32
FG_YELLOW = 33
FG_BLUE = 34
FG_MEGENTA = 35
FG_CYAN = 36
FG_LIGHT_GRAY = 37
BG_BLACK = 40
BG_RED = 41
BG_GREEN = 42
BG_YELLOW = 43
BG_BLUE = 44
BG_MEGENTA = 45
BG_CYAN = 46
BG_LIGHT_GRAY = 47

print_colorful_text("I am Groot", BOLD, FG_GREEN, BG_BLUE)
