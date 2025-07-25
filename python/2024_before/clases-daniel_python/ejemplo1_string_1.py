#!/usr/bin/python -tt
# coding=utf-8
# B. ambos extremos
# Dada una cadena s, devuelve una cadena hecha de los primeros 2
# y los ultimos 2 caracteres de la cadena original,
# entonces 'spring' produce 'spng'. Sin embargo, si la longitud de la cadena
# es menor que 2, devuelve la cadena vacía.

"""
el comentairio
"""
def main():
	#   multiplos()
	ambos_extremos()

def multiplos():
	for i in range(1,101):
		if i%3 == 0 or i%5 ==0:
			print(i)

def ambos_extremos():
	s="hello"
	resultado="helo"
	1 = string un array 
	crear dos variables 
	asignarl valor a las variables 
	union 
	imprime 

	print("segundo paso : encontrar dos primeros carateres")
	print("tercer paso : encontrar dos ultimos carateres")
	print("unior los caracteres del 2 y del 3")
	print("imprimir")
	pri= s[0:2]
	ult= s[3:]
	a=pri+ult
	print(a)

def ambos_extremos():
	s="hello"
	resultado="helo"
	1 = string un array 
	crear dos variables 
	asignarl valor a las variables 
	union 
	imprime 

	print("segundo paso : encontrar dos primeros carateres")
	print("tercer paso : encontrar dos ultimos carateres")
	print("unior los caracteres del 2 y del 3")
	print("imprimir")
	pri= s[0:2]
	ult= s[3:]
	a=pri+ult
	print(a)

if __name__=='__main__':
	main()