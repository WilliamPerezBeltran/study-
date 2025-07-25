'''
NOTA IMPORTANTE:
read() en files lo que hace es convertir todo el 
archivo en un string gigante

por ejemmpo 
f = open (filename, 'rU')
string_gigante = f.read()
string_gigante contiene todo el archivo en un string 
'''

import sys

def Names(filename):
	f = open(filename,'rU')
	text = f.read()
	print text
	f.close() 

def main():
	Names(sys.argv[1])

if __name__ == '__main__':
	main()
