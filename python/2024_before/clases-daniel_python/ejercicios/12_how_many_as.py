#!/usr/bin/python -tt
# coding=utf-8




""""

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
string = aba
numero = 10
respueta = 7 
------------------
string = accaca
numero = 15
contar= 'a'
respueta = 
accacaacaccacac
respuesta = 7


aba 
len(nuevo_string)=>10
abaabaaba a = a=>7
aba aba aba a

aba 10
aba 10
10/len('aba') = 3
len('aba')*3 = 9

10-9 = nos falta 1 para llegar a 10 unidades
n - (numero_dePartes_enteras*len(s))
1. contar cuantas as hay en el string que dan 
2. Contar cuantas partes enteras hay para llegar al número que nos piden (encontrar las as de las partes enteras )
3. Encontrar la cantidad faltante(encontrar las as de las partes faltantes ).
4. sumar ambas partes 
5. retornar el resultado
"""




def count_as(s,n):
	l =len(s)
	numero_de_repeticiones = n//l 
	numero_as_de_s = s.count('a')
	number_of_as_in_partes_enteras = numero_as_de_s*numero_de_repeticiones
	rest = n - numero_de_repeticiones*len(s)
	return number_of_as_in_partes_enteras + s[rest:].count('a')

def main():
	print(count_as('aabaab',15))

if __name__=='__main__':
	main()
