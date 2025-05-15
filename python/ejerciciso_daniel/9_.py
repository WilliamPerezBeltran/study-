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





#valor suministrado 4
#resultado: 1 4 4 9 9 9 16 16 16 16 16

  
"""
Método de ordenamiento burbuja
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

# lista = [44,42,56,86,52,17]
lista = [4,2,6,8,5,7]

print("array para ordenar = %s"%(str(lista)) )

def swap(mayor, menor):
	pivote = mayor
	lista[x] = menor
	lista[x+1] = pivote

for i in range(len(lista)): 
	for x in range(len(lista)-1):
		if lista[x] > lista[x+1]:
			swap(lista[x],lista[x+1])
			print(lista)



 
"""
Método de ordenamiento de burbuja 
revisa cada elemento de la lista con el siguiente elemento, 
intercambiandolos de posicion si esta en el orden equivocado
"""

# 4 2 6 8 5 7 
# 2 4 6 8 5 7 
# 2 4 6 8 5 7 
# 2 4 6 5 7 8
# 2 4 5 6 7 8 

***********************************************************
***********************************************************
***********************************************************
***********************************************************

#!/usr/bin/python -tt
# coding=utf-8

"""
Lilah has a string, s, of lowercase English letters that she repeated infinitely many times.

Given an integer,n , find and print the number of letter a's in the first n letters of Lilah's infinite string.

For example, if the string s='abcac' and n=10, the substring we consider is abcacabcac, the first 10  characters
 of her infinite string. There are 4 occurrences of a in the substring.

Function Description

Complete the repeatedString function in the editor below. It should return an integer representing the number of
 occurrences of a in the prefix of length n in the infinitely repeating string.

repeatedString has the following parameter(s):

s: a string to repeat
n: the number of characters to consider
Input Format

The first line contains a single string, .
The second line contains an integer, .


Sample Input 0

aba
10
Sample Output 0

7

explicacion:

aba aba aba a
se repitio el string  3 veces enteras y un a 
y el numero de a es : 7
"""

# s = string
# n = el numero de repeticiones que tiene que hacer el string


import sys
 

def repeated_string(s, n):
    l = len(s)
    numbers_of_repetition = n // l
    numbers_a_partes_enteras = s.count("a") * numbers_of_repetition
    rest = n - (l * numbers_of_repetition)
    return numbers_a_partes_enteras + s[:rest].count("a")


def test(got, expected):
    if got == expected:
        prefix = " OK "

    else:

        prefix = " X "

    print("%s got %s expected %s " % (prefix, repr(got), repr(expected)))


def main():
    test(repeated_string("aba", 10), 7)
    test(repeated_string("abcac", 10), 4)
    test(repeated_string("a", 1000000000000), 1000000000000)


if __name__ == "__main__":
    main()
