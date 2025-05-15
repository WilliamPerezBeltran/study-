#!/usr/bin/python -tt
# coding=utf-8

class Animal(object):
	def __init__(self):
		self.patas = 4
		self.orejas = 2

class Mamifero(object):
	def __init__(self):
		self.tipo = "Mamifero"

class Perro(Animal,Mamifero):
	def __init__(self,nombre,edad):
		super(Perro,self).__init__()
		self.nombre = nombre
		self.edad = edad

	def getNombre(self):
		print self.nombre
	
	def getEdad(self):
		print self.edad

m = Perro('william',57)
m.getNombre()
m.getEdad()
print m.patas