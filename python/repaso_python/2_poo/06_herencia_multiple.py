#!/usr/bin/python -tt
# coding=utf-8


class Clase1(object):
	def __init__(self):
		self.atributo_clase_1 = "soy un atributo de la clase 1"

	def metodoClase1(self):
		print "soy un metodo de la clase 1"

class Clase2(object):
	def __init__(self):
		self.attributo_clase_2 = "soy un atributo de la clase 2"

	def metodoClase2(self):
		print "soy un metodo de la clase 2"

"""
herencia multiple
"""


# class SubClass(MyParentClass):
# def __init__(self):
# super(SubClass, self).__init__()

class Clase3(Clase1,Clase2):

	def __init__(self):
		super(Clase3, self).__init__()

		self.atributo_clase_3 = "soy un atributo de la clase 3"

	def metodoClase3(self):
		print "soy un metodo de la clase 3"


p = Clase3()
# print p.atributo_clase_1
p.metodoClase1()
p.metodoClase2()
p.metodoClase3()
print p.atributo_clase_1
print p.atributo_clase_3

