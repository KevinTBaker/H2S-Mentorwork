import sys
import string

def makeCap(string):
	ret = ""
	i = True
	for char in string:
		if i:
			ret += char.upper()
	else:
		ret += char.lower()
	if char != ' ':
		i = not i
	return(ret)

def replaceVowels(string):
	vowels = ['A', 'E', 'I', 'O', 'U']
	for vowel in vowels:
		string = string.replace(vowel, '*')
	return(string)
def check_parenthesis(word):
	stack = []
	opening = ('(', '[', '{')
	closing = (')', ']', '}')
	mappings = dict(zip(opening, closing))
	for char in word:
		if char in opening:
			stack.append(mappings[char])
		elif char in closing:
			if not stack or char != stack.pop():
				return False
	return not stack

def main(argv):
	argc = len(argv)
	if argc == 2:
		caps = makeCap(argv[1])
		print(caps)
		replace = replaceVowels(caps)
		print(replace)
		parens = check_parenthesis(replace)
		print("Balanced? {}".format(parens))
	else:
		print("Error: Invalid Input")
main(sys.argv)
