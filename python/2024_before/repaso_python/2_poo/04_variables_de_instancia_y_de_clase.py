#!/usr/bin/python -tt
# coding=utf-8

"""
En general las variables de instancia son para datos únicos de cada instancia 
y las variables de clase son para atributos y métodos compartidos por todas las 
instancias de la clase 

Todos las instancias comparten las variables de clase 
en cambio, las variables de instancia son unicas para cada instancia 
"""

class Perro():

	""" Variable de clase """	
	tipo = "canino"

	def __init__(self,nombre,raza):
		""" Variables de instancia """
		self.nombre = nombre
		self.raza = raza


perro1 = Perro('madona','pitbull')
perro2 = Perro('bork','pastor')
perro3 = Perro('maracondo','chiguagua')

print "mi nombre es %s, y mi raza es: %s"%(perro1.nombre, perro1.raza)
print "mi nombre es %s, y mi raza es: %s"%(perro2.nombre, perro2.raza)
print "mi nombre es %s, y mi raza es: %s"%(perro3.nombre, perro3.raza)

# se puede llamar sin crear una instancia
print Perro.tipo
print Perro.tipo
