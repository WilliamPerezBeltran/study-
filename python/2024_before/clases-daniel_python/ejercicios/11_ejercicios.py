#!/usr/bin/python -tt
# coding=utf-8

"""
1)Método de ordenamiento burbuja
Revisa cada elemento de la lista 
con el siguiente elemente intercambiando los elementos de posicion 
si estan en el orden equivocado
Ejemplo
4 2 6 8 5 7
2 4 6 8 5 7
2 4 6 5 8 7
2 4 6 5 7 8
2 4 5 6 7 8
este ordenamiento no estan eficiente pero es bueno para estudiarlo
"""
"""
4 2 6 8 5 7
2 4 6 8 5 7
2 4 6 8 5 7
2 4 6 5 8 7
2 4 6 5 7 8 
2 4 5 6 7 8
"""
def burbuja(array):
	for b in range(len(array)-1,0,-1):
		for u in range(b):
			if array[u]>array[u+1]:
				original=array[u]
				array[u]=array[u+1]
				array[u+1]=original

def main():
	lista=[34,32,1,2,3,5,4,3,4,5,4,7,6,53,98]
	burbuja(lista)
	print(lista)

if __name__=='__main__':
	main()
