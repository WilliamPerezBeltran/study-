#!/usr/bin/python -tt
# coding=utf-8

"""
encapsulamiento:
se refiere a la delimitacion de nuestros métodos  (públicos y privados)
"""

"""
existen solamente dos tipos de variables en python publicas y privadas 
para definir varibles publicas es necesario utilizar la palabra reservada self
self.variable y se puede acceder tan solo sacando una instancia y llamando a la variable 

variables privadas se definen con dos guiones bajo es decir "__" osea 
self.__variable y para llamarlas es necesario utilizar los setters y los getters , 
los setter para definir la variable  y los getter para obtener la varible 
"""

class Persona():
	def __init__(self):
		self.__nombre = None
		self.__edad = None

	"""
	getters
	setters
	=> set , get
	"""
	def set_nombre(self,nombre):
		self.__nombre = nombre

	def get_nombre(self):
		if type(self.__nombre) == str:
			return self.__nombre
		else:
			print "tu dato no es un string "
	def set_edad(self,edad):
		self.__edad = edad

	def get_edad(self):
		return self.__edad

p = Persona()
p.set_nombre('william')
p.set_edad(12)

print "tu nombre es: ", p.get_nombre() 
print "tu edad es: ", p.get_edad()