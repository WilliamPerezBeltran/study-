class Pelota():

	def __init__(self):
		self.radio = 5
		self.peso = 1.2
		self.color = 'rojo'

	def mover(self):
		print('la pelota se esta moviendo')

	def revotar(self):
		print('la pelota esta revotando')


p = Pelota() #se crea la instancia p que hace referencia al objecto pelot
p2 = Pelota() #se crea la instancia p que hace referencia al objecto pelot
print p.radio
print p.peso
print p.color
p.mover()
p2.revotar()