#!/usr/bin/python -tt
# coding=utf-8

"""

Averiguar si el contenido de las posiciones PARES
de un vector dado por el usuario es el mismo.
El tamaño máximo del vector es 100

"""

import sys
import pdb
# def analized_vertor(list_1=[1,2,3,4,5,6,7,8,9]):
def analized_vertor(list_1=[1,2,1,4,1,6,1,8,1]):
	if len(list_1) <= 100:
		prev = 0
		enter_first_time = True
		rta = ''
		for index,item in enumerate(list_1):
			if index%2 == 0:
				if enter_first_time:
					enter_first_time = False
					prev = item
				else:
					if prev != item:
						rta = 'X'
						break
					else:
						rta = 'OK'

	else:
		print('La lista es mayor a 100 no podemos analizar su lista')

	return rta



print(analized_vertor())
