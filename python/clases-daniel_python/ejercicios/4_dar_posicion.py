"""

hacer un programa que diga si la palabra o la frase es palindromo o no 

ejemplo 
"A torre da derrota" es palandromo
"ana" es palandromo
"""

"""


1. dividir la palabra en sus respectivos caracteres
2. coger el nuevo array e invertirlo
3. mirar si el nuevo array invertido es igual al string
4. si es verdadero es porque es palindromo 
5. si no es porque no es palindromo 

"""

import sys 
import pdb



def posicion():
	z=0
	for posicion, valor in enumerate([2,3,4,5,56,7]):
		print("%d => %d "%(posicion, valor))


	new_array = []
	for x in range(5):
		new_array.append(x)
	print(new_array)

	#list comprehensions

	new_array = [x for x in range(5)]
	print(new_array)
		#z=z+1


def main():
	posicion()

if __name__=='__main__':
	main()
