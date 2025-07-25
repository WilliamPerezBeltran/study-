#!/usr/bin/python -tt
# coding=utf-8

"""
Given an array of integers, return indices of the two 
numbers such that they add up to a specific target.

You may assume that each input would have exactly 
one solution, and you may not use the same element twice.

dado un array de enteros, retornar los dos indices dentro de la lista
de modo que la posicion de ESTOS sumen el target dado 

such that = de modo que 
add up = suma  

"""

import sys 

def Twosum(list_numbers,target):
	for x in range(len(list_numbers)):
		for y in range(x+1,len(list_numbers)):
			if (list_numbers[x] + list_numbers[y]) == target:
				return [x,y]

def test(got,expected):
	if got == expected:
		prefix = ' OK '
	else:
		prefix = ' X '
	print '%s got %s expected %s '%(prefix,repr(got),repr(expected))
	
def main():
	args = sys.argv[1:]
	test(Twosum([2, 7, 11, 15],9),[0,1])
	test(Twosum([2, 3, 4, 5,6],11),[3,4])
	test(Twosum([2, 3, 4, 5,6,7,8,9,10,16,15],15),[3,8])
	

if __name__=='__main__':
	main()
