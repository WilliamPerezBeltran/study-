"""
valor suministrado 5
resultado 1335555777777779999999999999999
n = 5 =>  1 33 5555 77777777 9999999999999999

tenemos que 1,3,5,7,9 son impares

1. la secuencia esta formada por numeros impares
2. cada numero impar se escribe tantas veces como lo indique
la potencia de 2 correspondiente
2**0 = 1
2**1 = 2
2**2 = 4
2**3 = 8
2**4 = 16

3. la cantidad de grupos de numeros impares coincide con el valor dado por el usuario

"""

import sys 
import pdb

def way_one_serie(n):
	impar = 1
	new_array = []

	for x in range(n):
		for y in range(2**x):
			new_array.append(impar)
		impar+=2
	return new_array


def main():
	arg = sys.argv[1:]
	print(*way_one_serie( int(arg[0]) ), sep=", ")

if __name__=='__main__':
	main()
