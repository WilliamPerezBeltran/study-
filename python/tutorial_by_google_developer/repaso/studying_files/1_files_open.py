import sys 

# NOTA:
# Esta forma de leer lo hace una por una linea 

def Names(filename):

	f = open(filename,'rU')
	for line in f:
		print line, ##si le pongo coma al final no deja linea que las separe
	f.close()


def main():
	Names(sys.argv[1])

if __name__ == '__main__':
	main()
