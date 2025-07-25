import sys

def main():
	print 'Hello there', sys.argv[1]
	print repeat('william',False)
	print repeat('oscar', True)

def repeat(s,exclaim):
	result = s*3
	# result = s+s+s 
	if exclaim:
		result = result+ '!!!'
	return result


if __name__ == '__main__':
	main()
	sys.exit(0)

