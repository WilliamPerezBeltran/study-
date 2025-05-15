import sys 

def main():
	print strings()

def strings():
	s = 'hi'
	print s[0]
	print s[1]
	print len(s)
	print s + ' ole'
	raw = r'this\t\n and that'
	print 'LOWER'.lower()
	a = '---'.join(['aaa', 'bbb', 'ccc'])
	string = ' william fernando perez '
	print string.strip()[0]
	print string.strip()[1]
	print string.strip()[2]
	print string.strip()[0:7]
	print string.strip()[3:7]
	  # % operator
	print "%d little %s, and %s, or %s" % (3, 'huff', 'puff', 'house')
	print "%d the way of concatenate %s " % (100, 'YES')
	 # Add parentheses to make the long line work:
	text = ("%d pigs %s, and %s your %s down."
		% (3, 'huff', 'puff', 'house'))
	print text
	# Split the line into chunks, which are concatenated automatically by Python
	text1 = (
	"%d little pigs come out, "
	"or I'll %s, and I'll %s, "
	"and I'll blow your %s down."
	% (3, 'huff', 'puff', 'house'))
	print text1
	return ''

if __name__ == '__main__':
	main()