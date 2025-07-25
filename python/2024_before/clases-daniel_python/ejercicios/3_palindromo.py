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


def palindromo(s):

	new_array = []
	for x in range(len(s)-1,-1,-1):
		new_array.append(s[x].lower())

	if s.lower() == ''.join(new_array):
		return ("el string {} es palindromo y su palindr... es {} ".format(s,''.join(new_array)))
	else:
		return("el string {} no palindromo y su palindr... es {} ".format(s,''.join(new_array)))




def main():
	arg = sys.argv[1:]
	print(palindromo(arg[0]) )

if __name__=='__main__':
	main()
