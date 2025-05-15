# un objecto es lo mismo que una clase

class Humano():
	def __init__(self):
		self.nombre = 'juan'
		self.edad = 23
		self.peso =63
		self.estatura = 1.2 

	def correr(self):
		print("El humano esta corriendo ")

	def reir(self):
		print("el humano esta riendo")

copia_humano = Humano()
print(copia_humano.nombre)
print(copia_humano.edad)
print(copia_humano.peso)
copia_humano.correr()
copia_humano.reir()

