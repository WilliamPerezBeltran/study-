#!/usr/bin/python -tt
# coding=utf-8

print "---------------------------------------------------"
lista = [x for x in range(10)]
print lista

array = []
for x in range(10):
	array.append(x)
print array

print "como vemos las listas son iguales  ", array,lista
print "---------------------------------------------------"

lista1 = [x for x in range(10) if x<7] #con condicional 
print lista1


print "---------------------------------------------------"

lista2 = [x*x for x in range(10) if x<7] #con condicional 
print lista2


print "---------------------------------------------------"


string = ['dado','ajedrez','botella']
lista3 = [x+'_:) ' for x in string]
print lista3

print "---------------------------------------------------"

def elevado(x):
	return x*x
	
lista4 = [elevado(x) for x in range(12)]
print 'lista4'
print lista4

print "---------------------------------------------------"