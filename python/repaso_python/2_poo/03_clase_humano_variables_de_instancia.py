class Humano():
	def __init__(self,nombre,edad,peso,estatura):
		self.nombre = nombre
		self.edad = edad
		self.peso = peso
		self.estatura = estatura

	def comer(self):
		print '%s esta comiendo '%(self.nombre)

	def dormir(self):
		print '%s esta durmiendo '%(self.nombre)

print ("""
	estas son las llamadas variables de instancia
	pasadas desde la instancia del objecto
""")
persona1 = Humano('william',35,85,1.80)
persona2 = Humano('oscar',32,88,1.70)
persona3 = Humano('william',20,45,1.20)


persona1.comer()
persona2.comer()
persona3.comer()

persona1.dormir()
persona2.dormir()
persona3.dormir()

