
import sys

print 'estamos en utilities_urllib'
print 'estamos en utilities_urllib'
print 'estamos en utilities_urllib'
print 'estamos en utilities_urllib'
def Cat(filename):
	try:
		f = open(filename)
		text = f.read()
		print '----', filename
		print text
	except IOError:
		print 'IOError: el archivo no existe', filename



def main():
	pass
	args = sys.argv[1:]
	for arg in args:
		Cat(arg)

if __name__ == '__main__':
	main()