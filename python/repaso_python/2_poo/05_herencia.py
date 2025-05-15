#!/usr/bin/python -tt
# coding=utf-8



"""
herencia 
es cuando una clase nueva se crea a partir de una clase existente, herencado todos sus metodos 
y atributos . La clase principal se le denomona clase padre o clase principal , a las 
demas clases que heredan de la clase padre se le denomina clase hija o sub clase 

La herencia es uno de los mecanismos de los lenguajes de programación orientada a objetos
basados en clases, por medio del cual una clase se deriva de otra de manera que extiende
su funcionalidad.

"""

class Padre(object):
  	
	def __init__(self):
		self.nombre = 'william'
		self.color = 'green'
		self.hair = 'blonde'
	
	def colorEyes(self):
		return 'tiene color de ojos: %s'%(self.color)

	def giveName(self):
		return 'el nombre es: %s'%(self.nombre)

class Hijo1(Padre):
	pass

class Hijo2(Padre):
	pass

class Hijo3(Padre):
	pass


h1 = Hijo1()
h2 = Hijo1()
h3 = Hijo1()
print h1.nombre
print h2.colorEyes()
