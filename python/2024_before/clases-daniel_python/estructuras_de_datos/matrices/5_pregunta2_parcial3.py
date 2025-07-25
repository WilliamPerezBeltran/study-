#!/usr/bin/python -tt
# coding=utf-8

def triangulo():
	matriz=[
	[1,1,1,1],
	[1,1,1,1],
	[1,1,1,1],
	[1,1,1,1]]

	tuplas = (('s','superior'),('i','inferior'),('n','sin orientacion'))

	superior=0
	inferior=0
	rta = None

	for i in range(len(matriz)):
		for j in range(len(matriz)):
			if i<j:
				superior+=matriz[i][j]
			elif i>j:
				inferior+=matriz[i][j]

	if superior>inferior:
		rta = 's'
	elif superior<inferior:
		rta = 'i'
	else:
		rta = 'n'

	for item_tupla in tuplas:
		if item_tupla[0] == rta:
			return item_tupla[1]

def main():
	print(f"el resultado de la matriz es {triangulo()}")


if __name__=='__main__':
	main()

