class pelota():
	tipo = "canino"
	def __init__(self,name,age):
		self.name = name
		self.age = age
		self.mover_parametro = 23
	def mover(self):
		return print("se esta moviendo {}".format(self.mover_parametro))

	def estatico(self):
		return print("esta estatico")


p = pelota("william",89)
print(p.mover())
print(p.estatico())
print(p.name)
print(p.age)
print(p.tipo)