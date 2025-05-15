import sys

def main():
	print repeat('oscar', True)

def repeat(s,exclaim):
	raw = 'this\t\n and that'
	print raw

	multi ="""the life is life
	it is short """
	print multi

	string= 'my string'

	print string.isalpha()
	print string.isdigit()
	print string.isspace()
	print string.startswith('m')
	print string.endswith('g')
	print string.find('string')
	print string.replace('my','all my')
	print string.split()
	print '--'.join(['1','2'])

	string1 = 'Hello we are here'

	print string1[1]
	print string1[1:7]
	print string1[:]
	print string1[0:14]
	print string1[:14]
	print string1[:16]

	print string1[-1]
	print string1[-2]
	print string1[-3]
	print string1[:-3]
	print string1[-3:]
	print string1[:5] + string1[5:]

	ustring = u'A unicode \u018e string \xf1'
	print ustring 
	print type(ustring)

	s = ustring.encode('utf-8')

	print s 
	print type(s)

	t = unicode(s, 'utf-8')
	print t
	print type(t)


	# print type(ustring)

	# s = ustring.encode('utf-8')
	# print type(s)
	# print s

	# t = unicode(s, 'utf-8') 
	# print t == ustring     
	# print t     

	return ''


if __name__ == '__main__':
	main()
	sys.exit(0)

