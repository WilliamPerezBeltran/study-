class Humano():
	def __init__(self):
		self.nombre = 'juan'
		self.edad = 35
		self.peso = 90
		self.estatura = 1.85

	def comer(self):
		print '%s esta comiendo'%(self.nombre)
 
persona = Humano()
print ("""
este ejercicio muestra las variables del constructor pero quemadas en el 
el otro ejercicio se mostrara las variables pasadas desde la misma instancia
""")
print 'Nombre: ', persona.nombre
print 'Edad: ', persona.edad
print 'Peso: ', persona.peso
print 'Estatura: ', persona.estatura
persona.comer()
