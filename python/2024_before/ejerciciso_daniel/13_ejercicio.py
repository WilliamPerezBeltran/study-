#!/usr/bin/python -tt
# coding=utf-8

"""
Averiguar si dos vectores son iguales y tienen el mismo contenido.
Si no es así, especifficar la primera posición en la cual se hicieorn diferentes.
"""

import sys
import pdb
def analized_vertor(list_1=[1,2,3,4,5,6,7,8,9],list_2=[1,2,3,4,5,6,7,8454,9]):
	if str(list_1) == str(list_2):
		print('las listas {} y {} son iguales '.format(list_1,list_2))
	else:
		for index, item_1 in enumerate(list_1):
			if item_1 != list_2[index]:
				print("Lista 1 {}".format(str(list_1)))
				print("Lista 2 {}".format(str(list_2)))
				print("Posi  i {}".format(str([x for x in range(len(list_1))])))
				print("la primera posición en la cual se hicieorn diferentes es {} ".format(index))



analized_vertor()




