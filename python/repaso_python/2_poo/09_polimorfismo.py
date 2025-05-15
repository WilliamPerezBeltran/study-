#!/usr/bin/python -tt
# coding=utf-8

"""
son comportamientos diferentes asociados a objectos distintos, 
que pueden compartir el mismo nombre
"""

class Carro(object):
	def tipo(self):
		print "carro automatico"

class Moto(Carro):
	def tipo(self):
		print "moto manual"

class Bicicleta(Carro):
	def tipo(self):
		print "bicleta manuel con llanticas"

c = Carro()
m = Moto()
b = Bicicleta()

c.tipo()
m.tipo()
b.tipo()