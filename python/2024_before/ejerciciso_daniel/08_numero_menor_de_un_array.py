#valor suministrado 4
#resultado: 1 4 4 9 9 9 16 16 16 16 16

import sys
import pdb

def numero_menor_de_un_array():
	# a = [1,2,4,2,3,2,54,5,67,4,3,6,3]
	a = [12,23,34,54,43,23,12,1212,6767,4454,3,34,2,46,576,87,87,4,53,5567,56,0]

	pivote = True
	for x in a:
		if pivote:
			menor = x
			pivote = False
		else:
			if x < menor:
				menor = x

	print(a)
	print(menor)





def main():
	numero_menor_de_un_array()

if __name__=='__main__':
	main()
