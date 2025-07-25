class carro():
	def __init__(self,color,deportivo,todo_terreno,velocidad,tamaño):
		self.color= color
		self.deportivo=deportivo
		self.todo_terreno=todo_terreno
		self.velocidad=velocidad
		self.tamaño=tamaño

	def corre(self):
		return (f"corriendo a una velocidad de {self.velocidad}")

	def frena(self):
		return (f"frenando de una velocidad de {self.velocidad}")

	def luces(self):
		return "encendiendo luces"

	def inflando(self):
		return "inflando llantas"

	def desinflando(self):
		return "desinflando llantas"


intancia_carro_1= carro("rojo","si","no",20,"mediano")
print(intancia_carro_1.color)
print(intancia_carro_1.deportivo)
print(intancia_carro_1.todo_terreno)
print(intancia_carro_1.velocidad)
print(intancia_carro_1.tamaño)

print(intancia_carro_1.corre())
print(intancia_carro_1.frena())
print(intancia_carro_1.luces())
print(intancia_carro_1.inflando())
print(intancia_carro_1.desinflando())

intancia_carro_2= carro("verde","no","si",40,"pequeño")
print(intancia_carro_2.color)
print(intancia_carro_2.deportivo)
print(intancia_carro_2.todo_terreno)
print(intancia_carro_2.velocidad)
print(intancia_carro_2.tamaño)

print(intancia_carro_2.corre())
print(intancia_carro_2.frena())
print(intancia_carro_2.luces())
print(intancia_carro_2.inflando())
print(intancia_carro_2.desinflando())