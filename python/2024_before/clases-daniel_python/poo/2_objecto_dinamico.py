class Humano:
	def __init__(self,nombre, edad, peso, estatura):
		self.nombre = nombre
		self.edad = edad
		self.peso = peso
		self.estatura = estatura

	def imprimir_atributos(self):
		return f"{self.nombre} - {self.edad} - {self.peso} - {self.estatura}" 

	def hablar(self):
		return " mi nombres {} ".format(self.nombre)

instancia_humano1 = Humano("william",23,43,80.4)
instancia_humano3 = Humano()

print(instancia_humano1.nombre)
print(instancia_humano1.edad)
print(instancia_humano1.peso)
print(instancia_humano1.estatura)
print(instancia_humano1.imprimir_atributos())
print(instancia_humano1.hablar())

print("*******************")

instancia_humano2 = Humano("oscar",123,403,890.4)
print(instancia_humano2.nombre)
print(instancia_humano2.edad)
print(instancia_humano2.peso)
print(instancia_humano2.estatura)
print(instancia_humano2.imprimir_atributos())
print(instancia_humano2.hablar())