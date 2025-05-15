#!/usr/bin/python -tt
# coding=utf-8



"""
en /home/usuario/Escritorio/scraper/scraper/scraper/spiders/energy_linx.py
En la linea 49 del energy_linx hay un super
def init(self, **kwargs):
super(EnergyLinxSpider, self).init(**kwargs)
¿Para qué hay que declararse , cual es su función?

El super llama la función del padre. 
EnergyLinxSpider hereda de BaseSpider, entonces al llamar super desde el __init__ de 
EnergyLinxSpider llama el init de BaseSpider.
"""

class Clase1(object):
	def __init__(self):
		self.name1 = 'el atributo clase1 william'
		self.apellido1 = 'perez'

	def imprimirNombre1(self):
		return self.name1

	def imprimirApellido(self):
		return self.apellido1

class Clase2(object):
	def __init__(self):
		self.name2 = 'oscar'
		self.apellido2 = 'perez'

	def imprimirNombre2(self):
		return self.name2

	def imprimirApellido(self):
		return self.apellido2

class class3(Clase1,Clase2):

	def __init__(self):
		# llamando al super puede llamar a las otras clases
		super(class3,self).__init__() 
		self.name3 = 'el atributo name3'
		self.apellidp3 = 'el atributo apellido3'
	def imprimirNombre3(self):
		return self.name3

p = class3()

print p.name3
print p.name1
print p.imprimirNombre1()
print p.imprimirNombre3()
