#!/usr/bin/python -tt
# coding=utf-8

"""
lambdas:
Son funciones anonimas, estas funciones labdas siempre retornan un valor, pueden ser usadas en 
cualquier lugar donde sea requerido un onjecto de tipo función
"""

# las funciones lambda vienen almacenadas por variables
# y son funciones anonimas
# y no require de la palabra reservada return 

lam = lambda x: x+5
print lam(5) 

# esto es equivalente a esto:

def suma(x):
	return x+5


# pero tambien podemos enviarle mas parametros a la funcion anonima 
lam = lambda x,y,z: x+y+z
print lam(1,2,3)

"""
automaticamente regresa el valor que se le asigna 
y esto es similar a esot =>

"""

def suma(x,y,z):
	return x+5


