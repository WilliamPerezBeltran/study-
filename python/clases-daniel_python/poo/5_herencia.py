class Padre(object):
	def __init__(self,nombre,apellido,cabello,ojos):
		self.nombre = nombre

	def ver_nombre(self):
		return f"el nombre del padre es {self.nombre}"

padre = Padre('Camilo','Quiroga','negro','verdes')
print(padre.ver_nombre())


class Hijo1(Padre):
	pass
class Hijo2(Padre):
	pass

class Hijo3(Padre):
	pass


instance_hijo1 = Hijo1('rodirgo','leal','rubio','negros')
instance_hijo2 = Hijo2('rocio','perez','castaño','negros')
instance_hijo3 = Hijo3('william','rodriguez','rubio','azules')
instance_hijo4 = Hijo1('daniel','vidal','rubio','cafes')
print(instance_hijo1.ver_nombre())
print(instance_hijo2.ver_nombre())
print(instance_hijo3.ver_nombre())
print(instance_hijo4.ver_nombre())